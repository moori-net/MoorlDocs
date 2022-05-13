---
description: This plugin is based on a fundamental redevelopment of the form builder and offers maximum flexibility and integrity for Shopware 6.
tags:
- Shopware 6 Plugin
- Build forms
- B2B
- Send E-Mail
---

# Form Builder 2 | Base Version

This plugin is based on a fundamental redevelopment of the [Form Builder](../MoorlFormBuilder/index.md) and offers maximum flexibility and integrity for Shopware 6.

!!! note "Note for all customers who already own the Form Builder"

    This plugin has a fundamentally different structure and does not offer the possibility to migrate the previous forms.
          
    Unfortunately, it is also not possible to duplicate/transfer the subscriptions after consultation with Shopware.
          
    Since I don't want to put my existing customers at a disadvantage, the form construction kit will continue to be provided with updates. But no new functions will be developed.
          
    For all interested parties with active subscriptions I offer a 50% voucher for Basis and Add-Ons.
    
    The voucher is issued individually and cannot be combined with discount campaigns.

## Example forms for download

- [Simple contact form](examples/simple-contact-form.json)

## Add-Ons

This plugin has been shortened in its basic version by some functions, so that it can be offered at an affordable price.
affordable price. All further functions can be obtained.

It is also possible to create your own add-ons, a developer documentation will follow soon.

1. [Classic Add-On](../MoorlFormsClassic/index.md): Contains all functions of the [Form Builder](../MoorlFormBuilder/index.md).
2. [Exit-Intent-Popups Add-On](../MoorlFormsPopup/index.md): Use forms as popup
3. [Slides Add-On](../MoorlFormsSlides/index.md): Use slides
4. [Customer-Forms Add-On](../MoorlFormsCustomer/index.md): Customised forms for registration and customer area
5. [Product-Configurator Add-On](../MoorlFormsCustomProducts/index.md): Additional information on products incl. price calculation
6. Order Add-On**: Additional order details incl. price calculation on the shopping basket
7. [Product-Request Add-On](../MoorlFormsProduct/index.md): Product-specific enquiry forms
8. customer-specific add-ons on request

(\* In development, \*\* In concept phase)

## Example Add-On for developers

[Example Add-On](https://github.com/moorl/MoorlFormsExample)

## What is this plugin good for?

The Shopware 6 _Form Builder 2_ plugin makes it child's play to create complex forms with independent
task areas.

It is modular, so processes and individual fields can be expanded as desired.

## Installation

!!! note

    If you have any problems with the plugin, please note the following [notes](../) in the FAQ section.

1. install
   [Foundation](../MoorlFoundation/index.md)
2. install Form Builder 2 in the Plugin Manager
3. go to: Contents | Form Builder 2

Here you can create or import a new form.

## Settings

### Basic configuration

![](images/fb-01.jpg)

![](images/fb-02.jpg)

1. create new form
2. import

![](images/fb-03.jpg)

1. form settings
2. save form
3. export
4. structure area of the form elements
5. settings area (form/element)

![](images/fb-04.jpg)

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

![](images/fb-05.jpg)

#### Layout and stylesheet settings

You can assign stylesheet attributes to each form/element.

The CSS options vary depending on the type of form/element.

![](images/fb-06.jpg)

### Settings for elements

#### Field configuration

All elements from the Field and Multi-Field group can have additional properties in this configuration.

![](images/fb-07.jpg)

#### Selection Configuration

All elements from the Multi-Field group can receive database-specific values. Add-ons offer more possibilities here.

![](images/fb-08.jpg)

#### Responsive behaviour

If the parent element is from the Rows group, all elements contained in it can be given responsive properties.
The rule "Mobile-First" applies here, the properties are always passed on.

The distribution is as follows.

Viewport (xs to xxl) | Inherited (Yes/No) | Display (Yes/No) | Width | Sorting/Arrangement

![](images/fb-09.jpg)

#### Configuration Upload Field

![](images/fb-10.jpg)

#### Configuration Date

![](images/fb-11.jpg)

#### Configuration Time

![](images/fb-12.jpg)

#### Configuration number

![](images/fb-13.jpg)

#### Configuration HTML (language related)

![](images/fb-14.jpg)

#### Configuration Card Section

![](images/fb-15.jpg)

### Settings for forms

#### Configuration e-mail

Here you can configure the e-mail recipient. If no value is entered, the shop's standard e-mail address will be used.
of the shop is used.

The function "Send copy" and "Recipient according to selection condition" are available in the Classic Add-On!

![](images/fb-16.jpg)

![](images/fb-17.jpg)

## CMS settings

The form does not have its own block, but can be accessed via the "Replace element" icon!

After the CMS element has been inserted, you can assign forms of type CMS or Test to the CMS page.

![](images/fb-22.jpg)

## Output in the storefront

### Form validation

The example form is of type "Test" the client-side validation is deactivated.
The Form Builder 2 supports recursive server-side validation of the input fields!

![](images/fb-18.jpg)

The client-side validation is active again. Now the form is validated twice.

![](images/fb-19.jpg)

### Sending an e-mail

In this example I show you how the e-mail is sent in the standard.

![](images/fb-20.jpg)

![](images/fb-21.jpg)

## Security

- HTML tags are masked to prevent harmful scripts.
