from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password_hash: str

class UserUpdate(BaseModel):
    username: str | None = None
    email: str | None = None
    password_hash: str | None = None

class UserOut(BaseModel):
    user_id: int
    username: str
    email: str