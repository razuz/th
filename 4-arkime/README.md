### install Arkime

NB ! Make sure you set hostname properly and rewrite sX with your student number.
```shell
hostnamectl set-hostname sX.elliku.eu
```

```shell
mkdir -p /home/student/arkime
cd /home/student/arkime
wget https://s3.amazonaws.com/files.molo.ch/builds/ubuntu-22.04/arkime_4.3.2-1_amd64.deb
sudo dpkg -i arkime_4.3.2-1_amd64.deb
apt-get -f install -y
```

You will need to run Configure script to setup Arkime. You can run it with the following command and with output:

```shell
# /opt/arkime/bin/Configure
Found interfaces: br-d6211de5c3b4;docker0;eth0;eth1;lo;veth02ca5a1;veth243c608
Semicolon ';' seperated list of interfaces to monitor [eth1] eth0
Install Elasticsearch server locally for demo, must have at least 3G of memory, NOT recommended for production use (yes or no) [no] 
Elasticsearch server URL [http://localhost:9200] https://localhost:9200
Password to encrypt S2S and other things, don't use spaces [no-default] 
Password to encrypt S2S and other things, don't use spaces [no-default] randomness
Arkime - Creating configuration files
Installing sample /opt/arkime/etc/config.ini
Arkime - Installing /etc/security/limits.d/99-arkime.conf to make core and memlock unlimited
Download GEO files? You'll need a MaxMind account https://arkime.com/faq#maxmind (yes or no) [yes] 
Arkime - Downloading GEO files
2023-07-26 16:37:58 URL:https://www.iana.org/assignments/ipv4-address-space/ipv4-address-space.csv [23329/23329] -> "/tmp/tmp.r4QTwP1kGV" [1]
https://raw.githubusercontent.com/wireshark/wireshark/master/manuf:
2023-07-26 16:37:58 ERROR 404: Not Found.

Arkime - Configured - Now continue with step 4 in /opt/arkime/README.txt
```

Init elasticsearch
```shell
/opt/arkime/db/db.pl --insecure --esuser elastic:changeme https://localhost:9200 init
```

Init admin user
```shell
/opt/arkime/bin/arkime_add_user.sh --insecure admin "Admin User" studentpass1 --admin
```

make certificate readable for arkime
```shell
sudo cp /var/lib/docker/volumes/es_certs/_data/ca/ca.crt /usr/local/share/ca-certificates/es.crt /usr/local/share/ca-certificates/ca.crt
sudo chmod 644 /usr/local/share/ca-certificates/ca.crt
```

Change certificate in config file /opt/arkime/etc/config.ini. caTrustFile variable should look like this
```
caTrustFile=/usr/local/share/ca-certificates/ca.crt
```

Change elasticsearch config in /opt/arkime/etc/config.ini
```shell
elasticsearch=https://elastic:changeme@localhost:9200
```

add geoip database
```shell
cd /opt/arkime/etc
wget https://github.com/P3TERX/GeoLite.mmdb/raw/download/GeoLite2-ASN.mmdb
wget https://github.com/P3TERX/GeoLite.mmdb/raw/download/GeoLite2-Country.mmdb
wget https://standards-oui.ieee.org/oui/oui.csv > oui.txt
```

start capture and viewer
```shell
systemctl start arkimecapture.service
systemctl start arkimeviewer.service
```
