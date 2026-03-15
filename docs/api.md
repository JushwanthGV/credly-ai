# API Documentation - Credly

Base URL: `http://localhost:8000/api/v1`

---

## Shops

### List all shops
```
GET /shops
```

Response:
```json
{
  "shops": [
    {
      "id": "uuid",
      "name": "Shop Name",
      "phone": "1234567890",
      "address": "Address",
      "balance": 1500.00,
      "created_at": "2024-01-01T00:00:00Z",
      "updated_at": "2024-01-01T00:00:00Z"
    }
  ]
}
```

### Get shop by ID
```
GET /shops/{id}
```

### Search shops
```
GET /shops/search?q=query
```

### Create shop
```
POST /shops
```

Request:
```json
{
  "name": "Shop Name",
  "phone": "1234567890",
  "address": "Address (optional)"
}
```

### Update shop
```
PUT /shops/{id}
```

### Delete shop
```
DELETE /shops/{id}
```

---

## Orders

### List orders for shop
```
GET /shops/{shop_id}/orders
```

### Get order by ID
```
GET /orders/{id}
```

### Create order
```
POST /orders
```

Request:
```json
{
  "shop_id": "uuid",
  "items": [
    {
      "product_id": "uuid",
      "quantity": 5
    }
  ],
  "notes": "Optional notes"
}
```

### Delete order
```
DELETE /orders/{id}
```

---

## Payments

### List payments for shop
```
GET /shops/{shop_id}/payments
```

### Create payment
```
POST /payments
```

Request:
```json
{
  "shop_id": "uuid",
  "amount": 500.00,
  "payment_method": "cash",
  "notes": "Optional notes"
}
```

### Delete payment
```
DELETE /payments/{id}
```

---

## Products

### List products
```
GET /products
```

Response:
```json
{
  "products": [
    {
      "id": "uuid",
      "name": "Product Name",
      "unit_price": 10.00,
      "is_active": true,
      "created_at": "2024-01-01T00:00:00Z"
    }
  ]
}
```

### Create product
```
POST /products
```

Request:
```json
{
  "name": "Product Name",
  "unit_price": 10.00
}
```

### Update product
```
PUT /products/{id}
```

---

## Balance

### Get shop balance
```
GET /shops/{id}/balance
```

Response:
```json
{
  "shop_id": "uuid",
  "total_orders": 5000.00,
  "total_payments": 3500.00,
  "balance": 1500.00
}
```

---

## Error Responses

All endpoints may return:

### 400 - Bad Request
```json
{
  "detail": "Error message"
}
```

### 404 - Not Found
```json
{
  "detail": "Resource not found"
}
```

### 500 - Internal Server Error
```json
{
  "detail": "Internal server error"
}
```
