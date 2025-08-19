from datetime import datetime, timezone
from typing import Optional
from sqlmodel import SQLModel, Field, ForeignKey
from enum import Enum


class PaymentMethod(str, Enum):
    upi = "UPI"
    card = "Card"
    cash = "Cash"
    wallet = "Wallet"


class PaymentStatus(str, Enum):
    pending = "pending"
    success = "success"
    failed = "failed"


class Payment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    order_id: int = Field(ForeignKey("order.id"), nullable=False)

    transaction_id: str = Field(nullable=False, unique=True, index=True, max_length=100)
    amount: float = Field(nullable=False)

    method: PaymentMethod = Field(nullable=False, max_length=50)
    status: PaymentStatus = Field(
        default=PaymentStatus.pending, nullable=False, max_length=50
    )

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), nullable=False
    )
