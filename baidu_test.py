import requests
import json

SCHEMA="http://"
POST="/v1/lps/logistics/direction HTTP/1.1"
HOST="lps.baidubce.com"
BODY={
    "taskId": "c4b95d57e2a34d668fa39f4de1986086",
    "vehicleId": "006fd3ee925d4170b98c3892244a598f",
    "routeId": "dd8f09630781445eb42df16f5b812313",
    "origin": "31.753584,117.205126",
    "destination": "31.561788,117.170631",
    "retCoordType": "bd09ll",
    "height": 2,
    "width": 2,
    "weight": 2,
    "length": 2,
    "axleWeight": 2,
    "axleCount": 2,
    "isTrailer": 0,
    "plateProvince": "豫",
    "plateNumber": "A12345",
    "plateColor": 1
}

response=requests.post(SCHEMA+HOST+POST, json=BODY)
print(response)