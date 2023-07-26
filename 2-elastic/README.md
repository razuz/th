## Install

Installing Elastic and Kibana.
```shell
cd /home/student/es
```
Update sysctl
```shell
sudo sysctl -w vm.max_map_count=262144
```
Change passwords if necessary in .env file and then boot up the cluster
```shell
sudo docker compose up -d
```

To install fleet server install agent with modified parameters
```shell
sudo ./elastic-agent install --fleet-server-es=https://localhost:9200 --fleet-server-service-token=__YOUR_TOKEN__ --fleet-server-policy=fleet-server-policy  --fleet-server-port=8220 --fleet-server-es-ca /var/lib/docker/volumes/es_certs/_data/ca/ca.crt
````


## other stuff

seeing what containers are running
```shell
docker ps
```

Cheat sheet for docker commands
https://raw.githubusercontent.com/sangam14/dockercheatsheets/master/dockercheatsheet8.png