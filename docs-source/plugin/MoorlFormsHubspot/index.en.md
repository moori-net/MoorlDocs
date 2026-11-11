# Hubspot Forms Integration

This extension is compatible with [Form Construction Kit 2](https://docs.moori.net/en/plugin/MoorlForms/)!

## Installation

!!! note

    If you have any problems with the plugin, please note the following [notes](https://docs.moori.net/en/plugin/) in the FAQ section.

1. install
   [Foundation](https://docs.moori.net/en/plugin/MoorlFoundation/)
2. install Hubspot Forms Integration in the Plugin Manager

## Setup

The extension submits mapped values to an existing HubSpot form. Its HubSpot configuration determines subsequent contact handling, notifications and automations. The plugin does not implement separate ticket management or file uploads.

The HubSpot menus below are historical setup examples and have not been checked against a current external HubSpot interface.

### Create a Hubspot account

You can create a Hubspot account relatively easily. For example, use your Google account and choose a free plan!

### Create a private Hubspot app

- Go to "Profile & Settings".
- Create a new app in the left sidebar under "Account setup" -> "Integration" -> "Private apps".
- The app needs the following permissions: forms-uploaded-files, forms, crm.objects.contacts.write, crm.objects.contacts.read
- Copy the token and switch to the Shopware Admin.

### Create a Hubspot client in Shopware

- Navigate to "Settings" -> "Extensions" -> "moori Clients"
- Create a new client of type “Hubspot” (technical type `api-hubspot`)
- Enter the token of your private Hubspot app
- You will find the portal ID in the account menu of Hubspot under your username.
- Test the client

### Create a form in Hubspot

- Navigate from the main menu in Hubspot to "Marketing" -> "Forms"
- Create a new form of the type "Embedded", you can use the template for contact forms for testing purposes.
- Save the form without making any changes

With this form, contacts are automatically created in Hubspot as soon as it is filled in and submitted.

### Connect Hubspot form with flow builder

- Navigate to the flow builder and open e.g. "Contact form has been sent".
- Go to the "Flow" tab
- Add the action "Send to Hubspot form".
- Select your Hubspot client
- Select your form created in Hubspot
- Create the data mappings, in our example you can use the placeholders for "Flow with contact".

Check mappings against the data of the selected Flow event. This integration does not catch Twig or HTTP errors, so processing can fail. Missing or entirely empty mappings instead skip submission.

### Connect Hubspot form with Form Builder 2 form

- Open your form in the Shopware Admin
- In the basic settings of the form, select the option "Send to Hubspot form" under "Form actions".
- Open the **Hubspot** tab in the form settings
- Select your Hubspot client
- Select the form you created in Hubspot
- Assign the available target fields directly in the central mapping table
- Use form placeholders with a technical field name and `.value`, for example `{{ email.value }}`
- Assign further fields such as first name, last name and message, then save the form

The current implementation does not assign individual Hubspot fields in the element settings.

## Technical scope

The form action is `hubspot-form`; the Flow action is `action.send.hubspot` and requires `MailAware`. Both use `clientId`, `formId` and `mapping`; new form mappings start with `null`, `null` and `[]`. The credentials `token` and `portalId` belong to the Foundation client.

The form list is read from `/marketing/v3/forms/`. Mapped values are rendered with Twig and sent to the secure HubSpot form submission endpoint. Flow placeholders refer to available event data, for example `{{ contactFormData.email }}`. Empty mapping values are omitted, including plain text `0` under PHP's empty-value check.

The integration does not implement file handling, separate contact/ticket management or automatic pagination of the form list. The Foundation client's connection test reads contacts, so it checks a different API path from form submission. The first successfully initialized client remains in the service; different clients in one service lifetime require separate verification.

The scope names above come from the existing setup documentation and Foundation client. They are not an externally verified statement of the permissions currently required by HubSpot.

## Test

After a deliberate submission to your designated test account, check the form submission and mapped values in HubSpot. An email is sent only if the relevant notifications or automations are configured in HubSpot; the plugin does not guarantee one.
