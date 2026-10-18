# Strukturierte Eventdaten

Die Detailseite einer Veranstaltung veröffentlicht einmalig ein JSON-LD-Objekt nach [schema.org/Event](https://schema.org/Event). Dies gilt auch bei einer CMS-Erlebniswelt für die Eventseite. Listings, Kundenkonto und Warenkorb erzeugen keine zusätzlichen Event-Objekte.

## Automatische Angaben

| Eigenschaft | Quelle |
| --- | --- |
| `@context`, `@type` | `https://schema.org`, `Event` |
| `@id`, `url`, `mainEntityOfPage` | Absolute SEO-URL des Events im aktuellen Verkaufskanal |
| `identifier` | Event-ID |
| `name`, `description`, `keywords` | Übersetzte Eventtexte; Beschreibung ohne HTML, ersatzweise Teaser |
| `startDate`, `endDate`, `duration` | Eventzeiten mit Offset der eingestellten Event-Zeitzone; Dauer nur bei positivem Zeitabstand |
| `image` | Eventbild, soweit vorhanden |
| `location` | Veranstaltungsort, Postadresse, Land/Region und vorhandene Koordinaten |
| `eventStatus`, `eventAttendanceMode` | Ausgangswerte `EventScheduled`, `OfflineEventAttendanceMode` |
| `offers` | Aktuell öffentliche Tickettypen mit Preis, Währung, Verfügbarkeit und Verkaufsfristen |
| `maximumAttendeeCapacity`, `remainingAttendeeCapacity` | Summe der Kontingente bzw. freien Plätze der aktuell öffentlichen Tickettypen |
| `isAccessibleForFree` | Nur bei vorhandenen Preisen: wahr, wenn alle öffentlichen Tickettypen kostenlos sind |

Preise verwenden dieselbe Preisermittlung wie der Verkauf: Währung, Umrechnungsfaktor und Steueranzeige des Kundenkontexts. Ausverkaufte Angebote werden als `SoldOut` ausgegeben oder entsprechend der Anzeigeoption ausgeblendet. Interne Tickettypen und Kategorien außerhalb ihres Anzeigezeitraums werden nicht veröffentlicht. Fehlende optionale Daten werden ausgelassen. Es werden keine Kundendaten, Ticketinhaber, E-Mail-Adressen, Handynummern oder Ticket-Tokens übernommen.

## Weitere Eigenschaften pflegen

Unter **Event → SEO → Strukturierte Eventdaten (schema.org)** steht **Zusätzliche Event-Eigenschaften (JSON)** zur Verfügung. Das übersetzbare Feld `schemaOrg` akzeptiert ein JSON-Objekt mit beliebigen Eigenschaften des Event-Vokabulars und seiner Oberklasse `Thing`, einschließlich verschachtelter Objekte und Listen. Es gibt keine auf einzelne Eigenschaften beschränkte Positivliste.

Beispiel:

```json
{
  "@type": "MusicEvent",
  "organizer": {
    "@type": "Organization",
    "name": "Stadtpark Veranstaltungen",
    "url": "https://example.com"
  },
  "performer": [
    { "@type": "MusicGroup", "name": "Park Band" }
  ],
  "doorTime": "2027-07-17T17:30:00+02:00",
  "inLanguage": "de",
  "typicalAgeRange": "16-",
  "eventStatus": "https://schema.org/EventScheduled"
}
```

Damit sind auch `about`, `actor`, `aggregateRating`, `attendee`, `audience`, `composer`, `contributor`, `director`, `funder`, `funding`, `hasParticipationOffer`, `hasSponsorshipOffer`, `maximumPhysicalAttendeeCapacity`, `maximumVirtualAttendeeCapacity`, `previousStartDate`, `recordedIn`, `review`, `sponsor`, `subEvent`, `superEvent`, `translator`, `workFeatured` und `workPerformed` sowie geerbte Eigenschaften wie `alternateName`, `sameAs` oder `potentialAction` pflegbar. Solche Angaben werden ausschließlich aus diesem ausdrücklich veröffentlichten Metadatenfeld übernommen, nicht aus privaten Ticketdaten.

Eigene Angaben ersetzen die jeweilige automatische Eigenschaft vollständig. So kann `location` ein `VirtualLocation`-Objekt oder eine Liste physischer und virtueller Orte sein. `null` entfernt eine optionale automatische Eigenschaft. Der schema.org-Kontext bleibt fest vorgegeben. Ein `eventSchedule` ersetzt in der Ausgabe `startDate`, `endDate` und `duration`; die Zeitangaben stehen dann im `Schedule`-Objekt. Das erzeugt keine wiederkehrenden Verkaufsveranstaltungen oder Tickets.

Eine leere Eingabe entfernt die Ergänzungen dieser Sprache; Shopwares Sprachfallback bleibt wirksam. Ungültiges JSON oder ein anderer Wurzeltyp als ein Objekt wird im Editor angezeigt und beim Speichern durch die DAL-Typprüfung abgewiesen. Die fachliche Eignung der schema.org-Eigenschaften liegt beim Autor; hierfür den [Schema Markup Validator](https://validator.schema.org/) verwenden. Bei Google gelten zusätzlich dessen [Event-Richtlinien](https://developers.google.com/search/docs/appearance/structured-data/event).

`eventStatus` ist eine Suchmaschinenangabe für z. B. Absage oder Verschiebung. Sie ersetzt keinen Aktiv-Schalter und verändert weder Verkauf noch Scannerfreigabe. Auch alle anderen Metadaten verändern keine Kontingente, Preise oder Buchungsregeln.

## Schema und Deployment

Die bestehende Tabelle `moorl_tv_ticket_sale_translation` erhält die nullable JSON-Spalte `schema_org`. Sie wird aus `TicketSaleTranslationDefinition` mit dem externen Schemawerkzeug erzeugt; keine zusätzliche PHP-Migration. Anschließend Cache leeren und Administration bauen. Das öffentliche Schema und die REST-API stellen das Feld als `schemaOrg` bereit.
