from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str
    email: str
    password: str

class PostSchema(BaseModel):
    title: str
    content: str
    user_id: int