# Oscar Yu (LordExodius)
# June 5th 2021
# CanPost Tracking Module for bloodhound

from dotenv import load_dotenv
import os
import requests
import xml.etree.ElementTree as ET

load_dotenv()
user = os.getenv("CanPostDevAPIuser")
password = os.getenv("CanPostDevAPIpass")

def trackCanPost(trackNumber):
    print(trackNumber)
    url = f"http://soa-gw.canadapost.ca/vis/track/pin/{trackNumber}/detail"

    headers = {
        "Accept" : "application/vnd.cpc.track-v2+xml",
        "Accept-language" : "en-CA"
    }

    response = requests.get(url, headers=headers, auth=(user, password))
    if response.ok:

        output = ""

        root = ET.fromstring(response.content)

        for occurrence in root.find("{http://www.canadapost.ca/ws/track-v2}significant-events"):
            for event in occurrence:
                if not event.text == None:
                    output += f"{event.tag.removeprefix('{http://www.canadapost.ca/ws/track-v2}')}: {event.text}" + "\n"
            output += "\n"

        return [True, output]
    
    else:
        return [False, response.content]
