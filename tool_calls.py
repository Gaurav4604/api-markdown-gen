from typing import Any
import ollama
from pydantic import BaseModel
import yaml
import os
import geocoder
from datetime import datetime
from timezonefinder import TimezoneFinder
import utils
import requests
import json


class TimeZone(BaseModel):
    timezone: str


class Doc(BaseModel):
    file: str
    selection_reason: str
    question_for_doc: str


class DocList(BaseModel):
    files: list[Doc]


class Query(BaseModel):
    api_with_params: str


class Response(BaseModel):
    response: str
    file: str
    question_for_doc: str
    query: str


directory = "yml"


def list_files(directory):
    try:
        files = [
            f
            for f in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, f))
        ]
        return list(map(lambda x: directory + "/" + x, files))
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


files = list_files(directory)

yml_files = list(
    map(lambda path: yaml.safe_load(open(path, "r", encoding="utf-8")), files)
)


def get_today_date() -> datetime:
    """
    Gets today's date time data

    Returns:
        datetime
    """
    return datetime.now()


def get_lat_long(location: str) -> list[int]:
    """
    Gets the Latitude and Longitude for the provided location

    Args:
        location (str): The location for which latitude and longitude is requested
    Returns:
        list[int]: a list containing 2 elements, in order latitude and longitude associated to the location
    """
    return list(map(lambda x: round(x, 2), geocoder.arcgis(location).latlng))


timezone_system_prompt = """
You are a timezone detector, your role is to choose
and return a timezone from list of target timezones provided, 
that is the closest to the user's provided timezone
"""


def get_timezone(latlng: list[int]) -> str:
    """
    Gets the timezone associated with the latitude and longitude, compatible with API calls
    Args:
        latlng (list[int]): An array with 2 elements, in order of latitude and longitude
    Returns:
        str: timezone closest to the latitude and longitude provided, which works with the API
    """
    targets = [
        "America%2FAnchorage",
        "America%2FLos_Angeles",
        "America%2FDenver",
        "America%2FChicago",
        "America%2FNew_York",
        "America%2FSao_Paulo",
        "GMT",
        "Europe%2FLondon",
        "Europe%2FBerlin",
        "Europe%2FMoscow",
        "Africa%2FCairo",
        "Asia%2FBangkok",
        "Asia%2FSingapore",
        "Asia%2FTokyo",
        "Australia%2FSydney",
        "Pacific%2FAuckland",
    ]
    tf = TimezoneFinder()
    tz = tf.timezone_at(lat=latlng[0], lng=latlng[1])
    res = ollama.chat(
        model="gemma2",
        messages=[
            {"role": "system", "content": timezone_system_prompt},
            {
                "role": "user",
                "content": """
                your role is to choose
                and return a timezone from list of target timezones provided, 
                that is the closest to my current timezone

                these are the target timezones {}, this is my current timezone {}""".format(
                    targets, tz
                ),
            },
        ],
        options={
            "temperature": 0.1,
            "low_vram": True,
            "num_ctx": 1024,
        },
        format=TimeZone.model_json_schema(),
    )
    # return res["message"]["content"]
    return TimeZone.model_validate_json(res["message"]["content"]).timezone


doc_selection_reasoning_system = """
You are a query simplification tool,
You will be provided a weather based natural language query along with a list of documents that might contain meta-data associated with the query,

Your role is to decompose the query into simpler sub-queries, that can be associated with document list,
The targetted documents need to be aggregated from all documents,
You need to link the aggregated documents, with generated sub-queries, and provide reasoning for choosing these documents,
in the reasoning, you need to formulate a "question" that you can pitch, to each document selected during the sub-query

the MAXIMUM number of selections should be 2
and use most critical conditions that would correlate to the query
"""


def doc_selection_reasoning_dump(doc: Any, query: str):
    prompt = """
<documents> 
    {}
</documents> 

<helper-context>
Provided above, is a list of documents containing tags and description associated to the API call they're responsible for
NOTE: unless extremely essential, do not include historical_weather_api.md file in the final conclusion
</helper-context>

<user-query>
{}
</user-query>
    """.format(
        doc, query
    )
    return prompt


def generate_target_docs_for_query(user_query: str) -> list[Doc]:
    """
    Extracts out weather api documents and their parameters
    to be used to generate API calls, that are targetted to respond to user's query

    Args:
        user_query (str): the raw query, user has asked to the model
    Returns:
      list[Doc]: A list of documents, containing file name, the reason for their selection, sub-query they target
    """
    files_meta = list(map(lambda yml: yml["meta"], yml_files))

    res = ollama.chat(
        model="marco-o1",
        messages=[
            {"role": "user", "content": doc_selection_reasoning_system},
            {
                "role": "user",
                "content": doc_selection_reasoning_dump(files_meta, user_query),
            },
        ],
        format=DocList.model_json_schema(),
        options={
            "temperature": 0.1,
            "num_ctx": 8192,
            "low_vram": True,
            "num_threads": 16,
        },
    )
    return DocList.model_validate_json(res["message"]["content"]).files


query_generation_system = """
You are not an AI assistant, you are a API endpoint generator,
You are supposed to look at the document's API parameters, and 
respond to user's question, by generating a REST API endpoint, that satisfies
user's question
NOTE: unless the parameters are specified in the query URL
their return values are not considered to generate a response,
so include the parameters responsible according to the question
"""


def query_generation_prompt(
    doc: str,
    api_endpoint: str,
    latlng: list[int],
    current_datetime: datetime,
    timezone: str,
    question: str,
) -> str:
    prompt = """
<document> 
    {}
</document> 
Provided above, is a document containing parameters accepted by the API endpoint for a "REST API - GET call",
the following is some helper context info,
which provides the API endpoint for the document and target the location provided in the question
<helper-context>
    <api-info>
        {}
    </api-info>
    <latitude-longitude>
        {}
    <latitude-longitude>
    <date-time>
        today's date: {}
        current time: {}
    </date-time>
    <timezone>
        {}
    </timezone>
</helper-context>

Question: {}
    """.format(
        doc,
        api_endpoint,
        latlng,
        current_datetime.strftime("%Y-%m-%d"),
        current_datetime.strftime("%H:%M:%S"),
        timezone,
        question,
    )
    return prompt


def generate_and_execute_api_calls(
    selected_docs: list[Doc],
    latlng: list[int],
    current_datetime: datetime,
    timezone: str,
) -> list[Response]:
    """
    Creates API queries associated with the docs provided
    And Executes Them
    Args:
        selected_docs (list[Doc]): list of documents for which the API calls need to be generated
        latlng (list[int]): a list containing 2 elements, in order latitude and longitude associated to the location
        current_datetime (datetime): datetime information of the location
        timezone: the timezone in which the location exists
    Returns:
      list[Response]: A list of Response objects, with each object containing a Response generated for the Question associated to it
    """
    queries: list[Response] = []
    for doc in selected_docs:
        target = list(filter(lambda x: doc.file in x["meta"]["filename"], yml_files))[0]
        res = ollama.chat(
            model="gemma2",
            messages=[
                {"role": "system", "content": query_generation_system},
                {
                    "role": "user",
                    "content": query_generation_prompt(
                        target["parameters"],
                        target["api-endpoint"],
                        latlng,
                        current_datetime,
                        timezone,
                        doc.question_for_doc,
                    ),
                },
            ],
            format=Query.model_json_schema(),
            options={
                "temperature": 0.1,
                "num_ctx": 16384,
                "low_vram": True,
                "num_threads": 16,
            },
        )

        query = Query.model_validate_json(res["message"]["content"]).api_with_params

        query = utils.fix_date_time_value(query)
        query = utils.fix_start_date_incompletion(query)
        query = utils.fix_forecast_day_inconsistency(query)

        api_response = requests.get(query)

        if api_response.status_code == 200:
            res = json.dumps(api_response.json(), indent=2)
            queries.append(
                Response(
                    response=res,
                    file=doc.file,
                    question_for_doc=doc.question_for_doc,
                    query=query,
                )
            )
        else:
            queries.append(
                Response(
                    response="",
                    file=doc.file,
                    question_for_doc=doc.question_for_doc,
                    query=query,
                )
            )

    return queries


functions = {
    "generate_target_docs_for_query": generate_target_docs_for_query,
    "generate_and_execute_api_calls": generate_and_execute_api_calls,
}

q1 = "in the next seven days, when would be a good time to swim, in the ocean, in Adelaide?"
q2 = "will tomorrow afternoon be a nice time to swim in the ocean in Adelaide?"
q3 = "should I wear a hat tomorrow?"
q4 = "is it gonna be sweater weather soon?"

q_used = q4

messages = [
    {
        "role": "user",
        "content": q_used,
    }
]

latlng = get_lat_long("Adelaide")
print("Lat Long data: ", latlng)
date_data = get_today_date()
print("Date data: ", date_data)

tz = get_timezone(latlng)
print("Timezone data: ", tz)

docs = generate_target_docs_for_query(q_used)
print("Selected Docs: ", docs)
api_queries = generate_and_execute_api_calls(docs, latlng, date_data, tz)
print("Generated API Responses: ", api_queries)

res = ollama.chat(
    model="marco-o1",
    messages=[
        {
            "role": "user",
            "content": """
    Based on the Responses: {}
    Answer the initial Question: {}
    while pointing to response data you've taken as factors for the result""".format(
                api_queries, q_used
            ),
        },
    ],
    options={"temperature": 0.1, "num_ctx": 8192},
)

print(res["message"]["content"])


# system_main = """
# You're a tool and payload generator, that works with a pipeline
# of tools to generate a response for user's query, by constructing weather related API calls,
# related to user's query location, along with realtime date and geographical data
# """

# response = ollama.chat(
#     "llama3.2",
#     messages=messages,
#     tools=[
#         get_today_date,
#         get_lat_long,
#         generate_target_docs_for_query,
#         generate_api_calls,
#     ],
#     options={"temperature": 0.1},
# )

# print(response.model_dump_json(indent=2))

# if response.message.tool_calls:
#     # There may be multiple tool calls in the response
#     for tool in response.message.tool_calls:
#         # Ensure the function is available, and then call it
#         if function_to_call := functions.get(tool.function.name):
#             print("Calling function:", tool.function.name)
#             print("Arguments:", tool.function.arguments)
#             output = function_to_call(**tool.function.arguments)
#             print("Function output:", output)
#         else:
#             print("Function", tool.function.name, "not found")

# # Only needed to chat with the model using the tool call results
# if response.message.tool_calls:
#     # Add the function response to messages for the model to use
#     messages.append(response.message)
#     messages.append(
#         {"role": "tool", "content": str(output), "name": tool.function.name}
#     )

#     # Get final response from model with function outputs
#     final_response = ollama.chat("llama3.2", messages=messages)
#     print("Final response:", final_response.message.content)

# else:
#     print("No tool calls returned from model")
