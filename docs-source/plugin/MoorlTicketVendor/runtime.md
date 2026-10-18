# Ticket Vendor: Betrieb und Funktionen

Die vollständige [Händleranleitung](index.md), [Installation](manual.md), [Kundenanleitung](customer.md) und [App-/API-Dokumentation](mobile-app.md) stehen zusätzlich als deutsche und englische `.tpl.md`-Vorlagen mit gerenderten Markdown-Dateien bereit. Die mobile App ist ein dokumentiertes Zielbild und noch nicht implementiert.

## Einstieg

Die Kunden-Ticketübersicht verwendet die Struktur und Styles der nativen Shopware-Bestellübersicht mit aufklappbaren Details. Jedes Ticket hat zusätzlich einen zufälligen, vom QR-Token unabhängigen Deeplink unter `/account/tickets/{id}/{deeplink}`. Er öffnet nur dieses Ticket ohne Kundenlogin; Bearbeitung per POST auf `/personalize` und PDF-Download per GET auf `/download` verwenden denselben Link. Bestelltickets bleiben an ihren Verkaufskanal gebunden. Bearbeitung ist bei `pending`/`valid`, PDF-Download bei `valid`/`redeemed` möglich. Der Link erzeugt keine Kundenanmeldung. Antworten sind nicht cachebar, nicht indexierbar und übertragen keinen Referrer.

Für die Bereitstellung `moorl_tv_ticket.deeplink` samt eindeutigem Index mit dem externen Schemawerkzeug ergänzen. Neue Tickets erhalten beim DAL-Insert einen individuellen Code, bestehende beim Anzeigen im Kundenkonto oder beim Versand. Das Datenpaket `ticket-mail` erneut importieren: Unveränderte alte Standard-Mailtexte werden um die persönlichen Links ergänzt. Eigene Mailtexte bleiben erhalten; dort kann pro Ticket `{{ ticket.url }}` als Link verwendet werden. Die Versandprojektion enthält diesen Verwaltungslink, weiterhin keinen QR-Token. Die Domain folgt Bestellung beziehungsweise Kundenzuordnung und Sprache; bei manuellen Tickets ohne Zuordnung wird eine aktive Storefront-Domain verwendet.

Veranstaltungen werden unter Kataloge verwaltet, Tickettypen unter Einstellungen. Tickettypen gehören zu genau einer Veranstaltung. Zum öffentlichen Verkauf müssen Veranstaltung und Typ aktiv sein und die Verkaufszeiträume passen. Ohne Endzeitpunkt endet der öffentliche Verkauf zum Veranstaltungsbeginn. Preise, Steuern und Kontingente werden serverseitig gelesen.

Die Veranstaltungsübersicht ist eine normale Shopware-Kategorie mit dem Foundation-CMS-Baustein `moorl-tv-ticket-sale-listing`; in der Plugin-Konfiguration wird sie unter `category` ausgewählt. Die eigene Listing-Route `/tickets` entfällt. Der Detailcontroller bedient ausschließlich `/tickets/{saleId}`. Native SEO-URLs verwenden standardmäßig `tickets/{{ sale.translated.name }}/{{ sale.id }}`. Angemeldete Kunden finden berechtigte Tickets unter `/account/tickets` und können gültige Tickets als PDF herunterladen.

Bestell- und Kundendetails enthalten Ticket-Tabs. In der Veranstaltung lassen sich Tickets direkt anlegen. Der Tickettyp wird auf die Veranstaltung eingeschränkt. Ticketnummern entstehen beim Speichern aus dem Core-Nummernkreis `moorl_tv_ticket` und bleiben anschließend unveränderlich. Token werden für neue Tickets kryptographisch zufällig mit 32 Zeichen erzeugt und erscheinen ausschließlich im berechtigten PDF beziehungsweise QR-Code.

## Suche und Erlebniswelten

**Veranstaltungen mit Archiv (statisch)** (`moorl-tv-ticket-sale-static-listing`) ist ein zusätzlicher CMS-Baustein. Er zeigt alle aktiven Events unabhängig vom Ticket-Verkaufszeitraum, ohne Filter oder Seitennavigation: laufende/kommende Events nach Beginn aufsteigend, vergangene danach absteigend und ausgegraut. Für die Einordnung zählt `endAt`, ersatzweise `startAt`; genau zum Ende wechselt das Event ins Archiv. Flyer, Termin, Titel, Ort und Teaser werden aus dem Event geladen. Archiv-Einträge ohne alternative URL verlinken nicht auf die nicht mehr verfügbare Ticketdetailseite; zukünftige Events außerhalb des Verkaufszeitraums bekommen ebenfalls keinen internen Kauflink.

Am Event kann unter **Allgemein → Alternative Veranstaltungs-URL** beispielsweise die Adresse einer privaten Community hinterlegt werden. Titel und Aktionsbutton im statischen Listing verwenden dann diese Adresse. Externe Adressen öffnen mit `noopener noreferrer` in einem neuen Tab. Die Adresse ist optional; der normale Verkauf und das bisherige dynamische Listing behalten ihre Regeln. Vor Verwendung die nullable Spalte `alternative_url` mit dem Schemawerkzeug erzeugen und Administration/Theme bauen.

Die Foundation-Erweiterte-Suche muss aktiviert sein. Ticket Vendor ergänzt dann einen Veranstaltungsbereich in der Schnellsuche und auf der Suchergebnisseite. Die Plugin-Konfiguration steuert Aktivierung, Trefferzahl und optional das Foundation-Layout getrennt für beide Ansichten und je Verkaufskanal. Es gelten dieselben Sichtbarkeits- und Verkaufszeitfilter wie auf den Veranstaltungsseiten; individuelle Kundentickets werden nicht durchsucht.

Das separate Foundation-Datenpaket `cms-page` installiert bei Aktivierung oder Update die geschützten Vorlagen **Ticket Vendor – Events** und **Ticket Vendor – Event detail**. Das eigene Datenpaket wird auch bei bereits installiertem Basisdatenpaket nachgeladen. Für Anpassungen die Vorlage in den Erlebniswelten duplizieren. Der Kategorie eine Erlebniswelt mit Veranstaltungslisting zuweisen und sie in der Plugin-Konfiguration unter `category` auswählen. Der Zurück-Link auf Veranstaltungsdetails führt zur SEO-URL dieser Kategorie und entfällt bei leerer Auswahl. `cmsPageId` bestimmt die Standard-CMS-Seite für Veranstaltungsdetails; eine direkt am Event hinterlegte CMS-Seite hat Vorrang. Ohne CMS-Auswahl wird die einfache Detaildarstellung verwendet.

Das CMS-Element `moorl-tv-ticket-sale-listing` bietet Veranstaltungslisten einschließlich Seitennavigation und lässt sich auch auf normalen CMS-Seiten verwenden. `moorl-tv-ticket-sale-detail` rendert auf Veranstaltungsdetailseiten die Veranstaltungsdaten und den Ticketkauf. Ältere ergänzende CMS-Inhalte ohne dieses Element werden weiterhin innerhalb der bisherigen Detaildarstellung eingebunden.

Nach Übernahme des Codes das Plugin aktualisieren und die Administration neu bauen, damit Datenpaket, Suchkonfiguration und CMS-Element im bestehenden Shop verfügbar sind.

## Bestellung und Kontingent

Die native Warenkorbposition heißt `moorl_tv_ticket`; `referencedId` ist die ID des Tickettyps. Der Collector liest Preis und Steuer neu ein. Der Processor verwirft vom Client gesetzte Preisdefinitionen, Flags und Payloads und prüft Verkaufszeiten sowie aggregierte Mindest-/Höchstmengen pro Tickettyp.

Im Warenkorb und in der Warenkorb-Seitenleiste stehen unter dem Tickettyp der übersetzte Veranstaltungsname und ein Auszug des Event-Teasers, ersatzweise der Event-Beschreibung. Der Auszug enthält höchstens 200 Zeichen ohne HTML. Beide Angaben werden bei der Neuberechnung aus den aktuellen Veranstaltungsdaten übernommen.

Der Warenkorb reserviert keine Plätze. Erst die gemeinsame Transaktion aus nativer Bestellspeicherung und Ticketerstellung belegt das Kontingent. Pro Bestellposition und Stückzähler entsteht genau ein Ticket. Wiederholungen verwenden bestehende Tickets. Verkaufsvoraussetzungen werden unmittelbar vor der Erstellung aus aktuellen gesperrten Daten gelesen.

Der DAL prüft auch manuelle/API-Schreibzugriffe: Tickettyp und Veranstaltung müssen zusammenpassen, und `pending`, `valid` sowie `redeemed` zählen gegen das Kontingent. `expired` und `revoked` belegen keinen Platz. Sperren folgen Veranstaltung → Tickettyp → Ticket; der abgeleitete `quantitySold` wird in derselben Schreibtransaktion aktualisiert. Ein Typ mit ausgestellten Tickets kann nicht nachträglich zu einer anderen Veranstaltung verschoben werden.

## Zahlung und Ablauf

Neue Bestelltickets sind `pending`. Die konfigurierbare Zahlungsfrist beträgt standardmäßig 30 Minuten. Nur der bestätigte native Zahlungsstatus `paid` aktiviert Tickets und stellt sie zum Versand an. Maßgeblich ist die aktuelle primäre Zahlungstransaktion beziehungsweise die neueste Transaktion, wenn keine primäre hinterlegt ist.

Bestellstornierung, vollständige Erstattung und Chargeback widerrufen noch belegende Tickets. Der Ablaufjob liest den Zahlungszustand unter Sperre erneut: Bezahlte Tickets werden aktiviert; tatsächlich offene Bestellungen werden storniert und ihre Tickets auf `expired` gesetzt. Bei bereits abgeschlossenen, aber unbezahlten Bestellungen verwendet er die nativen Übergänge `reopen` und `cancel`. Ein Fehler bei einer einzelnen Bestellung wird protokolliert und blockiert die übrigen Bestellungen nicht.

Nach Fristablauf bereits stornierte Bestellungen bleiben bei später Zahlung gesperrt; das System protokolliert die nötige manuelle Zahlungsabstimmung. Es führt keine automatische Zahlungserstattung beim Zahlungsanbieter aus. Noch nicht stornierte abgelaufene Tickets können bei bestätigter Zahlung nur innerhalb des weiterhin verfügbaren Kontingents aktiviert werden. Teilzahlung genügt nicht zur Aktivierung.

## Dokumente und Versand

`dompdf/dompdf` und `tecnickcom/tcpdf` sind Composer-Abhängigkeiten. PDFs enthalten Veranstaltungsdaten, Tickettyp, lesbare Nummer und lokal erzeugten QR-Code. Externe Ressourcen und PHP-Ausführung im PDF-Renderer sind deaktiviert.

Das Foundation-Datenpaket `ticket-mail` installiert einen nativen Mailtyp und deutsche/englische Vorlagen. Vorhandene Vorlagen werden erhalten. Die Versandadresse kommt aus dem expliziten Ticketempfänger, sonst dem zugewiesenen Kunden, sonst dem Bestellkunden-Snapshot. Automatische Zustellung gruppiert Tickets nach Bestellung, Verkaufskanal und tatsächlichem Empfänger. So landen abweichende Empfänger nicht im selben Anhang.

Der Messenger-Handler prüft Gültigkeit und Versandstatus vor jeder Zustellung. `deliveryAttempts`, `deliveryStatus`, `deliveredAt` und ein bereinigter Fehlercode dokumentieren den Verlauf. Eine verbindungsgebundene Datenbanksperre serialisiert gleichzeitige Versandversuche. Bereits versendete Tickets werden bei automatischen Wiederholungen übersprungen; die Admin-Aktion kann ausdrücklich erneut versenden. Fehlgeschlagene Zustellung liefert einen Fehlerstatus an die Administration.

Der periodische Wiederherstellungslauf stellt noch nicht zugestellte gültige Tickets mit weniger als fünf Versuchen erneut an, frühestens fünf Minuten nach der letzten Änderung. Messenger verwendet zusätzlich seine konfigurierte begrenzte Retry-Strategie. Nach ausgeschöpften Versuchen lassen sich Fehler beheben und Tickets manuell erneut versenden. Ein Prozessabbruch zwischen SMTP-Annahme und Speicherung des Erfolgs kann eine doppelte E-Mail verursachen; es gibt keine transaktionsübergreifende Exactly-once-Garantie mit SMTP.

Flow Builder bietet die Aktion „Tickets versenden“ für Ereignisse mit Bestellkontext an. Sie stellt gültige Tickets in die Versandwarteschlange und benötigt keine zusätzliche Konfiguration.

## Check-in und Zugriffe

Der Admin-Scanner bietet Kamera-QR-Erkennung über `BarcodeDetector` und manuelle Token-Eingabe. Kameraerkennung hängt von Browserunterstützung und einem sicheren Browserkontext ab; die manuelle Eingabe bleibt verfügbar. Bei einem Netzwerkfehler verwendet ein erneuter Versuch dieselbe Scan-Anfrage-ID.

`POST /api/_action/moorl-tv/check-in` erwartet `saleId`, `token`, `scanRequestId` und optional `deviceId`. Authentifizierung erfolgt über die native Admin-/Integration-API; benötigt wird das dedizierte Recht `moorl_tv_ticket:scan`. Nach der nativen ACL-Prüfung führt der Controller ausschließlich den fest definierten Check-in samt Audit in einem begrenzten System-Scope aus; allgemeine Ticket-Schreibrechte erhält der Benutzer nicht. Die Antwort enthält `result`, `ticketNumber`, `attendeeName`, `attendeePhone` und `checkinId`, keinen Token. Erfolgreiche Einlösung erfolgt atomar, Wiederholungen derselben Anfrage erhalten dieselbe Antwort, und eine andere Anfrage erkennt das Ticket als bereits eingelöst. Falsche Veranstaltung, geschlossene Veranstaltung und ungültige Tickets werden abgewiesen und protokolliert.

Das Foundation-Paket `scanner-role` erstellt die Rolle **Ticket Vendor – Scanner** mit genau `moorl_tv_ticket:scan` und `moorl_tv_ticket_sale:read`. Es erzeugt keine Benutzer oder Zugangsschlüssel und erhält bei erneutem Import bestehende Rollenanpassungen und Zuordnungen. Die Rolle erlaubt keine allgemeine Ticketabfrage/-änderung, PDFs, Versand, Widerruf, Kunden-/Bestellabfrage oder direkte Check-in-CRUD-Zugriffe. Native Standardrechte für authentifizierte Admin-Benutzer gelten zusätzlich. Zusätzliche Rollen und der Administrator-Schalter erweitern den Zugriff; eine Beschränkung auf einzelne Veranstaltungen gibt es nicht. Bisherige Scanner benötigen das neue Recht auch dann, wenn sie Ticket-Update-/Check-in-Create-Rechte haben.

Admin-PDFs erfordern `moorl_tv_ticket:read`, Senden/Widerrufen erfordern `moorl_tv_ticket:update`. Kundendownloads prüfen die direkte Kundenzuordnung oder den Bestellkunden, wenn keine direkte Zuordnung besteht. Eine Neuzuweisung an einen anderen Kunden sperrt den ursprünglichen Bestellkunden aus. Downloads sind privat und werden nicht zwischengespeichert.

## Installation und Worker

Bei regulärer Plugin-Aktivierung/Aktualisierung installiert der bestehende Foundation-Lifecycle-Helper die Datenpakete `data`, `ticket-number`, `ticket-mail`, `seo` und `scanner-role`. Wiederholung setzt Händlerkonfiguration, Vorlagen, Nummernkreisstand und Scanner-Rollenanpassungen nicht zurück. Bei bestehenden Entwicklungsinstallationen lassen sich diese Pakete auch über die Foundation-Datenverwaltung nachladen.

Das Schema bleibt bei sechs Tabellen; neue handgeschriebene Migrationen sind nicht erforderlich. Bestehende, vom Benutzer erzeugte Migrationen bleiben erhalten. Die Dokumentation in `schema.md` beschreibt die Feldnamen.

Im Zielsystem müssen die üblichen Shopware-Worker laufen:

```sh
bin/console scheduled-task:register
bin/console scheduled-task:run --time-limit=60
bin/console messenger:consume async low_priority --time-limit=60
bin/console dal:refresh:index --only=moorl_tv_ticket_sale.seo
```

Der Task `moorl_tv.expire_tickets` läuft standardmäßig minütlich und übernimmt Ablauf sowie Wiederherstellung der Zustellung. Supervisor/Cron und Transportnamen richten sich nach der Shopware-Installation. Der Mailer benötigt die normale Shopware-Absender-/SMTP-Konfiguration. Nach Deployment Worker neu starten und Administration/Storefront-Assets veröffentlichen.

## Prüfung

Die PHPUnit-Suite läuft gegen eine ausdrücklich gewählte isolierte `moorl_tv_*_test`-Datenbank. Sie prüft unter anderem echte parallele Verbindungen für den letzten Platz und doppelte Einlösung, Bestell-Rollback, Zahlungs-/Erstattungs-/Ablaufzustände, Kundenzugriffe, PDFs und Versandfehler. HTTP-Tests rendern Veranstaltungsseiten und fügen Tickets über den nativen Shopware-Warenkorb-Endpunkt hinzu. Mailtransporte sind in den Versandtests ersetzt; es werden keine echten E-Mails versendet.

Die Administration hat Node-Tests mit installierten Shopware-/Foundation-Helfern. Container, Twig und gezielte Admin-/Storefront-Produktionsbuilds werden separat geprüft. Ein realer Zahlungsanbieter, echte SMTP-Zustellung und Gerätekameras sind zusätzlich in der jeweiligen Betriebsumgebung zu prüfen.

Abschlussprüfung am 16.10.2026: **87 PHP-Tests mit 1085 Assertions**, ohne übersprungene Tests, Warnungen oder Deprecations; **27 Admin-Tests**, beide Produktionsbuilds, Containerprüfung, 87 PHP-Syntaxprüfungen und 14 Twig-Prüfungen erfolgreich. Eine unabhängige Codeprüfung wurde nach den Korrekturen ohne offene wichtige Befunde abgeschlossen.

Ergänzungsprüfung für Dokumentation und Scanner-Rolle am 16.10.2026: **89 PHP-Tests mit 1134 Assertions** ohne übersprungene Tests, Warnungen oder Deprecations sowie **28 Admin-Tests** erfolgreich. Der gezielte Admin-Produktionsbuild, Containerprüfung, Store-YAML/JSON und Dokumentations-Frontmatter wurden geprüft. HTTP-Tests belegen Check-in mit der eingeschränkten Rolle, gesperrte allgemeine Ticketaktionen und erhaltene Rollenänderungen/-zuweisungen beim erneuten Foundation-Import.
