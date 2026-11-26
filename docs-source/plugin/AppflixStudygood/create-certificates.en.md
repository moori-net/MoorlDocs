# Create custom certificate templates

Studygood selects a template based on the document type assigned to a course. You can register an additional template in your own Shopware plugin and assign it to individual courses.

The example assumes Shopware 6.7 and an active Studygood plugin. The example plugin's main class is `AcmeStudygoodCertificates`. Add `appflix/studygood` to the dependencies in its `composer.json`.

## Create the Twig file

Create `src/Resources/views/documents/acme-workshop-certificate.html.twig` in your plugin. Twig receives the course as `studygoodCourse`, the associated product as `product`, the participant as `customer`, and the project directory as `rootDir`. Studygood uses Dompdf to generate the PDF. Use HTML and CSS for the print layout. You can embed logos as images.

```twig
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Certificate of participation</title>
    <style>
        @page { margin: 20mm; }
        body { font-family: "DejaVu Sans", sans-serif; }
    </style>
</head>
<body>
    <h1>Certificate of participation</h1>
    <p>{{ customer.firstName }} {{ customer.lastName }}</p>
    <p>participated in the following course</p>
    <h2>{{ studygoodCourse.translated.name ?? studygoodCourse.name }}</h2>
</body>
</html>
```

## Register the renderer

Create `src/Core/Certificate/WorkshopCertificateRenderer.php`. `supports()` returns the technical name of the document type and `view()` returns the path to the Twig file. The part after `@` is the example plugin's bundle name. The default paper size is A4 in portrait orientation. Override `pageConfig()` to change `pageSize` or `pageOrientation`.

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

Register the renderer with the `document.renderer` tag in your plugin's `src/Resources/config/services.xml`. If the file already exists, add the service to its `<services>` block.

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

## Create the document type

Add the following to the plugin's main class in `src/AcmeStudygoodCertificates.php`. It registers the document type on install and update. If `install()` or `update()` already exist, add the call to `registerCertificateType()` to those methods. The ID is derived from the technical name so that updating the plugin preserves existing course assignments.

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
            'name' => 'Workshop certificate',
        ]], Context::createDefaultContext());
    }
}
```

The technical name must match `supports()` and contain `studygood` for the course selector to list it. `name` is the display name. Use a distinct technical name for each additional template.

## Assign and test the template

1. Refresh the plugin list with `bin/console plugin:refresh`. Install and activate the example plugin with `bin/console plugin:install --activate AcmeStudygoodCertificates`. If it is already installed, bump its version and run `bin/console plugin:update AcmeStudygoodCertificates`.
2. Clear the Shopware cache with `bin/console cache:clear` and reload the administration.
3. Open the course under **Content → Studygood Courses**. Select **Workshop certificate** under **General → Certificate template** and save the course.
4. Sign in as a customer and open **My subscriptions**. For an active subscription, the download appears once the course is marked as complete or the subscription's event date has passed. Download the certificate and check the participant's name, the course, and the layout in the PDF.

If a product contains courses with different templates, download the certificates individually in the customer account. The combined download in the administration uses a single renderer for the included courses.
