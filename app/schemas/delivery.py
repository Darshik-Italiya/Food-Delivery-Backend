from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from ..models.delivery import DeliveryStatus


class DeliveryCreate(BaseModel):
    order_id: int
    delivery_partner_id: int


class DeliveryOut(BaseModel):
    id: int
    order_id: int
    delivery_partner_id: int
    pickup_time: Optional[datetime]
    delivery_time: Optional[datetime]
    status: DeliveryStatus

    class Config:
        from_attributes = True
