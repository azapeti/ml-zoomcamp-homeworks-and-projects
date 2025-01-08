#!/usr/bin/env python
# coding: utf-8

import requests

url = "http://localhost:9696/predict"

patient = [
  {
    "age": 35,
    "sex": "f",
    "bp": "normal",
    "cholesterol": "normal",
    "na_to_k": 10.355
  },
  {
    "age": 57,
    "sex": "m",
    "bp": "high",
    "cholesterol": "high",
    "na_to_k": 22.893
  },
  {
    "age": 60,
    "sex": "m",
    "bp": "low",
    "cholesterol": "high",
    "na_to_k": 13.521
  }
]


response = requests.post(url, json=patient).json()
print(response)