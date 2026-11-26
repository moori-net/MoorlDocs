# Eigene Zertifikatvorlagen erstellen

Studygood wählt die Vorlage anhand des Dokumenttyps am Kurs aus. In einem eigenen Shopware-Plugin kannst du eine weitere Vorlage registrieren und sie einzelnen Kursen zuweisen.

Das Beispiel setzt Shopware 6.7 und ein aktives Studygood voraus. Die Hauptklasse des Beispielplugins heißt `AcmeStudygoodCertificates`. Füge `appflix/studygood` zu den Abhängigkeiten seines `composer.json` hinzu.

## Twig-Datei erstellen

Lege im eigenen Plugin die Datei `src/Resources/views/documents/acme-workshop-certificate.html.twig` an. Twig erhält den Kurs als `studygoodCourse`, das zugehörige Produkt als `product`, die teilnehmende Person als `customer` und den Projektpfad als `rootDir`. Für das PDF verwendet Studygood Dompdf. Verwende HTML und CSS für das Drucklayout. Logos lassen sich als eingebettete Bilder einbinden.

```twig
<!doctype html>
<html lang="de">
<head>
    <meta charset="utf-8">
    <title>Teilnahmezertifikat</title>
    <style>
        @page { margin: 20mm; }
        body { font-family: "DejaVu Sans", sans-serif; }
    </style>
</head>
<body>
    <h1>Teilnahmezertifikat</h1>
    <p>{{ customer.firstName }} {{ customer.lastName }}</p>
    <p>hat an folgendem Kurs teilgenommen</p>
    <h2>{{ studygoodCourse.translated.name ?? studygoodCourse.name }}</h2>
</body>
</html>
```

## Renderer registrieren

Erstelle `src/Core/Certificate/WorkshopCertificateRenderer.php`. `supports()` liefert den technischen Namen des Dokumenttyps und `view()` den Pfad zur Twig-Datei. Der Teil nach `@` entspricht hier dem Bundle-Namen des Beispielplugins. Das Standardformat ist A4 im Hochformat. Mit `pageConfig()` kannst du `pageSize` und `pageOrientation` ändern.

```php
<?php declare(strict_types=1);

namespace Acme\StudygoodCertificates\Core\Certificate;

use Appflix\Studygood\Core\Certificate\StudygoodCertificateRenderer;

final class WorkshopCertificateRenderer extends StudygoodCertificateRenderer
{
    public const DOCUMENT_TYPE = 'acme_studygood_workshop';

    public function supports(): string
    {
        return self::DOCUMENT_TYPE;
    }

    public function view(): string
    {
        return '@AcmeStudygoodCertificates/documents/acme-workshop-certificate.html.twig';
    }
}
```

Registriere den Renderer mit dem Tag `document.renderer` in der `src/Resources/config/services.xml` des eigenen Plugins. Füge den Dienst bei einer vorhandenen Datei in den bestehenden `<services>`-Block ein.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<container xmlns="http://symfony.com/schema/dic/services">
    <services>
        <service id="Acme\StudygoodCertificates\Core\Certificate\WorkshopCertificateRenderer">
            <argument type="service" id="Shopware\Core\Checkout\Document\Twig\DocumentTemplateRenderer"/>
            <argument>%kernel.project_dir%</argument>
            <tag name="document.renderer"/>
        </service>
    </services>
</container>
```

## Dokumenttyp anlegen

Ergänze die Hauptklasse des Plugins in `src/AcmeStudygoodCertificates.php`. Sie legt den Dokumenttyp bei Installation und Update an. Falls `install()` oder `update()` bereits vorhanden sind, füge den Aufruf von `registerCertificateType()` dort ein. Die ID wird aus dem technischen Namen abgeleitet, damit ein Update dieselbe Zuordnung beibehält.

```php
<?php declare(strict_types=1);

namespace Acme\StudygoodCertificates;

use Acme\StudygoodCertificates\Core\Certificate\WorkshopCertificateRenderer;
use Shopware\Core\Framework\Context;
use Shopware\Core\Framework\Plugin;
use Shopware\Core\Framework\Plugin\Context\InstallContext;
use Shopware\Core\Framework\Plugin\Context\UpdateContext;
use Shopware\Core\Framework\Uuid\Uuid;

class AcmeStudygoodCertificates extends Plugin
{
    public function install(InstallContext $context): void
    {
        $this->registerCertificateType();
    }

    public function update(UpdateContext $context): void
    {
        $this->registerCertificateType();
    }

    private function registerCertificateType(): void
    {
        $technicalName = WorkshopCertificateRenderer::DOCUMENT_TYPE;

        $this->container->get('document_type.repository')->upsert([[
            'id' => Uuid::fromStringToHex($technicalName),
            'technicalName' => $technicalName,
            'name' => 'Workshop-Zertifikat',
        ]], Context::createDefaultContext());
    }
}
```

Der technische Name muss mit `supports()` übereinstimmen und `studygood` enthalten, damit das Auswahlfeld ihn anzeigt. `name` ist der sichtbare Name. Verwende für jede weitere Vorlage einen eigenen technischen Namen.

## Vorlage zuweisen und testen

1. Aktualisiere die Plugin-Liste mit `bin/console plugin:refresh`. Installiere und aktiviere das Beispielplugin mit `bin/console plugin:install --activate AcmeStudygoodCertificates`. Erhöhe bei einem bereits installierten Plugin die Version und führe `bin/console plugin:update AcmeStudygoodCertificates` aus.
2. Leere den Shopware-Cache mit `bin/console cache:clear` und lade die Administration neu.
3. Öffne unter **Inhalte → Studygood Kurse** den gewünschten Kurs. Wähle unter **Allgemein → Zertifikatvorlage** den Eintrag **Workshop-Zertifikat** und speichere den Kurs.
4. Öffne als angemeldeter Kunde **Meine Abos**. Bei einem aktiven Abo erscheint der Download, sobald der Kurs als abgeschlossen gilt oder der im Abo hinterlegte Eventtermin vergangen ist. Lade das Zertifikat herunter und prüfe Namen, Kurs und Layout im PDF.

Enthält ein Produkt Kurse mit verschiedenen Vorlagen, lade die Zertifikate einzeln im Kundenkonto herunter. Der Sammeldownload in der Administration verwendet für die zusammengefassten Kurse einen gemeinsamen Renderer.
