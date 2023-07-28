### Install The Hive 4 & Cortex with docker compose

```shell
mkdir /opt/hive
cd /opt/hive
```

Create `.env` file and `docker-compose.yml` file based on the files in this repo
```shell
wget https://raw.githubusercontent.com/razuz/th/main/6-hive/.env
wget https://raw.githubusercontent.com/razuz/th/main/6-hive/docker-compose.yml
```


```shell
mkdir -p vol/{nginx,ssl,thehive,elasticsearch}
```


Copy over the following files, from this repository:

- application  ->  /opt/hive/vol/thehive/application.conf
- certs.conf   ->  /opt/hive/vol/nginx/certs.conf
- cortex.conf  ->  /opt/hive/vol/nginx/cortex.conf
- thehive.conf ->  /opt/hive/vol/nginx/thehive.conf

```shell
wget https://raw.githubusercontent.com/razuz/th/main/6-hive/application.conf > /opt/hive/vol/thehive/application.conf
wget https://raw.githubusercontent.com/razuz/th/main/6-hive/certs.conf > /opt/hive/vol/nginx/certs.conf
wget https://raw.githubusercontent.com/razuz/th/main/6-hive/cortex.conf > /opt/hive/vol/nginx/cortex.conf
wget https://raw.githubusercontent.com/razuz/th/main/6-hive/thehive.conf > /opt/hive/vol/nginx/thehive.conf
```

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




## Creating test alerts in Hive

```shell
cd /opt/hive
```

- Download `requirements.txt` and `hive.py` to the folder
- Create a virtual env with: `python3 -m venv venv`
- Activate virtualenv: `source venv/bin/activate`
- Edit the token and url in `hive.py` on line 49. Optionally edit alert details.
- Save the file and run it with: `python hive.py`
- You should see an alert in The Hive


