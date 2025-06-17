import os

MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
MONGO_USERNAME = os.getenv("MONGO_INITDB_ROOT_USERNAME", "admin")
MONGO_PASSWORD = os.getenv("MONGO_INITDB_ROOT_PASSWORD", "Malcom@2024")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "cybersec_chatbot")

CHROMA_COLLECTION_NAME = "cybersec_docs"
CHROMA_PERSIST_DIR = "vectordb/chromadb_setup/chroma_store"

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

DOCS_PATH = "data/cybersecurity_documents"
EMBEDDED_DOCS_JSON = "vectordb/chromadb_setup/embedded_docs.json"