import chromadb
from chromadb.config import Settings
import json
import os
from pathlib import Path

CHROMA_DB_PATH = str(Path(__file__).resolve().parent.parent / "chroma_db")
chroma_client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
collection_name = "cybersec_docs"
collection = chroma_client.get_or_create_collection(name="cybersec_docs")

with open("../embeddings/data/embedded_docs.json", "r") as f:
    embedded_docs = json.load(f)

ids = [f"doc_{i}" for i in range(len(embedded_docs))]
documents = [item["text"] for item in embedded_docs]
embeddings = [item["embedding"] for item in embedded_docs]
metadatas = [item["metadata"] for item in embedded_docs]


collection.add(
    documents=documents,
    embeddings=embeddings,
    metadatas=metadatas,
    ids=ids
)
print(f"Inserted {len(documents)} documents into ChromaDB collection '{collection_name}'.")
