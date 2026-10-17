# Complete Ticket Vendor

The user authorizes the complete plugin, superseding the earlier phase-one exclusions in CODEX.md. Work in the existing plugin, preserve its six-table schema and Foundation conventions, and do not commit or modify the Git index. A separate mobile application is outside this PHP plugin; provide an authenticated scanner API and an administration scanner.

## Behavior

- Public event listing/detail, configurable Foundation CMS elements, purchase forms, account ticket list and protected PDF download. Published active events/types only; respect selling dates and event end.
- Dedicated `moorl_tv_ticket` cart line items reference ticket type IDs. Price/tax/currency and purchase limits come from the server. Recalculation checks availability without reserving. Final order persistence and ticket allocation are atomic. One ticket per position unit; retries do not create duplicates.
- All DAL ticket writes, including manual administration creation, validate type/event consistency and enforce quota under row locks. Pending, valid and redeemed tickets occupy quota; expired/revoked tickets release it. Keep `quantitySold` consistent transactionally. No reservation/issuance tables.
- Confirmed paid orders activate pending tickets and queue delivery. Canceled/refunded orders revoke tickets. Expiry rechecks current payment state, cancels genuinely unpaid orders and releases quota. Late payment may reactivate expired tickets only if capacity is still available; never silently oversell.
- PDF contains readable ticket number, event/type/location and QR token. Group mail by actual recipient and order/sales channel; use native mail templates, message handling, retry tracking and explicit admin resend. Never send real email during development verification.
- Authenticated admin API checks in tokens atomically, scopes to an event, prevents repeated redemption, persists audit results, and treats retried request IDs idempotently. Enforce ACL and customer ownership on download/action routes.
- Administration stays on Foundation modules/helpers, with customer/order ticket lists, actions and scanner. Provide German and English snippets, configuration, lifecycle data and tests.

## Shared interfaces

- `Core/Service/TicketLifecycleService::issueOrder(string $orderId, Context $context): array` returns ticket IDs; line item type is `moorl_tv_ticket`, referencedId is type ID.
- `TicketLifecycleService::settleOrder(string $orderId, Context $context): array` rereads order/payment states, changes eligible statuses and returns newly activated ticket IDs.
- `TicketLifecycleService::expire(Context $context): int` handles due pending orders and standalone pending tickets.
- `Core/Service/TicketDeliveryService::send(array $ticketIds, Context $context, bool $force = false): array` returns a delivery summary; only valid/redeemed tickets can be sent.
- `Core/Service/TicketDocumentService::render(array $ticketIds, Context $context): string` returns PDF bytes; controllers enforce ownership/ACL before invoking it.
- `Core/Message/SendTicketsMessage` carries ticket IDs; its handler invokes delivery. Checkout subscribers queue newly activated IDs.
- Admin actions: `POST /api/_action/moorl-tv/check-in` (`saleId`, `token`, `scanRequestId`, optional `deviceId`); `POST /api/_action/moorl-tv/ticket/{id}/revoke`; `POST .../{id}/send`; `GET .../{id}/download`. Scanner result includes `result`, `ticketNumber`, `checkinId`, and no token.
- Storefront routes: `/tickets`, `/tickets/{saleId}`, `/account/tickets`, `/account/tickets/{id}/download`; purchase uses native cart add with type `moorl_tv_ticket`.

## Implementation ownership

Root owns inventory validation, lifecycle, check-in, runtime configuration, shared service imports and final integration. Commerce task owns cart factory/collector/processor, atomic order integration, payment subscribers and its own commerce.xml. Presentation task owns public/account controllers/views, Foundation CMS integration, administration extensions/actions/scanner and presentation.xml. Delivery task owns PDF/QR, mail templates and data package, message handler, download/send controllers and delivery.xml. Each task writes meaningful failing tests before behavior changes and verifies against installed APIs. Shared main services.xml imports are integrated by root.

## Verification

Use the existing isolated `moorl_tv_demo_1792133308246_test` database. Integration tests must cover idempotency, exact remaining quota, bulk/manual writes, failed order rollback, payment/expiry/cancellation, unauthorized download, check-in replay/concurrency and send retry. Reuse installed PHPUnit, Node tests and Docker Shopware for compilation. Do not execute migration or destructive commands against the normal shop database. Record limitations honestly.
