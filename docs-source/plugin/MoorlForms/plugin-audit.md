# Dokumentationsabgleich der MoorlForms-Pluginfamilie

Stand: **10. November 2026**. Dieser Bericht gehört zur [zentralen Feature-Übersicht](all-features.md). Technische Einzelheiten und konkrete Erweiterungsverträge stehen in der `CODEX.md` jedes Plugins.

## Prüfstand

Die 13 lokalen Pluginverzeichnisse wurden inventarisiert. Verglichen wurden Composer-Anforderungen, Plugin-Lifecycle, DI-Registrierungen, Datenmodelle/Migrationen, PHP-Verarbeitung, Admin-Importketten und Einstellungen, Storefront-JavaScript, Twig-Templates, Beispiele und vorhandene deutsche/englische Handbücher. Eine Klasse, Übersetzung oder Einstellung wurde nur dann als reguläre Funktion gezählt, wenn auch Registrierung und Aufrufpfad dazu passen.

**Die Anmeldung und die ersten visuellen Abgleiche sind erfolgt:** Im lokalen Shopware-Admin **6.7.15.1** wurden dieselben **30 Admin-Ansichten erneut auf Englisch in 1920 × 1080 Pixeln** aufgenommen. Sie zeigen Basiseditor, Feld-/Layout-/Auswahl-/Uploadkonfiguration, CMS-Einbindung und Order-Einstellungen. Die [Screenshotübersicht](admin-screenshots.md), die [englische Galerie](admin-screenshots.en.md) und das [Aufnahmemanifest](admin-screenshots.json) verzeichnen alle Bilder, Routen, Zeitpunkte und den tatsächlichen Pluginstand. Zugangsdaten wurden nicht in der Dokumentation gespeichert.

Passende historische Adminbilder wurden in den Basis-/Order-Handbüchern durch die neuen FHD-Aufnahmen ersetzt. Verbleibende JPGs sind ausdrücklich historische Illustrationen. Auch lokale, gitignorierte `dist`-Dateien können von den geprüften Quellen abweichen. Ihre Existenz belegt weder einen aktuellen Neubau noch den Inhalt eines veröffentlichten Releases.

Die Pluginregistrierung des laufenden Shops enthält **MoorlForms 2.7.9 (aktiv)**, **MoorlFormsOrder 2.7.2 (aktiv)** und **MoorlFormsCustomProducts 2.7.0 (deaktiviert)**. Die übrigen zehn lokalen Pluginverzeichnisse sind dort nicht registriert. Diese registrierten Versionsnummern sind getrennt von den unten genannten Composer-Quellständen zu lesen. CustomProducts liefert deaktiviert kein Konfigurationsschema; der frühere Aufruf bestätigte die fehlende Konfiguration. Die alten Fehlerbilder wurden entfernt. Es wurden keine Plugins installiert/aktiviert oder aktualisiert. Ihre Featureoberflächen bleiben deshalb weiterhin nicht visuell geprüft.

Die Screenshotserie wurde nach vollständigem Browser-Neuladen neu erstellt, mit englischer Oberfläche und Inhaltssprache (`en-GB`). Die vorherige rote Critical-Anzeige ist verschwunden. Vor jeder Aufnahme wurde auf sichtbare Fehlerbenachrichtigungen geprüft; keine Fehler wurden für die Aufnahme ausgeblendet. Deutsche FHD-Varianten und alte Login-/Konfigurationsfehlerbilder wurden auf Benutzerwunsch entfernt. Beide Dokumentationssprachen verwenden dieselben neuen englischen PNGs unter `images/admin-fhd/en/`. Eigene Entity und Empfangsbestätigung wurden temporär ausgewählt, nicht gespeichert; danach Originalstand per Repository bestätigt: `salutation`, Aktionen `mail`, `mail-copy`, `captcha`. Auch Erlebniswelt und Plugin-Einstellungen wurden nicht gespeichert.

## Bestand und Quellenrevisionen

Revisionen beziehen sich auf den jeweiligen HEAD zu Beginn des Abgleichs; die Dokumentationsänderungen dieses Audits sind dabei noch nicht enthalten. Die Datei-Anzahl ist das von `rg --files <plugin>/src` sichtbare Inventar, keine Zeilenzahl und keine Behauptung einer vollständigen Laufzeitabdeckung.

| Plugin | Composer-Version | Revision | Quelldateien | Technische Orientierung |
| --- | --- | --- | ---: | --- |
| MoorlForms | 2.7.11 | `6d3cba7` | 329 | `MoorlForms/CODEX.md`, aktualisiert |
| MoorlFormsClassic | 2.7.1 | `e4cea4b` | 94 | `MoorlFormsClassic/CODEX.md`, neu |
| MoorlFormsCsv | 2.7.1 | `3e56640` | 24 | `MoorlFormsCsv/CODEX.md`, neu |
| MoorlFormsCustomer | 2.7.0 | `9288ad2` | 22 | `MoorlFormsCustomer/CODEX.md`, neu |
| MoorlFormsCustomProducts | 2.7.1 | `1ddaf16` | 32 | `MoorlFormsCustomProducts/CODEX.md`, aktualisiert |
| MoorlFormsExample | 1.7.0 | `3ad6b95` | 21 | `MoorlFormsExample/CODEX.md`, neu |
| MoorlFormsHubspot | 2.7.0 | `fecd47d` | 22 | `MoorlFormsHubspot/CODEX.md`, neu |
| MoorlFormsMautic | 2.7.0 | `be564fa` | 55 | `MoorlFormsMautic/CODEX.md`, neu |
| MoorlFormsOrder | 2.7.3 | `de139f2` | 28 | `MoorlFormsOrder/CODEX.md`, neu |
| MoorlFormsPopup | 2.7.0 | `441e39a` | 20 | `MoorlFormsPopup/CODEX.md`, neu |
| MoorlFormsProduct | 2.7.0 | `eccd74f` | 18 | `MoorlFormsProduct/CODEX.md`, neu |
| MoorlFormsSlides | 2.7.0 | `8947730` | 24 | `MoorlFormsSlides/CODEX.md`, neu |
| MoorlFormsWebhook | 2.7.0 | `2452f5e` | 30 | `MoorlFormsWebhook/CODEX.md`, neu |

## Korrigierte Dokumentationsabweichungen

| Bereich | Frühere Aussage / Lücke | Abgeglichener Stand und Quelle |
| --- | --- | --- |
| Basis: Funktionsumfang | Twig und verschachtelte Felder teilweise Classic zugeordnet | Twig ist in `Core/Framework/Twig/FbExtension.php` und `FbTokenParser.php` registriert; `nested-fields` in `Resources/config/element-types.xml`. Zentrale Übersicht korrigiert. |
| Basis: Mail | Empfangsbestätigung, vollständige Mailkopie und Empfängerrouting vermischt | Basisaktionen `mail`, `receipt-confirmation`; Classic `mail-copy` plus Kundenschalter. `FormDataStruct::findMailReceiver/findMailCopyReceiver` und `FormActionReceiptConfirmation` unterscheiden die Datenkontexte. |
| Basis: Export | JSON-/ZIP-Funktionen nicht nach sichtbarem Bedienweg getrennt | `moorl-fb-form.mixin.js::exportForm` lädt `.json`; ZIP-Service/Route existieren, der Dialogbutton in `page/detail/index.html.twig` ist auskommentiert. |
| Basis: Entwurf | CODEX beschrieb Löschen schon beim Absenden | `fb-store.plugin.js` behält Daten während Senden/Fehlern und entfernt sie beim Reset; Passwörter ausgeschlossen. Cookie-Deklaration kommt aus Classic. |
| Basis: Backendvalidierung | Allgemeine Validierungsaussagen verdeckten typspezifische Grenzen | Date/Time/Number/URL ergänzen keine vollständigen entsprechenden PHP-Fachconstraints; Browsergrenzen von Pflicht/Längen/Regex-/Vergleichsvalidierung getrennt beschrieben. |
| Basis: Checkboxgruppen | TODO konnte als vollständig fehlendes Min/Max verstanden werden | Browserplugin und Symfony-`Count` vorhanden; optionale Gruppen werden im MultiField-Pfad früh übersprungen. |
| Basis: eigene Entities | Grenze und Filtersyntax nicht vollständig erklärt | `ElementSelectionCustomEntity`: maximal 500, zeilenweises `feld=wert`, boolesche Werte, Nullzeichenfolge `0`, LF/CRLF/CR, zusätzliche `=` im Wert. |
| Basis: Teststatus | Alter CODEX-Stand meldete Label-Testfehler und 13 Tests | Der inzwischen korrigierte Test erwartet den Platzhalter ohne Label; aktuellen Prüfstand unten dokumentiert. |
| Classic | Historische Funktionsgleichheit mit altem FormBuilder, unklare Typ-/Aktionszuordnung | Registrierte `twig`/`inline`, 13 zusätzliche Elemente, fünf Aktionen und vier Auswahlquellen aufgeführt. Keine Gleichheitsgarantie über unbekannte Altversionen. |
| Classic: Repeater | Einheitliche Defaultgrenzen naheliegend | Admin/JS 1–10; PHP 1–5 nur bei fehlendem/leerem gesamten Konfigurationsblock. Explizite Konfiguration empfohlen. |
| Classic: Verlauf/Druck | Druck konnte als unabhängige oder rechtlich bestätigte Funktion erscheinen | `write-history` speichert, `print-view` baut auf einer History-ID auf. Kein Nachweis einer bestimmten Rechtsqualität. |
| Popup | Automatisch auf jeder Shopseite verfügbar | Subscriber begrenzt Seitenereignisse auf Navigation, Produkt, Landing, Login, Checkout Confirm/Finish. |
| Popup: Darstellung | Allgemeine Modaloptionen auf Popup übertragbar | Standardtemplate hardcodiert `modal-lg modal-dialog-centered`; eigene CSS-Klasse/randlos konfigurierbar, sonst Template-/CSS-Anpassung. |
| Slides | Verfügbare Animationen oder eigene Speicherung des Schritts naheliegend | Nur `slides`/`slide` registriert. Animationstyp/Service ohne reguläre Registrierung; aktueller Schritt ohne eigene Persistenz. |
| Customer | Registrierung, Accountaktualisierung und Mapping nicht präzise getrennt | `customer-register`, `customer-account`, `/account/form/{id}`, Kunden-/Custom-Field-Zuordnung und Registrierungsereignis dokumentiert. |
| CustomProducts: Preise | Absolute Abschläge angeblich noch nicht möglich | `absolute-discount` vorhanden. Wirkung der Optionen hängt zusätzlich von `priceCalculationPriority` und Mengenbezug ab. |
| CustomProducts: Speicherung | Warenkorb- und Entityspeicherung vermischt | Konfiguration zuerst im Cart-Payload; Zuordnung nach `order_line_item` und Zusammenfassungen bei Bestellübernahme. |
| Order: Preise | Warenkorbpreiskalkulation als vorhandene Funktion beworben | Service und Cartprocessor erzeugen keine entsprechenden Preispositionen. Sichtbare Preisoption nicht als implementierte Preiswirkung gezählt. |
| Order: Zuordnung/Anzeige | Produktgruppe zwingend, Anzeige über früheren Adminblock | Ohne Stream kann Order global passen. Aktueller Adminpfad in Bestelldetails; Dokumentoverride konkret Lieferschein. |
| Product | Kauf generell ausgeschlossen | Standard `keepProductUntouched=true`; Templates ändern Darstellung. Kein eigener Cart-/Store-API-Kaufschutz. |
| Csv | Datei-/Mappingpfad und Formatgrenzen unklar | Medienauswahl `csvId`, Header-/Spaltenmapping, lokaler `public/<media.path>`-Pfad, zusätzliche leere Abschlusszeile und nicht ausgewertetes Escape-Feld dokumentiert. |
| Hubspot/Mautic | Zuordnung in einzelnen Elementeinstellungen | Gemeinsame Mappingkomponente im Integrationsreiter; `clientId`, `formId`, `mapping`; direkter Formular- und `MailAware`-Flow-Pfad getrennt. |
| Mautic | API-Klassen und allgemeine Mailingversprechen als Featureumfang interpretierbar | 33 API-Klassen sind Bibliotheksumfang. Aktive Integration nutzt REST für Auswahl und separate Bibliothek für Formular-Submission; Zielaktionen bestimmt Mautic. |
| Webhook | Template-/Test-/Antwortverhalten nicht vollständig beschrieben | GET/POST, POST-Bodyarten, Twig nur auf Mapping-/Templatepfad; Test sendet wirklich ohne Laufzeit-Twigauflösung. Bereits gelesenes Responsebody kann Testanzeige leeren. |
| Example | Ohne Einschränkung als aktuelles Entwicklerbeispiel verlinkt | Inkompatible Lifecycle-Signaturen und alte Zustandszugriffe dokumentiert; vor Aktivierung an aktuelle Interfaces anpassen. |

Die Änderungen korrigieren die Dokumentation. Entdeckte Implementierungsgrenzen wurden nicht durch unbestellte Funktionsänderungen verdeckt. Prüfbare Folgearbeiten sind im jeweiligen `CODEX.md` mit Quellpfaden beschrieben.

## Unveränderte Implementierungsbefunde für Folgearbeiten

Diese Punkte sind aus konkreten Aufrufpfaden abgeleitet. Wo keine gezielte Reproduktion vorliegt, sind sie keine behaupteten End-to-End-Fehler. Die zuständige `CODEX.md` beschreibt jeweils die genaue Grenze.

| Bereich | Quellbefund | Nächster gezielter Nachweis |
| --- | --- | --- |
| Basis: Standardwerte | `field.html.twig` markiert Contextvorgaben asynchron, `hidden.html.twig` rendert direkt; Textarea übernimmt den Marker nicht | Angemeldeter/abgemeldeter Kunde mit aktivem HTTP-Cache und mehreren Feldtypen |
| Basis: Validatorzustand | `FbService` hält gemeinsamen Validatorzustand; kein pauschaler Reset am Anfang jedes `submitForm()` | Mehrere unabhängige Formulare/Cartpositionen in einem Aufruf |
| Classic: Druck | Printcontroller lädt nach History-ID ohne dort sichtbare zusätzliche Kunden-/Sitzungszuordnung | Autorisierungsanforderung und vollständigen Routing-/Proxykontext prüfen |
| Classic: Auswahl | Produktstream-Auswahl lädt maximal 50; Cache ist nach Produktgruppe organisiert | Mehrere Auswahlfelder mit gleichem Stream und unterschiedlicher Konfiguration |
| Slides | Ausgabe verlangt CSS-/Übergangsstruktur; unregistrierter Service referenziert nicht vorhandene Klasse | Reales gespeichertes Formular mit vollständiger/fehlender Konfiguration anzeigen |
| Customer | Zusatzpfad für Registrierung hängt von übermittelten Formular-IDs ab | Registrierung mit/ohne Formular-ID und fachlich erforderlichen Zusatzangaben |
| CustomProducts | Initialisierung/mehrere Submitantworten und Zahlenwert `0` besitzen besondere Pfade | Mehrere Formulare, fehlgeschlagene Pflichtwerte, Null-/Nullstringwerte und Mengenwechsel |
| Order | Nachgelagerter Entity-Write erhält die geladene Formularcollection, nicht ausschließlich den zuvor gefilterten Teil | Bestellung mit unterschiedlich zugeordneten Formularen und Produktgruppen |
| Csv | Service behält erste Datei und Konfiguration; Kopfzeilenleser erwartet zusätzliche leere Abschlusszeile | Zwei verschiedene CSV-Ziele in einem Request und Dateivarianten mit/ohne Leerzeile |
| Hubspot/Mautic | Initialisierter Client und Context werden im Service behalten | Zwei Clients in demselben Request bzw. langlebigem Prozess |
| Mautic | REST-Listenfehler werden nicht explizit auf das erwartete `forms`-Array normalisiert; Submission nutzt separaten Pfad | Falsche API-Zugangsdaten, unerwartete API-Antwort und kontrolliertes Formularziel |
| Webhook | HTTP-Fehler werden intern geloggt; Twigfehler können als Textparameter versendet werden; Teststate wird nicht zurückgenommen | Kontrollierter lokaler Endpunkt mit HTTP-Fehler, ungültigem Twig und anschließendem normalen Request |
| Webhook: Antwort/Logs | Responsebody wird fürs Log gelesen und beim Test erneut ohne Rewind abgefragt; Config/Requestoptionen werden unmaskiert geloggt | Response-/Logprüfung mit ausschließlich synthetischen Testwerten |
| Example | Klassenladen mit aktuellen Interfaces scheitert an Lifecycle-Signaturen | Signaturen/Zustandszugriffe an aktuelle Interfaces anpassen, danach separat testen |

## Belegte Erweiterungspunkte

Die Basis stellt `moorl.fb.form`, `moorl.fb.action`, `moorl.fb.element` und `moorl.fb.selection` bereit. Die Integrations-Add-ons registrieren zusätzlich eigene Flow-Aktionen auf Grundlage eines `MailAware`-Kontexts. Mautics umfangreiche API-Klassen sind keine zusätzlichen Shopware-Adminmodule. Die zentrale Feature-Tabelle enthält sämtliche tatsächlich registrierten fachlichen Typen, Aktionen und Auswahlquellen; Zustands-/Layoutdetails stehen zusätzlich in den Plugin-CODEX-Dateien.

## Admin-Aufnahmen in Full HD

Vorgesehen ist ein Browser-Viewport von **1920 × 1080 CSS-Pixeln**, Device Scale Factor **1**, PNG-Ausgabe mit **1920 × 1080 Bildpixeln**. Ein vollständiges Scrollbild wird nicht als FHD-Viewportaufnahme bezeichnet. Lange Einstellungen erhalten mehrere einzeln beschriftete Aufnahmen. Produktivdaten und Zugangsdaten gehören nicht in die Dokumentationsbilder; Versand-/Testbuttons werden für reine Aufnahmen nicht ausgelöst.

### Erneute englische Aufnahme

Die [FHD-Galerie](admin-screenshots.en.md) zeigt ausschließlich die 30 neu aufgenommenen englischen Adminansichten. Zeitpunkte, Auflösung und Sprachkennung stehen im Manifest. Die deutschen Varianten und die früheren Diagnosebilder sind gelöscht.

### Aufnahmeliste und erwarteter Abgleich

| Plugin / Ansicht | Einstieg | Erwartung aus dem Quellcode | Aktueller Status |
| --- | --- | --- | --- |
| Basis: Formularliste/Neuanlage | `#/moorl/fb/form/list` | Liste, Erstellen/Import, verfügbare Vorlagen | Aufgenommen; siehe FHD-Galerie |
| Basis: Allgemein | `#/moorl/fb/form/detail/{id}` | Typ-/Aktionsliste, Aktivierung, technische/übersetzte Namen | Aufgenommen; siehe FHD-Galerie |
| Basis: Layout und Zuweisung | Formularreiter | Responsive Gestaltung, Sichtbarkeitsfilter, Zielentity | Aufgenommen; siehe FHD-Galerie |
| Basis: Mail | Formularreiter | Allgemeiner/sprachbezogener Empfänger, Vorlagen, Empfangsbestätigung | Aufgenommen; siehe FHD-Galerie |
| Basis: Feld/Auswahl/Upload | `#/moorl/fb/form/detail/{id}/element/{elementId}` | Typspezifische Karten, 500er-Hinweis bei eigenen Entities | Aufgenommen; siehe FHD-Galerie |
| Basis: CMS | Erlebniswelten, Element tauschen | CMS-Element ohne eigenen Block, Formularauswahl/custom1–4 | Aufgenommen; siehe FHD-Galerie |
| Basis: Plugin-Konfiguration | `#/sw/extension/config/MoorlForms` | Logger, Anhänge, Trimming, Längenanzeige, Modale | Aufgenommen; siehe FHD-Galerie |
| Classic: Elemente/Bedingungen | Basis-Elementeditor | Zusätzliche Typen, Repeater-/Bedingungskarten, Auswahlquellen | Plugin im laufenden Shop nicht registriert |
| Classic: Verlauf | `#/moorl/fb/history/list`, `#/moorl/fb/history/detail/{id}` | Einsendungen/Detail-/Druckbezug, Einstellungen → Erweiterungen → Verlauf | Plugin im laufenden Shop nicht registriert |
| Popup | Basisformular vom Typ `popup` | Trigger, Sitzungslimit, randlos/CSS | Plugin im laufenden Shop nicht registriert |
| Slides | Basis-Elementeditor | `slides` mit `slide`-Kindern; keine reguläre Animationstyp-Auswahl | Plugin im laufenden Shop nicht registriert |
| Customer | Basisformular-/Plugin-Konfiguration | Registrierungs-/Kontotyp, Kundenzuordnung | Plugin im laufenden Shop nicht registriert |
| CustomProducts | Basisformular-/Plugin-Konfiguration | Preis-/Mengenoptionen und Produktgruppe | Plugin deaktiviert; keine aktuelle Featureaufnahme |
| CustomProducts: Bestellposition | `#/sw/order/detail/{id}/general` | Positionsmenü „Zeige Konfiguration“ | Plugin deaktiviert; keine aktuelle Featureaufnahme |
| Order | Basisformular-/Plugin-Konfiguration | Checkoutlock/Remember/Dokumente; Preis-UI ohne nachgewiesene Berechnung | Formular-/Plugin-Einstellungen aufgenommen |
| Order: Bestelldaten | `#/sw/order/detail/{id}/details` | Formularzusammenfassung vor Versandkarte | Keine geeignete Testbestellung geöffnet |
| Product | Basisformular vom Typ `product-request` | Modal/Kaufbereich/Preis-Schalter und Produktgruppe | Plugin im laufenden Shop nicht registriert |
| Csv | Formularreiter/Flow-Modal | CSV-Medienauswahl, Spaltenmapping und Formatfelder | Plugin im laufenden Shop nicht registriert |
| Hubspot | Formularreiter/Flow-Modal | Client/Formular/Mapping; keine Elementfeld-Zuordnung | Plugin im laufenden Shop nicht registriert |
| Mautic | Formularreiter/Flow-Modal | Client/Formular/Mapping; Formularlisten von REST-API abhängig | Plugin im laufenden Shop nicht registriert |
| Webhook | Formularreiter/Flow-Modal | URL/Methode/Auth/Query/Header/POST-Body/Template | Plugin im laufenden Shop nicht registriert |
| Example | Kein ungeprüftes Aktivieren | Erst Lifecycle-Signaturen korrigieren; Quellenbeispiel kein UI-Nachweis | Nicht registriert; zusätzlich Klassenkompatibilität prüfen |

Plugin, Route/Ansicht, Sprache, registrierter Pluginstand, Datum, Dateiname und Auflösung sind für die neuen Aufnahmen im Manifest festgehalten. Die Bilder bestätigen die sichtbaren Einstellungen; eine erfolgreiche Mail-/CRM-/Checkout-Verarbeitung wurde dadurch nicht getestet. Bei Order zeigt die Oberfläche weiterhin den alten Hinweis auf zwingende Produktgruppe und Preiskonfiguration; die technische Anleitung beschreibt diese beiden Grenzen weiterhin genauer als der vorhandene UI-Hinweis.

## Tests und weitere Nachweise

Alle folgenden vorhandenen Suiten wurden für diesen Dokumentationsabgleich frisch ausgeführt:

| Suite | Ergebnis | Reichweite |
| --- | --- | --- |
| MoorlForms PHPUnit | 43 Tests, 202 Assertions erfolgreich | Isolierte Basislogik, kein kompletter Shopware-/Mail-/Cartablauf |
| MoorlForms JavaScript | 52 Tests erfolgreich | Formularantworten/Entwurf/Validierung und JSON-Download mit kontrollierter Testumgebung |
| MoorlFormsClassic Node | 44 Tests erfolgreich | Vorhandene isolierte JavaScript-Tests |
| MoorlFormsClassic PHPUnit | 41 Tests, 77 Assertions erfolgreich | Vorhandene isolierte PHP-Tests |
| MoorlFormsOrder PHPUnit | 8 Tests, 26 Assertions erfolgreich | Vorhandene Order-Service-/Payloadpfade |
| MoorlFormsCustomProducts PHPUnit | 1 Test, 7 Assertions erfolgreich | Positionsänderung/Payloadpersistenz |

Die anderen Add-ons besitzen keine eigenen entsprechend eingerichteten Testsuiten. Eine grüne Basissuite testet deren externe Integrationen nicht mit. Aktuelle Befehle und Bedingungen stehen im jeweiligen `CODEX.md`; ZIP-Tests benötigen die PHP-ZIP-Erweiterung. Endgültige Dokuprüfung: alle geänderten Git-Diffs auf Whitespace, Dokumentationslinks und vorhandene Bilder prüfen; Ergebnisse nicht aus alten Behauptungen übernehmen.

Für Order existiert keine pluginlokale `phpunit.xml.dist`. Der bestätigte Aufruf lautet vom Shopware-Root: `php vendor/bin/phpunit --bootstrap custom/plugins/MoorlFormsOrder/tests/bootstrap.php custom/plugins/MoorlFormsOrder/tests`. Die übrigen genannten PHP-Suiten besitzen eigene Konfigurationen.

Die gemeinsamen Ergebnisse sind **93 PHP-Tests mit 312 Assertions** und **96 JavaScript-Tests**, jeweils erfolgreich. Es wurde ausschließlich Dokumentation geändert; daraus wird keine neue Laufzeitfunktion abgeleitet.

Nach der Neuaufnahme wurden alle 30 PNG-Dateiköpfe auf exakt 1920×1080 geprüft. Das Manifest enthält ausschließlich `en-GB`-Aufnahmen mit neuen Zeitpunkten und jeweils null sichtbaren Fehlerbenachrichtigungen. Die abschließende Prüfung von 50 neuen/geänderten Markdowndateien, 627 lokalen Verweisen und allen 13 Git-Diffs war erfolgreich. Es sind keine deutschen Dateien der FHD-Serie übrig. Die früheren bilingualen Bildanzahlen gelten nicht mehr.

## Dokumentationsquellen und Weiterarbeit

- Die Basis verwendet `index*.tpl.md`, `manual*.tpl.md`, `store*.tpl.md`; ihre generierten Ausgabedateien müssen nicht im Repository vorhanden sein.
- Die Add-ons verwenden überwiegend direkt `docs/index.md` und `docs/index.en.md`. Alle Fachkorrekturen in beiden Sprachen nachziehen.
- Die vorher nahezu leere englische Feature-Seite wird als vollständige Entsprechung der zentralen Übersicht gepflegt.
- Beispiele wurden als Quellmaterial geprüft. Ein alter JSON-Export ist kein bereits erfolgreich getesteter Import in die aktuelle Datenbank.
- Kein Shopware-Neuaufsetzen, Pluginaktivieren, Demoimport, CRM-/Webhookversand oder echter Kauf wurde für die Dokumentationsarbeit durchgeführt.
- Offen bleiben die Featureaufnahmen nicht registrierter/deaktivierter Add-ons und die datenabhängigen Bestellansichten. Eine vollständige visuelle Prüfung setzt einen entsprechend eingerichteten Shop und geeignete Testdaten voraus; der Login ist kein Hindernis mehr.
