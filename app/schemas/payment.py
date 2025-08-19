from pydantic import BaseModel
from datetime import datetime
from ..models.payment import PaymentMethod, PaymentStatus


class PaymentCreate(BaseModel):
    order_id: int
    transaction_id: str
    amount: float
    method: PaymentMethod


class PaymentOut(BaseModel):
    id: int
    order_id: int
    transaction_id: str
    amount: float
    method: PaymentMethod
    status: PaymentStatus
    created_at: datetime

    class Config:
        from_attributes = True
