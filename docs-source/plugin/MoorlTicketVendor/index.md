---
description: "Veranstaltungen und Tickets direkt in Shopware verwalten: mit Kontingenten, PDF-/QR-Tickets, Zahlungsfreigabe, Artist-Booking, Line-up, Gästelisten und Online-Check-in."
tags:
  - Tickets
  - Veranstaltungen
  - Gästeliste
  - Check-in
  - Shopware 6.7
---

# Veranstaltungen und Eintrittskarten

Veranstaltungen und Tickets direkt in Shopware verwalten: mit Kontingenten, PDF-/QR-Tickets, Zahlungsfreigabe, Artist-Booking, Line-up, Gästelisten und Online-Check-in.

![Vorschau](images/storefront-event.png)

---

## Plugin Demo

Zu diesem Plugin steht eine Storefront-Demo zum Testen bereit. Unter folgenden Link kann das Plugin getestet werden:

- [https://demo-sw67.moori.net/MoorlTicketVendor](https://demo-sw67.moori.net/MoorlTicketVendor)


## Plugin erwerben

Dieses Plugin kann im offiziellen **Shopware Community Store** erworben werden.

- [Shopware Community Store](https://store.shopware.com/de/search?search=MoorlTicketVendor)


**Wichtiger Hinweis:** Sie benötigen das Foundation Plugin, welches Ihnen kostenlos zur Verfügung steht: [moori Foundation](../MoorlFoundation/index.md)


## Quickstart

Für dieses Plugin steht ein **Demo-Paket** zum Testen bereit.

Gehen Sie zu `Einstellungen` → [`Demo Assistent`](../MoorlFoundation/demo-assistant.md) und wählen Sie dort `MoorlTicketVendor` aus.

**Hinweis:** In einigen Fällen werden neue Kategorien und Seiten zu Ihrem Shop hinzugefügt. Bitte beachten Sie, dass die Demo-Daten ausschließlich zu Testzwecken dienen. Die darin enthaltenen Bilder können urheberrechtlich geschützt sein und dürfen nicht der Öffentlichkeit zugänglich gemacht werden.


---

## Voraussetzungen und erster Ablauf

Ticket Vendor setzt Shopware 6.7 mit Storefront und MoorlFoundation ab 1.7.109 (Versionsreihe 1.7) voraus. Foundation stellt unter anderem Formulare, Listen, CMS-Helfer und Datenpakete bereit. Installieren und aktivieren Sie Foundation zuerst. Für Zahlungsfristen und automatischen Versand müssen Shopwares geplante Aufgaben und Nachrichtenverarbeitung laufen.

Ein erster vollständiger Durchlauf sieht so aus:

1. Unter **Kataloge → Ticketverkäufer - Veranstaltungen** eine Veranstaltung erstellen.
2. Beginn, Ende, Ort und Inhalte pflegen; Veranstaltung aktivieren.
3. Einen aktiven Tickettyp mit Preis, Steuer und Kontingent zuordnen.
4. Eine Kategorie mit dem CMS-Veranstaltungslisting anlegen und in der Plugin-Konfiguration unter **Seite mit Veranstaltungen (Liste)** auswählen. Die Veranstaltung über diese Kategorie öffnen und eine Testbestellung aufgeben.
5. Den tatsächlichen Zahlungsablauf prüfen. Sobald Shopware die maßgebliche Transaktion als `paid` meldet, werden die Tickets gültig und zum Versand vorgemerkt.
6. Das PDF im Kundenkonto beziehungsweise in der Administration öffnen.
7. Im Scanner Event und Einlösebereich wählen. Einzeltickets sind nach einem Scan verbraucht; Pakete bleiben bis zur letzten Einlösung gültig.

## Veranstaltungen verwalten

Die Veranstaltungsliste zeigt die angelegten Veranstaltungen. Die Detailansicht bündelt Stammdaten, öffentliche Inhalte, Ort sowie zugeordnete Tickettypen, Kundentickets und Check-in-Protokolle.

![Veranstaltungsübersicht mit Terminen und Veranstaltungsorten.](images/admin-events.png)

| Bereich | Verwendung |
| --- | --- |
| Name und Beschreibung | Öffentliche Bezeichnung und ausführliche Veranstaltungsinformationen; übersetzbare Inhalte in den verwendeten Shopsprachen pflegen. |
| Aktiv | Dieser Schalter steuert die Freigabe der Veranstaltung. Für den Verkauf müssen zusätzlich die Zeitfenster passen. |
| Beginn und Ende | Zeitpunkt der Veranstaltung. Ein Enddatum beendet auch die Gültigkeitsprüfung am Einlass. |
| Zeitzone | IANA-Bezeichnung, etwa `Europe/Berlin`. Zeitangaben werden technisch in UTC gespeichert; bei Importen UTC verwenden. |
| Anzeigen ab/bis | Separates Zeitfenster für öffentliche Sichtbarkeit und Verkauf. Es ersetzt die Veranstaltungszeiten nicht. |
| Veranstaltungsort und Adresse | Ortsname, Hinweise, Straße, Postleitzahl, Stadt und Land. |
| Medien und SEO | Bilder, Teaser, Metadaten und weitere Foundation-Inhalte für die öffentliche Darstellung. |
| Erlebniswelt | Optional eine CMS-Seite für die Veranstaltungsdetailseite zuordnen. |

Eine öffentliche Veranstaltung benötigt ein passendes Anzeigezeitfenster. Ist ein Endzeitpunkt vorhanden, endet der öffentliche Verkauf mit diesem; ohne Endzeitpunkt bereits mit dem Beginn. Für einen früheren Vorverkaufsschluss setzen Sie zusätzlich „Anzeigen bis“.

Die Veranstaltung besitzt keinen technischen Namen. Ihre Identität ergibt sich aus der ID; der übersetzte Name dient der Darstellung. Vorhandene Tickets jedes Status verhindern die Eventlöschung; nach ihrer ausdrücklichen Löschung werden verbleibende Event-Protokolle mit dem Event entfernt. Deaktivieren Sie die Veranstaltung oder begrenzen Sie den Verkaufszeitraum, um den Verkauf zu beenden.

![Veranstaltungsdetails: Titel, Teaser und Beschreibung.](images/admin-event.png)

![Öffentliche Eventseite mit Bild, Datum, Veranstaltungsort und Link zur Ticketwahl.](images/storefront-event.png)

## Tickettypen, Preise und Kontingente

Tickettypen stehen unter **Einstellungen** zur Verfügung und können außerdem innerhalb ihrer Veranstaltung verwaltet werden. Ein Tickettyp gehört genau einer Veranstaltung, beispielsweise „Standard“, „VIP“ oder „Gästeliste“.

| Feld | Bedeutung |
| --- | --- |
| Veranstaltung | Zugehörige Veranstaltung. Ein Typ mit ausgestellten Tickets kann nicht in eine andere Veranstaltung verschoben werden. |
| Name | Bezeichnung für Kunden und Verwaltung. |
| Aktiv | Aktive Typen können öffentlich angeboten werden. Inaktive Typen eignen sich für interne Einladungen. |
| Preis und Steuer | Shopware-Preise und Steuersatz. Die Preisberechnung erfolgt serverseitig in der Warenkorbwährung. |
| Gesamtkontingent | Maximale Zahl gleichzeitig belegter Plätze dieses Typs. |
| Belegte Kontingenteinheiten | Automatisch berechnete, schreibgeschützte Belegung einschließlich offener und eingelöster Tickets. |
| Einlösebereich | Einlass, Getränke oder Essen; genau ein Bereich pro Ticket. |
| Einlösungen pro Ticket | Ganze Zahl ab 1; jeder bewusste Scan verbraucht eine. |
| Personenplätze pro Ticket | Beim Einlass mindestens 1; bei Getränken/Essen genau 0. |
| Mindest-/Maximalabnahme | Zulässige Gesamtmenge dieses Typs im Kaufvorgang. |
| Anzeigen ab/bis | Optionaler Verkaufszeitraum zusätzlich zur Veranstaltung. |
| Position | Reihenfolge der Tickettypen. |

`pending`, `valid` und `redeemed` belegen das Kontingent. `expired` und `revoked` geben es frei. Ein eingelöstes Ticket gibt keinen Platz für einen weiteren Verkauf frei. Ein Warenkorb reserviert noch keinen Platz; die Belegung entsteht erst beim Bestellabschluss. Die abschließende Kontingentprüfung und Ticketerstellung erfolgen gemeinsam, sodass konkurrierende Käufe nicht denselben letzten Platz erhalten.

Auch manuell erstellte Tickets unterliegen der Kontingentprüfung. Das Gesamtkontingent darf nicht unter die bestehende Belegung gesenkt werden.

![Fünfer-Gruppenticket: Preis, Einlösungen und Kontingent.](images/admin-type.png)

## Pakete und feste Ticketwerte

Ein Fünfer-Gruppenticket belegt fünf Typkontingent-Einheiten und fünf Eventplätze und enthält fünf Einlösungen auf einem QR-Code. Ein Fünfer-Getränkepaket belegt eine Typkontingent-Einheit und keinen Eventplatz. Ein Kontingent von 100 erlaubt daher 20 Gruppentickets oder 100 Getränkepakete. Bei vier freien Eventplätzen ist das Gruppenticket nicht mehr kaufbar; das Getränkepaket kann weiterhin verfügbar sein. Preis und Kaufmenge zählen vollständige Tickets/Pakete.

Jedes ausgestellte Ticket speichert Bereich, Limit und Personenplätze aus seinem Typ. Spätere Typänderungen gelten für neue Tickets. Ein ungebundenes manuelles Ticket kann vor der ersten Einlösung mit neuen Ausstellungswerten und Kontingentprüfung einem anderen Typ zugeordnet werden; nach der ersten Nutzung sind Typ und Event fest. Widerruf und Reaktivierung erhalten den Verbrauch. Vollständig verbrauchte Tickets werden dadurch nicht erneut einlösbar. Konto/PDF zeigen den gespeicherten Leistungsumfang; das Konto den aktuellen Verbrauch.

![Ticketwahl mit Einzeleintritt, Gruppentickets und Verzehrpaketen.](images/storefront-tickets.png)

## Öffentliche Darstellung und Erlebniswelten

Die in der Plugin-Konfiguration unter `category` gewählte Shopware-Kategorie verwendet eine Erlebniswelt mit dem Element `moorl-tv-ticket-sale-listing`. Sie zeigt verfügbare Veranstaltungen mit Seitennavigation und ist das Ziel des Zurück-Links auf Veranstaltungsdetails. Die Detailseite `/tickets/{saleId}` verwendet die am Event hinterlegte CMS-Seite, ersatzweise die konfigurierte Standardseite `cmsPageId`. Ohne CMS-Auswahl wird die einfache Detaildarstellung verwendet; ohne ausgewählte Kategorie entfällt der Zurück-Link. Der Ticketkauf verwendet den normalen Shopware-Warenkorb und Checkout. Tickets sind digitale Warenkorbpositionen; sie benötigen keinen physischen Versand.

Über das Foundation-CMS-Element **Veranstaltungen** (`moorl-tv-ticket-sale-listing`) können Sie eine Veranstaltungsliste in Erlebniswelten einbinden. Die Veranstaltungsdetailseite kann zusätzlich ihre zugewiesene CMS-Seite laden.

Die mitgelieferte SEO-Vorlage erzeugt URLs nach dem Muster `tickets/<Veranstaltungsname>/<ID>`. Nach Änderungen müssen die SEO-Indizes aktuell sein. Ein vorhandenes, angepasstes SEO-Template wird bei erneutem Datenimport erhalten.

Mit **Veranstaltungen mit Archiv (statisch)** (`moorl-tv-ticket-sale-static-listing`) fügen Sie eine feste Übersicht aller aktiven Events hinzu. Laufende und kommende Veranstaltungen stehen mit dem nächsten Termin zuerst oben; vergangene folgen absteigend und ausgegraut. Verkaufszeiträume begrenzen diese Übersicht nicht. Verfügbare Events verlinken immer auf ihre interne Veranstaltungsdetailseite. Dort wird eine hinterlegte **Alternative Veranstaltungs-URL** als Aktionsbutton angezeigt. Erlaubt sind HTTP(S)-Adressen und interne Pfade; externe Adressen öffnen in einem neuen Tab. Ohne gültige alternative URL führt der Button zur Ticketauswahl. Vergangene Events und kommende Events außerhalb ihres Verkaufszeitraums erhalten im Listing keinen Link, auch mit alternativer URL. Die optionale Spalte `moorl_tv_ticket_sale.alternative_url` (`VARCHAR(2048)`, nullable) bei bestehenden Tabellen gezielt per SQL ergänzen und anschließend Administration und Theme neu bauen.

![Die statische CMS-Liste zeigt kommende Veranstaltungen mit Bildern und Ticketlinks.](images/storefront-events.png)

![Vergangene Events stehen unter dem kommenden Programm, ausgegraut und ohne Kaufbutton.](images/storefront-archive.png)

## Bestellung, Bezahlung und automatische Freigabe

Für jede gekaufte Einheit entsteht ein eigenes Ticket. Eine Bestellposition mit Menge drei erzeugt also drei Ticketnummern und drei QR-Codes. Mehrere Kategorien einer Veranstaltung und Tickets verschiedener Veranstaltungen können in einer Bestellung vorkommen.

Bestelltickets starten mit **Zahlung ausstehend**. Standardmäßig beträgt die Zahlungsfrist 30 Minuten; sie ist in der Erweiterungskonfiguration über **Zahlungsfrist in Minuten** einstellbar. Der vollständige native Zahlungsstatus `paid` schaltet Tickets frei. Eine offene, autorisierte oder nur teilweise bezahlte Transaktion genügt nicht. Auch ein Checkout mit Preis 0 benötigt den entsprechenden nativen Zahlungsabschluss; verwenden Sie für sofort gültige Einladungen die manuelle Anlage.

Der Ablaufjob prüft die tatsächliche Zahlung erneut. Offene, überfällige Bestellungen werden über die nativen Statusübergänge storniert; die zugehörigen Tickets laufen ab und geben ihr Kontingent frei. Das kann die gesamte Bestellung einschließlich weiterer Positionen betreffen. Berücksichtigen Sie dies bei Mischwarenkörben und Zahlungsmethoden mit längerer Zahlungsdauer.

Bestellstornierung, vollständige Erstattung und Chargeback widerrufen noch belegende Tickets. Bereits stornierte Bestellungen werden durch eine spätere Zahlung nicht automatisch wieder freigegeben. Prüfen Sie solche Fälle im Zahlungsanbieter und in Shopware manuell. Das Plugin veranlasst keine eigene Rückerstattung beim Zahlungsanbieter.

![Ein Standardticket im Shopware-Warenkorb mit Veranstaltung, Menge und Preis.](images/storefront-cart.png)

## Kundentickets und Status

Ticketstatus und Versandstatus werden übersetzt angezeigt. Den Ticketstatus können berechtigte Administratoren im Ticketformular korrigieren. Wird ein vollständig eingelöstes Ticket wieder auf **Gültig** gesetzt, steht genau eine Einlösung erneut zur Verfügung; frühere Einlösungen und Scanprotokolle bleiben erhalten. Zahlungs-, Ablauf- und Check-in-Automatismen gelten weiterhin. Im Kontextmenü von Tickets und Gästelisten-Anmeldungen mit ausgestelltem Ticket kopiert **Ticket-Bearbeitungslink kopieren** den öffentlichen Bearbeitungslink, beispielsweise zum Teilen per WhatsApp.

Generierte Tickets finden Sie in der Veranstaltung sowie in den Ticket-Tabs der Bestell- und Kundendetails. Die Ticketansicht zeigt unter anderem Nummer, Veranstaltung, Typ, Empfänger, Bestellbezug, Gültigkeits- und Versandstatus.

| Ticketstatus | Bedeutung |
| --- | --- |
| `pending` – Zahlung ausstehend | Platz belegt, noch kein Einlass und kein gültiges Ticket-PDF. |
| `valid` – Gültig | Freigegeben und beim passenden offenen Event einlösbar. |
| `redeemed` – Eingelöst | Bereits verwendet; ein weiterer eigenständiger Scan wird abgewiesen. |
| `expired` – Abgelaufen | Zahlungsfrist abgelaufen; keine Einlassberechtigung. |
| `revoked` – Widerrufen | Gesperrt, etwa nach Stornierung oder manuellem Widerruf. |

Die Ticketnummer stammt aus dem nativen Nummernkreis **Ticketnummern** (`moorl_tv_ticket`), standardmäßig `T-{n}` ab 10000. Sie wird beim Speichern vergeben und anschließend unveränderlich angezeigt. Der QR-Code enthält einen separaten zufälligen Ticket-Token. Die sichtbare Ticketnummer ist deshalb kein Ersatz für den QR-Code oder Token beim Scannen.

Der QR-Code enthält ausschließlich den Ticket-Token, keine Personen-, Veranstaltungsdaten oder Links. Neue Standard- und Gästelistentickets erhalten einheitlich acht Zeichen; Demotickets verwenden eigene Beispielcodes. Bereits ausgegebene längere Tokens bleiben gültig. Der vollständige Token steht im PDF direkt unter dem QR-Code und kann im Scanner manuell eingegeben werden. Für ältere PDFs das Ticket erneut herunterladen.

Handynummern in Tickets und Gästelisten werden beim Speichern von Leerzeichen, einschließlich geschützter Leerzeichen und Tabs, befreit. `+`, Klammern und Bindestriche bleiben erhalten. Das gilt auch für Administration und CSV-Import. Leere Eingaben entfernen die optionale Nummer; bestehende Datensätze werden nicht gesammelt umgeschrieben. Die Bearbeitungssperren bereits eingelöster Tickets und ausgestellter Gästelisteneinträge gelten weiterhin.

## Manuelle Tickets und Gästeliste

Im Reiter **Gästeliste** der Veranstaltung stehen die Anmeldungen aller zugehörigen Tickettypen. Das Anmeldedatum ist die erste Spalte; neue Anmeldungen stehen oben. Ticketstatus und Versandstatus sind in dieser Liste ausgeblendet. Bemerkungen, Ehrenamtliche Unterstützung und das verknüpfte Ticket finden Sie im allgemeinen Reiter des Anmeldungsformulars.

Sie können innerhalb einer Veranstaltung direkt ein neues Kundenticket anlegen. Der Veranstaltungsbezug wird vorbelegt, und die Typauswahl enthält nur deren Tickettypen. Bestellung und Kundenkonto sind optional. Manuelle Tickets starten mit Status **Gültig**; sie warten nicht auf eine Zahlung.

Für eine interne Gästeliste:

1. Einen Tickettyp „Gästeliste“ mit Preis 0 und eigenem Kontingent anlegen.
2. Den Typ **inaktiv** lassen, damit er nicht öffentlich verkauft wird. Die Veranstaltung selbst muss für den Einlass aktiv bleiben.
3. Für jeden Gast ein Ticket dieses Typs erstellen.
4. Optional einen Kunden oder eine Empfänger-E-Mail zuordnen.
5. Das PDF ausgeben oder gezielt versenden und beim Einlass regulär scannen.

Ein Ticket ohne Kundenkonto und ohne Bestellposition ist zulässig. Ohne erreichbaren E-Mail-Empfänger ist es speicherbar und kann als PDF ausgegeben werden; für den Versand muss ein Empfänger ergänzt werden. Der automatische Wiederherstellungslauf berücksichtigt auch noch nicht versendete gültige manuelle Tickets: Das Speichern eines Tickets mit Empfänger ist daher kein dauerhafter „nur speichern“-Modus.

Zusätzlich bietet der Gästelisten-Tab eines kostenlosen Tickettyps ein privates Anmeldeformular mit Name, E-Mail, optionaler Telefonnummer und Ehrenämtern. Anmeldungen lassen sich bestätigen und anschließend einzeln in Tickets umwandeln. Eine Anmeldung reserviert noch keinen Platz. Ausgestellte Tickets lassen sich im Scanner auch über den Namen finden; Anmeldungen ohne Ticket erscheinen dort nicht. Ein Begleitpersonenzähler ist nicht vorgesehen.

Die Checkbox **Allgemein → Personalisierung möglich** am Tickettyp steuert Namensänderungen im Kundenkonto und über den öffentlichen Bearbeitungslink. Sie ist standardmäßig aktiviert. Deaktivieren Sie sie für feste Teilnehmernamen, beispielsweise bei der Gästeliste. Preis und Gästelistenzuordnung haben keinen Einfluss auf die Freigabe. Die Handynummer bleibt bei ausstehenden und gültigen Tickets änderbar. Berechtigte Administratoren können Namen weiterhin nach den bestehenden Statusregeln korrigieren. Bestehende Installationen benötigen den [Schemaabgleich](schema.md#personalisierung-am-tickettyp).

## PDF und E-Mail-Versand

Am Tickettyp unter **Allgemein → Hinweis für die Ticket-E-Mail** lassen sich zusätzliche Hinweise einschließlich einer WhatsApp-Einladungs-URL als mehrzeiliger Text je Sprache pflegen. Die Ticket-Mail zeigt den Hinweis beim jeweiligen Ticket in der Empfängersprache. Leere Hinweise werden ausgelassen. Bei eigenen Mailvorlagen `ticket.emailNote` innerhalb der Ticket-Schleife ergänzen; die Aktualisierung bestehender Installationen ist in [Schema](schema.md#e-mail-hinweis-am-tickettyp) beschrieben.

Die Ticketaktionen bieten **PDF herunterladen**, **Erneut versenden** und **Ticket widerrufen** entsprechend den Benutzerrechten. Gültige und eingelöste Tickets können als PDF ausgegeben werden. Ein erneuter Download macht ein bereits eingelöstes Ticket nicht wieder gültig.

Die Versandadresse wird in dieser Reihenfolge ermittelt:

1. Explizite Empfänger-E-Mail am Ticket.
2. E-Mail des zugewiesenen Kunden.
3. E-Mail aus dem Bestellkunden-Snapshot.

Tickets einer Bestellung werden nach tatsächlichem Empfänger und Verkaufskanal gruppiert versendet. Abweichende Empfänger erhalten dadurch keine fremden Tickets im selben Anhang. Die Vorlage **Ticketversand** ist auf Deutsch und Englisch enthalten und kann über die Shopware-Mailverwaltung angepasst werden. Im Vorlagenkontext stehen `tickets` mit `ticketNumber`, `eventName` und `typeName` bereit; die QR-Tokens werden dort nicht offengelegt. Der PDF-Anhang wird vom Plugin erzeugt.

| Versandstatus | Bedeutung |
| --- | --- |
| `pending` – Ausstehend | Noch keine erfolgreiche Zustellung vermerkt. |
| `sent` – Versendet | Der Mailtransport hat den Versand angenommen; dies ist keine Lesebestätigung. |
| `failed` – Fehlgeschlagen | Ein Versandversuch ist gescheitert. Empfänger, Vorlage, SMTP und Worker prüfen. |

Der geplante Wiederherstellungslauf stellt ausstehende oder fehlgeschlagene gültige Tickets mit weniger als fünf Versuchen erneut an, frühestens fünf Minuten nach der letzten Änderung. Messenger verwendet zusätzlich seine konfigurierte Retry-Strategie. Die Admin-Aktion erlaubt einen gezielten erneuten Versand bereits versendeter Tickets.

Gleichzeitige Versandversuche werden serialisiert. Falls ein Prozess unmittelbar nach SMTP-Annahme und vor Speicherung des Erfolgs abbricht, kann eine Wiederholung dennoch eine zweite Mail erzeugen.

## Flow Builder

Die Aktion **Tickets versenden** steht für Flow-Ereignisse mit Bestellkontext zur Verfügung. Sie benötigt keine zusätzliche Aktionskonfiguration und stellt gültige beziehungsweise bereits eingelöste Tickets dieser Bestellung zum Versand an. Bereits erfolgreich versendete Tickets werden übersprungen. Ein Flow ersetzt weder die Zahlungsfreigabe noch die laufenden Worker.

## Einlass mit dem Browser-Scanner

1. Einen Benutzer mit der Rolle **Ticket Vendor – Scanner** anmelden lassen.
2. **Dashboard → Ticketscanner** öffnen.
3. Die richtige Veranstaltung und den Bereich Einlass, Getränke oder Essen auswählen.
4. **QR mit Kamera scannen** starten und gegebenenfalls die Kameraberechtigung erteilen. Alternativ **Manuell** wählen und im Feld **Ticket-Token** nach Token, Handynummer, E-Mail oder Namen suchen. Das passende Ticket auswählen, die Angaben prüfen und anschließend auf **Einchecken** klicken. Die Auswahl allein löst das Ticket nicht ein.
5. Das Ergebnis prüfen. Nur **Check-in akzeptiert** bestätigt eine neue Einlösung.

Die Suche zeigt ausschließlich Tickets der ausgewählten Veranstaltung, einschließlich bereits eingelöster und ungültiger Tickets. Ticketnummer, Name, E-Mail, Handynummer, Status, Einlösebereich und Verbrauch helfen bei der Auswahl. Weitere Treffer werden beim Scrollen nachgeladen. Bereits vollständig eingelöste Tickets liefern auch bei manueller Auswahl keine weitere Einlösung. Der gewählte Einlösebereich und alle übrigen Check-in-Regeln gelten weiterhin. Die bestehende Scanner-Rolle reicht für die Suche aus.

Der Scanner füllt den Bildschirm aus und passt seine Bedienelemente an Smartphones und Tablets an. **Kamera** und **Manuell** wechseln die Erfassungsart. Nach einem Ergebnis startet **Nächstes Ticket** die Kamera erneut oder fokussiert die manuelle Eingabe. Erfolgreiche Einlösung, bereits eingelöstes Ticket und Ablehnung werden mit Text, Symbol und unterschiedlichen Farben angezeigt.

Über **Vollbild öffnen** lässt sich zusätzlich der Browser-Vollbildmodus aktivieren, sofern das Gerät ihn unterstützt. **Zur Administration** verlässt die Scanneransicht. Beim Verlassen oder Wechsel zur manuellen Eingabe wird die Kamera gestoppt. Bei einem Verbindungsfehler bleiben Token und Anfrage-ID für **Erneut prüfen** erhalten.

Die Kameraerkennung benötigt einen sicheren Browserkontext, üblicherweise HTTPS, und Kameraberechtigung. Ohne native QR-Erkennung übernimmt der lokal eingebundene jsQR-Fallback die Auswertung der Kamerabilder. Die manuelle Eingabe bleibt auch ohne Kameraerkennung nutzbar. Es ist eine Onlineverbindung zum Shop erforderlich.

| Ergebnis | Vorgehen am Einlass |
| --- | --- |
| Check-in akzeptiert | Einlass gewähren. Das Ticket wurde eingelöst. |
| Falscher Bereich | Den angezeigten Bereich verwenden; es wurde nichts verbraucht. |
| Ticket bereits eingelöst | Keinen weiteren Einlass allein anhand dieses Codes gewähren; Klärung durch Veranstaltungsleitung. |
| Andere Veranstaltung | Veranstaltungsauswahl prüfen. |
| Veranstaltung geschlossen | Aktivierung und Endzeit durch die Verwaltung prüfen lassen. |
| Ticket nicht gültig | Zahlung, Ablauf oder Widerruf durch die Verwaltung prüfen lassen. |
| Unbekanntes Ticket | Vollständigen Code prüfen; bei Bedarf Verwaltung einschalten. |
| Netzwerkfehler | Es liegt noch kein verlässliches Ergebnis vor. Denselben Scan erneut versuchen. |

Jeder bewusste Scan verbraucht eine Einlösung und zeigt Verbrauch, Limit und Rest. Bis zur letzten Einlösung bleibt das Ticket gültig. Die Kamera pausiert nach einem Ergebnis bis **Nächstes Ticket**. Event- oder Bereichswechsel setzen Kamera, Eingabe und offene Wiederholung zurück. Die API verhindert einen doppelten Verbrauch der letzten Einlösung bei parallelen Scans. Eine technische Wiederholung derselben Anfrage liefert das ursprüngliche Ergebnis, ein neuer Scan eines eingelösten Tickets meldet dagegen „bereits eingelöst“. Das Check-in-Protokoll dokumentiert Ergebnis, Zeitpunkt, Anfrage-ID und gegebenenfalls Gerät sowie Benutzer/Integration. Es bietet keine Funktion zum Zurücksetzen eines Check-ins.

Der Einlass verlangt eine aktive Veranstaltung, deren vorhandenes Enddatum nicht überschritten ist. Es gibt derzeit keine separate konfigurierbare Einlassöffnung: Ein künftiger Veranstaltungsbeginn verhindert einen Scan allein nicht.

![Scanner mit ausgewählter Veranstaltung und manueller Token-Eingabe.](images/admin-scanner.png)

## Benutzer und Scanner-Rolle

Das Foundation-Datenpaket **scanner-role** legt **Ticket Vendor – Scanner** an. Weisen Sie es unter **Einstellungen → System → Benutzer & Berechtigungen** einem separaten Benutzer zu und lassen Sie dessen Administrator-Schalter ausgeschaltet.

Die Rolle enthält ausschließlich `moorl_tv_ticket_sale:read` und `moorl_tv_ticket:scan`. Damit kann sie Veranstaltungen lesen, Tickets innerhalb einer Veranstaltung suchen und den definierten Check-in ausführen. Sie erhält keine allgemeine Ticketlese-/Schreibberechtigung, keinen PDF-, Versand- oder Widerrufszugriff und keinen Zugriff auf Kunden oder Bestellungen. Shopwares standardmäßige Login-Berechtigungen gelten zusätzlich.

Berechtigungen mehrerer Rollen addieren sich. Prüfen Sie daher auch weitere Rollen und verwenden Sie für Einlasspersonal keinen Administratorzugang. Die Rolle ist nicht auf einzelne Veranstaltungen beschränkt; sie kann für alle Veranstaltungen des Shops eingesetzt werden. Individuell geänderte Rollennamen, Rechte und Zuweisungen bleiben bei erneutem Import erhalten.

In den zusätzlichen Berechtigungen steht **Ticket Vendor → Tickets scannen und Veranstaltungen lesen** zur Verfügung. Bestehende Einlassrollen, die bislang nur `moorl_tv_ticket:update` und `moorl_tv_ticket_checkin:create` besitzen, benötigen das neue Scan-Recht oder die neue Rolle. Allgemeine Ticketänderungsrechte sind dafür nicht mehr nötig. Nach Rollenänderungen neu anmelden.

## Daten- und Demopakete

Das optionale Demopaket **standard** ergänzt eine eigenständige Demo-Site unter der Shop-Navigation. Die vorhandene Shop-Startseite und ihre Kategorie bleiben erhalten. Im Foundation-Demo-Assistenten **MoorlTicketVendor → standard** und den gewünschten Storefront-Verkaufskanal wählen.

| Seite | SEO-Pfad | Inhalt |
| --- | --- | --- |
| Einstieg | `/MoorlTicketVendor` | Eventtexte in drei Spalten und Social Links |
| Events | `/MoorlTicketVendor/Events` | Statisches Veranstaltungslisting |
| Booking | `/MoorlTicketVendor/Booking` | Artist-Roster mit Booking-Anfragen |
| Kontakt | `/MoorlTicketVendor/Kontakt` | Natives Shopware-Kontaktformular |

Alle drei Veranstaltungen und vier Artists erhalten eigene JPEG-Bilder mit **1080 × 1350 px (4:5)**. Sie liegen im Paket unter `media/moorl_tv_ticket_sale` beziehungsweise `media/moorl_tv_artist` und werden ausdrücklich in die zugehörigen Medienordner importiert. Die Social Links sind erkennbare Demo-Platzhalter; vor Verwendung eigene Profile eintragen. Das vergangene Digital Forum ist aktiv und erscheint als Archivbeispiel im statischen Veranstaltungslisting.

Leere Einstellungen für die Veranstaltungs- und Booking-Kontaktkategorie werden im gewählten Verkaufskanal mit den Demo-Kategorien vorbelegt. Bereits vorhandene Auswahlen bleiben erhalten. Beim Entfernen werden nur eigene Demo-Kategorien ohne fremde Unterkategorien und nicht anderweitig verwendete Demo-CMS-Seiten entfernt. Die Basis-CMS-Vorlagen und selbst angelegte Kategorien bleiben erhalten. Weiterverwendete Demo-Layouts, etwa in eigenen Kategorien oder Produkten, bleiben auch bei einer späteren Deinstallation erhalten. Bei einer Deinstallation ohne „Benutzerdaten behalten“ entfernt die anschließende Lifecycle-Bereinigung den Plugin-Kategoriebaum einschließlich selbst angelegter Unterkategorien. Dies ist das vorgesehene Deinstallationsverhalten. Sollen eigene Unterkategorien erhalten bleiben, diese vorher aus dem Demo-Baum verschieben.

Die regulären Foundation-Datenpakete installieren Medienordner, Import-/Exportprofile, Nummernkreis, Mailvorlage, SEO-Vorlage und Scanner-Rolle. Sie werden bei regulärer Aktivierung beziehungsweise Aktualisierung nachgeladen. Einzelne Pakete können über Foundations Datenverwaltung nachinstalliert werden.

Das optionale Demopaket **standard** enthält drei Veranstaltungen, zehn Tickettypen, zwölf Kundentickets und drei Check-in-Beispiele. „Live im Stadtpark“ umfasst Standard, VIP und die interne Gästeliste mit 20 Plätzen und drei gültigen Beispieltickets. Ein zukünftiger Fotografie-Workshop und ein vergangenes Forum zeigen weitere Statusfälle.

Die Daten brauchen keine Bestellung. Ein konfigurierter Foundation-Demokunde wird optional verknüpft. Nummern, Tokens und Versand-/Check-in-Status sind feste Beispieldaten; sie eignen sich nicht für produktiven Einlass. Der Import versendet selbst keine Mails. Laufende Worker können später noch nicht versendete gültige Demotickets aufgreifen; verwenden Sie deshalb eine Testumgebung mit Test-Mailtransport.

![Die Demo-Einstiegsseite verbindet Eventtexte mit dem gemeinsamen Seitenheader.](images/storefront-home.png)

![Social Links verbinden die Demo-Startseite mit externen Profilen; Beispielkonten vor der Nutzung ersetzen.](images/storefront-social-links.png)

## Häufige Fragen

**Warum ist die Veranstaltung im Shop nicht sichtbar?** Prüfen Sie Aktiv-Schalter, Anzeigezeitraum und Veranstaltungsende. Ohne Ende gilt der Beginn als öffentliche Verkaufsgrenze.

**Warum fehlt ein Tickettyp?** Er muss zur Veranstaltung gehören, aktiv sein und im eigenen Verkaufszeitraum liegen. Ein interner Gästelistentyp bleibt bewusst inaktiv.

**Warum ist ein Ticket trotz Bestellung nicht gültig?** Maßgeblich ist der bestätigte Zahlungsstatus, nicht allein die Bestellanlage oder eine Zahlungsankündigung.

**Warum kommt keine E-Mail?** Prüfen Sie Empfänger, Versandstatus, Mailvorlage, SMTP-Konfiguration sowie Messenger und geplante Aufgaben. Ein PDF-Download kann unabhängig vom Mailversand funktionieren.

**Können Gastbesteller Tickets erhalten?** Ja, der Versand kann die Bestell-E-Mail verwenden. Die Mail enthält außerdem einen persönlichen Link je Ticket, über den auch Gastbesteller dieses Ticket ohne Login bearbeiten und bei gültigem Status als PDF herunterladen können. Den Link vertraulich behandeln.

**Gibt es Sitzplätze oder Offline-Einlass?** Der aktuelle Umfang arbeitet mit Kontingenten je Tickettyp, ohne Sitzplan und ohne Offline-Freigabe. Die separate mobile App ist noch nicht vorhanden.

## Artists, Stages und geheime Gästeliste

Artists werden unter **Einstellungen → Erweiterungen → Ticketverkäufer - Artists** gepflegt. „Auf der Website für Booking anbieten“ zeigt das Profil in der Booking-Auswahl; Anfragen führen zur vorhandenen Kontaktseite oder zum optionalen externen Bookingkontakt. Gage und Bookingnotiz bleiben intern. Das CMS-Element „Artists für Booking“ und die Seite /artists/booking verwenden dieselbe Auswahl.

![Artist-Roster mit Genre, Booking-Verfügbarkeit, Kollektiv und Label.](images/admin-artists.png)

![Booking-Tab: interne Gage und Notiz, öffentliche Verfügbarkeit und externer Kontakt.](images/admin-artist-booking.png)

![Öffentliches Booking-Roster mit Artist-Bildern, Genres und individuellen Anfragelinks.](images/storefront-booking.png)

![Artists ohne externen Bookingkontakt führen zur konfigurierten Kontaktkategorie.](images/storefront-contact.png)

Im Event unter „Programm“ Stages und Auftritte anlegen. Ein Artist kann mehrere Sets haben; Stage, Uhrzeiten und ein eigenes Genre pro Auftritt sind optional. Ohne eigenes Genre zeigt die Timetable das Genre aus dem Artist-Profil. Der native Datum-/Uhrzeit-Picker erlaubt vollständige Zeitpunkte und Sets über Mitternacht. Line-up und Timetable werden am Event unabhängig freigegeben. Das gemeinsame Line-up führt jeden Artist einmal auf und hebt sein Kollektiv, ersatzweise das Label, in der Primärfarbe hervor. Jede Stage erhält eine eigene Timetable mit festen Spalten für Zeit, Artist und Genre; Auftritte ohne Stage stehen separat unter „Ohne Stage“. Kollektiv und Label stehen ausschließlich im Line-up. Beginn und Ende enthalten jeweils Datum und Uhrzeit und bleiben unabhängig optional. Die Eingabe und Ausgabe erfolgen in der Event-Zeitzone; gespeichert wird UTC. Die öffentliche Timetable zeigt nur Uhrzeiten; das Datum dient intern der Sortierung. Die Timetable sortiert nach Beginn; Auftritte ohne Beginn stehen zuletzt. Ein separates Auftrittsdatum entfällt. Eine optionale maximale Teilnehmerzahl begrenzt alle Tickettypen gemeinsam. „In öffentlichen Listen anzeigen“ kann ausgeschaltet werden; der direkte Eventlink bleibt erreichbar.

![Programm-Tab: Stages der Veranstaltung und zugeordnete Sets.](images/admin-program.png)

![Eine Stage über ihr Zeilenmenü bearbeiten.](images/admin-stage.png)

![Set-Bearbeitung mit Artist, Stage und vollständigen Start-/Endzeitpunkten in der Event-Zeitzone.](images/admin-performance.png)

![Veröffentlichtes Line-up und Timetable nach Stages, einschließlich eines Sets ohne feste Uhrzeit.](images/storefront-program.png)

Am kostenlosen Tickettyp unter Gästeliste die Registrierung aktivieren, Ehrenämter pflegen und den geheimen Link kopieren. Einleitung und Regeln bleiben am Event. Bei mehreren Storefront-Domains die gewünschte Linkadresse auswählen; der tatsächliche Formularaufruf bleibt als Anmeldungsursprung gespeichert. Tickets und Anmeldungen benötigen einen Verkaufskanal; bei manueller Anlage oder CSV-Import muss er ausgewählt bzw. zugeordnet werden. Eine fehlende Sprache wird mit der Shopware-Systemsprache vorbelegt. Neue Gästelisten-Tickets übernehmen beide Werte aus der Anmeldung. Bereits ausgestellte Tickets bleiben unverändert. Bei der Anmeldung ist die Handynummer Pflicht; separate Registrierungszeitfenster entfallen. Anmeldungen reservieren keinen Platz. Bei vollem Typkontingent oder voller Eventkapazität schließt das Formular automatisch und öffnet bei wieder freien Plätzen erneut. Nach Prüfung erstellt „Ticket erstellen und senden“ ein normales Ticket und stößt die E-Mail an; Wiederholungen verwenden dasselbe Ticket. Mehrere Gäste dürfen dieselbe E-Mail nutzen. Im Bearbeitungsdialog eines Gästelisteneintrags lassen sich alle verfügbaren Unterstützungsoptionen per Mehrfachauswahl zuordnen. Die Auswahl kann auch nach der Ticketausstellung ergänzt, geändert oder geleert werden. Tickets werden einzeln über das Kontextmenü der Anmeldung erstellt und versendet. Über „Bestätigungslink versenden“ im Kontextmenü kann die Bestätigung auch für manuelle und importierte Anmeldungen angefordert oder erneut versendet werden. Dafür ist das Zusatzrecht zum Versenden von Bestätigungslinks erforderlich. Bereits bestätigte Anmeldungen sind von der Aktion ausgenommen. Nach neuer Storefront-Anmeldung benachrichtigt der Flow „Ticket Vendor - Neue Gästelisten-Anmeldung“ standardmäßig die Administration mit Name, E-Mail, Handynummer und einem direkten Admin-Link zum Tickettyp. Empfänger und Vorlage lassen sich im Flow Builder anpassen; CSV-/Admin-Einträge und wiederholte Anfragen lösen diese Benachrichtigung nicht aus.

![Gästelisten-Anmeldungen und Formulareinstellungen am kostenlosen Tickettyp.](images/admin-guestlist.png)

![Anmeldung bearbeiten: Gast, Einladender, Tickettyp, Sprache und Verkaufskanal.](images/admin-guestlist-entry.png)

![Die private Anmeldeseite erläutert Veranstaltung und Gästelistenablauf.](images/storefront-guestlist.png)

![Das vollständige Anmeldeformular enthält Unterstützungsoptionen, Bemerkungen und die Zustimmung zu den Eventregeln.](images/storefront-guestlist-form.png)

Nach neuer Storefront-Anmeldung erhält auch der Gast eine Eingangsbestätigung mit individuellem Link „Anmeldung bestätigen“. Jede Anmeldung wird separat bestätigt, auch bei gemeinsamer E-Mail-Adresse. Das Aufrufen des signierten Links setzt direkt „Anmeldung bestätigt am“; eine weitere Aktion ist nicht erforderlich. Das ist keine Ticketfreigabe; die manuelle Ticketerstellung bleibt unverändert. Der separate Gast-Flow und die DE/EN-Vorlage gehören zu guestlist-mail. Bestands-, CSV- und Demoeinträge erhalten keine automatische Bestätigungsmail. Vor Bereitstellung die beiden neuen Gästelistenfelder bei bestehenden Datenbanken gemäß schema.md ergänzen; neue Installationen verwenden die SQL-Migrationen.

Gästelisteneinträge und Tickets lassen sich mit den jeweiligen Löschrechten einzeln oder per bestätigter Mehrfachauswahl löschen. Ein gelöschter Gästelisteneintrag lässt ein bereits ausgestelltes Ticket bestehen. Beim Löschen eines Tickets bleibt die Anmeldung ohne Ticketverknüpfung erhalten; die zugehörigen Check-in-Protokolle werden mitgelöscht. Belegtes Kontingent wird frei; Bestellungen und Kunden bleiben bestehen. Verknüpfte Check-ins können nicht einzeln gelöscht werden, Protokolle ohne Ticketzuweisung dagegen schon. Veranstaltungen lassen sich erst nach dem ausdrücklichen Löschen aller Tickets löschen; dann werden ihre Tickettypen, Anmeldungen, Bühnen, Auftritte und verbleibenden Check-ins mitgelöscht. Globale Artists und Unterstützungsoptionen bleiben bestehen. Die Migration `Migration1792713600EventDeletion` aktualisiert diese Löschregeln auch für vorhandene Tabellen; die übrigen Schemaübergänge stehen in [schema.md](schema.md).

Neue Installationen verwenden die mitgelieferten SQL-Migrationen. Bestehende Tabellen und Daten vor dem Update gezielt abgleichen. Bestehende Bestellpositionsbezüge müssen vor dem Entfernen der alten Spalten übernommen werden; der Befehl moorl-tv:backfill-ticket-orders zeigt zunächst nur eine Vorschau. Ablauf und explizite Anwendung stehen in [Schema und Datenübernahme](schema.md). Anschließend Administration/Storefront bauen und Worker neu starten.
