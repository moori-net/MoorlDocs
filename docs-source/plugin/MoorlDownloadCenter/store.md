**Wichtiger Hinweis:** Sie benötigen das Foundation Plugin, welches Ihnen kostenlos zur Verfügung steht: [Foundation](https://store.shopware.com/de/search?search=MoorlFoundation)


## Digitale Inhalte professionell bereitstellen

Mit dem Download Center verwalten und verkaufen Sie digitale Inhalte direkt in Shopware. Stellen Sie Ihren Kunden Bedienungsanleitungen, Produktkataloge, Software, Updates, Medien, Lizenzschlüssel oder umfangreiche Download-Pakete bereit. Sie entscheiden dabei für jeden Inhalt, ob er öffentlich sichtbar, erst nach dem Kauf verfügbar oder nur ausgewählten Kunden und Kundengruppen zugänglich sein soll.

Das Plugin verbindet Produktverkauf, Dateiverwaltung und Kundenbereich in einem durchgängigen Ablauf. Kunden finden ihre berechtigten Inhalte in ihrem Account unter **Meine Einkäufe** und können Dateien, externe Links und Codes dort zentral aufrufen.

## Öffentliche Downloads und geschützte ESD-Produkte

Ein Download Center kann öffentliche und private Inhalte enthalten:

- **Öffentliche Downloads** eignen sich für Anleitungen, Datenblätter, Kataloge oder andere Informationen, die bereits auf der Produktdetailseite verfügbar sein sollen.
- **Private Downloads** werden erst für berechtigte Kunden sichtbar. Sie eignen sich für Software, bezahlte Dokumente, Mitgliederinhalte, Schulungsunterlagen oder individuelle Dateien.
- **ESD-Produkte** verknüpfen ein Produkt mit einem Download Center. Nach dem Kauf entsteht automatisch ein persönliches Download-Abonnement.
- **Direkte Zuweisungen** geben Inhalte unabhängig von einer Bestellung für einzelne Kunden oder Kundengruppen frei.

Sie können öffentliche und private Inhalte innerhalb eines Produkts kombinieren. So lässt sich beispielsweise eine frei zugängliche Produktanleitung mit einem nach dem Kauf geschützten Installationspaket anbieten.

## Kontrollierte Freischaltung und Abonnements

Für private ESD-Produkte erstellt das Plugin pro gekauftem Artikel ein eigenes Download-Abonnement. Der Zugriff richtet sich nach dem Produktpreis und dem Zahlungsstatus:

- Kostenlose digitale Produkte können sofort freigeschaltet werden.
- Kostenpflichtige Produkte stehen bereit, sobald die Bestellung bezahlt wurde.
- Zugriffe können im Admin manuell aktiviert oder deaktiviert werden.
- Eine Laufzeit kann den Zugriff auf ein festes Enddatum begrenzen.
- Jeder Kunde sieht Status, Gültigkeit und verfügbare Inhalte übersichtlich im Kundenbereich.

Damit eignet sich das Download Center sowohl für einmalige digitale Käufe als auch für zeitlich begrenzte Zugänge, Lizenzmodelle oder ergänzende Inhalte zu physischen Produkten.

## Dateien, externe Links und Lizenzschlüssel

Ein Download Center kann unterschiedliche Arten digitaler Inhalte bündeln:

- **Dateien** aus einem konfigurierten Dateisystem
- **Externe Links**, etwa zu Portalen oder Downloads von Drittanbietern
- **Seriennummern und Lizenzschlüssel** für Softwareprodukte
- **Volumenlizenzschlüssel**, die mehrfach verkauft werden können
- **Download-Codes**, mit denen Kunden persönliche Inhalte selbst freischalten

Für Dateien können verschachtelte Verzeichnisse verwendet werden. Über eine `metadata.xml` lassen sich einzelne Dateien ausblenden sowie mit Beschreibungen und eigenen Icons ergänzen. So können Sie auch umfangreiche Download-Bereiche übersichtlich strukturieren.

## Flexible Speicherorte

Speichern Sie Ihre Inhalte dort, wo sie für Ihr Projekt sinnvoll liegen. Das Download Center unterstützt unter anderem:

- lokales Dateisystem
- FTP und SSH
- Amazon S3
- WebDAV
- Nextcloud

Über Dateisystem-Clients lassen sich Dateien auch außerhalb des Shopware-Servers verwalten. Das ist besonders hilfreich für große Pakete, bestehende Infrastruktur oder Inhalte, die von mehreren Systemen genutzt werden.

## Kundenbereich, CMS und Produktdetailseite

Ihre Kunden erhalten einen klaren Zugang zu ihren Inhalten:

- Ein eigenes Konto-Modul bündelt alle persönlichen Download-Abonnements.
- Öffentliche Downloads lassen sich auf Produktdetailseiten darstellen.
- Download Center können als CMS-Element in Shopping Experiences eingebunden werden.
- Berechtigte Kunden können Dateien herunterladen, externe Links öffnen und zugewiesene Codes einsehen.
- Gastbesteller erhalten einen persönlichen Deeplink zu ihren Download-Abonnements.

Der Deeplink wird aus der konfigurierten Basis-URL und einem persönlichen Token erzeugt. Damit können auch Gastbesteller ohne regulären Login ihre gekauften Inhalte erreichen.

## Automatisierte Benachrichtigungen mit dem Flow Builder

Für Download-Abonnements stellt das Plugin eigene Flow-Builder-Ereignisse bereit. Damit können Sie E-Mails und weitere automatisierte Abläufe gezielt an den Status eines Abonnements knüpfen:

- **EsdCreated**: Ein Download-Abonnement wurde angelegt.
- **EsdActivated**: Ein Abonnement wurde freigeschaltet.
- **EsdDeactivated**: Ein Abonnement wurde deaktiviert.

Die mitgelieferte E-Mail-Vorlage enthält Kundendaten, den Namen des Download Centers und den persönlichen Deeplink. Sie können sie im Flow Builder als Ausgangspunkt für eigene Benachrichtigungen verwenden, etwa für neue Downloads, erfolgreiche Zahlungen oder manuelle Freischaltungen.

## Typische Einsatzbereiche

Das Download Center eignet sich unter anderem für:

- Software, Erweiterungen und Updates
- Lizenzschlüssel, Seriennummern und Aktivierungscodes
- E-Books, Whitepaper, Vorlagen und Schulungsunterlagen
- Produktkataloge, Datenblätter und Bedienungsanleitungen
- Inhalte für Händler, Kunden- oder Mitgliedergruppen
- Downloads mit zeitlich begrenztem Zugriff
- Medienbibliotheken mit öffentlichem und geschütztem Bereich

## Funktionsübersicht

- öffentliche und private Download Center
- Produktzuweisung für digitale Produkte und ESD-Verkäufe
- direkte Freigabe für Kunden und Kundengruppen
- automatische Download-Abonnements nach dem Kauf
- Zahlungsstatus-basierte und manuelle Freischaltung
- zeitlich begrenzte Zugriffe
- Dateien, externe Links, Codes und Lizenzschlüssel
- verschachtelte Verzeichnisse und Datei-Metadaten
- lokale und externe Dateisysteme
- CMS-Element und Produktdetailseiten-Integration
- Kundenbereich für persönliche Downloads und Abonnements
- Deeplinks für Gastbesteller
- Flow-Builder-Events und E-Mail-Vorlagen für Benachrichtigungen
