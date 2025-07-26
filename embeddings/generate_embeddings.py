# embeddings/generate_embeddings.py

from sentence_transformers import SentenceTransformer
import json
import os

# Load the model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Load your real data from the JSON file
with open("data/cybersecurity_documents/dataset.json", "r", encoding="utf-8") as f:
    documents = json.load(f)

texts = [doc["text"] for doc in documents]
metadata_list = [doc["metadata"] for doc in documents]

# Generate embeddings
embeddings = model.encode(texts, show_progress_bar=True)

# Save as JSON
embedded_data = []
for i, embedding in enumerate(embeddings):
    embedded_data.append({
        "text": texts[i],
        "embedding": embedding.tolist(),
        "metadata": metadata_list[i]
    })

# Save to disk
os.makedirs("data", exist_ok=True)
with open("data/embedded_docs.json", "w", encoding="utf-8") as f:
    json.dump(embedded_data, f, indent=2)

print("✅ Embeddings generated and saved to data/embedded_docs.json")
