import chromadb
from chromadb.config import Settings

def get_chroma_client():
    """ it initialises chromadb client with default settings"""
    client = chromadb.PersistentClient(path="./chromadb_data")
    return client
def get_or_create_collection(collection_name="cyber_docs"):
    """to get or to create a collection in chromadb"""
    client = get_chroma_client()
    try:
        collection = client.get_collection(collection_name)
    except Exception:
        collection = client.create_collection(collection_name)
    return collection
if __name__ == "__main__":
    collection = get_or_create_collection()
    print(f"ChromaDB collection '{collection.name}' is ready")