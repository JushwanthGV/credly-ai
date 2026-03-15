from datetime import datetime
from uuid import UUID
from typing import Optional
from pydantic import BaseModel


class ShopBase(BaseModel):
    name: str
    phone: Optional[str] = None
    address: Optional[str] = None


class ShopCreate(ShopBase):
    pass


class ShopUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None


class ShopResponse(ShopBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    balance: Optional[float] = 0

    class Config:
        from_attributes = True
