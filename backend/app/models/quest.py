from pydantic import BaseModel, Field

class QuestBase(BaseModel):
    quest_name: str = Field(max_length=100)

class QuestCreate(QuestBase):
    pass

class QuestUpdate(BaseModel):
    quest_name: str | None = Field(default=None, max_length=100)
    region_id: int | None = None
    difficulty: int | None = None

class QuestRead(QuestBase):
    quest_id: int
