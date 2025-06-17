from pymongo import MongoClient
from models import User, Message, Feedback

MONGO_URI = "mongodb://admin:Malcom@2024@localhost:27017"
DB_NAME = "cybersec_chatbot"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

def insert_user(user: User):
    return db.users.insert_one(user.dict())

def find_user_by_email(email: str):
    return db.users.find_one({"email": email})

def insert_message(msg: Message):
    return db.messages.insert_one(msg.dict())

def get_messages_by_user(user_id: str):
    return list(db.messages.find({"user_id": user_id}))

def insert_feedback(fb: Feedback):
    return db.feedback.insert_one(fb.dict())

def get_feedback_for_message(message_id: str):
    return db.feedback.find_one({"message_id": message_id})