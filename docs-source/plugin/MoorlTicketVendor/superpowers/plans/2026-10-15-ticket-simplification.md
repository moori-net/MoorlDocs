# Ticket simplification implementation plan

> **For agentic workers:** Use superpowers:executing-plans to implement this plan inline.

**Goal:** Persist tickets without separate reservation or issuance entities.

**Architecture:** Six DAL tables remain. Tickets carry optional customer and email recipient, payment expiry and delivery tracking. Orders group tickets through `orderLineItem.orderId`; no duplicated order or batch ID. Schema generation uses the existing MoorlDevTools builder, without plugin migrations.

**Tech Stack:** Installed Shopware 6.7, PHP 8.2, Foundation DAL collections/traits/UniqueKey, PHPUnit, MySQL.

**Spec:** User-approved design in this conversation, incorporated into `CODEX.md` and `docs/schema.md` by task 2.

## Global constraints

- Keep the work in the user's existing uncommitted plugin workspace; no commits, worktree moves or migration restoration.
- Phase 1 remains persistence only: no cart, checkout, payment jobs, mail transport or admin UI.
- Keep token internal and readable; preserve native required reference versions with optional IDs.
- Docker copies must belong to www-data. Change only the isolated test database, never the shop schema.

## Review focus

- Manual tickets with only email, only customer, or no recipient must persist without an order.
- Explicit email takes precedence over customer and stored order-customer email; no recipient returns null.
- Multiple ticket types and orders must group correctly through versioned order positions.
- Pending/expired and delivery states round-trip; unsupported states and invalid emails are rejected by DAL.
- Generated schema retains unique order units and restricts deletion of historical tickets and core references.

### Task 1: Simplify DAL and prove persistence

**Files:** Ticket definition/entity, Sale and Type inverse associations, Checkin uniqueness, plugin table list/services; remove Reservation/Issuance classes. Adapt `tests/Integration/PersistenceTest.php`; replace obsolete migration tests with a test-only schema generator and recipient resolution unit tests.

- [x] Write persistence tests for standalone email tickets, customer tickets, order grouping, pending expiry and delivery state. Run focused tests against old model and observe failure without issuance.
- [x] Remove both entities and all active references; add optional customer, EmailField recipient, expiry, delivery status/timestamp/attempts/error to Ticket. Reuse EntityCustomerTrait. Add recipient resolution from loaded associations, defaults and native Choice flags. Add UniqueKey flags for ticket number, order-unit tuple and scan request.
- [x] Generate six tables with the existing builder in the isolated empty test schema; no application migrations. Run full plugin suite, lint and whitespace checks.

### Task 2: Align documentation and review

**Files:** `CODEX.md`, `docs/schema.md`, historical plan status.

- [x] Rewrite current guidance around the six-table model and external schema creation; document runtime workflows as future work and removal of obsolete migration tests.
- [x] Fresh review of source/tests/schema integrity; resolve significant issues and record exact verification results here.

## Execution record

Pre-flight: Ticket changes are shared with fixtures/schema tests; documentation follows the resulting DAL. No conflicting interfaces. Existing repository has no initial commit, so plan scripts requiring HEAD/worktrees cannot apply; execute inline without staging or committing.

Task 1: complete. RED: standalone fixture rejected by required issuanceId. GREEN: full Docker suite passed, including optional email/customer, order grouping, expiry/delivery tracking. Empty email override RED then GREEN via fallback resolution.
Task 2: complete. CODEX.md/schema.md reflect six tables and explicit no-migrations policy. Fresh independent read-only review identified one important forward RestrictDelete bug. Fixed with three native inverse Core EntityExtensions; focused regression RED then GREEN (2 tests, 9 assertions), full suite GREEN (19 tests, 253 assertions).
Final: Ruling: selected existing schema builder emits DATETIME without fractional precision; accept and document its actual output rather than introduce migrations or change another plugin. Cost: millisecond precision needs external tool configuration if required.
Final: Ruling: runtime capacity/cart/allocation/counters, payment/expiry/cancellation, transport/retry/grouping, token/scanner/redemption/audit sanitization and lifecycle cross-field transitions remain follow-up work under Phase 1 persistence scope. Production schema deployment and legacy-data conversion remain user-controlled through external tools. Cost: persistence alone provides none of these runtime workflows.
Final: minor (deferred): additional non-live order-position grouping/version roundtrip test. Native version definitions and live order associations pass; CMS draft references are covered.
Verification complete: real MoorlDevTools generated all six tables after inverse-extension correction in fresh moorl_tv_simplified_final_20261015_test, exit 0. Complete plugin suite: 19 tests, 253 assertions, exit 0. All 27 PHP files lint clean, whitespace check clean, no migration files restored, no root-owned Docker plugin files. Local unit run passed (3 tests, 4 assertions; integration explicitly skipped without database). No commits or index changes.
