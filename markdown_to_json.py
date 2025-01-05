import json
from mrkdwn_analysis import MarkdownAnalyzer

doc = MarkdownAnalyzer("temp.md")

headers = doc.identify_headers().get("Header")

required_headers = [
    "API Documentation",
    "Hourly Parameter Definition",
    "15-Minutely Parameter Definition",
    "Daily Parameter Definition",
    "JSON Return Object",
    "Errors",
]


content_meta = []

data = doc.text.splitlines()

for index, header in enumerate(required_headers):
    target, target_index = [
        (x, idx) for idx, x in enumerate(headers) if x["text"] == header
    ][0]
    endTarget = headers[target_index + 1]

    content_meta.append(
        {
            "header": header,
            "data": "\n".join(data[target["line"] : endTarget["line"]]),
        }
    )

with open("template.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(content_meta))
    f.close()
