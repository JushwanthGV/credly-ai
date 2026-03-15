# AGENTS.md - Credly AI Development Guidelines

This file provides guidelines for agentic coding agents operating in this repository.

## Project Overview

**Credly** is a ledger and order management app for a distributor managing local shops. Single-user system for tracking orders, payments, and outstanding balances.

### Core Data Objects
- Shops, Orders, OrderItems, Products, Payments
- Outstanding balance per shop

### Tech Stack
| Layer | Technology |
|-------|------------|
| Frontend | Next.js 14 (App Router), React, Tailwind CSS, shadcn/ui |
| Backend | FastAPI (Python), REST API |
| Database | PostgreSQL |
| ORM | SQLAlchemy with Alembic |
| Testing | Playwright (E2E), Pytest (Backend) |
| Linting | ESLint |
| Formatting | Prettier |

---

## Commands

### Backend

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
alembic upgrade head

# Start server
uvicorn app.main:app --reload

# Run tests
pytest
```

### Frontend

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Run linting
npm run lint
```

### Testing (Playwright)

```bash
# Run all Playwright tests
npx playwright test

# Run a single test file
npx playwright test tests/<filename>.spec.js

# Run tests matching a pattern
npx playwright test --grep "shop"

# Run tests in headed mode (see browser)
npx playwright test --headed

# Run tests with debug mode
npx playwright test --debug

# Open Playwright UI to record/manage tests
npx playwright codegen
```

### Linting & Formatting

```bash
# ESLint
npx eslint .
npx eslint . --fix

# Prettier
npx prettier --write .
npx prettier --check .
```

---

## Code Style Guidelines

### General Principles

- Keep code simple and readable - the target user needs a fast, minimal interface
- Mobile-first design (single-user on phone while visiting shops)
- Large buttons, fast search, minimal navigation

### Python (Backend)

1. **Naming Conventions**
   - Variables/functions: `snake_case` (e.g., `shop_name`, `get_orders`)
   - Classes: `PascalCase` (e.g., `ShopService`)
   - Constants: `UPPER_SNAKE_CASE`

2. **Imports**
   - Group: standard library → external packages → local modules
   - Use absolute imports

3. **Formatting**
   - Follow PEP 8
   - Max line length: 100 characters

### JavaScript/TypeScript (Frontend)

1. **Naming Conventions**
   - Variables/functions: `camelCase`
   - Classes/Components: `PascalCase`
   - File names: `kebab-case`

2. **Imports**
   - Use explicit relative imports for local modules
   - Group: external libraries → internal modules

3. **Formatting (Prettier)**
   - 2-space indentation
   - Single quotes for strings
   - Semicolons required
   - Trailing commas

### Error Handling

- Always wrap async operations in try/catch
- Provide meaningful error messages
- Log errors appropriately

---

## Project Structure

```
credly-ai/
├── frontend/               # Next.js application
│   ├── app/               # App Router pages
│   ├── components/        # React components
│   ├── lib/               # Utilities
│   └── package.json
│
├── backend/                # FastAPI application
│   ├── app/
│   │   ├── api/          # API endpoints
│   │   ├── models/      # SQLAlchemy models
│   │   ├── schemas/     # Pydantic schemas
│   │   └── services/    # Business logic
│   ├── alembic/          # Migrations
│   └── requirements.txt
│
├── tests/                  # E2E tests
├── docs/                   # Project documentation
├── memory/                 # Project context
├── tasks/                  # Task tracking
└── agents/                # Agent roles
```

---

## Agent Roles

See individual agent role files in `agents/` folder:
- `team_lead.md` - Project coordination and planning
- `product_manager.md` - Feature prioritization
- `planner.md` - Task breakdown
- `architect.md` - System design
- `backend_dev.md` - Backend implementation
- `frontend_dev.md` - Frontend implementation
- `code_reviewer.md` - Code review
- `docs_agent.md` - Documentation maintenance
- `qa_agent.md` - Quality assurance
- `playwright_agent.md` - E2E testing
- `git_agent.md` - Version control
- `deploy_agent.md` - Deployment

---

## Development Workflow

1. **Team Lead** creates tasks in `tasks/backlog.md`
2. **Planner** breaks down features into development tasks
3. **Architect** designs system architecture
4. **Backend Dev** implements API endpoints
5. **Frontend Dev** implements UI components
6. **Code Reviewer** reviews code changes
7. **Docs Agent** updates documentation
8. **QA Agent** verifies functionality
9. **Git Agent** commits changes

---

## Documentation

All documentation is maintained in the `docs/` directory:
- `architecture.md` - System architecture
- `api.md` - REST API documentation
- `database_schema.md` - Database schema
- `backend.md` - Backend development guide
- `frontend.md` - Frontend development guide
- `setup_local_dev.md` - Local setup instructions
- `user_guide.md` - End-user documentation

---

## Key UX Requirements

- **Extremely simple interface** - user operates quickly while visiting shops
- Large buttons for touch targets (min 48px)
- Fast search functionality
- Minimal navigation depth (max 2 taps)
- Mobile-friendly layout (primary use case)
