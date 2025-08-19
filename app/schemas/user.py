from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from ..models.user import User_Roles


class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    phone_number: Optional[str] = None
    address: Optional[str] = None
    role: User_Roles = User_Roles.customer


class UserOut(BaseModel):
    id: int
    name: str
    email: str
    phone_number: Optional[str]
    address: Optional[str]
    role: User_Roles
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
