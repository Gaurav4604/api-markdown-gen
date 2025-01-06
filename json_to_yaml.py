import ollama


client = ollama.Client()

system = """
You are NOT an AI assistant,
You are a smart JSON to YAML converter,
your role is to look at the YAML file format,
and a corresponding JSON file,
from which this YAML file was derived,
and use it to convert every future JSON file I provide
The JSON file will contain key value pairs,
and the values contain markdown syntax
"""


yaml_template = """
This is the reference YAML file:
{}
"""

json_template = """
This is the reference JSON file:
{}
"""

json_convert_template = """
convert this JSON file to YAML:
{}
"""

yaml = open("yml/weather_forecast_api.yml", "r", encoding="utf-8").read()
json = open("json/weather_forecast_api.json", "r", encoding="utf-8").read()

json_convert = open("json/climate_api.json", "r", encoding="utf-8").read()


res = client.chat(
    model="gemma2",
    messages=[
        {"role": "system", "content": system},
        {"role": "user", "content": yaml_template.format(yaml)},
        {"role": "user", "content": json_template.format(json)},
        {"role": "user", "content": json_convert_template.format(json_convert)},
    ],
    options={"num_ctx": 4096},
)

print(res["message"]["content"])
