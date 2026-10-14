---
description: Verschachtelte Verzeichnisse, private und Öffentliche Downloads, Digitale Produkte, CMS Elemente, Verwaltung von Seriennummern und statischen Links, Amazon S3, FTP, WebDAV und Nextcloud
tags:
  - Downloads
  - ESD
  - Digitale Produkte
  - Shopware 6.7
---

# Download Center

Verschachtelte Verzeichnisse, private und Öffentliche Downloads, Digitale Produkte, CMS Elemente, Verwaltung von Seriennummern und statischen Links, Amazon S3, FTP, WebDAV und Nextcloud

![Download Center](images/dlc-01.jpg)

---

## Plugin erwerben

Dieses Plugin kann im offiziellen **Shopware Community Store** erworben werden.

- [Shopware Community Store](https://store.shopware.com/de/search?search=MoorlDownloadCenter)


**Wichtiger Hinweis:** Sie benötigen das Foundation Plugin, welches Ihnen kostenlos zur Verfügung steht: [moori Foundation](../MoorlFoundation/index.md)


---

## Ersteinrichtung

### Verfügbare Dateisysteme

* Lokales Dateisystem
* FTP
* SSH
* Amazon S3
* WebDAV
* Nextcloud
* Azure (wird bei Bedarf nachgeliefert)
* Google Storage (wird bei Bedarf nachgeliefert)

Der Shopware Medien-Manager wird nicht verwendet. Für eine WebDAV-Verbindung kann beispielsweise folgendes Plugin eingesetzt werden:
https://store.shopware.com/frosh11030048018f/webdav.html

### Fehlende Dienste nachladen

Einige Dienste benötigen Composer-Pakete. Führen Sie die folgenden Befehle im Hauptverzeichnis Ihres Shopware-6-Shops aus:

```text
composer require league/flysystem-ftp
composer require league/flysystem-webdav
```

### Übersicht

In der Übersicht finden Sie eine Zusammenfassung aller Downloads. In diesem Beispiel ist das Demopaket bereits installiert.

![](images/dlc-01.jpg)

### Download Center konfigurieren

#### Plugin-Konfiguration

![](images/dlc-00.jpg)

- **Deeplink URL**: Basis-URL für persönliche Links zu Download-Abonnements, insbesondere für Gastbesteller. Tragen Sie Ihre Domain einschließlich `/account/subscription/` ein.
- **Kunden mit Code hinzufügen**: Blendet im Kundenbereich das Eingabefeld ein, mit dem Kunden einen Download-Code einlösen können.

#### Basiskonfiguration

![](images/dlc-02.jpg)

![](images/dlc-03.jpg)

- **Aktiv**: Schaltet das Download Center frei.
- **Name**: Bezeichnung des Download Centers.
- **Typ**: Private Downloads stehen nur berechtigten Kunden zur Verfügung. Öffentliche Downloads sind auf der Produktdetailseite sichtbar.
- **Hat Dateien**: Aktiviert die Client-Auswahl und den Datei-Explorer.
- **Client**: Dateisystem-Client, aus dem die Dateien geladen werden.
- **Hat Links**: Aktiviert den Bereich für externe Links.
- **Hat Codes**: Aktiviert die Verwaltung von Codes und Lizenzschlüsseln.
- **Produkte**: Verknüpft Produkte mit dem Download Center. Bei privaten Downloads wird der Zugriff nach dem Kauf freigeschaltet.
- **Kunden** und **Kundengruppen**: Weisen Downloads direkt einzelnen Kunden oder Kundengruppen zu.
- **Kunden-Downloads via Code erstellen**: Ermöglicht Kunden, persönliche Downloads über einen Code freizuschalten. Diese Codes sind nicht als Seriennummern für ESD-Produkte vorgesehen.
- **Sprache** und **Verkaufskanal**: Beschränken die Anzeige der Downloads auf eine Sprache oder einen Verkaufskanal.

#### Datei-Explorer

Wählen Sie das Verzeichnis aus, das für den Download bereitsteht. Unterverzeichnisse bleiben für berechtigte Kunden zugänglich und können beispielsweise für Kategorien oder Sprachen verwendet werden.

![](images/dlc-04.jpg)

#### Links

Hier können Sie externe Links eintragen, etwa wenn Sie einen Lizenzschlüssel für ein Microsoft-Produkt anbieten, aber die Datei nicht selbst bereitstellen. Das entlastet Ihre Bandbreite.

![](images/dlc-05.jpg)

#### Einkäufe

Hier finden Sie eine Übersicht aller Einkäufe Ihrer Kunden. Bei Bedarf können Sie Abonnements auch selbst erstellen oder anpassen.

![](images/dlc-06.jpg)

#### Codes

In diesem Bereich verwalten Sie Seriennummern und Volumenlizenzschlüssel für Ihre Softwareprodukte. Ein Volumenlizenzschlüssel kann mehrfach verkauft werden.

Für persönliche Kunden-Downloads können Sie einen neuen Code anlegen; dieser wird automatisch generiert.

![](images/dlc-07.jpg)

#### Zusätzliche Gestaltungsmöglichkeiten

Über eine `metadata.xml` im Verzeichnis können Sie einzelne Dateien ergänzend konfigurieren:

- visibility (private): Blendet eine Datei aus (z.B. für die metadata.xml selbst)
- description: Eine zusätzliche Beschreibung für die Datei (aktuell nur einsprachig!)
- image: Eine Bild-URL oder Base64 für das Icon

Beispiel:

```xml
<files>
    <file name="_metadata.xml">
        <visibility>private</visibility>
        <description>Blendet diese XML-Datei aus</description>
    </file>
        <file name="FroshTools-0.2.12.zip">
        <visibility>private</visibility>
    </file>
    <file name="sample.pdf">
        <description>Irgendein PDF aus dem Internet</description>
        <image>data:image/png;base64,(...)</image>
    </file>
    <file name="FroshPlatformAdminer-0.3.4.zip">
        <description>Ein tolles Tool um Datenbanken in Shopware 6 zu verwalten</description>
        <image>https://avatars.githubusercontent.com/u/36633261?s=200&v=4</image>
    </file>
</files>
```

## Storefront

### Einkaufswelten

In diesem Beispiel wird ein Download Center als CMS-Element eingebunden.

![](images/dlc-20.jpg)

Ein Unterverzeichnis wird geöffnet.

![](images/dlc-21.jpg)

### Produkte

Ein ESD-Produkt kann einen Download, einen Code oder beides enthalten.

![](images/dlc-22.jpg)

Ein Produkt mit öffentlichen Downloads, beispielsweise Bedienungsanleitungen.

![](images/dlc-23.jpg)

!!! note

      Sie können private und öffentliche Downloads bei einem Produkt kombinieren.

### Einkauf von ESD-Produkten

#### Warenkorb

In diesem Beispiel enthält der Warenkorb ein kostenloses ESD-Produkt, ein Produkt mit Codes und ein kostenpflichtiges ESD-Produkt.

![](images/dlc-24.jpg)

![](images/dlc-25.jpg)

#### Meine Einkäufe

Im Kundenbereich erscheint neben der Bestellübersicht die Seite **Meine Einkäufe** mit den Download-Abonnements.

![](images/dlc-26.jpg)

1. Kostenlose ESD-Produkte sind sofort freigeschaltet; der Zugriff kann zeitlich begrenzt sein.
2. Kostenpflichtige ESD-Produkte stehen bereit, sobald die Bestellung den Zahlungsstatus **bezahlt** erreicht.
3. Das Abonnement zeigt Status und Inhalte an.

Nach dem Setzen des Zahlungsstatus **bezahlt** stehen die Downloads und Codes zur Verfügung.

![](images/dlc-27.jpg)

![](images/dlc-28.jpg)

### Flow Builder und E-Mail-Benachrichtigungen

Für Download-Abonnements stehen eigene Flow-Builder-Events zur Verfügung. Damit können Sie E-Mail-Benachrichtigungen unabhängig von der Bestell-E-Mail auslösen.

| Event | Wird ausgelöst, wenn |
| --- | --- |
| `EsdCreated` | ein Download-Abonnement angelegt wurde |
| `EsdActivated` | ein Abonnement freigeschaltet wurde (`active = true`) |
| `EsdDeactivated` | ein Abonnement deaktiviert wurde (`active = false`) |

Beim Anlegen eines Abonnements wird nach `EsdCreated` zusätzlich das zum Status passende Aktivierungs- oder Deaktivierungs-Event ausgelöst.

Legen Sie im Flow Builder einen Flow mit einem dieser Events an und fügen Sie die Aktion **E-Mail versenden** hinzu. Die mitgelieferte E-Mail-Vorlage **Download Benachrichtigung** ist auf Deutsch und Englisch verfügbar.

In den E-Mail-Vorlagen stehen unter anderem diese Variablen zur Verfügung:

```twig
{{ customer.firstName }}
{{ customer.lastName }}
{{ esd.downloadCenter.translated.name }}
{{ deeplink }}
```

`{{ deeplink }}` enthält die vollständige URL zur Seite **Meine Einkäufe** beziehungsweise zu den Subscriptions. Sie wird aus der Plugin-Einstellung **Deeplink URL** und dem persönlichen Token des Abonnements gebildet. Dadurch funktioniert der Link auch für Gastbesteller.

!!! note

      Der bisherige Bestell-Subscriber, der Links als Custom Fields an der Bestellung speichert, ist veraltet. Verwenden Sie für neue Benachrichtigungen die Flow-Builder-Events und die E-Mail-Vorlagen.

### Persönliche Downloads

Neben Abonnements können Downloads direkt Kunden oder Kundengruppen zugewiesen werden. Berechtigte Kunden sehen diese Downloads ebenfalls in ihrem Kundenbereich.

![](images/dlc-29.jpg)

Das Eingabefeld zum Einlösen eines Codes wird bei Bedarf über die Plugin-Konfiguration ein- oder ausgeblendet.

## Gastbesteller

Gastbesteller können ESD-Produkte kaufen und über einen persönlichen Deeplink auf ihre Downloads zugreifen. Für ältere Bestell-E-Mail-Vorlagen stehen weiterhin die folgenden Custom Fields zur Verfügung:

Für den Textbereich:

```text
{{ order.customFields.downloadCenterPlain }}
```

Für den HTML-Bereich:

```html
{{ order.customFields.downloadCenterHtml|raw }}
```

![](images/dlc-30.jpg)

Der Link führt Gastbesteller direkt zu ihren Download-Abonnements.

![](images/dlc-32.jpg)
