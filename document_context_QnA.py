import ollama
import yaml

yml = yaml.safe_load(open("temp.yaml"))


def document_dump_prompt(doc, question, helper):
    prompt = """
<document> 
    {}
</document> 
Provided above, is a document
the following is some helper context info,
which provides the API endpoint for the document and target the location provided in the question
<helper-context>
    {}
</helper-context>

Question: {}
    """.format(
        doc, helper, question
    )
    return prompt


import frontmatter


helper = """
<api-info>
 {}
</api-info>
<latitude-longitude>
{}
<latitude-longitude>
""".format(
    "https://api.open-meteo.com/v1/forecast", [-12.46, 130.84]
)

question = "is it raining right now?"

system = """
You are not an AI assistant, you are a API endpoint generator,
You are supposed to look at the document's API parameters, and 
respond to user's question, by generating a REST API endpoint, that satisfies
user's question
NOTE: unless the parameters are specified in the query URL
their return values are not considered to generate a response,
so include the parameters responsible according to the question
"""


res = ollama.chat(
    model="marco-o1",
    messages=[
        # {"role": "system", "content": system},
        {
            "role": "user",
            # "content": document_dump_prompt(yml, question, helper),
            "content": """
Assess this response:
{"latitude":-12.5,"longitude":130.875,"generationtime_ms":0.015974044799804688,"utc_offset_seconds":0,"timezone":"GMT","timezone_abbreviation":"GMT","elevation":27.0,"current_units":{"time":"iso8601","interval":"seconds","precipitation":"mm"},"current":{"time":"2025-01-06T11:15","interval":900,"precipitation":0.00}}
for the query response, and answer my question: is it raining right now?
""",
        },
    ],
    options={"temperature": 0.1, "num_ctx": 16384},
)

print(res["message"]["content"])
import json

print(json.dumps(res.model_dump(), indent=2))
