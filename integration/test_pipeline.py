from chromadb_setup.query_chroma import query_documents
from utils.config import CHROMA_COLLECTION_NAME

def test_query():
    test_question = "what is phishing attack?"
    results = query_documents(test_question, top_k=3)

    print("query:", test_question)
    print("Top Results:")
    for i, res in enumerate(results, start=1):
        print(f"\nResult {i}:")
        print(f"ID: {res['id']}")
        print(f"Text: {res['text'][:250]}...")
        print(f"Metadata: {res['metadata']}")


if __name__ == "__main__":
    test_query()