from markitdown import MarkItDown
from extraction import scrape_page
from playwright.sync_api import sync_playwright

md = MarkItDown()
start_url = "https://open-meteo.com/en/docs"
result = md.convert_url(start_url)
print(result.text_content)
with open("sample.md", "w", encoding="utf-8") as f:
    f.write(result.text_content)
