from fastapi import APIRouter

from app.api.v1.endpoints import shops, products, orders, payments, balance

api_router = APIRouter()

api_router.include_router(shops.router)
api_router.include_router(products.router)
api_router.include_router(orders.router)
api_router.include_router(payments.router)
api_router.include_router(balance.router)
