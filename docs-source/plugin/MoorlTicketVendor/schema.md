# TicketVendor: aktuelles Datenmodell

Stand: 16.10.2026. Das Plugin enthält inzwischen Checkout, Zahlungsprüfung, Administration, Versand und Check-in. Diese Datei beschreibt das Datenmodell; Betriebsabläufe stehen in [runtime.md](runtime.md).

## Tabellen und Beziehungen

Neu für strukturierte Eventdaten: nullable JSON-Spalte `moorl_tv_ticket_sale_translation.schema_org` über das externe Schemawerkzeug erzeugen. Die DAL-Eigenschaft `schemaOrg` ist übersetzbar und API-lesbar. Ergänzungen werden mit automatisch erzeugten Eventdaten zusammengeführt und als JSON-LD auf der Detailseite ausgegeben. Details: [schema-org.md](schema-org.md). Es wird keine zusätzliche PHP-Migration angelegt.

Veranstaltungen haben keinen eigenen Status. Freigabe und Sichtbarkeit ergeben sich aus `active` und den vorhandenen Zeitfenstern. Bei bestehenden Installationen die obsolete Spalte `moorl_tv_ticket_sale.status` mit dem externen Schemawerkzeug entfernen und vorhandene Veranstaltungs-Importprofile ohne dieses Feld abgleichen. Ticket-, Versand- und Bestellstatus sind davon unabhängig.

| Tabelle | Zweck und Beziehungen |
|---|---|
| `moorl_tv_ticket_sale` | Event mit Foundation-Inhalt, Banner, Adresse/Koordinaten, CMS-Bezug, Verkaufszeitraum und separaten Eventzeiten |
| `moorl_tv_ticket_sale_translation` | Foundation-Texte/Meta-Daten und `location_description`; PK `moorl_tv_ticket_sale_id`, `language_id` |
| `moorl_tv_ticket_type` | Kategorie; erforderlicher Sale-/Steuerbezug, Foundation-Preis/Medien/Basistexte/Zeitraum, Kontingent/Kaufgrenzen |
| `moorl_tv_ticket_type_translation` | Basistexte; PK `moorl_tv_ticket_type_id`, `language_id` |
| `moorl_tv_ticket` | Individuelles Ticket; erforderliche Veranstaltung und Typ, optionale Bestellposition und optionaler Kunde |
| `moorl_tv_ticket_checkin` | Scan-Audit mit optionalem Ticket und Sale; unbekannte Tokens können protokolliert werden |

`TicketReservation` und `TicketIssuance` samt ihren Tabellen/Services/Associations entfallen. Kein `issuanceId`, keine Batch-ID, keine duplizierte `orderId` am Ticket. Gruppierung per DAL-Filter `orderLineItem.orderId`; bei abweichendem Core-Versionskontext auch Version berücksichtigen. Die Veranstaltung wird direkt über `saleId`/`sale` gespeichert, zusätzlich zum Typbezug. So können Tickets über `Veranstaltung.tickets` angelegt und direkt nach Veranstaltung gefiltert werden. Die spätere Ausstellungslogik muss `ticket.saleId === ticket.type.saleId` sicherstellen; zwei unabhängige Fremdschlüssel prüfen diese Übereinstimmung nicht.

Relationen werden durch `FieldMultiEntityCollection` erzeugt. Die Storage-Namen enthalten den vollständigen Namen der referenzierten Tabelle; Properties und Collection-Namen folgen `ExtractedDefinition` einschließlich der vorhandenen `PROPERTY_NAME`-Konstanten.

| Relation | FK-Property / SQL-Spalte | Association |
|---|---|---|
| Ticket → Typ | `typeId` / `moorl_tv_ticket_type_id` | `type` |
| Ticket → Sale | `saleId` / `moorl_tv_ticket_sale_id` | `sale` |
| Typ → Sale | `saleId` / `moorl_tv_ticket_sale_id` | `sale` |
| Check-in → Ticket | `ticketId` / `moorl_tv_ticket_id` | `ticket` |
| Check-in → Sale | `saleId` / `moorl_tv_ticket_sale_id` | `sale` |

Die inversen Collections heißen `types`, `tickets` und `checkins`; Core-Extensions verwenden `tickets` beziehungsweise `sales`. Bestellpositionen werden über `ExtractedDefinition::addVersionDefinition()` als versioniert registriert. Die vom Helper erzeugte Referenzversion erhält weiterhin `Required` und den `order_unit`-Unique-Key, während die Positions-ID optional bleibt.

Bestehende Datenbanken mit den bisherigen verkürzten FK-Spalten müssen mit dem externen Schemawerkzeug abgeglichen werden. Diese Codeänderung führt keine Schemaänderung oder Datenmigration aus.

Veranstaltungen verwenden `id` und den übersetzbaren `name`; `technicalName`/`technical_name` entfällt bei `moorl_tv_ticket_sale`. Die alten generierten Create-Table-Migrationen müssen über das externe Werkzeug neu erzeugt werden. In vorhandenen Datenbanken die bisherige `technical_name`-Spalte entfernen, da ihre alte `NOT NULL`-Vorgabe Inserts ohne dieses Feld verhindern würde. Bei Tickettypen und den Import-/Exportprofilen selbst bleibt deren technischer Name erhalten.

Für den direkten Veranstaltungsbezug muss das externe Schemawerkzeug zusätzlich `moorl_tv_ticket.moorl_tv_ticket_sale_id` mit FK auf `moorl_tv_ticket_sale.id` anlegen. Bei vorhandenen Tickets zunächst die Spalte nullable hinzufügen, die Werte aus dem zugehörigen Tickettyp übernehmen und anschließend `NOT NULL` und den FK aktivieren. Bestehende Create-Table-Migrationen erweitern bereits vorhandene Tabellen nicht.

## Ticketfelder

Alle Entities haben UUID-ID und Shopware-Zeitstempel; Ticket zusätzlich `customFields`.

| Property / Spalte | Anforderung |
|---|---|
| `typeId` / `moorl_tv_ticket_type_id` | Erforderlicher Typbezug |
| `saleId` / `moorl_tv_ticket_sale_id` | Erforderlicher direkter Veranstaltungsbezug |
| `orderLineItemId` / `order_line_item_id` | Optional, NULL bei manuellen Tickets |
| `orderLineItemVersionId` / `order_line_item_version_id` | Erforderlich mit Live-Default, auch bei NULL-Positions-ID |
| `unitIndex` / `unit_index` | Integer ≥ 0, Default 0; einzelne Einheit der Bestellposition |
| `ticketNumber` / `ticket_number` | Native `NumberRangeField`, automatisch aus Nummernkreis `moorl_tv_ticket`, eindeutig und nach Erstellung unveränderlich, maximal 64 Zeichen |
| `token` | Erforderlicher eindeutiger Klartext, maximal 64 Zeichen; intern über `getToken()` |
| `customerId` / `customer_id` | Optionaler Shopware-Kunde, Foundation `EntityCustomerTrait` |
| `recipientEmail` / `recipient_email` | Optionales natives `EmailField`, auch ohne Kundenkonto |
| `attendeeName` / `attendee_name` | Optionales `StringField`, maximal 511 Zeichen, Vor- und Nachname auf PDF und Scan-Ergebnis |
| `attendeePhone` / `attendee_phone` | Optionale Handynummer als `StringField`, nullable `VARCHAR(64)`; Scan-Ergebnis und Anruflink im Browser-Scanner |
| `attendeePhone` / `attendee_phone` | Optionale Handynummer als `StringField`, nullable `VARCHAR(64)`; Scan-Ergebnis und Anruflink im Browser-Scanner |
| `status` | `pending`, `valid` (Default), `expired`, `redeemed`, `revoked` |
| `expiresAt` / `expires_at` | Optionale Zahlungsfrist für offene Tickets |
| `issuedAt` / `issued_at` | Erforderlicher Zeitpunkt der Ticketerzeugung, auch vor Zahlung |
| `redeemedAt`, `revokedAt` | Optionale Einlöse-/Widerrufszeitpunkte |
| `deliveryStatus` / `delivery_status` | `pending` (Default), `sent`, `failed` |
| `deliveredAt` / `delivered_at` | Optionaler Versandzeitpunkt |
| `deliveryAttempts` / `delivery_attempts` | Integer ≥ 0, Default 0 |
| `lastDeliveryError` / `last_delivery_error` | Optionaler interner Fehlertext; keine Tokens/Geheimnisse speichern |

`getDeliveryRecipientEmail()` löst die Adresse aus **expliziter E-Mail → Kunde → Bestellkunde** auf. Für Fallbacks müssen `customer` und `orderLineItem.order.orderCustomer` geladen sein. Der Bestellkunde liefert den in der Bestellung gespeicherten E-Mail-Snapshot. Ohne Empfänger bleibt das Ergebnis NULL; das Ticket darf gespeichert werden, ist aber noch nicht versandfähig. Ein leerer E-Mail-Override wird nicht als Versandadresse verwendet.

Token und letzter Versandfehler sind nicht `ApiAware` und werden bei allgemeiner JSON-Serialisierung ausgeblendet. Vertrauenswürdige Dienste lesen die Getter. Allgemeine Admin-API-Ausgaben veröffentlichen den Token nicht. Neue Tokens werden mit 32 zufälligen Zeichen erzeugt; der Check-in-Endpunkt prüft Token und Event-ID gemeinsam.

## Zustände und Abläufe

Für die Handynummer `moorl_tv_ticket.attendee_phone` über das externe Schemawerkzeug als nullable `VARCHAR(64)` ergänzen. Name und Nummer sind in Administration und Kundenkonto bei `pending`/`valid` bearbeitbar; nach Einlösung, Ablauf oder Widerruf sperrt der DAL beide Felder. Eine leere Nummer wird im Kundenkonto gelöscht, ein nicht mitgesendetes Feld erhält die bisherige Nummer. Scan-Wiederholungen geben die zum ursprünglichen Scan gespeicherte Nummer zurück; bei unbekannten oder fremden Veranstaltungstickets bleibt sie `null`.

Für die Handynummer `moorl_tv_ticket.attendee_phone` über das externe Schemawerkzeug als nullable `VARCHAR(64)` ergänzen. Name und Nummer sind in Administration und Kundenkonto bei `pending`/`valid` bearbeitbar; nach Einlösung, Ablauf oder Widerruf sperrt der DAL beide Felder. Eine leere Nummer wird im Kundenkonto gelöscht, ein nicht mitgesendetes Feld erhält die bisherige Nummer. Scan-Wiederholungen geben die zum ursprünglichen Scan gespeicherte Nummer zurück; bei unbekannten oder fremden Veranstaltungstickets bleibt sie `null`.

Für die Personalisierung mit dem externen Schemawerkzeug die nullable Spalte `moorl_tv_ticket.attendee_name` als `VARCHAR(511)` ergänzen. Es gibt keine zusätzliche PHP-Migration. Neue Bestelltickets speichern den Namen aus dem Bestellkunden-Snapshot. Bei bestehenden oder manuellen Tickets ohne Namen verwendet die Ausgabe den geladenen Bestellkunden, sonst den zugewiesenen Kunden. Die Änderung des Namens setzt weder Kundenzuordnung noch Empfänger-E-Mail um. Der DAL sperrt Namensänderungen bei bereits eingelösten, abgelaufenen und widerrufenen Tickets unter denselben Sperren wie die Kontingentprüfung.

- Warenkorb-Neuberechnung prüft Kontingent ohne Reservierung.
- Bestellabschluss prüft/belegt Kontingent atomar mit `pending`-Tickets, `expiresAt` und eindeutigen Positionseinheiten. Dieser Checkout muss `pending` ausdrücklich setzen; der DAL-Default `valid` dient manuellen Tickets.
- Zahlung aktiviert Tickets. Nicht bezahlte Tickets nach erneuter Zahlungsprüfung und Stornierung der Bestellung auf `expired` setzen; damit Kontingent freigeben und Historie erhalten. Bei später Zahlung muss die Laufzeitlogik eine ausdrückliche Entscheidung treffen.
- Bestellungen gruppieren Tickets für Sammelmails; manuelle Tickets werden einzeln verschickt. Der Versand trennt unterschiedliche tatsächliche Empfänger.
- Versandstatus liegt am Ticket. Die implementierten Dienste, Wiederholungen, Sperren und Zahlungs-/Ablaufentscheidungen sind in `runtime.md` beschrieben.

## Schemaerstellung und Integrität

**Keine PHP-Migrationen:** Die vom Benutzer gelöschten Dateien bleiben gelöscht. Das Produktivschema wird mit seinem externen Tool erzeugt/abgeglichen. Die Definitionen sind die aktuelle Quelle. Bestehende Produktivdaten wurden nicht umgebaut. Bei vorhandenen Daten müssen Empfänger/Versandinformationen aus alten Ausstellungen vor dem Entfernen der Tabellen übernommen werden; das externe Tool erledigt diese fachliche Datenübernahme nicht automatisch.

Foundation `UniqueKey` wird vom vorhandenen MoorlDevTools `SchemaBuilderExtension` ausgewertet:

| Index | Spalten |
|---|---|
| `uniq_moorl_tv_ticket_number` | `ticket_number` |
| `uniq_moorl_tv_ticket_token` | `token` |
| `uniq_moorl_tv_ticket_order_unit` | `order_line_item_id`, `order_line_item_version_id`, `unit_index` |
| `uniq_moorl_tv_ticket_checkin_request` | `scan_request_id` |

Der Order-Unit-Index erlaubt mehrere manuelle Tickets ohne Positions-ID. Ticketnummer und Token bleiben auch dann eindeutig. Native Referenzversionen sind NOT NULL mit Live-Default; NULL setzt der Core-Serializer auf Live zurück. Zusammengesetzte FKs sichern bestehende Positionen/CMS-Versionen ab.

Sale → Typ, Typ → Ticket und Ticket → Check-in verwenden `RestrictDelete`; ebenfalls Ticket → Bestellposition/Kunde und Sale → CMS. Check-ins bleiben Audit-Daten. Keine implizite Löschung von Tickets beim Löschen einer Bestellung oder eines Kunden.

Für Core-Bezüge liegt das DAL-Flag auf inversen One-to-many-Associations in `CustomerExtension`, `OrderLineItemExtension` und `CmsPageExtension`. So bleibt das Löschen eines ungescannten Tickets oder eines ungenutzten CMS-verknüpften Sales möglich, während referenzierte Core-Datensätze geschützt sind. Die Extensions ergänzen keine SQL-Spalten. Der SchemaBuilder leitet daraus die restriktiven FKs ab; seine temporären Änderungen an kompilierten Feldern laufen im separaten Schemahelfer-Prozess.

Das Tool erzeugt FK-Indizes, aber keine fachlichen Suchindizes aus DAL-Flags. Bei späteren Laufzeitabfragen bei Bedarf ergänzen: Ticket `(moorl_tv_ticket_type_id, status, expires_at)`, Check-in `(moorl_tv_ticket_id, scanned_at)` und Typ `(moorl_tv_ticket_sale_id, position)`. Native `Choice(..., strict: true)`, `EmailField` und Integer-Grenzen validieren DAL-Schreibzugriffe. Das Tool erzeugt daraus keine SQL-CHECKs; direkte SQL-Zugriffe umgehen diese Validierung. Statusfelder bleiben VARCHAR, keine SQL-ENUMs.

Der aktuelle Builder erzeugt DATETIME ohne Millisekunden-Präzision; DATETIME(3) aus den früheren manuellen Migrationen wird nicht automatisch übernommen. Falls Millisekunden benötigt werden, muss das externe Schematool diese Präzision vorgeben.

`quantitySold` bleibt ein abgeleiteter, für Benutzer schreibgeschützter Zähler. `pending`, `valid`, `redeemed` belegen Plätze; `expired`/`revoked` geben sie frei. Der DAL prüft und aktualisiert das Kontingent unter Sperren in derselben Transaktion wie die Ticketänderung.

## Verifikation

Lokale Unit-Tests, Integrationstests werden ohne explizite Testdatenbank übersprungen:

```powershell
php vendor/bin/phpunit -c custom/plugins/MoorlTicketVendor/phpunit.xml.dist
```

Isolierte Docker-Testdatenbank vorbereiten und komplette Plugin-Suite ausführen:

```powershell
docker exec -e MOORL_TV_TEST_DATABASE_NAME=moorl_tv_simplified_20261015_test -w /var/www/html shopware_6.7.14.1 php custom/plugins/MoorlTicketVendor/tests/create-schema.php
docker exec -e MOORL_TV_TEST_DATABASE_NAME=moorl_tv_simplified_20261015_test -w /var/www/html shopware_6.7.14.1 php vendor/bin/phpunit -c custom/plugins/MoorlTicketVendor/phpunit.xml.dist
```

Der explizite Schemahelfer verwendet den realen MoorlDevTools-Builder. Er prüft Datenbanknamen und lehnt das Ersetzen nichtleerer Tickettabellen ab. Nur die isolierte Testdatenbank darf verändert werden; kein Zugriff auf das Schema der normalen Shopdatenbank. Shopware TestBootstrapper installiert bei Bedarf den Core und die beiden Plugins. Die alten Migrationstests wurden entfernt, weil deren Migrationsklassen vom Benutzer gelöscht wurden. Ihre Persistenz-/Versionsprüfungen verbleiben in den aktuellen DAL-Tests.

Für eine erneute saubere Schemaerzeugung einen unbenutzten Testdatenbanknamen wählen. Das Ablehnen bereits befüllter Testtabellen ist beabsichtigt. Der spätere CMS-Draft-Test kann wegen Core-DDL/Versionsverhalten Testdaten hinterlassen.

Prüflauf vom 16.10.2026 nach dem unabhängigen Review: Schema auf der frischen Shopware-Datenbank `moorl_tv_foundation_20261016_070348_test` über MoorlDevTools erzeugt; komplette Plugin-Suite **24 Tests, 589 Assertions**, ohne übersprungene Tests. Geprüft sind Foundation-FK-Namen, Entity-/Collection-Hydrierung, Versionsflags, Unique-Indizes und beide Löschschutzrichtungen. Alle **28 PHP-Dateien** bestehen den Syntaxcheck und verwenden Klassenimporte am Dateianfang. Eine zusätzliche Bestell-Draftversion als Testfall bleibt eine optionale Erweiterung; Bestellbezüge werden bisher mit Live-Version und CMS-Bezüge auch mit einer Draftversion geprüft.
