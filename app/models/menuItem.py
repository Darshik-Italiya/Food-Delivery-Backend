from datetime import datetime, timezone
from typing import Optional
from sqlmodel import SQLModel, Field, ForeignKey


class MenuItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    restaurant_id: int = Field(ForeignKey("restaurant.id"), nullable=False)

    name: str = Field(nullable=False, max_length=150)
    description: Optional[str] = Field(default=None, max_length=500)
    price: float = Field(nullable=False)
    category: Optional[str] = Field(default=None, max_length=100)
    is_available: bool = Field(default=True, nullable=False)

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), nullable=False
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), nullable=False
    )
