# test file
from uspsTracking import trackUSPS
from codeIdentifier import checkUPS, identify

code = "1Z234567890"


print(code[2:])
print(code[len(code) - 1])

checkUPS("1Z999AA10123456784")

print(identify(9449011108400143553282))

trackingNumber = input("Enter Tracking Number: ")
trackUSPS(trackingNumber)