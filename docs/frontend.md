# Frontend Documentation - Credly

## Overview

Next.js 14 application with Tailwind CSS and shadcn/ui for the Credly ledger and order management system.

---

## Tech Stack

- **Framework**: Next.js 14 (App Router)
- **Styling**: Tailwind CSS
- **Components**: shadcn/ui (Radix UI)
- **HTTP Client**: fetch / axios
- **Language**: TypeScript

---

## Project Structure

```
frontend/
├── app/
│   ├── layout.tsx          # Root layout
│   ├── page.tsx           # Shop list (home)
│   ├── shops/
│   │   ├── [id]/
│   │   │   └── page.tsx  # Shop detail page
│   │   └── new/
│   │       └── page.tsx  # New shop page
│   ├── orders/
│   │   └── page.tsx
│   └── payments/
│       └── page.tsx
├── components/
│   ├── ui/                # shadcn/ui components
│   │   ├── button.tsx
│   │   ├── input.tsx
│   │   ├── card.tsx
│   │   ├── dialog.tsx
│   │   ├── table.tsx
│   │   └── ...
│   ├── shops/
│   │   ├── shop-list.tsx
│   │   ├── shop-card.tsx
│   │   ├── shop-form.tsx
│   │   └── shop-detail.tsx
│   ├── orders/
│   │   ├── order-form.tsx
│   │   └── order-list.tsx
│   └── payments/
│       ├── payment-form.tsx
│       └── payment-list.tsx
├── lib/
│   ├── api.ts            # API client
│   └── utils.ts          # Utility functions
├── tailwind.config.ts
└── package.json
```

---

## Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start development server:
```bash
npm run dev
```

The app will be available at `http://localhost:3000`

---

## Components

### shadcn/ui Components

Install additional components as needed:
```bash
npx shadcn-ui@latest add button
npx shadcn-ui@latest add input
npx shadcn-ui@latest add card
```

---

## API Client

The API client is defined in `lib/api.ts`:

```typescript
const API_BASE = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1';

export const api = {
  shops: {
    list: () => fetch(`${API_BASE}/shops`),
    get: (id: string) => fetch(`${API_BASE}/shops/${id}`),
    create: (data: ShopInput) => fetch(`${API_BASE}/shops`, { method: 'POST', body: JSON.stringify(data) }),
    // ... etc
  },
  // ... other endpoints
};
```

---

## Pages

### Shop List (Home)
- `/` - Main page showing all shops with balances
- Search functionality
- FAB to add new shop

### Shop Detail
- `/shops/[id]` - Shop details with order and payment history

### Add Shop
- `/shops/new` - Form to create new shop

---

## UX Guidelines

- Mobile-first design (min-width: 320px)
- Large touch targets: minimum 48px height
- Single-handed operation
- Maximum 2 taps to complete any action
- Clear visual hierarchy
- Prominent balance display

---

## Environment Variables

Create `.env.local`:
```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
```

---

## Building for Production

```bash
npm run build
npm start
```
