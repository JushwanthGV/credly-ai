# Architecture - Credly

## Overview

Credly is a ledger and order management application for a distributor managing local shops. Single-user system for tracking orders, payments, and outstanding balances.

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
├── docs/                       # Project documentation
├── memory/                     # Project context (for agents)
├── tasks/                      # Task tracking
└── agents/                     # Agent roles
```

---

## Core Data Objects

- **Shops** - Retail shops that place orders
- **Orders** - Orders placed by shops
- **OrderItems** - Individual items within an order
- **Products** - Product catalog with prices
- **Payments** - Payments made by shops

---

## Balance Calculation

```
outstandingBalance = sum(orders.total) - sum(payments.amount)
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
