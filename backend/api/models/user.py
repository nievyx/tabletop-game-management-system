from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password_hash: str

class UserUpdate(UserCreate):
    username: str
    email: str
    password_hash: str

class UserOut(BaseModel):
    user_id: int
    username: str
    email: str