# Installation und Betrieb: Ticket Vendor

## Voraussetzungen

Strukturierte Eventdaten werden automatisch auf der Veranstaltungsseite ausgegeben. Weitere schema.org-Eigenschaften können unter **Event → SEO → Strukturierte Eventdaten** je Sprache ergänzt werden. Vor dem Einsatz die nullable JSON-Spalte `moorl_tv_ticket_sale_translation.schema_org` mit dem externen Schemawerkzeug erzeugen. [Feldzuordnung und Beispiele](schema-org.md).

- Shopware 6.7 mit Storefront; die tatsächlichen Paketgrenzen stehen in `composer.json` (`shopware/core: ~6.7.0`).
- MoorlFoundation 1.7 (`moorl/foundation: ~1.7.0`), vor Ticket Vendor installiert und aktiviert.
- PHP und Datenbank entsprechend Ihrer Shopware-Version. Entwicklungsprüfungen erfolgen mit PHP 8.2 und Shopware 6.7.14.1.
- Composer-Abhängigkeiten `dompdf/dompdf: ^3.1` und `tecnickcom/tcpdf: ^6.7.7` für PDFs und QR-Codes. Bei Installation und Updates über die Erweiterungsverwaltung führt Shopware Composer aus, um diese bereitzustellen. Der Server benötigt dafür Composer und Zugriff auf die Paketquellen. Bei Composer-Deployments löst der reguläre Deploymentprozess die Abhängigkeiten auf.
- Funktionierende Shopware-Mailkonfiguration sowie dauerhaft laufende Nachrichtenverarbeitung und geplante Aufgaben.
- HTTPS und eine zuverlässige Onlineverbindung für Einlassgeräte. Browser-Kamerascans benötigen zusätzlich `BarcodeDetector`-Unterstützung.

## Installation

Mit **Veranstaltungen mit Archiv (statisch)** (`moorl-tv-ticket-sale-static-listing`) fügen Sie eine feste Übersicht aller aktiven Events hinzu. Laufende und kommende Veranstaltungen stehen mit dem nächsten Termin zuerst oben; vergangene folgen absteigend und ausgegraut. Verkaufszeiträume begrenzen diese Übersicht nicht. Über **Alternative Veranstaltungs-URL** am Event können private Events beispielsweise zur Community verlinken. Ohne alternative URL führt der Link bei verfügbaren Events zur Veranstaltungsseite. Vergangene Events erhalten keinen Kaufbutton. Die optionale Spalte `moorl_tv_ticket_sale.alternative_url` (`VARCHAR(2048)`, nullable) mit dem Schemawerkzeug ergänzen und anschließend Administration und Theme neu bauen.

Weisen Sie einer Shopware-Kategorie eine Erlebniswelt mit `moorl-tv-ticket-sale-listing` zu und wählen Sie diese Kategorie in der Plugin-Konfiguration unter **Seite mit Veranstaltungen (Liste)** (`category`). Dort stellen Sie unter **Standard-CMS-Seite für Veranstaltungsdetails** (`cmsPageId`) das Standardlayout für Events ein. Die am Event ausgewählte CMS-Seite hat Vorrang.

1. Foundation installieren und aktivieren.
2. Ticket Vendor über die Erweiterungsverwaltung oder Ihren Deploymentprozess installieren und aktivieren.
3. Bei einer Quellcodeinstallation Composer-Abhängigkeiten bereitstellen und Administration/Storefront nach dem üblichen Shopware-Verfahren bauen. Bei einem Distributionspaket die enthaltenen Assets veröffentlichen.
4. Cache leeren und das verwendete Theme kompilieren.
5. Installation der Foundation-Datenpakete kontrollieren: `data`, `ticket-number`, `ticket-mail`, `seo`, `scanner-role`.
6. Worker einrichten und eine vollständige Testbestellung einschließlich Zahlung, PDF, E-Mail und Check-in durchführen.

Die Aktivierung verwendet den vorhandenen Foundation-Lifecycle-Helper. Die Pakete ergänzen Medienordner und Importprofile, Ticketnummernkreis, Ticket-Mailvorlagen, SEO-Vorlage sowie die Scanner-Rolle. Das Demopaket wird separat geladen.

## Worker und Indizes

Beispiele aus dem Shopware-Hauptverzeichnis; in der Produktion über Ihre Prozessverwaltung dauerhaft betreiben beziehungsweise regelmäßig neu starten:

```sh
bin/console scheduled-task:register
bin/console scheduled-task:run --time-limit=60
bin/console messenger:consume async low_priority --time-limit=60
bin/console dal:refresh:index --only=moorl_tv_ticket_sale.seo
```

Die Transportnamen müssen zur Messenger-Konfiguration Ihrer Installation passen. Der Task `moorl_tv.expire_tickets` hat ein Intervall von 60 Sekunden und übernimmt Zahlungsfristen sowie das erneute Anstellen nicht zugestellter gültiger Tickets. Eine Registrierung allein führt ihn noch nicht aus. Nach Codeupdates laufende Worker neu starten.

## Erweiterung konfigurieren

Unter den Erweiterungseinstellungen steht **Zahlungsfrist in Minuten**, standardmäßig **30**. Passen Sie sie an Ihre Zahlungsmethoden an. Nach Fristablauf kann der Ablaufjob die gesamte noch unbezahlte Bestellung stornieren; beachten Sie insbesondere Vorkasse und Mischbestellungen. Eine verspätete Zahlung auf eine bereits stornierte Bestellung verlangt manuelle Abstimmung und führt nicht automatisch zu einer Rückzahlung.

Shopware muss die abgeschlossene Zahlung als `paid` melden. Prüfen Sie die Statusübergänge Ihres tatsächlichen Zahlungsanbieters; eine reine Autorisierung oder Teilzahlung aktiviert keine Tickets.

## Mail, Nummernkreis und SEO

| Einrichtung | Prüfung |
| --- | --- |
| Mailtransport und Absender | Shopware-SMTP/Absender konfigurieren; Testversand ausschließlich an kontrollierte Adressen durchführen. |
| Vorlage Ticketversand | Deutsche und englische Vorlage vorhanden, mit `tickets` (`ticketNumber`, `eventName`, `typeName`) nutzbar. PDF wird separat angehängt. |
| Nummernkreis Ticketnummern | Native Kennung `moorl_tv_ticket`; Standard `T-{n}` ab 10000. Bestehende Nummern und Zähler werden nicht zurückgesetzt. |
| SEO | Standardroute `frontend.moorl.tv.detail`; Muster `tickets/{{ sale.translated.name }}/{{ sale.id }}`. Nach Änderungen Index aktualisieren. |

Bei erneuter Installation dieser Datenpakete werden vorhandene Nummernkreis-Konfiguration, Mailvorlagen und SEO-Templates erhalten. Ein Versandstatus `sent` belegt die Annahme durch den Mailtransport, nicht die Zustellung ins Postfach oder das Öffnen durch den Empfänger.

## Einlasspersonal einrichten

1. Prüfen, ob das Datenpaket **scanner-role** installiert ist; bei bestehenden Installationen gegebenenfalls über die Foundation-Datenverwaltung nachladen.
2. Unter **Einstellungen → System → Benutzer & Berechtigungen** einen separaten Benutzer anlegen.
3. Die Rolle **Ticket Vendor – Scanner** zuweisen und Administratorzugriff ausschalten.
4. Weitere Rollen entfernen, wenn ausschließlich Einlassberechtigungen gewünscht sind.
5. Mit diesem Benutzer anmelden und **Dashboard → Ticketscanner** testen.

Die Rolle gewährt `moorl_tv_ticket_sale:read` und `moorl_tv_ticket:scan`. Allgemeines Ticketändern, Versand, Widerruf, PDF-Ausgabe, Kunden- und Bestellzugriffe sind nicht enthalten. Standardrechte, die Shopware jeder Admin-Anmeldung automatisch gibt, bleiben bestehen. Veranstaltungsbezogene Zugriffsbeschränkungen gibt es nicht.

Das Datenpaket erstellt weder Benutzer noch Passwörter noch API-Zugangsschlüssel. Ein erneuter Import überschreibt eine bestehende Rolle mit derselben Paket-ID nicht; individuelle Anpassungen und Zuweisungen bleiben erhalten. Das ausdrückliche Entfernen des Pakets entfernt diese Rolle und ihre Zuordnungen. Benötigte eigene Rollen vorher separat anlegen.

**Umstellung bestehender Scanner:** Der Check-in-Endpunkt verlangt jetzt `moorl_tv_ticket:scan`. Frühere Kombinationen aus Ticket-Update- und Check-in-Create-Recht ersetzen dieses Recht nicht. Neue Rolle zuweisen oder unter zusätzlichen Berechtigungen den Scanner-Eintrag aktivieren; anschließend neu anmelden. Allgemeine Ticketrechte können entfallen, wenn sie sonst nicht gebraucht werden.

## Vor dem ersten Verkauf

- Veranstaltung und Typ aktivieren und gültige Zeitfenster kontrollieren.
- Preise, Steuer, Währung, Kontingent und Kaufgrenzen prüfen.
- Datum/Uhrzeit bei Importen in UTC pflegen und Zeitzonenanzeige im verwendeten Theme prüfen.
- Konto- und Gastbestellung mit Ihrem Zahlungsanbieter testen.
- Ticket-PDF, Empfängerzuordnung und tatsächliche SMTP-Zustellung prüfen.
- Zwei Einlassgeräte mit demselben Ticket testen: nur eine eigenständige Anfrage darf neu akzeptiert werden.
- Kameraerkennung im vorgesehenen Browser und manuelle Token-Eingabe testen.

## Demodaten

Der Demoimport legt die aktive Kategorie **Veranstaltungen** unter der Shop-Navigation an und weist ihr die CMS-Vorlage **Ticket Vendor – Events** mit dem Veranstaltungslisting zu. Der Einstieg erfolgt über die normale Kategorienavigation; ein zusätzlicher Tickets-Link in den Header-Aktionen entfällt. Beim Entfernen des Demopakets wird die Demo-Kategorie entfernt, sofern sie keine Unterkategorien enthält. Die CMS-Vorlage und selbst angelegte Kategorien bleiben erhalten.

Das optionale Foundation-Demopaket **standard** umfasst drei Veranstaltungen, sieben Tickettypen, zwölf Tickets und drei Check-in-Einträge. Es enthält auch eine interne Gästeliste mit drei gültigen Tickets. Verwenden Sie es in einer Testumgebung; die Tokens sind bekannte Beispieldaten.

Ergänzend enthält es vier Artists mit Social Links, Kollektiv-/Labelangaben und unterschiedlichen Booking-Beispielen: Kontaktformular, externe E-Mail, externe URL und ein nicht öffentlich für Booking angebotener Artist. Interne Buyout-Gagen und Hinweise sind ebenfalls hinterlegt. Drei Bühnen beziehungsweise Räume und sechs Auftritte zeigen parallele Sets, mehrere Auftritte desselben Artists sowie eine Ankündigung ohne feste Bühne oder Uhrzeit.

Vier offene Gästelistenanmeldungen für **Live im Stadtpark** zeigen Einladende, freiwillige Aufgaben, Bemerkungen und eine gemeinsame E-Mail-Adresse für zwei Gäste. Das Konzert erhält beim ersten Import den kostenlosen internen Tickettyp und den von Foundation gewählten Storefront-Verkaufskanal als Formularkonfiguration. Die Anmeldungen enthalten Verkaufskanal und Sprache für die spätere Ticketfreigabe im Admin. Den geheimen Formularlink dort über die reguläre Link-Aktion erzeugen; er ist nicht fest in den Demodaten hinterlegt. Erneuter Import erhält den erzeugten Link, bestehende Entscheidungen und Ticketzuordnungen sowie eine zwischenzeitliche Deaktivierung des konfigurierten Formulars.

Der Import selbst löst keinen Versand aus. Aktive Worker können danach noch nicht versendete gültige Demotickets aufgreifen. Verwenden Sie für Demos einen Test-Mailtransport und keine echten Empfänger. Der Verkaufszähler wird anhand der belegenden Ticketstatus gesetzt.

## Aktualisierung und Deinstallation

Vor Updates Daten und Konfiguration sichern. Aktualisieren Sie Foundation und Ticket Vendor innerhalb ihrer unterstützten Versionsgrenzen, stellen Sie Abhängigkeiten und Assets bereit, leeren Sie Caches und starten Sie Worker neu. Neu hinzugekommene Datenpakete werden bei der regulären Plugin-Aktualisierung installiert; bestehende Konfiguration wird gemäß den jeweiligen Paketen erhalten.

Eine Deinstallation mit Beibehaltung der Benutzerdaten erhält die Daten. Bei einer Deinstallation ohne Beibehaltung entfernt der Foundation-Lifecycle die Plugin-Daten sowie paketbezogene Einrichtungen. Prüfen Sie vorher Archivierung, Bestellbezüge und Rollenverwendung. Datenpakete und Plugin nicht während eines laufenden Einlasses entfernen.

## Fehlerdiagnose

| Symptom | Kontrollieren |
| --- | --- |
| Keine Veranstaltung sichtbar | Aktiv, Anzeigezeitfenster, Eventende; ohne Ende den Beginn. |
| Kauf abgelehnt | Typzuordnung, aktive Verkaufszeiträume, Kontingent und aggregierte Kaufgrenzen. |
| Zahlung bestätigt, Ticket offen | Native primäre/neuste Transaktion, `paid`, Statusereignisse und Serverprotokoll. |
| Zahlungsfristen werden nicht verarbeitet | Taskregistrierung, laufender Task-Runner und Messenger-Verarbeitung. |
| Mail fehlt | Empfänger, Vorlage, SMTP, Versandstatus/-versuche, Warteschlange und Fehlertransport. |
| Scanner zeigt 403 | Neues Scan-Recht, vollständige Rollenzuweisung und erneute Anmeldung. |
| Kamera startet nicht | HTTPS, Kameraberechtigung, `BarcodeDetector`; manuelle Eingabe verwenden. |
| „Veranstaltung geschlossen“ | Veranstaltung aktiv, Endzeit in UTC und Serverzeit. |
| Kunde sieht Ticket nicht | Direkte Kundenzuweisung beziehungsweise Bestellkunde und Verkaufskanal. Eine reine E-Mail-Zuordnung erzeugt keinen Kontozugriff. |

Für technische Details siehe [Laufzeitdokumentation](runtime.md), [Schema](schema.md) und [Scanner-API](mobile-app.md). Die [Händleranleitung](index.md) beschreibt die tägliche Verwaltung.

## Ticket-Darstellung und Personalisierung

Unter **Erweiterungen → Meine Erweiterungen → Ticket Vendor → Konfiguration → Ticket-Darstellung** wählen Sie Karten oder eine kompakte Liste. Verfügbarkeit, genaue Restmenge, Ticketbilder und Beschreibungen lassen sich getrennt anzeigen; ausverkaufte Tickettypen können ausgeblendet werden. Einstellungen gelten je Verkaufskanal und für die Ticket-Auswahl auf Veranstaltungsseiten und im Detail-CMS-Element.

Jedes Ticket hat ein Feld **Vor- und Nachname** (`attendeeName`). Beim Kauf wird der Bestellkundenname als Ausgangswert gespeichert. Kunden mit Konto ändern den Namen unter **Mein Konto → Tickets**; Händler bearbeiten ihn im Ticketformular. Änderungen sind nur bei `pending` und `valid` möglich. PDF und Scanner zeigen den Namen; ein erneuter PDF-Download enthält die Änderung. Es wird keine zusätzliche E-Mail ausgelöst. Der Ticketstatus wird im Formular schreibgeschützt angezeigt; die vorgesehenen Statusaktionen bleiben verfügbar.

Vor dem Deployment das neue nullable Feld `moorl_tv_ticket.attendee_name` (`VARCHAR(511)`) über das externe Schemawerkzeug anlegen. Bestehende Tickets mit leerem Namensfeld verwenden den Bestellkundennamen beziehungsweise den zugewiesenen Kunden als Fallback. Anschließend Administration und Storefront bauen, Theme kompilieren, Cache leeren und Worker neu starten.

## Handynummer pro Ticket

Optional können Sie pro Ticket eine **Handynummer** ergänzen oder ändern. Für die Bearbeitung gelten dieselben Regeln wie beim Namen. Die Nummer erscheint beim Scan und kann im Browser-Scanner über **Anrufen** gewählt werden.

`attendeePhone` / `attendee_phone`: nullable `VARCHAR(64)`; vor dem Einsatz mit dem externen Schemawerkzeug anlegen.

## Artists, Stages und geheime Gästeliste

Artists werden unter den Kataloginhalten gepflegt. „Auf der Website für Booking anbieten“ zeigt das Profil in der Booking-Auswahl; Anfragen führen zur vorhandenen Kontaktseite oder zum optionalen externen Bookingkontakt. Gage und Bookingnotiz bleiben intern. Das CMS-Element „Artists für Booking“ und die Seite /artists/booking verwenden dieselbe Auswahl.

Im Event unter „Programm“ Stages und Auftritte anlegen. Ein Artist kann mehrere Sets haben; Stage und Uhrzeiten sind optional. Line-up und Timetable werden separat am Event veröffentlicht. Eine optionale maximale Teilnehmerzahl begrenzt alle Tickettypen gemeinsam. „In öffentlichen Listen anzeigen“ kann ausgeschaltet werden; der direkte Eventlink bleibt erreichbar.

Unter „Gästeliste“ Formular aktivieren, einen kostenlosen Tickettyp und den Verkaufskanal wählen, Einleitung und Regeln pflegen und den geheimen Link kopieren. Anmeldungen reservieren keinen Platz. Nach Prüfung erstellt „Ticket erstellen und senden“ das Ticket und stößt die E-Mail an. Fehler und erneuter Versand verwenden dasselbe Ticket. Mehrere Gäste können dieselbe E-Mail nutzen. Das Formular enthält Ehrenamt, eingeladen von und Bemerkungen, ohne Zahlungsabwicklung. Tickets werden einzeln über das Kontextmenü der Anmeldung erstellt und versendet.

Vor dem Update das externe Schemawerkzeug für die neuen Tabellen und Felder einsetzen. Bestehende Bestellpositionsbezüge müssen vor dem Entfernen der alten Spalten übernommen werden; der Befehl moorl-tv:backfill-ticket-orders zeigt zunächst nur eine Vorschau. Ablauf und explizite Anwendung stehen in [Schema und Datenübernahme](schema.md). Anschließend Administration/Storefront bauen und Worker neu starten.
