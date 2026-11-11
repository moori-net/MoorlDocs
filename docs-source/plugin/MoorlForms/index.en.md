---
description: The Form Builder makes it child's play to create complex forms with independent task areas. It has a modular structure and can be used flexibly for any cases.
tags:
- Shopware 6 Plugin
- Build forms
- File upload
- B2B
- Send E-Mail
---

# Form builder 2 | Base version

The Form Builder makes it child's play to create complex forms with independent task areas. It has a modular structure and can be used flexibly for any cases.

![Preview](images/admin-form-general.png)

---

## Purchase the Plugin

This plugin can be purchased in the **Shopware Community Store**.

- [Shopware Community Store](https://store.shopware.com/en/search?search=MoorlForms)


**Important note:** You need the free [moori Foundation plugin](https://docs.moori.net/en/plugin/MoorlFoundation/).

---

## Custom forms for Shopware 6

- You want to create your own forms in Shopware?
- You don't have a Shopware Professional subscription, but don't want to do without this essential feature?
- The possibilities of the Shopware Professional form builder are not enough?
- You build complex forms and are looking for a good basis for your individual adjustments?

If you can answer one of these questions with "yes", then you are definitely on the right track!

## Example forms for download

- [Simple contact form](examples/simple-contact-form.json)
- [Entity mapping form](examples/entity-mapping-form.json)
- [Responsive form](examples/responsive-form.json)
- [All features](examples/all-features.json)

Further examples can be found in the respective documentation of the add-ons!

## Add-Ons

This plugin has been shortened in its basic version by some functions, so that it can be offered at an affordable price.
affordable price. All further functions can be obtained.

The complete [feature overview](https://docs.moori.net/en/plugin/MoorlForms/all-features/) covers the base plugin and all add-ons. Each plugin directory contains a `CODEX.md` documenting its extension contracts and limits.

1. [Classic Add-On](https://docs.moori.net/en/plugin/MoorlFormsClassic/): Conditions, repeaters, additional fields, submission history, printing and additional actions
2. [Exit-Intent-Popups Add-On](https://docs.moori.net/en/plugin/MoorlFormsPopup/): Use forms as popup
3. [Slides Add-On](https://docs.moori.net/en/plugin/MoorlFormsSlides/): Use slides
4. [Customer-Forms Add-On](https://docs.moori.net/en/plugin/MoorlFormsCustomer/): Customised forms for registration and customer area
5. [Product-Configurator Add-On](https://docs.moori.net/en/plugin/MoorlFormsCustomProducts/): Additional information on products incl. price calculation
6. [Order Add-On](https://docs.moori.net/en/plugin/MoorlFormsOrder/): Additional checkout inputs, optional checkout lock and storage on the order
7. [Product-Request Add-On](https://docs.moori.net/en/plugin/MoorlFormsProduct/): Product-specific enquiry forms
8. [CSV Add-On](https://docs.moori.net/en/plugin/MoorlFormsCsv/): Write mapped form inputs to CSV files
9. [Hubspot Add-On](https://docs.moori.net/en/plugin/MoorlFormsHubspot/): Send data using a configured HubSpot integration
10. [Mautic Add-On](https://docs.moori.net/en/plugin/MoorlFormsMautic/): Mautic form/contact integration
11. [Webhook Add-On](https://docs.moori.net/en/plugin/MoorlFormsWebhook/): Configurable HTTP requests with form data
12. Custom add-ons on request

(\* In development, \*\* In concept phase)

## Example Add-On for developers

[Example Add-On](https://github.com/moorl/MoorlFormsExample). Its local version contains outdated method signatures and must be adapted to the current base interfaces before activation. See its `CODEX.md` and the [feature overview](https://docs.moori.net/en/plugin/MoorlForms/all-features/).

## What is this plugin good for?

The Shopware 6 _Form Builder 2_ plugin makes it child's play to create complex forms with independent
task areas.

It is modular, so processes and individual fields can be expanded as desired.

## Installation

!!! note

    If you have any problems with the plugin, please note the following [notes](https://docs.moori.net/en/plugin/) in the FAQ section.

1. install
   [Foundation](https://docs.moori.net/en/plugin/MoorlFoundation/)
2. install Form Builder 2 in the Plugin Manager
3. go to: Contents | Form Builder 2

Here you can create or import a new form.

## Settings

The screenshots in this guide show the English administration in Full HD (1920 × 1080). Both documentation languages use the same images.

### Basic configuration

![](images/admin-list.png)

![](images/admin-new-import.png)

1. create new form
2. import

![](images/admin-form-general.png)

1. form settings
2. save form
3. export
4. structure area of the form elements
5. settings area (form/element)

![](images/admin-element-text.png)

1. context menu for creating, deleting or duplicating elements
2. general element settings

### Settings in detail

#### Assignments of elements and forms

You can generally configure the visibility of forms and elements here.

Show a form/element...

- show only in a certain period of time
- only display in a certain sales channel
- show only for a selected delivery country
- show only for a selected shipping method or payment method
- Display only for a selected customer group

A product-specific form...

- can be assigned to a product stream

An element of the group Sections...

- can be assigned to a background image here

Some of these assignments are only available in the Form Builder 2 Add-Ons!

![](images/admin-form-assignment.png)

![Element visibility and entity mapping](images/admin-element-assignment.png)

#### Layout and stylesheet settings

You can assign stylesheet attributes to each form/element.

The CSS options vary depending on the type of form/element.

![](images/admin-form-layout.png)

### Settings for elements

#### Field configuration

All elements from the Field and Multi-Field group can have additional properties in this configuration.

![](images/admin-element-field-settings.png)

#### Selection Configuration

All elements from the Multi-Field group can receive database-specific values. Add-ons offer more possibilities here.

![Selection element](images/admin-element-selection.png)

![](images/admin-element-selection-settings.png)

Select `custom-entity` to configure a DAL source, labels and filters. At most 500 options are loaded. This screenshot shows an unsaved selection.

![Custom entity selection settings (unsaved example)](images/admin-element-custom-entity.png)

#### Responsive behaviour

If the parent element is from the Rows group, all elements contained in it can be given responsive properties.
The rule "Mobile-First" applies here, the properties are always passed on.

The distribution is as follows.

Viewport (xs to xxl) | Inherited (Yes/No) | Display (Yes/No) | Width | Sorting/Arrangement

![](images/admin-element-layout.png)

#### Configuration Upload Field

![Upload element](images/admin-element-upload.png)

![](images/admin-element-upload-settings.png)

#### Date, time and number fields

Date fields provide calendar settings, weekday selection and date limits. Time and number fields have their own input settings. These browser constraints do not automatically establish equivalent server-side validation; see the feature overview.

#### HTML and card sections

HTML content is language-specific. Card sections group related content and can be styled through their layout settings.

#### Validation

Configure required fields, lengths, patterns and comparisons on the element.

![Element validation settings](images/admin-element-validation.png)

#### Embedded CMS elements

Add a CMS element to the form structure and configure its content.

![Embedded CMS element](images/admin-element-cms.png)

![Embedded CMS element settings](images/admin-element-cms-settings.png)

### Settings for forms

Select the processing actions in the general form settings. Available actions depend on the active add-ons.

![Available form actions](images/admin-form-actions.png)

#### Configuration e-mail

Here you can configure the e-mail recipient. If no value is entered, the shop's standard e-mail address will be used.
of the shop is used.

The base plugin already provides `receipt-confirmation` for an acknowledgement and resolves recipients from form settings, translations, suitable selected options or entity context. Classic adds a full mail copy with its own template and optional customer checkbox. An acknowledgement and a full copy are different features.

![](images/admin-form-mail.png)

The following image shows receipt confirmation temporarily selected in the editor; this draft was not saved.

![](images/admin-form-mail-receipt-draft.png)

## CMS settings

The form does not have its own block, but can be accessed via the "Replace element" icon!

After the CMS element has been inserted, you can assign forms of type CMS or Test to the CMS page.

![Form in the Shopping Experiences editor](images/admin-cms-page.png)

![](images/admin-cms-element-settings.png)

![Select a form for the CMS element](images/admin-cms-form-selection.png)

## Plugin settings

Open **Extensions → My extensions → Form Builder 2 → Configure**. The general settings include logging, uploads and attachments, trimming and input length indicators. Modal settings control forms opened in a modal.

![General plugin settings](images/admin-plugin-config-general.png)

![Modal plugin settings](images/admin-plugin-config-modal.png)

## Output in the storefront

### Form validation

Field validation can combine browser checks with recursive server-side validation. Configure required fields, lengths, patterns and comparisons for the actual input types. Browser-only date, time, number and URL constraints have separate limits described in the feature overview.

### Sending an e-mail

Enable the `mail` action and choose recipients and templates in the form's email settings. The email can include the formatted form summary and configured attachments. Receipt confirmation and the Classic mail copy are separate actions.

## Security

- The formatted HTML summary escapes input values. Custom HTML/Twig and integrations still require configuration appropriate to their use; not every browser constraint has a corresponding server-side domain validator. See the [feature overview](https://docs.moori.net/en/plugin/MoorlForms/all-features/).
