from uuid import UUID
from pydantic import BaseModel


class BalanceResponse(BaseModel):
    shop_id: UUID
    total_orders: float
    total_payments: float
    balance: float
