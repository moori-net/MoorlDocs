**Documentation:** 
[https://docs.moori.net/en/plugin/MoorlScrolling/](https://docs.moori.net/en/plugin/MoorlScrolling/)


**Important note:** You need the Foundation Plugin, which is available free of charge: [Foundation](https://store.shopware.com/en/search?search=MoorlFoundation)


## Requirements

MoorlScrolling requires Shopware 6.7 with Storefront and MoorlFoundation from the 1.7 series. MoorlInterrupter is optional.

## Installation and activation

1. Install and activate MoorlFoundation first if it is not already available.
2. Install MoorlScrolling under **Extensions > My extensions** and activate the plugin.
3. Open **Configure** from the plugin's menu.
4. Select a sales channel, or **All sales channels** to set global defaults.
5. Enable **Enable infinite scrolling**. Choose the required areas using **Category listings** and **Search results**.
6. Save the configuration and reload the corresponding category or search page in the Storefront.

Both plugin activation and **Enable infinite scrolling** are required. Settings use Shopware's existing SystemConfig; no additional database tables are needed.

## First functional check

Open a listing with at least two product pages. By default, following pages load automatically and previous pages manually. The next page is prepared in the background. The manual loading link remains available.

Then open a later page directly, for example using `?p=2`. Check loading previous products, changing a filter and using standard pagination. When MoorlInterrupter is installed, its content should remain on the configured pages and at the intended positions.

## Sales channels and loading limits

An individual sales channel initially inherits the global settings. Remove inheritance at a field to save a channel-specific value.

By default, each direction pauses after three automatically loaded pages until the customer continues manually. A range contains at most 20 inserted pages; the adjacent-page link then opens the regular shop page. Set the corresponding limit to `0` to remove it.

## Themes and other extensions

One primary category or search listing per document is supported. Check the result with your theme and other listing extensions before production use. For custom installations from source, deploy the Storefront assets and compile the theme through the usual Shopware build process.
