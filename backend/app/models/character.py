from pydantic import BaseModel, Field

class CharacterBase(BaseModel):
    profile_id: int
    class_id: int
    level: int = Field(default=1, ge=1)

class CharacterCreate(CharacterBase):
    pass

class CharacterUpdate(CharacterBase):
    profile_id: int | None = None
    class_id: int | None = None
    level: int | None = Field(default=None, ge=1)

class CharacterRead(CharacterBase):
    profile_id: int | None
