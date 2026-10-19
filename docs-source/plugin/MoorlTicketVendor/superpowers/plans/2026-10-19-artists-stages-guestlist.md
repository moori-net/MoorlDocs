# Artists, Stages, Guestlist Implementation Plan

> For agentic workers: use superpowers:subagent-driven-development. No commits or index changes. User explicitly authorized implementation on 19.10.2026.

**Goal:** Implement the approved event-program/guestlist extension and replace persisted ticket order-position references with direct order references.
**Architecture:** Reuse Shopware DAL, Foundation modules, existing inventory, mail, PDF and scanner infrastructure. Three bounded implementation packages share explicit interfaces; root integrates and verifies the combined result.
**Tech Stack:** Installed Shopware 6.7/Foundation, PHP, Doctrine DBAL, Twig, Symfony Messenger, PHPUnit, Node administration tests.
**Spec:** ../specs/2026-10-19-artists-stages-guestlist-design.md

## Global Constraints

- No hand-written PHP migrations, commits, index changes, production-schema writes or real emails.
- Preserve all pre-existing staged/unstaged changes; work in the supplied plugin checkout on branch 6.7.
- bookingEnabled means public booking offer only; existing shop contact form or optional external bookingContact. No booking workflow.
- Definition-driven external schema generation, Foundation field/relation/module helpers and existing full FK naming.
- Full timestamps remain UTC with an event IANA timezone; timetable startAt/endAt use optional HH:mm strings and the core time picker without date validation (user simplification, 19.10.2026). Private fields excluded from public output.

## Review Focus

Direct-order retry/ownership/version invariants; concurrent last-seat allocation across categories; private guestlist controls through arbitrary DAL writes; website visibility across CMS/search/SEO; customerless ticket channel/language and retry recovery.

## Task 1: Direct order reference and persistent delivery context

**Files:** Ticket definition/entity/access; OrderLineItemExtension -> OrderExtension; TicketLifecycleService, inventory/person-alization/checkin/delivery/document/deeplink services; account controller; Flow action; ticket admin filters; corresponding existing tests and a new direct-order test.
**Interfaces:** Ticket has nullable orderId, native required orderVersionId, order association; unitIndex unique within order/version/type. Nullable salesChannelId/languageId are standalone-ticket context. Existing public service signatures stay unchanged.

- [x] Write/run failing behavior tests: aggregated same-type positions create exactly five tickets; repeated allocation returns same IDs after revoke/expiry; order fallback and explicit standalone language/channel resolve correctly.
- [x] Replace stored line references end-to-end; aggregate allocation; reject changed allocation shape; preserve transactional rollback and ownership recheck.
- [x] Update existing affected fixtures/tests to real OrderEntity relationships; verify targeted PHPUnit and Node tests, PHP syntax.

## Task 2: Artists, stages and event programme

**Files:** new Content/Artist, Stage, Performance; new program validation/loader, program.xml, administration program registration, public program/booking templates and controller/CMS integration. Owns TicketSale definition/entity/translation files and event listing/SEO visibility changes.
**Interfaces:** Sale adds listed=true, lineupPublished=false, timetablePublished=false, capacity nullable; guestlistEnabled=false, guestlistOpenAt/guestlistCloseAt nullable, guestlistTicketTypeId nullable, guestlistSalesChannelId nullable, hidden guestlistAccessKey nullable, guestlistConfig nullable JSON; translated guestlistIntroduction/guestlistRules. Sale associations stages, performances, guestlistEntries. Artist has public bookingEnabled and bookingContact, internal feeAmount/bookingNote without a currency relation. Guestlist entries record their decision user through userId/user (ON DELETE SET NULL). Stage/performance have no active flag.

- [x] Write/run failing tests for multiple sets, foreign-stage rejection, public projection (no fee/note leak), booking offer/contact behavior and listed filtering.
- [x] Implement five definitions, entities/collections/translations, DAL validation and public programme/booking output using Foundation patterns.
- [x] Add event fields and publication controls, event-filtered editing and conflict hints. Bind booking CTA to the existing configured contact CMS page or external email/URL.
- [x] Verify focused PHP/Node tests and syntax; report exact exported registration function and service imports to root.

## Task 3: Secret guestlist and atomic issuance

**Files:** new Content/GuestlistEntry; guest services, storefront/admin controllers, guestlist.xml, guest registration/templates and focused tests. Does not edit shared Sale/Ticket definitions, root services or main.js.
**Interfaces:** Sale fields from Task 2. Ticket fields from Task 1. GuestlistEntry fields exactly as spec, decision nullable rejected/cancelled, unique submissionId and ticketId; event uses property sale. Public schema-independent validation/service behavior can be tested locally before integration.

- [x] Write/run failing tests for request validation, same-request retry, shared-email guests, code/period/channel checks and issue idempotency.
- [x] Implement fixed form, secret-link copy/rotate actions, defensive server validation, rate/honeypot/origin controls, private responses and snapshots.
- [x] Implement locked issuance/cancel/decline; create existing valid ticket via DAL and queue existing SendTicketsMessage after commit; preserve recovery on queue failure.
- [x] Foundation admin event grid and per-entry/bulk actions with independent result; no booking or payment subsystem.
- [x] Verify targeted tests and syntax; report service interfaces and import/register names to root.

## Task 4: Root integration, event capacity and data tooling

**Files:** main services.xml and administration main.js/snippets, PLUGIN_TABLES, schema helper, inventory subscriber/purchase validator after Task 1, data/demo/import-export packages, schema/runtime/CODEX documentation, backfill tooling and combined integration tests.
**Interfaces:** Import program.xml/guestlist.xml and new registrations; full twelve-table dependency order. capacity is checked under the existing sale row lock across pending/valid/redeemed tickets of every category; no new sold counter. Order backfill is an explicit guarded external-tool operation, never a lifecycle production migration.

- [x] Add/run failing cross-category event-capacity and integrated DAL/entity tests in fresh isolated moorl_tv_*_test DB.
- [x] Integrate registrations, ACL/snippets, module fields, definitions and inverse core-reference protections.
- [x] Implement capacity consistently in DAL and purchase visibility/limits; update demo/import profiles and document safe old-order backfill.
- [x] Verify full PHPUnit and administration suites, schema builder, container/Twig and scoped production assets. Docker copy ownership remains www-data:www-data.

## Task 5: Independent review and final verification

- [x] Review package implementations against spec and security/concurrency failure modes; fix reproduced important defects with tests.
- [x] Run full integrated checks once all fixes are present and update documentation with actual evidence and any environment limitations.
- [x] Report implemented behavior and external schema/backfill deployment steps; no production DB updates, commits or mail sends.

## Final verification — 19.10.2026

- Twelve tables generated from real MoorlDevTools definitions in moorl_tv_extension_20261019_test; no ordinary shop schema/data migrated.
- Full Docker PHPUnit: 203 tests, 2014 assertions, no failures/errors/skips; seven pre-existing Foundation ProductListingResult dynamic-property deprecations remain.
- Administration Node: 55 tests pass. PHP syntax, container wiring, 28 Twig templates and scoped native administration/storefront production builds pass.
- Independent task reviews reproduced/fixed scanner lock inversion, localized mail labels, guest export scoping and native Admin serialization; independent whole-change final review found no remaining Important/Critical defect.
- Existing order-reference backfill is provided as a default read-only console command; --apply is an explicit later operator operation after external schema staging.
- No commits, index changes, production schema operations, real email sends or separate booking process.
