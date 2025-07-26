# integration/test_pipeline.py

from chromadb_setup.query_chroma import query_documents

def test_query():
    question = "DDos attack mitigation strategies"
    results = query_documents(question, top_k=3)
    
    print(f"\nQuery: {question}\nTop Results:\n")
    for i, res in enumerate(results):
       print(f"Result {i+1}:\nID: {res['id']}\nDocument: {res['document']}\nMetadata: {res['metadata']}\n")


if __name__ == "__main__":
    test_query()
