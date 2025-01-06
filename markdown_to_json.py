import os
import json
import re
import markdown
from mrkdwn_analysis import MarkdownAnalyzer


def extract_api_links(markdown_text: str) -> str:
    """
    Given a string of Markdown content, convert it to HTML using `markdown`,
    then search for links containing the substring 'api.'.

    Returns:
        str or None: The first link found that contains 'api.', or None if none were found.
    """
    # Convert the Markdown text to HTML
    html = markdown.markdown(markdown_text)

    # Use a regex pattern to find the href values containing 'api'
    pattern = r'<a\s+href="([^"]*)".*?api'
    matches = re.findall(pattern, html)

    # Return the first match or None
    return matches[0].split("?")[0] if matches else None


# Mapping from file names to the headers we want to extract
headers_map = {
    "weather_forecast_api": [
        "API Documentation",
        "Hourly Parameter Definition",
        "15-Minutely Parameter Definition",
        "Daily Parameter Definition",
        "JSON Return Object",
        "Errors",
    ],
    "air_quality_api": [
        "API Documentation",
        "Hourly Parameter Definition",
        "JSON Return Object",
        "Errors",
    ],
    "climate_api": [
        "API Documentation",
        "Daily Parameter Definition",
        "JSON Return Object",
        "Errors",
    ],
    "elevation_api": ["API Documentation", "JSON Return Object", "Errors"],
    "ensemble_api": [
        "API Documentation",
        "Hourly Parameter Definition",
    ],
    "geocoding_api": ["API Documentation", "JSON Return Object", "Errors"],
    "global_flood_api": [
        "API Documentation",
        "Daily Parameter Definition",
        "JSON Return Object",
        "Errors",
    ],
    "historical_weather_api": [
        "API Documentation",
        "Hourly Parameter Definition",
        "Daily Parameter Definition",
        "JSON Return Object",
        "Errors",
    ],
    "marine_weather_api": [
        "API Documentation",
        "Hourly Parameter Definition",
        "Daily Parameter Definition",
        "JSON Return Object",
        "Errors",
    ],
}


def process_file(file_name: str) -> None:
    """
    Process a single file by:
      1. Reading the Markdown content from docs/<file_name>.md.
      2. Identifying the specified headers as given by the global `headers_map`.
      3. Extracting the text blocks from each required header until the next header.
      4. Finding the first 'api.' link in the text.
      5. Writing the extracted data to json/<file_name>.json.
    """
    md_path = os.path.join("docs", f"{file_name}.md")

    if not os.path.exists(md_path):
        print(f"❗ File not found: {md_path}. Skipping...")
        return

    print(f"🔎 Analyzing: {md_path}")
    doc = MarkdownAnalyzer(md_path)

    # Identify all headers in the document
    all_headers = doc.identify_headers().get("Header", [])
    if not all_headers:
        print(f"❗ No headers found in {md_path}. Skipping...")
        return

    # We want only the lines of text from the Markdown
    data_lines = doc.text.splitlines()

    # The list of required headers for this file
    required_headers = headers_map[file_name]
    content_meta = []

    # For each required header, collect the lines from this header
    # up to the next header (or the end of file)
    for header in required_headers:
        matches = [(h, idx) for idx, h in enumerate(all_headers) if h["text"] == header]
        if not matches:
            print(f"❗ Header '{header}' not found in {md_path}.")
            continue  # Skip this header if not found

        target, target_index = matches[0]  # We only take the first match if multiple
        try:
            end_target = all_headers[target_index + 1]  # The next header in the list
        except IndexError:
            # If there's no next header, pick an arbitrary line number near the end
            end_target = {"line": len(data_lines)}

        # Extract the chunk of text from this header to the next header
        header_data = "\n".join(data_lines[target["line"] : end_target["line"]])

        content_meta.append(
            {
                "header": header,
                "data": header_data,
            }
        )

    # Lastly, add the first 'api.' link found in the entire doc
    api_endpoint = extract_api_links(doc.text)
    content_meta.append({"api-endpoint": api_endpoint})

    # Write to JSON
    os.makedirs("json", exist_ok=True)
    output_path = os.path.join("json", f"{file_name}.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(content_meta, f, indent=2)

    print(f"✅ Finished: {output_path}\n")


def main():
    """
    Main driver function:
      1. Iterates over each file name in headers_map.
      2. Processes each file to extract the relevant Markdown headers and API links.
    """
    print("🚀 Starting the JSON extraction process...\n")

    # Process each file in headers_map
    for file_key in headers_map.keys():
        process_file(file_key)

    print("🏁 Extraction process complete. All JSON files stored in 'json/' directory.")


if __name__ == "__main__":
    main()
