# Documentation and scanner role implementation plan

> Execution: inline using superpowers:executing-plans. The user explicitly authorised starting without confirmation. No commits or changes to existing staged migrations.

**Goal:** Document the shipped Ticket Vendor, describe the future scanner app honestly, and provide a restricted scanner role through Foundation data.

**Architecture:** Preserve the six-table model. Add a `scanner-role` data package and the dedicated `moorl_tv_ticket:scan` action privilege, with native Shopware ACL enforcement and matching Administration navigation. Documentation follows Download Center's German/English `.tpl.md` structure.

**Tech Stack:** PHP 8.2, Shopware 6.7, MoorlFoundation data helpers, Administration JavaScript, Markdown templates, Shopware extension YAML.

**Spec:** User request of 16 October 2026: comprehensive documentation, `mobile-app.tpl.md` for the not-yet-existing app, customer documentation, store description/metadata, and a scanner-only Admin role under `src/Data`.

## Constraints and review focus

- No mobile application is shipped; distinguish actual API/browser scanner from planned mobile behaviour everywhere.
- Role grants event reading and check-in only, not general ticket updates, PDFs, sending, revocation, customer/order access or integration management. Native default Admin login privileges still apply.
- Role creation is repeatable and preserves merchant edits and assignments. No users, passwords or integration keys are created.
- Existing explicit ticket-update/check-in-create permissions must be replaced with the new scan privilege for existing operators; document the change.
- No new schema migrations, live email delivery, external publication or user-data removal.

## Task 1: scanner role and permissions

- [x] Add failing HTTP tests: scanner-only user can read events and check in, retries work, direct ticket changes/send/revoke/PDF/customer/order access are denied; read-only user cannot scan.
- [x] Add failing role import test: Foundation installs one role, repeated import preserves edits/assignments, removal affects only its fixed role ID.
- [x] Implement `Data/ScannerRole/DataScannerRole.php`, register in `data.xml`, use `moorl_tv_ticket:scan` in controller and scanner UI and add native privilege mapping/translations.
- [x] Run focused PHPUnit and Administration tests, then build Administration assets.

## Task 2: documentation and store metadata

- [x] Create German/English `index`, `manual`, `customer`, `mobile-app`, and `store` templates; keep customer instructions short, describe API errors/retries/auth and planned app acceptance criteria precisely.
- [x] Add `.shopware-extension.yml` with actual USPs, features, FAQ, generated document paths and existing/created plugin icon; fill composer descriptions.
- [x] Update runtime/development docs for role installation, scope and compatibility; validate YAML/JSON, links, PHP syntax/container and complete relevant tests.

## Verification record

- Full isolated PHPUnit suite: 89 tests, 1134 assertions, no warnings/deprecations/skips.
- Administration: 28 Node tests and scoped native production build passed; built manifest uses `moorl-ticket-vendor-BMSfc_qL.js`.
- Container lint passed. Store YAML, all referenced store documents/icon, JSON and documentation frontmatter parsed successfully; 22 top-level Markdown files and 53 relative links checked.
- Scanner HTTP tests verify actual authentication, event lookup, atomic redemption/retry, denied CRUD/send/revoke/PDF/customer/order access, and preservation of role edits and assignments on reimport.
- Independent read-only review found one frontmatter quoting issue; templates were quoted, Markdown regenerated and YAML validation passed. No other important findings.
- Initial check-in test exposed native DAL ACL validation; the route now authorises the dedicated scan action before a narrowly scoped system-context transition and audit write. Subsequent denied-write HTTP assertions passed.
- Existing regenerated migrations changed a class name used by `MetaMediaDeletionTest`; only its test import/construction was updated to the actual generated name. No migration source/index changes made by this task.
- Ruling: implement in the existing shared plugin workspace and do not commit or change the index, consistent with the user's established workflow and CODEX.md.
- Normal development database reports Ticket Vendor inactive. No activation or user/integration creation performed. The role is installed automatically on activation/update; its Foundation installation/removal was verified in the isolated database.
- German/English templates plus rendered Markdown and icon are present locally. Administration assets were copied to local plugin output and development public bundle; copied Docker files owned by www-data.
