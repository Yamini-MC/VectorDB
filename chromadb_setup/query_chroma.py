import chromadb
from chromadb.config import Settings
from utils.config import CHROMA_COLLECTION_NAME
from pathlib import Path

CHROMA_DB_PATH = str(Path(__file__).resolve().parent.parent / "chroma_db")
chroma_client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
def query_documents(query_text: str, top_k: int = 3):
    collection = chroma_client.get_collection(name=CHROMA_COLLECTION_NAME)
    results = collection.query(query_texts=[query_text], n_results=top_k)
    formatted_results = []
    for i in range(len(results['documents'][0])):
        formatted_results.append({
            "id": results['ids'][0][i],
            "text": results['documents'][0][i],
            "metadata": results['metadatas'][0][i]
        })
    return formatted_results