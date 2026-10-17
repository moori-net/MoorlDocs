# Ticket Vendor installation and operation

## Requirements

- Shopware 6.7 with Storefront. Exact package constraints are in `composer.json` (`shopware/core: ~6.7.0`).
- MoorlFoundation 1.7 (`moorl/foundation: ~1.7.0`), installed and activated first.
- PHP/database versions supported by your Shopware installation. Development verification uses PHP 8.2 and Shopware 6.7.14.1.
- Composer packages `dompdf/dompdf: ^3.1` and `tecnickcom/tcpdf: ^6.7.7` for PDF/QR generation. During installation and updates through extension management, Shopware runs Composer to provide these packages. The server needs Composer and access to the package sources. Composer deployments resolve dependencies through their normal deployment process.
- Configured Shopware mail transport, continuously running message consumers and scheduled tasks.
- HTTPS and reliable online connectivity for entrance devices. Browser camera recognition additionally requires `BarcodeDetector` support.

## Installation

Assign a shopping experience containing `moorl-tv-ticket-sale-listing` to a Shopware category and select that category under **Page with events (list)** (`category`) in the plugin configuration. Select the default event layout under **Default event detail CMS page** (`cmsPageId`). A CMS layout assigned directly to an event takes precedence.

1. Install and activate Foundation.
2. Install and activate Ticket Vendor through extension management or your deployment process.
3. For a source deployment, resolve Composer dependencies and build Administration/Storefront through the normal Shopware process. Publish bundled assets when using a distribution package.
4. Clear caches and compile the active theme.
5. Check the Foundation data packages: `data`, `ticket-number`, `ticket-mail`, `seo`, `scanner-role`.
6. Configure workers and test an entire order, payment, PDF, email and check-in workflow.

Activation uses the existing Foundation lifecycle helper. Packages supply media folders, import profiles, number range, mail templates, SEO template and scanner role. Demo data is loaded separately.

## Workers and indexes

Examples from the Shopware project root; run continuously or restart regularly through your production process manager:

```sh
bin/console scheduled-task:register
bin/console scheduled-task:run --time-limit=60
bin/console messenger:consume async low_priority --time-limit=60
bin/console dal:refresh:index --only=moorl_tv_ticket_sale.seo
```

Transport names must match the installation's Messenger configuration. `moorl_tv.expire_tickets` has a 60-second interval and handles payment deadlines and requeuing of undelivered valid tickets. Registering a task alone does not execute it. Restart workers after code updates.

## Extension configuration

**Payment deadline in minutes** defaults to **30**. Choose a value appropriate for your payment methods. After expiry, the task may cancel the entire unpaid order; account for bank transfers and mixed orders. Late payment on an already cancelled order requires manual reconciliation and does not trigger an automatic refund.

The relevant native payment transaction must reach `paid`. Test real provider status transitions; authorisation or partial payment is insufficient.

## Mail, number range and SEO

| Setup | Check |
| --- | --- |
| Transport and sender | Configure Shopware SMTP/sender; use controlled recipients for tests. |
| Ticket delivery template | German/English content; `tickets` exposes `ticketNumber`, `eventName`, `typeName`. PDF is attached separately. |
| Ticket numbers | Native `moorl_tv_ticket` type, default `T-{n}` starting at 10000. Existing numbers/counters are preserved. |
| SEO | `frontend.moorl.tv.detail`, default `tickets/{{ sale.translated.name }}/{{ sale.id }}`. Refresh the index after changes. |

Repeated data installation preserves existing number range configuration, mail templates and SEO templates. `sent` records acceptance by the transport, not confirmed inbox delivery or opening.

## Entrance staff setup

1. Check that **scanner-role** is installed; existing installations can load it through Foundation data management.
2. Create a separate user under **Settings → System → Users & permissions**.
3. Assign **Ticket Vendor – Scanner** and disable administrator access.
4. Remove other roles if the account should only perform entrance duties.
5. Sign in with that account and test **Catalogues → Ticket scanner**.

The role grants `moorl_tv_ticket_sale:read` and `moorl_tv_ticket:scan`. It does not include general ticket modification, sending, revocation, PDF, customer or order access. Shopware's default authenticated Administration privileges still apply. It is not restricted to selected events.

No users, passwords or integration keys are created by the data package. Reimporting does not overwrite an existing role with the package's fixed ID, preserving customisation and assignments. Explicit package removal deletes that role and its assignments. Create separate custom roles first if needed.

**Existing scanners:** The endpoint now requires `moorl_tv_ticket:scan`. Ticket-update/check-in-create privileges alone do not satisfy it. Assign the new role or enable the additional scanner permission and sign in again. General ticket permissions may be removed if no longer needed elsewhere.

## Before opening sales

- Check active event/type, event status `published` and all sales windows.
- Review prices, taxes, currencies, quota and purchase limits.
- Import timestamps in UTC and verify time display with your theme.
- Test registered and guest checkout with the intended payment provider.
- Verify PDFs, recipient assignment and real SMTP delivery.
- Scan one ticket from two devices: only one independent request may be accepted as a new redemption.
- Test camera recognition in the intended browser and manual token entry.

## Demo data

The demo import adds the active **Veranstaltungen** category below the shop navigation and assigns the **Ticket Vendor – Events** CMS layout with its event listing. Visitors enter through the regular category navigation; there is no additional ticket link among the header actions. Removing the demo package removes its category if it has no subcategories. The CMS layout and merchant-created categories are retained.

The optional **standard** Foundation demo has three events, seven ticket types, twelve tickets and three check-in records, including an internal guest list with three valid tickets. Use a test environment; tokens are known examples.

Import itself does not send email. Running workers may subsequently pick up undelivered valid demo tickets. Use a test mail transport and avoid real recipients. Occupancy counters are derived from quota-occupying ticket states.

## Updates and removal

Back up data and configuration before updates. Update Foundation and Ticket Vendor within their supported constraints, deploy dependencies/assets, clear caches and restart workers. Normal plugin updates install newly introduced data packages while preserving configuration according to each package's rules.

Uninstallation with retained user data preserves records. Without retained data, Foundation removes plugin data and package-owned setup. Review archiving, order references and role use beforehand. Do not remove packages or the plugin during active admission.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| No public event | Active, `published`, display window, event end; without end, event start. |
| Purchase rejected | Type/event assignment, sales windows, quota, aggregated purchase limits. |
| Paid order, pending ticket | Relevant primary/latest transaction, native `paid` state, events and server logs. |
| Deadlines not processed | Task registration, running scheduler and Messenger consumers. |
| Email missing | Recipient, template, SMTP, delivery attempts/state, queues and failure transport. |
| Scanner returns 403 | New scan privilege, complete role assignment, fresh login. |
| Camera unavailable | HTTPS, permission, `BarcodeDetector`; use manual input. |
| Event closed | Active and `published`, UTC end time and server clock. |
| Ticket absent from account | Direct customer assignment or order customer and sales channel. Email alone grants no account ownership. |

See the [merchant guide](index.en.md), [scanner API](mobile-app.en.md), [runtime notes](runtime.md) and [schema](schema.md) for details.
