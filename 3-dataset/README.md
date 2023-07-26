## Importing data

* Install integrations
  * Windows integration
* Go to Stack Management -> Index Management -> Index Templates
* Create Template
  * Name: otrf
  * Index patterns: otrf-*
  * Enable "Create data stream"
  * (optional) Priority: 400
  * (optional) Version: 1
* Add components:
  * logs-windows.forwarded@package
  * logs-windows.powershell@package
  * logs-windows.powershell_operational@package
  * logs-windows.sysmon_operational@package
* Add index settings
```shell
{
  "index": {
    "lifecycle": {
      "name": "otrf-policy"
    },
    "number_of_replicas": "0",
    "default_pipeline": "logs-windows.forwarded-1.27.0"
  }
}
```
* skip Mappings
* skip Aliases

* Download some example data
```shell
apt-get install -y unzip
cd /opt
sudo ln -s /opt/Elastic/Agent/data/elastic-agent-*/components/filebeat /usr/local/bin/filebeat
cd 
git clone https://github.com/OTRF/Security-Datasets.git
cd /opt/Security-Datasets/datasets/compound/apt29/day1/
unzip apt29_evals_day1_manual.zip
cd /opt/Security-Datasets/datasets/compound/apt29/day2/
unzip apt29_evals_day2_manual.zip
cd /opt/Security-Datasets/datasets/compound/windows/apt3/
tar xvzf empire_apt3.tar.gz
```

Create filebeat.yml file
```shell
cd /opt
mkdir fb
cd fb
wget https://raw.githubusercontent.com/razuz/th/main/3-dataset/filebeat.yml
filebeat -c /opt/fb/filebeat.yml --path.data /opt/fb --path.home /opt/fb --path.logs /opt/fb
```