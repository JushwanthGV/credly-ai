# Backend Documentation - Credly

## Overview

FastAPI-based REST API for the Credly ledger and order management system.

---

## Tech Stack

- **Framework**: FastAPI
- **ORM**: SQLAlchemy
- **Database**: PostgreSQL
- **Migrations**: Alembic
- **Validation**: Pydantic

---

## Project Structure

```
backend/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints/
│   │       │   ├── shops.py
│   │       │   ├── orders.py
│   │       │   ├── payments.py
│   │       │   └── products.py
│   │       └── router.py
│   ├── core/
│   │   ├── config.py
│   │   └── database.py
│   ├── models/
│   │   ├── shop.py
│   │   ├── order.py
│   │   ├── payment.py
│   │   └── product.py
│   ├── schemas/
│   │   ├── shop.py
│   │   ├── order.py
│   │   ├── payment.py
│   │   └── product.py
│   ├── services/
│   │   ├── shop_service.py
│   │   ├── order_service.py
│   │   ├── payment_service.py
│   │   └── balance_service.py
│   └── main.py
├── alembic/
│   ├── versions/
│   ├── env.py
│   └── ini
├── requirements.txt
└── .env.example
```

---

## Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your database credentials
```

4. Run database migrations:
```bash
alembic upgrade head
```

5. Start the server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

---

## Running Tests

```bash
pytest
```

---

## API Documentation

Interactive API documentation is available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

---

## Models

### Shop
- id (UUID)
- name (str)
- phone (str, optional)
- address (str, optional)
- created_at (datetime)
- updated_at (datetime)

### Order
- id (UUID)
- shop_id (UUID, FK)
- total (Decimal)
- status (str)
- notes (str, optional)
- created_at (datetime)

### OrderItem
- id (UUID)
- order_id (UUID, FK)
- product_id (UUID, FK)
- quantity (int)
- unit_price (Decimal)
- total (Decimal)

### Payment
- id (UUID)
- shop_id (UUID, FK)
- amount (Decimal)
- payment_method (str, optional)
- notes (str, optional)
- created_at (datetime)

### Product
- id (UUID)
- name (str)
- unit_price (Decimal)
- is_active (bool)
- created_at (datetime)

---

## Services

### ShopService
- `get_all_shops()` - List all shops
- `get_shop_by_id(id)` - Get shop by ID
- `search_shops(query)` - Search shops by name
- `create_shop(data)` - Create new shop
- `update_shop(id, data)` - Update shop
- `delete_shop(id)` - Delete shop

### OrderService
- `get_orders_by_shop(shop_id)` - List orders for shop
- `get_order_by_id(id)` - Get order by ID
- `create_order(data)` - Create new order
- `delete_order(id)` - Delete order

### PaymentService
- `get_payments_by_shop(shop_id)` - List payments for shop
- `create_payment(data)` - Create new payment
- `delete_payment(id)` - Delete payment

### BalanceService
- `get_shop_balance(shop_id)` - Calculate shop balance

---

## Error Handling

All errors return a JSON response with a `detail` field:

```json
{
  "detail": "Error message"
}
```

Common status codes:
- 200: Success
- 201: Created
- 400: Bad Request
- 404: Not Found
- 500: Internal Server Error
