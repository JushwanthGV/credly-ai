from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.core.database import get_db
from app.models import Shop, Order, Payment
from app.schemas import BalanceResponse

router = APIRouter(prefix="/shops", tags=["balance"])


@router.get("/{shop_id}/balance", response_model=BalanceResponse)
def get_shop_balance(shop_id: UUID, db: Session = Depends(get_db)):
    shop = db.query(Shop).filter(Shop.id == shop_id).first()
    if not shop:
        raise HTTPException(status_code=404, detail="Shop not found")

    total_orders = (
        db.query(func.coalesce(func.sum(Order.total), 0))
        .filter(Order.shop_id == shop_id)
        .scalar()
    )
    total_payments = (
        db.query(func.coalesce(func.sum(Payment.amount), 0))
        .filter(Payment.shop_id == shop_id)
        .scalar()
    )

    return BalanceResponse(
        shop_id=shop_id,
        total_orders=float(total_orders),
        total_payments=float(total_payments),
        balance=float(total_orders) - float(total_payments),
    )
