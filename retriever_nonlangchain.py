import chromadb
import ollama
from ExtendedOllamaEmbeddingFunction import OllamaEmbeddingFunction

ef = OllamaEmbeddingFunction(
    model_name="llama3.2", url="http://localhost:11434/api/embeddings"
)


client = chromadb.PersistentClient(path="db")
collection = client.get_collection("markdown_documents", embedding_function=ef)

result = collection.query(
    query_texts=["what would be the air quality in brisbane today?"],
    # where_document={"$contains": '{"text": "rain"}'},
    n_results=3,
)

import json

# print(json.dumps(result, indent=4))
for doc in result["documents"][0]:
    print(doc)
    print()
print(result)
# print(collection.count())


"""
next steps:
1. since some files can link docs to other files, build a file crawler tool, which can be used to fetch required file, based on this logic
i.e. -> file-1 links to file-2's param docs, fetch file-2 data (probably as tool call from ollama), extract params from it, send for additional context
"""

