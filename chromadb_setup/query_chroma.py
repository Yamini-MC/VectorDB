# chromadb_setup/query_chroma.py

import chromadb
from sentence_transformers import SentenceTransformer

# Initialize Chroma client and collection
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection(name="cybersec_docs")

# Load embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def query_documents(query: str, top_k: int = 3):
    # Embed the query
    query_embedding = model.encode([query])[0]

    # Perform similarity search
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    output = []
    # Ensure we only access what's actually returned
    returned = len(results["ids"][0])

    for i in range(returned):
        output.append({
            "id": results["ids"][0][i],
            "document": results["documents"][0][i],
            "metadata": results["metadatas"][0][i],
            "distance": results["distances"][0][i]
        })

    return output
