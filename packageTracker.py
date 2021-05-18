import requests
from codeIdentifier import identify
from bs4 import BeautifulSoup

code = input("Enter Tracking Number: ")

#links
usps = "https://tools.usps.com/go/TrackConfirmAction?ttLc=2&text28777=&tLabels=" + code

#format
code = code.replace(" ", "").upper()

carrier = identify(code)

if carrier:
    print(f"{code} is a tracking number from {carrier}")
else:
    print(f"{code} does not appear to be a valid tracking number")

if carrier == "USPS":
    url = usps
    page = requests.get(url)
    print("Page Status:", page.status_code)
    soup = BeautifulSoup(page.content, "html.parser")
    status = soup.find(class_ = "delivery_status")
    print(status)



