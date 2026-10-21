**Important note:** You need the Foundation Plugin, which is available free of charge: [Foundation](https://store.shopware.com/en/search?search=MoorlFoundation)


## Plugin Demo

A storefront demo is available for testing this plugin. The plugin can be tested at the following link:

- [https://demo-sw67.moori.net/MoorlTicketVendor](https://demo-sw67.moori.net/MoorlTicketVendor)


## Sell event tickets directly in Shopware

Ticket Vendor lets you manage events and sell admission through your existing Shopware shop. Concerts, workshops, seminars and community events receive dedicated pages, ticket categories and defined quotas. Sales use the native cart and checkout without requiring additional Shopware products.

From purchase to entrance, the workflow stays in your shop: confirmed full payment activates individual tickets, delivered as PDFs with QR codes and made available to authorised customers in their accounts. An Administration browser scanner validates codes at the entrance.

## Categories, prices and quotas

Offer Standard, VIP, reduced-price and other ticket categories. Each type has its own prices, taxes, quota and minimum/maximum purchase quantities. Configure sales windows separately from event times.

Final quota checks happen in the same transaction as order persistence, accounting for competing purchases. Each purchased unit receives an individual ticket, its own native Shopware number-range number and a separate QR code.

## Group tickets and service packages

Group admission and drinks/food packages offer configurable redemptions in a fixed area on one QR code. Each deliberate scan uses one unit and shows progress. Group tickets occupy weighted person places; service packages use no event admission capacity.

## Payment activation and traceable states

Order tickets initially wait for confirmed payment. The native `paid` state activates them and queues automatic delivery. Payment deadlines, expiry, cancellation, full refunds and chargebacks affect validity. Pending tickets can expire after the configured deadline and release quota.

Administration shows whether tickets are valid, redeemed, expired or revoked, separately from pending, accepted or failed delivery. Late payment on already cancelled orders requires manual reconciliation.

## PDF tickets and customer accounts

PDF attachments contain event information, ticket category, number and QR code. Signed-in customers can also download their authorised tickets from their accounts. Guest purchasers receive PDFs and personal ticket links by email. Each link allows them to personalise and download that individual ticket without a customer login.

German/English email templates, delivery tracking, retries and explicit resending support daily operations. The **Send tickets** Flow Builder action additionally queues tickets from an order context.

## Invitations and internal guest lists

Create tickets directly within an event, without an order or customer account. A free, publicly hidden type with its own quota supports invitations and guest-list tickets. They use the same PDFs, codes and admission checks as purchased tickets.

A private registration form collects names, email, optional phone numbers and voluntary support choices. Confirmation links, CSV import and manual ticket issuance support administration. Registrations do not reserve places; capacity is occupied when a ticket is issued.

## Admission with a dedicated scanner role

The integrated Administration scanner supports camera QR recognition in compatible browsers and manual token entry. Online validation checks against the shop. Concurrent scans are handled atomically, previously used codes are recognised and scan attempts are audited.

The supplied **Ticket Vendor – Scanner** role permits event lookup and check-in without general ticket modification, customer or order rights. An authenticated Admin API supports custom integrations. A standalone mobile scanner app is not currently included.

## Artists, booking and event programmes

Manage artist profiles with images, genres, collectives, labels and social links. The booking roster in Shopping Experiences displays selected artists and directs enquiries to the configured contact category, an email address or an external booking URL. Fees and booking notes remain internal.

Assign artists to stages and sets with optional start/end times, including performances across midnight. Publish the event line-up and stage timetables independently.

## Administration, Shopping Experiences and SEO

Event details bring together ticket categories, individual customer tickets and check-in records. Ticket tabs on order/customer details assist support. Foundation forms and lists provide consistent management.

Public event pages, CMS listings with an optional archive, translated content and native SEO URLs support event presentation. Configure ticket cards or a compact list, availability, images and descriptions per sales channel. Foundation supplies import/export profiles and data packages. The optional demo site includes a homepage with social links, Events, Booking and Contact pages, event and artist images, ticket examples and a guest list.

## Features

- Dedicated events/types without creating extra products.
- Per-type prices, taxes, quotas, purchase limits and sales windows.
- Native Shopware cart/checkout with atomic allocation.
- Individual ticket numbers, QR codes and PDFs.
- Payment-based activation, deadlines, expiry and revocation.
- Automatic email delivery, tracking and resending.
- Downloads for authorised signed-in customers.
- Manual tickets and internal free guest-list categories.
- Browser scanner, check-in audit and restricted scanner role.
- Authenticated check-in endpoint for custom integrations.
- Event pages, CMS listing, translations and SEO URLs.
- Private guest registration with confirmation links and voluntary support.
- Artist booking roster, stages, line-up and timetables.
- Group and service packages with multiple redemptions.
- Personal ticket links for editing and downloads without a customer login.
- Event archive and configurable ticket presentation.
- Ticket views on events, orders and customers.
- Flow Builder action and Foundation data/demo packages.
