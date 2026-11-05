# Veranstaltungsserien

Eine Serie bündelt gemeinsame Inhalte mehrerer Veranstaltungen. Die Zuordnung ist optional: Einzelevents funktionieren weiterhin wie bisher.

## Serie und Termine verwalten

Unter **Kataloge → Veranstaltungsserien** eine Hauptveranstaltung anlegen und Texte, Medien, Veröffentlichung, SEO und CMS-Layout pflegen. Der Tab **Termine** zeigt die Veranstaltungen im normalen Entity-Grid. Über **Vorhandene Veranstaltung zuordnen** in der oberen Aktionsleiste wird eine Veranstaltung im Modal ausgewählt und ausdrücklich zugeordnet. **Termine generieren** öffnet dort den Generator als eigenes Modal. Eine neue einzelne Veranstaltung zunächst speichern und danach zuordnen.

In der Storefront verwenden zugeordnete Veranstaltungen Namen, Beschreibung, Teaser, Suchbegriffe, Titelbild, Banner und Meta-Inhalte ihrer Serie. In der Storefront werden lokale Inhalte während der Zuordnung nicht angezeigt oder für die Inhaltssuche verwendet. Eigene Überschreibungen gibt es dort nicht. Im Admin bleiben die eigenen Texte, Bilder und Metadaten des Events sichtbar und bearbeitbar; Listen und Auswahlfelder verwenden die eigenen Inhalte. Es gibt keine Vererbungsanzeige oder separate Serienvorschau. Die Zuordnung wird ausschließlich über das optionale Feld **Veranstaltungsserie** geändert oder geleert. Datum, Zeitzone, Ort, Preise, Tickettypen, Kontingente, Programm und Gästeliste bleiben am Termin. Ortsbeschreibung, Tickettyptexte und Gästelistenregeln werden nicht vererbt.

Beim Abtrennen werden die aktuellen gemeinsamen Serieninhalte in die Veranstaltung übernommen, einschließlich Übersetzungen und Medienreferenzen. Danach ist sie ein unabhängig bearbeitbares Einzelevent. Ein Wechsel der Serie ist eine ausdrückliche Zuordnungsaktion. Eine Serie mit zugeordneten Veranstaltungen lässt sich nicht löschen.

## Veröffentlichung

Ein Termin wird nur öffentlich angezeigt und verkauft, wenn seine eigenen Freigaben und die Freigaben der Serie erfüllt sind. Das Deaktivieren der Serie verändert die gespeicherten Aktiv-Schalter der Termine nicht. Nach der Reaktivierung gelten die individuellen Freigaben erneut. Bestehende Tickets bleiben abrufbar und gemäß den bisherigen Regeln einlösbar.

Die Option **Gelistet** betrifft die Auffindbarkeit der Serie im Listing, nicht die Aktivierung ihrer Termine. Ein aktiver direkter Serienaufruf ohne kommende Termine zeigt eine leere Terminübersicht. Dynamische Serienlistings zeigen Serien mit verfügbaren Terminen; das statische Element erlaubt zusätzlich eine Übersicht ohne kommende Termine.

## Termine generieren

Die Serie speichern und oben **Termine generieren** öffnen. Im Modal einen gespeicherten Mustertermin auswählen. Dessen Zeitzone, Ort, operative Einstellungen und Tickettypen werden als Vorlage verwendet. Die gemeinsamen Inhalte kommen von der gewählten Zielserie. Nach erfolgreicher Generierung schließt sich das Modal und die Terminliste wird aktualisiert; ungespeicherte Änderungen an der Serie bleiben erhalten.

1. Lokalen Beginn festlegen.
2. **Intervall in Tagen** wählen, beispielsweise alle 3 oder 14 Tage, oder **Wochentage**, beispielsweise Montag und Donnerstag jeder Woche.
3. Anzahl der Termine oder letztes Datum einschließlich festlegen.
4. Aktiv oder inaktiv anlegen auswählen. Die Wahl gilt für neue Termine und ihre neuen Tickettypen. Eine deaktivierte Serie wird dadurch nicht aktiviert.
5. Vorschau prüfen und die Termine anlegen.

Die Vorschau ist auf 250 Termine und bei einem Enddatum auf fünf Jahre begrenzt. Alle Termine behalten die lokale Uhrzeit ihrer Vorlage; Sommerzeitwechsel werden berücksichtigt. Nicht existierende oder doppeldeutige lokale Uhrzeiten werden abgewiesen. Eine monatliche Wiederholung ist nicht vorgesehen.

Tickets, Bestellungen, Kunden, Einlösungen, Anmeldungen, Verkaufszähler, Bühnen, Auftritte und geheime Gästelistenlinks werden nicht kopiert. Neue Gästelisten sind zunächst deaktiviert. Bereits erzeugte Slots werden bei Wiederholung übersprungen; vorhandene Termine und deren Aktivierung werden nicht nachträglich geändert. Nach Änderung der Eingaben oder der Vorlage ist eine neue Vorschau erforderlich.

## CMS und Suche

Serien besitzen eine eigene Detailroute `/moorl-tv/series/{seriesId}` und eigene SEO-URLs. Ein eigenes Serienlayout kann am Datensatz ausgewählt werden; ansonsten greift die Plugin-Konfiguration **Standard-CMS-Seite für Seriendetails** und danach das mitgelieferte Layout. Die Layouts der einzelnen Veranstaltungen bleiben separat.

Die Erlebniswelten bieten **Seriendetail**, **Serienlisting**, **statisches Serienlisting** und **Serientermine**. Das Terminelement verwendet die aktuelle Serie oder eine ausdrücklich ausgewählte Serie. Ohne Serienkontext zeigt es keine fremden Termine. Die Suche und Suchvorschläge haben eigene Schalter und Limits in der Plugin-Konfiguration; Foundations erweiterte Suche muss aktiv sein.

Redaktionelle Benutzer benötigen zusätzlich die passenden Serienrechte. Der Scanner benötigt weiterhin nur seine bisherigen Scan-/Eventleserechte und sucht Veranstaltungen über eine begrenzte Projektion. Tickets gelten ausschließlich für ihren konkreten Termin.

## Upgrade und Demodaten

Die neue additive `Migration1793871339EventSeries` läuft nach `Migration1793194127Initial`. Die Initialmigration bleibt unverändert. Bestehende Veranstaltungen behalten IDs, Inhalte, URLs, Ticketbezüge und `seriesId = NULL`; es erfolgt keine automatische Gruppierung. Das Update erfolgt über den regulären Shopware-Plugin-Updateprozess. Danach Administration neu bauen und Assets/Cache über den bestehenden Deploymentablauf aktualisieren.

Das optionale Foundation-Demopaket **series** enthält eine Serie mit Terminen in Berlin und Hamburg und jeweils einem Tickettyp. Zusätzlich legt es unter der Navigation des ausgewählten Verkaufskanals die Kategorie **Veranstaltungsserien** mit einer eigenen CMS-Übersichtsseite an. Die Übersicht unter `/MoorlTicketVendor/Series` zeigt gezielt die Demo-Serie und verlinkt deren Termine. Bereits geladene Pakete erneut importieren, um die Übersicht zu ergänzen.

Das Paket ist unabhängig vom Paket **standard** und verwendet eine eigene Kennung für die Entfernung seiner Demodaten. Selbst ergänzte Unterkategorien und anderweitig verwendete Übersichtslayouts bleiben beim Entfernen erhalten. Es erzeugt keine Kunden, Tickets oder Check-ins.
