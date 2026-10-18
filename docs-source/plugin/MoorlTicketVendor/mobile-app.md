# Mobile Scanner-App: Zielbild und vorhandene Schnittstelle

## Verfügbarkeit

**Eine eigenständige mobile Scanner-App existiert derzeit noch nicht.** Dieses Dokument ist die fachliche und technische Grundlage für ihre spätere Entwicklung. Es gibt noch keinen App-Download, keine Store-Veröffentlichung, keine native Kameraimplementierung und keinen Offline-Modus.

Bereits vorhanden sind der Browser-Scanner in der Shopware-Administration, die Scanner-Rolle und der authentifizierte Check-in-Endpunkt. Die folgenden Abschnitte trennen das geplante App-Verhalten vom heute nutzbaren API-Vertrag.

## Vorgesehener Appumfang

Die zukünftige App soll Einlasspersonal auf einem Smartphone oder Tablet durch einen kurzen Ablauf führen:

1. Shop-Adresse über HTTPS eingeben und sich mit einem eingeschränkten persönlichen Shopware-Zugang anmelden.
2. Eine Veranstaltung aus dem Shop auswählen und deren Namen dauerhaft im Scanbildschirm anzeigen.
3. QR-Code mit der Gerätekamera erfassen oder den vollständigen Token manuell eingeben.
4. Den Server abfragen und Ergebnis sowie gegebenenfalls Ticketnummer deutlich anzeigen.
5. Erst nach abgeschlossenem Ergebnis den nächsten eigenständigen Scan starten.
6. Bei einem Verbindungsfehler dieselbe Anfrage sicher wiederholen können; beim Abmelden Sitzung und sensible lokale Daten entfernen.

Vorgesehen sind barrierearm erkennbare Ergebniszustände mit Text und optional Ton/Vibration. App-Navigation, Kamera, sichere Zugangsdatenablage, Sitzungsverlängerung und Verteilung müssen erst implementiert und auf den Zielgeräten geprüft werden. Das Plugin liefert dafür keine fertige mobile Oberfläche oder eigenes App-Pairing.

## Shop und Berechtigungen vorbereiten

Das Foundation-Datenpaket **scanner-role** installiert **Ticket Vendor – Scanner**. Es enthält:

| Recht | Zweck |
| --- | --- |
| `moorl_tv_ticket_sale:read` | Veranstaltungen über die native Admin API suchen und lesen. |
| `moorl_tv_ticket:scan` | Ausschließlich den Check-in-Vorgang ausführen. |

Keine allgemeinen Ticketänderungs-, Ticketlese-, Kunden- oder Bestellrechte sind erforderlich. Die Rolle erlaubt keinen PDF-Download, Versand oder Widerruf. Sie beschränkt den Scanner jedoch nicht auf bestimmte Veranstaltungen. Zusätzliche Rollen und Administratorrechte erweitern die effektiven Berechtigungen.

Ein Administrator legt Benutzer separat an und weist die Rolle zu. Der Datenimport erstellt keine Anmeldedaten und keine Integrationen. Die Zusatzberechtigung **Ticket Vendor → Tickets scannen und Veranstaltungen lesen** kann auch in eigenen Rollen verwendet werden. Frühere Ticket-Update-/Check-in-Create-Rechte allein genügen dem neuen Endpunkt nicht mehr.

## Authentifizierung: vorhandene Shopware API

Die Schnittstelle verwendet die **Admin API**, nicht die öffentliche Store API. Anfragen benötigen einen gültigen nativen Bearer-Token. Ein `sw-access-key` aus einem Verkaufskanal ersetzt diese Authentifizierung nicht.

Für eine später entwickelte persönliche App kann die vorhandene Shopware-Anmeldung genutzt werden:

```http
POST /api/oauth/token
Content-Type: application/json

{
  "grant_type": "password",
  "client_id": "administration",
  "username": "scanner-user",
  "password": "<persönliches Passwort>"
}
```

Shopware liefert die nativen Token- und Ablaufdaten. Die zukünftige App muss abgelaufene Sitzungen behandeln und den gegebenenfalls gelieferten Refresh-Token nach dem nativen Verfahren verwenden. Sie darf Passwörter nicht protokollieren oder dauerhaft im Klartext speichern. Authentifizierungsrichtlinien der konkreten Installation sind zu berücksichtigen.

Serverseitige Integrationen können alternativ den nativen `client_credentials`-Ablauf mit einer nicht administrativen Integration und zugewiesener Scanner-Rolle verwenden. Gemeinsame Integrations-Geheimnisse gehören nicht fest in eine verteilte mobile App. Ein eigener Device-Code-, QR-Pairing- oder App-Login-Endpunkt ist nicht implementiert.

## Veranstaltungen laden: vorhandene Admin API

```http
POST /api/search/moorl-tv-ticket-sale
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "page": 1,
  "limit": 25,
  "filter": [
    { "type": "equals", "field": "active", "value": true },
    { "type": "equals", "field": "status", "value": "published" }
  ],
  "sort": [{ "field": "startAt", "order": "ASC" }],
  "includes": {
    "moorl_tv_ticket_sale": ["id", "name", "startAt", "endAt", "timezone", "locationName"]
  }
}
```

Die App muss die native Suchantwort und weitere Seiten verarbeiten und für den Check-in die `id` des ausgewählten Events als `saleId` übernehmen. Eine gespeicherte Liste ist keine lokale Einlassberechtigung. Der Server prüft bei jedem Scan erneut.

## Ticket einchecken: vorhandener Plugin-Endpunkt

```http
POST /api/_action/moorl-tv/check-in
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "saleId": "0123456789abcdef0123456789abcdef",
  "token": "<Inhalt des Ticket-QR-Codes>",
  "scanRequestId": "b360a0d88ae44b8fa9d96cd58491c079",
  "deviceId": "entrance-north-01"
}
```

| Feld | Vertrag |
| --- | --- |
| `saleId` | Erforderlicher String mit gültiger Shopware-UUID. Üblicherweise 32 Hex-Zeichen ohne Bindestriche. |
| `token` | Erforderlicher, nach Trimmen nicht leerer String, maximal 64 Bytes. Neue Tickets verwenden 32 zufällige Zeichen; importierte Tokens können anders aussehen. |
| `scanRequestId` | Erforderlicher eindeutiger String mit 16–64 Zeichen aus `A–Z`, `a–z`, `0–9`, `_`, `-`. Empfohlen: zufällige UUID in Hex-Darstellung. |
| `deviceId` | Optionaler String, maximal 128 Bytes, etwa eine lokale Gerätekennung ohne personenbezogene Daten. |

Das QR enthält den Token selbst, keine zu öffnende URL. Die App darf den Token nicht gegen die sichtbare Ticketnummer austauschen. Der Server ermittelt Benutzer beziehungsweise Integration aus der Authentifizierung; `scannerIdentifier` ist kein vom Client zu setzendes Feld.

Eine erfolgreiche Verarbeitung liefert HTTP 200, zum Beispiel:

```json
{
  "result": "accepted",
  "ticketNumber": "T-10000",
  "attendeeName": "Ada Lovelace",
  "checkinId": "f948564f0fc744f1bb26a8317ab55e4a4"
}
```

HTTP 200 bedeutet eine fachlich verarbeitete Anfrage. Nur `accepted` bestätigt eine erfolgreiche Einlösung dieser Anfrage. Die Antwort enthält niemals den QR-Token.

| `result` | Bedeutung | Vorgesehene Appanzeige |
| --- | --- | --- |
| `accepted` | Gültiges Ticket atomar eingelöst. | Einlass akzeptiert. |
| `already_redeemed` | Ticket durch eine andere eigenständige Anfrage bereits eingelöst. | Kein erneuter Einlass; Klärung anbieten. |
| `wrong_event` | Ticket gehört zu einer anderen Veranstaltung. | Auswahl prüfen; `ticketNumber` bleibt `null`. |
| `event_closed` | Veranstaltung inaktiv, nicht `published` oder vorhandene Endzeit überschritten. | Veranstaltungsleitung kontaktieren. |
| `not_valid` | Ticket ist beispielsweise offen, abgelaufen oder widerrufen. | Keine Freigabe; Verwaltung kontaktieren. |
| `unknown` | Token nicht gefunden. | Code prüfen; `ticketNumber` ist `null`. |

Die Einlassprüfung berücksichtigt derzeit keine gesonderte Einlassöffnungszeit. Ein Startdatum in der Zukunft verhindert die Einlösung allein nicht. Typ-Aktivität dient dem öffentlichen Verkauf; ein gültiges manuelles Gästelistenticket eines inaktiven Typs bleibt bei offener Veranstaltung einlösbar.

## Wiederholungen und parallele Geräte

Die App muss vor dem ersten Sendeversuch eine `scanRequestId` erzeugen und mit Veranstaltung und Token bis zum endgültigen Ergebnis zusammenhalten. Geht eine Antwort verloren, wird **dieselbe** Anfrage mit **derselben** ID wiederholt. Sie erhält dasselbe gespeicherte Ergebnis und dieselbe `checkinId`, auch wenn der erste Versuch bereits eingelöst hat.

Für eine neue bewusste Erfassung desselben oder eines anderen Tickets wird eine **neue** ID verwendet. Die Wiederholung einer alten akzeptierten Anfrage darf in der Bedienoberfläche nicht als zusätzliche neue Person gezählt werden. Werden Event oder Token zu einer bereits benutzten ID geändert, antwortet der Server mit HTTP 409.

Mehrere Geräte dürfen dieselbe Veranstaltung gleichzeitig scannen. Die serverseitige Transaktion serialisiert konkurrierende Einlösungen. Zwei unterschiedliche Anfragen für denselben gültigen Code führen zu einer Annahme und einer Meldung „bereits eingelöst“.

## Technische Fehler

| HTTP/Fehler | Vorhandene Bedeutung beziehungsweise notwendiges Appverhalten |
| --- | --- |
| 400 | Ungültige Feldtypen, fehlende Werte, fehlerhafte UUID, leere/zu lange Tokens oder unzulässige Anfrage-ID. Eingabe korrigieren. |
| 401 | Keine gültige Authentifizierung. Anmeldung erneuern; noch keine Einlassentscheidung ableiten. |
| 403 | Scanner-Recht fehlt. Rollenzuweisung prüfen; keine Freigabe. |
| 404 | Angegebene Veranstaltung existiert nicht. Veranstaltungsliste aktualisieren. |
| 409 | Anfrage-ID gehört bereits zu einem anderen Scan. Nicht blind als Erfolg behandeln. |
| Timeout/Verbindungsabbruch/5xx | Ergebnis unklar. Kein lokaler Erfolg; denselben Scan mit derselben Anfrage-ID erneut abfragen. |

Die App muss auch Installations- oder Proxyfehler wie Rate Limits behandeln, ohne daraus einen erfolgreichen Einlass abzuleiten. Native Fehlerantworten verwenden Shopwares `errors`-Format.

## Protokoll und Datenschutz

Das Backend protokolliert Scan-ID, Zeitpunkt, Ergebnis und gegebenenfalls Ticket, Veranstaltung, Gerät und authentifizierten Scanner. In Metadaten wird ein Einweg-Fingerprint der Anfrage gespeichert; der rohe Token gehört weder ins Check-in-Protokoll noch in App-Analytics oder Fehlerberichte. PDFs und Kameraansichten können Zugangsdaten enthalten und müssen entsprechend behandelt werden.

Die künftige App sollte nur notwendige Sitzungs- und offene Wiederholungsdaten sicher lokal halten und nach Abschluss beziehungsweise Abmeldung entfernen. Die technischen Details der sicheren Ablage und deren Tests sind Teil der späteren App-Entwicklung.

## Bewusst außerhalb des aktuellen Umfangs

Offline-Ticketdatenbank, spätere Konfliktsynchronisierung, Einlass ohne Serverbestätigung, App-Verteilung über Apple/Google, Push-Mitteilungen, Gerätepaarung, veranstaltungsbezogene Benutzerfreigaben und namentliche Gästelistensuche sind nicht vorhanden. Auch Tickets anlegen, bearbeiten, erstatten oder einen Check-in zurücksetzen gehören nicht zur Scanner-Rolle.

## Abnahmekriterien für die zukünftige App

- Persönliche Anmeldung und Abmeldung einschließlich abgelaufener Sitzungen funktionieren mit der Scanner-Rolle.
- Veranstaltungssuche unterstützt Seitennavigation und zeigt das ausgewählte Event vor jedem Scan.
- Kamera und manuelle Eingabe funktionieren auf den konkret festgelegten iOS-/Android-Zielgeräten; diese Implementierung steht noch aus.
- Alle sechs fachlichen Ergebnisse und technische Fehler haben eindeutige Textanzeigen.
- Ein Antwortverlust lässt sich ohne doppelte Einlösung und ohne doppelte Personenzählung wiederholen.
- Zwei Geräte können den letzten Scan nicht gleichzeitig als neue Einlösung akzeptieren.
- Ohne Netz gibt es keine lokale Einlassfreigabe.
- Passwörter, Bearer-Tokens und Ticketcodes erscheinen nicht in Protokollen oder Analytics.
- Allgemeine Ticketänderung, Versand, Widerruf sowie Kunden-/Bestellabfrage bleiben mit der Scanner-Rolle serverseitig gesperrt.

Bis zur Entwicklung dieser App verwenden Sie den vorhandenen [Browser-Scanner](index.md#einlass-mit-dem-browser-scanner).
