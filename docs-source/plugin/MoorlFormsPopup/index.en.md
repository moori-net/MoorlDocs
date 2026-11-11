# Form Builder 2 | Exit-Intent-Popups Add-On

With this add-on for [Form Builder 2](https://docs.moori.net/en/plugin/MoorlForms/), you can open forms as popups on supported shop pages: the home page, product, category and landing pages, login, checkout confirmation and order completion. Settings control the trigger, delay and page selection.

## New form of type "Popup"

An active and available form of type `popup` is loaded on the configured supported pages. Its trigger determines when it opens. Custom controller pages, the cart and other account pages are not automatically covered by this add-on.

There are further settings for this form.

## Settings

As a rule, the same popup should not open again and again, unless you want to annoy your customers.
Use the option to show the popup only once per session!

Popups that open immediately can be perceived as annoying. Set a delay in seconds. Triggers are registered only after this delay; scroll, click and exit triggers still need the corresponding event to occur afterwards. Without a saved value, the storefront JavaScript uses 10 seconds.

Select a supported page type. If none is selected, the popup applies to all pages covered by the add-on. For products, categories and landing pages, you can additionally select specific records; an empty ID selection means all records of that page type. General form availability, such as sales channel, language, dates and rules, still applies.

You can open the popup for a specific event. If no event is selected,
the popup will open as an "Exit-Intent".

Available triggers are load (`onLoad`), first scroll (`onScroll`), exit intent (`onExit`) and clicking elements (`onClickElement`). For clicks, enter a valid CSS selector. It is evaluated after the delay, so elements inserted later do not automatically receive a listener. Exit intent uses the mouse leaving the document; no equivalent dedicated touch trigger is implemented.

“Only once per session” is enabled by default. The current source stores opened form IDs in `sessionStorage` under `moorl-fb-popup`. This is browser session storage, not a permanent record on the customer account. With this restriction disabled, click triggers can reopen the popup. Multiple matching popups are not coordinated through a shared queue.

## Borderless popups

You don't have to use the popup for forms, you can also display other content.
For example, a discount code if the customer leaves the order completion after a certain time?

You can easily customise the borderless popup.

Borderless mode removes the default header and footer buttons for cancel/submit. If the content is a form, add suitable submit and, where needed, close controls to the content. The add-on itself does not generate discount codes or perform newsletter registration; content and configured form actions determine the result. Newsletter registration requires the corresponding extension or integration.

This is what the popup could look like now!

## Ideas for using the popup

1. offer newsletter registration if the customer stays on the same page for 60 seconds.
2. offer discount code when the customer wants to leave the order completion.
3. feedback or rating form on the order confirmation.

and much more...

## Setup and technical limits

Open Content → Form Builder → a form, choose “Popup form”, then configure its popup settings under General. There is no separate popup navigation module. Technical administration routes are `moorl.fb.form.list` and `moorl.fb.form.detail`.

The popup uses the base plugin’s AJAX submission and available form elements. Remembering form input or saving a submission history is separate from remembering whether a popup was shown. The Slides add-on can provide content with several steps.

Technical details were checked against source code on 10 November 2026. Local build artifacts can differ from source; this does not certify a browser test or asset build.
