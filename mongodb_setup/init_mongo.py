from pymongo import MongoClient


MONGO_URI = "mongodb://admin:Malcom@2024@localhost:27017/"
DB_NAME = "cybersec_chatbot"
COLLECTIONS = ["users", "messages", "feedback"]

def initialize_mongo():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]

    print(f"connected to MongoDB: {DB_NAME}")

    for col in COLLECTIONS:
        if col in db.list_collection_names():
            print(f"collection already exists: {col}")
        else:
            db.create_collection(col)
            print(f"Created collection: {col}")
    client.close()

if __name__ == "__main__":
    initialize_mongo()