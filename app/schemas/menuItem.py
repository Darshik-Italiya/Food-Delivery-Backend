from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class MenuItemCreate(BaseModel):
    restaurant_id: int
    name: str
    description: Optional[str] = None
    price: float
    category: Optional[str] = None


class MenuItemOut(BaseModel):
    id: int
    restaurant_id: int
    name: str
    description: Optional[str]
    price: float
    category: Optional[str]
    is_available: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
