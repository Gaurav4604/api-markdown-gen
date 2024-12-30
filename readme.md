# **API Docs Extractor**

The API Docs Extractor is a Python-based script that utilizes web scraping, rule-based Markdown generation, and
LLM (Large Language Model) based Markdown cleanup to create a webpage Markdown translation.

## **Description**

The API Docs Extractor takes in a URL of an API documentation website as input and extracts the necessary
information to generate a clean and readable Markdown representation of the documentation. It uses web scraping
with Playwright to interact with the website, Trafilatura for rule-based Markdown generation, and ollama's LLM
server (Llama 3.2) for natural language processing tasks such as cleaning up generated Markdown.

## **Features**

- Webpage Markdown translation
- Rule-based Markdown generation using Trafilatura
- LLM-based Markdown cleanup with ollama's Llama 3.2
- Python-based script for ease of use and customization

## **How it Works**

1. **Web Scraping**: Playwright is used to interact with the API documentation website, extracting relevant
   information such as page titles, headings, and text content.
2. **Rule-Based Markdown Generation**: Trafilatura's rule-based Markdown generation engine creates a clean and
   readable Markdown representation of the extracted information.
3. **LLM-Based Markdown Cleanup**: ollama's Llama 3.2 is used to perform natural language processing tasks such as
   spell-checking, grammar correction, and fluency improvement on the generated Markdown.

## **Output**

The API Docs Extractor generates a clean and readable Markdown representation of the API documentation website,
complete with headings, sections, and relevant information.

## **Example Use Case**

- URL: `https://api.example.com/docs`
- Output: A Markdown representation of the API documentation website, including page titles, headings, and text
  content.

Here's a sample README for your project:

**README**

# API Docs Extractor

A Python-based script that extracts webpage Markdown translation using web scraping, rule-based Markdown
generation, and LLM (Large Language Model) based Markdown cleanup.

## Requirements

- Python 3.8+
- ollama (for LLM server)
- playwright (for web scraping)
- trafilatura (for rule-based Markdown generation)

## Installation

```bash
pip install -r requirements.txt
```

## Contributing

Pull requests and issues are welcome!
