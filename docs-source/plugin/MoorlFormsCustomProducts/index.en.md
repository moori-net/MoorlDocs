# Form Builder 2 | Product-Configurator Add-On

With this add-on for [Form Builder 2](../MoorlForms/index.md), you can make products individually configurable and influence their prices. Input fields can be mapped to supported database fields.

This description was checked against the local source of version 2.7.1 on 10 November 2026. The existing illustrations come from earlier versions and have not been freshly verified in the current administration. The plugin package requires Shopware `~6.7.8`, MoorlFoundation `~1.7.29` and MoorlForms `~2.7.0`.

## Example forms for download

- [Product Configurator Add-On](examples/custom-products-add-on.json)
- [Product Configurator Add-On (Area calculation)](examples/custom-products-add-on-ac.json)

After importing, check the product group, target entity `order_line_item`, tax/currency data and individual custom fields. The area example has no product-group assignment. The examples contain older export data; an actual import through the current interface was not performed for this documentation review.

## New form of the type "Product Configurator"

With this form you can on the one hand influence the product prices via the options and on the other hand you can use the mapping to save the configuration in custom-fields e.g. for further technical processing of the data.

Under **Content → Form builder 2**, create a form of type “Product configurator” (`custom-product`). The add-on uses the base editor and adds its price-order setting there. It has no separate administration navigation. Configuration fields are embedded in the existing purchase form, so no additional submit button is needed there.

![](images/fbcp-01.jpg)

Example form.

![](images/fbcp-04.jpg)

The related entity is `order_line_item`, the order position. Configuration is first stored as payload on the cart item. After checkout, mappings and summaries are written to the order item.

![](images/fbcp-02.jpg)

![](images/fbcp-03.jpg)

Assign the form to a dynamic product group to determine which products offer it. Products without product-stream IDs are skipped by the current assignment logic.

Also check the price and currency settings. Current cart calculations use the product price definition's tax rules for option prices; a separate form tax rate is not generally required for that calculation.

It is also possible to combine several forms for the products! However, make sure that you always use individual technical names for your input fields!

## Price definitions

You can define price definitions for the options.

![](images/fbcp-05.jpg)

Options support absolute surcharges and absolute discounts. For a fixed discount, choose the `absolute-discount` price type; the configured amount is subtracted from the price. The earlier limitation to positive absolute surcharges no longer applies.

![](images/fbcp-06.jpg)

Percentage prices are relative to the price of the product. You can also define negative percentage prices.

## Length and area calculations

Use “Number” or “Number range” fields with their price multiplier to multiply the product price by the input value. Multiple multipliers are multiplied together, for example length × width for an area calculation.

The `priceCalculationPriority` switch in the Product Configurator card determines whether option amounts are multiplied too. With `B` as the base unit price, `S` as the sum of selected option amounts and `M` as the combined multiplier:

| Setting | Unit price |
| --- | --- |
| Off or unset | `B × M + S` |
| On | `(B + S) × M` |

When multiple forms are combined, the first form by form priority determines this setting. Product quantity is applied in addition. A numeric zero is currently skipped as a multiplier on the server; check the preview against the cart separately for such boundary values.

![](images/area-calc-01.jpg)

![](images/area-calc-02.jpg)

![](images/area-calc-03.jpg)

## Mapping

Map input fields to supported properties of the order item or existing custom fields. These mappings are written after checkout; uploads are transferred as media references.

![](images/fbcp-07.jpg)

## Storefront

In this example you can see the product configurator in action!

![](images/fbcp-08.jpg)

Here you can select a text, an upload and various options.

![](images/fbcp-09.jpg)

The price is updated according to the selection the customer makes.

![](images/fbcp-10.jpg)

The number of products is also taken into account.

![](images/fbcp-11.jpg)

The configuration is finished, off to the shopping cart!

![](images/fbcp-12.jpg)

![](images/fbcp-13.jpg)

Small adjustments can be made at any time before the order is completed!

![](images/fbcp-14.jpg)

The configuration is displayed in text form in the order overview.

When reordering from the order history, the stored configuration payload is submitted again. Processing and price calculation then use the currently available forms and products.

## Admin

If you do not use the mapping, you can still access the configuration at any time.

![](images/fbcp-15.jpg)

Open **Orders → Order → General** and select “Show configuration” from the item context menu. The summary remains available without individual field mappings.

![](images/fbcp-16.jpg)

For e-mail and custom document templates, use `{{ orderLineItem.customFields._moorl_fb_html }}` or `{{ orderLineItem.customFields._moorl_fb_plain }}`. Here, `orderLineItem` must refer to the current order item in your template; adjust the variable name to match its loop. The add-on also stores `_moorl_fb_json`, `_moorl_fb_xml` and `_moorl_fb_media_ids`. It does not automatically update all mail and document templates.

![](images/fbcp-17.jpg)

Since the custom fields for order items are not visible in the admin, here is a screenshot from the database to show that the field has been saved correctly.

## Plugin settings

Open **Extensions → My extensions → Product Configurator Add-On → Configure**.

| Setting | Default | Effect |
| --- | --- | --- |
| Lock checkout if required fields are empty | Off | Blocks ordering when configuration validation errors are detected |
| Show badge in product box | On | Marks configurable products |
| Show button in product box | On | Leads to configuration on the detail page |
| Load forms only for the product detail page | Off | Restricts product enrichment to detail pages |
| Load forms only for product listings | Off | Restricts product enrichment to listings |

With both loading restrictions off, products are enriched globally. With both on, both specific loading paths run. Listing output depends on products being enriched in that context.

The browser display is a preview; the calculated cart is authoritative. Check price order, quantity, currency, tax state and the required-field lock with your form and theme configuration. General compatibility with discount/promotion extensions has not been established by this add-on alone.
