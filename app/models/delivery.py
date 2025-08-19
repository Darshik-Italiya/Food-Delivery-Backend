from datetime import datetime, timezone
from typing import Optional
from sqlmodel import SQLModel, Field, ForeignKey
from enum import Enum


class DeliveryStatus(str, Enum):
    assigned = "assigned"
    picked_up = "picked_up"
    delivered = "delivered"
    failed = "failed"


class Delivery(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    order_id: int = Field(ForeignKey("order.id"), nullable=False)
    delivery_partner_id: int = Field(ForeignKey("user.id"), nullable=False)

    pickup_time: Optional[datetime] = Field(default=None)
    delivery_time: Optional[datetime] = Field(default=None)

    status: DeliveryStatus = Field(
        default=DeliveryStatus.assigned, nullable=False, max_length=50
    )
