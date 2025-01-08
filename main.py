import argparse
import tool_calls


def weather_agent_pipeline(question: str) -> tool_calls.Conclusion:
    """
    Orchestrates the entire weather pipeline to gather and interpret weather data
    for a given question, then returns a concluding statement.

    Args:
        question (str): The question from the user (e.g. "Is it going to rain this evening?")

    Returns:
        tool_calls.Conclusion: A conclusion object containing the answer to user's question,
        along with the reasoning for the same
    """
    meta = tool_calls.get_question_meta_data(question)
    print(meta)
    print(f"🔎 Starting weather pipeline for location '{meta.location}'...")

    # Generate documents relevant to user query
    docs = tool_calls.generate_target_docs_for_query(question)
    print(f"🗂️ Documents selected based on query '{question}':")
    for doc in docs:
        print(f"   - {doc.model_dump_json(indent=2)}")

    # Execute API calls
    api_queries = tool_calls.generate_and_execute_api_calls(
        docs, meta.latlng, meta.timezone
    )
    print(f"🌐 Executed API queries. Total responses received: {len(api_queries)}")
    for query in api_queries:
        print(f"   - {query.model_dump_json(indent=2)}")

    # Infer conclusion from the gathered data
    conclusion = tool_calls.infer_conclusion(api_queries, question)
    print(f"✅ Final conclusion: {str(conclusion)}")
    return conclusion


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Weather agent pipeline.")
    parser.add_argument(
        "-q",
        "--question",
        type=str,
        required=True,
        help="Weather question to be answered",
    )
    args = parser.parse_args()

    # Execute pipeline with user-provided question
    conclusion = weather_agent_pipeline(args.question)
