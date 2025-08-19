from datetime import datetime, timezone
from typing import Optional
from sqlmodel import SQLModel, Field, ForeignKey
from enum import Enum


# Enum for notification type
class NotificationType(str, Enum):
    order_update = "order_update"
    delivery_update = "delivery_update"
    promotion = "promotion"


class Notification(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    user_id: int = Field(ForeignKey("user.id"), nullable=False)
    message: str = Field(nullable=False, max_length=500)

    type: NotificationType = Field(nullable=False, max_length=50)

    is_read: bool = Field(default=False, nullable=False)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), nullable=False
    )
