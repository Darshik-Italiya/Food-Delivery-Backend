from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from ..models.order import OrderStatus, PaymentStatus


class OrderCreate(BaseModel):
    customer_id: int
    restaurant_id: int
    total_price: float


class OrderOut(BaseModel):
    id: int
    customer_id: int
    restaurant_id: int
    total_price: float
    status: OrderStatus
    payment_status: PaymentStatus
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
