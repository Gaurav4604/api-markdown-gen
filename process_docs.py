import os
from semantic_text_splitter import MarkdownSplitter
import frontmatter
import chromadb
import chromadb.utils.embedding_functions as embedding_functions

import shutil


def remove_folder(folder_path):
    try:
        # Remove the contents of the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

        # Remove the folder itself
        os.rmdir(folder_path)
    except FileNotFoundError:
        print(f"Folder '{folder_path}' not found.")
    except PermissionError:
        print(f"Permission denied to remove folder '{folder_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


class Document:
    content = ""
    metadata: dict = {}

    def __init__(self, content="", metadata={}):
        self.content = content
        self.metadata = metadata


# Directory containing your Markdown files
markdown_directory = "docs"

# Load all Markdown files in the directory
documents = []
drop_keys = ["description", "hostname", "sitename", "url"]
for filename in os.listdir(markdown_directory):
    if filename.endswith(".md"):
        file_path = os.path.join(markdown_directory, filename)
        doc = frontmatter.load(file_path)
        doc["source"] = filename
        doc["date"] = doc["date"].strftime("%d-%m-%Y")
        for key in drop_keys:
            if key in doc.keys():
                del doc[key]
        documents.append(doc)


def metadata_str(metadata):
    items = ",\n".join(f"{key}: {value}" for key, value in metadata.items())
    return items


langdocs = []
for doc in documents:
    # chunks = splitter.chunks(doc.content)
    # for chunk in chunks:
    langdoc = Document(content=doc.content, metadata=doc.metadata)
    langdocs.append(langdoc)

remove_folder("db")
# Initialize ChromaDB client
client = chromadb.PersistentClient(path="db")

ef = embedding_functions.OllamaEmbeddingFunction(
    url="http://localhost:11434/api/embeddings", model_name="llama3.2"
)

# Create a collection
collection = client.create_collection(
    name="markdown_documents",
    embedding_function=ef,
    metadata={
        "hnsw:space": "cosine",
        "hnsw:search_ef": 100,
        "hnsw:construction_ef": 1000,
    },
)

# Add chunks to the collection
collection.add(
    ids=[f"id{i}" for i in range(len(langdocs))],
    documents=[chunk.content for chunk in langdocs],
    metadatas=[chunk.metadata for chunk in langdocs],
)


import requests

# import json

# res = requests.post(
#     url="http://localhost:11434/api/embeddings",
#     data=json.dumps({"model": "llama3.2", "prompt": langdocs[0].content}),
# )

# print(res.json())
