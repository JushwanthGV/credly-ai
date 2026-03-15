# Backlog - Phase 1 Development Tasks

## Updated for Next.js + FastAPI + PostgreSQL Stack

---

## Phase 1: Backend Setup

### Infrastructure

- [ ] T001: Set up PostgreSQL database (local or cloud)
- [ ] T002: Create backend project structure (backend/)
- [ ] T003: Set up Python virtual environment and requirements.txt
- [ ] T004: Configure FastAPI with CORS and middleware
- [ ] T005: Set up SQLAlchemy with Alembic

### Database Models

- [ ] T006: Create Shop model and migration
- [ ] T007: Create Product model and migration
- [ ] T008: Create Order model and migration
- [ ] T009: Create OrderItem model and migration
- [ ] T010: Create Payment model and migration

### Backend API

- [ ] T011: Implement Shops API (CRUD + search)
- [ ] T012: Implement Products API (CRUD)
- [ ] T013: Implement Orders API (CRUD)
- [ ] T014: Implement Payments API (CRUD)
- [ ] T015: Implement Balance calculation endpoint

---

## Phase 2: Frontend Setup

### Project Initialization

- [ ] T016: Create Next.js project with Tailwind
- [ ] T017: Install and configure shadcn/ui
- [ ] T018: Set up API client (axios or fetch wrapper)
- [ ] T019: Configure ESLint and Prettier for frontend

### UI Components (shadcn/ui)

- [ ] T020: Set up layout components (Header, Container)
- [ ] T021: Configure Button, Input, Card components
- [ ] T022: Configure Dialog/Modal components
- [ ] T023: Configure Table components

---

## Phase 3: Frontend Features

### Shop Management

- [ ] T024: Implement shop list page with search
- [ ] T025: Implement add/edit shop form
- [ ] T026: Implement shop detail page

### Order Management

- [ ] T027: Implement add order form
- [ ] T028: Implement order list per shop
- [ ] T029: Implement order total calculation

### Payment Tracking

- [ ] T030: Implement add payment form
- [ ] T031: Implement payment history per shop

### Balance Tracking

- [ ] T032: Implement balance display on shop list
- [ ] T033: Implement balance calculation from API

---

## Phase 4: Testing & Polish

### E2E Testing

- [ ] T034: Write Playwright tests for shop management
- [ ] T035: Write Playwright tests for order management
- [ ] T036: Write Playwright tests for payment tracking

### UX Polish

- [ ] T037: Mobile-first responsive styling
- [ ] T038: Large touch targets (min 48px)
- [ ] T039: Loading states and error handling

---

## Task Dependencies

### Backend Phase
- T001-T005: Infrastructure setup
- T006-T010: Database models (depend on T001-T005)
- T011-T015: API endpoints (depend on T006-T010)

### Frontend Phase
- T016-T019: Frontend setup (can parallel with backend)
- T020-T023: UI components (depend on T016-T019)
- T024-T026: Shop Management (depend on T011, T015)
- T027-T029: Order Management (depend on T012, T024-T026)
- T030-T031: Payment Tracking (depend on T013, T024-T026)
- T032-T033: Balance Tracking (depend on T015, T027-T031)

### Final Phase
- T034-T036: Testing (depend on features)
- T037-T039: Polish (final)
