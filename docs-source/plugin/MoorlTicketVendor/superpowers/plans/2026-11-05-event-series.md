# Veranstaltungsserien Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Optionale Veranstaltungsserien mit zentralen Inhalten, eigenständigen Terminen, eigener CMS-/Suchintegration und Intervallgenerierung ergänzen.

**Architecture:** Neue Main-Entity TicketSeries neben den bestehenden TicketSale-Entities. Ein zentraler Resolver stellt gemeinsame Inhalte bereit; Ticketverkauf und Einlösung bleiben am Termin. Neue additive Migrationen bauen auf dem bisherigen Migrationsstand auf.

**Tech Stack:** PHP, Shopware 6.7 DAL/Migrationen/Symfony, MoorlFoundation, Vue-Administration, Twig, PHPUnit und Node-Test-Runner.

**Spec:** [Veranstaltungsserien](../specs/2026-11-05-event-series-design.md)

**Umsetzungsstand:** Die Erweiterung ist implementiert. Das optionale Demopaket `series` wurde separat vom Standardpaket angelegt, damit beide Pakete unabhängig entfernt werden können. Neue Einzelveranstaltungen werden zunächst gespeichert und anschließend explizit zugeordnet; die Generierung legt vollständige Serientermine direkt an. Bedienung und Upgrade: [Veranstaltungsserien](../../event-series.md).

## Global Constraints

- Bestehende Admin-Entities, Event-IDs, technische Routen und Ticketbezüge bleiben erhalten.
- seriesId ist optional; keine automatische Gruppierung bestehender Events.
- `Migration1793194127Initial` bleibt unverändert; neue native Migrationen folgen mit neuem Zeitstempel.
- Gemeinsame Inhalte kommen bei gesetzter seriesId ausschließlich aus der Serie, ohne lokale Überschreibungen.
- Datum, Ort, Tickettypen, Kapazität, Programm, Gästeliste und Einlösung bleiben am Event.
- Bestätigt: Deaktivierte Serie sperrt öffentliche Anzeige und neue Käufe ihrer Termine; bestehende Tickets bleiben abrufbar/einlösbar. Eigene Termin-active-Werte werden dabei nicht überschrieben.
- Bestätigt: Aktivierung wird beim Generieren gewählt; required active wird auf neu erzeugte Events und Tickettypen angewandt, niemals rückwirkend auf vorhandene Slots.
- Wiederholung hat zwei Modi: Tagesintervall (intervalDays) oder ausgewählte ISO-Wochentage (weekdays). Keine monatliche Wiederholung.
- Keine Commits oder Änderungen am Index ohne Benutzerauftrag (CODEX.md).
- Keine Tests/Migrationen an der laufenden Shopdatenbank; Integration nur gegen explizite `moorl_tv_*_test`-Datenbanken, kein echter Mailversand.
- Die im Entwurf als technische Vorschläge benannten Details gehören zur Prüfung dieses Plans, nicht zu bereits einzeln bestätigten Benutzerentscheidungen.

## Review Focus

- Alte lokale Eventtexte dürfen weder Anzeige noch Suchtreffer einer zugeordneten Serie beeinflussen: Tasks 2, 3, 6.
- Serienänderung muss übersetzte Inhalte, PDF/Mail und Caches erreichen, ohne historische Bestellungen umzuschreiben: Tasks 2, 3, 7.
- Winter-/Sommerzeit, Tagesintervalle/Wochentagsauswahl und wiederholte/gleichzeitige Generierung dürfen keine still verschobenen oder doppelten Termine erzeugen: Tasks 8, 9.
- Bestandsupgrade, teilweise ausgeführte DDL und Erstinstallation müssen gleiche Tabellen/FKs ergeben, ohne bestehende Inhalte zu verlieren: Task 1.
- Öffentliche Serien-/Eventbeziehungen dürfen keine privaten Tickets/Anmeldungen ausgeben und keine breiteren Scannerrechte voraussetzen: Tasks 2, 4, 5, 10.

## Bestand und Dateiverantwortung

Alle Pfade beziehen sich auf das Pluginverzeichnis. Neue Series-Dateien folgen den direkt entsprechenden TicketSale-Dateien; es werden keine bestehenden Adminmodule umbenannt.

| Bereich | Bestehender Anschluss | Neue Verantwortung |
| --- | --- | --- |
| Modell/Migration | Core/Content/TicketSale, Migration, MoorlTicketVendor.php | Core/Content/TicketSeries, additive Migration |
| Gemeinsamer Inhalt | TicketSaleController, TicketSaleListing, Cart/Document/Delivery | Core/Service/EventContentResolver und unveränderliche Präsentationskopien |
| Admin | module/moorl-tv-sale, module/index.js | module/moorl-tv-series, Serienauswahl/Vorschau am Event |
| CMS | Data/CmsPage, module/sw-cms, TicketSale/Cms | TicketSeries/Cms und eigene Seiten/Elemente |
| Suche | TicketSaleListing, TicketSaleSearchRoute | TicketSeriesListing, gemeinsame Content-Suchkriterien |
| SEO/Cache | TicketSaleSeoUrlRoute/Indexer, StorefrontCacheSubscriber | TicketSeriesSeoUrlRoute/Indexer und Invalidierung abhängiger Events |
| Generierung | Administration/Controller, DalWriteStorageReader | TicketSeriesGenerationController, Planer und transaktionaler Generator |

## Task 1: Additives Schema und DAL-Modell

**Create:** `src/Core/Content/TicketSeries/TicketSeries{Definition,Entity,Collection}.php`, `TicketSeriesTranslation{Definition,Entity,Collection}.php` im selben Ordner; `src/Migration/Migration<nativer Zeitstempel>EventSeries.php`; `src/Resources/config/series.xml`; `tests/Integration/EventSeriesMigrationTest.php`, `tests/Unit/EventSeriesDefinitionTest.php`.

**Modify:** `src/Core/Content/TicketSale/TicketSale{Definition,Entity}.php`, `src/Core/Extension/CmsPageExtension.php`, `src/MoorlTicketVendor.php`, `src/Resources/config/services.xml`, `tests/Unit/InitialMigrationTest.php`, `tests/Integration/TicketMigrationTest.php`, `tests/PluginMigrations.php`, Schemaaudits mit festen Tabellenzahlen.

**Interfaces:** Entity `moorl_tv_ticket_series`; TicketSale `getSeriesId(): ?string`, `getSeries(): ?TicketSeriesEntity`, `getGenerationKey(): ?string` samt Settern; TicketSeries `getSales(): ?TicketSaleCollection`. Native Repository-ID `moorl_tv_ticket_series.repository`.

- [ ] Tests zuerst: `testExistingEventSurvivesUpgradeWithoutSeries`, `testFreshInstallAndUpgradeProduceIdenticalSchema`, `testMigrationCanResumeAfterSeriesTablesWereCreated`, `testSeriesDeletionIsRestrictedWhileEventsExist`, `testCmsPageDeletionIsRestricted`, `testUnlinkedEventsAllowMultipleNullGenerationKeys` und `testGeneratedSlotIsUniqueWithinSeries`. Vorhandene Beispieldaten vor/nach dem Upgrade inklusive Ticket-IDs/Tokens vergleichen.
- [ ] Rotlauf der neuen Tests in einer isolierten Datenbank dokumentieren. Erwartet: fehlende Entity/Spalten, nicht Verbindungsfehler.
- [ ] Native Migration über `bin/console database:create-migration --plugin MoorlTicketVendor --name EventSeries` bei Umsetzung erzeugen. Nur neue Datei bearbeiten; Schema und Flags wie im Entwurf, neue Tabellen vor den Sale-FKs registrieren. Initialmigration isoliert gegen ihren historischen Stand testen; Gesamtstand über alle Migrationen prüfen.
- [ ] Uninstall-Tabelle in FK-gültiger Reihenfolge ergänzen; `series.xml` importieren, Entity und Übersetzungen registrieren. TicketSeriesDefinition implementiert EntityAutoCacheInterface mit START_TIME=show_from, END_TIME=show_until, ACTIVE=active und den betroffenen CMS-Typen; `moorl.foundation.entity_auto_cache`-Tag registrieren. Keine Migration gegen den laufenden Shop starten.
- [ ] Grünlauf: `php vendor/bin/phpunit -c custom/plugins/MoorlTicketVendor/phpunit.xml.dist --filter 'EventSeriesMigrationTest|EventSeriesDefinitionTest|InitialMigrationTest|TicketMigrationTest'` aus dem Shoproot mit isolierter DB-Umgebung. Erwartet: neue und historische Prüfungen bestehen.

## Task 2: Effektive Inhalte und sichere Serienzuordnung

**Create:** `src/Core/Service/EventContentResolver.php`, `src/Core/Service/EventSeriesAssignmentService.php`, `src/Core/Subscriber/EventSeriesAssignmentSubscriber.php`, `src/Administration/Controller/TicketSeriesAssignmentController.php`, `tests/Unit/EventContentResolverTest.php`, `tests/Integration/EventSeriesAssignmentTest.php`.

**Modify:** `src/Resources/config/series.xml`, betroffene Event-Readonly-Projektion im Admin, optional gemeinsame Hilfs-Struct unter `src/Core/Content/TicketSale/`.

**Interfaces:** `EventContentResolver::resolve(TicketSaleCollection $sales, Context $context): TicketSaleCollection` liefert Kopien mit wirksamen gemeinsamen Feldern; `EventSeriesAssignmentService::assign(string $saleId, ?string $seriesId, Context $context): void` erledigt zuordnen/wechseln/abtrennen. Der Subscriber validiert Verknüpfungsänderungen: nur vollständig vorbereitete Übernahmen zulassen, rohe Abtrennung ohne die Inhaltsübernahme abweisen. Import-/Sync-Adapter verwenden für diesen Vorgang denselben Service; keine verschachtelten Repository-Writes aus PreWriteValidationEvent starten. HTTP `POST /api/_action/moorl-tv/event/{saleId}/series` mit `{seriesId: UUID|null}`.

- [ ] Tests zuerst: `testStandaloneContentIsUnchanged`, `testLinkedEventIgnoresOldLocalContentEvenForEmptySeriesFields`, `testSeriesLanguageFallbackDoesNotUseLocalEventTranslation`, `testResolutionDoesNotMutateRepositoryEntities`, `testResolvingManyEventsLoadsSeriesInOneBatch`.
- [ ] Integrationstests zuerst: Abtrennen kopiert gemeinsame Werte aller vorhandenen Serien-Sprachen, bereinigt gemeinsame Alttexte in lokalen-only Sprachdatensätzen und erhält lokale Orts-/Gästelistentexte sowie Event-/Ticket-IDs; Wechsel leert generationKey; rohe DAL-Abtrennung ohne Übernahmeprozess wird abgewiesen. Fehlendes Serienleserecht/fehlendes Event-update verhindert Zuordnung. Gleichzeitige Serienänderung/Abtrennung liefert konsistenten Stand oder Retry.
- [ ] Rotlauf, dann Resolver und Zuordnungsregeln implementieren. Beim Abtrennen alle gemeinsamen Felder pro Sprache der Vereinigungsmenge aus Event/Serie als sprachlich aufgelösten Snapshot setzen, nie name=NULL schreiben. Pflichtname beim Neuanlegen mit Serie durch lokalen Snapshot erfüllen; API-Fehler liefern verständliche Validierung. Keine automatischen Inhaltssynchronisierungen zu allen Events und keine globalen JSON-Encoder-Änderungen.
- [ ] Begrenzte öffentliche Inhaltsprojektion für berechtigt gelesene Events definieren; nur öffentliche gemeinsame Felder in Adminvorschau/Scanner, kein allgemeines Serienrepository für Scanner öffnen.
- [ ] Grünlauf mit Filter `EventContentResolverTest|EventSeriesAssignmentTest|ScannerRoleTest|TicketStoreApiPrivacyTest`. Ausführungskontext wie Task 1.

## Task 3: Bestehende Event-Leser auflösen

**Modify:** `src/Storefront/Controller/TicketSaleController.php`, `src/Core/Content/TicketSale/SalesChannel/TicketSaleListing.php`, alle drei bestehenden `src/Core/Content/TicketSale/Cms/*Resolver.php`, `src/Core/Checkout/Cart/TicketCartProcessor.php`, `src/Core/Checkout/Cart/TicketPurchaseValidator.php`, `src/Core/Service/TicketDocumentService.php`, `src/Core/Service/TicketDeliveryService.php`, `src/Core/Service/EventStructuredDataBuilder.php`, `src/Storefront/Controller/TicketAccountController.php` (Index und Deeplink-single), `src/Storefront/Controller/TicketDownloadController.php`, `src/Core/Content/Ticket/TicketAccess.php` für die benötigten Associations; zugehörige DI-Dateien und Twig-Ausgaben.

**Test:** `tests/Integration/EventSeriesContentTest.php` neu; vorhandene `tests/Unit/TicketPurchasePresentationTest.php`, `TicketMailDataTest.php`, `EventStructuredDataTest.php` und Document-/Account-/Deeplinktests erweitern.

**Interfaces:** Konsumiert Resolver aus Task 2. Öffentliche Verfügbarkeit erweitert bestehende Eventregeln um Serien-active/showFrom/showUntil; weder Preis noch Bestand werden aus Serien bezogen.

- [ ] Tests zuerst: Zwei Termine übernehmen denselben neuen Serientitel/Bild in Detail, CMS, Warenkorb, PDF und Mail, aber unterschiedliche Orte/Zeiten/Preise. Historische Bestellpositionen behalten saleName und Metadaten; bereits verschickte Tickets werden nicht erneut gesendet.
- [ ] Tests zuerst: Deaktivierte Serie verhindert neuen Kauf/öffentliche Termindetails, erlaubt weiterhin berechtigten PDF-/Kontozugriff und Einlösung bestehender Tickets. Event-active bleibt unverändert; Reaktivierung der Serie respektiert die individuellen Freigaben. Einzelevent funktioniert ohne geladenen Parent. Reihenfolge der Sprachauflösung entspricht tatsächlicher Empfängersprache.
- [ ] Rotlauf; alle Loader gebündelt um benötigte Serien/Medien erweitern oder den Resolver-Batch nutzen. Präsentationskopien nie persistieren. Eventverfügbarkeit über einen gemeinsam genutzten Serienfilter bzw. PurchaseValidator prüfen, nicht nur im Twig verstecken.
- [ ] Grünlauf der neuen Tests und bestehender Präsentations-/Cart-/Mail-/Privacytests. Erwartet: unveränderte IDs und Kontingentberechnung, überall gleiche aufgelöste Inhalte.

## Task 4: Serienmodul und Event-Zuordnung in der Administration

**Create:** `src/Resources/app/administration/src/module/moorl-tv-series/index.js`; `src/Resources/app/administration/src/component/moorl-tv-series-content/{index.js,index.html.twig}`; `src/Resources/app/administration/src/component/moorl-tv-scanner-event-select/index.js` analog zum bestehenden Scanner-Ticketselect; `src/Resources/app/administration/src/service/ticket-series-api.service.js`; `tests/administration/event-series.test.mjs`.

**Modify:** `src/Resources/app/administration/src/module/index.js`, `module/moorl-tv-sale/index.js`, `component/index.js`, `init/acl.init.js`, `snippet/{de-DE,en-GB}.json` unter demselben Adminroot; Scannerseite und `service/ticket-api.service.js`; Backend `src/Administration/Controller/TicketRuntimeController.php`. Serienauswahl und terminspezifische Felder in vorhandene Foundation-Formulare integrieren.

**Interfaces:** Foundation-Modul `moorl-tv-series`, Entity `moorl_tv_ticket_series`, Seitentyp `moorl_tv_ticket_series_detail`; API-Service `assign(saleId, seriesId)` nutzt Task 2. Termintabellenkriterium exakt `seriesId = aktuelle Serien-ID`. `TicketActions::searchEvents(term, page=1)` nutzt den neuen begrenzten `/scanner/events`-Endpunkt mit dem Resolver aus Task 2; bestehender UTC-Cutoff von drei Tagen, aktive Events und maximal 25 Ergebnisse pro Seite serverseitig erzwingen.

- [ ] Node-Tests zuerst: Module registriert, bestehende Module weiterhin erreichbar, neue/leere Serie zeigt keine fremden Termine; Serienauswahl optional; Inhalte mit Serie readonly und ohne Serie editierbar; Abtrennen erklärt Inhaltsübernahme und ruft die Aktion einmal auf.
- [ ] Node-Tests zuerst: Nicht ausreichende Rechte blenden schreibende Aktionen aus; abgewiesener API-Aufruf zeigt konkrete Fehlermeldung und lässt Zuordnung unverändert. Eventlabels kombinieren effektiven Namen, Datum und Ort. Scanner-Eventselect lädt ausschließlich seine begrenzte Projektion und braucht kein Serien-read; API-Test mit den tatsächlichen Scannerrollenrechten, Pagination und altem lokalen Namen ergänzen.
- [ ] Rotlauf: `node --test custom/plugins/MoorlTicketVendor/tests/administration/event-series.test.mjs` vom Shoproot; danach Modul, Vorschau, Aktionen und DE/EN-Snippets implementieren, mit vorhandenen Foundation-Helpern.
- [ ] Grünlauf: neuer Test sowie `components.test.mjs`, `scanner-component.test.mjs` und `scanner-ticket-select.test.mjs`. Scannerrechte gegen Backend zusätzlich mit ScannerRoleTest prüfen.

## Task 5: Eigene Seriendetailseite und CMS-Elemente

**Create:** `src/Storefront/Controller/TicketSeriesController.php`; `src/Core/Content/TicketSeries/Cms/TicketSeries{Detail,Listing,StaticListing,Dates}CmsElementResolver.php`; `src/Core/Content/TicketSeries/SalesChannel/TicketSeriesListing.php`; `src/Resources/views/storefront/page/ticket-series/detail.html.twig`; die vier `cms-element-moorl-tv-ticket-series-{detail,listing,static-listing,dates}.html.twig` unter `src/Resources/views/storefront/element/`; Serienkarten/-Terminlisten unter `src/Resources/views/storefront/component/ticket-series/`.

**Modify:** `src/Resources/config/series.xml`, `src/Resources/config/config.xml`, `src/Resources/app/administration/src/module/sw-cms/index.js`, neues Serienmodul für Foundation-Listingregistrierung, `src/Data/CmsPage/DataCmsPage.php`, `src/Data/CmsPage/content/cms_page.json`, `src/MoorlTicketVendor.php`, Storefront- und Admin-Snippets.

**Test:** `tests/Integration/EventSeriesStorefrontTest.php`, `tests/Unit/EventSeriesCmsTest.php`, `tests/administration/event-series-cms.test.mjs` neu.

**Interfaces:** `frontend.moorl.tv.series.detail` mit seriesId; CMS-Typen exakt wie im Entwurf. Dates-Element: aktuelle Serie aus EntityResolverContext oder statische seriesId, Criteria nach seriesId mit Limit max. 100, Standard 12, Sortierung startAt/id. Serienkarten laden Termine als gebündelte Vorschau, nicht unbeschränkt über sales.

- [ ] Tests zuerst: ID ungültig/unbekannt/inaktiv außerhalb Freigabe ergibt 404; richtiges Serienlayout/Slotconfig und Verkaufskanal-Fallback werden geladen; Standardlayout enthält genau eine H1 und Terminliste.
- [ ] Tests zuerst: Dates-Resolver ohne gültigen Kontext liefert leere Daten, listet keine fremden Events und serialisiert keine privaten Relationen. Pagination bleibt auch bei null Treffern korrekt; direkter Serienaufruf ohne kommende Termine zeigt Leerezustand.
- [ ] Tests zuerst: dynamische und statische Listings respektieren ihre unterschiedlichen Archivregeln; CMS-Installer erhält Händlerlayouts bei Wiederholung. Event-CMS-Seitentyp bleibt unverändert.
- [ ] Rotlauf; Controller/Resolver/Templates/Registrierung und zwei neue CMS-Seiten implementieren. Eigene IDs einmalig festlegen, keine existierenden Seiten umwidmen. `seriesCmsPageId` mit passendem Seitenfilter ergänzen.
- [ ] Grünlauf der neuen Tests und `DataPackageTest|StaticEventListingTest|PresentationAccessTest`; Node-CMS-Test aus Shoproot ausführen.

## Task 6: Serien- und Terminsuche samt Suggest

**Create:** `src/Core/Service/EventContentSearchCriteria.php`; `src/Resources/app/administration/src/helper/event-content-search.helper.js` und `src/Resources/app/administration/src/extension/moorl-tv-sale-list/index.js`; `src/Resources/views/storefront/page/search/search-moorl-tv-ticket-series-listing.html.twig`; `src/Resources/views/storefront/layout/header/search-suggest-moorl-tv-ticket-series-listing.html.twig`; `tests/Unit/EventSeriesSearchTest.php`, `tests/Integration/EventSeriesSearchIntegrationTest.php`.

**Modify:** `TicketSeriesListing.php` aus Task 5, `src/Core/Content/TicketSale/SalesChannel/TicketSale{Listing,SearchRoute}.php`, `src/Resources/config/series.xml`, `src/Resources/config/config.xml`, Eventlisten-/Select-Suchkriterien in den Plugin-Adminmodulen, nicht Foundation global.

**Interfaces:** `EventContentSearchCriteria::apply(Criteria $criteria, string $term): void` für TicketSale; gleiches Kriterienformat in JS als `applyEventContentSearch(criteria, term)`. Löst den term in Datenbankfilter auf und leert den ursprünglichen DAL-term; lokale Inhalte nur bei seriesId=NULL, Serieninhalte nur bei seriesId!=NULL. Die JS-Extension überschreibt ausschließlich `moorl-tv-sale-list.itemCriteria` auf Grundlage des Foundation-$super-Kriteriums und wird im bestehenden extension/index.js registriert. SeriesListing-Titel `moorl-tv-ticket-series-listing`, Such-/Suggest-Tags wie bisher; Configkeys `seriesSearchActive`, `seriesSearchLimit`, `seriesSuggestActive`, `seriesSuggestLimit`, optionale `seriesSearchConfig*`/`seriesSuggestConfig*` analog Bestand. `TicketSeriesListing::getConfig(string $key): mixed` bildet generische Foundation-Keys auf diese Serienkeys mit passendem bool/int/JSON-Verhalten ab; unbekannte nicht serienbezogene Keys delegieren an parent.

- [ ] Tests zuerst: geänderter Serientitel findet Serie und zugehörige Events; alter lokaler Name eines zugeordneten Events trifft nicht; lokaler Name eines Einzelevents trifft weiterhin; Suche nach Ort findet nur passende Termine; Mehrwortsuche und Sprach-Fallback funktionieren.
- [ ] Tests zuerst: getrennte Trefferzahlen, Grenzwerte 1–100, Such-/Suggest-Deaktivierung und Seite 2 bei weniger Produkttreffern funktionieren auf beiden Tabs. Die generischen Foundation-getConfig-Abfragen müssen nachweislich Serienkonfiguration und nicht die Eventkeys lesen. Öffentliche Filter greifen vor Gesamtzählung und Pagination. Eigene Tabnavigation erhält search und tab korrekt.
- [ ] Rotlauf; Serienlisting registrieren und vorhandene Paginationkorrektur für beide Tabnamen erweitern. Adminlisten und Eventselects erzeugen dieselben effektiven Inhaltsfilter. Keine neue externe Suchinfrastruktur und kein nachträgliches Aussortieren bereits paginierter Treffer.
- [ ] Grünlauf der neuen Tests sowie `TicketSaleListingTest|TicketSaleStaticListingTest` und Node-Tests zu Eventlisten/Selects.

## Task 7: SEO, Cache, Datenpakete und Lifecycle

**Create:** `src/Storefront/Framework/Seo/TicketSeriesSeoUrlRoute.php`, `src/Core/Content/TicketSeries/SalesChannel/TicketSeriesSeoIndexer.php`, `tests/Integration/EventSeriesSeoCacheTest.php`.

**Modify:** `src/Storefront/Framework/Seo/TicketSaleSeoUrlRoute.php`, `src/Core/Content/TicketSale/SalesChannel/TicketSaleSeoIndexer.php`, `src/Storefront/Subscriber/StorefrontCacheSubscriber.php`, `src/Data/Seo/DataSeo.php`, `src/Data/content/{media_default_folder,import_export_profile}.json`, `src/Resources/config/{seo,series}.xml`, `src/Resources/installation/{de-DE,en-GB}.json`, PLUGIN_TABLES und Lifecycle-Löschreihenfolge.

**Interfaces:** Serien-SEO-Template aus dem Entwurf; SeriesIndexer stößt zusätzlich Event-SEO-Aktualisierung der betroffenen seriesId an, in begrenzten Batches. Cache bleibt auf dem vorhandenen `moorl-tv-storefront`-Tag, inklusive Serienübersetzungen.

- [ ] Tests zuerst: eigene Seriencanonical und eigenständige Eventcanonical, alter Event-SEO-Link bleibt gültig; Änderung der Serienübersetzung invalidiert warme Serien-, Event-, Such- und zuvor leere Listingseiten. Ohne Write über showFrom/showUntil hinaus fortgeschaltete Uhr muss dieselben warmen Seiten korrekt freigeben/sperren (Foundation-Live-/Scheduled-Prüfung einbeziehen). Preis-/Bestandsänderung am Termin aktualisiert abhängige Serienvorschau.
- [ ] Tests zuerst: SEO- und CMS-Installer erhalten vorhandene Händleranpassungen; separate Serienimportprofile werden neu angelegt; Eventprofile ohne seriesId bleiben lauffähig; keepUserData erhält Serien, vollständige Entfernung löscht in gültiger Reihenfolge.
- [ ] Rotlauf; Indexer/Route/Cache und Datenpakete implementieren. Serienschreibvorgang darf keine Endlosschleife von Eventwrites auslösen; Inhalte werden nicht materialisiert. Domain und Sprache aus bestehendem SEO-Kontext verwenden.
- [ ] Grünlauf mit `EventSeriesSeoCacheTest|SeoPresentationTest|DataPackageTest|StorefrontCacheTest|EventStructuredDataTest`.

## Task 8: Deterministischer Intervallplaner

**Create:** `src/Core/Service/EventSeriesSchedulePlanner.php`, `src/Core/Content/TicketSeries/Generation/{ScheduleRequest,SchedulePlan,ScheduleSlot}.php`, `tests/Unit/EventSeriesSchedulePlannerTest.php`.

**Interfaces:** `EventSeriesSchedulePlanner::plan(ScheduleRequest $request, string $timezone, ?int $durationSeconds): SchedulePlan`; Slot enthält localStart, UTC-Beginn/-Ende und generationKey. ScheduleRequest hat mode (`interval` oder `weekdays`), nur bei interval intervalDays (1–365), nur bei weekdays eine nicht leere eindeutige ISO-Wochentagsliste (1–7), außerdem lokaler Startbeginn, seriesId, templateSaleId, required active und genau eines von count/until. Weitere Grenzen entsprechen dem Entwurf; kein Datenbankwrite im Planer.

- [ ] Tests zuerst: intervalDays=1/3/14, Startdatum als erster Slot; weekdays=[1,4] liefert Montag/Donnerstag mit gleicher Uhrzeit, einschließlich Wochenwechsel und erster Treffer erst nach Startdatum. count/until exklusiv, until inklusive, maximal 250 Slots und fünf Jahre; Tagesintervall über 31.01./29.02./Jahreswechsel ohne Sonderregel. Wochentag 19 Uhr bleibt über Sommerzeit hinweg lokal 19 Uhr.
- [ ] Tests zuerst: ungültige/doppeldeutige lokale Uhrzeit Europe/Berlin, ungültige IANA-Zone, unbekannter Modus, intervalDays=0, leere/doppelte/außerhalb 1–7 liegende weekdays, Modus mit unpassendem Zusatzfeld, fehlendes oder nicht boolesches active, beide/kein Endkriterium und negative Dauer liefern Validierungsfehler. Leerer Wochentagsbereich erzeugt keine Slots. Endzeit bewahrt verstrichene Dauer oder NULL.
- [ ] Rotlauf; lokale Kalenderrechnung mit expliziter Prüfung des Offsets/Roundtrips implementieren. Request normalisieren und stabile generationKeys nach Spezifikation erzeugen; Fehler auf einzelne Eingabefelder beziehen.
- [ ] Grünlauf: `php vendor/bin/phpunit -c custom/plugins/MoorlTicketVendor/phpunit.xml.dist --filter EventSeriesSchedulePlannerTest` ohne Datenbank erforderlich.

## Task 9: Vorschau und transaktionale Generierung

**Create:** `src/Core/Service/EventSeriesGenerationService.php`, `src/Administration/Controller/TicketSeriesGenerationController.php`, `tests/Integration/EventSeriesGenerationTest.php`, `tests/administration/event-series-generation.test.mjs`; Admincomponent `src/Resources/app/administration/src/component/moorl-tv-series-generator/{index.js,index.html.twig}`.

**Modify:** `src/Resources/config/series.xml`, `src/Resources/app/administration/src/service/ticket-series-api.service.js`, Serienmodul, Komponentenregistrierung und Snippets; `tests/support/concurrency-worker.php` für parallele Generatoranfragen.

**Interfaces:** `preview(ScheduleRequest $request, Context $context): array` und `generate(ScheduleRequest $request, string $previewHash, Context $context): array` am GenerationService. HTTP POST `/api/_action/moorl-tv/series/{seriesId}/schedule/preview` und `/generate`; Request enthält Modus, Terminregel und boolesches active gemäß Task 8, keine clientseitigen Typdaten. Antwort: slots/previewHash samt gewähltem active und wirksamer Serienfreigabe oder createdIds/skippedSlots. Konflikt veralteter Vorschau HTTP 409; ungültige Eingaben HTTP 400, fehlende Rechte HTTP 403.

- [ ] Tests zuerst: Vorschau schreibt nichts; zweimalige gleiche Generierung und zwei parallele Anfragen erzeugen insgesamt genau einen Eventdatensatz pro Slot. Wiederholung mit anderem Modus oder active erzeugt dieselben Slots nicht erneut und verändert keine bestehenden Termine. Geänderter Mustertermin/Typ, Eingabemodus/Aktivierungswahl oder Serienfreigabe nach Vorschau führt zu 409 ohne Teilanlage. Fehlender Mustertermin, falsche Rechte, leere Vorschau und ungültige Slotfenster erzeugen keine Daten.
- [ ] Tests zuerst: neue Event-/Typ-IDs, active=true und active=false werden jeweils explizit auf alle neuen Events/Typen angewandt; quantitySold=0, NULL/verschobene Freigabefenster. Aktiv anlegen bei deaktivierter Serie ändert nicht deren Freigabe und öffnet keinen Verkauf. Keine kopierten Tickets/Bestellungen/Kunden/Check-ins/Anmeldungen/Programmobjekte und keine wiederverwendeten Gästelistengeheimnisse. Manuelle gleichzeitige Termine bleiben unangetastet; verschobene generierte Slots werden bei Wiederholung nicht neu erzeugt.
- [ ] Rotlauf; Service mit DAL-Schreibzugriffen in einer DB-Transaktion implementieren. Reihenfolge `order → bestehende sales (ID-sortiert) → series (ID-sortiert) → types (ID-sortiert) → tickets` einhalten; Generator sperrt Muster-sale vor Serie, Zuordnung sale vor alter/neuer Serie. Keine schreibenden Eventlocks nach einem reinen Serieswrite. Nach Vorablesen die Zuordnung unter Locks erneut prüfen; Paralleltest Generierung/Typänderung/Zuordnungswechsel ergänzen. Vorschauhash aus normalisiertem Request und den exakten Kopierfeldern des Entwurfs berechnen; nach dem Sperren neu prüfen.
- [ ] Node-Tests zuerst: Auswahl Intervall in Tagen oder Wochentage blendet passende Pflichtfelder ein; Aktiv/Inaktiv muss beim Generieren gewählt sein. Vorschau zeigt Termine, vorhandene Slots, Aktivierungswahl und gesperrte Serienfreigabe; Anlegen erst nach nicht leerer erfolgreicher Vorschau. Modus-, Wochentags- oder Aktivierungsänderung verwirft Hash; Doppelklick gesperrt; 409 fordert neue Vorschau an. Danach Modal/Formular und API-Service implementieren.
- [ ] Grünlauf Integration/Node; Paralleltest bestätigt Transaktion/Unique-Index statt nur sequenzieller Idempotenz. Keine Testtickets aus realen Events kopieren.

## Task 10: Gesamtintegration, Dokumentation und Übergabe

**Modify:** `CODEX.md`, `docs/schema.md`, `docs/runtime.md`, `docs/index{,.en}.tpl.md` sowie daraus erzeugte Ausgaben nach Repositoryworkflow; neue Serien-Demodaten im bestehenden Standardpaket nur additiv.

**Test:** `tests/Integration/EventSeriesAcceptanceTest.php` neu; bestehende Scanner-, Checkout-, Store-API-Privacy- und Bestelltests einbeziehen.

- [ ] Abnahmetest zuerst: Einzelevent plus Serie mit zwei Orten und unterschiedlichen Ticketpreisen anlegen; Serie ändern; beide Termine finden, buchen und ausschließlich am richtigen Termin scannen. Serie deaktivieren und Bestandskundenzugriff prüfen; einen Termin abtrennen und danach unabhängig bearbeiten.
- [ ] Testinstallation auf leerer isolierter DB und Upgrade einer isolierten Kopie des vorherigen Schemas vergleichen. Nur sachlich benötigte Schemaabweichungen zulassen; Wiederholung muss Daten erhalten. Die ursprüngliche Migrationsdatei über Gitdiff als unverändert nachweisen.
- [ ] PHP-Gesamtsuite: `php vendor/bin/phpunit -c custom/plugins/MoorlTicketVendor/phpunit.xml.dist` mit ausdrücklich ausgewählter Testdatenbank. Node-Gesamtsuite: `node --test custom/plugins/MoorlTicketVendor/tests/administration/*.test.mjs` vom Shoproot. Danach Container-/Twig-/Admin-Build mit den tatsächlich im Projekt vorhandenen Buildbefehlen prüfen, keine neuen Toolchains einführen.
- [ ] Im Browser Foundation-Formulare, Serie/CMS-Vorschau, Sprachwechsel, Suche/Suggest, Pagination und Generierungsmodal prüfen. Kein echter Mailversand. Der Scanner wird mit dem bestehenden eingeschränkten Rechtssatz getestet.
- [ ] Doku auf neue additive Migrationen und optionale Zuordnung aktualisieren; alte „keine neuen Migrationen“-Vorgaben für diese Erweiterung ausdrücklich ersetzen. Tagesintervall-/Wochentags-/DST-Regeln, wählbare Aktivierung generierter Events und Inhaltsübernahme beim Abtrennen erklären.
- [ ] Abschließender Diff-/Anforderungsabgleich und Review vor Umsetzungsauslieferung. Kein Commit, Push, Deployment oder Ausführen am Produktivbestand ohne entsprechenden Auftrag.

## Ausführungshinweise

Dieser Plan führt keine der aufgeführten Implementierungsschritte aus. Die Skizze ist als zusammenhängende Erweiterung in zehn prüfbare Aufgaben aufgeteilt. Migration/DAL kommen zuerst, darauf folgen Inhalt, Admin/CMS/Suche und Generierung. Review-Schwerpunkt sind die Schnittstellen zwischen diesen Bereichen.

Die bekannten lokalen PHP-/Containerstände vor Umsetzung erneut prüfen. Historische Testumgebungen können eine ältere aktive Foundation-Version enthalten; die reguläre Pluginvoraussetzung muss erfüllt sein, statt die Schutzprüfung zu umgehen. Testbefehle erst mit gültiger isolierter Datenbank und aktivem Plugin bewerten.
