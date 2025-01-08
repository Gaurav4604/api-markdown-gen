# **Gen-Weather-RAG**

This repository provides a Retrieval-Augmented Generation (RAG) chain pipeline to handle weather-related questions using dynamic query generation, chain-of-thought reasoning, and structured output. By orchestrating multiple steps—location extraction, document retrieval, API parameter generation, and final conclusion—this codebase enables a seamless flow from user query to final answer.

## Overview

- Retrieval-Augmented Generation (RAG): The pipeline performs a document lookup (stored in .yml files) and uses those artifacts to generate weather-related API queries.
- Chain-of-Thought Reasoning: It breaks down user queries into sub-questions, chooses relevant documents, and systematically executes a chain of logic to produce answers.
- Structured Output: Uses pydantic models to ensure responses (including partial steps) are well-defined JSON objects.
- Dynamic Query Generation: Based on the selected documents, the pipeline programmatically builds REST API endpoints aligned with the user’s question (e.g., daily or hourly forecasts).
- This approach allows the system to infer context from both user prompts and a local knowledge base, resulting in precise, data-driven weather insights for user's question.

## Requirements

- Python 3.8+
- ollama (for LLM server)

## Installation

```bash
ollama pull llama3.2
ollama pull gemma2
ollama pull marco-o1

pip install -r requirements.txt
```

## Example Usage

```bash
python main.py -q "will it rain in the next hour in tokyo?"
```

```json
{
  "answer": "No, based on the available weather forecasts, there is no indication of rain in Tokyo within the next hour.",
  "reasoning": "The provided weather and marine condition data does not show any precipitation expected in the upcoming hour. Additionally, there are no marine conditions that would affect the likelihood of rain in Tokyo during this timeframe."
}
```

## **How it Works**

NOTE: steps 1 to 6 are already done, if you want to add more APIs, you can do so by adding files containing api-endpoint, parameters etc to `/yml` directory

1. **Markdown Generation**: open-meteo's API documentation webpages are scraped for API parameters, and stored in `/docs` directory
2. **Manual Filteration and Cleanup**: A subset of files extracted are selected and rest are moved to `archive`
3. **Rule-Based YAML File Generation**: Using `mrkdown_analysis`, for each markdown file, the tables containing parameters are converted to .yaml file, with

   - parameter name
   - unit
   - description

   for easier **structuring and readability of the parameters during RAG context generation**

4. **Manual Refactor and Cleanup**: Some parameters might be mis-named or mis-represented, these are either _removed_ or _renamed_ to their actual values **manually**.

5. **LLM-based Document metadata Generation**: Using `marco-o1` _advanced reasoning_ model

   - description
   - tags
   - filename

   is extracted out for each of the files

6. **Manual Refactor and Cleanup**: Another round of cleanup and removal of invalid tags, and editing of incorrect description if required, is done.

7. **Pipeline**: This is the file where magic happens, a RAG pipeline is created
   1. question context is obtained, for geo-location and date-time, timezone metadata (using geolocation libraries and `llama3.2`)
   2. the user's question is extracted into sub-questions, with documents associated with sub-questions clubbed in the response (using `marco-o1`)
   3. API calls with parameters are generated and executed for these sub-questions (using `gemma2`)
   4. Conclusion is obtained on the basis of these API-calls, sub-question and user's main question (using `marco-o1`)

## **Output**

The output will usually be a conclusion and reasoning associated to the provided conclusion, as a pydantic model named `Conclusion`
present in `tool_calls.py`

## Contributing

Pull requests and issues are welcome!
