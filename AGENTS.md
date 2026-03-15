# AGENTS.md - Credly AI Development Guidelines

This file provides guidelines for agentic coding agents operating in this repository.

## Project Overview

**Credly** is a ledger and order management app for a distributor managing local shops. Single-user system for tracking orders, payments, and outstanding balances.

### Core Data Objects
- Shops, Orders, Products, Transactions
- Outstanding balance per shop

### Tech Stack
- **Testing**: Playwright (browser automation/E2E tests)
- **Linting**: ESLint
- **Formatting**: Prettier
- **Module System**: CommonJS

---

## Commands

### Running Tests

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

### Linting

```bash
# Run ESLint on all files
npx eslint .

# Fix auto-fixable issues
npx eslint . --fix
```

### Formatting

```bash
# Format all files with Prettier
npx prettier --write .

# Check formatting without writing
npx prettier --check .
```

### Development

```bash
# Start development server (when available)
npm run dev

# Build project (when available)
npm run build
```

---

## Code Style Guidelines

### General Principles

- Keep code simple and readable - the target user needs a fast, minimal interface
- Mobile-first design (single-user on phone while visiting shops)
- Large buttons, fast search, minimal navigation

### JavaScript/TypeScript Conventions

1. **Naming Conventions**
   - Variables/functions: `camelCase` (e.g., `shopName`, `getOrders`)
   - Classes/Components: `PascalCase` (e.g., `ShopCard`, `OrderForm`)
   - Constants: `UPPER_SNAKE_CASE` (e.g., `MAX_RETRY_COUNT`)
   - File names: `kebab-case` (e.g., `shop-card.js`, `order-form.spec.js`)

2. **Imports**
   - Use explicit relative imports for local modules
   - Group imports: external libraries → internal modules → styles
   - Avoid wildcard imports (`* as`)

   ```javascript
   // Good
   const { chromium } = require('playwright');
   const { Shop } = require('../models');
   const styles = require('./shop-card.css');
   ```

3. **Formatting (Prettier)**
   - Use 2-space indentation
   - Single quotes for strings
   - Semicolons required
   - Max line length: 100 characters
   - Trailing commas in multiline objects/arrays

4. **Types**
   - Use JSDoc comments for complex types if TypeScript not available
   - Prefer explicit types for function parameters and return values

5. **Error Handling**
   - Always wrap async operations in try/catch
   - Provide meaningful error messages
   - Log errors appropriately for debugging

   ```javascript
   // Good
   async function createOrder(shopId, items) {
     try {
       const order = await Order.create({ shopId, items });
       return order;
     } catch (error) {
       console.error('Failed to create order:', error);
       throw new Error('Could not create order. Please try again.');
     }
   }
   ```

6. **Testing (Playwright)**
   - Test files: `*.spec.js` or `*.test.js` in `tests/` folder
   - Use descriptive test names: `test('should create order for shop')`
   - Use meaningful selectors (data-testid, aria-labels)
   - Clean up test data after each test

   ```javascript
   test('should display shop balance', async ({ page }) => {
     await page.goto('/shops/1');
     await expect(page.locator('[data-testid="balance"]')).toBeVisible();
   });
   ```

7. **Code Organization**
   - Keep files under 200 lines
   - Single responsibility per module
   - Extract reusable logic into utilities
   - Group related functionality in folders

---

## Project Structure

```
credly-ai/
├── agents/              # Agent role definitions
├── memory/              # Project context and decisions
├── tasks/               # Task tracking
├── tests/               # Playwright E2E tests
├── src/                 # Source code (when created)
├── package.json
├── .eslintrc.json       # ESLint config (create if needed)
├── .prettierrc          # Prettier config (create if needed)
└── playwright.config.js # Playwright config (create if needed)
```

---

## Agent Roles

See individual agent role files in `agents/` folder:
- `team_lead.md`
- `product_manager.md`
- `planner.md`
- `architect.md`
- `backend_dev.md`
- `frontend_dev.md`
- `code_reviewer.md`
- `qa_agent.md`
- `playwright_agent.md`
- `git_agent.md`
- `deploy_agent.md`

---

## Key UX Requirements

- **Extremely simple interface** - user operates quickly while visiting shops
- Large buttons for touch targets
- Fast search functionality
- Minimal navigation depth
- Mobile-friendly layout (primary use case)
