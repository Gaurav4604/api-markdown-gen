import tool_calls
import ollama

q1 = "in the next seven days, when would be a good time to swim, in the ocean, in Darwin?"
q2 = "will tomorrow afternoon be a nice time to swim in the ocean in Adelaide?"
q3 = "should I wear a hat tomorrow?"
q4 = "is it gonna be sweater weather soon?"

q_used = q1


location = tool_calls.get_location_from_question(q_used)

if not location.location_found:
    location.location = "Adelaide"

print("🔎 Starting weather pipeline for location '{}'...".format(location.location))

# Retrieve Latitude and Longitude


# Generate documents relevant to user query
docs = tool_calls.generate_target_docs_for_query(q_used)
print(f"🗂️ Documents selected based on query '{q_used}':")
for doc in docs:
    print(f"   - {doc.model_dump_json(indent=2)}")

# Execute API calls
api_queries = tool_calls.generate_and_execute_api_calls(docs, latlng, date_data, tz)
print(f"🌐 Executed API queries. Total responses received: {len(api_queries)}")
for query in api_queries:
    print(f"   - {query.model_dump_json(indent=2)}")

# Infer conclusion from the gathered data
conclusion = tool_calls.infer_conclusion(api_queries, q_used)
print("✅ Final conclusion:")
print(conclusion.model_dump_json(indent=2))
