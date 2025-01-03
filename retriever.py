
from langchain.chains import RetrievalQA
from langchain_ollama import OllamaLLM
from langchain_ollama.embeddings import OllamaEmbeddings

# Initialize the embeddings with the Llama 3.2 model
embeddings = OllamaEmbeddings(model="llama3.2")

# Initialize Chroma vector store with the existing collection
vector_store = Chroma(
    collection_name="markdown_documents",
    persist_directory="db",
    embedding_function=embeddings,
)

# Set up the retriever
retriever = vector_store.as_retriever()

# Initialize the language model
llm = OllamaLLM(model="llama3.2")


# from langchain.chains import create_retrieval_chain
# from langchain.chains.combine_documents import create_stuff_documents_chain
# from langchain.prompts import PromptTemplate

# prompt_template = PromptTemplate(
#     input_variables=["context", "input"],
#     template=(
#         "Use the following context to answer the question.\n\n"
#         "Context:\n{context}\n\n"
#         "Question: {input}\n"
#         "Answer:"
#     ),
# )

# combine_docs_chain = create_stuff_documents_chain(llm=llm, prompt=prompt_template)

# # Set up the RetrievalQA chain
# qa_chain = create_retrieval_chain(
#     retriever=retriever, combine_docs_chain=combine_docs_chain
# )

# query = (
#     "Give me the API call query to get rain data for yesterday for Darwin, Australia"
# )

# # Get the response
# response = qa_chain.invoke({"input": query})


# print(response["answer"])
# print(response["context"])
