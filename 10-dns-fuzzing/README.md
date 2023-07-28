## DNSTwist

### Installation

Install DNSTwist
```bash
sudo apt-get install python3-dnspython python3-geoip python3-whois python3-requests python3-ssdeep python3-pip automake libtool
git clone https://github.com/elceef/dnstwist.git
cd dnstwist
```

Run DNSTwist for the domain that you would like to analyse:
```shell
./dnstwist.py -r transferwise.com
```
