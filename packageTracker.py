import requests
from codeIdentifier import identify

code = input("Enter Tracking Number: ")

#format
code = code.replace(" ", "").upper()

carrier = identify(code)

if carrier:
    print(f"{code} is a tracking number from {carrier}")
else:
    print(f"{code} does not appear to be a valid tracking number")


