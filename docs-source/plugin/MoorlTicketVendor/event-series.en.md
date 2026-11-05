# Event series

A series provides shared content for multiple events. Membership is optional; standalone events continue to work as before.

## Manage a series

Create a series under **Catalogues → Event series**. Edit shared text, media, publication settings, SEO and the series CMS layout there. The **Dates** tab shows the standard entity grid. **Assign an existing event** in the top action bar opens a modal to select and explicitly assign an event. **Generate dates** opens a separate modal from the same action bar. Save a new standalone event before assigning it to a series.

In the storefront, linked events use the series name, description, teaser, keywords, cover, banner and metadata. Their local content is not displayed or searched in the storefront while linked. In Administration, the event’s own texts, images and metadata remain visible and editable; lists and selectors use local content. There is no inheritance notice or separate series preview. Change or clear membership through the optional **Event series** field. Dates, time zones, venues, prices, ticket types, capacities, programmes and guest lists remain specific to each event. Venue descriptions, ticket type text and guest-list rules remain local.

Detaching copies the current shared series content, translations and media references into the event. It then becomes independently editable. A series with assigned events cannot be deleted.

## Publication

Public visibility and new purchases require both the event and its series to be available. Disabling a series does not overwrite the activation switches of its events. Existing tickets remain accessible and redeemable under their original check-in rules. The series **Listed** setting controls its listing visibility without disabling its events.

## Generate dates

Save the series and open **Generate dates** from its top action bar. Choose a saved template event, a local start time, and either an interval in days or selected weekdays each week. Set a count or an inclusive end date, then explicitly choose whether new events and their new ticket types should be active. Preview the dates before generating them. This choice never activates a disabled series. Successful generation closes the modal and refreshes the dates without discarding unsaved series edits.

There are at most 250 dates per preview and a five-year horizon when using an end date. Dates retain their local time across daylight-saving changes. Nonexistent or ambiguous local times are rejected. Monthly recurrence is not included.

Venue and operative settings are copied from the template, while shared content comes from the target series. Tickets, orders, customers, check-ins, registrations, sales counters, stages, performances and guest-list secrets are not copied. New guest lists are disabled initially. Repeating generation skips existing slots without changing existing events or activation settings. Changed inputs or template data require a new preview.

## CMS and search

Series have an independent detail route `/moorl-tv/series/{seriesId}`, SEO URLs and a CMS layout. Layout selection uses the series layout, the sales-channel default series layout, then the supplied default. Individual event layouts remain separate.

Shopping Experiences includes series detail, dynamic series listing, static series listing and series dates elements. The dates element uses the current series or an explicitly selected one. Search and suggestions have separate series configuration and require Foundation advanced search. The scanner continues to use its existing permissions and a bounded event search endpoint.

## Upgrade and demo

The additive `Migration1793871339EventSeries` follows the unchanged `Migration1793194127Initial`. Existing events remain standalone with unchanged IDs, content, URLs and ticket references. Apply the regular Shopware plugin update and the established Administration build, asset and cache deployment steps.

The optional Foundation **series** demo package provides a series with dates in Berlin and Hamburg and one ticket type per date. It also creates an **Event series** category under the selected sales channel's navigation, with its own CMS overview at `/MoorlTicketVendor/Series`. The overview lists only the demo series and links to its dates. Reimport an existing package to add the overview.

It is independent of the **standard** package and has a separate cleanup marker. Removing it preserves merchant-added child categories and reused overview layouts. It creates no customers, tickets or check-ins.
