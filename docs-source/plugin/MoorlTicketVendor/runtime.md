# Ticket Vendor: Betrieb und Funktionen

Prüfstand 21.10.2026 nach der Datenbankbehebung: **325 PHP-Tests mit 3332 Assertions** und **92 Administrationstests** bestanden. Der PHP-Lauf meldet sieben bestehende Deprecations in der Core-/Foundation-Listingsuche. Die SQL-Initialinstallation und die additive Indexergänzung mit bestehenden Testdaten wurden isoliert geprüft; der bestehende Demoshop wurde lesend abgeglichen. Synthetische Lastmessungen ergänzen die Funktionsprüfung; ihre Ergebnisse und Grenzen stehen unter [Datenbankprüfung und Lastverhalten](#datenbankprüfung-und-lastverhalten). Neun reale FullHD-Aufnahmen aus Storefront und Administration sind in der [Händleranleitung](index.md#screenshots-aus-storefront-und-administration) eingebunden. Echte Payment-/SMTP-Transporte und Gerätekameras sind nicht Teil dieser Prüfung.

Die vollständige [Händleranleitung](index.md), [Installation](manual.md), [Kundenanleitung](customer.md) und [App-/API-Dokumentation](mobile-app.md) stehen zusätzlich als deutsche und englische `.tpl.md`-Vorlagen mit gerenderten Markdown-Dateien bereit. Die mobile App ist ein dokumentiertes Zielbild und noch nicht implementiert.

## Einstieg

### Einheitliche Storefront-Überschriften

`storefront/component/moorl-tv-header.html.twig` liefert den gemeinsamen Header für Seiten (`headingLevel: 1`), Sektionen (`2`) und Karten/Untersektionen (`3`). Er nimmt `title`, `titleId`, `eyebrow`, `lead`, `detail` und `additionalClasses` entgegen. Normale Texte werden escaped, Detailinhalte sanitisiert. Ohne eigenen Eyebrow nutzt nur die Seitenvariante den Shopnamen. Die Darstellung verwendet feste Größen an responsiven Breakpoints und für Seitenheader einen unteren Abstand von 3rem.

Unter **Erweiterungen → Meine Erweiterungen → Ticket Vendor → Konfigurieren → Storefront-Überschriften** lassen sich die Header für CMS-/Kategorie-/Landingpages und Login-/Checkout-Anmeldeseiten getrennt deaktivieren. Beide Optionen sind standardmäßig aktiv (`pageHeaderCmsEnabled`, `pageHeaderLoginEnabled`). Bei deaktivierter Einbindung erscheint die native Shopware-Darstellung. Statische redaktionelle CMS-Inhalte bleiben erhalten; bereits im Header enthaltene dynamische Kategorienamen und Beschreibungen werden nicht doppelt ausgegeben.

Die Plugin-Seiten verwenden den Header unabhängig vom aktiven Theme. Sidequest benötigt dafür keine eigenen Seitenheader-Templates.

Eventfotos werden im Hochformat **4:5** dargestellt; das passende Uploadformat ist **1080 × 1350 px**. Im Event-Header steht das Foto ab 768 px links und der Hero-Bereich rechts, auf kleineren Bildschirmen untereinander. Ohne Foto nutzt der Hero die volle Breite. Das Format gilt auch für die Standard-Veranstaltungslisten. Themes können den rechten Bereich über `moorl_tv_detail_header_hero` überschreiben; Foto und Spaltenlayout bleiben dabei erhalten.

Die Kunden-Ticketübersicht verwendet die Struktur und Styles der nativen Shopware-Bestellübersicht mit aufklappbaren Details. Jedes Ticket hat zusätzlich einen zufälligen, vom QR-Token unabhängigen Deeplink unter `/account/tickets/{id}/{deeplink}`. Er öffnet nur dieses Ticket ohne Kundenlogin; Bearbeitung per POST auf `/personalize` und PDF-Download per GET auf `/download` verwenden denselben Link. Bestelltickets bleiben an ihren Verkaufskanal gebunden. Bearbeitung ist bei `pending`/`valid`, PDF-Download bei `valid`/`redeemed` möglich. Der Link erzeugt keine Kundenanmeldung. Antworten sind nicht cachebar, nicht indexierbar und übertragen keinen Referrer.

Für die Bereitstellung `moorl_tv_ticket.deeplink` samt eindeutigem Index bei bestehenden Tabellen gezielt per SQL ergänzen. Neue Tickets erhalten beim DAL-Insert einen individuellen Code, bestehende beim Anzeigen im Kundenkonto oder beim Versand. Das Datenpaket `ticket-mail` erneut importieren: Unveränderte alte Standard-Mailtexte werden um die persönlichen Links ergänzt. Eigene Mailtexte bleiben erhalten; dort kann pro Ticket `{{ ticket.url }}` als Link verwendet werden. Die Versandprojektion enthält diesen Verwaltungslink, weiterhin keinen QR-Token. Die Domain folgt Bestellung beziehungsweise Kundenzuordnung und Sprache; bei manuellen Tickets ohne Zuordnung wird eine aktive Storefront-Domain verwendet.

Veranstaltungen werden unter Kataloge verwaltet, Tickettypen unter Einstellungen. Tickettypen gehören zu genau einer Veranstaltung. Zum öffentlichen Verkauf müssen Veranstaltung und Typ aktiv sein und die Verkaufszeiträume passen. Ohne Endzeitpunkt endet der öffentliche Verkauf zum Veranstaltungsbeginn. Preise, Steuern und Kontingente werden serverseitig gelesen.

Die Veranstaltungsübersicht ist eine normale Shopware-Kategorie mit dem Foundation-CMS-Baustein `moorl-tv-ticket-sale-listing`; in der Plugin-Konfiguration wird sie unter `category` ausgewählt. Die eigene Listing-Route `/tickets` entfällt. Der Detailcontroller bedient ausschließlich `/tickets/{saleId}`. Native SEO-URLs verwenden standardmäßig `tickets/{{ sale.translated.name }}/{{ sale.id }}`. Angemeldete Kunden finden berechtigte Tickets unter `/account/tickets` und können gültige Tickets als PDF herunterladen.

Bestell- und Kundendetails enthalten Ticket-Tabs. In der Veranstaltung lassen sich Tickets direkt anlegen. Der Tickettyp wird auf die Veranstaltung eingeschränkt. Ticketnummern entstehen beim Speichern aus dem Core-Nummernkreis `moorl_tv_ticket` und bleiben anschließend unveränderlich. Standardtickets erhalten weiterhin kryptographisch zufällige Tokens mit acht Zeichen; der bestehende Gästelistenpfad verwendet weiterhin 32 Zeichen. Die QR-Ausgabe enthält nur den jeweiligen Token. Vorhandene Codes und persönliche Links bleiben unverändert.

## Gästelisten aus CSV importieren

Das Profil **[moori] Ticket Vendor - Gästeliste** unterstützt Import und Export. `id` und `submissionId` werden bei neuen Anmeldungen automatisch erzeugt. Name und E-Mail zuordnen; Tickettyp (`typeId`) und Verkaufskanal (`salesChannelId`) müssen aus der Datei oder aus Profilstandardwerten kommen. Ohne Verkaufskanal wird der Datensatz abgewiesen. Eine nicht angegebene `languageId` erhält die Shopware-Systemsprache. Ein Import legt Anmeldungen an und versendet keine Tickets.

Tickets und Gästelisten-Anmeldungen benötigen Verkaufskanal und Sprache. Im Admin ist der Verkaufskanal manuell auszuwählen; die Sprache wird bei neuen Datensätzen mit der Systemsprache vorbelegt. Storefront und Checkout speichern ihren tatsächlichen Kontext. Die Ausstellung eines Gästelisten-Tickets übernimmt die gespeicherten Werte der Anmeldung. Die bisherigen Plugin-Vorgaben entfallen. Änderungen an der Anmeldung schreiben bereits ausgestellte Tickets nicht um.

Ein erneuter Import ohne Datensatz-IDs legt weitere Anmeldungen an. Zum gezielten Aktualisieren die IDs aus einem vorherigen Export verwenden. E-Mail-Adressen allein sind kein eindeutiges Merkmal, weil mehrere Gäste dieselbe Adresse verwenden dürfen.

## Gästelisten und Tickets löschen

Gästelisteneinträge und Tickets können über die normale Löschfunktion in der Administration einzeln gelöscht werden. Ein gelöschter Gästelisteneintrag lässt ein bereits ausgestelltes Ticket bestehen. Wird ein Ticket gelöscht, bleiben Anmeldung und Check-in-Protokoll erhalten und ihre Ticketverknüpfung wird aufgehoben. Belegtes Kontingent wird frei; Bestellungen und Kunden bleiben bestehen. Das Feld Decision und die Ablehnungs-/Stornoaktionen entfallen. Vor Verwendung das Schema bei bestehenden Datenbanken gemäß schema.md abgleichen, insbesondere die beiden Ticket-Fremdschlüssel auf SET NULL.

## E-Mail bei neuer Gästelisten-Anmeldung

Zusätzlich erhält der Gast über den separaten Flow `moorl_tv.guestlist.confirmation.requested` eine Eingangsbestätigung mit individuellem Link **Anmeldung bestätigen**. Die DE/EN-Vorlage und der aktive Flow **Ticket Vendor - Gästelisten-Anmeldung bestätigen** gehören ebenfalls zu `guestlist-mail`. Der Standardempfänger ist der Gast dieser Anmeldung. Die Adminvorlage und ihr Empfänger bleiben getrennt. Vor Aktivierung die beiden neuen Gästelistenspalten aus `schema.md` mit dem externen Werkzeug ergänzen und die fehlenden Basisdaten installieren. Normale erneute Installation erhält vorhandene Vorlagen/Flows; ein explizites Entfernen mit anschließendem Neuimport des Datenpakets setzt dessen erzeugte Standarddaten zurück.

Der Link öffnet `/guestlist/registration/{entryId}/confirm` ohne Kundenkonto. Das Aufrufen des gültigen signierten Links per GET speichert direkt **Anmeldung bestätigt am** in Liste und Detail und zeigt die Erfolgsmeldung. Es gibt keinen zusätzlichen Button. HEAD-Aufrufe bestätigen nichts. Wiederholtes Aufrufen behält den ersten Bestätigungszeitpunkt. Die Symfony-URI-Signatur gilt nur für genau diesen Datensatz und seinen gespeicherten Verkaufskanal. Mehrere Anmeldungen mit derselben E-Mail-Adresse erhalten getrennte Links und müssen einzeln bestätigt werden. Der Link hat kein Zeitlimit; bei geänderter E-Mail-Adresse oder gelöschtem Eintrag wird er ungültig. Die Bestätigung reserviert keinen Platz und erstellt kein Ticket. Die bisherige manuelle Ticketerstellung bleibt auch für unbestätigte Einträge verfügbar.

CSV-, Admin- und Demo-Einträge erhalten keine automatische Bestätigungsmail oder Bestätigung.

Im Kontextmenü einer Anmeldung kann **Bestätigungslink versenden** mit dem Zusatzrecht `moorl_tv_guestlist_entry:send_confirmation` gewählt werden. Das gilt für manuelle, importierte und offene Storefront-Anmeldungen, auch mit ausgestelltem Ticket. Die Aktion legt einen fehlenden Signierschlüssel an und löst den vorhandenen Bestätigungs-Flow in der gespeicherten Sprache und im Verkaufskanal der Anmeldung aus. Der konfigurierte Mail-Flow muss aktiv sein. Ein erneuter Versand verwendet denselben Link. Bereits bestätigte Anmeldungen werden nicht erneut angeschrieben. Versandfehler bleiben sichtbar und lassen einen erneuten Versuch zu. Es wird dabei weder ein Ticket erstellt noch die Anmeldung als bestätigt markiert.

Wiederholtes Absenden derselben Anfrage sendet keine weitere Nachricht. Der Gast-Flow stellt `guestlist.id`, `name`, `email`, `typeId`, `typeName`, `eventId`, `eventName` und `confirmationUrl` bereit. Die URL wird aus einer Domain des tatsächlichen Anmeldungs-Verkaufskanals gebildet, bevorzugt passend zur Sprache. Ein Mail-/Flowfehler nimmt eine bereits gespeicherte Anmeldung nicht zurück; der Fehler wird mit der Eintrags-ID protokolliert, ohne Link oder Schlüssel zu loggen.

Das Datenpaket **guestlist-mail** installiert den Flow **Ticket Vendor - Neue Gästelisten-Anmeldung** und eine deutsche/englische Mailvorlage **Neue Gästelisten-Anmeldung**. Der aktive Standard-Flow verwendet die normale Aktion **E-Mail versenden** mit Empfänger **Administration** (Benutzer mit Administratorrecht). Unter **Einstellungen → Flow Builder** können Empfänger, Bedingungen und Vorlage angepasst oder der Flow deaktiviert werden. Für eine einzelne Adresse statt aller Administratoren den Empfängertyp **Benutzerdefiniert** verwenden.

Auslöser ist `moorl_tv.guestlist.registered`, in der Administration **Ticket Vendor – Gästelisten-Anmeldung eingegangen**. Er wird nach einer neu gespeicherten Storefront-Anmeldung ausgelöst. Wiederholtes Absenden derselben Anfrage, fehlgeschlagene Anmeldungen sowie CSV-/Admin-Einträge erzeugen kein Event. Die Benachrichtigung enthält Name, E-Mail, optionale Handynummer, Veranstaltung und Tickettyp. Ohne Telefonnummer zeigt die Vorlage einen entsprechenden Hinweis.

Die Vorlagenvariablen stehen unter `guestlist`: `id`, `name`, `email`, `phone`, `typeId`, `typeName`, `eventId`, `eventName`, `adminUrl`. Der Link verwendet die konfigurierte `APP_URL` und öffnet `/admin#/moorl/tv/type/detail/{typeId}`. Er benötigt eine normale Adminanmeldung und die passenden Leserechte. Der geheime Formularlink und dessen Schlüssel werden nicht in die Benachrichtigung aufgenommen.

Das Paket wird beim regulären Plugin-Update installiert; dafür ist keine Schemaänderung nötig. Vorhandene Flows und Mailvorlagen werden durch die Paketinstallation nicht überschrieben. Die normale Shopware-Mailkonfiguration und deren Worker gelten weiterhin; Versandfehler machen eine bereits gespeicherte Anmeldung nicht ungültig. Die Registrierung verschickt dadurch kein Eintrittsticket an den Gast.

## Suche und Erlebniswelten

**Veranstaltungen mit Archiv (statisch)** (`moorl-tv-ticket-sale-static-listing`) ist ein zusätzlicher CMS-Baustein. Er zeigt alle aktiven Events unabhängig vom Ticket-Verkaufszeitraum, ohne Filter oder Seitennavigation: laufende/kommende Events nach Beginn aufsteigend, vergangene danach absteigend und ausgegraut. Für die Einordnung zählt `endAt`, ersatzweise `startAt`; genau zum Ende wechselt das Event ins Archiv. Flyer, Termin, Titel, Ort und Teaser werden aus dem Event geladen. Archiv-Einträge ohne alternative URL verlinken nicht auf die nicht mehr verfügbare Ticketdetailseite; zukünftige Events außerhalb des Verkaufszeitraums bekommen ebenfalls keinen internen Kauflink.

Am Event kann unter **Allgemein → Alternative Veranstaltungs-URL** beispielsweise die Adresse einer privaten Community hinterlegt werden. Titel und Aktionsbutton im statischen Listing verwenden dann diese Adresse. Externe Adressen öffnen mit `noopener noreferrer` in einem neuen Tab. Die Adresse ist optional; der normale Verkauf und das bisherige dynamische Listing behalten ihre Regeln. Vor Verwendung die nullable Spalte `alternative_url` bei bestehenden Tabellen gezielt per SQL erzeugen und Administration/Theme bauen.

Die Foundation-Erweiterte-Suche muss aktiviert sein. Ticket Vendor ergänzt dann einen Veranstaltungsbereich in der Schnellsuche und auf der Suchergebnisseite. Die Plugin-Konfiguration steuert Aktivierung, Trefferzahl und optional das Foundation-Layout getrennt für beide Ansichten und je Verkaufskanal. Es gelten dieselben Sichtbarkeits- und Verkaufszeitfilter wie auf den Veranstaltungsseiten; individuelle Kundentickets werden nicht durchsucht.

Das separate Foundation-Datenpaket `cms-page` installiert bei Aktivierung oder Update die geschützten Vorlagen **Ticket Vendor – Events** und **Ticket Vendor – Event detail**. Das eigene Datenpaket wird auch bei bereits installiertem Basisdatenpaket nachgeladen. Für Anpassungen die Vorlage in den Erlebniswelten duplizieren. Der Kategorie eine Erlebniswelt mit Veranstaltungslisting zuweisen und sie in der Plugin-Konfiguration unter `category` auswählen. Der Zurück-Link auf Veranstaltungsdetails führt zur SEO-URL dieser Kategorie und entfällt bei leerer Auswahl. `cmsPageId` bestimmt die Standard-CMS-Seite für Veranstaltungsdetails; eine direkt am Event hinterlegte CMS-Seite hat Vorrang. Ohne CMS-Auswahl wird die einfache Detaildarstellung verwendet.

Das CMS-Element `moorl-tv-ticket-sale-listing` bietet Veranstaltungslisten einschließlich Seitennavigation und lässt sich auch auf normalen CMS-Seiten verwenden. `moorl-tv-ticket-sale-detail` rendert auf Veranstaltungsdetailseiten die Veranstaltungsdaten und den Ticketkauf. Ältere ergänzende CMS-Inhalte ohne dieses Element werden weiterhin innerhalb der bisherigen Detaildarstellung eingebunden.

Nach Übernahme des Codes das Plugin aktualisieren und die Administration neu bauen, damit Datenpaket, Suchkonfiguration und CMS-Element im bestehenden Shop verfügbar sind.

## Bestellung und Kontingent

Die native Warenkorbposition heißt `moorl_tv_ticket`; `referencedId` ist die ID des Tickettyps. Der Collector liest Preis und Steuer neu ein. Der Processor verwirft vom Client gesetzte Preisdefinitionen, Flags und Payloads und prüft Verkaufszeiten sowie aggregierte Mindest-/Höchstmengen pro Tickettyp.

Im Warenkorb und in der Warenkorb-Seitenleiste stehen unter dem Tickettyp der übersetzte Veranstaltungsname und ein Auszug des Event-Teasers, ersatzweise der Event-Beschreibung. Der Auszug enthält höchstens 200 Zeichen ohne HTML. Beide Angaben werden bei der Neuberechnung aus den aktuellen Veranstaltungsdaten übernommen.

Der Warenkorb reserviert keine Plätze. Erst die gemeinsame Transaktion aus nativer Bestellspeicherung und Ticketerstellung belegt das Kontingent. Mengen gleicher Tickettypen werden über die Bestellpositionen aggregiert. Pro Bestellung, nativer Version, Tickettyp und internem Stückzähler entsteht genau ein Ticket mit direktem Bestellbezug. Wiederholungen verwenden bestehende Tickets. Verkaufsvoraussetzungen werden unmittelbar vor der Erstellung aus aktuellen gesperrten Daten gelesen.

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

Der Admin-Scanner bevorzugt Kamera-QR-Erkennung über `BarcodeDetector` und verwendet bei fehlender oder fehlerhafter nativer Erkennung den lokal eingebundenen jsQR-Fallback. Manuelle Token-Eingabe ist ebenfalls möglich. Kameraerkennung hängt von Browserunterstützung und einem sicheren Browserkontext ab; die manuelle Eingabe bleibt verfügbar. Bei einem Netzwerkfehler verwendet ein erneuter Versuch dieselbe Scan-Anfrage-ID.

`POST /api/_action/moorl-tv/check-in` erwartet `saleId`, `token`, `scanRequestId` und optional `deviceId` sowie `redemptionCategory`. Bereiche sind `admission`, `drinks`, `food`; fehlt das Feld, gilt Einlass. Unbekannte oder falsch typisierte Werte ergeben HTTP 400. Benötigt wird weiterhin `moorl_tv_ticket:scan`; der Controller führt nur die feste Scanneraktion im System-Scope aus. Die Antwort ergänzt `redemptionCategory`, `redemptionCount`, `maxRedemptions`, `remainingRedemptions`. Unbekannte oder veranstaltungsfremde Tickets liefern diese Felder und Teilnehmerdaten als null. `wrong_category` zeigt den tatsächlichen Bereich und verbraucht nichts.

Jeder bewusste Scan erhöht den Zähler unter der Sperrreihenfolge Bestellung → Veranstaltung → Typ → Ticket genau um eins. Das Ticket bleibt bis zur letzten Einlösung `valid`; diese setzt `redeemed` und `redeemedAt`. Prüfung, Änderung und Audit liegen in einer Transaktion. Die kurzlebige Context-Extension `moorlTvRedemptionWrite` autorisiert ausschließlich die Zähleränderung während des Scanner-DAL-Updates und wird in `finally` entfernt beziehungsweise wiederhergestellt. Allgemeine DAL-/Importzugriffe dürfen den Zähler nicht ändern. Typ-/Eventsnapshots werden vor der ersten Nutzung nur bei ausdrücklich zulässiger manueller Typkorrektur gemeinsam erneuert.

Die Anfrage-ID bindet Event, Token und Bereich. Identische Wiederholungen liefern die gespeicherte ursprüngliche Antwort mit damaligem Verbrauch; ein anderer Inhalt ergibt HTTP 409. Historische Fingerprints werden ausschließlich bei Einlass-Wiederholungen erkannt und als historische Einmalberechtigung rekonstruiert. Neue bewusste Scans benötigen eine neue ID. Kameraerkennung pausiert nach dem Ergebnis bis zum nächsten bewussten Scan. Bereichs-/Eventwechsel entwerten alte Kameracallbacks und setzen Ergebnis, Eingabe und offene Wiederholung zurück.

Das Foundation-Paket `scanner-role` erstellt die Rolle **Ticket Vendor – Scanner** mit genau `moorl_tv_ticket:scan` und `moorl_tv_ticket_sale:read`. Es erzeugt keine Benutzer oder Zugangsschlüssel und erhält bei erneutem Import bestehende Rollenanpassungen und Zuordnungen. Die Rolle erlaubt keine allgemeine Ticketabfrage/-änderung, PDFs, Versand, Widerruf, Kunden-/Bestellabfrage oder direkte Check-in-CRUD-Zugriffe. Native Standardrechte für authentifizierte Admin-Benutzer gelten zusätzlich. Zusätzliche Rollen und der Administrator-Schalter erweitern den Zugriff; eine Beschränkung auf einzelne Veranstaltungen gibt es nicht. Bisherige Scanner benötigen das neue Recht auch dann, wenn sie Ticket-Update-/Check-in-Create-Rechte haben.

Admin-PDFs erfordern `moorl_tv_ticket:read`, Senden/Widerrufen erfordern `moorl_tv_ticket:update`. Kundendownloads prüfen die direkte Kundenzuordnung oder den Bestellkunden, wenn keine direkte Zuordnung besteht. Eine Neuzuweisung an einen anderen Kunden sperrt den ursprünglichen Bestellkunden aus. Downloads sind privat und werden nicht zwischengespeichert.

## Installation und Worker

Bei regulärer Plugin-Aktivierung/Aktualisierung installiert der bestehende Foundation-Lifecycle-Helper die Datenpakete `data`, `ticket-number`, `ticket-mail`, `seo` und `scanner-role`. Wiederholung setzt Händlerkonfiguration, Vorlagen, Nummernkreisstand und Scanner-Rollenanpassungen nicht zurück. Bei bestehenden Entwicklungsinstallationen lassen sich diese Pakete auch über die Foundation-Datenverwaltung nachladen.

Das Schema umfasst sechzehn Tabellen. Der vollständig erneuerte native Migrationssatz legt sie mit direkten SQL-Statements an; MoorlDevTools-Migrationsfunktionen werden nicht verwendet. Die Migrationen sind eine Installationsbasis und bauen bestehende Tabellen nicht automatisch um. Die Dokumentation in `schema.md` beschreibt die Feldnamen und Bestandsübergänge.

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

## Artists, Programm und Gästeliste (19.10.2026)

Artists besitzen öffentliche Profile und optional ein Bookingangebot. bookingEnabled steuert ausschließlich die Website-Auswahl; der Kontakt führt zur konfigurierten Shop-Kontaktseite oder zum externen Bookingkontakt. Es gibt keinen Bookingprozess. Gage, Währung und interne Bookingnotiz gelangen nicht in die öffentliche Ausgabe.

Stages werden am Event angelegt; Auftritte können vorab ohne Stage oder Uhrzeit gepflegt werden. Mehrere Sets desselben Artists bleiben getrennt. Line-up und Timetable werden am Event unabhängig freigegeben. Das gemeinsame Line-up führt jeden Artist einmal auf und hebt sein Kollektiv, ersatzweise das Label, in der Primärfarbe hervor. Jede Stage erhält eine eigene Timetable mit festen Spalten für Zeit, Artist und Genre; Auftritte ohne Stage stehen separat unter „Ohne Stage“. Kollektiv und Label stehen ausschließlich im Line-up. Beginn und Ende enthalten jeweils Datum und Uhrzeit und bleiben unabhängig optional. Die Eingabe und Ausgabe erfolgen in der Event-Zeitzone; gespeichert wird UTC. Die öffentliche Timetable zeigt nur Uhrzeiten; das Datum dient intern der Sortierung. Die Timetable sortiert nach Beginn; Auftritte ohne Beginn stehen zuletzt. Ein separates Auftrittsdatum entfällt. Der native Datum-/Uhrzeit-Picker verwendet die Event-Zeitzone und gibt UTC-Werte weiter. Es gibt keine zusätzliche Reihenfolge- oder Überschneidungsprüfung. listed=false blendet aus Listen/Suche/Sitemap aus, schützt aber nicht den direkten Eventaufruf.

Für die Gästeliste am kostenlosen internen Tickettyp die Registrierung aktivieren und Ehrenämter pflegen. Einleitung und Regeln stehen weiterhin am Event. Der Typ zeigt den geheimen Link und seine Anmeldungen in einer normalen Foundation-Tabelle. Bei mehreren Storefront-Domains die gewünschte Linkadresse auswählen; es wird kein Registrierungs-Verkaufskanal gespeichert. Der tatsächliche Formularaufruf wird als Ursprung an der Anmeldung gespeichert. Neu ausgestellte Tickets übernehmen Verkaufskanal und Sprache aus der Anmeldung. Bei manuellen Einträgen und CSV-Import muss der Verkaufskanal zugeordnet werden; eine fehlende Sprache erhält die Systemsprache. Telefonnummern sind immer optional; separate Registrierungszeitfenster entfallen.

Anmeldung bedeutet noch keine Reservierung. Sobald das Typkontingent oder die Eventkapazität ausgeschöpft ist, nimmt das Formular keine neuen Anmeldungen an. Bei wieder freien Plätzen öffnet es automatisch, solange die Registrierung freigegeben und das Event aktiv/nicht beendet ist. Bereits erfolgreiche Anfragen bleiben bei Wiederholung bestätigt. Nach Prüfung erzeugt „Ticket erstellen und senden“ ein normales Ticket und belegt Typ-/Eventkontingent. Wiederholungen erzeugen kein zweites Ticket; Mailfehler werden am Ticket behandelt. Nach manuellem Abschalten dürfen vorhandene Anmeldungen weiterhin bearbeitet werden. Für eingeschränkte Rollen sind `moorl_tv_guestlist_entry:issue` und `moorl_tv_ticket_type:guestlist_link` mit den nötigen Leserechten zuzuweisen. Alte Eventlinks werden nach der Datenübernahme weitergeleitet; bereits geöffnete alte Formulare neu laden. Schema- und Übernahmeschritte stehen in `schema.md`.

Neue kundenlose Tickets verwenden ihren gespeicherten Kanal und ihre Sprache für Zugang, Domain und Versand. Mailbezeichnungen und PDF werden in diesem Kontext neu geladen. Die optionale Gesamtkapazität eines Events gilt über alle Tickettypen einschließlich manueller und Gästetickets.

Prüfstand vom 21.10.2026: sechzehn Tabellen durch die neuen direkten SQL-Migrationen in isolierter Datenbank erzeugt; 285 PHP-Tests mit 2616 Assertions sowie 77 Administrationstests bestanden. Der PHP-Lauf meldet sieben Deprecations zu dynamischen Eigenschaften in der vorhandenen Core-/Foundation-Listingsuche. Die Prüfungen umfassen den Abgleich aller persistenten DAL-Spalten mit dem SQL-Schema, Fremdschlüssel und Löschregeln, wiederholte Initialmigrationen, Übersetzungen, native Adminbeziehungen, öffentliche Formularvalidierung und einen veralteten Transaktions-Snapshot. Es wurden keine normalen Shopdaten migriert und keine echten Mails verschickt.

## Datenbankprüfung und Lastverhalten

Der [lesende Schema-/Bestandsabgleich und die gezielte Ergänzung der Jobindizes](schema.md#lesender-schema--und-bestandsabgleich) sind getrennte Betriebsschritte. Die 16 Initialmigrationen ändern weiterhin keine vorhandenen Tabellen.

Scans, Teilnehmeränderungen und Versandtracking verändern normalerweise keine Belegung. Diese Updates behalten die bisherigen Sperren und Einzelprüfungen, überspringen jedoch die vollständigen Typ-/Eventzählungen und das erneute Schreiben unveränderter Verkaufszähler. Bei echter Belegungsänderung und Kontingentabsenkung bleibt die vollständige Prüfung erhalten.

Eine isolierte lokale Messung unter MySQL 8.0.46 mit 10.000 belegenden Tickets ergab bei zehn Scans rund 52 ms vor und 13 ms nach der Änderung im Median; vollständige Bestandszählungen je Scan sanken von drei auf null. Sieben parallele Prozesse für vier Scanner, Ticketausstellung, manuellen Ablauf und Versandbuchhaltung hielten die Bestands-/Einlöseregeln bei 1.000 und 10.000 Tickets ein. Gemeinsame Event-/Typsperren bleiben bestehen. Diese Messung ist keine Zusage für eine bestimmte Scannerzahl und umfasst keinen Browser-Checkout, Payment-Provider oder SMTP-Versand.

Die reproduzierbaren Messskripte liegen im Entwicklungscheckout unter `tests/performance/lifecycle-queries.php` und `tests/performance/inventory-writes.php`. Sie akzeptieren nur ausdrücklich ausgewählte `moorl_tv_*_test`-Datenbanken. Die Inventarmessung verlangt leere Ticketbestände; niemals gegen den laufenden Shop ausführen. Indexmessungen verwenden eine temporäre Tabellenkopie. Messberichte gehören außerhalb der Pluginverzeichnisse unter `var/testing/`.
