from datetime import datetime
from uuid import UUID
from typing import Optional, List
from pydantic import BaseModel


class OrderItemBase(BaseModel):
    product_id: UUID
    quantity: float


class OrderItemCreate(OrderItemBase):
    pass


class OrderItemResponse(OrderItemBase):
    id: UUID
    order_id: UUID
    unit_price: float
    total: float

    class Config:
        from_attributes = True


class OrderItemInOrder(OrderItemBase):
    name: Optional[str] = None
    unit_price: float
    total: float


class OrderBase(BaseModel):
    shop_id: UUID
    notes: Optional[str] = None


class OrderCreate(OrderBase):
    items: List[OrderItemCreate]


class OrderResponse(OrderBase):
    id: UUID
    total: float
    status: str
    created_at: datetime
    items: List[OrderItemResponse] = []

    class Config:
        from_attributes = True
