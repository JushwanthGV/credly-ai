# Architecture - Credly

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Next.js 14 (App Router), React, Tailwind CSS, shadcn/ui |
| Backend | FastAPI (Python), REST API |
| Database | PostgreSQL |
| ORM | SQLAlchemy with Alembic migrations |
| Testing | Playwright (E2E), Pytest (Backend) |

---

## System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Frontend (Next.js)                   │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐  │
│  │   Pages     │  │ Components  │  │   API Client   │  │
│  │  /app/      │  │  shadcn/ui  │  │  (fetch/axios) │  │
│  └─────────────┘  └─────────────┘  └─────────────────┘  │
└─────────────────────────────────────────────────────────┘
                           │
                           ▼ HTTP/REST
┌─────────────────────────────────────────────────────────┐
│                    Backend (FastAPI)                     │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐  │
│  │   Routes    │  │  Services   │  │   Repositories │  │
│  │  /api/v1/    │  │   Business  │  │   (SQLAlchemy)  │  │
│  └─────────────┘  └─────────────┘  └─────────────────┘  │
└─────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│                  Database (PostgreSQL)                   │
│    Shops │ Orders │ OrderItems │ Payments │ Products    │
└─────────────────────────────────────────────────────────┘
```

---

## Database Schema

### Shops Table
| Column | Type | Constraints |
|--------|------|-------------|
| id | UUID | PRIMARY KEY |
| name | VARCHAR(255) | NOT NULL |
| phone | VARCHAR(20) | NULLABLE |
| address | TEXT | NULLABLE |
| created_at | TIMESTAMP | DEFAULT NOW() |
| updated_at | TIMESTAMP | DEFAULT NOW() |

### Products Table
| Column | Type | Constraints |
|--------|------|-------------|
| id | UUID | PRIMARY KEY |
| name | VARCHAR(255) | NOT NULL |
| unit_price | DECIMAL(10,2) | NOT NULL |
| is_active | BOOLEAN | DEFAULT TRUE |
| created_at | TIMESTAMP | DEFAULT NOW() |

### Orders Table
| Column | Type | Constraints |
|--------|------|-------------|
| id | UUID | PRIMARY KEY |
| shop_id | UUID | FOREIGN KEY (shops.id) |
| total | DECIMAL(10,2) | NOT NULL |
| status | VARCHAR(20) | DEFAULT 'pending' |
| notes | TEXT | NULLABLE |
| created_at | TIMESTAMP | DEFAULT NOW() |

### OrderItems Table
| Column | Type | Constraints |
|--------|------|-------------|
| id | UUID | PRIMARY KEY |
| order_id | UUID | FOREIGN KEY (orders.id) |
| product_id | UUID | FOREIGN KEY (products.id) |
| quantity | INTEGER | NOT NULL |
| unit_price | DECIMAL(10,2) | NOT NULL |
| total | DECIMAL(10,2) | NOT NULL |

### Payments Table
| Column | Type | Constraints |
|--------|------|-------------|
| id | UUID | PRIMARY KEY |
| shop_id | UUID | FOREIGN KEY (shops.id) |
| amount | DECIMAL(10,2) | NOT NULL |
| payment_method | VARCHAR(50) | NULLABLE |
| notes | TEXT | NULLABLE |
| created_at | TIMESTAMP | DEFAULT NOW() |

---

## API Endpoints

### Shops
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/v1/shops | List all shops |
| GET | /api/v1/shops/{id} | Get shop by ID |
| GET | /api/v1/shops/search?q= | Search shops |
| POST | /api/v1/shops | Create shop |
| PUT | /api/v1/shops/{id} | Update shop |
| DELETE | /api/v1/shops/{id} | Delete shop |

### Orders
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/v1/shops/{shop_id}/orders | List orders for shop |
| GET | /api/v1/orders/{id} | Get order by ID |
| POST | /api/v1/orders | Create order |
| DELETE | /api/v1/orders/{id} | Delete order |

### Payments
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/v1/shops/{shop_id}/payments | List payments for shop |
| POST | /api/v1/payments | Create payment |
| DELETE | /api/v1/payments/{id} | Delete payment |

### Products
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/v1/products | List products |
| POST | /api/v1/products | Create product |
| PUT | /api/v1/products/{id} | Update product |

### Balance
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/v1/shops/{id}/balance | Get shop balance |

---

## Project Structure

```
credly-ai/
├── frontend/                    # Next.js application
│   ├── app/                    # App Router pages
│   │   ├── page.tsx           # Shop list (home)
│   │   ├── shops/
│   │   │   ├── [id]/         # Shop detail page
│   │   │   └── new/          # New shop page
│   │   ├── orders/
│   │   └── payments/
│   ├── components/             # React components
│   │   ├── ui/               # shadcn/ui components
│   │   └── shops/            # Feature components
│   ├── lib/                   # Utilities
│   │   ├── api.ts            # API client
│   │   └── utils.ts
│   ├── tailwind.config.ts
│   └── package.json
│
├── backend/                    # FastAPI application
│   ├── app/
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── endpoints/
│   │   │       └── router.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── database.py
│   │   ├── models/           # SQLAlchemy models
│   │   ├── schemas/          # Pydantic schemas
│   │   ├── services/         # Business logic
│   │   └── main.py
│   ├── alembic/               # Database migrations
│   └── requirements.txt
│
├── tests/                      # E2E tests
│   └── *.spec.js
│
├── memory/                     # Project documentation
├── tasks/                      # Task tracking
└── agents/                     # Agent roles
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

## UX Guidelines

- Mobile-first design (min-width: 320px)
- Large touch targets: minimum 48px height
- Single-handed operation
- Maximum 2 taps to complete any action
- Clear visual hierarchy
- Prominent balance display (green for low, red for high)
- Use shadcn/ui components for consistency

---

## Development Phases

1. **Setup**: Backend/Frontend project initialization
2. **Database**: PostgreSQL setup, Alembic migrations
3. **Backend API**: CRUD for all entities
4. **Frontend**: UI components and pages
5. **Integration**: Connect frontend to backend
6. **Testing**: E2E tests with Playwright
