from datetime import datetime
from pydantic import BaseModel, EmailStr,Field

class PlayerBase(BaseModel):
    email: EmailStr = Field(max_length=255)
    display_name: str = Field(max_length=100)

class PlayerCreate(PlayerBase):
    password_hash: str

class PlayerUpdate(BaseModel):
    email: EmailStr | None = Field(default=None, max_length=255)
    display_name: str | None = Field(default=None, max_length=100)
    password_hash: str | None = None

class PlayerRead(PlayerBase):
    player_id: int
    date_created: datetime