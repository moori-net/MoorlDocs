# Ticket Vendor: Datenmodell und Schemaübergang

Stand: 19.10.2026. Quelle sind die installierten DAL-Definitionen und Foundation-Flags. Das externe Schemawerkzeug erzeugt/gleicht Tabellen ab. Keine zusätzlichen PHP-Migrationen, keine automatische Produktivdatenübernahme.

## Zwölf Tabellen

| Tabelle | Aufgabe |
|---|---|
| moorl_tv_ticket_sale | Event mit Foundation-Inhalten, Adresse, Zeiten, Zeitzone, Kapazität und Veröffentlichung/Gästelistenkonfiguration |
| moorl_tv_ticket_sale_translation | Übersetzte Inhalte, Meta-/Ortsdaten, schemaOrg, guestlistIntroduction und guestlistRules |
| moorl_tv_ticket_type | Eventkategorie mit Preis/Steuer, Kontingent und Kaufgrenzen |
| moorl_tv_ticket_type_translation | Übersetzte Typtexte |
| moorl_tv_ticket | Einzelnes Ticket mit optionaler direkter Bestellung, Kunde/Empfänger, Personalisierung, Status und Versandtracking |
| moorl_tv_ticket_checkin | Unveränderter Scan-Audit einschließlich abgewiesener Versuche und Anfrage-ID |
| moorl_tv_artist | Profil, Medien/Logo, Social Links, Kollektiv/Label, Bookingangebot und interne Angaben |
| moorl_tv_artist_translation | Foundation-Basistexte, Name/Beschreibung/Teaser mit Fallback |
| moorl_tv_stage | Eventbezogene Bühne/Area, Bild und Reihenfolge |
| moorl_tv_stage_translation | Name und Beschreibung |
| moorl_tv_performance | Artist-Auftritt am Event mit optionaler Stage und Uhrzeiten als Text |
| moorl_tv_guestlist_entry | Persönliche Anfrage, Regel-Snapshot, Entscheidung und optionales Ticket |

UUIDs sind BINARY(16), vollständige Zeitpunkte UTC und Event-Zeitzonen IANA-Namen. Timetable-Uhrzeiten sind einfache lokale HH:mm-Texte ohne Datum oder Umrechnung. FK-Storage-Namen folgen Foundation: saleId = moorl_tv_ticket_sale_id, typeId = moorl_tv_ticket_type_id, artistId = moorl_tv_artist_id, stageId = moorl_tv_stage_id. Native Core-Bezüge verwenden ihre Core-Spaltennamen.

## Ticket und Bestellung

orderId/order_id ist nullable. orderVersionId/order_version_id ist nativ erforderlich mit Live-Default, auch ohne Bestellung. Association order ersetzt orderLineItem. Die aktuelle Definition enthält keine order_line_item_id oder order_line_item_version_id mehr.

unitIndex ist eine technische Einheit innerhalb Bestellung/Version/Tickettyp. Der Unique-Key umfasst order_id, order_version_id, moorl_tv_ticket_type_id und unit_index; MoorlDevTools bestimmt die physische Indexspaltenreihenfolge. Mengen gleicher Typen aus mehreren Positionen werden aggregiert. Wiederholungen berücksichtigen alle historischen Ticketzustände. Ein bestellgebundenes Ticket wird nicht hart gelöscht; Herkunft/Einheit bleiben unveränderlich.

saleId und typeId sind erforderlich und müssen zusammenpassen. customerId, recipientEmail, attendeeName (511), attendeePhone (64) bleiben eigenständige Angaben. Kundenlose Tickets können salesChannelId und languageId speichern; neue Gästetickets übernehmen den Anmeldekontext. Bestelltickets verwenden den Bestellkontext, alte Kundentickets ihre Fallbacks. Explizite Empfängeradresse hat Vorrang vor Kunde und Bestellkunde.

Ticketnummer aus NumberRange, QR-token und persönlicher deeplink bleiben getrennt. Token, Deeplink und Versandfehler erscheinen nicht in allgemeinen API-Ausgaben. Ticketzustände: pending, valid, expired, redeemed, revoked. Versandzustände: pending, sent, failed. Pending/valid/redeemed belegen Plätze; expired/revoked geben sie frei. quantitySold ist abgeleitet und schreibgeschützt. expiresAt ist die Zahlungsfrist, issuedAt der fachliche Ausstellungszeitpunkt.

## Neue Eventfelder

listed (Default true), lineupPublished/timetablePublished (Default false), capacity nullable. Timetable setzt Line-up-Freigabe voraus. listed ist nur Auffindbarkeit, kein Geheimhaltungsschutz. capacity gilt zusätzlich zu Typkontingenten für alle belegenden Tickets.

Gästeliste: guestlistEnabled (false), guestlistOpenAt/guestlistCloseAt, guestlistTicketTypeId (Storage guestlist_moorl_tv_ticket_type_id), guestlistSalesChannelId (guestlist_sales_channel_id), guestlistAccessKey (nullable VARCHAR(40), intern), guestlistConfig (JSON). Konfiguration enthält phoneRequired und volunteerRoles (technischer Schlüssel → Beschriftung oder Sprachmap). Der gewählte Typ muss kostenlos sein und zum Event gehören; für den Verkauf darf er inaktiv sein.

guestlistTicketTypeId erhält einen physischen FK zu moorl_tv_ticket_type.id mit ON DELETE SET NULL. Damit bleibt der optionale Bezug auch bei direkten SQL-Löschungen gültig. Der DAL-Konfigurationsschutz für verwendete Gästetickettypen bleibt zusätzlich bestehen. Die gegenseitigen Event-/Typbezüge sind bei der Installationsreihenfolge zu berücksichtigen; der Generator trennt die Fremdschlüssel nicht mehr pauschal in weitere Dateien ab.

## Artist, Stage und Auftritt

Artist hat bookingEnabled (false), bookingContact (E-Mail/HTTP(S)), priority (höher zuerst), media/Logo, Social-Link-Liste, genre und Kollektiv/Label. genre ist ein optionales, nicht übersetztes StringField (moorl_tv_artist.genre, nullable VARCHAR(255)), wird in Administration und öffentlichen Artistkarten angezeigt und ist im Import-/Exportprofil enthalten. Die Spalte wird über das externe Schemawerkzeug ergänzt. feeAmount ist optional und nichtnegativ in kleinster Geldeinheit ohne Währungsrelation; bookingNote ist intern. Artist.currencyId/currency und die Spalte currency_id entfallen. Keine zusätzliche Artist-/Stage-/Auftrittsaktivierung.

Stage und Performance haben saleId, position (aufsteigend), CustomFields und Zeitstempel. Performance hat erforderlichen Artist, optionale Stage und unabhängig optionale startAt/endAt als StringField: start_at/end_at sind nullable VARCHAR(5) für HH:mm. Der Core-Picker mt-datepicker mit dateType=time liefert die Uhrzeit als Text. Es gibt keine zusätzliche Datums-, Reihenfolge-, Sommerzeit- oder Überschneidungsprüfung; beispielsweise 23:30–01:00 ist erlaubt. Die Timetable folgt position, bei gleicher Position dem Beginn (fehlender Beginn zuletzt). Stage muss demselben Event angehören; belegte Stages werden nicht auf andere Events verschoben. Mehrere Sets desselben Artists sind erlaubt. Die öffentliche Ausgabe ist eine explizite Projektion ohne interne Angaben.

Bestehende DATETIME-Spalten start_at/end_at ausschließlich an moorl_tv_performance über das externe Schemawerkzeug auf VARCHAR(5) umstellen. Vorhandene Werte vorher aus UTC in die jeweilige Event-Zeitzone umrechnen und als HH:mm übernehmen; nicht durch direktes Kürzen des DATETIME-Texts. Event-, Ticket- und Gästelistenfristen bleiben vollständige Zeitpunkte. Keine PHP-Migration oder automatische Produktivschemaänderung.

## Gästelistenintegrität und Rechte

Unique-Keys auf submission_id und nullable moorl_tv_ticket_id. Keine Eindeutigkeit auf E-Mail. Gleiche Anfrage-ID erzeugt keinen zweiten Eintrag; mehrere Gäste dürfen dieselbe Adresse verwenden. Entscheidung ist NULL, rejected oder cancelled; Ausstellungsstatus folgt ticketId. Versand- und Ticketstatus werden nicht dupliziert.

Anmeldung speichert Name, E-Mail, optional Telefon/Einladenden/Ehrenämter/Bemerkung, separate interne Notiz, Ursprungsprache/-kanal und bestätigten Regeltext. Eingabegrenzen und Auswahlwerte werden serverseitig validiert. Ursprung und Regeltext sind unveränderlich; nach Ausstellung ist auch die Teilnehmeranmeldung eingefroren.

Dedizierte Adminrechte issue/decide/guestlist_link schützen die begrenzten Aktionen. Scannerrechte bleiben unverändert. Ticketverknüpfung und Entscheidung sind keine frei beschreibbaren CRUD-Felder. Interne Artist-/Eventdaten bleiben generisch gefiltert; der Admin-JSONAPI-Adapter stellt nur vom Core autorisierte Attribute und Beziehungen wieder her. Geheimschlüssel wird ausschließlich durch die dedizierte Aktion herausgegeben.

Der Bearbeiter einer Entscheidung wird über userId/user mit UserDefinition referenziert (nullable user_id, ON DELETE SET NULL). Nur die dedizierten Entscheidungsaktionen schreiben diese Zuordnung. Beim Löschen eines Benutzers bleiben Anmeldung, Entscheidung und processedAt erhalten. Der bisherige Name processedById/processed_by_id entfällt; vorhandene Bearbeiter-IDs bei einer Umstellung vor dem Entfernen der alten Spalte nach user_id übernehmen. Das externe Schemawerkzeug erzeugt die Änderungen.

Restriktive inverse Relationen schützen Events, Typen, Artists, Stages, Tickets und relevante Core-Referenzen. Übersetzungen folgen ihren Eltern. Tickets/Check-ins/ausgestellte Anmeldungen werden nicht implizit kaskadierend gelöscht.

Die TaxExtension schützt Steuern, die von Tickettypen verwendet werden, bereits im DAL. Der generierte FK moorl_tv_ticket_type.tax_id verwendet RESTRICT statt CASCADE; auch unverkaufte Typen werden beim Löschen einer Steuer nicht entfernt. Die inverse Steuerrelation wird nicht als zusätzliche öffentliche API-Association angeboten.

## Bestehende Bestellpositionsdaten übernehmen

Diesen Ablauf zuerst mit einer Kopie der Datenbank prüfen. Während der eigentlichen Umstellung Checkout, Ticketänderungen und Worker anhalten, damit alter und neuer Aussteller nicht gleichzeitig arbeiten.

1. Mit dem externen Schemawerkzeug nur neue Tabellen/Spalten ergänzen, bestehende Positionsspalten und deren Daten behalten. Am Ticket neue nullable order_id sowie native order_version_id ergänzen. Den neuen Gruppierungsindex erst nach Übernahme aktivieren oder sicherstellen, dass die neuen Bestell-IDs zunächst NULL sind.
2. Vorschau aus dem Shopware-Projekt ausführen:

       bin/console moorl-tv:backfill-ticket-orders

3. Der Befehl prüft erforderliche Spalten, erkennt fehlende Bestellpositionsreferenzen und widersprüchliche bereits vorhandene direkte Zuordnungen. Ohne --apply werden keine Daten oder Schemata geändert.
4. Den bisherigen Unique-Key über Positions-ID/Versions-ID/unit_index mit dem externen Werkzeug entfernen, seinen FK zunächst behalten. Sonst können verschobene Stückzähler mit noch vorhandenen alten Werten kollidieren.
5. Explizit anwenden:

       bin/console moorl-tv:backfill-ticket-orders --apply

6. Der Befehl überträgt in einer Transaktion Bestell-ID/Version und vergibt pro Bestellungsversion/Tickettyp neue stabile Einheiten. Sortierung ist alte Positions-ID, alter Stückzähler und Ticket-ID. Ticket-ID, Nummer, Token, Empfänger und Status werden nicht ersetzt. Manuelle Tickets ohne alte Positionszuordnung bleiben unverändert.
7. Vollständigkeit, historische Zustände, direkte Bestellbezüge und neue Eindeutigkeit prüfen. Anschließend neue FKs/Unique-Indizes aktivieren und erst dann alte Positions-FKs/-Spalten entfernen. Quelle ist nun die OrderExtension statt OrderLineItemExtension.
8. Cache/Assets aktualisieren und Worker neu starten. Vorhandene Ticket-URLs und QR-Codes bleiben erhalten.

Der Befehl führt keinerlei DDL aus und wird nie automatisch durch Aktivierung/Update aufgerufen. Ein generierter Schemaabgleich allein ersetzt diese Datenübernahme nicht. In dieser Sitzung wurde nur gegen eine isolierte Testdatenbank gearbeitet, keine bestehende Shopdatenbank umgebaut.

## Schema-Prüfungen

tests/create-schema.php akzeptiert ausschließlich eine explizite moorl_tv_*_test-Datenbank und verweigert das Ersetzen nichtleerer Plugin-Tabellen. Es verwendet den tatsächlichen MoorlDevTools-Builder. Wegen Event/Typ-FK-Zyklen werden zuerst alle Tabellen, danach die Fremdschlüssel erzeugt. Unique-Flags kommen aus den Definitionen. Nicht eindeutige zusätzliche Suchindizes sind bei Bedarf über das externe Tool anzulegen, insbesondere (Event, E-Mail) und (Event, Entscheidung, erstellt).

MoorlDevTools erzeugt CREATE-/ALTER-Anweisungen und Fremdschlüssel wieder zusammen pro Entity in einer Migrationsdatei. Die globale Verschiebung aller ADD-FOREIGN-KEY-Operationen und die dadurch entstandenen zusätzlichen Dateien wurden zurückgenommen. Der Builder lässt Referenzen nicht wegen einer zusätzlichen One-to-many-Beziehung zu derselben Entity aus und wertet inverse Löschregeln anhand der konkreten FK-Spalte aus. Bisherige noch nicht ausgelieferte generierte Migrationen mit fehlendem Gästelisten-FK beziehungsweise CASCADE an tax_id neu erzeugen; bei installierten Schemata den regulären Abgleich über das externe Werkzeug verwenden. Das Plugin ergänzt keine handgeschriebenen PHP-Migrationen und führt diese Umstellung nicht automatisch durch.

    docker exec -e MOORL_TV_TEST_DATABASE_NAME=moorl_tv_extension_20261019_test -w /var/www/html shopware_6.7.14.1 php custom/plugins/MoorlTicketVendor/tests/create-schema.php
    docker exec -e MOORL_TV_TEST_DATABASE_NAME=moorl_tv_extension_20261019_test -w /var/www/html shopware_6.7.14.1 php vendor/bin/phpunit -c custom/plugins/MoorlTicketVendor/phpunit.xml.dist

Der Testname ist eine Entwicklungsreferenz; niemals eine reguläre Shopdatenbank als Testdatenbank verwenden. Native Mailtransporte werden in Versandtests ersetzt. Weitere Laufzeitdetails stehen in runtime.md.
