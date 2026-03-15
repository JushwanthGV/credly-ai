from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models import Payment, Shop
from app.schemas import PaymentCreate, PaymentResponse

router = APIRouter(prefix="/payments", tags=["payments"])


@router.get("/shop/{shop_id}", response_model=List[PaymentResponse])
def get_payments_by_shop(shop_id: UUID, db: Session = Depends(get_db)):
    payments = (
        db.query(Payment)
        .filter(Payment.shop_id == shop_id)
        .order_by(Payment.created_at.desc())
        .all()
    )
    return payments


@router.post("", response_model=PaymentResponse, status_code=status.HTTP_201_CREATED)
def create_payment(payment_data: PaymentCreate, db: Session = Depends(get_db)):
    shop = db.query(Shop).filter(Shop.id == payment_data.shop_id).first()
    if not shop:
        raise HTTPException(status_code=404, detail="Shop not found")

    db_payment = Payment(**payment_data.model_dump())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment


@router.delete("/{payment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_payment(payment_id: UUID, db: Session = Depends(get_db)):
    payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")

    db.delete(payment)
    db.commit()
    return None
