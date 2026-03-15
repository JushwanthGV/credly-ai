from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.core.database import get_db
from app.models import Shop, Order, Payment
from app.schemas import ShopCreate, ShopUpdate, ShopResponse

router = APIRouter(prefix="/shops", tags=["shops"])


@router.get("", response_model=List[ShopResponse])
def get_shops(db: Session = Depends(get_db)):
    shops = db.query(Shop).all()
    result = []
    for shop in shops:
        total_orders = (
            db.query(func.coalesce(func.sum(Order.total), 0))
            .filter(Order.shop_id == shop.id)
            .scalar()
        )
        total_payments = (
            db.query(func.coalesce(func.sum(Payment.amount), 0))
            .filter(Payment.shop_id == shop.id)
            .scalar()
        )
        balance = float(total_orders) - float(total_payments)
        shop_response = ShopResponse(
            id=shop.id,
            name=shop.name,
            phone=shop.phone,
            address=shop.address,
            created_at=shop.created_at,
            updated_at=shop.updated_at,
            balance=balance,
        )
        result.append(shop_response)
    return result


@router.get("/search", response_model=List[ShopResponse])
def search_shops(q: str, db: Session = Depends(get_db)):
    shops = db.query(Shop).filter(Shop.name.ilike(f"%{q}%")).all()
    result = []
    for shop in shops:
        total_orders = (
            db.query(func.coalesce(func.sum(Order.total), 0))
            .filter(Order.shop_id == shop.id)
            .scalar()
        )
        total_payments = (
            db.query(func.coalesce(func.sum(Payment.amount), 0))
            .filter(Payment.shop_id == shop.id)
            .scalar()
        )
        balance = float(total_orders) - float(total_payments)
        shop_response = ShopResponse(
            id=shop.id,
            name=shop.name,
            phone=shop.phone,
            address=shop.address,
            created_at=shop.created_at,
            updated_at=shop.updated_at,
            balance=balance,
        )
        result.append(shop_response)
    return result


@router.get("/{shop_id}", response_model=ShopResponse)
def get_shop(shop_id: UUID, db: Session = Depends(get_db)):
    shop = db.query(Shop).filter(Shop.id == shop_id).first()
    if not shop:
        raise HTTPException(status_code=404, detail="Shop not found")

    total_orders = (
        db.query(func.coalesce(func.sum(Order.total), 0))
        .filter(Order.shop_id == shop.id)
        .scalar()
    )
    total_payments = (
        db.query(func.coalesce(func.sum(Payment.amount), 0))
        .filter(Payment.shop_id == shop.id)
        .scalar()
    )
    balance = float(total_orders) - float(total_payments)

    return ShopResponse(
        id=shop.id,
        name=shop.name,
        phone=shop.phone,
        address=shop.address,
        created_at=shop.created_at,
        updated_at=shop.updated_at,
        balance=balance,
    )


@router.post("", response_model=ShopResponse, status_code=status.HTTP_201_CREATED)
def create_shop(shop: ShopCreate, db: Session = Depends(get_db)):
    db_shop = Shop(**shop.model_dump())
    db.add(db_shop)
    db.commit()
    db.refresh(db_shop)
    return ShopResponse(
        id=db_shop.id,
        name=db_shop.name,
        phone=db_shop.phone,
        address=db_shop.address,
        created_at=db_shop.created_at,
        updated_at=db_shop.updated_at,
        balance=0,
    )


@router.put("/{shop_id}", response_model=ShopResponse)
def update_shop(shop_id: UUID, shop_update: ShopUpdate, db: Session = Depends(get_db)):
    shop = db.query(Shop).filter(Shop.id == shop_id).first()
    if not shop:
        raise HTTPException(status_code=404, detail="Shop not found")

    update_data = shop_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(shop, key, value)

    db.commit()
    db.refresh(shop)

    total_orders = (
        db.query(func.coalesce(func.sum(Order.total), 0))
        .filter(Order.shop_id == shop.id)
        .scalar()
    )
    total_payments = (
        db.query(func.coalesce(func.sum(Payment.amount), 0))
        .filter(Payment.shop_id == shop.id)
        .scalar()
    )
    balance = float(total_orders) - float(total_payments)

    return ShopResponse(
        id=shop.id,
        name=shop.name,
        phone=shop.phone,
        address=shop.address,
        created_at=shop.created_at,
        updated_at=shop.updated_at,
        balance=balance,
    )


@router.delete("/{shop_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_shop(shop_id: UUID, db: Session = Depends(get_db)):
    shop = db.query(Shop).filter(Shop.id == shop_id).first()
    if not shop:
        raise HTTPException(status_code=404, detail="Shop not found")

    db.delete(shop)
    db.commit()
    return None
