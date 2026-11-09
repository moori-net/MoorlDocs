# Checkout Field Feedback Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Validierungsfehler der Bestellformulare direkt unter den zugehörigen Eingabefeldern anzeigen, mit der vorhandenen JavaScript-Zuordnung.

**Architecture:** Der Checkout behält seinen bestehenden Auto-Submit mit anschließendem Redirect. PHP stellt die Validierungsantworten pro Formular beim Rendern der Bestätigungsseite bereit. Der vorhandene `MoorlFbFormValidatorPlugin` verarbeitet diese initialen Antworten genauso wie seine bisherigen `onFormResponse`-Ereignisse und nutzt weiterhin `window.formValidation`.

**Tech Stack:** Shopware 6.7, Symfony Validator und Session, Twig, Shopware Storefront JavaScript.

**Spec:** Nutzeranforderung vom 09.11.2026: feldbezogene Fehlermeldungen im Checkout; vorhandene Feedback-Elemente und JavaScript-Zuordnung wiederverwenden. Umsetzung vom Nutzer freigegeben; Ausführungsstand siehe unten.

## Rahmen und Entscheidungen

- Auto-Submit, Uploads, Session-Payload, Redirect mit `scrollTo` und serverseitige Bestellsperre bleiben erhalten.
- Keine Umstellung des Checkouts auf den normalen AJAX-Submit von `MoorlFbFormPlugin`: Dieser setzt unter anderem einen Submit-Button voraus und leert das Formular nach Erfolg.
- Kein paralleler Twig-Renderer für Feldfehler: bestehende `.form-field-feedback`-Elemente und Shopware-Validierung verwenden.
- Formularglobale Fehler bleiben im allgemeinen Feedback sichtbar. Feldfehler erscheinen unter den Feldern; der allgemeine Warenkorbhinweis bleibt als Zusammenfassung bestehen.
- Bei aktiver `checkoutLock` bleibt der bisherige Validierungszeitpunkt erhalten, einschließlich der Prüfung beim Laden der Seite. Ohne Sperre werden Fehler erst nach einer tatsächlichen Formularübermittlung angezeigt.
- Mehrere Formulare und verschachtelte Felder müssen korrekt zugeordnet werden. Keine Änderung an bestehenden Formularnamen.
- Zwei getrennte Plugin-Repositories sind betroffen: `MoorlFormsOrder` und `MoorlForms`. Gemeinsame Auslieferung beziehungsweise eine Mindestversion von `moorl/forms` vor Release berücksichtigen.

## Betroffene Produktdateien

Alle Pfade relativ zu `custom/plugins/`:

| Datei | Geplante Änderung |
| --- | --- |
| `MoorlFormsOrder/src/Core/Service/FbOrderService.php` | Ergebnisse aller übermittelten Formulare erfassen; Fehler pro Formular für Redirect und Rendering bereitstellen; Sperrvalidierung erhalten. |
| `MoorlFormsOrder/src/Storefront/Controller/FormController.php` | Alle Ergebnisse berücksichtigen; Feldfehler nicht zusätzlich als globale Flash-Nachrichten ausgeben. |
| `MoorlFormsOrder/src/Resources/views/storefront/page/checkout/confirm/index.html.twig` | Initiale Validierungsantworten sicher als Validator-Optionen ausgeben; vorhandenen Formular-Loop und Auto-Submit erhalten. |
| `MoorlForms/src/Resources/app/storefront/src/fb-form-validator/fb-form-validator.plugin.js` | Initiale Antworten und bestehende Events über dieselbe Feldzuordnung verarbeiten; Suchbereich je Formular beachten. |

`form-feedback.html.twig`, die einzelnen Feldtemplates, `fb-form.plugin.js`, `main.js`, `FormSubmitResponse.php` und `CheckoutFormError.php` benötigen nach diesem Ansatz keine Änderung. Die bestehende Plugin-Registrierung des Validators auf `form` reicht aus. Gebaute Storefront-Artefakte erst beim üblichen Build aktualisieren.

## Prüfschwerpunkte

1. Fehler im ersten von mehreren Formularen bleiben sichtbar, auch wenn das letzte gültig ist.
2. Gleichnamige Felder in unterschiedlichen Formularen erhalten nur ihre eigenen Meldungen.
3. Repeater, Checkbox-Gruppen und Mehrfachauswahl behalten ihre korrekte Feldzuordnung.
4. Korrigierte oder entfernte Formulare hinterlassen keine alten Meldungen; leere Fehlerlisten werden berücksichtigt.
5. Formularglobale Fehler und Meldungen mit Sonderzeichen werden sicher angezeigt; normale Formulare behalten ihre bisherige Event-Verarbeitung.

## Aufgabe 1: Validierungsantworten vollständig durch den Checkout führen

**Dateien:**
- Ändern: `src/Core/Service/FbOrderService.php`
- Ändern: `src/Storefront/Controller/FormController.php`
- Neu: `tests/Unit/Core/Service/FbOrderServiceValidationTest.php`
- Neu: `tests/Unit/Storefront/Controller/FormControllerValidationTest.php`

**Schnittstellen:**
- `FbOrderService::changeCart(Request $request, Cart $cart, SalesChannelContext $salesChannelContext): array` liefert `array<string, FormSubmitResponse>`, indiziert nach Formular-ID. Der einzige gefundene Aufrufer ist der zu ändernde Controller.
- JSON-Nutzlast weiterhin über `FormSubmitResponse::getJsonResponse()` erzeugen; keine zweite Pfadkonvertierung in PHP einführen.
- Session-Schlüssel `MoorlFormsOrder.validation` als Konstante in `FbOrderService`; Inhalt: Antworten nach Formular-ID, ausschließlich serialisierbare Feedbackdaten, keine Validatorobjekte.
- Cart-Extension `MoorlFormsOrderValidation` als `ArrayStruct(['forms' => $responses])` für Twig. Nur aktuell relevante Formulare aufnehmen.

- [ ] Tests zuerst schreiben: erstes Formular ungültig/letztes gültig; alle gültig; wiederholter Submit korrigiert Fehler; entfernte Formulare werden herausgefiltert; Sperre an/aus; globale und feldbezogene Meldungen im Controller unterscheiden.
- [ ] Tests ausführen und den erwarteten Fehler vor der Implementierung bestätigen.
- [ ] In `changeCart()` alle Antworten unmittelbar pro Formular erzeugen und erfassen. Validatorzustand je Formular isolieren; `reset()` nicht zwischen Schritten einsetzen, die noch dessen Tree-Zustand benötigen. Bestehende Uploadverarbeitung und Payload-Speicherung erhalten. Fehlende/unbekannte Formular-IDs kontrolliert behandeln.
- [ ] Nach jedem Submit den Session-Fehlerstand vollständig ersetzen, auch bei Erfolg. Ergebnisse nicht aus der letzten Schleifeniteration ableiten.
- [ ] In `enrichCart()` bei aktiver Sperre pro Formular frisch validieren, Ergebnisse vor dem Reset kopieren und einen gemeinsamen Sperrfehler setzen, sobald mindestens ein Formular ungültig ist. Bei deaktivierter Sperre nur gespeicherte Submit-Antworten für die aktuell sichtbaren Formulare bereitstellen. Bei fehlenden Formularen alte Extension entfernen und veraltete Sessioneinträge bereinigen.
- [ ] Im Controller alle Antworten auswerten. Nur globale Violations als Flash-Nachrichten ausgeben; feldbezogene Meldungen kommen über die Extension. Redirect und bisherige Bestelllogik erhalten. Keine zusätzliche Bestellsperre allein durch die neue Feedbackanzeige einführen.
- [ ] Die neuen Tests und die vorhandenen `MoorlFormsOrder/tests` mit PHPUnit ausführen. Bootstrap analog zu den vorhandenen Unit-Tests verwenden; PHP passend zur installierten Shopware-Version verwenden.

## Aufgabe 2: Bestehenden JavaScript-Validator um initiale Antworten ergänzen

**Dateien im Repository MoorlForms:**
- Ändern: `src/Resources/app/storefront/src/fb-form-validator/fb-form-validator.plugin.js`
- Neu: `tests/Storefront/fb-form-validator.test.mjs`

**Schnittstellen:**
- Neue optionale Plugin-Option `initialResponses: []`.
- Ein Eintrag hat `{scopeSelector: '#fb-<formId>', violations: [...]}`; Violations behalten das bestehende Schema `name`, `path`, `message`, `global`.
- Bestehendes `onFormResponse` mit `event.detail.violations` bleibt kompatibel.
- Gemeinsame Methode `_applyViolations(violations, scope = this._form)` für Event-Antworten und Initialdaten. Initialdaten nach Registrierung der Listener verarbeiten.

- [ ] Fokussierte Tests zuerst schreiben: initiale Antwort erreicht `window.formValidation`; Event-Antwort funktioniert weiter; gleiche Namen in zwei Formularbereichen bleiben getrennt; mehrere Meldungen je Feld bleiben erhalten; leere Antworten und globale Violations werden übersprungen.
- [ ] Tests mit `node --test tests/Storefront/fb-form-validator.test.mjs` ausführen; produktive Methode testen, nicht eine kopierte Implementierung. Shopware-Imports im Test isoliert laden, entsprechend der vorhandenen Toolchain.
- [ ] Gemeinsame Zuordnung implementieren. Felder im angegebenen Formularbereich suchen; Gruppen und `name[]` berücksichtigen. Für komplexe Namen keine ungeprüfte Stringinterpolation in CSS-Selektoren verwenden.
- [ ] Meldungen pro Feld sammeln und über `addErrorMessage()`/`setFieldInvalid()` gemeinsam setzen, damit mehrere Fehler nicht gegenseitig überschrieben werden. Schlüssel für Fehlermeldungen je Formular/Feld eindeutig halten.
- [ ] Eigene frühere Serverfehlermarkierungen bei erneuter Verarbeitung entfernen, ohne andere Validierungsergebnisse pauschal zu löschen. Globale Fehler nicht als fehlendes Eingabefeld protokollieren.
- [ ] Neue Tests und die vorhandenen MoorlForms-Tests ausführen. Beim DOM-Test zusätzlich Rückmeldung unter dem richtigen `aria-describedby`-Ziel prüfen.

## Aufgabe 3: Checkout-Template anbinden

**Datei im Repository MoorlFormsOrder:**
- Ändern: `src/Resources/views/storefront/page/checkout/confirm/index.html.twig`

- [ ] Aus `page.cart.extensions.MoorlFormsOrderValidation.forms` die Liste `initialResponses` aufbauen: pro Formular ID-basierter Bereich `#fb-<formId>` und dessen Violations.
- [ ] Die Liste als `data-moorl-fb-form-validator-options` am bestehenden `#checkoutForm` übergeben. `json_encode` und HTML-Attribut-Escaping verwenden, kein ungefiltertes `raw`.
- [ ] Vorhandene Feedback-Container und `aria-describedby`-Verbindungen nutzen. Keine Initialisierung von `MoorlFbFormPlugin` am Checkout-Formular ergänzen; keine konkurrierenden Submit-Handler.
- [ ] Template mit installierter Shopware-Umgebung linten und das gerenderte JSON mit Meldungen prüfen, die Anführungszeichen, HTML-Zeichen und Umlaute enthalten.

## Aufgabe 4: Integration und Auslieferung prüfen

- [ ] Storefront über das bestehende Shopware-Buildverfahren neu bauen; keine neue Build-Toolchain einführen.
- [ ] Im Browser bei aktivierter Sperre ein leeres Pflichtfeld prüfen: Meldung direkt darunter, `is-invalid`, `aria-invalid`, Warenkorbzusammenfassung und gesperrte Bestellung.
- [ ] Feld korrigieren und Auto-Submit abwarten: Wert erhalten, Feldmeldung verschwunden, Bestellbarkeit entsprechend dem gesamten Formularzustand aktualisiert.
- [ ] Zwei Formulare testen: Fehler im ersten, zweites gültig; gleichnamige Felder; verschachtelte Felder, Repeater, Checkboxen, Mehrfachauswahl und Upload.
- [ ] Mit deaktivierter Sperre prüfen: keine neue Sofortvalidierung beim ersten Seitenaufruf, feldbezogenes Feedback nach Submit, unveränderte Bestellbarkeit.
- [ ] Reguläres AJAX-Formular außerhalb des Checkouts prüfen: Feedbackbereich und `onFormResponse` funktionieren weiter; kein doppeltes Feedback.
- [ ] Mit deaktiviertem JavaScript prüfen, dass serverseitige Bestellsperre und allgemeine Meldungen weiterhin tragen.
- [ ] Versionsanforderung für `moorl/forms` anhand der tatsächlichen Release-Version festlegen; falls nötig `MoorlFormsOrder/composer.json` beim Release anpassen. Keine Versionsnummer während der Planung erfinden.

## Ergebnis der Planung

Vier Produktdateien in zwei Plugins, drei neue gezielte Testdateien sowie übliche Build-Artefakte bei der Umsetzung. Eine Composer-Anpassung ist nur für die Release-Abhängigkeit vorgesehen.

## Ausführungsstand 09.11.2026

- Aufgaben 1–3 implementiert, Änderungen bleiben uncommitted in den bestehenden Plugin-Checkouts. Zusätzlich `MoorlFormsOrder/tests/bootstrap.php` für die Autoloads beider Plugins ergänzt.
- Schnittstellenprüfung: `changeCart()` hat einen Aufrufer, den Controller; dessen Verarbeitung ist auf das Antwortarray umgestellt. Template und Validator verwenden dieselbe `initialResponses`-Struktur.
- Entscheidung: Die Feedback-Funktion darf bei deaktivierter `checkoutLock` keine zusätzliche Bestellsperre erzeugen. Der bisher im Controller direkt hinzugefügte Sperrfehler entfällt; die konfigurierte Sperrvalidierung bleibt im Service.
- Entscheidung: Fehlerhafte oder nicht zum aktuellen Warenkorb gehörende Formular-IDs werden als Bad Request abgewiesen; Validierungszustand wird dabei nicht verändert. Ein bereits gesetzter `IGNORE_VALIDATION_EVENT`-Zustand bleibt erhalten.
- Entscheidung: Checkbox-/Radiofelder mit gemeinsamem Feedback werden gesammelt zurückgesetzt, bevor ihr gemeinsamer Meldungstext gelöscht wird. Später hinzugefügte native Validierungsmeldungen werden erhalten.
- Review-Korrektur: Switch-/AGB-Templates enthalten teilweise kein `aria-describedby`. Der Validator ergänzt den Verweis auf den bereits vorhandenen `<field.id>-feedback`-Container und erhält andere Beschreibungsverweise. Keine zusätzlichen Produktdateien nötig.
- Tests: `php vendor/bin/phpunit --bootstrap custom/plugins/MoorlFormsOrder/tests/bootstrap.php custom/plugins/MoorlFormsOrder/tests` — 8 Tests, 26 Assertions, erfolgreich.
- Tests: `node --test custom/plugins/MoorlForms/tests/Storefront/fb-form-validator.test.mjs` — 6 Tests erfolgreich. Produktions-Plugin und originale Shopware-Feedback-Hilfe werden mit einer kleinen DOM-Testumgebung ausgeführt.
- Vorbestehender Befund: Die MoorlForms-PHP-Suite hat unverändert einen Fehler in `ElementValueRuleTest::testConfiguresATranslatedLabelForTheTechnicalNameField` (fehlendes übersetztes Label); bereits vor den Änderungen reproduziert.
- Prüfung: PHP-Syntax und eigenständiges Twig-Rendering einschließlich JSON-Attribut-Escaping mit Anführungszeichen, HTML-Zeichen und Umlauten erfolgreich. Für diesen isolierten Rendercheck nur die Shopware-Namensauflösung durch normale Twig-Tags ersetzt.
- Build: MoorlForms mit der originalen Shopware-Webpack-Konfiguration und temporärem Plugin-Manifest separat kompiliert. Keine Änderung am Projekt-Manifest oder an anderen Plugins. Ausgabe im üblichen ignorierten `dist/storefront`-Verzeichnis.
- Unabhängige Codeprüfung abgeschlossen; keine verbleibenden kritischen oder wichtigen Befunde.
- Offen für die lauffähige Shopumgebung: Browserabnahme der Checkout-, Upload- und Repeater-Abläufe, vollständiger Shop-Build/Asset-Installation und Festlegung der Release-Mindestversion von `moorl/forms`. Lokaler Kernelstart ist bereits durch den fehlenden Containerparameter `mcp.servers.unassigned` blockiert.
