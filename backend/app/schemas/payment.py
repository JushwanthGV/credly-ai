from datetime import datetime
from uuid import UUID
from typing import Optional
from pydantic import BaseModel


class PaymentBase(BaseModel):
    shop_id: UUID
    amount: float
    payment_method: Optional[str] = None
    notes: Optional[str] = None


class PaymentCreate(PaymentBase):
    pass


class PaymentResponse(PaymentBase):
    id: UUID
    created_at: datetime

    class Config:
        from_attributes = True
