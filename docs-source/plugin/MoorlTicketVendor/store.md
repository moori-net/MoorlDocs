## Veranstaltungen und Tickets direkt in Shopware

Mit Ticket Vendor verwalten Sie Veranstaltungen und verkaufen Eintrittskarten über Ihren vorhandenen Shopware-Shop. Konzerte, Workshops, Seminare oder Community-Events erhalten eigene Veranstaltungsseiten, passende Ticketkategorien und klar definierte Kontingente. Der Verkauf nutzt den normalen Warenkorb und Checkout; zusätzliche Shopware-Produkte müssen Sie dafür nicht anlegen.

Vom Ticketkauf bis zum Einlass bleiben die Abläufe im Shopsystem: Nach bestätigter vollständiger Zahlung werden individuelle Tickets freigegeben, als PDF mit QR-Code versendet und im Kundenkonto zum Download angeboten. Ein Browser-Scanner in der Administration prüft die Codes beim Einlass.

## Eigene Kategorien, Preise und Kontingente

Bieten Sie Standard-, VIP-, ermäßigte oder andere Ticketkategorien an. Jeder Typ besitzt eigene Preise und Steuern, ein Kontingent sowie Mindest- und Höchstmengen für den Kauf. Verkaufszeiträume und Veranstaltungszeiten lassen sich getrennt pflegen.

Die abschließende Kontingentprüfung erfolgt zusammen mit der Bestellspeicherung. Auch gleichzeitig eintreffende Bestellungen werden berücksichtigt. Für jede gekaufte Einheit entsteht ein individuelles Ticket mit eigener Nummer aus Shopwares Nummernkreis und eigenem QR-Code.

## Freigabe nach Zahlung und nachvollziehbare Status

Tickets aus Bestellungen warten zunächst auf die bestätigte Zahlung. Nach dem nativen Status `paid` erfolgt die Freigabe und der automatische Versand. Zahlungsfristen, Ablauf, Stornierung, vollständige Erstattung und Chargeback fließen in die Ticketgültigkeit ein. Offene Tickets können nach Ablauf der konfigurierten Zahlungsfrist verfallen und ihr Kontingent wieder freigeben.

In der Verwaltung sehen Sie getrennt, ob ein Ticket gültig, bereits eingelöst, abgelaufen oder widerrufen ist und ob sein Versand aussteht, erfolgreich angenommen wurde oder fehlgeschlagen ist. Verspätete Zahlungen auf bereits stornierte Bestellungen benötigen eine manuelle Abstimmung.

## PDF-Tickets und Kundenbereich

Der PDF-Anhang enthält Veranstaltungsinformationen, Tickettyp, Ticketnummer und QR-Code. Angemeldete Kunden finden ihre berechtigten Tickets zusätzlich im Kundenkonto. Gastbesteller erhalten PDF und persönlichen Ticketlink per E-Mail. Über diesen Link können sie ihr einzelnes Ticket ohne Kundenlogin personalisieren und herunterladen.

Deutsche und englische Mailvorlagen, Versandstatus, Wiederholungsversuche und ein gezielter erneuter Versand unterstützen den laufenden Betrieb. Mit der Flow-Builder-Aktion **Tickets versenden** lassen sich Tickets aus einem Bestellkontext zusätzlich zum Versand vormerken.

## Einladungen und interne Gästeliste

Erstellen Sie Tickets auch direkt in der Veranstaltung – ohne Bestellung und ohne Kundenkonto. Ein kostenloser, öffentlich ausgeblendeter Tickettyp mit eigenem Kontingent eignet sich für Einladungen und Gästelistentickets. Diese verwenden dieselben PDFs, Codes und Einlassprüfungen wie verkaufte Tickets.

Ein privates Anmeldeformular erfasst Namen, E-Mail, optionale Telefonnummer und Ehrenämter. Bestätigungslinks, CSV-Import und die manuelle Ticketausstellung unterstützen die Verwaltung. Anmeldungen reservieren noch keine Plätze; erst das ausgestellte Ticket belegt das Kontingent.

## Kontrollierter Einlass mit eigener Scanner-Rolle

Der integrierte Admin-Scanner unterstützt QR-Erkennung per Gerätekamera in geeigneten Browsern sowie die manuelle Token-Eingabe. Die Prüfung erfolgt online gegen den Shop. Parallele Scans werden atomar verarbeitet; bereits verwendete Codes werden erkannt und Scanversuche protokolliert.

Die mitgelieferte Rolle **Ticket Vendor – Scanner** erlaubt Veranstaltungsabfrage und Check-in, ohne allgemeine Ticketänderungs-, Kunden- oder Bestellrechte zu vergeben. Für individuelle Anbindungen steht eine authentifizierte Admin-API bereit. Eine eigenständige mobile Scanner-App ist derzeit nicht Bestandteil der Erweiterung.

## Verwaltung, Erlebniswelten und SEO

Veranstaltungen bündeln Tickettypen, generierte Kundentickets und Check-in-Protokolle. Zusätzliche Ticketansichten in Bestell- und Kundendetails erleichtern Rückfragen und Support. Foundation-Formulare und Listen sorgen für eine einheitliche Verwaltung.

Öffentliche Veranstaltungsseiten, ein CMS-Listing für Erlebniswelten, übersetzbare Inhalte und native SEO-URLs unterstützen die Präsentation im Shop. Datenpakete liefern die Basiseinrichtung, Import-/Exportprofile für Veranstaltungen und Tickettypen sowie ein optionales Demopaket einschließlich Gästeliste.

## Funktionsübersicht

- Eigene Veranstaltungen und Tickettypen ohne zusätzliche Produktanlage.
- Preise, Steuern, Kontingente, Kaufgrenzen und Verkaufszeiträume je Tickettyp.
- Nativer Shopware-Warenkorb und Checkout mit atomarer Ticketzuteilung.
- Individuelle Ticketnummern, QR-Codes und PDF-Tickets.
- Zahlungsabhängige Freigabe, Zahlungsfrist, Ablauf und Widerruf.
- Automatischer E-Mail-Versand, Versandstatus und erneuter Versand.
- Ticketdownloads für berechtigte angemeldete Kunden.
- Manuelle Tickets und interne kostenlose Gästelistentypen.
- Browser-Scanner, Check-in-Protokoll und eingeschränkte Scanner-Rolle.
- Authentifizierter Check-in-Endpunkt für eigene Anbindungen.
- Veranstaltungsseiten, CMS-Listing, Übersetzungen und SEO-URLs.
- Ticketansichten an Veranstaltung, Bestellung und Kunde.
- Flow-Builder-Aktion sowie Foundation-Daten- und Demopakete.

## Voraussetzungen

Die Erweiterung setzt **MoorlFoundation 1.7** und **Shopware 6.7 mit Storefront** voraus. Automatischer Versand und Fristverarbeitung benötigen die regulären Shopware-Worker und einen eingerichteten Mailtransport. Der Scanner arbeitet online; Kameraerkennung hängt von HTTPS und Browserunterstützung ab. Sitzplatzpläne, Offline-Einlass und eine eigenständige mobile App gehören nicht zum aktuellen Umfang.

Gruppeneinlass sowie Getränke-/Essenspakete bieten konfigurierbare Einlösungen in einem festen Bereich auf einem QR-Code. Jeder bewusste Scan verbraucht eine Einheit und zeigt den Fortschritt. Gruppentickets belegen gewichtete Personenplätze; Verzehrpakete keine Einlassplätze des Events.

## Einblicke in die Erweiterung

Die folgenden Aufnahmen vom 21.10.2026 zeigen den vorhandenen Demoshop mit SIDEQUEST-Theme und die Shopware-Administration. Alle PNGs haben **1920 × 1080 Pixel (FullHD)** bei 100 % Browserzoom. Die Oberfläche dieser Demo ist Englisch, die Veranstaltungsdaten sind teilweise Deutsch. Theme, Inhalte und verfügbare Optionen hängen von Ihrer Installation ab.

![Veranstaltung mit Line-up](images/storefront-event.png)

![Gruppenticket: Preis, Einlösungen und Kontingent](images/admin-type.png)

![Scanner mit Veranstaltung und manueller Eingabe](images/admin-scanner.png)
