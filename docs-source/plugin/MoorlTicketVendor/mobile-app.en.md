# Mobile scanner app: planned experience and existing API

## Availability

**A standalone mobile scanner app does not exist yet.** This document specifies its intended workflow and the interface already supplied by the plugin. No app download, app-store release, native camera implementation or offline mode is available.

The Administration browser scanner, scanner role and authenticated check-in endpoint are already implemented. Planned mobile behaviour and the current API contract are distinguished below.

## Planned app workflow

The future app should guide entrance staff through a short smartphone/tablet workflow:

1. Enter the HTTPS shop address and sign in with a restricted personal Shopware account.
2. Choose an event and keep its name visible throughout scanning.
3. Capture a QR code with the device camera or enter its complete token manually.
4. Ask the server and display the outcome and any returned ticket number clearly.
5. Start the next independent scan only after completing the current outcome.
6. Retry an uncertain request safely after connection failure; remove session and sensitive local data at logout.

Accessible text with optional sound/vibration is intended. Navigation, camera support, secure credential storage, token renewal and distribution still need implementation and testing on target devices. The plugin supplies no native mobile UI or app-pairing mechanism.

## Shop and permissions

The **scanner-role** Foundation package creates **Ticket Vendor – Scanner** with:

| Privilege | Purpose |
| --- | --- |
| `moorl_tv_ticket_sale:read` | Search/read events through the native Admin API. |
| `moorl_tv_ticket:scan` | Execute the fixed check-in action only. |

General ticket read/update, customer and order privileges are unnecessary. PDF download, sending and revocation are excluded. The role is not restricted to selected events. Other roles and administrator access expand effective permissions.

An administrator creates users and assigns the role separately. The package creates no login credentials or integrations. Custom roles can use **Ticket Vendor → Scan tickets and read events** under additional permissions. Earlier ticket-update/check-in-create privileges alone no longer authorise the endpoint.

## Authentication: existing Shopware API

The endpoint belongs to the **Admin API**, not the public Store API. Requests need a valid native Bearer token. A sales channel `sw-access-key` does not replace authentication.

An implemented personal app may use the existing Shopware login:

```http
POST /api/oauth/token
Content-Type: application/json

{
  "grant_type": "password",
  "client_id": "administration",
  "username": "scanner-user",
  "password": "<personal password>"
}
```

Shopware returns native token and expiry information. The future app must handle expired sessions and use the native refresh procedure when a refresh token is supplied. Passwords must not be logged or persisted in plaintext. Respect the installation's authentication policies.

Server integrations may instead use native `client_credentials` with a non-administrative integration assigned the scanner role. Do not embed shared integration secrets in distributed mobile applications. No dedicated device-code, QR-pairing or app-login endpoint is implemented.

## Loading events: existing Admin API

```http
POST /api/search/moorl-tv-ticket-sale
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "page": 1,
  "limit": 25,
  "filter": [
    { "type": "equals", "field": "active", "value": true }
  ],
  "sort": [{ "field": "startAt", "order": "ASC" }],
  "includes": {
    "moorl_tv_ticket_sale": ["id", "name", "startAt", "endAt", "timezone", "locationName"]
  }
}
```

Parse the native search response and subsequent pages. Use the selected event's `id` as `saleId`. Cached events do not authorise local admission; the server checks each scan again.

## Check-in: implemented plugin endpoint

```http
POST /api/_action/moorl-tv/check-in
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "saleId": "0123456789abcdef0123456789abcdef",
  "token": "<ticket QR code contents>",
  "scanRequestId": "b360a0d88ae44b8fa9d96cd58491c079",
  "deviceId": "entrance-north-01",
  "redemptionCategory": "admission"
}
```

| Field | Contract |
| --- | --- |
| `saleId` | Required string containing a valid Shopware UUID, conventionally 32 hexadecimal characters without hyphens. |
| `token` | Required string, non-empty after trimming, at most 64 bytes. New tickets use 32 random characters; imported tokens may differ. |
| `scanRequestId` | Required unique string, 16–64 characters from `A–Z`, `a–z`, `0–9`, `_`, `-`. Random hexadecimal UUID recommended. |
| `deviceId` | Optional string, at most 128 bytes, for example a local device label without personal information. |
| `redemptionCategory` | String: `admission`, `drinks` or `food`. Missing values default to `admission` for existing clients; null, unknown or wrongly typed values produce HTTP 400. New clients should always send the selected area. |

The QR contains the token itself, not a URL to open. Do not substitute the visible ticket number. The server derives the scanner user/integration from authentication; `scannerIdentifier` is not a client-controlled field.

Processed requests return HTTP 200, for example:

```json
{
  "result": "accepted",
  "ticketNumber": "T-10000",
  "attendeeName": "Ada Lovelace",
  "attendeePhone": "+491701234567",
  "redemptionCategory": "admission",
  "redemptionCount": 2,
  "maxRedemptions": 5,
  "remainingRedemptions": 3,
  "checkinId": "f948564f0fc744f1bb26a8317ab55e4a4"
}
```


`redemptionCategory` in the response is the actual ticket area; the audit column records the requested area. `redemptionCount`, `maxRedemptions` and `remainingRedemptions` describe consumption after processing, and retries retain that exact snapshot. Unknown and wrong-event scans return null for all four fields, ticket number and attendee data. Each deliberate scan uses exactly one redemption. Pause camera recognition after each result until **Next scan**; an unchanged code must not consume multiple units automatically.

HTTP 200 means the request was processed. Only `accepted` confirms redemption for that request. Responses never contain the QR token.

| `result` | Meaning | Intended app display |
| --- | --- | --- |
| `accepted` | One redemption consumed atomically. | Confirm one admission/service and show progress. |
| `already_redeemed` | All included redemptions consumed. | No additional admission/service; show exhausted progress. |
| `wrong_category` | Requested area differs from the ticket area. No use consumed. | Show the required `redemptionCategory`. |
| `wrong_event` | Ticket belongs to another event. | Check event selection; `ticketNumber` is `null`. |
| `event_closed` | Event inactive or configured end time passed. | Contact event manager. |
| `not_valid` | Ticket pending, expired or revoked, for example. | No approval; contact administration. |
| `unknown` | Token not found. | Check code; `ticketNumber` is `null`. |

There is no separate admission opening time. A future event start alone does not prevent redemption. Type activity controls public sales: valid manual guest-list tickets for inactive types remain redeemable for an open event.

## Retries and concurrent devices

Generate a `scanRequestId` before the first attempt and retain it with the event/token/area until the outcome is known. If the response is lost, repeat the **same request with the same ID**. It returns the original outcome, `checkinId` and original progress snapshot, even when later scans have increased consumption.

Use a **new ID** for each new deliberate scan, whether of the same or a different ticket. Replaying a previously accepted request must not count another attendee in the UI. Changing event, token or area for a used ID produces HTTP 409. An event or area change must cancel pending camera callbacks and reset input, result and pending retry. Existing legacy fingerprints are accepted for admission retries only.

Multiple devices can scan the same event concurrently. Server transactions serialise competing redemptions. Two different requests competing for the last redemption produce one acceptance and one “already redeemed” outcome. Earlier independent scans each consume one unit until the limit. A package stays `valid` until the final unit sets `redeemed` and `redeemedAt`.

## Technical failures

| HTTP/failure | Meaning or required app behaviour |
| --- | --- |
| 400 | Invalid types/fields, UUID, empty/oversized token or invalid request ID. Correct input. |
| 401 | Authentication missing/expired. Renew login; do not infer an admission decision. |
| 403 | Scan privilege missing. Check roles; no approval. |
| 404 | Event does not exist. Refresh event selection. |
| 409 | Request ID already used for a different scan. Do not treat as success. |
| Timeout/disconnection/5xx | Outcome uncertain. No local success; retry the same scan and ID. |

Handle installation/proxy failures such as rate limits without interpreting them as approval. Native error responses use Shopware's `errors` structure.

## Audit and sensitive data

The backend records request ID, time, result and, when applicable, ticket, event, device and authenticated scanner. Metadata stores a one-way request fingerprint, not the raw token. Ticket tokens must not enter app analytics, crash reports or logs. PDFs and camera views can contain admission credentials.

The future app should retain only necessary session/pending-retry data in secure local storage and remove it after completion/logout. Storage implementation and its tests remain part of future app development.

## Outside the current scope

Offline ticket databases, later conflict synchronisation, admission without server confirmation, Apple/Google distribution, push messages, device pairing, per-event user restrictions and named guest-list search are unavailable. Creating/editing/refunding tickets and resetting check-ins are also outside the scanner role.

## Acceptance criteria for future development

- Personal login/logout and expired sessions work with the scanner role.
- Event search handles pagination and shows the selected event before scanning.
- Camera/manual entry work on explicitly chosen iOS/Android devices; these implementations are still outstanding.
- All seven business outcomes and technical failures have clear text displays.
- Lost responses can be retried without double redemption or double attendee counting.
- Two devices cannot both accept one ticket as a new redemption.
- No local admission approval without connectivity.
- Passwords, Bearer tokens and ticket codes never enter logs/analytics.
- General modification, sending, revocation and customer/order requests remain blocked server-side for scanner accounts.

Until that application is developed, use the existing [browser scanner](index.en.md#admission-with-the-browser-scanner).
