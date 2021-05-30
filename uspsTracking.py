# Oscar Yu (LordExodius)
# May 28th 2021
# USPS tracking module for bloodhound

from usps import USPSApi
from dotenv import load_dotenv
from pprint import pprint
import os

from usps.usps import TrackingInfo

load_dotenv()
USPSuser = os.getenv("USPSuser")
usps = USPSApi(USPSuser)

def trackUSPS(trackNumber):
    trackStatus = usps.track(trackNumber).result
    trackResponse = trackStatus.get("TrackResponse")
    trackInfo = trackResponse.get("TrackInfo")
    trackError = trackInfo.get("Error")
    trackId = trackInfo.get("@ID")
    print(f"Tracking Number:{trackId}\n")

    if trackError is None:
        trackSummary = trackInfo.get("TrackSummary")
        trackDetail = trackInfo.get("TrackDetail")

        return [True, [trackSummary, trackDetail]]

        print(f"Tracking Summary: {trackSummary}\n")
        print("Tracking Details:")
        pprint(trackDetail)

    else:
        return [False, ("TrackError:", trackError.get("Description"))]