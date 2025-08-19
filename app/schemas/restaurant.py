from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class RestaurantCreate(BaseModel):
    name: str
    owner_id: int
    description: Optional[str] = None
    location: str


class RestaurantOut(BaseModel):
    id: int
    name: str
    owner_id: int
    description: Optional[str]
    location: str
    rating: float
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
