**Important note:** You need the Foundation Plugin, which is available free of charge: [Foundation](https://store.shopware.com/en/search?search=MoorlFoundation)


## Browse product listings in both directions

MoorlScrolling lets customers load more products directly in category listings and search results. Choose manual or automatic loading independently for previous and following pages. Optional preloading prepares adjacent pages in the background.

The extension uses existing Shopware product listings. Filters, sorting and standard pagination remain part of the shopping flow. Configuration requires no additional database tables.

## Manual loading or infinite scroll

A loading link gives customers control over when more products appear. Automatic mode loads products as they scroll toward the listing boundary, while keeping the manual link available. Each direction can be configured separately.

Direct entry on page 5 initially displays that page's products. Customers can add page 4 above it or page 6 below it. Prepending earlier products preserves the position of the product being viewed.

## Designed to work with MoorlInterrupter

Each inserted product page retains its own listing section. MoorlInterrupter page rules, positions and responsive widths are preserved. Interrupters from different pages are not mixed into a shared product row.

MoorlInterrupter is optional. MoorlScrolling also works with product listings without interrupters.

## Preloading and visible progress

Prepare the next page or both adjacent pages in the background. A prepared page becomes visible only when it is actually loaded into the listing. Preloading can also be combined with manual loading.

A compact progress bar shows, for example, “24 of 120 products”. Direct entry on a later page includes preceding pages in the count. At the listing end, the bar remains visible at 100 percent.

## Settings for each sales channel

Use global defaults and override them per sales channel when needed. Category listings and search results can be enabled separately. Configure loading behavior, preloading, pagination and page URL updates while scrolling.

Configurable limits control automatically inserted pages and the total number of pages in a range. By default, automatic loading pauses after three pages per direction and a range contains at most 20 pages. Set the corresponding limit to 0 to remove it. Regular page links keep further products accessible.

## Navigation and error recovery

Already inserted pages are reached directly. A jump to another page starts a new range there. Filter, sorting and page-size changes restart at page 1. If loading fails, existing products remain usable; customers can retry or open the regular shop page.

MoorlScrolling supports one primary category or search listing per document in Shopware 6.7 with Storefront. Wishlists, product sliders, cross-selling and multiple independent listings are outside its scope. Custom themes and extensions with Listing overrides require combination testing.
