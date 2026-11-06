# Customer anonymization implementation plan

**Goal:** Add a disabled-by-default Shopware switch in step 5 to replace personal customer data, including customer snapshots and addresses in orders, in the destination database.

**Architecture:** StepConfigureDestinationShop delegates to a focused CustomerDataAnonymizer using only its destination connection. Fixed bulk updates run in one transaction. IDs, foreign keys, order amounts and history remain intact. Stable ID-derived identifiers and `.invalid` emails permit repeat execution. Remove birthdays, companies, VAT IDs, custom fields, IP addresses and existing credentials from the covered customer records as well as names/address/contact details. Clear customer recovery tokens.

**Scope:** customer, customer_address, order_customer, order_address and customer_recovery. This option does not claim to remove personal data in documents, logs, reviews, newsletters or third-party/plugin tables.

## Tasks

- [x] Write failing PHPUnit tests for default configuration, opt-in wiring, real SQL replacement, preserved relationships, repeat execution and rollback.
- [x] Implement the helper and destination-step switch; add German/English labels and a precise help text.
- [x] Run PHP and administration tests, syntax/JSON checks and independent review. Exercise SQL with temporary fixture tables only, never real customer records.

## Review focus

Only the target connection is written; disabled or absent configuration must not touch personal data. Include guest/deleted-customer orders and all order versions. Destination errors must stop the step and roll back. Existing records/configurations retain the disabled default.

## Verification

- Initial targeted PHPUnit run: four expected failures before implementation.
- Full PHPUnit suite in isolated Docker copy: 96 tests, 305 assertions, no skips. Local run also passed, with the opt-in MySQL test skipped.
- MySQL fixtures use connection-local temporary tables only. Covered repeated execution, linked and unlinked orders, duplicate IDs across versions, preserved foreign keys, and actual rollback after a later statement fails.
- Plugin Node tests: 61 passed.
- PHP syntax checks and `git diff --check` passed; snippets parsed as JSON and the plugin production administration build passed in the isolated Docker copy.
- Independent review: no actionable findings within the documented scope.
- No staging process was run against real customer records. Build/test files live under `/tmp/moorl-staging-anonymization-verify` in the container; live plugin sources and databases were not deployed or anonymized.
