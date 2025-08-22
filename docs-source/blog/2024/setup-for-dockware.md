---
description: Setup for Dockware
tags:
- Dockware
---

# My setup for Dockware

## Create docker-compose.yaml

### Quick Start Developer setup

[dockware/dev on Dockerhub](https://hub.docker.com/r/dockware/dev/tags)

```yaml
version: '3'

services:
  shopware_6_7_latest:
    container_name: shopware_6_7_latest
    image: dockware/dev:6.7.1.2
    ports:
      - "22:22"     # ssh
      - "80:80"     # apache2
      - "443:443"   # apache2 https
      - "8080:8080" # watch
      - "8888:8888" # watch admin
      - "9998:9998" # watch storefront proxy
      - "9999:9999" # watch storefront
      - "3306:3306" # mysql port
    #volumes:
    #  - "./src:/var/www/html"
    #  - "./src:/var/www/html/custom/plugins"
    networks:
      - web
    environment:
      - PHP_VERSION=8.2
      - XDEBUG_ENABLED=0
networks:
  web:
    external: false
```

### Advanced with ElasticSearch

```yaml
version: '3'

services:
  shopware:
    container_name: shopware
    image: dockware/dev:latest
    ports:
      - "22:22"     # ssh
      - "80:80"     # apache2
      - "443:443"   # apache2 https
      - "8888:8888" # watch admin
      - "9998:9998" # watch storefront proxy
      - "9999:9999" # watch storefront
      - "3306:3306" # mysql port
    networks:
      - web
    environment:
      - PHP_VERSION=8.1
      - XDEBUG_ENABLED=0
      - OPENSEARCH_URL=opensearch:9200
      - SHOPWARE_ES_INDEXING_ENABLED=1
      - SHOPWARE_ES_ENABLED=1
      - SHOPWARE_ES_THROW_EXCEPTION=1

  opensearch:
    image: opensearchproject/opensearch:2
    ports:
      - "9200:9200"
      - "9300:9300"
    networks:
      - web
    volumes:
      - opensearch-data:/usr/share/opensearch/data
    environment:
      - discovery.type=single-node
      - plugins.security.disabled=true
      - OPENSEARCH_INITIAL_ADMIN_PASSWORD='osx#n9%e4bk6Em'

volumes:
  opensearch-data:

networks:
  web:
    external: false
```

## Start containers

Start the docker containers with the Docker default command in detached mode:

```ruby
docker-compose up -d
```

## SSH Login

* Hostname: localhost:22
* Username: dockware
* Password: dockware

Shop-Root: /var/www/html/
Plugin-Root: /var/www/html/custom/plugins/

## Add missing PHP extensions

```ruby
sudo apt install php8.2-ssh2
sudo sed -i '$a extension=ssh2.so' /etc/php/8.2/fpm/php.ini
sudo service php8.2-fpm reload
```

## Install symfony profiler 

```ruby
composer require --dev symfony/profiler-pack
composer require --dev symfony/doctrine-bridge
composer require --dev doctrine/sql-formatter
```


## Install Dev Tools

[Dev Tools](https://github.com/moori-net/MoorlDevTools/releases)
### Most common commands

```ruby
# Create migration files based on EntityDefinitions - Please do not forget to download the Migration directory from deployment server!
bin/console mdt:migration:create MoorlPlugin -m dry|live|file|cleanup -a

# Install single Plugin or all with dependencies
bin/console mdt:plugin:install MoorlPlugin|all

# Uninstall single Plugin or all with dependencies
bin/console mdt:plugin:uninstall MoorlPlugin|all

# Update single Plugin or all with dependencies
bin/console mdt:plugin:update MoorlPlugin|all

# Demo install single Plugin or all with dependencies
bin/console mdt:demo:install MoorlPlugin|all -r
```