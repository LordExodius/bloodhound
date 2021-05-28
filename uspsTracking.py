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
        print(f"Tracking Summary: {trackSummary}\n")
        print("Tracking Details:")
        pprint(trackDetail)

    else:
        print("TrackError:", trackError.get("Description"))