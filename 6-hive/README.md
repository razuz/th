### Install The Hive 4 & Cortex with docker compose

```shell
mkdir /opt/hive
cd /opt/hive
```

Create `.env` file and `docker-compose.yml` file based on the files in this repo

```shell
mkdir -p vol/{nginx,ssl,thehive,elasticsearch}
```


Copy over the following files, from this repository:

- application  ->  /opt/hive/vol/thehive/application.conf
- certs.conf   ->  /opt/hive/vol/nginx/certs.conf
- cortex.conf  ->  /opt/hive/vol/nginx/cortex.conf
- thehive.conf ->  /opt/hive/vol/nginx/thehive.conf

Symlink Let's Encrypt certs to the correct location:

```shell
cp /etc/letsencrypt/live/s*.elliku.eu/fullchain.pem /opt/hive/vol/ssl/cert.pem
cp /etc/letsencrypt/live/s*.elliku.eu/privkey.pem /opt/hive/vol/ssl/cert.key
```

Fix elasticsearch folder permissions:

```shell
chown -R 1000:1000 /opt/hive/vol/elasticsearch
```

Run the setup:

```shell
docker network create proxy
docker compose up -d
```

## Initial setup

1. Go to cortex on https://sX.elliku.eu:8443
1. Click on the update database button
1. Create user `admin` & password `Thr3atHunt!ng`
1. Log in with the freshly created account
1. Create a second non admin organisation
1. Go to users tab for new organisation, create a user there and create API key for the user
1. Update the `.env` file with the new API key
1. Restart the setup:
    * `docker compose down`
    * `docker compose up -d`
1. Log in to The Hive at https://sX.elliku.eu with user `admin@thehive.local` & password `secret`

