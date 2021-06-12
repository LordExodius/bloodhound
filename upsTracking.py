# Oscar Yu (LordExodius)
# June 10th 2021
# UPS Tracking Module for bloodhound using RESTful API

from dotenv import load_dotenv
import requests
import json
import os
import pprint

load_dotenv()
accessKey = os.getenv("UPSAccessKey")
userID = os.getenv("UPSid")
password = os.getenv("UPSpass")

def trackUPS(trackNumber):
    print(f"Tracking Number: {trackNumber}")
    url = f"https://wwwcie.ups.com/track/v1/details/{trackNumber}"

    headers = {
        "transId" : "111111",
        "transactionSrc" : "bloodhound",
        "AccessLicenseNumber" : accessKey,
        #"Username" : userID,
        #"Password" : password,
        "Content-Type" : "application/json",
        "Accept" : "application/json"
    }
    
    response = requests.get(url, headers=headers)
    print(response.status_code)

    trackResponse = json.loads(response.content.decode("ASCII"))
    if "warnings" in trackResponse: #check if valid tracking number
        return [False, trackResponse]

    else:
        trackInfo = trackResponse["trackResponse"]["shipment"][0]["package"][0]["activity"]
        output = ""
        for activity in trackInfo:
            for item in activity:
                output += f"{item}:{activity[item]}\n"
            output += "\n"

        return[True, output]

print(trackUPS("92055900100111152280003029"))