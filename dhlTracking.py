# Oscar Yu (LordExodius)
# June 5th 2021
# DHL Tracking Module for bloodhound

from dotenv import load_dotenv
import requests
import os
import json
import pprint

print("DHL MODULE ACTIVE")

load_dotenv()
DHL_API_Key = os.getenv("DHLAPIKey")

def trackDHL(trackNumber):
    url = "https://api-eu.dhl.com/track/shipments"

    payload = {
        "trackingNumber" : trackNumber
    }

    headers = {
        "Accept" : "application/json", 
        "DHL-API-Key" : DHL_API_Key
    }

    response = requests.get(url, params=payload, headers=headers)

    if response.ok:
        return [True, json.loads(response.content)]
        
    else:
        return [False, json.loads(response.content)]