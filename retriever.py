from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


CHROMA_PATH = "chroma_db"
COLLECTION_NAME = "technova_knowledge"


def get_retriever():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = Chroma(
        persist_directory=CHROMA_PATH,
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 4}
    )

    return retriever