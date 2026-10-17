# Complete Ticket Vendor Implementation Plan

> For agentic workers: use superpowers:subagent-driven-development or superpowers:executing-plans. No commits or index changes are authorized.

**Goal:** Complete the existing ticket vendor with purchase, fulfillment, customer access and check-in.
**Architecture:** Preserve the six DAL entities. Separate transaction-critical lifecycle/inventory from cart, presentation and delivery; reuse installed Shopware/Foundation APIs.
**Tech stack:** Shopware 6.7, Foundation 1.7, Doctrine DBAL, Symfony Messenger, native mail/PDF tooling, PHPUnit and administration Node tests.
**Spec:** ../specs/2026-10-16-complete-plugin.md

## Global constraints

No new reservation tables, no hand-written schema migrations, no commits, no real email during tests. All PHP classes use imports at file top. Shared interfaces and file ownership are in the spec.

## Review focus

Concurrent last-seat allocation; client-controlled prices; retries of order/payment/scan requests; customer access across orders; delivery failure after mail handoff. Each owning task tests its respective cases.

## Tasks

1. Inventory and lifecycle: write DAL integration tests for overbooking and event/type mismatch; implement transactional pre/post-write validation and derived counters. Implement order unit allocation, state settlement, expiry and scheduled handling. Verify repeated callbacks and rollback.
2. Commerce: write cart behavior tests for server prices, dates and combined purchase limits. Implement native line item factory and collector/processor; wrap final persistence transactionally with allocation; queue paid tickets and handle state transitions. Verify full checkout rollback.
3. Presentation: implement Foundation-backed public/CMS listing/detail, cart forms, customer tickets and ownership-aware UI, admin customer/order tabs, send/download/revoke/scanner actions. Test criteria/registration/templates and route behavior.
4. Delivery: implement PDF/QR, native templates/data, grouped recipient delivery, Messenger handler and protected download/send actions. Test PDF output, recipient isolation, retry/force semantics and access checks without transport side effects.
5. Integration: import separate XML service files/routes; review source against actual APIs, run complete PHP/admin tests, route/container lint and administration/storefront builds, fix findings and update runtime documentation.

## Status

- [x] Inventory/lifecycle/check-in
- [x] Commerce
- [x] Presentation
- [x] Delivery
- [x] Full integration and verification

## Verification record

- PHPUnit: 87 tests, 1085 assertions, no skips, warnings or deprecations in the complete isolated-database run.
- Administration: 27 Node tests pass using installed Shopware/Foundation components and native Flow Builder behavior.
- Actual concurrent independent processes verify one remaining seat and exactly one redemption; independent connections also verify final eligibility after concurrent deactivation despite a stale DAL snapshot.
- Native HTTP storefront listing/detail/cart-add and unauthenticated scanner access checks pass.
- Production administration Vite and scoped storefront webpack builds pass; 87 PHP files parse and 14 Twig templates validate. Container wiring validates.
- Independent review findings about current eligibility reads and expiry of completed unpaid orders were reproduced/fixed and re-reviewed. No important findings remain in the reviewed scope.
- New mail/SEO data packages installed in the development shop; SEO indexing completed. No real SMTP sends or device-camera checks performed. Worker and payment-provider operation follows docs/runtime.md.
- Foundation fixes: handle an absent storefront channel during data replacement, and use a declared listing result property instead of PHP dynamic properties.
