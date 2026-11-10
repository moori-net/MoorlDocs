---
description: Overview of the entire MoorlForms plugin family, checked against registered extensions and their processing paths.
tags:
- Shopware 6 Plugin
- Create forms
- Add-ons
---

# Form Builder 2 | All features

This overview covers the base plugin and all twelve add-ons available locally. Source review date: **10 November 2026**. It describes implemented features and their limitations. See the [audit report](plugin-audit.md) for administration checks, screenshots and outstanding runtime verification. Available configuration depends on the installed and active add-ons.

## Which plugin do I need?

| Plugin | Purpose | Main limitation |
| --- | --- | --- |
| **MoorlForms** | Form editor, CMS and test forms, input fields, layout, validation, email, receipt confirmation, media, entity mapping, import/export and a Flow event | Does not automatically record every submission in history; use Classic for that. |
| [Classic](../MoorlFormsClassic/index.md) | Conditions, repeaters, image selection, additional input fields, newsletter, email copy, history, print view and ICS | A printed record is not a legal certification. |
| [Popup](../MoorlFormsPopup/index.md) | Trigger forms on page load, scroll, exit intent or click | Automatic integration only on supported page types; once per browser session and form by default. |
| [Slides](../MoorlFormsSlides/index.md) | Split a form into navigable steps | Does not independently save the current step; existing animation fragments are not a regular animation element. |
| [Customer](../MoorlFormsCustomer/index.md) | Additional registration fields and editable forms in the customer account | Map existing customer properties/custom fields deliberately; does not create a new general customer database. |
| [CustomProducts](../MoorlFormsCustomProducts/index.md) | Product configuration, price options, quantity handling, file uploads and transfer to cart/order | Products are assigned through dynamic product groups; configure price logic and quantity behavior. |
| [Order](../MoorlFormsOrder/index.md) | Additional checkout information, optional order lock, storage on the order and output | The visible price option does not establish that cart price calculation is implemented. |
| [Product](../MoorlFormsProduct/index.md) | Product enquiries, button/modal and product information in forms | Hiding the buy button/price does not provide a general server-side purchase block. |
| [Csv](../MoorlFormsCsv/index.md) | Write submissions as CSV rows with mapped columns | Requires file storage and column configuration; not a complete form export including media. |
| [Hubspot](../MoorlFormsHubspot/index.md) | Submit form values to a configured HubSpot client/form | Requires the matching Foundation integration; an administration mapping alone does not confirm delivery. |
| [Mautic](../MoorlFormsMautic/index.md) | Submit data to existing Mautic forms | The target form determines contacts and subsequent actions; no separate contact CRUD in the Shopware administration. |
| [Webhook](../MoorlFormsWebhook/index.md) | Send form values to configured HTTP endpoints | Method, URL, format and mapping determine the actual request. A screenshot does not confirm delivery. |
| **MoorlFormsExample** | Developer example for custom extensions | Uses outdated method signatures in the current source; adapt them to the base contracts before activation. |

## Working in the administration

Start at **Content → Form Builder 2**. The list provides existing forms, creation, import and duplication. The detail view combines the element tree on the left with settings for the selected form or element.

1. Create a form or import JSON.
2. Set the technical name, translated display name, type and required actions.
3. Add layout and input elements in the tree. Available child types depend on the selected group.
4. Configure required fields, defaults, layout and assignments.
5. Activate and save the form.
6. For CMS use, replace an existing CMS element in the Shopping Experience with the form element and select the form.
7. Save the Shopping Experience separately and check the result in the relevant sales channel.

The base plugin supplies **one CMS element and no separate CMS block**. Its form selection targets CMS/test forms. The CMS configuration also provides four freely assignable values, `custom1` to `custom4`. Saving the Shopping Experience does not automatically save form settings.

### Form and element configuration

| Area | Options |
| --- | --- |
| General | Activation, technical name, translated name; type and action selection for forms; type, visibility and color for elements |
| Layout | CSS classes/properties, responsive Bootstrap layout, spacing and type-specific styling |
| Email | General/language-specific recipients and email template; separate receipt confirmation template; Classic adds email copies and further options |
| Assignment | Date range, sales channel, language, Rule Builder rule, customer group, delivery country, payment and shipping method, where supported by the type |
| Data mapping | Target entity, database storage and field mapping including existing custom fields; optionally use selection labels instead of technical values |
| Add-on areas | For example popup triggers, product selection, integration mapping, CSV/webhook settings or Classic history |

Technical names determine input names, conditions and data paths. They must be unique at the same payload level. Nested fields create paths such as `billingAddress.street`. Missing add-ons can hide settings and action providers; importing a form does not install them.

## Form types and integration

| Plugin | Technical type/integration | Behavior |
| --- | --- | --- |
| Base | `cms` | Independently submitted form in Shopping Experiences |
| Base | `test` | CMS test mode with additional options; technical provider errors are propagated |
| Base | Twig tag `{% fb_form 'technical_name' %}` | Embed a form in the theme using its technical name or ID; requires a sales channel context |
| Classic | `inline` | Embed additional fields in an existing form; the surrounding process must handle the data |
| Classic | `twig` | Additional Classic form type for theme integration; the Twig tag itself already belongs to the base plugin |
| Popup | `popup` | Triggered form on supported pages |
| Customer | `customer-register`, `customer-account` | Registration or a dedicated customer account area; target entity `customer` |
| CustomProducts | `custom-product` | Assigned product forms and transfer of their configuration to cart line items; target entity `order_line_item` |
| Order | `order` | Additional checkout information; target entity `order` |
| Product | `product-request` | Product enquiry; target entity `product` |

Twig integration belongs to the base plugin. Classic is needed for additional Classic features, not simply to render a form in a theme.

## Base elements

| Group | Elements/technical names | Purpose and configuration |
| --- | --- | --- |
| Rows | `form-row`, `row` | Responsive arrangement of input fields or sections, mobile-first inherited widths and order |
| Text | `text`, `textarea`, `tel`, `url` | Single-/multiline text, telephone and HTML URL input |
| Email | `email`, `email-secondary` | Email validation; primary email fields can provide a reply/confirmation address |
| Toggles | `checkbox`, `switch` | Individual yes/no inputs |
| Numbers | `number`, `number-range` | Number input or slider; HTML minimum, maximum and step |
| Date/time | `date`, `time` | HTML date/time with configurable limits; weekday exclusions for date inputs in the browser |
| Other inputs | `password`, `hidden`, `window-location` | Masked input, hidden value and current page address |
| File | `upload` | One file per field; size/MIME configuration, email attachment and optional media storage |
| Selection | `select`, `multiselect`, `checkbox-group`, `radio-group` | Manual or dynamic options; search availability depends on presentation |
| Options | `option` | Technical value, translated label and, depending on type, media/recipient/price |
| Structure | `section`, `card`, `html`, `nested-fields` | Sections, collapsible cards, HTML content and structured field names |
| Content | `image`, `cms-element` | Images and embedded CMS elements |
| Form parts | `form-submit`, `form-captcha`, `form-notice`, `form-tos`, `form-feedback` | Submission, Shopware captcha, notices, privacy confirmation and feedback |
| Internal | `root`, `test` | Root and technical test element; not separate business form types |

Depending on type, input fields support required status, placeholder, default value, minimum/maximum length, regex, comparison field, additional text/icon, tooltip, disabled presentation and floating label. Manage translated content through the administration language selector. HTML content is stored in the element translation; Twig translation snippets can also be used.

### Dynamic selection

The base plugin provides **countries**, **salutations** and **custom entities**. Countries can be filtered by sales channel. Classic adds product-related selection sources.

For custom entities, configure the entity name, label property, sort property, optional email property and filters. Each filter line follows `field=value`, for example:

```text
active=true
stock=0
```

At most **500 entries** are loaded; there is no server-side pagination or search across further results here. A searchable select therefore does not automatically search the entire database.

### Validation limits

The base plugin validates required values, text lengths/array counts, configured regex and field comparisons on the server. Email, password and upload types add their own checks. Browser validation applies in addition.

Date/time limits, weekday exclusions, number ranges/steps and the URL input type do not each have a complete server-side business validator in their corresponding classes. Add appropriate backend validation for binding business restrictions.

Checkbox groups already have browser-side min/max logic and a server-side `Count` path. Both normally apply through the required-field path; the MultiField validator skips optional groups early. The old TODO line therefore does not mean this feature is entirely absent.

## Actions, email and processing

| Plugin | Action | Requirement/result |
| --- | --- | --- |
| Base | `upload-files` | Save uploads in the media manager and provide media references for subsequent steps |
| Base | `mail` | Send a submission using the configured template to the resolved shop/form recipient |
| Base | `receipt-confirmation` | Receipt confirmation to a suitable populated primary email field; separate template, not an automatic complete data copy |
| Base | `event` | Trigger `moorl_form.submit` for configured Flows |
| Classic | `mail-copy` | Complete copy with its own template and optional customer choice |
| Classic | `write-history` | Store the submission for later administration viewing |
| Classic | `print-view` | Provide print output based on saved history |
| Classic | `subscribe-newsletter` | Run the optional newsletter process |
| Classic | `ics-attachment` | Prepare a calendar file for email attachments |
| Csv | `csv-form` | Write mapped values as a CSV row |
| Hubspot | `hubspot-form` | Submit values using a client/form mapping |
| Mautic | `mautic-form` | Submit values using a client/form mapping |
| Webhook | `webhook-form` | Make a request using the configured URL, method, format and mapping |

The action list selects active providers; execution order follows registration/priority. Uploads run with high priority before ordinary actions. An error in an available action is logged and collected; later actions are still attempted. The base plugin supplies no background queue or automatic retry.

| Result | Customer feedback |
| --- | --- |
| Invalid inputs | Error message and field violations; inputs can be corrected |
| Valid inputs, processing without a captured error | Configured success message |
| Valid inputs, error in an executed action/storage | Form submitted, but problems occurred during processing |
| Missing action provider | A `warning` log entry only; no customer warning is generated |
| Unexpected HTTP/JSON response in the browser | Submission could not be confirmed; inputs are retained |

An accepted submission resets the form even when processing warnings occur. Redirects are suppressed when there are warnings. See [processing results](processing-results.md) for details. The existing `FormActionDatabase` and `FormActionBlacklist` classes are not registered selectable base actions.

### Recipients, templates and attachments

Recipients can come from shop configuration, form configuration, form translations, a selected option or a mapped entity. `entityMailDetection` controls replacement/addition of an entity email address. Option-based routing must match the selection actually used.

Email templates receive the form data context. Examples:

```twig
{{ form.getPretty()|raw }}
{{ form.getPretty('plain') }}
{{ form.fieldName('email') }}
{{ form.fieldValue('billingAddress.street') }}
```

The HTML summary escapes data itself; this does not automatically make custom unchecked HTML safe. Password values are masked in formatted output. Media/file attachments depend on the selected process; `orderSendAttachments` for order emails is disabled by default.

## Add-ons in detail

### Classic

Classic adds AND-linked conditions with the operators `is`, `not`, `contains`, `isset`, `notset`, `gt`, `lt`, `gte`, `lte`; semicolon-separated values represent alternatives. Conditions affect visibility and server-side processing.

It also adds `form-send-copy`, `form-newsletter`, `repeater`, `rating`, `tax-id-number`, `signature`, `bic`, `iban`, `checkbox-slider`, `radio-slider`, `radio-grid`, `checkbox-media` and `radio-media`. No `checkbox-grid` is registered. An IBAN checksum does not confirm account ownership. Signature/print functionality does not establish a particular legal status.

Additional selection sources are `customer-group`, `customer-order`, `customer-address` and `product-stream`. Order/address sources refer to the logged-in customer; the product stream selection loads at most 50 products. A repeater renders a field group multiple times. Administration/browser defaults normally allow 1 to 10 repetitions; PHP applies 1 to 5 only when the entire `config.repeater` block is missing or empty. Configure the intended limits explicitly.

History and print output are separate steps that must be enabled. Print view requires saved history. Classic also provides the cookie declaration for draft storage implemented in the base plugin. [Setup and limitations](../MoorlFormsClassic/index.md).

Classic also adds redirect settings after submission without processing errors: reload, product, category, fixed URL or a Twig-based URL. The available account target type is treated as a reload by the current base controller. Processing warnings suppress the redirect so the feedback remains visible.

### Popup

Triggers are page load, scroll, exit intent and a click on a configured element. Borderless presentation and a custom CSS class are configurable. The standard template fixes size/alignment at `modal-lg modal-dialog-centered`; different sizes/positions require template/CSS changes. The JavaScript default waits ten seconds and records display per form in `sessionStorage`.

The subscriber integrates popups on navigation, product, landing page, login and checkout confirmation/finish pages. This does not cover every page type. Mobile availability depends on the trigger. [Setup](../MoorlFormsPopup/index.md).

### Slides

`slides` contains individual `slide` elements with previous/next navigation and step-specific input checks. This is form structure, not another form type. The current step is not saved independently. Animation fragments and the unregistered Slides service do not establish another available feature. [Setup](../MoorlFormsSlides/index.md).

Button labels and classes are configurable, as are automatic scrolling to the top (`autoScrollTop`, off by default), the top offset (`offsetTop`, default 60) and hiding disabled buttons (`hideButtons`). An optional submit button is enabled only in the final step. The container template requires both `config.css` and `config.animateInOut`; missing configuration can prevent output. Step validation checks required fields in the active step and does not replace final server-side validation.

### Customer

`customer-register` extends registration; `customer-account` supplies an editable form at `/account/form/{id}`. Inputs can be mapped to existing customer/custom-field properties. Registration and account updates have different lifecycles; successful storage does not confirm subsequent email/CRM processing. The registration event is `checkout.customer.moorl_form_register` and contains the first registration form. The supplied Flow has no actions yet; configure the required follow-up steps in Flow Builder. [Setup](../MoorlFormsCustomer/index.md).

### CustomProducts

Product forms are assigned through dynamic product groups. Configurations, including upload references, are transferred to cart line items and orders. Depending on type/configuration, price options can account for absolute/relative surcharges/discounts, numeric multipliers and product quantity. Not every option is always multiplied by every numeric factor.

For base value `B`, sum of option amounts `S` and numeric multiplier `M`, the initial calculation is `B × M + S` with `priceCalculationPriority` off, or `(B + S) × M` with it on. The setting of the first matching form determines which applies; the subsequent cart processing path handles price/tax calculation and product quantity.

Product selection, cart calculation and later order display are separate processing steps. [Price and quantity examples](../MoorlFormsCustomProducts/index.md).

### Order

Forms of type `order` collect additional checkout information. A product group can restrict applicability; without such an assignment a form can apply globally. `checkoutLock` is off by default, `remember` is on, and `addToDocuments` is off.

Inputs are cached per session and stored on the order after order creation. The current document override affects the delivery note. The administration summary appears in order details. The existing price UI does not calculate separate cart price items in this add-on. [Setup](../MoorlFormsOrder/index.md).

The event `moorl_form.order_placed` is triggered for each processed form; it does not provide its own `OrderAware`/order entity contract. Flow conditions and templates must use the event data actually offered.

### Product

`product-request` associates enquiry forms with products from dynamic product groups. The enquiry button/modal, price/buy-button presentation and product information are configurable. `keepProductUntouched=true` prevents product modifications by default. The UI does not provide a general API purchase block. [Setup](../MoorlFormsProduct/index.md).

Free selection of the form position or integration into a product tab is not implemented in the current add-on; the corresponding position selector is commented out.

### Csv, Hubspot, Mautic and Webhook

CSV writes mapped columns to a selected media file. Configuration is stored in `form.config.csv` with `csvId` and `mapping`; the normal separator is `;`, enclosure is `"`. The PHP path reads/writes locally under `public/<media.path>`. The current header-reading logic expects an additional empty final line, for example a header followed by two line breaks. The escape character offered in the administration is not used by the PHP writing path. Remote-only media storage is not covered by this local path.

CRM add-ons use the corresponding Foundation integration. Hubspot and Mautic use the integration mapping in the form with `clientId`, `formId` and `mapping`; mapping entries contain `name` and `data`, and form placeholders are written as, for example, `{{ email.value }}`. The earlier instruction to assign fields individually in element settings does not describe the current mapping UI.

Webhook creates HTTP requests from form configuration. The UI offers GET/POST, optional Basic authentication, query parameters, headers and POST bodies as an empty body, raw text, JSON or URL-encoded form data. Mapping values and an optional global template are rendered with Twig during normal execution; the destination URL and raw text body are not rendered. Request and connection timeout are each ten seconds. The test button actually sends to the destination, but does not resolve form/Flow Twig values. Its text output can show “No content” because the response body has already been read for logging.

These paths are independent: CSV storage is not CRM transfer, and accepting a form does not guarantee successful external delivery. Webhook catches HTTP errors internally, so they do not automatically reach the base plugin's processing report. CRM mapping skips entries with PHP-empty `data`, including text `"0"`. Verify the actual integration separately even after successful form acceptance.

The Flow actions `action.write.csv`, `action.send.hubspot`, `action.send.mautic` and `action.send.webhook` are also registered. They require an appropriate `MailAware` Flow context; this is a separate entry point from the direct form action. These four add-ons register no form types of their own. Historical `*-contact` checks in the administration do not establish another provider.

Details: [CSV](../MoorlFormsCsv/index.md), [Hubspot](../MoorlFormsHubspot/index.md), [Mautic](../MoorlFormsMautic/index.md), [Webhook](../MoorlFormsWebhook/index.md).

### Example and custom extensions

`MoorlFormsExample` demonstrates a form type, an action and an element (each named `example`), plus administration/product extensions. It registers no selection source of its own. Some current method signatures do not match the base plugin. It is therefore not a reference plugin that can be activated without prior verification.

Custom extensions require PHP implementation **and** DI registration, plus administration imports, translations and Twig templates where needed:

| Extension | Tag | Contract |
| --- | --- | --- |
| Form type | `moorl.fb.form` | `FormTypeInterface` |
| Action | `moorl.fb.action` | `FormActionInterface` |
| Element | `moorl.fb.element` | `ElementTypeInterface` |
| Selection source | `moorl.fb.selection` | `ElementSelectionInterface` |

Each plugin's `CODEX.md` documents the actual methods and integration points. An option name or an existing PHP file alone does not enable a feature.

## Data, export and drafts

The visible export button downloads a **JSON file with a filename extension**. Forms, elements and loaded translations use a shared payload. Import/duplication reassigns IDs and tree relationships. JSON import removes media references; media files are not included in JSON.

A ZIP export service with media/language options is implemented; its dialog button is commented out in the current detail view. JSON and ZIP features must therefore not be described as identical visible workflows.

Entity mapping writes configurable inputs and summaries to existing DAL entities, including custom fields. It is not a free-form SQL editor. Required target attributes must receive valid values.

The base plugin stores drafts only with `moorl-fb-store` consent; Classic supplies its cookie entry. Sending failures retain the draft; reset/accepted submission removes it. Passwords are not stored; file, hidden, disabled and read-only fields are not restored. URL parameters can prefill fields, including multiple selections. The `context` defaults supported by the ordinary input template can be loaded asynchronously for logged-in customers. Hidden fields instead render Twig synchronously; textareas currently do not carry the asynchronous marker. See the [how-tos](how-tos.en.md) for the precise scope.

## Plugin-wide settings

| Key | Default/effect |
| --- | --- |
| `loggerLevel` | `400` (ERROR); set WARNING `300` or lower to see missing-provider warnings |
| `orderSendAttachments` | `false`; upload attachments in order confirmation emails |
| `entityMailDetection` | No explicit XML default; `no`, `yes-replace` or `yes-append` |
| `showLength` | `true`; length indicator enabled |
| `showLengthType` | `text`; alternative `progress-bar` |
| `trimStringValues` | `false`; trim surrounding whitespace from submitted strings |
| `modalStaticLoad` | `true`; load modal content statically |
| `modalDialogSize` | `modal-md` |
| `modalDialogOrientation` | `modal-dialog-auto` |
| `ignoreCustomFieldSet` | `false`; normally include demo custom fields during updates |

## Further reading

- [Main page](index.en.md), [how-tos](how-tos.en.md) and [FAQ](faq.en.md)
- [Processing results](processing-results.md)
- [Documentation audit and administration screenshots](plugin-audit.md)
- [English administration screenshots in Full HD](admin-screenshots.en.md)
- [German feature overview](all-features.md)

Technical details, limitations and implementation findings that have not yet been reproduced are recorded in each plugin's `CODEX.md`. The empty autocomplete endpoint, unregistered placeholders and old demos are not counted as ready-to-use features.
