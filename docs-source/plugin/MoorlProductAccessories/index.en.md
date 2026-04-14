---
description: Shopware 6 plugin for accessories, product bundles and configurators: assign accessories flexibly, price them individually, and sell them directly in the storefront.
tags:
  - Accessories
---

# Product add-ons & accessories

Shopware 6 plugin for accessories, product bundles and configurators: assign accessories flexibly, price them individually, and sell them directly in the storefront.

![Preview](images/storefront-product-detail-categories.jpg)

---

## Plugin Demo

A storefront demo is available for testing this plugin. The plugin can be tested at the following link:

- [https://demo-sw67.moori.net/MoorlProductAccessories](https://demo-sw67.moori.net/MoorlProductAccessories)


## Purchase the Plugin

This plugin can be purchased in the **Shopware Community Store**.

- [Shopware Community Store](https://store.shopware.com/en/search?search=MoorlProductAccessories)


**Important note:** You need the Foundation Plugin, which is available free of charge: [moori Foundation](../MoorlFoundation/index.md)


## Quickstart

A **demo package** is available for testing this plugin.

Go to `Settings` → [`Demo Assistant`](../MoorlFoundation/demo-assistant.md) and select `MoorlProductAccessories`.

**Note:** In some cases, new categories and pages will be added to your shop. Please note that the demo data is provided for testing purposes only. The images included may be protected by copyright and must not be made publicly available.


---

## Initial Setup

### Plugin Configuration

![Plugin Configuration](images/admin-plugin-config-1.jpg)
![Plugin Configuration](images/admin-plugin-config-2.jpg)

#### Settings

- **Display of the accessory product name in the configurator**
- **Update the price based on the current selection**
- **Create bundle products for the shopping cart**: This setting is required if accessories should have individual prices.
- **Show available stock on the product detail page**
- **Enable for these customer groups**: The configurator is only available for the selected customer groups. Note: This setting will be replaced by the Rule Builder in the future.

#### Product Price Calculation

- **Calculation priority**: If multiple price calculations apply, a priority can be defined here.
- **Stop calculation after first match**: When recalculating the price, all subsequent price calculations will be skipped from this point onward.
- **Source for price calculation**
- **Source for list price**

### General Overview

![Plugin Configuration](images/admin-settings.jpg)

In the main administration navigation under `Settings` → `Extensions` → (`Accessory Products` or `Accessory Categories`), you will find an overview of all created entries.

## Accessory Categories

![Accessory Categories List](images/admin-category-list.jpg)
![Accessory Categories Detail](images/admin-category-detail-1.jpg)
![Accessory Categories Detail](images/admin-category-detail-2.jpg)

### General Settings

- **Name**
- **Type**: There are currently four different selection types available: `Single selection`, `Multiple selection`, `Single selection with image`, and `Multiple selection with image`.
- **Teaser**: Additional informational text for the category
- **Allow no selection**: The selection in the configurator is optional.
- **Sort order**
- **Accessory products**: A list of all products assigned to the current category.

## Accessory Products

![Accessory Products List](images/admin-accessory-list.jpg)
![Accessory Products Detail](images/admin-accessory-detail-general-1.jpg)
![Accessory Products Detail](images/admin-accessory-detail-general-2.jpg)
![Accessory Products Detail](images/admin-accessory-detail-price.jpg)

### General Settings

- **Product**: This accessory belongs to the selected product.
- **Accessory**: The product that is offered as an accessory.
- **Dynamic product group**: This accessory belongs to the selected product group.
- **Category**: This accessory is listed under the selected category.

Note: **Product** and **Dynamic product group** are optional. However, only one of these two assignments should be used.

### Visibility

- **Name**: Alternative name if the accessory should be displayed differently from the original product name.
- **Info**: Internal note.
- **Priority**: Priority within the selection.
- **Is default**: This option is preselected by default.

### Price

- **Show as discount**: If the new price is lower than the original price, it can be displayed as a discount.
- **Price calculation type**: `Original price of the accessory product`, `Custom price`, or `Percentage price of the main product`.
- **Price**: If `Custom price` is selected, an individual price can be entered here.
- **Percentage**: If `Percentage price of the main product` is selected, a percentage value can be entered here. `100` equals 100% of the main product price.
- **Source for price calculation**: Inherited from the plugin configuration and can optionally be adjusted here.
- **Source for list price**: Inherited from the plugin configuration and can optionally be adjusted here.

## Main Product

In the main administration navigation under `Catalogues` → `Products` → `Detail` → `Accessories`, accessory categories or accessory products can be assigned directly.

![Main Product](images/admin-product-detail-accessories.jpg)

- **Disable add to cart**: The product cannot be added directly to the shopping cart from the storefront listing.
- **Show bundle badge**

Note: Accessories can also be created or assigned directly in the modal.

![Main Product Modal](images/admin-accessory-modal.jpg)

## Dynamic Product Group

In the main administration navigation under `Catalogues` → `Dynamic Product Groups` → `Detail`, accessory categories or accessory products can be assigned directly.

![Dynamic Product Group](images/admin-product-stream-detail.jpg)

## Storefront Display

In this example, there are accessories assigned directly and accessories assigned via a dynamic product group.

![Configurator](images/storefront-product-detail-categories.jpg)

1. Single selection with image (optional)
2. Single selection with image
3. Multiple selection with image

![Off-canvas Cart](images/storefront-product-detail-cart.jpg)

The product is bundled together with the selected accessories and then added to the shopping cart.

![Cart](images/storefront-cart.jpg)

1. **The bundle**: The cart line item containing the total of all bundled products.
2. **The main product**: The main product is always listed first within the bundle with its original price.
3. **Accessory with custom price**
4. **Accessory with percentage price of the main product**: In this example, 10%.
5. **Accessory with original price**