# Ticket Vendor: Datenmodell und Schemaübergang

Stand: 20.10.2026. Quelle sind die installierten DAL-Definitionen und Foundation-Flags. Das externe Schemawerkzeug erzeugt/gleicht Tabellen ab. Keine zusätzlichen PHP-Migrationen, keine automatische Produktivdatenübernahme.

## Zwölf Tabellen

| Tabelle | Aufgabe |
|---|---|
| moorl_tv_ticket_sale | Event mit Foundation-Inhalten, Adresse, Zeiten, Zeitzone, Kapazität und Veröffentlichung |
| moorl_tv_ticket_sale_translation | Übersetzte Inhalte, Meta-/Ortsdaten, schemaOrg, guestlistIntroduction und guestlistRules |
| moorl_tv_ticket_type | Eventkategorie mit Preis/Steuer, Kontingent, Kaufgrenzen und Gästelistenkonfiguration |
| moorl_tv_ticket_type_translation | Übersetzte Typtexte |
| moorl_tv_ticket | Einzelnes Ticket mit optionaler direkter Bestellung, Kunde/Empfänger, Personalisierung, Status und Versandtracking |
| moorl_tv_ticket_checkin | Unveränderter Scan-Audit einschließlich abgewiesener Versuche und Anfrage-ID |
| moorl_tv_artist | Profil, Medien/Logo, Social Links, Kollektiv/Label, Bookingangebot und interne Angaben |
| moorl_tv_artist_translation | Foundation-Basistexte, Name/Beschreibung/Teaser mit Fallback |
| moorl_tv_stage | Eventbezogene Bühne/Area, Bild und Reihenfolge |
| moorl_tv_stage_translation | Name und Beschreibung |
| moorl_tv_performance | Artist-Auftritt am Event mit optionaler Stage und Uhrzeiten als Text |
| moorl_tv_guestlist_entry | Persönliche Anfrage an einen Tickettyp, Regel-Snapshot, Entscheidung und optionales Ticket |

UUIDs sind BINARY(16), vollständige Zeitpunkte UTC und Event-Zeitzonen IANA-Namen. Timetable-Uhrzeiten sind einfache lokale HH:mm-Texte ohne Datum oder Umrechnung. FK-Storage-Namen folgen Foundation: saleId = moorl_tv_ticket_sale_id, typeId = moorl_tv_ticket_type_id, artistId = moorl_tv_artist_id, stageId = moorl_tv_stage_id. Native Core-Bezüge verwenden ihre Core-Spaltennamen.

Tickettypen verwenden ihre UUID und den übersetzten Namen; `technicalName`/`technical_name` entfällt aus Modell, Administration, Demo und Import-/Exportmapping. Die bisherige erforderliche Spalte `moorl_tv_ticket_type.technical_name` vor Verwendung der geänderten Definition mit dem externen Schemawerkzeug entfernen und generierte Migrationen entsprechend abgleichen. Vorhandene Import-/Exportprofile ebenfalls aktualisieren. Keine zusätzliche PHP-Migration oder automatische Änderung bestehender Datenbanken.

## Ticket und Bestellung

orderId/order_id ist nullable. orderVersionId/order_version_id ist nativ erforderlich mit Live-Default, auch ohne Bestellung. Association order ersetzt orderLineItem. Die aktuelle Definition enthält keine order_line_item_id oder order_line_item_version_id mehr.

unitIndex ist eine technische Einheit innerhalb Bestellung/Version/Tickettyp. Der Unique-Key umfasst order_id, order_version_id, moorl_tv_ticket_type_id und unit_index; MoorlDevTools bestimmt die physische Indexspaltenreihenfolge. Mengen gleicher Typen aus mehreren Positionen werden aggregiert. Wiederholungen berücksichtigen alle historischen Ticketzustände. Ein bestellgebundenes Ticket wird nicht hart gelöscht; Herkunft/Einheit bleiben unveränderlich.

saleId und typeId sind erforderlich und müssen zusammenpassen. customerId, recipientEmail, attendeeName (511), attendeePhone (64) bleiben eigenständige Angaben. Kundenlose Tickets können salesChannelId und languageId speichern; neue Gästetickets übernehmen den Anmeldekontext. Bestelltickets verwenden den Bestellkontext, alte Kundentickets ihre Fallbacks. Explizite Empfängeradresse hat Vorrang vor Kunde und Bestellkunde.

Ticketnummer aus NumberRange, QR-token und persönlicher deeplink bleiben getrennt. Token, Deeplink und Versandfehler erscheinen nicht in allgemeinen API-Ausgaben. Ticketzustände: pending, valid, expired, redeemed, revoked. Versandzustände: pending, sent, failed. Pending/valid/redeemed belegen Plätze; expired/revoked geben sie frei. quantitySold ist abgeleitet und schreibgeschützt. expiresAt ist die Zahlungsfrist, issuedAt der fachliche Ausstellungszeitpunkt.

## Neue Eventfelder

listed (Default true), lineupPublished/timetablePublished (Default false), capacity nullable. Timetable setzt Line-up-Freigabe voraus. listed ist nur Auffindbarkeit, kein Geheimhaltungsschutz. capacity gilt zusätzlich zu Typkontingenten für alle belegenden Tickets.

Einleitung (`guestlistIntroduction`) und Regeln (`guestlistRules`) bleiben übersetzbare Eventtexte. Am Tickettyp liegen `guestlistEnabled` (Default false), `guestlistAccessKey` (nullable VARCHAR(40), intern) und `guestlistConfig` (JSON, ausschließlich `volunteerRoles`: technischer Schlüssel → Beschriftung oder Sprachmap). `guestlistTicketTypeId`, Registrierungszeitfenster, konfigurierter Registrierungs-Verkaufskanal und `phoneRequired` entfallen. Telefonnummern bleiben optional. Ein freigegebener Gästelistentyp muss kostenlos sein, darf für den öffentlichen Verkauf aber `active=false` haben.

Die Anmeldung besitzt required, unveränderlichen `typeId` (`moorl_tv_ticket_type_id`, FK RESTRICT); ihr Event ergibt sich über `type.sale`. Der bisherige direkte Event-FK der Anmeldung entfällt. Typen mit Anmeldungen lassen sich weder löschen noch auf andere Events verschieben. Auch kundenlose verknüpfte Tickets behalten ihren Typ/Event. Die zyklische Event-/Typreferenz entfällt vollständig.

## Artist, Stage und Auftritt

Artist hat bookingEnabled (false), bookingContact (E-Mail/HTTP(S)), priority (höher zuerst), media/Logo, Social-Link-Liste, genre und Kollektiv/Label. genre ist ein optionales, nicht übersetztes StringField (moorl_tv_artist.genre, nullable VARCHAR(255)), wird in Administration und öffentlichen Artistkarten angezeigt und ist im Import-/Exportprofil enthalten. Die Spalte wird über das externe Schemawerkzeug ergänzt. feeAmount ist optional und nichtnegativ in kleinster Geldeinheit ohne Währungsrelation; bookingNote ist intern. Artist.currencyId/currency und die Spalte currency_id entfallen. Keine zusätzliche Artist-/Stage-/Auftrittsaktivierung.

Stage und Performance haben saleId, position (aufsteigend), CustomFields und Zeitstempel. Performance hat erforderlichen Artist, optionale Stage und unabhängig optionale startAt/endAt als StringField: start_at/end_at sind nullable VARCHAR(5) für HH:mm. Der Core-Picker mt-datepicker mit dateType=time liefert die Uhrzeit als Text. Es gibt keine zusätzliche Datums-, Reihenfolge-, Sommerzeit- oder Überschneidungsprüfung; beispielsweise 23:30–01:00 ist erlaubt. Die Timetable folgt position, bei gleicher Position dem Beginn (fehlender Beginn zuletzt). Stage muss demselben Event angehören; belegte Stages werden nicht auf andere Events verschoben. Mehrere Sets desselben Artists sind erlaubt. Die öffentliche Ausgabe ist eine explizite Projektion ohne interne Angaben.

Bestehende DATETIME-Spalten start_at/end_at ausschließlich an moorl_tv_performance über das externe Schemawerkzeug auf VARCHAR(5) umstellen. Vorhandene Werte vorher aus UTC in die jeweilige Event-Zeitzone umrechnen und als HH:mm übernehmen; nicht durch direktes Kürzen des DATETIME-Texts. Event-, Ticket- und Gästelistenfristen bleiben vollständige Zeitpunkte. Keine PHP-Migration oder automatische Produktivschemaänderung.

## Gästelistenintegrität und Rechte

Unique-Keys auf submission_id und nullable moorl_tv_ticket_id. Keine Eindeutigkeit auf E-Mail. Gleiche Anfrage-ID erzeugt keinen zweiten Eintrag; eine Wiederholung an einem anderen Typ ist ein Konflikt. Mehrere Gäste dürfen dieselbe Adresse verwenden. Entscheidung ist NULL, rejected oder cancelled; Ausstellungsstatus folgt ticketId. Versand- und Ticketstatus werden nicht dupliziert.

CSV-Importe benötigen weder `id` noch `submissionId`: Shopware erzeugt die Datensatz-ID; fehlende, NULL- oder leere Anfrage-IDs werden pro neuer Anmeldung vor der DAL-Pflichtfeldprüfung als zufällige UUID mit 32 Hexzeichen erzeugt. Mitgelieferte Anfrage-IDs und bestehende Werte bei Updates bleiben erhalten. Kein zufälliger Datenbank-Default und keine Schemaänderung. Ohne mitgelieferte Datensatz-ID legt ein erneuter Import neue Anmeldungen an; gleiche E-Mail-Adressen werden nicht zusammengeführt.

CSV-Importe benötigen weder `id` noch `submissionId`: Shopware erzeugt die Datensatz-ID; fehlende, NULL- oder leere Anfrage-IDs werden pro neuer Anmeldung vor der DAL-Pflichtfeldprüfung als zufällige UUID mit 32 Hexzeichen erzeugt. Mitgelieferte Anfrage-IDs und bestehende Werte bei Updates bleiben erhalten. Kein zufälliger Datenbank-Default und keine Schemaänderung. Ohne mitgelieferte Datensatz-ID legt ein erneuter Import neue Anmeldungen an; gleiche E-Mail-Adressen werden nicht zusammengeführt.

Für größere Gästelisten über das externe Schemawerkzeug zusätzlich die Suchindizes `(moorl_tv_ticket_type_id, decision, created_at)` für gefilterte Listen und `(moorl_tv_ticket_type_id, email)` für die E-Mail-Suche vorsehen. Der generierte Typ-FK-Index allein begrenzt bereits auf den Typ; EXPLAIN auf dem isolierten Endschema zeigt für Listen jedoch zusätzliches Sortieren und für die Duplikatübersicht eine temporäre Gruppierung nach Name/E-Mail. Die zusätzlichen Indizes mit repräsentativen Daten und den tatsächlich verwendeten Filtern prüfen; sie beseitigen nicht automatisch jede Gruppierung oder Sortierung.

Anmeldung speichert Name, E-Mail, optional Telefon/Einladenden/Ehrenämter/Bemerkung, separate interne Notiz, Ursprungsprache/-kanal und bestätigten Regeltext. Eingabegrenzen und Auswahlwerte werden serverseitig validiert. Ursprung und Regeltext sind unveränderlich; nach Ausstellung ist auch die Teilnehmeranmeldung eingefroren.

Dedizierte Adminrechte `moorl_tv_guestlist_entry:issue`, `moorl_tv_guestlist_entry:decide` und `moorl_tv_ticket_type:guestlist_link` schützen die begrenzten Aktionen. Scannerrechte bleiben unverändert. Ticketverknüpfung und Entscheidung sind keine frei beschreibbaren CRUD-Felder. Interne Artist-/Event-/Typdaten bleiben generisch gefiltert; der Admin-JSONAPI-Adapter stellt nur vom Core autorisierte Attribute und Beziehungen wieder her. Geheimschlüssel wird ausschließlich durch die dedizierte Aktion herausgegeben.

Registrierungen reservieren keine Plätze. Formulare schließen bei erschöpftem Typkontingent oder voller Eventkapazität und öffnen bei wieder freien Plätzen automatisch, solange der Schalter gesetzt und das Event aktiv/nicht beendet ist. Bestehende Anfragen dürfen bei abgeschalteter Registrierung weiterhin nach den normalen Regeln bearbeitet werden. Typ- und Eventkontingent zählen `pending`, `valid`, `redeemed`; der Schalter wird durch Vollbelegung nicht umgeschrieben. Wiederholungen bereits erfolgreicher Anmeldungen werden auch bei Vollbelegung bestätigt.

Kanal und Sprache des tatsächlichen Storefrontaufrufs bleiben unveränderlich an der Anmeldung gespeichert. Beim Erstellen eines Gästelisten-Tickets haben die globalen SystemConfig-Werte `MoorlTicketVendor.config.guestlistTicketSalesChannelId` und `MoorlTicketVendor.config.guestlistTicketLanguageId` Vorrang, auch bei CSV-Anmeldungen ohne Ursprung. Beide Werte werden als Paar geprüft (aktive Storefront mit Domain, zugeordnete Sprache; eine eigene Sprachdomain ist nicht erforderlich) und am Ticket festgeschrieben. Sind beide leer, wird der vorhandene Anmeldungsursprung verwendet. Unvollständige Konfigurationen und fehlende Ursprünge werden nicht geraten. Ein Konfigurationswechsel verändert bestehende Tickets nicht. Kein zusätzliches Plugin-Datenbankfeld und keine PHP-Migration. Die Adminaktion erzeugt Domainlinks unter `/guestlist/type/{typeId}/{accessKey}`. Mehrere Storefront-Domains werden nur für den zu kopierenden Link ausgewählt; diese Auswahl wird nicht am Typ gespeichert.

## Bestehende Event-Gästelisten übernehmen

Zuerst an einer Datenbankkopie prüfen. Mit dem externen Schemawerkzeug additiv die drei Typfelder und eine zunächst nullable `moorl_tv_guestlist_entry.moorl_tv_ticket_type_id` ergänzen. Die bisherigen Eventfelder und der alte Event-FK der Anmeldung müssen für die Übernahme erhalten bleiben. Registrierungen, Checkout, Ticketänderungen und Worker während der tatsächlichen Übernahme anhalten.

    bin/console moorl-tv:backfill-guestlist-types

Die Vorschau schreibt nichts. Ausgestellte Einträge erhalten ihren tatsächlichen Tickettyp, übrige Einträge den bisherigen `event.guestlistTicketTypeId`. Eventkonfiguration, Geheimschlüssel und Ehrenämter werden übernommen; `phoneRequired` entfällt. Fehlende oder widersprüchliche Zuordnungen, fehlende Ursprünge und abweichende bereits gepflegte Typkonfigurationen werden als Konflikte ausschließlich mit Datensatz-IDs gemeldet. Es werden keine Ersatztypen oder Verkaufskanäle geraten.

    bin/console moorl-tv:backfill-guestlist-types --apply

Nur dieses Flag schreibt Daten; bei Konflikten wird nichts übernommen. Wiederholung ist stabil und erhält Entscheidungen, Ticket-IDs, Regeltexte und Versandursprünge. Der Befehl führt kein DDL aus und wird nie automatisch vom Plugin-Lifecycle gestartet. Nach vollständiger Prüfung `entry.typeId` required machen und FK RESTRICT aktivieren; erst danach alten Anmeldungs-Event-FK und obsolete Eventkonfiguration über das externe Werkzeug entfernen. `guestlistIntroduction` und `guestlistRules` bleiben bestehen. Eigene Exportprofile auf `typeId` umstellen.

In bestehenden ACL-Rollen das bisherige `moorl_tv_ticket_sale:guestlist_link` gezielt durch `moorl_tv_ticket_type:guestlist_link` ersetzen und `moorl_tv_ticket_type:read` ergänzen; andere Rechte/Zuweisungen erhalten. Aktuelle Administration bauen, Cache und Worker aktualisieren. Alte gültige Eventlinks leiten auf den passenden Typ weiter; bereits geöffnete alte Formulare müssen neu geladen werden. Eine Rotation entwertet beide Linkformen. Vor Entfernen alter Felder ist ein Rückweg über die gesicherten Werte möglich; danach ist für ein Rollback ein geprüftes Backup erforderlich.

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

tests/create-schema.php akzeptiert ausschließlich eine explizite moorl_tv_*_test-Datenbank und verweigert das Ersetzen nichtleerer Plugin-Tabellen. Es verwendet den tatsächlichen MoorlDevTools-Builder. Tabellen werden vor ihren Fremdschlüsseln erzeugt. Unique-Flags kommen aus den Definitionen. Nicht eindeutige zusätzliche Suchindizes sind über das externe Tool anzulegen, insbesondere `(moorl_tv_ticket_type_id, email)` und `(moorl_tv_ticket_type_id, decision, created_at)` für Anmeldungen. Die aktuelle Gästelistenstruktur benötigt keinen Event-/Typ-FK-Zyklus mehr.

MoorlDevTools erzeugt CREATE-/ALTER-Anweisungen und Fremdschlüssel gemeinsam pro Entity. Den vorhandenen generierten Migrationssatz vor Auslieferung mit dem externen Werkzeug auf das neue Typmodell und den Wegfall von `technical_name` abgleichen. Bei bestehenden Datenbanken zuerst die additive Datenübernahme ausführen; ein direkter destruktiver Komplettabgleich würde die bisherige Zuordnung entfernen. Das Plugin ergänzt keine handgeschriebenen PHP-Migrationen und führt diese Umstellung nicht automatisch durch. Ein grünes direkt aus DAL-Definitionen erzeugtes Testschema allein belegt nicht die Aktualität der vorhandenen generierten Migrationen.

    docker exec -e MOORL_TV_TEST_DATABASE_NAME=moorl_tv_extension_20261019_test -w /var/www/html shopware_6.7.14.1 php custom/plugins/MoorlTicketVendor/tests/create-schema.php
    docker exec -e MOORL_TV_TEST_DATABASE_NAME=moorl_tv_extension_20261019_test -w /var/www/html shopware_6.7.14.1 php vendor/bin/phpunit -c custom/plugins/MoorlTicketVendor/phpunit.xml.dist

Der Testname ist eine Entwicklungsreferenz; niemals eine reguläre Shopdatenbank als Testdatenbank verwenden. Native Mailtransporte werden in Versandtests ersetzt. Weitere Laufzeitdetails stehen in runtime.md.
