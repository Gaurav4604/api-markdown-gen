import os
from markitdown import MarkItDown
from mrkdwn_analysis import MarkdownAnalyzer


def markdown_extract(url: str) -> None:
    """
    Converts the webpage at `url` to Markdown, analyzes its headers,
    and saves the resulting markdown file into the `docs/` directory.

    Steps:
      1. Fetch webpage content as Markdown (using MarkItDown).
      2. Save it temporarily as 'temp.md'.
      3. Use MarkdownAnalyzer to find headers.
      4. Generate a final filename from the first H1 header text.
      5. Save final file in 'docs/'.
      6. Remove 'temp.md'.
    """
    print(f"⚙️  Extracting Markdown from: {url}")

    # 1. Fetch webpage content as Markdown
    md = MarkItDown()
    result = md.convert_url(url)

    # 2. Write to a temporary markdown file
    with open("temp.md", "w", encoding="utf-8") as f:
        f.write(result.text_content)

    # 3. Analyze the temporary file for headers
    doc = MarkdownAnalyzer("temp.md")
    headers = doc.identify_headers().get("Header")

    # Check if we found any headers
    if not headers:
        print(f"❗ No headers found on {url}, skipping...")
        os.remove("temp.md")
        return

    # Grab the first level-1 header
    h1_headers = list(filter(lambda x: x["level"] == 1, headers))
    if not h1_headers:
        print(f"❗ No H1 headers found on {url}, skipping...")
        os.remove("temp.md")
        return

    first_header = h1_headers[0]
    header_text = first_header["text"]

    # 4. Build the final filename from the H1 header
    file_slug = "_".join(header_text.lower().split(" ")) + ".md"
    output_path = os.path.join("docs", file_slug)

    # 5. Write the final markdown file to 'docs/'
    os.makedirs("docs", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result.text_content)

    # 6. Remove the temporary file
    os.remove("temp.md")

    print(f"✅ Saved: {output_path}\n")


def main():
    """
    Main execution flow:
      1. Convert the root /en/docs page to Markdown and save as temp.md.
      2. Extract the relevant list items from the doc.
      3. Build a list of links (append '/en/docs' as well).
      4. For each link, run `markdown_extract`.
    """
    print("🚀 Starting the docs extraction process...")

    root = "https://open-meteo.com"
    md = MarkItDown()

    # 1. Convert the main /en/docs page to markdown
    print(f"⚙️  Fetching main docs page: {root + '/en/docs'}")
    result = md.convert_url(root + "/en/docs")
    with open("temp.md", "w", encoding="utf-8") as f:
        f.write(result.text_content)

    # 2. Analyze the temporary file for unordered lists
    doc = MarkdownAnalyzer("temp.md")
    lists = doc.identify_lists().get("Unordered list", [])

    # In your original code, we pick the second element [1],
    # then slice from [15:]. Adjust or confirm what your data looks like.
    # For demonstration, we'll keep it as is but you might
    # want to refine this indexing based on real data.
    if len(lists) > 1:
        texts = lists[1][15:]
    else:
        texts = []

    # 3. Build links by parsing out the text, which is assumed to be in (URL) format
    print(f"🔗 Building links from identified lists...")
    links = [
        root + t["text"].split("(")[1].replace(")", "")
        for t in texts
        if "(" in t["text"] and ")" in t["text"]
    ]

    # Add the main docs page to the list of links
    links.append(root + "/en/docs")

    # Remove the temp file used for the main docs page
    os.remove("temp.md")

    # 4. Extract each link
    print(f"🌐 Found {len(links)} links. Beginning extraction...")
    for link in links:
        markdown_extract(link)

    print("🏁 All done! The docs have been extracted.")


if __name__ == "__main__":
    main()
