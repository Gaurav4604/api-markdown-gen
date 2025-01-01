from langchain_community.document_loaders import UnstructuredMarkdownLoader
import os
from semantic_text_splitter import MarkdownSplitter
from langchain.schema.document import Document
import frontmatter

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


splitter = MarkdownSplitter(1000)


def metadata_str(metadata):
    items = ",\n".join(f"{key}: {value}" for key, value in metadata.items())
    return items


document_chunks = []

for doc in documents:
    chunks = splitter.chunks(doc.content)
    for chunk in chunks:
        langdoc = Document(
            page_content=metadata_str(doc.metadata) + chunk, metadata=doc.metadata
        )
        document_chunks.append(langdoc)

from langchain_ollama.embeddings import OllamaEmbeddings

# Initialize the embeddings with the Llama 3.2 model
embeddings = OllamaEmbeddings(model="llama3.2")


import chromadb
from chromadb.config import Settings

# Initialize ChromaDB client
client = chromadb.PersistentClient(path="db", settings=Settings())

# Create a collection
collection = client.create_collection(name="markdown_documents")

# Add chunks to the collection
for i, chunk in enumerate(document_chunks):
    collection.add(
        ids=[str(i)],
        embeddings=[embeddings.embed_query(chunk.page_content)],
        documents=[chunk.page_content],
        metadatas=[chunk.metadata],
    )
