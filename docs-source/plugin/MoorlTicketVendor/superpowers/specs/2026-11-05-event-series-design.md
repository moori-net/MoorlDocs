# Veranstaltungsserien im MoorlTicketVendor

Stand: 05.11.2026. Freigegebene technische Grundlage der implementierten Erweiterung. Bedienung und Upgrade stehen in [Veranstaltungsserien](../../event-series.md).

## Ziel und verbindlicher Umfang

Eine neue Hauptveranstaltung bündelt beliebig viele eigenständige Veranstaltungen. Die bestehenden Admin-Entities und ihre Routen bleiben bestehen. Ein Event kann weiterhin ohne Serie angelegt werden. Texte und Bilder eines zugeordneten Events kommen aus der Hauptveranstaltung; Datum, Ort, Tickettypen, Preise, Kontingente, Programm, Gästeliste und Einlösungen bleiben am Event.

Die Serie erhält wie Veranstaltungen ein Foundation-Adminmodul, eine eigene CMS-Detailseite, SEO-URLs, Suche mit Suchvorschlägen und CMS-Listingelemente. Zusätzlich lassen sich Termine anhand eines Intervalls erzeugen.

Die neue Benutzeranweisung ersetzt für diese Erweiterung die früheren Verbote neuer Schemaänderungen in CODEX.md: neue additive Shopware-Migrationen nach der bestehenden Migration, kein erneuter Initialschema-Reset. Die vorhandene Migration `Migration1793194127Initial` bleibt unverändert. Es werden keine laufenden Shopdatenbanken während der Planung geändert.

## Architekturentscheidung

Gewählt ist eine separate Main-Entity `TicketSeries` (`moorl_tv_ticket_series`) mit optionaler Zuordnung am bestehenden `TicketSale`. Eine Self-Reference innerhalb der Events würde die Hauptveranstaltung mit Pflichtbeginn, Ort, Kapazität und Ticketverkauf belasten. Eine vollständige Aufteilung der bestehenden Events würde IDs und Integrationen unnötig verändern. Beide Alternativen entfallen.

Bestätigte Ergänzungen: Eine deaktivierte Serie blendet ihre Termine im Shop aus und sperrt neue Käufe; vorhandene Tickets bleiben abrufbar und einlösbar. Ob generierte Events aktiv angelegt werden, wird beim Generieren gewählt. Wiederholung erfolgt über einen einfachen Intervall oder bestimmte Wochentage. Weitere Detailregeln sind technische Vorschläge dieses Entwurfs.

## Datenmodell

| Entity | Neue oder maßgebliche Felder |
| --- | --- |
| TicketSeries | Foundation-Basisfelder, active, listed, showFrom, showUntil, mediaId, bannerId, Bannerdarstellung, cmsPageId, cmsPageVersionId |
| TicketSeriesTranslation | name, description, teaser, keywords, metaTitle, metaDescription, metaKeywords, metaMediaId, slotConfig |
| TicketSale | nullable seriesId und Association series; nullable generationKey ausschließlich für erzeugte Termine |
| TicketSeries.sales | Inverse One-to-many-Relation zu den bestehenden Events |

Die Feldtypen und SQL-Namen folgen den bestehenden Foundation-Collections. `seriesId` liegt als `moorl_tv_ticket_series_id BINARY(16) NULL` am Event. `generationKey` liegt als `generation_key CHAR(64) NULL` am Event und ist gegen allgemeine API-/Import-Writes geschützt; nur Generator und Zuordnungsservice dürfen ihn mit kurzlebiger interner Autorisierung schreiben oder löschen. Zusammengesetzter Unique-Index auf `(moorl_tv_ticket_series_id, generation_key)` verhindert doppelte Generierung desselben Slots. Manuelle Events haben keinen generationKey; mehrere Termine zur selben Uhrzeit bleiben damit möglich.

Keine eigenen Tickets, Tickettypen, Kapazitäten, Veranstaltungsadressen oder Pflichttermine an der Serie. Keine Serienverschachtelung. Die Serien-Zeitzone ist keine Vorgabe für bestehende Events; für die Generierung wird die Zeitzone des ausgewählten Mustertermins verwendet.

Serienübersetzungen verwenden die native Sprach-Fallback-Kette. Medienreferenzen verwenden SET NULL; Serienübersetzungen werden mit ihrer Serie gelöscht. Die inverse sales-Relation und der Event-FK schützen eine noch zugeordnete Serie mit RESTRICT. CMS-Seiten erhalten wie bei Events inversen DAL-Löschschutz und den passenden nativen Versionsbezug.

## Gemeinsame Inhalte und Einzelevents

Gemeinsam sind Name, Beschreibung, Teaser, Suchbegriffe, Titelbild, Banner inklusive Darstellungswerten sowie Meta-Texte und Meta-Bild. Ortsbeschreibung, Tickettyptexte/-bilder, Mailhinweise und Gästelistenregeln bleiben terminspezifisch. Es wird keine bislang nicht vorhandene Bildergalerie eingeführt.

Bei `seriesId = null` gelten ausschließlich die bisherigen lokalen Inhalte. Mit Serie gelten ausschließlich die Serieninhalte, auch wenn ein optionales Serienfeld leer ist. Es gibt keinen Rückfall auf alte lokale Eventtexte und keine Überschreibung pro Termin. Sprach-Fallback erfolgt innerhalb der Serie, nicht zwischen Serie und Event.

Ein zentraler `EventContentResolver` erstellt aus geladenen Events eine aufgelöste Präsentation. Er lädt Serien samt Medien für eine Collection gebündelt und erstellt Event-Kopien mit effektiven Inhalten. Persistierte Entities werden nicht verändert. Die Kopien dürfen nicht an Schreibservices übergeben werden. Datum, Ort, IDs und operative Relationsdaten werden unverändert übernommen. Öffentliche Projektionen enthalten keine privaten Ticket-, Booking- oder Anmeldedaten.

Alle Leser müssen denselben Resolver verwenden: Detail- und Listingseiten, CMS-Daten, Suchvorschläge, Warenkorb neuer Positionen, Kundenkonto, Deeplink, aktuelle PDFs, Maildaten, strukturierte Daten und Adminanzeigen. Historische Bestellpositionen behalten ihre gespeicherten Bezeichnungen und Metadaten; eine Serienänderung schreibt keine Bestellungen um und verschickt keine Tickets erneut.

Vorhandene lokale Inhaltsfelder bleiben im Schema und bei Zuordnung erhalten. Neue Serientermine erhalten einen lokalen Start-Snapshot aus der Serie, um die bisherigen Pflichtfelder zu erfüllen; dieser ist bei zugeordneten Events keine Inhaltsquelle. Nach einer Serienänderung werden keine Eventtexte synchronisiert.

Beim Abtrennen wird in einer Transaktion unter Serien-/Eventsperre der aktuelle Serieninhalt in die lokalen gemeinsamen Felder übernommen. Verwendet wird die Vereinigungsmenge aus lokalen und Serien-Sprachdatensätzen. Für jede dieser Sprachen werden alle gemeinsamen Felder aus der für diese Sprache nativ aufgelösten Serie übernommen, einschließlich des erforderlichen NOT-NULL-Namens. Terminspezifische Übersetzungsfelder bleiben erhalten. So werden alte lokale Texte nach dem Abtrennen nicht wieder sichtbar, auch bei lokalen Sprachen ohne eigene Serienübersetzung. Medienreferenzen werden kopiert, nicht die Dateien. Anschließend werden seriesId und generationKey geleert. Beim Wechsel zu einer anderen Serie bleiben lokale Altinhalte erhalten und die neue Serie liefert die Anzeige. Generierungsherkunft wird beim Wechsel gelöscht. Direkte DAL-/Import-/Sync-Writes unterliegen denselben Regeln wie Adminaktionen; fehlt bei einer rohen Verknüpfungsänderung der erforderliche Übernahmeprozess, wird der Write abgewiesen statt still unvollständig ausgeführt.

## Administration

Neues Modul `moorl-tv-series` auf Basis von `MoorlFoundation.ModuleHelper.registerModule`, Entity `moorl_tv_ticket_series`, CMS-Seitentyp `moorl_tv_ticket_series_detail`. Eigene Liste, Suche, Detailformular und CRUD-Berechtigungen nach Foundation-Muster. Vorhandene Events, Tickettypen und Scanner bleiben eigene Module.

Serienformular: Allgemein/Inhalte, Medien/Banner, Veröffentlichung, SEO, Layout sowie Tab Termine. Die Termintabelle ist nach seriesId gefiltert und bietet Neuanlage, Zuordnen eines vorhandenen Events und Intervallgenerierung. Ein vorhandenes Event wird weder dupliziert noch stillschweigend aus einer anderen Serie verschoben; ein Wechsel ist eine explizite Aktion.

Am Event erscheint eine optionale Serienauswahl. Zugeordnete gemeinsame Inhalte sind als schreibgeschützte Vorschau mit Link zur Hauptveranstaltung sichtbar. Datum, Ort und Verkaufsdaten bleiben wie bisher bearbeitbar. Abtrennen ist eine eigene Aktion mit Erklärung der Inhaltsübernahme. Eventlisten und Auswahllisten zeigen den effektiven Namen zusammen mit Datum und Ort.

Rechte werden getrennt gehalten: Serien-CRUD, Event-CRUD und Generierung. Die Generierung benötigt `moorl_tv_ticket_series:read`, `moorl_tv_ticket_sale:read`, `moorl_tv_ticket_sale:create` und `moorl_tv_ticket_type:read/create`. Zuordnen/Abtrennen benötigt Event-update und Leserecht an der betroffenen Serie. Direkte Verknüpfungsänderungen müssen diese Grenzen ebenfalls einhalten. Redakteure benötigen zusätzlich Serien-read, wenn ihre generischen Event-Suchkriterien series-Felder abfragen; eine entsprechende zusätzliche ACL-Zuordnung bündelt diese Abhängigkeit für redaktionelle Rollen. Die bestehende Scannerrolle erhält keine allgemeinen Serien-/Kunden-/Bestellrechte. Ihr Eventselect verwendet stattdessen `POST /api/_action/moorl-tv/scanner/events` mit Scan- und Event-read-Prüfung: begrenzte öffentliche Projektion aus Event-ID, effektivem Namen, Beginn, Ende, Zeitzone und Ort. Filter auf aktive Events ab dem bisherigen inklusiven Drei-Tage-Cutoff, serverseitige term/page-Suche und höchstens 25 Einträge je Seite bleiben erhalten. Dieser Endpunkt liest nur öffentliche Serienfelder intern; er öffnet keinen allgemeinen Serien-API-Zugriff.

## Storefront und CMS

Eigener Controller `TicketSeriesController`, Route `/moorl-tv/series/{seriesId}`, Routenname `frontend.moorl.tv.series.detail`. Die Serienseite zeigt gemeinsame Inhalte und darunter Termine mit Datum, Uhrzeit, Zeitzone, Ort und Link zum konkreten Ticketverkauf. Die Terminliste ist paginiert, standardmäßig aufsteigend nach startAt/id, und zeigt dieselben öffentlich verfügbaren Termine wie der bestehende Eventfilter.

Die Serie hat eine eigene `cmsPageId` und übersetzte slotConfig. Layoutauflösung: Serienlayout, Verkaufskanal-Konfiguration `seriesCmsPageId`, mitgeliefertes Standardlayout. Termindetails behalten ihre eigene bestehende CMS-Layoutauflösung. Das Serienlayout wird nicht als Eventlayout vererbt, weil Serien- und Termindetail verschiedene CMS-Kontexte haben.

Neue CMS-Elemente mit Foundation-Registrierung, Vorschau, Konfiguration, Resolver und Twig-Ausgabe:

- `moorl-tv-ticket-series-detail`: Serieninhalt im EntityResolverContext.
- `moorl-tv-ticket-series-listing`: dynamisches/paginiertes Serienlisting mit Foundation-Auswahl und Filtern.
- `moorl-tv-ticket-series-static-listing`: kuratierte/statische Übersicht analog zum bestehenden statischen Eventlisting, einschließlich Archivfällen.
- `moorl-tv-ticket-series-dates`: paginierte Termine der aktuellen oder explizit gewählten Serie; keine fremden Events bei fehlendem Serienkontext.

Eigene mitgelieferte CMS-Seiten für Serienlisting und Seriendetail, neue stabile IDs. Existierende CMS-Seiten und Händlerlayouts werden nicht ersetzt. Bestehende Eventlistings bleiben Terminlistings; Serien werden nicht stillschweigend anstelle von Events eingesetzt. Eigene Serien-CMS-Elemente entscheiden, wo Serienkarten erscheinen.

Serie active/showFrom/showUntil ist eine zusätzliche öffentliche Freigabe für ihre Termine. Eventeigene Freigaben bleiben zusätzlich erforderlich. Deaktivieren einer Serie verändert nicht die gespeicherten active-Werte der einzelnen Termine; es sperrt deren öffentliche Anzeige und neue Käufe über die übergeordnete Freigabe. Nach Reaktivierung gelten wieder die eigenen Terminfreigaben. Eine nicht gelistete Serie (`listed = false`) bleibt direkt aufrufbar und schaltet ihre Termine nicht ab. Serienkarten in dynamischer Suche/Listing setzen mindestens einen öffentlich verfügbaren Termin voraus. Eine direkt aufgerufene aktive Serie ohne kommende Termine zeigt einen Leerezustand; die statische Übersicht darf sie als Archiv anzeigen. Bestandskunden behalten Zugriff auf berechtigte Tickets/PDFs bei deaktivierter Serie; bestehende Tickets bleiben nach den bisherigen Check-in-Regeln einlösbar. Neue Käufe werden dann wie bei einem deaktivierten Event abgewiesen.

## Suche, SEO und Cache

`TicketSeriesListing` wird wie `TicketSaleListing` als `moorl.foundation.entity_search` und `moorl.foundation.entity_suggest` registriert. Eigene Such-/Suggest-Templates, Tab `moorl-tv-ticket-series-listing` und Konfigurationspräfix `seriesSearch*`/`seriesSuggest*` trennen Limits und Aktivierung von der bestehenden Eventsuche. `TicketSeriesListing::getConfig(string $key): mixed` übersetzt die generischen Foundation-Keys explizit auf die Serienkeys, einschließlich typed bool/int und JSON-Listingkonfiguration; ein neuer Präfix wirkt im vorhandenen Foundation-Listing nicht automatisch. Foundation advancedSearchActive bleibt Voraussetzung.

Die Paginationkorrektur des bestehenden `TicketSaleSearchRoute` muss beide Tabs berücksichtigen. Serientexte müssen auch zugeordnete Events in Eventsuche und Adminsuche auffindbar machen. Ein gemeinsamer Criteria-Builder berücksichtigt zwei Zweige: Einzelevents über lokale Inhalte; Serientermine über series.name/description/teaser/keywords. Ortsfelder bleiben terminspezifisch. Mehrere Wörter werden mit AND verknüpft, Felder pro Wort mit OR. Falsche Treffer auf aufbewahrte lokale Alttexte sind ausgeschlossen. Filter, Gesamttrefferzahl und Pagination werden in der Datenbank angewandt; keine nachträgliche PHP-Filterung. Im Admin werden die Suchkriterien in den betroffenen Plugin-Listen und Selects gebaut, ohne den globalen Shopware-API-Controller zu ändern.

Eigene SEO-Route und eigenes Template für Serien: `moorl-tv/series/{{ series.translated.name }}/{{ series.id }}`. Event-IDs, technische Eventrouten und existierende SEO-URLs bleiben gültig. Serienänderungen indexieren Serienseiten und betroffene Termindetails neu; bei Event-SEO wird der effektive Name verwendet. Jeder Termin behält eine eigene Canonical-URL. Seriendetail hat eine eigene Canonical-URL, keinen fingierten Veranstaltungsort und keine buchbaren Serien-Offers. Vorhandene Event-JSON-LD-Daten verwenden gemeinsamen Inhalt und konkrete Termindaten; keine zusätzliche schema.org-Typerweiterung für Serien im ersten Umfang.

`StorefrontCacheSubscriber` wird um Serie/Übersetzungen erweitert. Der bestehende gemeinsame Storefront-Tag invalidiert auch Terminseiten, Suchergebnisse, leere Listings und Serien-Termintabellen. `TicketSeriesDefinition` implementiert wie TicketSale `EntityAutoCacheInterface` und erhält den Tag `moorl.foundation.entity_auto_cache`, START_TIME=show_from, END_TIME=show_until, ACTIVE=active sowie die vier neuen und betroffenen bestehenden Event-CMS-Slottypen. Damit werden auch Freigabegrenzen ohne einen Schreibvorgang von Foundations Live-/Scheduled-Prüfung erfasst; warme direkte Seiten und leere Ergebnisse müssen darüber hinaus tatsächlich mit invalidiert werden. Kein N+1: Inhalt und Terminvorschau werden pro Ergebnisliste gebündelt geladen; keine unbeschränkten sales-Associations an jeder Serienkarte.

## Intervallgenerierung

Bewusste Adminaktion mit Vorschau und anschließendem Anlegen, keine laufende Hintergrund-Rekurrenz. Ausgangspunkt ist ein bestehender Mustertermin. Kopiert werden dessen Orts-/Adress-/Geodaten, Zeitzone, Kapazität, listed, terminspezifische Orts-/Gästelistentexte, CMS-Layout samt Slotkonfiguration und Freigabefenster. Die Serienzuordnung kommt aus der gewählten Zielserie, nicht aus dem Mustertermin. CustomFields und alternativeUrl werden zunächst nicht kopiert.

Tickettypen erhalten neue IDs und übernehmen explizit name/description/keywords/emailNote in allen Sprachen, price, taxId, mediaId, personalizationEnabled, redemptionCategory, maxRedemptions, capacityUnits, quantityTotal, minPurchase, maxPurchase, position und Freigabefenster. Alle nicht genannten Felder verwenden die normalen Defaults. Nicht kopiert werden Tickets, Kunden-/Bestellbezüge, Check-ins, Anmeldungen, Verkaufszähler, Versandzustände, geheime Gästelistenlinks, Volunteer-Zuordnungen, Stages oder Performances. Frische Typen erhalten die normalen neu erzeugten Geheimnisse; die Gästelistenfreigabe ist zunächst aus.

Die Generierungsmaske verlangt die Auswahl „Aktiv anlegen“ oder „Inaktiv anlegen“. Technisch steuert ein erforderliches boolesches active sowohl neue Events als auch deren neu kopierte Tickettypen; es wird nicht aus der Vorlage übernommen. Die Vorschau zeigt die Wahl und die wirksame Serienfreigabe. Aktiv anlegen aktiviert weder eine deaktivierte Serie noch überspringt es Freigabefenster. Wiederholte Generierung verändert keine bereits vorhandenen Termine oder deren Aktivierung.

Zwei Wiederholungsmodi ersetzen die bisher vorgeschlagene Monatsregel:

- `mode = interval`: alle intervalDays Tage (1–365), beispielsweise täglich, alle drei Tage oder alle 14 Tage. Das lokale Startdatum ist der erste Slot.
- `mode = weekdays`: jede Woche an den gewählten Wochentagen, beispielsweise Montag und Donnerstag. weekdays ist eine nicht leere Liste eindeutiger ISO-Wochentage (1=Montag bis 7=Sonntag); intervalDays wird in diesem Modus nicht akzeptiert. Der erste passende Tag am oder nach dem Startdatum ist der erste Slot. Alle Slots verwenden dieselbe lokale Uhrzeit.

Intervall in Tagen ist die technische Auslegung des einfachen Intervalls; eine monatliche Wiederholung und zusätzliche Wochenabstände im Wochentagsmodus sind nicht vorgesehen. Gemeinsame Eingabe: seriesId, templateSaleId, lokaler Startbeginn, mode, active, genau eines von count (1–250) oder until (lokales Datum inklusive), sowie previewHash beim Anlegen. Im Intervallmodus ist weekdays nicht erlaubt. Die Terminzeitzone wird vom Mustertermin übernommen. Bei until ist der Horizont maximal fünf Jahre und die Vorschau maximal 250 Kandidaten; bei Überschreitung erfolgt ein Validierungsfehler statt stiller Kürzung. Count zählt geplante Slots einschließlich bereits generierter Slots, nicht nur neu anzulegende Events. Ein Bereich ohne passenden Wochentag liefert eine leere Vorschau und erlaubt kein Anlegen.

Termine werden im lokalen Kalender gerechnet und anschließend nach UTC konvertiert; keine UTC-Sekundenaddition für Folgetermine. Monat-/Jahreswechsel und Schaltjahre folgen bei Tagesintervallen automatisch dem lokalen Kalender. Ungültige oder doppeldeutige lokale Uhrzeiten an Sommerzeitgrenzen führen zu einem verständlichen Validierungsfehler; der Benutzer wählt eine eindeutige Uhrzeit. Die Dauer des Mustertermins wird als tatsächliche verstrichene Sekunden übernommen; ohne Ende bleibt endAt leer. showFrom/showUntil von Event und Typen werden relativ zum Musterbeginn um die jeweilige UTC-Differenz verschoben; NULL bleibt NULL. Ungültige resultierende Zeitfenster werden abgewiesen.

Pro Slot wird `generationKey = sha256(seriesId + '|' + timezone + '|' + localStart)` gebildet. Vorhandene Slots werden in der Vorschau als vorhanden markiert und beim Wiederholen übersprungen. Ein später manuell verschobener generierter Termin behält seine Herkunft; Wiederholung erzeugt den ursprünglichen Slot nicht erneut. Vorhandene Termine werden niemals aktualisiert oder gelöscht. Manuell angelegte gleichzeitige Events blockieren die Generierung nicht.

Vorschau enthält pro Slot lokalen/UTC-Beginn, Ende, Existenzstatus, active und geplante Typen sowie die wirksame Serienfreigabe. previewHash bindet normalisierte Eingabe einschließlich Modus, sortierter Wochentage und Aktivierungswahl, relevante Muster-/Typdaten, Serienzuordnung und Serienfreigabe; Anlegen prüft diese Daten nach dem Sperren erneut, veraltete Vorschauen liefern HTTP 409. Eine Änderung gemeinsamer Serientexte allein muss die Vorschau nicht entwerten, weil sie nicht kopiert werden. Eine DB-Transaktion mit Muster-/Serien-/Typsperren und Unique-Index sichert konkurrierende Anfragen. Modus und Aktivierungswahl sind kein Bestandteil des generationKey: derselbe Slot darf auch bei anderer Auswahl nicht doppelt entstehen.

Die Sperrreihenfolge erweitert den Bestand: order, bestehende sales nach ID, series nach ID, types nach ID, tickets. Generator sperrt Mustertermin vor Zielserie und Mustertypen; Zuordnung sperrt Event vor alter/neuer Serie. Eine vorab gelesene Serienzuordnung wird nach Sperren erneut geprüft und bei Änderung neu versucht. Serienschreibvorgänge sperren anschließend keine bestehenden Eventzeilen zum Schreiben; abhängige IDs werden nur gelesen und zur Indexierung eingereiht. Neue selbst eingefügte Events/Typen gehören ausschließlich zur eigenen Transaktion. Deadlocks werden begrenzt wiederholt oder ohne Teilanlage als Konflikt gemeldet.

## Migration, Installation und Betrieb

Eine neue native Migration `Migration<neuer Zeitstempel>EventSeries` erstellt zwei Serientabellen, ergänzt nullable Eventspalten samt Index/FK und lässt alle vorhandenen Eventinhalte unverändert. Keine automatischen Serien, keine automatische Gruppierung und keine Datenlöschung. Bei Erstinstallation laufen bestehende Initialmigration und neue Migration der Reihe nach. Bestehende Installationen führen nur die neue Migration aus. `updateDestructive()` bleibt leer.

Direkte SQL-Statements und gezielte Schema-Prüfungen erlauben Wiederholung nach teilweise abgeschlossener MySQL-DDL; keine pauschalen Exception-Fallbacks. Der native Migrationsgenerator liefert den Zeitstempel erst bei Umsetzung. PLUGIN_TABLES, Deinstallation, Media-/Importprofile, Installertexte und Schemaaudits werden erweitert. Bestehende Importprofile erhalten seriesId nur über einen ausdrücklich kompatiblen Profilabgleich; Händlerprofile werden nicht überschrieben. Zuordnung ohne Serie bleibt Standard. Datenerhalt bei Deinstallation gilt auch für Serien.

Migrationstests trennen den unveränderlichen historischen Initialstand vom Schema nach allen Migrationen. Harte Annahmen „genau eine Migration/sechzehn Tabellen“ werden nur dort ersetzt, wo der aktuelle Gesamtstand geprüft wird. Bestandsupgrade und Neuinstallation müssen dasselbe neue Schema ergeben, inklusive identischer FK-Löschregeln und Indizes.

## Abnahme

Einzelevents verhalten sich unverändert. Zwei Termine derselben Serie zeigen nach Änderung des Seriennamens/Bildes überall die neuen Inhalte, behalten aber eigene Orte, Preise und Bestände. Abtrennen erhält Inhalte aller Sprachen. Serie mit Terminen lässt sich nicht löschen. Termine sind nur mit den bisherigen Event-/Ticketregeln kaufbar und scannbar. Serie ist im Admin, in CMS, Suche und Suggest separat verfügbar. Generierung über Tagesintervall oder ausgewählte Wochentage ist vorschaufähig, zeitzonenkorrekt und bei Wiederholung/Parallelität ohne Doppelanlage. Aktive und inaktive Anlage funktionieren gemäß Auswahl; eine deaktivierte Serie verhindert trotzdem die öffentliche Freigabe. Neue Migration bewahrt bestehende Daten und ist sowohl nach dem bisherigen Stand als auch bei Neuinstallation ausführbar.
