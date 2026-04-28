from datetime import datetime
from pydantic import BaseModel

class CharacterQuestBase(BaseModel):
    character_id: int
    quest_id: int
    completion_date: datetime | None = None

class CharacterQuestCreate(CharacterQuestBase):
    character_id: int
    quest_id: int

class CharacterQuestUpdate(BaseModel):
    # character_id: int | None = None
    # quest_id: int | None = None
    completion_date: datetime | None = None

class CharacterQuestRead(CharacterQuestBase):
    character_quest_id: int