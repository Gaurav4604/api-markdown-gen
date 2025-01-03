import chromadb.utils.embedding_functions as embedding_functions

ef = embedding_functions.OllamaEmbeddingFunction(
    url="http://localhost:11434/api/embeddings", model_name="llama3.2"
)

embeddings = ef(["This is my first text to embed", "This is my second document"])
print(embeddings)
