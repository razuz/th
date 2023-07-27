## update osquery installation

1. Add certificate to OS CA store
```shell
cp /var/lib/docker/volumes/es_certs/_data/ca/ca.crt /usr/local/share/ca-certificates/
update-ca-certificates -f
```
2. Get certificate fingerprint
```shell
openssl x509 -fingerprint -sha256 -in /usr/local/share/ca-certificates/es.crt | grep Finger | sed -e 's/://g' | sed -e 's/.*=//g'
```
3. add fingerprint to Fleet -> Settings -> Edit Output -> "Elasticsearch CA trusted fingerprint (optional)"
4. Delete agent with "Fleet server policy" under Fleet -> Agents
5. Cleanup the Agent installation
```shell
rm -rf /opt/Elastic
```
6. Reinstall the agent with the following command
```shell
curl -L -O https://artifacts.elastic.co/downloads/beats/elastic-agent/elastic-agent-8.8.2-linux-x86_64.tar.gz
tar xzvf elastic-agent-8.8.2-linux-x86_64.tar.gz
cd elastic-agent-8.8.2-linux-x86_64
sudo ./elastic-agent install \
--fleet-server-es=https://localhost:9200 \
--fleet-server-service-token=__YOUR_TOKEN_HERE \
--fleet-server-policy=fleet-server-policy \
--fleet-server-port=8220 \
--fleet-server-es-ca=/var/lib/docker/volumes/es_certs/_data/ca/ca.crt \
--fleet-server-es-ca-trusted-fingerprint=__FINGERPRINT_HERE__
```

7. Now go to Fleet -> Agent policies -> Fleet Server Policy and add integration OSQuery logs and OSQuery Manager
8. Go to OSQuery and install pre-built packages
9. start making queries