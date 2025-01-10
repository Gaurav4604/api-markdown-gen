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


class QuestionGeoMeta(BaseModel):
    location: str
    latlng: list[float]
    timezone: str


class Location(BaseModel):
    location: str
    location_found: bool


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


class Conclusion(BaseModel):
    answer: str
    reasoning: str


directory = "yml"


def list_files(directory):
    # ⏲️ Start time stamp
    start_time = datetime.now()
    print(f"📂 [list_files] Started at {start_time} ...")

    try:
        files = [
            f
            for f in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, f))
        ]
        return list(map(lambda x: directory + "/" + x, files))
    except FileNotFoundError:
        print(f"❗ [list_files] Directory '{directory}' not found.")
        return []
    except Exception as e:
        print(f"❗ [list_files] An error occurred: {e}")
        return []
    finally:
        end_time = datetime.now()
        print(
            f"✅ [list_files] Finished at {end_time} (Execution time: {end_time - start_time})"
        )


files = list_files(directory)

yml_files = list(
    map(lambda path: yaml.safe_load(open(path, "r", encoding="utf-8")), files)
)


def get_location_from_question(question: str) -> Location:
    """
    Extracts location information from the question

    Args:
        question (str): the question for which location needs to be extracted
    Returns:
        Location: the location value, and if it was found in the question
    """
    print(
        f"🕵️ [get_location_from_question] Extracting location from question: '{question}'"
    )

    res = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": "{} <- does this question contain location information? if so what is it?".format(
                    question
                ),
            }
        ],
        format=Location.model_json_schema(),
        options={"num_ctx": 512, "temperature": 0.1},
    )

    location = Location.model_validate_json(res["message"]["content"])
    print(
        f"📍 [get_location_from_question] Location extracted: {location.model_dump_json()}"
    )

    return location


def get_lat_long(location: str) -> list[float]:
    """
    Gets the Latitude and Longitude for the provided location

    Args:
        location (str): The location for which latitude and longitude is requested
    Returns:
        list[float]: a list containing 2 elements, in order latitude and longitude associated to the location
    """
    # ⏲️ Start time stamp
    start_time = datetime.now()
    print(f"🕵️ [get_lat_long] Started at {start_time}, location='{location}' ...")

    result = list(map(lambda x: round(x, 2), geocoder.arcgis(location).latlng))

    end_time = datetime.now()
    print(
        f"✅ [get_lat_long] Finished at {end_time} (Execution time: {end_time - start_time})"
    )
    return result


timezone_system_prompt = """
You are a timezone detector, your role is to choose
and return a timezone from list of target timezones provided, 
that is the closest to the user's provided timezone
"""


def get_timezone(latlng: list[float]) -> str:
    """
    Gets the timezone associated with the latitude and longitude, compatible with API calls
    Args:
        latlng (list[float]): An array with 2 elements, in order of latitude and longitude
    Returns:
        str: timezone closest to the latitude and longitude provided, which works with the API
    """
    # ⏲️ Start time stamp
    start_time = datetime.now()
    print(f"🌎 [get_timezone] Started at {start_time}, latlng={latlng} ...")

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
    chosen_tz = TimeZone.model_validate_json(res["message"]["content"]).timezone

    end_time = datetime.now()
    print(
        f"✅ [get_timezone] Finished at {end_time} (Execution time: {end_time - start_time})"
    )
    return chosen_tz


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


def doc_selection_reasoning_dump(doc: Any, location: str, query: str):
    # ⏲️ Start time stamp
    start_time = datetime.now()
    print(f"📝 [doc_selection_reasoning_dump] Started at {start_time} ...")

    prompt = """
<documents> 
    {}
</documents> 

<helper-context>
    <location>
        {}
    </location>
Provided above, is a list of documents containing tags and description associated to the API call they're responsible for
NOTE: unless extremely essential, do not include historical_weather_api.md file in the final conclusion
</helper-context>

<user-query>
{}
</user-query>
    """.format(
        doc, location, query
    )

    end_time = datetime.now()
    print(
        f"✅ [doc_selection_reasoning_dump] Finished at {end_time} (Execution time: {end_time - start_time})"
    )
    return prompt


def generate_target_docs_for_query(user_query: str, location: str) -> list[Doc]:
    """
    Extracts out weather api documents and their parameters
    to be used to generate API calls, that are targetted to respond to user's query

    Args:
        user_query (str): the raw query, user has asked to the model
    Returns:
      list[Doc]: A list of documents, containing file name, the reason for their selection, sub-query they target
    """
    # ⏲️ Start time stamp
    start_time = datetime.now()
    print(
        f"🗂️ [generate_target_docs_for_query] Started at {start_time}, user_query='{user_query}' ..."
    )

    files_meta = list(map(lambda yml: yml["meta"], yml_files))

    res = ollama.chat(
        model="marco-o1",
        messages=[
            {"role": "user", "content": doc_selection_reasoning_system},
            {
                "role": "user",
                "content": doc_selection_reasoning_dump(
                    files_meta, location, user_query
                ),
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
    doc_list = DocList.model_validate_json(res["message"]["content"]).files

    end_time = datetime.now()
    print(
        f"✅ [generate_target_docs_for_query] Finished at {end_time} (Execution time: {end_time - start_time})"
    )
    return doc_list


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
    latlng: list[float],
    timezone: str,
    question: str,
) -> str:
    # ⏲️ Start time stamp
    start_time = datetime.now()
    print(f"🔧 [query_generation_prompt] Started at {start_time} ...")

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
        datetime.now().strftime("%Y-%m-%d"),
        datetime.now().strftime("%H:%M:%S"),
        timezone,
        question,
    )

    end_time = datetime.now()
    print(
        f"✅ [query_generation_prompt] Finished at {end_time} (Execution time: {end_time - start_time})"
    )
    return prompt


def generate_and_execute_api_calls(
    selected_docs: list[Doc],
    latlng: list[float],
    timezone: str,
) -> list[Response]:
    """
    Creates API queries associated with the docs provided
    And Executes Them
    Args:
        selected_docs (list[Doc]): list of documents for which the API calls need to be generated
        latlng (list[float]): a list containing 2 elements, in order latitude and longitude associated to the location
        timezone: the timezone in which the location exists
    Returns:
      list[Response]: A list of Response objects, with each object containing a Response generated for the Question associated to it
    """
    # ⏲️ Start time stamp
    start_time = datetime.now()
    print(f"🤖 [generate_and_execute_api_calls] Started at {start_time} ...")

    queries: list[Response] = []
    for doc in selected_docs:
        # Log each doc as we iterate
        print(f"🔍 [generate_and_execute_api_calls] Processing doc: {doc.file} ...")

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

        print(f"🌐 [generate_and_execute_api_calls] Sending request: {query}")
        api_response = requests.get(query)

        if api_response.status_code == 200:
            res_text = json.dumps(api_response.json(), indent=2)
            queries.append(
                Response(
                    response=res_text,
                    file=doc.file,
                    question_for_doc=doc.question_for_doc,
                    query=query,
                )
            )
            print(f"✅ [generate_and_execute_api_calls] Request succeeded: {doc.file}")
        else:
            queries.append(
                Response(
                    response="",
                    file=doc.file,
                    question_for_doc=doc.question_for_doc,
                    query=query,
                )
            )
            print(f"❌ [generate_and_execute_api_calls] Request failed for: {doc.file}")

    end_time = datetime.now()
    print(
        f"✅ [generate_and_execute_api_calls] Finished at {end_time} (Execution time: {end_time - start_time})"
    )
    return queries


conclusion_template = """
    You are to provide weather data based conclusion to the provided question,
    after understanding the data responses, for each of the sub-questions asked
    while pointing to response data you've taken as factors for the conclusion as points

    Responses: {}
    Answer the initial Question: {}
"""


def infer_conclusion(queries: list[Response], question: str) -> Conclusion:
    """
    Generates a concluding statement based on the weather data responses
    and the original question asked.

    Args:
        queries (list[Response]): A list of Response objects which contain
            the data returned by the API calls for sub-questions.
        question (str): The original question provided by the user.

    Returns:
        Conclusion: the final conclusion summarizing the weather data in the context of the original question.
    """
    # ⏲️ Start time stamp
    start_time = datetime.now()
    print(f"📜 [infer_conclusion] Started at {start_time}, question='{question}' ...")

    # Build the prompt using the conclusion_template
    prompt_content = conclusion_template.format(queries, question)

    # Call the ollama.chat model to generate the conclusion
    res = ollama.chat(
        model="marco-o1",
        messages=[
            {
                "role": "user",
                "content": prompt_content,
            },
        ],
        options={"temperature": 0.1, "num_ctx": 8192},
        format=Conclusion.model_json_schema(),
    )

    conclusion = Conclusion.model_validate_json(res["message"]["content"])

    end_time = datetime.now()
    print(
        f"✅ [infer_conclusion] Finished at {end_time} (Execution time: {end_time - start_time})"
    )

    return conclusion


def get_question_meta_data(
    question: str, default_location="Adelaide"
) -> QuestionGeoMeta:
    """

    Extracts out geographical meta-data associated to the question,
    such as location, latitude-longitude, timezone and date-time

    Args:
        question (str): the question for which geographical meta-data needs to be extracted
        default_location (str): an optional location parameter passed, which is used in case the question doesn't contain location information

    Returns:
        QuestionGeoMeta: metadata containing location, latlng, timezone
    """

    location = get_location_from_question(question)
    if not location.location_found:
        location.location = default_location

    start_time = datetime.now()
    print(
        "🔎 Starting meta_data pipeline for location '{}'...\n".format(
            location.location
        )
    )
    print(f"📜 [meta_data] Started at {start_time}' ...\n")

    latlng = get_lat_long(location.location)
    print(f"📍 Retrieved lat/long for '{location.location}': {latlng}")

    # Determine Timezone
    tz = get_timezone(latlng)
    print(f"🌏 Derived timezone for coordinates {latlng}: {tz}")
    end_time = datetime.now()
    print(
        f"✅ [meta_data] Finished at {end_time} (Execution time: {end_time - start_time})\n"
    )
    return QuestionGeoMeta(location=location.location, latlng=latlng, timezone=tz)


tool_list = [
    get_question_meta_data,
    generate_target_docs_for_query,
    generate_and_execute_api_calls,
    infer_conclusion,
]

functions = {
    "get_question_meta_data": get_question_meta_data,
    "generate_target_docs_for_query": generate_target_docs_for_query,
    "generate_and_execute_api_calls": generate_and_execute_api_calls,
    "infer_conclusion": infer_conclusion,
}
