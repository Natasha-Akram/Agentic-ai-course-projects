from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


PDF_PATH = "data/tech_store_knowledge_base.pdf"
CHROMA_PATH = "chroma_db"
COLLECTION_NAME = "technova_knowledge"


def ingest_pdf():
    print("Loading PDF...")

    loader = PyPDFLoader(PDF_PATH)
    documents = loader.load()

    print(f"PDF loaded successfully.")
    print(f"Total pages: {len(documents)}")

    print("\nSplitting document into chunks...")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = text_splitter.split_documents(documents)

    print(f"Total chunks created: {len(chunks)}")

    print("\nLoading embedding model...")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Creating ChromaDB...")

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH,
        collection_name=COLLECTION_NAME
    )

    print("\nKnowledge base successfully stored in ChromaDB!")
    print(f"ChromaDB location: {CHROMA_PATH}")


if __name__ == "__main__":
    ingest_pdf()