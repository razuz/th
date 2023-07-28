## Install x0rz phishing catcher

```shell
sudo apt install python3-pip
git clone https://github.com/x0rz/phishing_catcher.git
cd phishing_catcher
pip3 install -r requirements.txt
```

update external.yaml and make config something like 
```yaml
# Change to true if you want to override suspicious.yaml
# and only use your own config in this file.
override_suspicious.yaml: true 

keywords:
# Add your own keywords here or override the score
# for the ones found in suspicious.yaml, e.g.:
#    'myownkeyword': 50
    'appleid': 1

tlds:
# Add your own TLDs here, e.g.:
#    '.nu':
#    '.se':
    '.ge': 100
```

run script
```shell
python3 catch_phishing.py
```

## Run the same thing in docker

fix Dockerfile to
```shell
FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "catch_phishing.py"]
```

run Dockerfile
```shell
docker build -t phishing_catcher .
docker run -t phishing_catcher
```