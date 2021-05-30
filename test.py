# test file
from uspsTracking import trackUSPS
from identifier import checkUPS, identify
from dotenv import load_dotenv
import os

code = "1Z234567890"

FEDEX1 = os.getenv("fedex1")
FEDEX3 = os.getenv("fedex3")
DHL = os.getenv("dhl1")
USPS1 = os.getenv("usps1")
USPS2 = os.getenv("usps2")

print(code[2:])
print(code[len(code) - 1])

checkUPS("1Z999AA10123456784")


print("Fedex:", identify(FEDEX1))
print("Fedex:", identify(FEDEX3))
print("DHL:", identify(DHL))
print("USPS:", identify(USPS1))
print("USPS:", identify(USPS2))

for i in range(3):
    trackingNumber = input("Enter Tracking Number: ")
    trackUSPS(trackingNumber)