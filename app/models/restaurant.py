from datetime import datetime, timezone
from typing import Optional
from sqlmodel import SQLModel, Field, ForeignKey


class Restaurant(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(nullable=False, max_length=150)
    owner_id: int = Field(ForeignKey("user.id"), nullable=False)
    description: Optional[str] = Field(default=None, max_length=500)
    location: str = Field(nullable=False, max_length=255)
    rating: float = Field(default=0.0, nullable=False)
    is_active: bool = Field(default=True, nullable=False)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), nullable=False
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), nullable=False
    )
