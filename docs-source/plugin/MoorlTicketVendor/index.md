---
description: "Veranstaltungen und Eintrittskarten direkt in Shopware verkaufen: mit Kontingenten, PDF-/QR-Tickets, Zahlungsfreigabe, Gästelistentickets und Online-Check-in."
tags:
  - Tickets
  - Veranstaltungen
  - Gästeliste
  - Check-in
  - Shopware 6.7
---

# Ticket Vendor – Veranstaltungen und Eintrittskarten

Veranstaltungen und Eintrittskarten direkt in Shopware verkaufen: mit Kontingenten, PDF-/QR-Tickets, Zahlungsfreigabe, Gästelistentickets und Online-Check-in.

Mit Ticket Vendor verwalten Sie Veranstaltungen, verkaufen Eintrittskarten über den Shopware-Warenkorb und prüfen diese beim Einlass. Veranstaltung, Tickettyp und individuelles Kundenticket sind eigene Datensätze. Sie müssen dafür keine Shopware-Produkte anlegen.

Diese Anleitung beschreibt den vorhandenen Pluginumfang. Der Browser-Scanner gehört bereits zum Plugin. Eine eigenständige mobile Scanner-App ist noch nicht verfügbar; ihr vorgesehener Ablauf und die vorhandene Schnittstelle stehen in der [App-Dokumentation](mobile-app.md).

## Wegweiser

- [Installation, Updates und Betrieb](manual.md)
- [Kurzanleitung für Ihre Kunden](customer.md)
- [Mobile Scanner-App und API-Vertrag](mobile-app.md)
- [Storebeschreibung](store.md)
- [Technische Laufzeitdetails](runtime.md)
- [Datenmodell und Schema](schema.md)

## Voraussetzungen und erster Ablauf

Ticket Vendor setzt Shopware 6.7 mit Storefront und MoorlFoundation 1.7 voraus. Foundation stellt unter anderem Formulare, Listen, CMS-Helfer und Datenpakete bereit. Installieren und aktivieren Sie Foundation zuerst. Für Zahlungsfristen und automatischen Versand müssen Shopwares geplante Aufgaben und Nachrichtenverarbeitung laufen.

Ein erster vollständiger Durchlauf sieht so aus:

1. Unter **Kataloge → Veranstaltungen** eine Veranstaltung erstellen.
2. Beginn, Ende, Ort und Inhalte pflegen; Veranstaltung aktivieren und den Status `published` setzen.
3. Einen aktiven Tickettyp mit Preis, Steuer und Kontingent zuordnen.
4. Eine Kategorie mit dem CMS-Veranstaltungslisting anlegen und in der Plugin-Konfiguration unter **Seite mit Veranstaltungen (Liste)** auswählen. Die Veranstaltung über diese Kategorie öffnen und eine Testbestellung aufgeben.
5. Den tatsächlichen Zahlungsablauf prüfen. Sobald Shopware die maßgebliche Transaktion als `paid` meldet, werden die Tickets gültig und zum Versand vorgemerkt.
6. Das PDF im Kundenkonto beziehungsweise in der Administration öffnen.
7. Im Ticketscanner dieselbe Veranstaltung auswählen und den QR-Code einmal einlösen. Ein weiterer Scan muss als bereits eingelöst erkannt werden.

## Veranstaltungen verwalten

Die Veranstaltungsliste zeigt die angelegten Veranstaltungen. Die Detailansicht bündelt Stammdaten, öffentliche Inhalte, Ort sowie zugeordnete Tickettypen, Kundentickets und Check-in-Protokolle.

| Bereich | Verwendung |
| --- | --- |
| Name und Beschreibung | Öffentliche Bezeichnung und ausführliche Veranstaltungsinformationen; übersetzbare Inhalte in den verwendeten Shopsprachen pflegen. |
| Aktiv und Status | Öffentlicher Verkauf setzt eine aktive Veranstaltung mit Status `published` voraus. |
| Beginn und Ende | Zeitpunkt der Veranstaltung. Ein Enddatum beendet auch die Gültigkeitsprüfung am Einlass. |
| Zeitzone | IANA-Bezeichnung, etwa `Europe/Berlin`. Zeitangaben werden technisch in UTC gespeichert; bei Importen UTC verwenden. |
| Anzeigen ab/bis | Separates Zeitfenster für öffentliche Sichtbarkeit und Verkauf. Es ersetzt die Veranstaltungszeiten nicht. |
| Veranstaltungsort und Adresse | Ortsname, Hinweise, Straße, Postleitzahl, Stadt und Land. |
| Medien und SEO | Bilder, Teaser, Metadaten und weitere Foundation-Inhalte für die öffentliche Darstellung. |
| Erlebniswelt | Optional eine CMS-Seite für die Veranstaltungsdetailseite zuordnen. |

Eine öffentliche Veranstaltung benötigt ein passendes Anzeigezeitfenster. Ist ein Endzeitpunkt vorhanden, endet der öffentliche Verkauf mit diesem; ohne Endzeitpunkt bereits mit dem Beginn. Für einen früheren Vorverkaufsschluss setzen Sie zusätzlich „Anzeigen bis“.

Die Veranstaltung besitzt keinen technischen Namen. Ihre Identität ergibt sich aus der ID; der übersetzte Name dient der Darstellung. Bereits verwendete Datensätze lassen sich wegen ihrer Ticket- und Protokollbezüge nicht beliebig löschen. Verwenden Sie zum Beenden des Verkaufs Sichtbarkeit und Status.

## Tickettypen, Preise und Kontingente

Tickettypen stehen unter **Einstellungen** zur Verfügung und können außerdem innerhalb ihrer Veranstaltung verwaltet werden. Ein Tickettyp gehört genau einer Veranstaltung, beispielsweise „Standard“, „VIP“ oder „Gästeliste“.

| Feld | Bedeutung |
| --- | --- |
| Veranstaltung | Zugehörige Veranstaltung. Ein Typ mit ausgestellten Tickets kann nicht in eine andere Veranstaltung verschoben werden. |
| Name | Bezeichnung für Kunden und Verwaltung. |
| Technischer Name | Technische Kennung des Tickettyps, beispielsweise `concert-vip`. |
| Aktiv | Aktive Typen können öffentlich angeboten werden. Inaktive Typen eignen sich für interne Einladungen. |
| Preis und Steuer | Shopware-Preise und Steuersatz. Die Preisberechnung erfolgt serverseitig in der Warenkorbwährung. |
| Gesamtkontingent | Maximale Zahl gleichzeitig belegter Plätze dieses Typs. |
| Verkaufte Tickets | Automatisch berechnete Belegung; das Feld ist schreibgeschützt und zählt auch offene und bereits eingelöste Tickets. |
| Mindest-/Maximalabnahme | Zulässige Gesamtmenge dieses Typs im Kaufvorgang. |
| Anzeigen ab/bis | Optionaler Verkaufszeitraum zusätzlich zur Veranstaltung. |
| Position | Reihenfolge der Tickettypen. |

`pending`, `valid` und `redeemed` belegen das Kontingent. `expired` und `revoked` geben es frei. Ein eingelöstes Ticket gibt keinen Platz für einen weiteren Verkauf frei. Ein Warenkorb reserviert noch keinen Platz; die Belegung entsteht erst beim Bestellabschluss. Die abschließende Kontingentprüfung und Ticketerstellung erfolgen gemeinsam, sodass konkurrierende Käufe nicht denselben letzten Platz erhalten.

Auch manuell erstellte Tickets unterliegen der Kontingentprüfung. Das Gesamtkontingent darf nicht unter die bestehende Belegung gesenkt werden.

## Öffentliche Darstellung und Erlebniswelten

Die in der Plugin-Konfiguration unter `category` gewählte Shopware-Kategorie verwendet eine Erlebniswelt mit dem Element `moorl-tv-ticket-sale-listing`. Sie zeigt verfügbare Veranstaltungen mit Seitennavigation und ist das Ziel des Zurück-Links auf Veranstaltungsdetails. Die Detailseite `/tickets/{saleId}` verwendet die am Event hinterlegte CMS-Seite, ersatzweise die konfigurierte Standardseite `cmsPageId`. Ohne CMS-Auswahl wird die einfache Detaildarstellung verwendet; ohne ausgewählte Kategorie entfällt der Zurück-Link. Der Ticketkauf verwendet den normalen Shopware-Warenkorb und Checkout. Tickets sind digitale Warenkorbpositionen; sie benötigen keinen physischen Versand.

Über das Foundation-CMS-Element **Veranstaltungen** (`moorl-tv-ticket-sale-listing`) können Sie eine Veranstaltungsliste in Erlebniswelten einbinden. Die Veranstaltungsdetailseite kann zusätzlich ihre zugewiesene CMS-Seite laden.

Die mitgelieferte SEO-Vorlage erzeugt URLs nach dem Muster `tickets/<Veranstaltungsname>/<ID>`. Nach Änderungen müssen die SEO-Indizes aktuell sein. Ein vorhandenes, angepasstes SEO-Template wird bei erneutem Datenimport erhalten.

## Bestellung, Bezahlung und automatische Freigabe

Für jede gekaufte Einheit entsteht ein eigenes Ticket. Eine Bestellposition mit Menge drei erzeugt also drei Ticketnummern und drei QR-Codes. Mehrere Kategorien einer Veranstaltung und Tickets verschiedener Veranstaltungen können in einer Bestellung vorkommen.

Bestelltickets starten mit **Zahlung ausstehend**. Standardmäßig beträgt die Zahlungsfrist 30 Minuten; sie ist in der Erweiterungskonfiguration über **Zahlungsfrist in Minuten** einstellbar. Der vollständige native Zahlungsstatus `paid` schaltet Tickets frei. Eine offene, autorisierte oder nur teilweise bezahlte Transaktion genügt nicht. Auch ein Checkout mit Preis 0 benötigt den entsprechenden nativen Zahlungsabschluss; verwenden Sie für sofort gültige Einladungen die manuelle Anlage.

Der Ablaufjob prüft die tatsächliche Zahlung erneut. Offene, überfällige Bestellungen werden über die nativen Statusübergänge storniert; die zugehörigen Tickets laufen ab und geben ihr Kontingent frei. Das kann die gesamte Bestellung einschließlich weiterer Positionen betreffen. Berücksichtigen Sie dies bei Mischwarenkörben und Zahlungsmethoden mit längerer Zahlungsdauer.

Bestellstornierung, vollständige Erstattung und Chargeback widerrufen noch belegende Tickets. Bereits stornierte Bestellungen werden durch eine spätere Zahlung nicht automatisch wieder freigegeben. Prüfen Sie solche Fälle im Zahlungsanbieter und in Shopware manuell. Das Plugin veranlasst keine eigene Rückerstattung beim Zahlungsanbieter.

## Kundentickets und Status

Generierte Tickets finden Sie in der Veranstaltung sowie in den Ticket-Tabs der Bestell- und Kundendetails. Die Ticketansicht zeigt unter anderem Nummer, Veranstaltung, Typ, Empfänger, Bestellbezug, Gültigkeits- und Versandstatus.

| Ticketstatus | Bedeutung |
| --- | --- |
| `pending` – Zahlung ausstehend | Platz belegt, noch kein Einlass und kein gültiges Ticket-PDF. |
| `valid` – Gültig | Freigegeben und beim passenden offenen Event einlösbar. |
| `redeemed` – Eingelöst | Bereits verwendet; ein weiterer eigenständiger Scan wird abgewiesen. |
| `expired` – Abgelaufen | Zahlungsfrist abgelaufen; keine Einlassberechtigung. |
| `revoked` – Widerrufen | Gesperrt, etwa nach Stornierung oder manuellem Widerruf. |

Die Ticketnummer stammt aus dem nativen Nummernkreis **Ticketnummern** (`moorl_tv_ticket`), standardmäßig `T-{n}` ab 10000. Sie wird beim Speichern vergeben und anschließend unveränderlich angezeigt. Der QR-Code enthält einen separaten zufälligen Ticket-Token. Die sichtbare Ticketnummer ist deshalb kein Ersatz für den QR-Code oder Token beim Scannen.

## Manuelle Tickets und Gästeliste

Sie können innerhalb einer Veranstaltung direkt ein neues Kundenticket anlegen. Der Veranstaltungsbezug wird vorbelegt, und die Typauswahl enthält nur deren Tickettypen. Bestellung und Kundenkonto sind optional. Manuelle Tickets starten mit Status **Gültig**; sie warten nicht auf eine Zahlung.

Für eine interne Gästeliste:

1. Einen Tickettyp „Gästeliste“ mit Preis 0 und eigenem Kontingent anlegen.
2. Den Typ **inaktiv** lassen, damit er nicht öffentlich verkauft wird. Die Veranstaltung selbst muss für den Einlass aktiv und `published` bleiben.
3. Für jeden Gast ein Ticket dieses Typs erstellen.
4. Optional einen Kunden oder eine Empfänger-E-Mail zuordnen.
5. Das PDF ausgeben oder gezielt versenden und beim Einlass regulär scannen.

Ein Ticket ohne Kundenkonto und ohne Bestellposition ist zulässig. Ohne erreichbaren E-Mail-Empfänger ist es speicherbar und kann als PDF ausgegeben werden; für den Versand muss ein Empfänger ergänzt werden. Der automatische Wiederherstellungslauf berücksichtigt auch noch nicht versendete gültige manuelle Tickets: Das Speichern eines Tickets mit Empfänger ist daher kein dauerhafter „nur speichern“-Modus.

Eine namentliche Gästelistenverwaltung mit freien Vor-/Nachnamen, Begleitpersonenzähler oder Einlasssuche nach Namen ist nicht enthalten. Der vorhandene Ablauf arbeitet mit individuellen Tickets und Codes.

## PDF und E-Mail-Versand

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
2. **Kataloge → Ticketscanner** öffnen.
3. Die richtige Veranstaltung auswählen.
4. **QR mit Kamera scannen** starten und gegebenenfalls die Kameraberechtigung erteilen. Alternativ den Ticket-Token manuell eingeben oder mit einem geeigneten Scanner als Text erfassen.
5. Das Ergebnis prüfen. Nur **Check-in akzeptiert** bestätigt eine neue Einlösung.

Der Scanner füllt den Bildschirm aus und passt seine Bedienelemente an Smartphones und Tablets an. **Kamera** und **Manuell** wechseln die Erfassungsart. Nach einem Ergebnis startet **Nächstes Ticket** die Kamera erneut oder fokussiert die manuelle Eingabe. Erfolgreiche Einlösung, bereits eingelöstes Ticket und Ablehnung werden mit Text, Symbol und unterschiedlichen Farben angezeigt.

Über **Vollbild öffnen** lässt sich zusätzlich der Browser-Vollbildmodus aktivieren, sofern das Gerät ihn unterstützt. **Zur Administration** verlässt die Scanneransicht. Beim Verlassen oder Wechsel zur manuellen Eingabe wird die Kamera gestoppt. Bei einem Verbindungsfehler bleiben Token und Anfrage-ID für **Erneut prüfen** erhalten.

Die Kameraerkennung setzt einen sicheren Browserkontext, üblicherweise HTTPS, und Unterstützung für `BarcodeDetector` voraus. Die manuelle Eingabe bleibt auch ohne Kameraerkennung nutzbar. Es ist eine Onlineverbindung zum Shop erforderlich.

| Ergebnis | Vorgehen am Einlass |
| --- | --- |
| Check-in akzeptiert | Einlass gewähren. Das Ticket wurde eingelöst. |
| Ticket bereits eingelöst | Keinen weiteren Einlass allein anhand dieses Codes gewähren; Klärung durch Veranstaltungsleitung. |
| Andere Veranstaltung | Veranstaltungsauswahl prüfen. |
| Veranstaltung geschlossen | Aktivierung, Status und Endzeit durch die Verwaltung prüfen lassen. |
| Ticket nicht gültig | Zahlung, Ablauf oder Widerruf durch die Verwaltung prüfen lassen. |
| Unbekanntes Ticket | Vollständigen Code prüfen; bei Bedarf Verwaltung einschalten. |
| Netzwerkfehler | Es liegt noch kein verlässliches Ergebnis vor. Denselben Scan erneut versuchen. |

Die API verhindert eine doppelte Einlösung bei parallelen Scans. Eine technische Wiederholung derselben Anfrage liefert das ursprüngliche Ergebnis, ein neuer Scan eines eingelösten Tickets meldet dagegen „bereits eingelöst“. Das Check-in-Protokoll dokumentiert Ergebnis, Zeitpunkt, Anfrage-ID und gegebenenfalls Gerät sowie Benutzer/Integration. Es bietet keine Funktion zum Zurücksetzen eines Check-ins.

Der Einlass verlangt eine aktive, veröffentlichte Veranstaltung, deren vorhandenes Enddatum nicht überschritten ist. Es gibt derzeit keine separate konfigurierbare Einlassöffnung: Ein künftiger Veranstaltungsbeginn verhindert einen Scan allein nicht.

## Benutzer und Scanner-Rolle

Das Foundation-Datenpaket **scanner-role** legt **Ticket Vendor – Scanner** an. Weisen Sie es unter **Einstellungen → System → Benutzer & Berechtigungen** einem separaten Benutzer zu und lassen Sie dessen Administrator-Schalter ausgeschaltet.

Die Rolle enthält ausschließlich `moorl_tv_ticket_sale:read` und `moorl_tv_ticket:scan`. Damit kann sie Veranstaltungen lesen und den definierten Check-in ausführen. Sie erhält keine allgemeine Ticketlese-/Schreibberechtigung, keinen PDF-, Versand- oder Widerrufszugriff und keinen Zugriff auf Kunden oder Bestellungen. Shopwares standardmäßige Login-Berechtigungen gelten zusätzlich.

Berechtigungen mehrerer Rollen addieren sich. Prüfen Sie daher auch weitere Rollen und verwenden Sie für Einlasspersonal keinen Administratorzugang. Die Rolle ist nicht auf einzelne Veranstaltungen beschränkt; sie kann für alle Veranstaltungen des Shops eingesetzt werden. Individuell geänderte Rollennamen, Rechte und Zuweisungen bleiben bei erneutem Import erhalten.

In den zusätzlichen Berechtigungen steht **Ticket Vendor → Tickets scannen und Veranstaltungen lesen** zur Verfügung. Bestehende Einlassrollen, die bislang nur `moorl_tv_ticket:update` und `moorl_tv_ticket_checkin:create` besitzen, benötigen das neue Scan-Recht oder die neue Rolle. Allgemeine Ticketänderungsrechte sind dafür nicht mehr nötig. Nach Rollenänderungen neu anmelden.

## Daten- und Demopakete

Der Demoimport legt die aktive Kategorie **Veranstaltungen** unter der Shop-Navigation an und weist ihr die CMS-Vorlage **Ticket Vendor – Events** mit dem Veranstaltungslisting zu. Der Einstieg erfolgt über die normale Kategorienavigation; ein zusätzlicher Tickets-Link in den Header-Aktionen entfällt. Beim Entfernen des Demopakets wird die Demo-Kategorie entfernt, sofern sie keine Unterkategorien enthält. Die CMS-Vorlage und selbst angelegte Kategorien bleiben erhalten.

Die regulären Foundation-Datenpakete installieren Medienordner, Import-/Exportprofile, Nummernkreis, Mailvorlage, SEO-Vorlage und Scanner-Rolle. Sie werden bei regulärer Aktivierung beziehungsweise Aktualisierung nachgeladen. Einzelne Pakete können über Foundations Datenverwaltung nachinstalliert werden.

Das optionale Demopaket **standard** enthält drei Veranstaltungen, sieben Tickettypen, zwölf Kundentickets und drei Check-in-Beispiele. „Live im Stadtpark“ umfasst Standard, VIP und die interne Gästeliste mit 20 Plätzen und drei gültigen Beispieltickets. Ein zukünftiger Fotografie-Workshop und ein vergangenes Forum zeigen weitere Statusfälle.

Die Daten brauchen keine Bestellung. Ein konfigurierter Foundation-Demokunde wird optional verknüpft. Nummern, Tokens und Versand-/Check-in-Status sind feste Beispieldaten; sie eignen sich nicht für produktiven Einlass. Der Import versendet selbst keine Mails. Laufende Worker können später noch nicht versendete gültige Demotickets aufgreifen; verwenden Sie deshalb eine Testumgebung mit Test-Mailtransport.

## Häufige Fragen

**Warum ist die Veranstaltung im Shop nicht sichtbar?** Prüfen Sie Aktiv-Schalter, `published`, Anzeigezeitraum und Veranstaltungsende. Ohne Ende gilt der Beginn als öffentliche Verkaufsgrenze.

**Warum fehlt ein Tickettyp?** Er muss zur Veranstaltung gehören, aktiv sein und im eigenen Verkaufszeitraum liegen. Ein interner Gästelistentyp bleibt bewusst inaktiv.

**Warum ist ein Ticket trotz Bestellung nicht gültig?** Maßgeblich ist der bestätigte Zahlungsstatus, nicht allein die Bestellanlage oder eine Zahlungsankündigung.

**Warum kommt keine E-Mail?** Prüfen Sie Empfänger, Versandstatus, Mailvorlage, SMTP-Konfiguration sowie Messenger und geplante Aufgaben. Ein PDF-Download kann unabhängig vom Mailversand funktionieren.

**Können Gastbesteller Tickets erhalten?** Ja, der Versand kann die Bestell-E-Mail verwenden. Der Kontodownload erfordert dagegen einen berechtigten Login; es gibt keinen öffentlichen Gast-Downloadlink.

**Gibt es Sitzplätze oder Offline-Einlass?** Der aktuelle Umfang arbeitet mit Kontingenten je Tickettyp, ohne Sitzplan und ohne Offline-Freigabe. Die separate mobile App ist noch nicht vorhanden.
