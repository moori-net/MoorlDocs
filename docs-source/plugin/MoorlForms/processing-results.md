# Verarbeitungsergebnisse und Warnmeldungen

## Alle Aktionen ausführen und Fehler sammeln

Alle aktivierten und verfügbaren Formularaktionen werden in der registrierten Reihenfolge ausgeführt. Eine Exception oder ein PHP-Fehler eines Providers wird protokolliert und im Formularbericht gesammelt; die nachfolgenden Aktionen werden trotzdem versucht. Dasselbe gilt für nachfolgende Elementverarbeitung und konfigurierte Entity-Speicherung. Es gibt keine Unterscheidung zwischen erforderlichen und optionalen Aktionen.

Die bestehenden `FormActionInterface`- und `FormTypeInterface`-Verträge bleiben unverändert. Ein Aktionsprovider muss Fehler durchreichen oder selbst in `FormEntity::getProcessingResult()` eintragen. Intern verschluckte Fehler kann die Basis nicht erkennen. Der integrierte Mail-Subscriber wertet deshalb auch ein `null`-Ergebnis des Shopware-Mailservices als Verarbeitungsproblem.

Der Debug-Formulartyp `test` reicht Exceptions weiterhin durch. Reguläre Validierungsverletzungen, etwa ein leeres Pflichtfeld oder eine ungültige E-Mail-Adresse, verhindern weiterhin das Absenden und die Verarbeitung. Eine technische Exception in einem Provider-Callback ist dagegen ein gesammeltes Verarbeitungsproblem und keine vom Kunden zu korrigierende Eingabeverletzung.

Die Fortsetzung gilt für die Aktions- und Formulartyp-Callbacks. Unerwartete Exceptions der eigentlichen Elementvalidierung oder des Validierungsereignisses werden nicht als bestandene Prüfung behandelt; es werden keine ungeprüften Eingaben zur weiteren Verarbeitung freigegeben.

## Rückmeldung an den Kunden

| Zustand | API | Rückmeldung |
| --- | --- | --- |
| Gültig und ohne Verarbeitungsfehler | `success: true`, `status: success`, `hasWarnings: false` | Konfigurierte Erfolgsmeldung |
| Gültig, aber Fehler bei der Verarbeitung | `success: true`, `status: warning`, `hasWarnings: true` | „Das Formular wurde abgeschickt. Bei der Verarbeitung sind jedoch Probleme aufgetreten. Wenden Sie sich bei Bedarf bitte an den Shopbetreiber.“ |
| Ungültige Eingaben | `success: false`, `status: error` | Konfigurierte Fehlermeldung und konkrete Validierungsverletzungen |

Die Warnmeldung wird im Storefront-Feedback als Warnung dargestellt. Eine konfigurierte Weiterleitung wird bei Warnungen nicht ausgeführt, damit die Nachricht sichtbar bleibt. Das Formular gilt als abgeschickt und wird wie bei einem normalen erfolgreichen Submit zurückgesetzt. Es gibt keine zusätzliche Wiederholungssperre.

`FormSubmitResponse::isSuccess()` beschreibt die Annahme gültiger Eingaben, nicht den Erfolg jeder einzelnen Folgeaktion. `getJsonResponse()` und `jsonSerialize()` berücksichtigen auch nachträgliche Schreibfehler im gemeinsamen Formularbericht und wechseln dann zur Warnmeldung. Technische Fehler werden nicht als Feld- oder globale Eingabe-Violations ausgegeben.

## Technischer Bericht und Logs

Fehlende Aktionsprovider werden mit Aktionsname und Phase als `Form action provider missing` geloggt und übersprungen. Sie erzeugen keinen Fehler im Formularbericht und keine Warnmeldung für den Kunden. Fehler bei der Ausführung vorhandener Provider werden weiterhin gesammelt und als Warnung ausgegeben.

`FormProcessingResult` sammelt Name, Phase, Status und bei Fehlern eine Logreferenz. `isSuccess()` dieses technischen Berichts zeigt, ob alle erfassten Schritte fehlerfrei waren; `hasWarnings()` zeigt gesammelte Probleme an. Der Bericht ist vom Annahmestatus der Formularantwort getrennt.

Fehler bleiben für die aktuelle Verarbeitung erhalten: Ein späterer erfolgreicher Aufruf desselben Schritts überschreibt weder einen früheren Fehler noch dessen Referenz. `resetForSubmission()` eröffnet die nächste Verarbeitung und übernimmt Meldungen aus der vorausgehenden Initialisierung. `processing` in der Antwort enthält die Schritte und die Angabe `partial`. Exception-Texte und übermittelte Werte gehören nicht in diesen Bericht; sie werden nicht an den Kunden ausgegeben.

Nach einer angenommenen Übermittlung läuft das Erfolgsereignis auch bei gesammelten Verarbeitungsproblemen, damit daran angebundene Funktionen weiterhin versucht werden. Zusätzlich wird bei Problemen das Fehlerereignis ausgelöst. Wirft ein Event-Subscriber selbst eine Exception, wird diese an der Dispatch-Grenze gesammelt; die Fortsetzung weiterer Subscriber innerhalb desselben Symfony-Events ist dadurch nicht garantiert.

## Datenbankschreiben und Add-ons

`upsertEntity()` behält den bisherigen `void`-Vertrag und delegiert an `upsertEntityResult()`. Die neue Methode gibt den technischen Bericht zurück. Vorbereitung, Uploads, Konvertierung, Repository-Auflösung und Schreiben sind in die Fehlerbehandlung eingeschlossen. Fehler werden geloggt und an allen beteiligten Formularen vermerkt, ohne eine neue ungefangene Exception in bestehende Add-on-Aufrufer einzuführen.

```php
$result = $fbService->upsertEntityResult($forms, $salesChannelContext, $entity);
if (!$result->isSuccess()) {
    // Den Fehler für die eigene Nachbearbeitung berücksichtigen.
    // Eine gültige Formularübermittlung wird mit Warnung bestätigt.
}
```

Bei eigenständigen Submits schreibt `FbService::submit()` die konfigurierte Entity vor dem Erfolgsereignis. Der Storefront-Controller schreibt sie nicht nochmals. Direkte Add-on-Aufrufe von `submitForm()` behalten standardmäßig ihren eigenen Speicherpfad; der zusätzliche vierte Parameter aktiviert die eigenständige Speicherung ausdrücklich.

Die Annahme des Formulars garantiert weder eine erfolgreiche Mailzustellung noch eine erfolgreiche Datenbankspeicherung. Hintergrundschreiben nach einer bereits abgeschlossenen Kunden-/Bestellerstellung können den abgeschlossenen Vorgang nicht zurücknehmen. Aufrufer müssen Bericht und Logs für ihre Nachbearbeitung auswerten.

Es gibt keinen automatischen Retry, keinen Rollback externer Aktionen und keine dauerhafte Idempotenzverwaltung. Ein erneutes Absenden kann bereits ausgeführte Aktionen wiederholen.

## Prüfung

```powershell
php -d extension=php_zip.dll vendor/bin/phpunit -c custom/plugins/MoorlForms/phpunit.xml.dist
node --test custom/plugins/MoorlForms/tests/Storefront/fb-processing.test.mjs
```

Die Tests prüfen die Fortsetzung nach Aktionsfehlern, PHP-Fehler, gesammelte Datenbankfehler, Warnmeldungen in allen Antwortformaten, die Reihenfolge der Speicherung, Add-on-Aufrufe ohne zusätzliche Speicherung und fehlgeschlagene Mailservice-Rückgaben. Die Storefront-Tests prüfen normale Rücksetzung bei Warnungen und weiterhin korrigierbare Eingabefehler. Externe Dienste und vollständige Shopware-Abläufe werden dadurch nicht als Integration getestet.
