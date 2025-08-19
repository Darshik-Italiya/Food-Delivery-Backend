from typing import Optional
from sqlmodel import SQLModel, Field, ForeignKey


class OrderItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    order_id: int = Field(ForeignKey("order.id"), nullable=False)
    menu_item_id: int = Field(ForeignKey("menuitem.id"), nullable=False)

    quantity: int = Field(default=1, nullable=False)

    price: float = Field(nullable=False)
