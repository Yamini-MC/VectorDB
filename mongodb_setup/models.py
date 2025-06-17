from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class User(BaseModel):
    username: str
    email: str
    joined_at: datetime = Field(default_factory=datetime.utcnow)

class Message(BaseModel):
    user_id: str
    user_input: str
    bot_response: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class Feedback(BaseModel):
    message_id: str
    rating: int
    comment: Optional[str] = None
    submitted_at: datetime = Field(default_factory=datetime.utcnow)
    