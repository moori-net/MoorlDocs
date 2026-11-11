# Form Builder 2 | Customer Forms Add-On

With this add-on for [Form Builder 2](https://docs.moori.net/en/plugin/MoorlForms/), you can add fields to customer registration and provide separate form pages in the customer account. Input can be mapped to existing customer fields and custom fields.

This description was checked against the local source of version 2.7.0 on 10 November 2026. The add-on-specific administration has not been visually verified in this environment.

## Setup and availability

The plugin package requires Shopware `~6.7.8`, MoorlFoundation `~1.7.29` and MoorlForms `~2.7.0`.

Create the form under **Content → Form builder 2** in Form Builder. Select “Extension of the customer registration” (`customer-register`) or “Form in the customer area” (`customer-account`). Both types use the related entity `customer`. Activation, sales channel and the base form's other availability conditions determine where the form is offered.

The add-on has no separate administration navigation or plugin configuration switches. Edit layout, fields, mappings and actions in the base form editor.

## Example forms for download

- [Customer-Account Form Add-On](examples/customer-account-add-on.json)
- [Customer-Registration Form Add-On](examples/customer-registration-add-on.json)

After importing, check the required custom fields and mail configuration. The examples use shop-specific field names; an actual import through the current interface was not performed for this documentation review.

## New form types

- Forms for the account area
- Forms for registration

## Mapping

Use field mapping to assign inputs to supported properties of the customer entity, such as `firstName`, `email` and existing fields under `customFields.<name>`. Set up any individual custom fields as required.

For example, the customer can upload a business registration, the mapping to the file is in a
custom field. An upload stores its media ID there, rather than the file contents.

### Customer-Account

The forms for the customer account are automatically included in the navigation.

The form adopts the appropriate database fields based on the mapping properties.

When saving, the data is again saved in the mapped database fields.

Optionally, the shop owner can be informed of a change by e-mail. Configure the mail action, recipients and template in the form; the add-on does not enable a default notification.

The account form is a separate page. Add a suitable submit button and, if needed, a feedback element, as shown in the account example. Both opening the page and saving require a logged-in customer.

### Customer registration

The additional input fields are embedded in Shopware's existing registration form. Separate form-wrapper or submit components are therefore unnecessary. Required fields are checked before Shopware registers the customer; after successful registration, mappings and uploads are assigned to the new customer.

The Flow Builder provides **Sign-up (Form Builder)**, with the technical event name `checkout.customer.moorl_form_register`. It contains the customer and one form. If multiple registration forms are present, only the first is exposed through this event. The supplied flow has no predefined actions; configure notifications or further steps yourself.

## Stored summaries

Alongside individual mappings, the base plugin writes `_moorl_fb_html`, `_moorl_fb_plain`, `_moorl_fb_json`, `_moorl_fb_xml` and the upload references `_moorl_fb_media_ids` to the customer's custom fields. Account forms are prefilled from the mapped customer fields; they do not create a separate customer database.
