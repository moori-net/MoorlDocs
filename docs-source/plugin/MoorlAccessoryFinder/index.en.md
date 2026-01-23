---
description: With this plugin you create for your store a comprehensive filter option for accessories of any kind. Your customers will find important accessories faster than with the normal search.
tags:
  - Accessories
  - Car Parts
  - Printer supplies
---

# Accessory finder | Car Parts, Printer supplies and more

With this plugin you create for your store a comprehensive filter option for accessories of any kind. Your customers will find important accessories faster than with the normal search.

![Preview](images/af14.JPG)

---

## Purchase the Plugin

The plugin can be purchased from the following stores. If you already have a Shopware account, please **always use** the link to the **Shopware Community Store** first, as alternative stores may cause licensing issues. If a plugin is **not** available in the Shopware Community Store, it is offered exclusively in one of the alternative stores.

- [Shopware Community Store](https://store.shopware.com/en/search?search=MoorlAccessoryFinder) *(recommended)*
- [moori Plugin Store](https://moori-plugin-store.com/MoorlAccessoryFinder)
- [Shopelfen Store](https://www.shopelfen.de/) *(under construction)*


**Important note:** You need the Foundation Plugin, which is available free of charge: [moori Foundation](../MoorlFoundation/index.md)


## Quickstart

A **demo package** is available for testing this plugin.

Go to **“Settings → [Demo Assistant](../MoorlFoundation/demo-assistant.md)”** and select **“MoorlAccessoryFinder”**.

**Note:** In some cases, new categories and pages will be added to your shop. Please note that the demo data is provided for testing purposes only. The images included may be protected by copyright and must not be made publicly available.


**Possible areas of use:**

1. printer accessories
2. vehicle accessories
3. spare parts
4. consumables

## Highlights
- Additional search suggestions
- Freely configurable level navigation
- Matching tab in the product description of the accessory product
- CMS filter element for category lists
- Simple and customizable

## Features
- Multiple filter groups, also suitable for the same category
- Customer's filter setting is saved for the session and can be reset
- Filter as sidebar element or full width
- TSN/HSN key number search possible
- Import/export of data via CSV for fast data transfer
- Custom Twig template for adjustments in the product detail tab
- Unlimited levels for filter
- Subcategories keep the filter settings

## Installation and operation

First install the Foundation Basis plugin via the Shopware 6 plugin manager.
Then you can install the Accessories Finder.

You can find the filter groups here:

![Logo](images/af1.JPG)

There you create a new Filtergroup:

![Logo](images/af2.JPG)

Once the filter group is created, three layers will be created automatically,
you can easily adjust them according to your needs. Please make sure
that the level starts from 1 and has no gaps.

![Logo](images/af4.JPG)

![Logo](images/af5.JPG)

Now you can start directly with the maintenance of the manufacturers. With larger amounts of data
the import should be done by a professional developer.

![Logo](images/af3.JPG)

After creating a manufacturer, click on the three dots (..) and on Edit
to get to the next level. There you can maintain as many layers as you like.

![Logo](images/af6.JPG)

![Logo](images/af8.JPG)

Arrived at the last level? Now you can assign the accessory products!

![Logo](images/af9.JPG)

Alternatively you can go to the product and there in the section "Accessories Categories" you can assign
assign your compatible devices/vehicles.

![Logo](images/af10.JPG)

A look into the frontend reveals if the assignments were successful.

![Logo](images/af12.JPG)

![Logo](images/af11.JPG)

To apply the filter, you now need an adjustment in the category listing.
Go to the "Sidebar" blocks and drag the "Accessory Filter" element into the template.

After you have saved the CMS page, make sure that this page has also been assigned to the
category where the accessories products are located.

![Logo](images/af13.JPG)

This is how it should now look in the frontend:

Filter not set:

![Logo](images/af14.JPG)

Filter set:

![Logo](images/af15.JPG)

Give your filter group the technical name "car_parts" to activate the key search.

![Logo](images/af16.JPG)

The plugin configuration can optionally be changed, if certain functions are not needed or there are
or there are problems with the performance.

![Logo](images/af17.JPG)