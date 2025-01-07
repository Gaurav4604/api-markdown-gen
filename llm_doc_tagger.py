import ollama
import yaml
import os
import json
from pydantic import BaseModel


# Define the schema for the response
class DocMeta(BaseModel):
    tags: list[str]
    description: str
    filename: str


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


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


def document_dump_prompt(doc):
    prompt = """
<document> 
    {}
</document> 

<helper-context>
Provided above, is a document containing parameters for an API call
Your role is to extract out tags associated to this document along with a 2 line description about the document
</helper-context>

<example>
tag: climate-change
</example>
    """.format(
        doc
    )
    return prompt


system = """
You are an advanced context based tag generator,
you're supposed to look at the document provided and generate tags for it,
all documents provided to you will contain weather, climate, elevation or sea related information
generate extremely targetted tags that capture the essence of the document.
NOTE: each document is from open-meteo, and requires latitude-longitude information, so avoid generating
information for these 2 parameters
"""


for path in files:
    res = ollama.chat(
        model="marco-o1",
        messages=[
            {"role": "system", "content": system},
            {
                "role": "user",
                "content": document_dump_prompt(
                    yaml.safe_load(open(path, "r", encoding="utf-8"))["parameters"]
                ),
            },
            {
                "role": "user",
                "content": "following is the file path, for the above document: {}".format(
                    path
                ),
            },
        ],
        format=DocMeta.model_json_schema(),
        options={"temperature": 0, "num_ctx": 16384},
    )

    doc = DocMeta.model_validate_json(res["message"]["content"])
    yml = None
    with open(path, "r", encoding="utf-8") as f:
        yml = yaml.safe_load(f)
        yml["meta"] = json.loads(doc.model_dump_json())
        yml = yaml.dump(
            yml,
            Dumper=NoAliasDumper,
            sort_keys=False,
            default_flow_style=False,
            allow_unicode=True,
            indent=2,
        )
        f.close()
    with open(path, "w", encoding="utf-8") as f:
        f.write(yml)
        f.close()
