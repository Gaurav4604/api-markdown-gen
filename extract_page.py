from playwright.sync_api import sync_playwright
import trafilatura
import ollama


prompt = """
Prompt:

You are an expert in markdown formatting and content editing. Your task is to take a raw markdown file and:

Fix Markdown Syntax:

Correct any malformed headers, bullet points, tables, or code blocks.
Ensure proper spacing and indentation where necessary.
Correct Grammar and Style:

Fix any grammatical errors, typos, and awkward phrasing in the text.
Maintain a professional, concise, and clear tone throughout.
Ensure Markdown Best Practices:

Add blank lines before and after headers, lists, and code blocks as per markdown conventions.
Use consistent header levels (#, ##, ###, etc.) and avoid skipping levels.
Properly format links, images, and inline code using appropriate markdown syntax.
Enhance Readability:

Reorganize content for logical flow where needed.
Break down long paragraphs into shorter, more readable ones.
Ensure proper use of emphasis (e.g., bold, italics) to highlight important points.
Preserve the Content's Intent:

Retain the original meaning and structure of the content while making improvements.
Input: Provide the raw markdown content below for review and formatting.

Output: Return the corrected and formatted markdown content without introducing new errors or unnecessary changes.
"""

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)  # Use headless=True for headless mode
    page = browser.new_page()

    # Go to the page and wait for network activity to settle
    page.goto("https://open-meteo.com/en/docs", wait_until="networkidle")

    # Scroll to the bottom of the page to trigger lazy loading
    page.evaluate("window.scrollTo(0, document.body.scrollHeight);")

    # Wait for additional network requests to complete
    page.wait_for_load_state("networkidle")

    # Find and click the button with text 'Python'
    button = page.locator("button:has-text('python')")
    if button.count() > 0:  # Ensure the button exists
        button.first.click()  # Click the first button with the text 'Python'
        page.wait_for_load_state("networkidle")  # Wait for network idle again

    # Get the resulting page's HTML
    html_content = page.content()
    with open("page.html", "w", encoding="utf-8") as file:
        file.write(html_content)

    # Close the browser
    browser.close()
    downloaded = trafilatura.extract(
        html_content,
        favor_precision=True,
        include_links=True,
        include_tables=True,
        with_metadata=True,
        deduplicate=True,
        output_format="markdown",
    )

    res = ollama.chat(
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": downloaded},
        ],
        model="llama3.2",
        options={
            "num_ctx": 8124,
            "temperature": 0.2,
        },
    )

    with open("docs_home.csv", "w", encoding="utf-8") as file:
        file.write(res["message"]["content"])
