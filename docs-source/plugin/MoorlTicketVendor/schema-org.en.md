# Structured event data

Each event detail page publishes one JSON-LD object using [schema.org/Event](https://schema.org/Event), including event pages using a CMS layout. Listings, account pages and carts do not add Event objects.

Name, description, keywords, image, event times with the event timezone offset, duration, venue/address/coordinates, absolute SEO URL, identifier and ticket offers are generated from existing data. Offers use the current currency, currency conversion, tax display, stock, purchase limits and sales periods. Inactive or currently hidden ticket categories are excluded. Sold-out offers use `SoldOut` or are hidden according to the display setting. Capacities sum the currently public ticket categories. Free admission is stated only when prices exist and all public categories are free. Missing optional information is omitted. Private customer and ticket-holder information, email addresses, mobile numbers and ticket tokens are never included automatically.

## Additional properties

Open **Event → SEO → Structured event data (schema.org)** and edit **Additional event properties (JSON)**. The translated `schemaOrg` field accepts any Event or inherited Thing property, including nested objects and arrays. There is no property allowlist.

```json
{
  "@type": "MusicEvent",
  "organizer": { "@type": "Organization", "name": "City Park Events", "url": "https://example.com" },
  "performer": [{ "@type": "MusicGroup", "name": "Park Band" }],
  "doorTime": "2027-07-17T17:30:00+02:00",
  "inLanguage": "en",
  "typicalAgeRange": "16-",
  "eventStatus": "https://schema.org/EventScheduled"
}
```

This also supports organizer/performer details, online or mixed attendance with `VirtualLocation`, sponsors, audience, accessibility, ratings, reviews, funding, previous dates, recurring schedules, parent/sub-events and creative works. Explicitly entered properties such as `attendee` are public metadata; they are not populated from ticket holders.

Custom values replace the corresponding automatic property in full; `null` omits an optional property. `@context` remains `https://schema.org`. Setting `eventSchedule` removes automatic `startDate`, `endDate` and `duration`; put dates on the Schedule object instead. This does not create recurring sales events or tickets. Empty input clears this language's additions while retaining Shopware's language fallback. Invalid editor input is retained visibly and rejected by DAL type validation on save. Authors remain responsible for valid schema.org semantics; use the [Schema Markup Validator](https://validator.schema.org/) and Google's additional [event guidelines](https://developers.google.com/search/docs/appearance/structured-data/event).

Default metadata uses `EventScheduled` and `OfflineEventAttendanceMode`. `eventStatus` can describe cancellations or rescheduling for search engines; it does not change the active switch, ticket sales or scanner access. Metadata never changes pricing, inventory or purchase rules.

## Schema and deployment

Generate the nullable JSON column `moorl_tv_ticket_sale_translation.schema_org` using the external schema tool and the updated DAL definition. No additional PHP migration is included. Clear caches and build administration assets. The API exposes the translated field as `schemaOrg`.
