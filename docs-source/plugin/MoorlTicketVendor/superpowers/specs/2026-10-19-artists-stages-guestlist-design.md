# Artists, Stages, Timetable und geheime Gästeliste

Stand: 19.10.2026. Vom Benutzer zur Umsetzung freigegeben, einschließlich direktem Bestellbezug und der folgenden Booking-Präzisierung.

## Ziel und Leitentscheidungen

MoorlTicketVendor erhält Artist-Profile, eventbezogene Stages und Auftritte sowie ein geheimes Gästelistenformular mit manueller Ticketfreigabe und automatischer Zustellung. Zugleich wird das bestehende Ticketmodell vereinfacht: Ein gekauftes Ticket gehört künftig direkt zur Bestellung, die gespeicherte Bestellpositionszuordnung entfällt.

Geprüft wurden die aktuellen Definitionen, Foundation-Helfer, Administration, Checkout, TicketLifecycleService, TicketInventorySubscriber, TicketAccess, Personalisierung, Scanner, Flow-Aktion, Versand, Deeplinks, Schemahelfer und vorhandene Tests. Das Referenzformular unter https://sidequest33.com/de/gaesteliste wurde am 19.10.2026 lesend ausgewertet. Produktcode, Datenbank, Git-Index und bestehende Benutzeränderungen bleiben in dieser Planungsrunde unberührt.

Entscheidungen für den ersten Ausbau:

- Vier neue fachliche Entities: Artist, Stage, Performance und GuestlistEntry.
- Globale Artists, Stages direkt am Event, beliebig viele Auftritte eines Artists.
- Keine separaten Aktiv-Schalter an Artist, Stage und Auftritt. Veröffentlichung von Line-up und Zeiten wird am Event gesteuert.
- bookingEnabled steuert ausschließlich das öffentliche Booking-Angebot des Artists. Anfragen laufen über das vorhandene Kontaktformular, alternativ über einen optionalen externen Bookingkontakt; kein eigener Bookingprozess.
- Eine optionale interne Gagenangabe mit Währung und Booking-Notiz. Kein zweiter Buyout-Betrag ohne konkreten Bedarf.
- Kleines festes Gästelistenformular, konfigurierbare Ehrenämter, keine allgemeine Formular-Engine.
- Mehrere Gäste dürfen dieselbe E-Mail-Adresse verwenden. Technische Wiederholungen werden anhand einer Anfrage-ID erkannt.
- Bestehende Ticket-, Kontingent-, PDF-, Mail-, Retry- und Scannerlogik weiterverwenden.
- Ein geheimer Formularlink kann mit passendem Adminrecht erneut kopiert und rotiert werden.
- Optionales Gesamtkontingent am Event schützt vor Überbelegung über mehrere Tickettypen hinweg.

## 1. Kritische Bewertung des bestehenden Ticketmodells

### Bestellposition durch direkten Bestellbezug ersetzen

Die Positionszuordnung ist aktuell technisch verwendet, aber für die vorhandene Fachlogik keine notwendige dauerhafte Beziehung:

| Aktueller Zweck | Künftige Lösung |
|---|---|
| Ticket der Bestellung zuordnen | Nullable orderId mit nativer orderVersionId |
| Zahlung, Storno, Fristablauf | Direkt über die Bestellung |
| Versandgruppen, Sprache und Verkaufskanal | Direkt über die Bestellung |
| Kundenberechtigung und Bestellkunden-Snapshot | order.orderCustomer |
| Doppeltes Ausstellen verhindern | Eindeutige Einheit pro Bestellung und Tickettyp |
| Admin-Bestellreiter und Bestellnummer | Direkter Filter auf orderId und order.orderNumber |

Konkrete Codebelege: TicketLifecycleService::issueOrder erzeugt die bisherige Kombination aus Position und unitIndex; settleOrder und expire arbeiten fachlich auf Bestellungsebene. TicketDeliveryService und TicketDeeplinkService verwenden die Position nur zum Laden der Bestellung. TicketAccess, TicketPersonalizationService, TicketInventorySubscriber und die Adminfilter müssen mit umgestellt werden. Eine automatische positionsbezogene Teilstornierung/-erstattung existiert derzeit nicht.

Zielmodell am Ticket:

- Entfernen: orderLineItemId, orderLineItemVersionId und Association orderLineItem.
- Ergänzen: nullable orderId, orderVersionId mit nativem Live-Default und Association order.
- Beibehalten: unitIndex als rein internes, nach Erstellung unveränderliches Ordnungsmerkmal innerhalb eines Tickettyps der Bestellung.
- Neuer Unique-Key: (order_id, order_version_id, moorl_tv_ticket_type_id, unit_index).
- Bei Tickets ohne Bestellung bleibt orderId NULL; mehrere manuelle/Gästetickets mit unitIndex 0 bleiben zulässig.
- orderId ist ein automatisch gesetzter Herkunftsbezug, keine frei editierbare Bestellzuweisung im Ticketformular.
- Entfernen der OrderLineItemExtension und Ersetzen durch eine OrderExtension für den inversen Löschschutz. Bestellungsversionierung nach dem installierten DAL-/Foundation-Muster berücksichtigen.

Beispiel: Zwei Bestellpositionen enthalten denselben Tickettyp mit Mengen 2 und 3. Die Ausstellung aggregiert auf fünf Tickets dieses Typs, mit unitIndex 0 bis 4. Dafür wird keine Positions-ID am Ticket benötigt. Bestellpositionen bleiben als normale Shopware-Kaufdaten und als Eingabe für die Ermittlung von Typen, Mengen und Preisen erhalten.

Ausstellung muss weiterhin unter Bestellungssperre und gemeinsam mit der nativen Bestellspeicherung atomar erfolgen. Bereits ausgestellte Tickets werden unabhängig von gültig, widerrufen oder abgelaufen als vorhandene Ausstellungen erkannt. Wiederholung mit derselben Ticketmenge liefert dieselben IDs. Ein späterer Aufruf mit abweichenden Mengen oder Tickettypen führt zu einem nachvollziehbaren Konflikt statt stiller Neuerstellung. Nachträgliche Bestellbearbeitung wird damit nicht unbemerkt zu einem zweiten Ticketauftrag. Bestellgebundene Tickets dürfen nicht hart gelöscht werden, solange die Ausstellung wiederholt werden kann.

Grenze der Vereinfachung: Positionsbezogene automatische Teilrückerstattung und Nachweis unterschiedlicher Einzelpositionspreise je konkretem Ticket sind damit kein Bestandteil des Modells. Finanzielle Originaldaten bleiben in Shopwares Bestellung und Positionen. Eine spätere solche Funktion müsste den Zuordnungsbedarf neu bewerten.

### Was im Bestand erhalten bleibt

| Feld / Funktion | Begründung |
|---|---|
| saleId und typeId | Das Event ist der direkte fachliche Zugriff; der Typ bestimmt Kategorie und Kontingent. Übereinstimmung weiterhin im DAL prüfen. |
| customerId | Kundenkonto-/Eigentümerzuordnung und bewusste Übertragung; ist nicht dasselbe wie eine Empfängeradresse. |
| recipientEmail | Ermöglicht Zustellung ohne Kunde oder Bestellung und abweichende Empfänger. |
| attendeeName und attendeePhone | Daten der teilnehmenden Person, unabhängig vom Käufer. |
| Ticketnummer, QR-token und deeplink | Unterschiedliche Aufgaben: lesbare Referenz, Einlass, persönliche Onlineverwaltung. Keine Zusammenlegung, die einen Einlasscode zum Verwaltungszugang macht. |
| Ticketstatus und Versandstatus | Eintrittsberechtigung und Mailzustellung sind unabhängig. |
| quantitySold | Geschützter abgeleiteter Zähler für Verfügbarkeit und Kontingentprüfung; kein frei pflegbarer Bestand. |
| expiresAt | Zahlungsfrist für offene Tickets, keine zweite Event-Endzeit. |
| issuedAt | Fachlicher Ausstellungszeitpunkt; kann bei Importen von createdAt abweichen. |
| Check-in-Audit | Belegt erfolgreiche und abgewiesene Scans einschließlich Wiederholungen. |

Kein neues Feld für den bereits ableitbaren Ursprung „Kauf/Manuell/Gästeliste“: Herkunft wird aus orderId und Gästelistenbezug angezeigt. Keine doppelte Speicherung von Bestellnummer, Zahlungsstatus, Versandstatus der Anmeldung oder separaten Ticketmengen am Antrag.

## 2. Neue Tabellen und Beziehungen

| Entity | Tabelle | Zweck |
|---|---|---|
| Artist | moorl_tv_artist | Wiederverwendbares Profil und Booking-Freigabe |
| ArtistTranslation | moorl_tv_artist_translation | Foundation-Basistexte mit Sprachfallback |
| Stage | moorl_tv_stage | Bühne/Area innerhalb genau eines Events |
| StageTranslation | moorl_tv_stage_translation | Übersetzbare Bezeichnung und Beschreibung |
| Performance | moorl_tv_performance | Ein Auftritt: Event, Artist, optionale Stage und Zeiten |
| GuestlistEntry | moorl_tv_guestlist_entry | Persönliche Anmeldung und optional genau ein Ticket |

Vier fachliche Haupttabellen plus zwei Übersetzungstabellen erweitern den Bestand auf zwölf Plugin-Tabellen. Keine zusätzliche Booking-, Label-, Kollektiv-, globale Venue-, Artist-Event-Mapping-, Reservierungs- oder Versandtabelle.

## 3. Artist: öffentliche Angaben und internes Booking

Öffentlich verwendbare Felder:

- Erforderlicher name und optionale description/teaser über Foundation-Basistexte und Sprachfallback.
- Optionales mediaId für das Bild und logoId für das Logo.
- socialLinks als Liste aus platform, label und gültiger HTTP-/HTTPS-url.
- Optional collectiveName und labelName als zwei Freitextfelder.
- priority, Default 0: höhere Werte zuerst, anschließend Name und ID.
- bookingEnabled, Default false: Profil darf in der Booking-Auswahl erscheinen.

Interne optionale Felder:

- feeAmount als nichtnegative Geldangabe in kleinster Geldeinheit ohne Währungsrelation; NULL bedeutet unbekannt, 0 ausdrücklich kostenlos.
- bookingContact als optionaler öffentlicher externer Bookingkontakt (E-Mail oder HTTP-/HTTPS-Adresse). Ohne externen Kontakt verweist „Booking anfragen“ auf das vorhandene Shop-Kontaktformular.
- bookingNote für Absprachen und Angaben zum Buyout.

Eine zweite Buyout-Summe, ein eigener Agentur-/Labelkatalog und Vertragsstatus sind zunächst überflüssig. Die Gage ist eine unverbindliche Profilangabe, keine nachträglich an allen Auftritten wirksame Honorarvereinbarung. Falls später konkrete Honorare pro Engagement gespeichert werden sollen, gehören diese zum Engagement, nicht als Überschreibung an das globale Artistprofil.

bookingEnabled steuert ausschließlich, ob der Artist auf der Website für Booking angeboten wird. Es steuert weder seine Eventzuordnung noch historische Line-ups. Die Website zeigt einen Hinweis und einen Link zum Kontaktformular oder zum externen bookingContact. Dafür entstehen keine Booking-Anfrage-Entity, Statusmaschine oder eigenen Nachrichten. Technischer Rider, Hotel-/Reiseplanung, Genre-Taxonomie und eigene Artist-SEO-Seiten bleiben weitere Ausbaustufen.

## 4. Stage und Performance

Stage: erforderliches saleId, übersetzbarer name/description, optionales mediaId, position (Default 0), customFields und Zeitstempel. Die Eventadresse bleibt der vorhandene Veranstaltungsort. Eine globale, eventübergreifend wiederverwendbare Venue mit eigener Adresse ist für die angefragten Festivalbühnen zunächst unnötig.

Performance: erforderliches saleId und artistId, optionales stageId, startAt/endAt, position (Default 0), customFields und Zeitstempel. Kein Unique-Key auf Event/Artist: Derselbe Artist darf mehrere Sets haben.

Regeln:

- Eine Stage muss zum Event des Auftritts gehören, auch bei DAL-/API-Schreibzugriffen.
- Einmal verwendete Stages dürfen nicht auf ein anderes Event verschoben werden.
- Ein Artist kann ohne Stage und ohne Zeiten angekündigt werden.
- Beginn und Ende sind unabhängig optionale HH:mm-Texte (StringField, nullable VARCHAR(5)), entsprechend der vereinfachten Benutzervorgabe vom 19.10.2026.
- Eingabe direkt über den Core-Time-Picker mt-datepicker/dateType=time; Anzeige ohne Datums-/Zeitzonenumrechnung.
- Keine zusätzliche Datums-, Reihenfolge-, Sommerzeit- oder Überschneidungsprüfung. Sets über Mitternacht sind erlaubt, eine Tagestabelle entfällt.
- Line-up-Sortierung: position aufsteigend, Artist-priority absteigend, Name und ID.
- Timetable-Sortierung: position aufsteigend, dann Beginn aufsteigend (fehlender Beginn zuletzt), danach ID. Damit bleibt die gewünschte Reihenfolge auch über Mitternacht erhalten.
- Artist-Übersicht zeigt jeden Artist einmal, Timetable zeigt jeden Auftritt.
- Stages mit Auftritten und Artists mit Auftritten werden nicht unbemerkt kaskadierend gelöscht.

Eventfelder lineupPublished und timetablePublished, beide Default false, steuern die öffentliche Ausgabe. Event-active bleibt Voraussetzung. timetablePublished wirkt nur zusammen mit lineupPublished. Es gibt keine Aktiv-Schalter je Artist, Stage und Auftritt; das verhindert zusätzliche Freigabekombinationen und versehentliches Ausblenden historischer Programme. Unfertige Programme werden zunächst vollständig intern gepflegt.

## 5. Gästelistenanmeldung: kleine feste Struktur

Pflicht sind saleId, name und email. Optionale Felder sind phone, invitedBy, volunteerRoles, remarks und internalNote. Telefonpflicht kann pro Event aktiviert werden. Name maximal 511, E-Mail maximal 254, Telefon maximal 64, invitedBy maximal 255 und Bemerkungen/Notiz jeweils maximal 4000 Zeichen.

Ergänzende technische Felder:

| Feld | Aufgabe |
|---|---|
| submissionId | Unveränderliche eindeutige UUID je Formularabsendung; Retry derselben Anfrage erzeugt keinen zweiten Datensatz |
| decision | Nullable: rejected oder cancelled; NULL bedeutet keine Ablehnung/Stornierung |
| ticketId | Nullable, eindeutig und nur durch die Freigabeaktion beschreibbar |
| processedAt, userId/user | Letzte fachliche Entscheidung und optionaler Admin-Benutzer; User-Relation mit ON DELETE SET NULL |
| salesChannelId, languageId | Ursprung und Versandkontext |
| acceptedRules | Snapshot des akzeptierten Regeltextes in der Formularsprache |
| createdAt/updatedAt | Eingang, zugleich Annahmezeit des beim Absenden bestätigten Regeltextes, sowie letzte Änderung |

Kein eigener gespeicherter Status „Ticket ausgestellt“: Er wird aus ticketId abgeleitet. Bei decision=NULL und ticketId=NULL ist die Anmeldung offen, bei decision=NULL und gesetztem ticketId ist ein Ticket ausgestellt. rejected/cancelled bestimmen die ablehnende Entscheidung. Die Adminanzeige unterscheidet damit offen, abgelehnt, storniert und Ticket ausgestellt; Ticketgültigkeit und Versandstatus kommen ausschließlich vom Ticket.

Die E-Mail-Adresse wird für Vergleich und Speicherung getrimmt und kleingeschrieben. Kein separates emailNormalized-Feld, kein Entfernen von Plus-Suffixen oder Punkten. Mehrere Personen mit derselben Adresse bleiben möglich. Ein nicht eindeutiger Event/E-Mail-Index unterstützt die Suche; ein weiterer gleicher Name ist ein Duplikathinweis im Admin, keine automatische Ablehnung.

Technische Wiederholung und fachliche Doppelanmeldung sind verschiedene Dinge: submissionId verhindert den doppelten POST, eine neue Anmeldung mit derselben E-Mail-Adresse wird zur Prüfung gespeichert. Bei wiederholter Anfrage werden weder vorhandene Daten überschrieben noch Details einer fremden Anmeldung zurückgeliefert.

Standard-Ehrenämter: Auf-/Abbau, Theke, Einlass, Deko, Promo und Awareness. Weitere Werte wie DJ sind pro Event ergänzbar. Aufgaben sind Mehrfachauswahl mit stabilen technischen Werten und übersetzbaren Beschriftungen. Freiwilligenmeldung bedeutet noch keine verbindliche Schichteinteilung.

Vorerst weglassen: Geschlecht, Zahlungsart, Erstattungsversprechen, Mengenfeld, Plus-eins-Automatik und allgemeiner Formularbaukasten. Diese Angaben aus dem Referenzformular sind für die beantragte Ticketfreigabe nicht erforderlich. Veranstaltungsinfos werden angezeigt, ein gemeinsamer Regeltext wird bestätigt. Nur tatsächlich benötigte Angaben kommen ins Formular.

## 6. Geheimer Zugang und Eventkonfiguration

Am Event:

- guestlistEnabled, Default false.
- Optionaler Anmeldebeginn und Anmeldeschluss.
- guestlistTicketTypeId: interner kostenloser Typ desselben Events mit eigenem Kontingent; darf im öffentlichen Verkauf inaktiv sein.
- guestlistSalesChannelId: erlaubter Ursprungskanal.
- guestlistAccessKey: zufälliger geheimer Code nach dem bestehenden Deeplink-Prinzip.
- guestlistConfig: begrenzte Einstellungen für Telefonpflicht und Ehrenämter.
- Übersetzbare Formulareinleitung und Hausregeln in der vorhandenen Eventübersetzung.

GET/POST /guestlist/{saleId}/{accessKey} prüft vor Anzeige und Speicherung Schlüssel, Event, Verkaufskanal und Anmeldefrist. Neue Anmeldungen enden spätestens mit endAt, ersatzweise startAt nach bestehender Eventkonvention. Unbekannte/rotierte Codes führen zu 404.

Zugangslink per berechtigter Adminaktion erneut kopieren oder rotieren. Keine Einmalausgabe und keine zusätzliche Einladungstabelle. Der Schlüssel bleibt aus allgemeinen API-/JSON-Antworten verborgen, wird nicht protokolliert und nur im dedizierten Admin-Endpunkt herausgegeben. Die Prüfung erfolgt mit konstantzeitlichem Vergleich. Bestehende Ticketlinks bleiben bei Rotation unverändert.

Private Antworten sind nicht öffentlich cachebar und erhalten noindex/nofollow sowie no-referrer. Kein Sitemap-/Navigations-/Sucheintrag. POST erhält serverseitige Feldprüfung, Honeypot, begrenzte Anfragerate und den zur installierten Shopware-Version passenden Formular-/Origin-Schutz.

Sinnvolle Ergänzung am Event: listed, Default true. Bei false erscheint das Event nicht in öffentlichen Eventlisten, Suche, CMS-Listings oder Sitemap; direkter Aufruf bleibt möglich. Das ist eine ausgeblendete Veranstaltung, kein personengebundener Zugriffsschutz. Der geheime Formularzugang bleibt davon unabhängig. Ein vollständig privates Event mit geschütztem Veranstaltungsort benötigt einen weitergehenden eigenen Zugriffsschutz und wird hier nicht versprochen.

## 7. Ticketfreigabe und Zustellung

Eine Anmeldung reserviert noch keinen Platz und ist keine Eintrittsberechtigung.

1. Adminaktion „Ticket erstellen und senden“ mit dediziertem Recht aufrufen.
2. Aktuelle Konfiguration laden und Transaktion öffnen. Sperrreihenfolge mit dem Bestand vereinheitlichen: Event, Tickettyp, Anmeldung und Ticket. Für gekaufte Tickets liegt die Bestellungssperre davor.
3. Nach den Sperren erneut prüfen. Ist ticketId gesetzt, vorhandenes Ticket zurückgeben, ohne automatische Neuerstellung oder erneuten Versand.
4. Nur offene Anmeldung freigeben; Typ/Event, kostenlosen Typ, Empfänger und Restkontingent prüfen. Freigabe darf nach Anmeldeschluss erfolgen, nicht nach effektivem Eventende oder bei inaktivem Event.
5. Bestehenden DAL nutzen: ein valid-Ticket mit saleId, typeId, attendeeName, attendeePhone und recipientEmail; orderId und customerId dürfen NULL bleiben.
6. Ticket-ID und Bearbeiter/Zeitpunkt am Antrag in derselben Transaktion speichern. decision bleibt NULL; der dargestellte Ausstellungsstatus folgt ticketId.
7. Nach Commit bestehende SendTicketsMessage anstellen. Bei Queuefehler bleibt das Ticket vorhanden und für den Wiederherstellungslauf versandfähig.
8. Versandstatus vom Ticket darstellen. Fehlerkorrektur und erneuter Versand verwenden dasselbe Ticket.

Anmeldung und Kontaktdaten sind nach Ausstellung gegen anonyme oder freie nachträgliche Änderung geschützt. Ticketkorrekturen verwenden die vorhandenen Ticketfunktionen; interne Notizen bleiben bearbeitbar. Ablehnen ist nur ohne Ticket möglich. Stornieren eines ausgestellten, noch nicht eingelösten Tickets widerruft dieses und setzt die Anmeldung auf cancelled; verbrauchte Tickets werden nicht rückwirkend über die Gästeliste storniert.

Am Ticket ergänzen: nullable salesChannelId und languageId für kundenlose Tickets. Bestehender Bestellkontext bleibt bei gekauften Tickets maßgeblich, neue explizite Felder bestimmen den Kontext kundenloser Gästetickets, alte Kundentickets behalten ihren Fallback. Versand, Deeplinks und Zugriffsprüfung verwenden denselben Kontext. Insbesondere darf eine kundenlose Neuanmeldung nicht pauschal auf jeder beliebigen Shopdomain zugänglich sein. Gruppierung trennt bei Bedarf Sprache und Kanal.

Ticketnummer, QR-Code, PDF, Mailvorlagen, Retry und Scanner bleiben bestehende Mechanismen. Kein neuer Mailservice. Die bekannte SMTP-Grenze bleibt: Prozessabbruch nach Annahme und vor Erfolgsspeicherung kann eine weitere E-Mail auslösen.

## 8. Optionales Gesamtkontingent am Event

capacity ist nullable. NULL erhält das bisherige Verhalten mit Kontingenten je Tickettyp. Mit gesetztem Wert müssen sowohl Typkontingent als auch Eventkapazität eingehalten werden.

Gezählt werden wie bisher pending, valid und redeemed über alle Typen desselben Events. Gäste-, Kauf- und manuelle Tickets nutzen dieselbe Prüfung. expired/revoked geben Plätze frei. Die Prüfung erfolgt im DAL unter der bereits vorhandenen Event-Sperre, nicht nur im Gästelistencontroller. Senken unter die aktuell belegten Plätze wird abgewiesen.

Damit können getrennte Typen für Vorverkauf, Abendkasse und Gäste nicht gemeinsam die Raumkapazität überbuchen. Ein zweiter manuell pflegbarer Event-Verkaufszähler ist nicht nötig. Kaufverfügbarkeit und Mengenobergrenzen müssen das verbleibende Eventkontingent ebenfalls berücksichtigen.

## 9. Administration, Sichtbarkeit und bewusst ausgelassener Umfang

Foundation-Module für Artists sowie eingebettete Stage-, Auftritts- und Gästelistentabellen am Event. Für diese eventbezogenen Tabellen ist keine zusätzliche Hauptnavigation nötig. Eine globale Gästelistenübersicht kann über dasselbe Foundation-Modul mit Eventfilter geöffnet werden.

Sinnvolle Bedienfunktionen:

- Artist-Suche und Bookingfilter, Medien/Links, interner Bookingbereich.
- Line-up-Tabelle mit Stagefilter und nach Event gefilterter Stageauswahl.
- Sichtbare Hinweise auf Zeitkonflikte.
- Gästelistenfilter nach Event, Entscheidung, Ehrenamt, Einladendem und Versandstatus.
- Mehrfachfreigabe mit Ergebnis je Anmeldung; jeder Eintrag wird separat atomar bearbeitet, fehlendes Kontingent stoppt keine bereits erfolgreichen Freigaben rückwirkend.
- Zähler für Anmeldungen, ausgestellte Tickets und verbleibendes Kontingent, aus den tatsächlichen Daten abgeleitet.
- Export über das vorhandene Import-/Exportsystem statt einer zweiten Exportinfrastruktur.

Öffentliche Eventseite und bestehendes Detail-CMS-Element teilen denselben Line-up-/Timetable-Loader. Artistkarten und Booking-Auswahl nutzen explizit ausgewählte öffentliche Felder. Gagen, Bookingkontakt/-notizen, Anmeldungen, Regeln-Snapshots und Geheimschlüssel bleiben intern.

Nicht im ersten Ausbau: grafischer Drag-and-drop-Timetable-Editor, globale Venue-/Label-/Kollektivverwaltung, Vertrags-/Schicht-/Hotelplanung, Bezahlformular für Gästelisten, automatisch bestätigte Ehrenamts-Rückerstattung und eigene Artist-SEO-Detailseiten.

## 10. Integrität und Umstellung vorhandener Daten

Foundation-Feldsammlungen, Traits, vollständige FK-Storage-Namen, native Translation-Definitionen und Shopware-Versionierung beibehalten. Keine PHP-Migrationen und keine ungefragten Änderungen an Produktivdaten. Der bisherige Sechs-Tabellen-Rahmen wird durch den Erweiterungsauftrag angepasst; andere Projektregeln gelten weiter.

Bei späterer Bestellbezugsumstellung:

1. Neue nullable orderId mit nativer Referenzversion ergänzen.
2. Direkte Bestellreferenzen aus den bisherigen Positionsrelationen übernehmen.
3. Je Bestellungsversion/Tickettyp stabile unitIndex-Werte vergeben, sortiert nach bisheriger Positions-ID, bisherigem unitIndex und Ticket-ID. Mehrere Positionen desselben Typs können bislang denselben unitIndex besitzen.
4. Übernahme auf Vollständigkeit, erhaltene Ticket-IDs/Nummern/Tokens/Statuswerte und neue Eindeutigkeit prüfen. Auch historische widerrufene/abgelaufene Tickets erhalten eigene stabile Einheiten.
5. Leser, Schreiber, Eigentümerprüfung unter Sperre, Scanner-Namensfallback, Versand, Deeplinks, Flow, Adminfilter und Tests gemeinsam auf die neue Beziehung umstellen.
6. Erst nach erfolgreicher Prüfung alte FK-Spalten, alten Unique-Key und Positions-Extension entfernen. Neue inverse Order-Association schützt verknüpfte Bestellungen vor Löschung.

Die Datenübernahme ist fachliche Arbeit, die ein generierter Schemaabgleich allein nicht ersetzt. Bestehende manuelle Tickets bleiben ohne Bestellbezug. Keine rückwirkenden Gästeanmeldungen aus vorhandenen Tickets erzeugen.

Neue Einschränkungen: eindeutige submissionId und ticketId der Anmeldung; Ticket-Ausstellungseinheit nach Bestellung/Version/Typ/Index. Entscheidungen, Ticketverknüpfung, Bestellherkunft und technische Indizes sind nicht frei im Formular editierbar. Ein Event, Artist oder eine Stage mit fachlichen Referenzen wird nicht implizit kaskadierend gelöscht. Scannerrolle erhält keine zusätzlichen Rechte.

## 11. Umsetzung in unabhängigen Paketen

1. **Ticketmodell vereinfachen:** direkter Bestellbezug, sichere Idempotenz und Datenübernahmeplan; Checkout, Zugriff, Zahlung/Storno/Ablauf, Versand, Flow und Admin gemeinsam umstellen.
2. **Artists und Programmplanung:** fünf neue Definitionen einschließlich Übersetzungen, Foundation-Administration, Stage-/Zeitvalidierung und Event-Freigabeschalter.
3. **Öffentliche Ausgabe:** Line-up, Timetable, Booking-Auswahl und listed-Filter konsequent in allen Listings/Suche/Sitemap.
4. **Gästelistenmodell und Zugang:** sechste neue Definition, feste Formularstruktur, Anfrage-Idempotenz, Regel-Snapshot und geheimer kopierbarer Link.
5. **Freigabe und Kapazität:** Ticketbezug, Versandkontext, atomare Einzelfreigabe, Mehrfachaktion und optionales Eventgesamtkontingent.
6. **Abschluss:** Demo-/Basisdaten, PLUGIN_TABLES und Schemahelfer, Import-/Exportprofile, deutsche/englische Snippets, Schema-/Betriebs-/Benutzerdokumentation und Regression.

Bestandsvereinfachung und Eventprogramm sind eigenständige Pakete. Die Gästeliste verwendet anschließend das vereinfachte Ticketmodell.

## 12. Abnahme und Prüfschwerpunkte

- Zwei Bestellpositionen desselben Tickettyps erzeugen aggregiert exakt die gekaufte Anzahl. Wiederholte Ausstellung und Zahlungsereignisse erzeugen keine zusätzlichen Tickets, auch nach Ablauf/Widerruf.
- Neue Bestellbezüge erhalten Namens-/Empfängerfallbacks, Kundenübertragung, Kanalgrenzen, Mailgruppierung, Flow, Storno und Zahlungsfrist. Gleichzeitige Eigentümeränderung wird unter Sperre erneut geprüft.
- Historische Tickets mit kollidierenden bisherigen unitIndex-Werten werden ohne Verlust ihrer Identität übernommen.
- Künstler bleibt nach deaktiviertem bookingEnabled in historischen Programmen. Es gibt keine zusätzliche Artist-/Stage-/Auftritts-Aktivierung.
- Mehrere Auftritte, unabhängig fehlende Zeiten/Stages und Mitternacht funktionieren mit einfachen Uhrzeittexten; Stage-fremde Events bleiben gesperrt.
- Unveröffentlichtes Line-up bzw. unveröffentlichte Zeiten werden nicht in HTML, APIs oder Event-JSON-LD ausgegeben.
- listed=false entfernt das Event aus allen öffentlichen Listen/Suche/Sitemap; direkte Erreichbarkeit ist ausdrücklich erhalten.
- Falscher/rotierter Formularcode, falscher Kanal, deaktiviertes oder geschlossenes Formular erlauben weder Lesen noch Schreiben.
- Doppelter POST mit gleicher submissionId erzeugt genau eine Anmeldung. Unterschiedliche Gäste mit derselben E-Mail-Adresse sind erlaubt; anonymes erneutes Absenden überschreibt keine vorhandenen Daten.
- Zwei parallele Freigaben derselben Anmeldung erzeugen ein Ticket. Konkurrenz verschiedener Tickettypen um den letzten Eventplatz wird ebenfalls serialisiert.
- DAL-/Kontingentfehler rollen Ticket und Verknüpfung gemeinsam zurück. Queue-/Mailfehler erzeugen kein zweites Ticket.
- Mehrfachaktion meldet je Eintrag Erfolg/Fehler und behält erfolgreiche Einzelfreigaben.
- Kundenlose neue Tickets nutzen ihre richtige Sprache und Domain, bestehende Ticketkontexte behalten definierte Fallbacks.
- Persönlicher Download, PDF und einmaliger Check-in funktionieren unverändert. Geheime Schlüssel und interne Booking-/Gastdaten erscheinen nicht in öffentlichen Antworten.
- Neues Schema lässt sich mit MoorlDevTools erzeugen; Schemahelfer und Datenpakete setzen keine feste Anzahl von sechs Tabellen mehr voraus.

Spätere Verifikation: gezielte PHPUnit-Unit-/Integrationstests, getrennte DB-Verbindungen für Parallelfälle, vorhandene Node-Admin-Tests, Container-/Twig-Prüfung und Admin-/Storefront-Build. Integration ausschließlich gegen ausdrücklich ausgewählte isolierte moorl_tv_*_test-Datenbank, Mailtransport ersetzt. In dieser Planungsrunde wurden keine Laufzeittests ausgeführt.

Die Empfehlungen sind bewusst konkret gewählt. Falls der fachliche Umfang später abweicht, wird nur die betroffene Entscheidung angepasst; es ist keine weitere allgemeine Entscheidungsrunde nötig, um den Entwurf zu beurteilen.
