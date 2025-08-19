from datetime import datetime, timezone
from typing import Optional
from sqlmodel import SQLModel, Field
from enum import Enum


class User_Roles(str, Enum):
    customer = "customer"
    restaurant_owner = "restaurant_owner"
    delivery_partner = "delivery_partner"
    admin = "admin"


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(nullable=False, max_length=100)
    email: str = Field(nullable=False, unique=True, index=True, max_length=100)
    password_hash: str = Field(nullable=False, max_length=255)
    phone_number: Optional[str] = Field(default=None, max_length=15)
    address: Optional[str] = Field(default=None, max_length=255)
    role: User_Roles = Field(
        default=User_Roles.customer,
        nullable=False,
        max_length=50,
    )
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), nullable=False
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), nullable=False
    )
