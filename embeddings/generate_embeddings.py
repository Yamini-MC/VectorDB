from sentence_transformers import SentenceTransformer
import json
import os

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

documents = [
    {"text": "Cybersecurity involves protecting systems from digital attacks.", "metadata": {"source": "doc1.pdf", "page": 1}},
    {"text": "Phishing is used to trick users into revealing sensitive information.", "metadata": {"source": "doc2.pdf", "page": 3}},
    {"text": "Firewalls are a basic form of network protection.", "metadata": {"source": "doc3.pdf", "page": 5}},
]

texts = [doc["text"] for doc in documents]

embeddings =model.encode(texts, show_progress_bar=True)

data_to_save = [
    {
        "text": text,
        "embedding": embedding.tolist(),
        "metadata": documents[i]["metadata"]
    }
    for i, (text,embedding) in enumerate(zip(texts,embeddings))
]

os.makedirs("data",exist_ok=True)
with open("data/embedded_docs.json", "w") as f:
    json.dump(data_to_save, f, indent=2)
    
print("embeddings generated and saved to data/embedded_docs.json")
