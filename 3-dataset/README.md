## Importing data

```shell
cd /opt
sudo ln -s /opt/Elastic/Agent/data/elastic-agent-*/components/filebeat /usr/local/bin/filebeat
git clone https://github.com/OTRF/Security-Datasets.git
```
Create filebeat.yml file
```shell
mkdir fb

filebeat -c /opt/fb/filebeat.yml --path.data /opt/fb --path.home /opt/fb --path.logs /opt/fb
```