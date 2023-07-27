#!/usr/bin/env python3
# encoding: utf-8

import json
import uuid

from typing import Dict
from thehive4py.api import TheHiveApi
from thehive4py.models import Alert, AlertArtifact


class HiveApi(object):
    def __init__(self, hive_url, hive_key):
        self.hive_url = hive_url
        self.api_key = hive_key
        self.artifacts = []
        self.artifacts = [
            AlertArtifact(dataType='ip', data='8.8.8.8'),
            AlertArtifact(dataType='domain', data='google.com')
        ]
        self.api = TheHiveApi(self.hive_url, self.api_key)

    def hive_create_alert(self) -> Dict:
        self.alert = Alert(title='Test alert 2',
                           tlp=1,
                           tags=['test', 'MITRE:T1072'],
                           description='This is a test alert',
                           type='TRAINING:OTHER',
                           source='testing',
                           sourceRef=f'{uuid.uuid4()}',
                           artifacts=self.artifacts,
                           severity=4)

        # Create the Alert
        # print('Creating Alert: {}'.format(self.alert))
        response = self.api.create_alert(self.alert)
        alert_response = json.dumps(response.json())
        if response.status_code == 201:
            # print("Alert created : {}".format(json.dumps(response.json())))
            # self.artifacts = []
            return alert_response
        else:
            # print('Failed to create alert {}/{}'.format(response.status_code, response.text))
            # self.artifacts = []
            return {"Success": False, "Error": response.text}


if __name__ == "__main__":
    api = HiveApi('https://sX.elliku.eu', 'USER_API_TOKEN_GOES_HERE')
    resp = api.hive_create_alert()
    print(resp)
