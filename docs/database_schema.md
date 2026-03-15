# Database Schema - Credly

Database: PostgreSQL

---

## Shops Table

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | UUID | PRIMARY KEY | Auto-generated |
| name | VARCHAR(255) | NOT NULL | Shop name |
| phone | VARCHAR(20) | NULLABLE | Phone number |
| address | TEXT | NULLABLE | Shop address |
| created_at | TIMESTAMP | DEFAULT NOW() | Creation timestamp |
| updated_at | TIMESTAMP | DEFAULT NOW() | Last update timestamp |

---

## Products Table

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | UUID | PRIMARY KEY | Auto-generated |
| name | VARCHAR(255) | NOT NULL | Product name |
| unit_price | DECIMAL(10,2) | NOT NULL | Price per unit |
| is_active | BOOLEAN | DEFAULT TRUE | Whether product is available |
| created_at | TIMESTAMP | DEFAULT NOW() | Creation timestamp |

---

## Orders Table

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | UUID | PRIMARY KEY | Auto-generated |
| shop_id | UUID | FOREIGN KEY (shops.id) | Reference to shop |
| total | DECIMAL(10,2) | NOT NULL | Order total amount |
| status | VARCHAR(20) | DEFAULT 'pending' | Order status |
| notes | TEXT | NULLABLE | Optional notes |
| created_at | TIMESTAMP | DEFAULT NOW() | Order creation timestamp |

---

## OrderItems Table

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | UUID | PRIMARY KEY | Auto-generated |
| order_id | UUID | FOREIGN KEY (orders.id) | Reference to order |
| product_id | UUID | FOREIGN KEY (products.id) | Reference to product |
| quantity | INTEGER | NOT NULL | Quantity ordered |
| unit_price | DECIMAL(10,2) | NOT NULL | Price at time of order |
| total | DECIMAL(10,2) | NOT NULL | Line item total |

---

## Payments Table

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | UUID | PRIMARY KEY | Auto-generated |
| shop_id | UUID | FOREIGN KEY (shops.id) | Reference to shop |
| amount | DECIMAL(10,2) | NOT NULL | Payment amount |
| payment_method | VARCHAR(50) | NULLABLE | cash, card, bank_transfer, etc. |
| notes | TEXT | NULLABLE | Optional notes |
| created_at | TIMESTAMP | DEFAULT NOW() | Payment timestamp |

---

## Entity Relationships

```
Shops (1) ──────< Orders (many)
Shops (1) ──────< Payments (many)
Orders (1) ─────< OrderItems (many)
Products (1) ───< OrderItems (many)
```

---

## Balance Calculation

```sql
SELECT 
  COALESCE(SUM(o.total), 0) - COALESCE(SUM(p.amount), 0) as balance
FROM shops s
LEFT JOIN orders o ON s.id = o.shop_id
LEFT JOIN payments p ON s.id = p.shop_id
WHERE s.id = :shop_id
```

---

## Indexes

- `idx_orders_shop_id` ON orders(shop_id)
- `idx_payments_shop_id` ON payments(shop_id)
- `idx_order_items_order_id` ON order_items(order_id)
- `idx_shops_name` ON shops(name) - for search

---

## Migrations

Database migrations are managed with Alembic.

Run migrations:
```bash
cd backend
alembic upgrade head
```

Create new migration:
```bash
alembic revision --autogenerate -m "description"
```
