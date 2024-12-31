import os
import time
from urllib.parse import urljoin

from playwright.sync_api import sync_playwright
import trafilatura
import frontmatter
from bs4 import BeautifulSoup


def scrape_page(page, url):
    """
    Scrolls the page, waits for all network requests to finish,
    optionally clicks the 'Python' button if it exists,
    and returns the final HTML content.
    """
    page.goto(url, wait_until="networkidle")
    # Scroll to the bottom for lazy-loaded content
    page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
    page.wait_for_load_state("networkidle")  # Wait again for network to be idle

    # Check for a 'Python' button and click it if present
    python_button = page.locator("button:has-text('python')")
    if python_button.count() > 0:
        python_button.first.click()
        page.wait_for_load_state("networkidle")

    # Return the resulting HTML
    return page.content()


def extract_and_save_markdown(html_content, api_endpoint=None):
    """
    Converts the HTML to Markdown, attaches any metadata (including the API endpoint),
    and saves the result to the 'docs' directory as a .md file.
    """
    # Extract markdown with Trafilatura
    markdown = trafilatura.extract(
        html_content,
        favor_precision=True,
        include_links=True,
        include_tables=True,
        with_metadata=True,
        deduplicate=True,
        fast=False,
        target_language="english",
        output_format="markdown",
    )
    if not markdown:
        return

    # Convert to frontmatter object
    fm_content = frontmatter.loads(markdown)

    # If no title is found, set a default
    if "title" not in fm_content:
        fm_content["title"] = "Untitled"

    # If we detected an API endpoint, store it in frontmatter
    if api_endpoint:
        fm_content["api-endpoint"] = api_endpoint

    # Convert back to text
    markdown_str = frontmatter.dumps(fm_content)

    # Prepare filename from the frontmatter title
    filename = fm_content["title"].replace(" ", "_").lower() + ".md"

    # Make sure 'docs' directory exists
    os.makedirs("docs", exist_ok=True)

    # Save file inside docs/ folder
    filepath = os.path.join("docs", filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(markdown_str)

    return filepath


def crawl_en_docs(start_url):
    """
    Performs a BFS crawl starting from 'start_url',
    visiting all pages whose link contains '/en/docs'.
    For each page, we:
      - Mark as visited
      - Scrape and extract data
      - Save to Markdown
      - Discover further links with '/en/docs'
    """
    visited = set()
    queue = [start_url]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        while queue:
            current_url = queue.pop(0)

            # Skip if already visited
            if current_url in visited:
                continue
            visited.add(current_url)

            print(f"🚀 Starting to scrape: {current_url}")
            start_time = time.time()

            # --- Scrape the page ---
            html_content = scrape_page(page, current_url)

            # --- Parse HTML with BeautifulSoup ---
            soup = BeautifulSoup(html_content, "html.parser")

            # 1) Extract the first form action that contains 'api.'
            api_links = [
                form.get("action")
                for form in soup.find_all("form", action=True)
                if "api." in form.get("action", "")
            ]
            first_api_link = api_links[0] if api_links else None

            # 2) Convert HTML -> Markdown + Save
            extract_and_save_markdown(html_content, api_endpoint=first_api_link)

            # 3) Find more '/en/docs' links & enqueue
            a_tags = soup.find_all("a", href=True)
            new_links = [
                urljoin("https://open-meteo.com", a["href"])
                for a in a_tags
                if "/en/docs" in a["href"]
            ]
            for link in new_links:
                if link not in visited:
                    queue.append(link)

            end_time = time.time()
            elapsed = end_time - start_time
            print(f"🏁 Finished scraping: {current_url} in {elapsed:.2f} seconds\n")

        browser.close()


if __name__ == "__main__":
    start_url = "https://open-meteo.com/en/docs"
    crawl_en_docs(start_url)
