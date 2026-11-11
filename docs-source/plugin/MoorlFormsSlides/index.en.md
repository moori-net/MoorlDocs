# Form Builder 2 | Slides Add-On

With this add-on for [Form Builder 2](https://docs.moori.net/en/plugin/MoorlForms/) you can split forms into several steps in a visually appealing way. This plugin is the perfect addition to the Popup Add-On!

## Example forms for download

- [Slides Add-On](examples/slides-add-on.json)

## New element of type "Slides"

This element is very demanding in configuration, but also powerful in application.

Add a `slides` container and `slide` children inside it. Place the actual form fields inside those slides. These are the two element types registered by this add-on; it does not add a new form type. Popup is an optional companion, not a required dependency.

## Configuration

Name the back and forward buttons.

You can also set button CSS classes, enable scrolling to the form with an offset, hide disabled buttons and add a submit button for the final step. The submit label and class can be configured too. The editor initializes previous/next classes with `btn btn-light`, automatic scrolling as enabled and the offset as 60 pixels.

The stylesheet settings are essential for the element, here you can make the following
configurations here:

1. animations for the transitions
2. the minimum height (recommended)
3. the slides are similar to bootstrap rows, here I recommend to set the horizontal and vertical alignment to "centre".

Note: The CSS properties are transferred to the slide elements within the slide.
This way the properties are consistent and you can e.g. adjust the background colour per slide!

Rendering requires both populated CSS and transition configuration (`config.css` and `config.animateInOut`). A configuration notice appears if either is missing. Child values override inherited parent values. The slider uses gallery mode without looping, touch swiping or mouse dragging; previous/next controls change the step.

The element of the type "Slide" is the sub-element and can be used as often as you like.

Since the CSS properties are set by the parent element, you can optionally adjust these settings.

You can define a background image in the tab "Assignment".

Each slide element supports responsive sub-elements, use this setting to align the fields.

You can freely position the main components of the form.

## Output in the storefront

In this example I used the pop-up form. But the slides are also suitable for
CMS elements as well!

## Navigation and validation

When Next is clicked, the storefront JavaScript checks the active slide’s required fields with browser validation. The base plugin’s complete form and server validation still governs submission. Optional fields are not checked by this particular step-validation method.

On a step change, the heading uses the active slide’s name. The optional submit button is enabled when changing to the final slide. Arrange required fields and submit controls to match the intended sequence.

Classic conditions can hide slides; the Slides JavaScript skips a hidden slide during a transition. Slides does not provide its own condition configuration. Verify the specific combination in a browser, particularly if the first or last step can be hidden.

## Storage and setup

Structure and settings are stored as normal form elements in the base plugin. There is no separate storage of the current step, no server-side partial submission and no automatic restoration of the same slide after reloading. The base plugin’s input storage is a separate feature.

Start under Content → Form Builder → a form → Structure → Slides element; technical administration routes are `moorl.fb.form.detail` and `moorl.fb.form.element`. There is no separate Slides menu entry. The downloadable example is an active CMS form with the `mail` action; popup configuration values alone do not turn it into a popup form.

A separate `animation` element type is not registered by the current plugin. Slide transitions are available through the corresponding layout options.

These additions reflect a source review dated 10 November 2026; they do not certify a browser test or asset build.
