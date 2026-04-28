from pydantic import BaseModel, Field

class ClassRead(BaseModel):
    class_id: int
    class_name: str = Field(max_length=255)
    description: str | None = None

class SpeciesRead(BaseModel):
    species_id: int
    species_name: str = Field(max_length=255)

class AlignmentRead(BaseModel):
    alignment_id: int
    alignment_name: str = Field(max_length=255)

class ItemTypeRead(BaseModel):
    item_type_id: int
    item_type_name: str = Field(max_length=255)

class RarityRead(BaseModel):
    rarity_id: int
    rarity_name: str = Field(max_length=255)

class RegionRead(BaseModel):
    region_id: int
    region_name: str = Field(max_length=255)

class DifficultyRead(BaseModel):
    difficulty_id: int
    difficulty_name: str = Field(max_length=255)
