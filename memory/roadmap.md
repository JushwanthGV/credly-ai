# Product Roadmap — Credly

## Phase 1: Shop Ledger MVP

### Goal
Build a simple mobile-friendly system that allows the distributor to track shops, record orders, and track outstanding balances.

### User Stories

1. **As a distributor, I want to add new shops so I can track their orders and payments.**
   - Add shop with name and phone number
   - View list of all shops
   - Search shops by name or phone

2. **As a distributor, I want to see how much each shop owes so I can track outstanding balances.**
   - View shop balance on shop list
   - View detailed balance breakdown on shop detail page

3. **As a distributor, I want to record orders for a shop so I can track what they owe.**
   - Add order with products and quantities
   - Auto-calculate order total
   - Add order to shop's outstanding balance

4. **As a distributor, I want to record payments from shops so I can reduce their balance.**
   - Record payment amount
   - Auto-reduce shop's outstanding balance
   - View payment history

### Features

#### 1. Shop Management
- Add new shop (name required, phone optional)
- Search shops by name (real-time filter)
- View shop list with balance
- View shop details

#### 2. Balance Tracking
- Track outstanding balance per shop
- Auto-update balance on order/payment
- Show balance prominently on shop card

#### 3. Order Management
- Add order for a shop
- Select products from predefined list
- Enter quantity
- Auto-calculate total
- Save order with timestamp

#### 4. Payment Tracking
- Record payment for a shop
- Enter payment amount
- Auto-reduce outstanding balance
- Save payment with timestamp

### Success Criteria

The user can:
- [ ] Open the app on phone
- [ ] Add a new shop
- [ ] Search and find a shop
- [ ] Add an order for a shop
- [ ] Record a payment for a shop
- [ ] See the current balance for each shop
- [ ] View order history for a shop
- [ ] View payment history for a shop

### Technical Approach

- Single HTML file with vanilla JS (simplest deployment)
- LocalStorage for data persistence
- Mobile-first responsive design
- Large touch targets (min 48px)

---

## Phase 2 (Future)

- Product catalog management
- Import shops from Khatabook PDF
- Shop location tracking

## Phase 3 (Future)

- Delivery route planning
- WhatsApp invoice sending
- Shop order analytics
