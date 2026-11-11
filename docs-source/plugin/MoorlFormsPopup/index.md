# Formular Baukasten 2 | Exit-Intent-Popups Add-On

Mit diesem Add-On für [Formular Baukasten 2](https://docs.moori.net/plugin/MoorlForms/) kannst du Formulare auf den unterstützten Shopseiten als Popup öffnen. Verfügbar sind Startseite, Produkt-, Kategorie- und Landingpages, Login, Bestellabschluss und Bestellbestätigung. Dazu gibt es Einstellungen für Auslöser, Wartezeit und Seitenauswahl.

## Neues Formular von Typ "Popup"

Ein verfügbares, aktives Formular vom Typ `popup` wird auf den konfigurierten unterstützten Shopseiten geladen. Wann es sich öffnet, bestimmt das gewählte Ereignis. Eigene Controllerseiten, Warenkorb und weitere Accountseiten werden vom Add-on nicht automatisch eingebunden.

Zu diesem Formular gibt es weitere Einstellungen.

## Einstellungen

In der Regel sollte sich dasselbe Popup nicht immer wieder öffnen, außer man möchte seine Kunden verärgern.
Nutze dazu die Option, das Popup nur einmalig pro Sitzung anzuzeigen!

Popups, die sich unmittelbar öffnen, können als störend empfunden werden. Lege eine Verweildauer in Sekunden fest. Erst nach dieser Wartezeit werden die Auslöser registriert; für Scroll-, Klick- oder Exit-Ereignisse muss das passende Ereignis anschließend noch eintreten. Ohne gespeicherten Wert verwendet das Storefront-JavaScript 10 Sekunden.

Wähle eine unterstützte Seitenart, auf der das Popup geöffnet wird. Ist keine Seitenart ausgewählt, gilt es für alle vom Add-on unterstützten Seiten. Für Produkte, Kategorien und Landingpages kann die Auswahl zusätzlich auf bestimmte Datensätze begrenzt werden; eine leere ID-Auswahl bedeutet alle Datensätze der jeweiligen Seitenart. Die allgemeinen Formularzuweisungen wie Verkaufskanal, Sprache, Zeitraum und Regeln gelten weiterhin.

Du kannst das Popup zu einem bestimmten Event öffnen. Sofern kein Event gewählt wurde,
wird das Popup sich als "Exit-Intent" öffnen.

Zur Auswahl stehen Laden (`onLoad`), erstes Scrollen (`onScroll`), Exit-Intent (`onExit`) und Klick auf Elemente (`onClickElement`). Beim Klick gibst du einen gültigen CSS-Selektor an. Der Selektor wird nach der Wartezeit ausgewertet; erst später eingefügte Elemente erhalten dadurch nicht automatisch einen Listener. Exit-Intent basiert auf dem Verlassen des Dokuments mit der Maus und bietet keinen eigenen gleichwertigen Touch-Auslöser.

„Nur einmal pro Sitzung“ ist standardmäßig eingeschaltet. Der aktuelle Sourcecode merkt bereits geöffnete Formular-IDs in `sessionStorage` unter `moorl-fb-popup`. Das ist der Sitzungsspeicher des Browsers, keine dauerhafte Speicherung am Kundenkonto. Ohne diese Einschränkung können Klickauslöser das Popup erneut öffnen. Mehrere passende Popups werden nicht über eine gemeinsame Warteschlange koordiniert.

## Randlose Popups

Du musst das Popup nicht zwingend für Formulare nutzen, sondern kannst auch andere Inhalte anzeigen.
Zum Beispiel einen Rabatt-Code, wenn der Kunde nach einer bestimmten Zeit den Bestellabschluss verlässt?

Das randlose Popup kannst du leicht individualisieren.

Randlos blendet den Standardheader und die Footerbuttons Abbrechen/Absenden aus. Wenn der Inhalt ein Formular bleiben soll, ergänze passende Absende- und gegebenenfalls Schließen-Elemente im Inhalt. Das Add-on selbst erzeugt keinen Rabattcode und keine Newsletteraktion; Inhalt und Formularaktionen bestimmen das Ergebnis. Eine Newsletter-Anmeldung benötigt die entsprechende Erweiterung beziehungsweise Integration.

So könnte das Popup nun aussehen!

## Ideen zum Einsatz des Popups

1. Newsletter Anmeldung anbieten, wenn der Kunde 60 Sekunden auf derselben Seite verweilt.
2. Rabatt-Code anbieten, wenn der Kunde den Bestellabschluss verlassen will.
3. Feedback- oder Bewertungsformular auf der Bestellbestätigung.

uvm...

## Einrichtung und technische Grenzen

Öffne Inhalte → Formular Baukasten → Formular, wähle den Typ „Popup-Formular“ und konfiguriere unter Allgemein die Popup-Einstellungen. Es gibt keinen separaten Popup-Menüpunkt. Technische Adminrouten sind `moorl.fb.form.list` und `moorl.fb.form.detail`.

Das Popup verwendet den normalen AJAX-Versand und die verfügbaren Formularelemente des Basisplugins. Das Speichern von Formulareingaben oder ein Einsendeverlauf ist von der einmaligen Anzeige des Popups getrennt. Für mehrstufige Inhalte kann zusätzlich das Slides-Add-on verwendet werden.

Die technischen Angaben wurden am 10.11.2026 mit dem Sourcecode abgeglichen. Lokal vorhandene Buildartefakte können vom Sourcecode abweichen; dies ist keine Bestätigung eines Browser- oder Assetbuild-Tests.
