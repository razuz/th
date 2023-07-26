### Install The Hive 4 & Cortex with docker compose

```shell
mkdir /opt/hive
cd /opt/hive
```

Create `.env` file and `docker-compose.yml` file based on the files in this repo

```shell
mkdir vol
mkdir -P vol/{nginx,ssl,thehive}
```


Copy over the following files:

- /opt/hive/vol/thehive/application.conf
- /opt/hive/vol/nginx/certs.conf
- /opt/hive/vol/nginx/cortex.conf
- /opt/hive/vol/nginx/thehive.conf

Symlink Let's Encrypt certs to the correct location:

```shell
cp /etc/letsencrypt/live/s*.elliku.eu/fullchain.pem /opt/hive/vol/ssl/cert.pem
cp /etc/letsencrypt/live/s*.elliku.eu/privkey.pem /opt/hive/vol/ssl/cert.key
```

Fix elasticsearch folder permissions:

```shell
mkdir /opt/hive/vol/elasticsearch
chown -R 1000:1000 /opt/hive/vol/elasticsearch
```

Run the setup:

```shell
docker compose up -d
```

## Initial setup

1. Go to cortex on https://sX.elliku.eu:8443
1. Click on the update database button
1. Create user `admin` & password `Thr3atHunt!ng`
1. Log in with the freshly created accounti
1. Go to users tab and create API key for the user
1. Update the `.env` file with the new API key
1. Restart The Hive node. `docker compose restart thehive`
1. Log in to The Hive at https://sX.elliku.eu with user `admin@thehive.local` & password `secret`

