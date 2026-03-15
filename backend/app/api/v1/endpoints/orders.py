from typing import List
from uuid import UUID
from decimal import Decimal
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models import Order, OrderItem, Product, Shop
from app.schemas import OrderCreate, OrderResponse, OrderItemResponse

router = APIRouter(prefix="/orders", tags=["orders"])


def get_orders_by_shop(shop_id: UUID, db: Session = Depends(get_db)):
    orders = (
        db.query(Order)
        .filter(Order.shop_id == shop_id)
        .order_by(Order.created_at.desc())
        .all()
    )
    result = []
    for order in orders:
        items = []
        for item in order.items:
            items.append(
                OrderItemResponse(
                    id=item.id,
                    order_id=item.order_id,
                    product_id=item.product_id,
                    quantity=float(item.quantity),
                    unit_price=float(item.unit_price),
                    total=float(item.total),
                )
            )
        result.append(
            OrderResponse(
                id=order.id,
                shop_id=order.shop_id,
                total=float(order.total),
                status=order.status,
                notes=order.notes,
                created_at=order.created_at,
                items=items,
            )
        )
    return result


@router.get("/shop/{shop_id}", response_model=List[OrderResponse])
def get_orders_by_shop_endpoint(shop_id: UUID, db: Session = Depends(get_db)):
    return get_orders_by_shop(shop_id, db)


@router.get("/{order_id}", response_model=OrderResponse)
def get_order(order_id: UUID, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    items = []
    for item in order.items:
        items.append(
            OrderItemResponse(
                id=item.id,
                order_id=item.order_id,
                product_id=item.product_id,
                quantity=float(item.quantity),
                unit_price=float(item.unit_price),
                total=float(item.total),
            )
        )

    return OrderResponse(
        id=order.id,
        shop_id=order.shop_id,
        total=float(order.total),
        status=order.status,
        notes=order.notes,
        created_at=order.created_at,
        items=items,
    )


@router.post("", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
def create_order(order_data: OrderCreate, db: Session = Depends(get_db)):
    shop = db.query(Shop).filter(Shop.id == order_data.shop_id).first()
    if not shop:
        raise HTTPException(status_code=404, detail="Shop not found")

    total = Decimal("0")
    order_items = []

    for item_data in order_data.items:
        product = db.query(Product).filter(Product.id == item_data.product_id).first()
        if not product:
            raise HTTPException(
                status_code=404, detail=f"Product {item_data.product_id} not found"
            )

        item_total = Decimal(str(item_data.quantity)) * product.unit_price
        total += item_total

        order_items.append(
            {
                "product_id": product.id,
                "quantity": item_data.quantity,
                "unit_price": float(product.unit_price),
                "total": float(item_total),
            }
        )

    db_order = Order(
        shop_id=order_data.shop_id, total=float(total), notes=order_data.notes
    )
    db.add(db_order)
    db.flush()

    for item_data in order_items:
        db_item = OrderItem(order_id=db_order.id, **item_data)
        db.add(db_item)

    db.commit()
    db.refresh(db_order)

    items_response = []
    for item in db_order.items:
        items_response.append(
            OrderItemResponse(
                id=item.id,
                order_id=item.order_id,
                product_id=item.product_id,
                quantity=float(item.quantity),
                unit_price=float(item.unit_price),
                total=float(item.total),
            )
        )

    return OrderResponse(
        id=db_order.id,
        shop_id=db_order.shop_id,
        total=float(db_order.total),
        status=db_order.status,
        notes=db_order.notes,
        created_at=db_order.created_at,
        items=items_response,
    )


@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(order_id: UUID, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    db.query(OrderItem).filter(OrderItem.order_id == order_id).delete()
    db.delete(order)
    db.commit()
    return None
