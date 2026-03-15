# Implementation Plan - Phase 1

## Sprint 1: Setup & Infrastructure

### T001: Create project folder structure
```
mkdir -p src/models src/services src/utils src/styles tests
```

### T002: Playwright Config
- Create `playwright.config.js`
- Configure test directory: `tests/`
- Set up base URL for local file testing
- Enable headed mode for debugging

### T003: ESLint Config
- Create `.eslintrc.json`
- Use ES6+ rules
- Enable `no-unused-vars` warning
- Configure for CommonJS (since package.json has "type": "commonjs")

### T004: Prettier Config
- Create `.prettierrc`
- Set: singleQuote: true, semi: true, tabWidth: 2, trailingComma: 'es5'

### T005: Base HTML with mobile viewport
- Create `index.html`
- Add meta viewport tag
- Add minimal CSS for mobile
- Add placeholder content

---

## Data Layer Implementation Order (T006-T010)

### T006-T009: Data Models
Create in `src/models/`:
- `Shop.js` - Shop model with validation
- `Order.js` - Order model with items array
- `Payment.js` - Payment model
- `Product.js` - Predefined product catalog

### T010: Data Service
Create `src/services/storage.js`:
- LocalStorage wrapper with CRUD operations
- Data validation on save/load
- Event system for data changes

---

## Feature Implementation Order

1. **Shop Management** (T011-T014)
   - Shop list view with search
   - Add shop modal
   - Shop detail view

2. **Order Management** (T015-T017)
   - Add order form
   - Order history display
   - Total calculation

3. **Payment Tracking** (T018-T019)
   - Add payment form
   - Payment history display

4. **Balance Tracking** (T020-T021)
   - Balance display component
   - Auto-calculation logic

---

## Testing Strategy

- E2E tests with Playwright
- Test critical user flows:
  1. Add shop → view in list → search
  2. Add order → verify balance increase
  3. Add payment → verify balance decrease
  4. Full flow: add shop → add order → add payment → check balance

---

## Next Steps

1. Execute Setup tasks (T001-T005)
2. Implement Data Layer (T006-T010)
3. Implement Shop Management features
4. Implement Order Management features
5. Implement Payment Tracking
6. Implement Balance Tracking
7. Add tests
8. Polish UI
