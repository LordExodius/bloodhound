from pprint import pprint
import requests
from identifier import identify
import uspsTracking

code = input("Enter Tracking Number: ")

#format
code = code.replace(" ", "").upper()

carriers = identify(code)

if carriers:
    print(f"{code} is a tracking number from {carriers}")
    finished = False
    while not finished:
        carrier = carriers[0]
        if carrier == "USPS":
            tracking = uspsTracking.trackUSPS(code)
            if tracking[0]:
                print(f"Tracking Summary:\n\n{tracking[1][0]}\n")
                print("Tracking Details:\n")
                pprint(tracking[1][1])
                finished = True
            else:
                carriers.remove("USPS")
                continue
        elif carrier == "DHL":
            print("DHL")
else:
    print(f"{code} does not appear to be a valid tracking number")


