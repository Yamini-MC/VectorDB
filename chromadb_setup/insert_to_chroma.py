# chromadb_setup/insert_to_chroma.py


import chromadb
import json
import os
import shutil


CHROMA_COLLECTION_NAME = "cybersec_docs"


# Delete the persistent ChromaDB directory if it exists (for a clean insert)
CHROMA_DB_PATH = "chroma_db"
if os.path.exists(CHROMA_DB_PATH):
    shutil.rmtree(CHROMA_DB_PATH)

client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
collection = client.get_or_create_collection(name=CHROMA_COLLECTION_NAME)

# Load embedded data
with open("data/embedded_docs.json", "r", encoding="utf-8") as f:
    embedded_docs = json.load(f)

# Insert into ChromaDB
for idx, doc in enumerate(embedded_docs):
    collection.add(
        documents=[doc["text"]],
        embeddings=[doc["embedding"]],
        metadatas=[doc["metadata"]],
        ids=[f"doc_{idx}"]
    )

print(f"✅ Inserted {len(embedded_docs)} documents into ChromaDB under '{CHROMA_COLLECTION_NAME}'.")
