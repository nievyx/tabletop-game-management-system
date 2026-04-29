from pydantic import BaseModel, Field


class CharacterBase(BaseModel):
    player_id: int
    character_name: str = Field(max_length=100)
    character_type: str
    class_id: int
    species_id: int
    alignment_id: int
    level: int = Field(default=1, ge=1)


class CharacterCreate(CharacterBase):
    pass


class CharacterUpdate(BaseModel):
    player_id: int | None = None
    character_name: str | None = Field(default=None, max_length=100)
    character_type: str | None = None
    class_id: int | None = None
    species_id: int | None = None
    alignment_id: int | None = None
    level: int | None = Field(default=None, ge=1)


class CharacterRead(CharacterBase):
    character_id: int