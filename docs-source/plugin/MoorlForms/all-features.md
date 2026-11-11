---
description: Funktionsübersicht der gesamten MoorlForms-Pluginfamilie, abgeglichen mit registrierten Erweiterungen und ihren Verarbeitungspfaden.
tags:
- Shopware 6 Plugin
- Formulare erstellen
- Add-Ons
---

# Formular Baukasten 2 | Alle Features

Diese Übersicht beschreibt die Basis und alle zwölf lokal vorhandenen Add-ons. Stand des Quellcodeabgleichs: **10. November 2026**. Sie beschreibt verfügbare Implementierungen und deren Grenzen. Die Konfiguration richtet sich nach den installierten und aktiven Add-ons.

## Welches Plugin benötige ich?

| Plugin | Aufgabe | Wichtige Grenze |
| --- | --- | --- |
| **MoorlForms** | Formulareditor, CMS- und Testformulare, Eingabefelder, Layout, Validierung, Mail, Empfangsbestätigung, Medien, Entity-Mapping, Import/Export und Flow-Ereignis | Keine automatische Ablage aller Einsendungen im Verlauf; dafür Classic verwenden. |
| [Classic](https://docs.moori.net/plugin/MoorlFormsClassic/) | Bedingungen, Repeater, Bildauswahl, zusätzliche Eingabefelder, Newsletter, Mailkopie, Verlauf, Druckansicht und ICS | Ein Druckprotokoll ist keine rechtliche Zertifizierung. |
| [Popup](https://docs.moori.net/plugin/MoorlFormsPopup/) | Formulare durch Laden, Scrollen, Verlassen oder Klick auslösen | Automatische Einbindung nur auf unterstützten Seitentypen; standardmäßig einmal pro Browsersitzung und Formular. |
| [Slides](https://docs.moori.net/plugin/MoorlFormsSlides/) | Formular in navigierbare Schritte aufteilen | Keine eigenständige Speicherung des aktuellen Schritts; vorhandene Animationsfragmente sind kein reguläres Animation-Element. |
| [Customer](https://docs.moori.net/plugin/MoorlFormsCustomer/) | Zusätzliche Registrierungseingaben und bearbeitbare Formulare im Kundenkonto | Vorhandene Kundenfelder/Custom Fields gezielt zuordnen; keine neue allgemeine Kundendatenbank. |
| [CustomProducts](https://docs.moori.net/plugin/MoorlFormsCustomProducts/) | Produktkonfiguration, Preisoptionen, Mengenbezug, Datei-Uploads und Weitergabe in Warenkorb/Bestellung | Produktzuordnung erfolgt über dynamische Produktgruppen; Preislogik und Mengenverhalten konfigurieren. |
| [Order](https://docs.moori.net/plugin/MoorlFormsOrder/) | Zusätzliche Checkout-Angaben, optionale Bestellsperre, Speicherung an der Bestellung und Ausgabe | Die sichtbare Preisoption belegt keine implementierte Warenkorbpreisberechnung. |
| [Product](https://docs.moori.net/plugin/MoorlFormsProduct/) | Produktbezogene Anfragen, Button/Modal und Produktinformationen im Formular | Kaufbutton/Preis ausblenden ist keine allgemeine serverseitige Kaufsperre. |
| [Csv](https://docs.moori.net/plugin/MoorlFormsCsv/) | Einsendungen als CSV-Zeilen mit zugeordneten Spalten schreiben | Dateiablage und Spaltenkonfiguration einrichten; kein vollständiger Formularexport mit Medien. |
| [Hubspot](https://docs.moori.net/plugin/MoorlFormsHubspot/) | Formularwerte an einen konfigurierten HubSpot-Client/Formularablauf übergeben | Benötigt die passende Foundation-Integration; Admin-Mapping allein bestätigt keine erfolgreiche Zustellung. |
| [Mautic](https://docs.moori.net/plugin/MoorlFormsMautic/) | Daten an vorhandene Mautic-Formulare übermitteln | Welche Kontakte und Folgeaktionen entstehen, bestimmt das Ziel-Formular; kein eigener Kontakt-CRUD im Shopware-Admin. |
| [Webhook](https://docs.moori.net/plugin/MoorlFormsWebhook/) | Formularwerte an konfigurierte HTTP-Endpunkte senden | Methode, URL, Format und Zuordnung bestimmen den tatsächlichen Request. Kein automatischer Zustellnachweis durch einen Screenshot. |
| **MoorlFormsExample** | Entwicklerbeispiel für eigene Erweiterungen | Im aktuellen Stand veraltete Methodensignaturen; vor Aktivierung an die Basisverträge anpassen. |

## In der Administration arbeiten

Einstieg: **Inhalte → Formular Baukasten 2**. Die Liste bietet vorhandene Formulare, Neuanlage, Import und Duplizieren. Die Detailansicht kombiniert links den Elementbaum mit den Einstellungen des ausgewählten Formulars oder Elements.

1. Formular erstellen oder JSON importieren.
2. Technischen Namen, übersetzten Anzeigenamen, Typ und gewünschte Aktionen bestimmen.
3. Layout und Eingabefelder im Baum anlegen. Untergeordnete Typen hängen von der gewählten Gruppe ab.
4. Pflichtfelder, Standardwerte, Layout und Zuweisungen einstellen.
5. Formular aktivieren und speichern.
6. Für CMS-Nutzung in der Erlebniswelt ein vorhandenes CMS-Element gegen das Formularelement austauschen und dort das Formular wählen.
7. Die Erlebniswelt zusätzlich speichern und das Ergebnis im passenden Verkaufskanal prüfen.

Das Basisplugin liefert **ein CMS-Element und keinen eigenen CMS-Block**. Seine Auswahl ist auf CMS-/Testformulare ausgerichtet. Die CMS-Konfiguration besitzt zusätzlich vier frei belegbare Werte `custom1` bis `custom4`. Eine Formulareinstellung wird durch Speichern der Erlebniswelt nicht automatisch mitgespeichert.

### Formular- und Elementkonfiguration

| Bereich | Möglichkeiten |
| --- | --- |
| Allgemein | Aktivierung, technischer Name, übersetzter Name; bei Formularen Typ und Aktionsauswahl; bei Elementen Typ, Sichtbarkeit und Farbe |
| Layout | CSS-Klassen, CSS-Eigenschaften, responsive Bootstrap-Aufteilung, Abstände und typspezifische Gestaltung |
| Mail | Empfänger allgemein/sprachbezogen und Mailtemplate; getrennte Vorlage für Empfangsbestätigung; Classic ergänzt Mailkopie und weitere Optionen |
| Zuweisung | Zeitraum, Verkaufskanal, Sprache, Rule-Builder-Regel, Kundengruppe, Lieferland, Zahlungs- und Versandart, soweit für den Typ freigegeben |
| Datenzuordnung | Ziel-Entity, Datenbankspeicherung und Feldzuordnung einschließlich vorhandener Custom Fields; Auswahllabel statt technischem Wert optional |
| Add-on-Bereiche | Beispielsweise Popup-Trigger, Produktauswahl, Integrationsmapping, CSV-/Webhook-Einstellungen oder Classic-Verlauf |

Technische Namen bestimmen Eingaben, Bedingungen und Datenpfade. Innerhalb derselben Nutzdatenebene müssen sie eindeutig sein. Verschachtelte Felder erzeugen Pfade wie `billingAddress.street`. Fehlende Add-ons können Einstellungen und Aktionsprovider ausblenden, ohne dass ein Import sie automatisch nachinstalliert.

## Formulartypen und Einbindung

| Plugin | Technischer Typ / Einbindung | Verhalten |
| --- | --- | --- |
| Basis | `cms` | Eigenständig absendbares Formular in Erlebniswelten |
| Basis | `test` | CMS-Testbetrieb mit erweiterten Optionen; technische Providerfehler werden durchgereicht |
| Basis | Twig-Tag `{% fb_form 'technical_name' %}` | Formular über technischen Namen oder ID im Theme einbinden; ein Verkaufskanalkontext ist erforderlich |
| Classic | `inline` | Zusätzliche Felder in ein bestehendes Formular einbetten; der umgebende Ablauf muss die Daten verarbeiten |
| Classic | `twig` | Zusätzlicher klassischer Formulartyp für die Theme-Einbindung; der Twig-Tag selbst gehört bereits zur Basis |
| Popup | `popup` | Triggergesteuertes Formular auf unterstützten Seiten |
| Customer | `customer-register`, `customer-account` | Registrierung bzw. eigener Bereich im Kundenkonto, Ziel-Entity `customer` |
| CustomProducts | `custom-product` | Zugeordnete Formulare am Produkt und Weitergabe der Konfiguration an Warenkorbpositionen, Ziel-Entity `order_line_item` |
| Order | `order` | Zusätzliche Angaben im Checkout, Ziel-Entity `order` |
| Product | `product-request` | Produktbezogene Anfrage, Ziel-Entity `product` |

Die Twig-Einbindung gehört zur Basis. Classic wird für zusätzliche Classic-Funktionen benötigt, nicht allein für das Rendern eines Formulars im Theme.

## Elemente der Basis

| Gruppe | Elemente / technische Namen | Zweck und Anpassung |
| --- | --- | --- |
| Zeilen | `form-row`, `row` | Responsive Anordnung von Eingabefeldern bzw. Sektionen, mobile-first vererbte Breiten und Reihenfolge |
| Text | `text`, `textarea`, `tel`, `url` | Ein-/mehrzeilige Eingaben, Telefon und HTML-URL-Feld |
| E-Mail | `email`, `email-secondary` | E-Mail-Prüfung; primäre Mailfelder können als Antwort-/Bestätigungsadresse dienen |
| Schalter | `checkbox`, `switch` | Einzelne Ja-/Nein-Eingaben |
| Zahlen | `number`, `number-range` | Zahlenfeld bzw. Schieberegler; HTML-Minimum, -Maximum und Schrittweite |
| Datum/Zeit | `date`, `time` | HTML-Datum/Zeit mit konfigurierbaren Grenzen; Wochentage bei Datum im Browser ausschließen |
| Weitere Eingaben | `password`, `hidden`, `window-location` | Maskierte Eingabe, versteckter Wert und aktuelle Seitenadresse |
| Datei | `upload` | Eine Datei pro Feld; Größen-/MIME-Konfiguration, Mailanhang und optional Medienablage |
| Auswahl | `select`, `multiselect`, `checkbox-group`, `radio-group` | Manuelle oder dynamische Optionen; Suchbarkeit abhängig von der Darstellung |
| Optionen | `option` | Technischer Wert, übersetzte Beschriftung, typspezifisch Medien/Empfänger/Preis |
| Struktur | `section`, `card`, `html`, `nested-fields` | Sektionen, aufklappbare Karten, HTML-Inhalte und strukturierte Feldnamen |
| Inhalte | `image`, `cms-element` | Bilder und eingebettete CMS-Elemente |
| Formularteile | `form-submit`, `form-captcha`, `form-notice`, `form-tos`, `form-feedback` | Absenden, Shopware-Captcha, Hinweistext, Datenschutzbestätigung und Rückmeldungen |
| Intern | `root`, `test` | Wurzel und technischer Testtyp; keine eigenständigen fachlichen Formulartypen |

Eingabefelder besitzen je nach Typ Pflichtstatus, Platzhalter, Standardwert, minimale/maximale Länge, Regex, Vergleichsfeld, Zusatztext/Icon, Tooltip, deaktivierte Darstellung und Floating Label. Übersetzbare Inhalte werden über den Admin-Sprachwechsel gepflegt. HTML-Inhalte liegen in der Elementübersetzung; Twig-Übersetzungsbausteine sind zusätzlich möglich.

### Dynamische Auswahl

Die Basis stellt **Länder**, **Anreden** und **eigene Entities** bereit. Bei Ländern kann nach Verkaufskanal gefiltert werden. Classic ergänzt produktbezogene Auswahl.

Für eigene Entities werden Entityname, Beschriftungsattribut, Sortierattribut, optional ein Mailattribut und Filter konfiguriert. Pro Zeile gilt `feld=wert`, beispielsweise:

```text
active=true
stock=0
```

Es werden höchstens **500 Einträge** geladen; es gibt hier keine serverseitige Pagination oder Suche über weitere Treffer. Ein suchbares Select sucht deshalb nicht automatisch in der gesamten Datenbank.

### Grenzen der Validierung

Die Basis validiert serverseitig Pflichtstatus, Textlängen/Array-Anzahl, konfigurierte Regex und Feldvergleiche. E-Mail, Passwort und Upload ergänzen eigene Prüfungen. Browservalidierung kommt zusätzlich hinzu.

Datum-/Zeitgrenzen, Wochentagausschlüsse, Zahlenbereich/Schrittweite und der URL-Eingabetyp sind in den betreffenden Klassen keine jeweils vollständigen serverseitigen Fachvalidatoren. Für verbindliche fachliche Einschränkungen sind passende Backend-Prüfungen erforderlich.

Checkbox-Gruppen besitzen bereits Min-/Max-Logik im Browser und einen serverseitigen `Count`-Pfad. Beide greifen regulär im Pflichtfeldpfad; optionale Gruppen werden im MultiField-Validator früh übersprungen. Die alte TODO-Zeile bedeutet daher nicht, dass die Funktion vollständig fehlt.

## Aktionen, Mail und Verarbeitung

| Plugin | Aktion | Voraussetzung / Ergebnis |
| --- | --- | --- |
| Basis | `upload-files` | Uploads im Medienmanager speichern und Medienreferenzen für Folgeschritte bereitstellen |
| Basis | `mail` | Einsendung mit konfigurierter Vorlage an ermittelten Shop-/Formularempfänger senden |
| Basis | `receipt-confirmation` | Empfangsbestätigung an geeignetes ausgefülltes primäres Mailfeld; eigene Vorlage, keine automatische vollständige Datenkopie |
| Basis | `event` | Ereignis `moorl_form.submit` für konfigurierte Flows auslösen |
| Classic | `mail-copy` | Vollständige Kopie mit eigenem Template und optionaler Kundenauswahl |
| Classic | `write-history` | Einsendung für spätere Admin-Ansicht ablegen |
| Classic | `print-view` | Auf gespeichertem Verlauf basierende Druckausgabe anbieten |
| Classic | `subscribe-newsletter` | Optionalen Newsletterablauf ausführen |
| Classic | `ics-attachment` | Kalenderdatei für Mailanhänge aufbereiten |
| Csv | `csv-form` | Zugeordnete Werte als CSV-Zeile schreiben |
| Hubspot | `hubspot-form` | Werte mit Client-/Formularzuordnung übertragen |
| Mautic | `mautic-form` | Werte mit Client-/Formularzuordnung übertragen |
| Webhook | `webhook-form` | Request anhand konfigurierter URL, Methode, Format und Mapping ausführen |

Die Aktionsliste wählt aktivierte Provider; ihre Ausführungsreihenfolge folgt der Registrierung/Priorität. Uploads laufen mit hoher Priorität vor normalen Aktionen. Ein Fehler einer verfügbaren Aktion wird geloggt und gesammelt; nachfolgende Aktionen werden weiterhin versucht. Die Basis liefert keine Hintergrundwarteschlange und keinen automatischen Retry.

| Ergebnis | Kundenrückmeldung |
| --- | --- |
| Eingaben ungültig | Fehlermeldung und Feldverletzungen; Eingaben können korrigiert werden |
| Gültig, Verarbeitung ohne erfassten Fehler | Konfigurierte Erfolgsmeldung |
| Gültig, Fehler in einer ausgeführten Aktion/Speicherung | Formular wurde abgeschickt, bei der Verarbeitung sind Probleme aufgetreten |
| Aktionsprovider fehlt | Nur Logeintrag auf Level `warning`; daraus entsteht keine Kundenwarnung |
| Unerwartete HTTP-/JSON-Antwort im Browser | Übermittlung konnte nicht bestätigt werden; Eingaben bleiben erhalten |

Bei angenommener Einsendung wird das Formular auch bei Verarbeitungswarnungen zurückgesetzt. Eine Weiterleitung wird bei Warnungen unterdrückt. Alle Details stehen unter [Verarbeitungsergebnisse](https://docs.moori.net/plugin/MoorlForms/processing-results/). Die vorhandenen Klassen `FormActionDatabase` und `FormActionBlacklist` sind keine registrierten auswählbaren Basisaktionen.

### Empfänger, Templates und Anhänge

Empfänger können aus Shopkonfiguration, Formularkonfiguration, Formularübersetzung, gewählter Option oder einer zugeordneten Entity stammen. Die Einstellung `entityMailDetection` steuert das Ersetzen/Ergänzen einer Entity-Adresse. Optionsabhängiges Routing muss zur tatsächlich verwendeten Auswahl passen.

Mailvorlagen erhalten den Formulardaten-Kontext. Beispiele:

```twig
{{ form.getPretty()|raw }}
{{ form.getPretty('plain') }}
{{ form.fieldName('email') }}
{{ form.fieldValue('billingAddress.street') }}
```

Die HTML-Zusammenfassung escaped Daten selbst; eigenes ungeprüftes HTML darf dadurch nicht automatisch als sicher gelten. Passwortwerte werden in der formatierten Ausgabe maskiert. Medien-/Dateianhänge hängen vom gewählten Ablauf ab; die Option `orderSendAttachments` für Bestellmails ist standardmäßig deaktiviert.

## Die Add-ons im Detail

### Classic

Classic ergänzt Bedingungen mit UND-Verknüpfung und den Operatoren `is`, `not`, `contains`, `isset`, `notset`, `gt`, `lt`, `gte`, `lte`; Semikolonwerte bilden Alternativen. Bedingungen werden für Anzeige und serverseitige Verarbeitung berücksichtigt.

Hinzu kommen die Elemente `form-send-copy`, `form-newsletter`, `repeater`, `rating`, `tax-id-number`, `signature`, `bic`, `iban`, `checkbox-slider`, `radio-slider`, `radio-grid`, `checkbox-media` und `radio-media`. Ein `checkbox-grid` ist nicht registriert. Eine IBAN-Prüfsumme bestätigt keine Kontoinhaberschaft. Eine Unterschrift-/Druckfunktion bestätigt keine bestimmte rechtliche Qualität.

Die zusätzlichen Auswahlquellen heißen `customer-group`, `customer-order`, `customer-address` und `product-stream`. Bestellungs-/Adressquellen beziehen sich auf den angemeldeten Kunden; die Produktstream-Auswahl lädt höchstens 50 Produkte. Ein Repeater kann Feldgruppen mehrfach ausgeben. Admin/Browser setzen regulär 1 bis 10 Wiederholungen an; PHP setzt 1 bis 5 nur dann, wenn der gesamte `config.repeater`-Block fehlt oder leer ist. Die gewünschten Grenzen deshalb ausdrücklich konfigurieren.

Verlauf und Druck sind eigene aktivierbare Schritte. Die Druckansicht benötigt einen gespeicherten Verlauf. Classic stellt außerdem die Cookie-Deklaration für die in der Basis implementierte Entwurfsspeicherung bereit. [Einrichtung und Grenzen](https://docs.moori.net/plugin/MoorlFormsClassic/).

Classic ergänzt auch Einstellungen für Weiterleitungen nach fehlerfreiem Submit: Reload, Produkt, Kategorie, feste URL oder Twig-basierte URL. Der angebotene Account-Zieltyp wird vom aktuellen Basiscontroller als Reload behandelt. Bei Verarbeitungswarnungen unterbleibt die Weiterleitung, damit die Rückmeldung sichtbar bleibt.

### Popup

Trigger sind Laden, Scrollen, Exit Intent und Klick auf ein konfiguriertes Element. Randlose Darstellung und eine eigene CSS-Klasse sind konfigurierbar. Größe und Ausrichtung sind im Standardtemplate `modal-lg modal-dialog-centered`; abweichende Größen/Positionen erfordern Template-/CSS-Anpassungen. Der JavaScript-Standard wartet zehn Sekunden und merkt sich die Anzeige je Formular in `sessionStorage`.

Der Subscriber bindet Popups auf Navigation, Produkt, Landingpage, Login sowie Checkout-Bestätigung/-Abschluss ein. Andere Seitentypen sind damit nicht pauschal abgedeckt. Die Verfügbarkeit auf Mobilgeräten hängt vom gewählten Trigger ab. [Einrichtung](https://docs.moori.net/plugin/MoorlFormsPopup/).

### Slides

`slides` enthält einzelne `slide`-Elemente mit Vor-/Zurück-Navigation und schrittbezogener Eingabeprüfung. Es handelt sich um Formularstruktur, nicht um einen zusätzlichen Formulartyp. Der aktuelle Schritt wird nicht eigenständig gespeichert. Animationsfragmente und der unregistrierte Slides-Service begründen keine weitere verfügbare Funktion. [Einrichtung](https://docs.moori.net/plugin/MoorlFormsSlides/).

Buttontexte und -klassen sind konfigurierbar, ebenso automatisches Scrollen nach oben (`autoScrollTop`, Standard aus), der obere Abstand (`offsetTop`, Standard 60) und das Ausblenden deaktivierter Buttons (`hideButtons`). Ein optionaler Absenden-Button wird erst im letzten Schritt freigegeben. Das Container-Template benötigt sowohl `config.css` als auch `config.animateInOut`; fehlende Konfiguration kann die Ausgabe verhindern. Die Schrittprüfung betrachtet Pflichtfelder des aktiven Schritts und ersetzt nicht die abschließende serverseitige Prüfung.

### Customer

`customer-register` ergänzt die Registrierung; `customer-account` stellt ein bearbeitbares Formular unter `/account/form/{id}` bereit. Eingaben können vorhandenen Kunden-/Custom-Field-Eigenschaften zugeordnet werden. Registrierung und Kontoaktualisierung haben verschiedene Lebenszyklen; eine erfolgreiche Speicherung belegt keine spätere Mail-/CRM-Verarbeitung. Das Registrierungsereignis ist `checkout.customer.moorl_form_register` und enthält das erste Registrierungsformular. Der mitgelieferte Flow besitzt noch keine Aktionen; gewünschte Folgen im Flow Builder konfigurieren. [Einrichtung](https://docs.moori.net/plugin/MoorlFormsCustomer/).

### CustomProducts

Produktformulare werden über dynamische Produktgruppen zugewiesen. Konfigurationen inklusive Uploadreferenzen werden an Warenkorbpositionen weitergegeben und in Bestellungen übernommen. Preisoptionen können abhängig von Typ und Konfiguration absolute/relative Zu-/Abschläge, Zahlenmultiplikatoren und die Produktmenge berücksichtigen. Nicht jede Option wird immer mit jedem Zahlenfaktor multipliziert.

Für Basiswert `B`, Summe der Optionsbeträge `S` und Zahlenmultiplikator `M` gilt bei ausgeschaltetem `priceCalculationPriority` zunächst `B × M + S`, bei eingeschalteter Option `(B + S) × M`. Die Einstellung des ersten passenden Formulars entscheidet; Preis-/Steuerberechnung und Produktmenge werden im anschließenden Warenkorbpfad berücksichtigt.

Die Auswahl im Produkt, die Warenkorbberechnung und die spätere Bestellanzeige sind getrennte Verarbeitungsschritte. [Preis- und Mengenbeispiele](https://docs.moori.net/plugin/MoorlFormsCustomProducts/).

### Order

Formulare vom Typ `order` erfassen zusätzliche Angaben im Checkout. Eine Produktgruppe kann die Gültigkeit einschränken; ohne solche Zuordnung kann ein Formular global passen. `checkoutLock` ist standardmäßig aus, `remember` standardmäßig an, `addToDocuments` standardmäßig aus.

Die Eingaben werden sitzungsbezogen zwischengespeichert und nach Bestellerstellung an der Bestellung abgelegt. Der aktuelle Dokumentoverride betrifft den Lieferschein. Die Admin-Zusammenfassung liegt in den Bestelldetails. Die vorhandene Preisoberfläche berechnet in diesem Add-on keine eigenen Warenkorbpreispositionen. [Einrichtung](https://docs.moori.net/plugin/MoorlFormsOrder/).

Das Ereignis `moorl_form.order_placed` wird je verarbeitetem Formular ausgelöst; es liefert keinen eigenen `OrderAware`-/Order-Entity-Vertrag. Flowbedingungen und Vorlagen müssen die tatsächlich angebotenen Eventdaten verwenden.

### Product

`product-request` verbindet ein Anfrageformular mit Produkten dynamischer Produktgruppen. Anfragebutton und Modal, Preis-/Kaufbuttondarstellung und Produktinformationen lassen sich konfigurieren. `keepProductUntouched=true` schützt standardmäßig vor Produktmanipulationen. Die Oberfläche ist keine allgemeine API-Kaufsperre. [Einrichtung](https://docs.moori.net/plugin/MoorlFormsProduct/).

Eine freie Auswahl der Formularposition beziehungsweise eine Produkttab-Integration ist im aktuellen Add-on nicht implementiert; der entsprechende Positionsselektor ist auskommentiert.

### Csv, Hubspot, Mautic und Webhook

CSV schreibt zugeordnete Spalten in eine ausgewählte Mediendatei. Die Konfiguration liegt unter `form.config.csv` mit `csvId` und `mapping`; reguläres Trennzeichen ist `;`, Texteinrahmung ist `"`. Der PHP-Pfad liest/schreibt lokal unter `public/<media.path>`. Das aktuelle Kopfzeilen-Einlesen erwartet eine zusätzliche leere Abschlusszeile, also beispielsweise Kopfzeile plus zwei Zeilenumbrüche. Das im Admin angebotene Escape-Zeichen wird vom PHP-Schreibpfad nicht ausgewertet. Eine reine Remote-Medienablage ist durch diesen lokalen Pfad nicht abgedeckt.

CRM-Add-ons nutzen die jeweilige Foundation-Integration. Hubspot und Mautic verwenden das Integrationsmapping im Formular und Konfigurationen für `clientId`, `formId` und `mapping`; Mappingeinträge besitzen `name` und `data`, Formularplatzhalter etwa `{{ email.value }}`. Die frühere Beschreibung „einfach in den Element-Einstellungen zuweisen“ reicht dafür nicht.

Webhook erzeugt HTTP-Requests aus der Formularkonfiguration. Die Oberfläche bietet GET/POST, optionale Basic-Authentifizierung, Queryparameter, Header und POST-Bodies als leerer Body, Rohtext, JSON oder URL-kodierte Formdaten. Mappingwerte und ein optionales globales Template werden im Normalbetrieb als Twig ausgewertet; Ziel-URL und Rohtextbody werden nicht gerendert. Timeout und Verbindungs-Timeout sind jeweils zehn Sekunden. Der Testbutton sendet tatsächlich an das Ziel, verwendet aber keine aufgelösten Formular-/Flow-Twigwerte. Seine Textanzeige kann wegen eines bereits fürs Log gelesenen Responsebodys „No content“ zeigen.

Diese Wege sind voneinander unabhängig: CSV-Ablage ist keine CRM-Übertragung, und eine erfolgreiche Formularannahme garantiert keine erfolgreiche externe Zustellung. Webhook fängt HTTP-Fehler intern ab; sie erreichen deshalb nicht automatisch den Verarbeitungsbericht der Basis. CRM-Mapping lässt Einträge mit PHP-leerem `data` aus, darunter Text `"0"`. Auch nach erfolgreicher Formularannahme ist die tatsächliche Integration gesondert zu prüfen.

Zusätzlich sind die Flow-Aktionen `action.write.csv`, `action.send.hubspot`, `action.send.mautic` und `action.send.webhook` registriert. Sie verlangen einen passenden `MailAware`-Flow-Kontext; das ist ein anderer Aufrufpfad als die direkte Formularaktion. Die vier Add-ons registrieren keine eigenen Formulartypen. Historische `*-contact`-Abfragen im Admin belegen keinen weiteren Provider.

Details: [CSV](https://docs.moori.net/plugin/MoorlFormsCsv/), [Hubspot](https://docs.moori.net/plugin/MoorlFormsHubspot/), [Mautic](https://docs.moori.net/plugin/MoorlFormsMautic/), [Webhook](https://docs.moori.net/plugin/MoorlFormsWebhook/).

### Example und eigene Erweiterungen

`MoorlFormsExample` demonstriert einen Formulartyp, eine Aktion, ein Element (jeweils `example`) und Admin-/Produkt-Erweiterungen. Es registriert keine eigene Auswahlquelle. Seine aktuellen Methodensignaturen passen teilweise nicht zur Basis. Es ist deshalb kein ungeprüft aktivierbares Referenzplugin.

Eigene Erweiterungen benötigen PHP-Implementierung **und** DI-Registrierung sowie gegebenenfalls Admin-Import, Übersetzungen und Twig-Template:

| Erweiterung | Tag | Vertrag |
| --- | --- | --- |
| Formulartyp | `moorl.fb.form` | `FormTypeInterface` |
| Aktion | `moorl.fb.action` | `FormActionInterface` |
| Element | `moorl.fb.element` | `ElementTypeInterface` |
| Auswahlquelle | `moorl.fb.selection` | `ElementSelectionInterface` |

Die `CODEX.md` im jeweiligen Plugin dokumentiert die tatsächlichen Methoden und Integrationspunkte. Ein Optionsname oder eine vorhandene PHP-Datei allein schaltet keine Funktion frei.

## Daten, Export und Entwürfe

Der sichtbare Exportbutton lädt eine **JSON-Datei mit Dateiendung** herunter. Formulare, Elemente und geladene Übersetzungen nutzen eine gemeinsame Payload. Beim Import/Duplizieren werden IDs und Baumbeziehungen neu zugeordnet. Medienreferenzen werden beim JSON-Import entfernt; Mediendateien gehören nicht zum JSON.

Ein ZIP-Exportservice mit Medien-/Sprachoptionen ist implementiert; sein Dialogbutton ist in der aktuellen Detailansicht auskommentiert. JSON- und ZIP-Funktionen deshalb nicht als identische sichtbare Workflows beschreiben.

Entity-Mapping schreibt konfigurierbare Eingaben und Zusammenfassungen in bestehende DAL-Entities, einschließlich Custom Fields. Es ist kein freier SQL-Editor. Erforderliche Zielattribute müssen valide versorgt werden.

Entwürfe speichert die Basis nur bei gesetzter Zustimmung `moorl-fb-store`; Classic liefert deren Cookie-Eintrag. Fehler beim Senden behalten den Entwurf, Reset/angenommene Einsendung entfernen ihn. Passwörter werden nicht gespeichert; Datei-, versteckte, deaktivierte und schreibgeschützte Felder werden nicht wiederhergestellt. URL-Parameter können Felder vorfüllen, einschließlich Mehrfachauswahl. Für die vom normalen Inputtemplate unterstützten `context`-Vorgaben gibt es asynchrones Nachladen bei angemeldeten Kunden. Versteckte Felder rendern Twig dagegen synchron; Textbereiche übernehmen den asynchronen Marker derzeit nicht. Die genaue Abgrenzung steht in den [Anleitungen](https://docs.moori.net/plugin/MoorlForms/how-tos/).

## Pluginweite Einstellungen

| Schlüssel | Standard / Wirkung |
| --- | --- |
| `loggerLevel` | `400` (ERROR); für fehlende Provider auf WARNING `300` oder niedriger stellen |
| `orderSendAttachments` | `false`; Uploadanhänge bei Bestellbestätigung |
| `entityMailDetection` | Kein expliziter Default in XML; `no`, `yes-replace` oder `yes-append` |
| `showLength` | `true`; Längenanzeige aktiv |
| `showLengthType` | `text`; alternativ `progress-bar` |
| `trimStringValues` | `false`; Rand-Leerzeichen übermittelter Strings entfernen |
| `modalStaticLoad` | `true`; Modalinhalte statisch laden |
| `modalDialogSize` | `modal-md` |
| `modalDialogOrientation` | `modal-dialog-auto` |
| `ignoreCustomFieldSet` | `false`; Demo-Custom-Fields beim Update regulär berücksichtigen |

## Weiterführend

- [Hauptseite](https://docs.moori.net/plugin/MoorlForms/), [Anleitungen](https://docs.moori.net/plugin/MoorlForms/how-tos/) und [FAQ](https://docs.moori.net/plugin/MoorlForms/faq/)
- [Verarbeitungsergebnisse](https://docs.moori.net/plugin/MoorlForms/processing-results/)
- [Englische Feature-Übersicht](https://docs.moori.net/en/plugin/MoorlForms/all-features/)

Die technischen Einzelheiten, Grenzen und noch nicht reproduzierten Implementierungsbefunde stehen in der jeweiligen `CODEX.md`. Der leere Autocomplete-Endpunkt, nicht registrierte Platzhalter und alte Demos werden nicht als einsatzbereite Features gezählt.
