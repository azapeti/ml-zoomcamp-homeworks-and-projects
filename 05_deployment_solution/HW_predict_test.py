#!/usr/bin/env python
# coding: utf-8

import requests


url = 'http://localhost:9696/predict'

client_id = 'abc-123'

client = {"job": "management", "duration": 400, "poutcome": "success"}
requests.post(url, json=client).json()


response = requests.post(url, json=client).json()
print(response)

if response['subscribe'] == True:
    print('sending promo email to %s' % client_id)
else:
    print('not sending promo email to %s' % client_id)