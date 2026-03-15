from datetime import datetime
from uuid import UUID
from typing import Optional
from decimal import Decimal
from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    unit_price: float


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    unit_price: Optional[float] = None
    is_active: Optional[bool] = None


class ProductResponse(ProductBase):
    id: UUID
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True
