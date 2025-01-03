import ollama


def document_dump_prompt(doc, question, helper):
    prompt = """
<document> 
    {}
</document> 
Provided above, is a document
the following is some helper context info, which provides the API endpoint for the document and target the location provided in the question
<helper-context>
    {}
</helper-context>

Question: {}
    """.format(
        doc, helper, question
    )
    return prompt


import frontmatter

doc = frontmatter.load("./docs/weather_forecast_api.md")


helper = """
<api-metadata>
 {}
</api-metadata>
<latitude-longitude>
{}
<latitude-longitude>
""".format(
    doc.metadata.items(), [-12.460989949999941, 130.84231457600004]
)

question = "would it rain in Darwin today?"

system = """
You are not an AI assistant, you are a API endpoint generator,
You are supposed to look at the document's API parameters, and 
respond to user's question, by generating a REST API endpoint, that satisfies
user's question
"""


res = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "system", "content": system},
        {
            "role": "user",
            "content": document_dump_prompt(doc.content, question, helper),
        },
    ],
    options={"temperature": 0.2, "num_ctx": 8192},
)

print(res["message"]["content"])
