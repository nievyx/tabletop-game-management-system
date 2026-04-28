from pydantic import BaseModel, Field

class InventoryBase(BaseModel):
    character_id: int
    item_id: int
    quantity: int = Field(default=1, ge=1)

class InventoryCreate(InventoryBase):
    pass

class Inventory(BaseModel):
    character_id: int | None = None
    item_id: int | None = None
    quantity: int| None = Field(default=None, ge=1)

class InventoryRead(InventoryBase):
    inventory_id: int

    