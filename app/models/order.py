from datetime import datetime, timezone
from typing import Optional
from sqlmodel import SQLModel, Field, ForeignKey
from enum import Enum


class OrderStatus(str, Enum):
    pending = "pending"
    accepted = "accepted"
    preparing = "preparing"
    out_for_delivery = "out_for_delivery"
    delivered = "delivered"
    cancelled = "cancelled"


class PaymentStatus(str, Enum):
    pending = "pending"
    paid = "paid"
    failed = "failed"


class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    customer_id: int = Field(ForeignKey("user.id"), nullable=False)
    restaurant_id: int = Field(ForeignKey("restaurant.id"), nullable=False)

    total_price: float = Field(nullable=False)

    status: OrderStatus = Field(
        default=OrderStatus.pending, nullable=False, max_length=50
    )
    payment_status: PaymentStatus = Field(
        default=PaymentStatus.pending, nullable=False, max_length=50
    )

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), nullable=False
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), nullable=False
    )
