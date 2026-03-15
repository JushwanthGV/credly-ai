# Local Development Setup - Credly

## Prerequisites

- Node.js 18+
- Python 3.10+
- PostgreSQL 14+
- Git

---

## 1. Clone the Repository

```bash
git clone <repository-url>
cd credly-ai
```

---

## 2. Database Setup

### Install PostgreSQL

**Windows:**
- Download from https://www.postgresql.org/download/windows/
- During installation, set password for postgres user

**macOS:**
```bash
brew install postgresql
brew services start postgresql
```

**Linux (Ubuntu):**
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
```

### Create Database

```bash
psql -U postgres
CREATE DATABASE credly;
\q
```

---

## 3. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env
# Edit .env with your database credentials

# Run migrations
alembic upgrade head

# Start backend server
uvicorn app.main:app --reload
```

The backend API will be available at `http://localhost:8000`

---

## 4. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Copy environment file
cp .env.local.example .env.local
# Edit .env.local with API URL

# Start development server
npm run dev
```

The frontend will be available at `http://localhost:3000`

---

## 5. Running Tests

### Backend Tests
```bash
cd backend
pytest
```

### Frontend E2E Tests
```bash
# Start the development servers first
# Then run Playwright tests
npx playwright test
```

---

## Development Commands

### Backend
```bash
cd backend
uvicorn app.main:app --reload     # Development server
pytest                            # Run tests
alembic upgrade head              # Run migrations
alembic revision --autogenerate   # Create migration
```

### Frontend
```bash
cd frontend
npm run dev                       # Development server
npm run build                     # Production build
npm run lint                      # Run ESLint
npx playwright test               # Run E2E tests
```

---

## Troubleshooting

### PostgreSQL Connection Issues

1. Check PostgreSQL is running:
```bash
# Linux
sudo systemctl status postgresql

# macOS
brew services list
```

2. Verify credentials in `.env`:
```
DATABASE_URL=postgresql://postgres:password@localhost:5432/credly
```

### Frontend API Connection

Ensure the backend is running and the API URL is correct in `.env.local`:
```
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
```

### Port Already in Use

If ports 3000 or 8000 are in use, specify different ports:
```bash
# Backend
uvicorn app.main:app --reload --port 8001

# Frontend
npm run dev -- -p 3001
```

---

## Project Structure Overview

```
credly-ai/
├── frontend/          # Next.js app (port 3000)
├── backend/          # FastAPI app (port 8000)
├── tests/            # Playwright tests
├── docs/             # Documentation
├── memory/           # Project context
├── tasks/           # Task tracking
└── agents/          # Agent roles
```
