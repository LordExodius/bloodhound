def identify(code):
    possible = checkLength(code)

    if len(possible) == 0:
        return False
    
    elif len(possible) == 1:
        return possible[0]

    elif len(possible) > 1:
        if "USPS" in possible: 
            if checkUSPS(code):
                return "USPS"
            else:
                possible.remove("USPS")
        
        if "UPS" in possible:
            if checkUPS(code):
                return "UPS"
            else:
                possible.remove("UPS")
    
    return possible

def checkLength(code):
    #USPS:
    #   20 digits
    #   13 digits, 2 starting letters, ending in US
    shipList = []

    length = len(code)
    if length == 20 or length == 22 or length == 13:
        shipList.append("USPS")
    if length == 18:
        shipList.append("UPS")
    if length >= 10 and length <= 39:
        shipList.append("DHL")
    if length >= 12 and length <= 14:
        shipList.append("FEDEX")

    return shipList

# VALIDITY CHECKER FOR EACH CODE FORMAT
# --------------------------------------------

# check if code is a valid USPS code
def checkUSPS(code):
    if len(code) == 20 or len(code) == 22:
        return True
    elif code[11:] == "US":
        return True
    else:
        return False

# check if code is a valid UPS code
def checkUPS(code):
    # must start with 1Z
    if code[:2] != "1Z":
        return False
    
    # checkdigit calculation
    else:
        # to check if character is a number
        numeric = "1234567890"

        # remove 1Z from code to check
        checkCode = code[2:17]
        print("Check code:", checkCode)
        runningTotal = 0

        for i in range(len(checkCode)):
            # if odd digit (even index)
            if i%2 == 0:
                if checkCode[i] in numeric:
                    runningTotal += int(checkCode[i])
                else:
                    runningTotal += (ord(checkCode[i]) - 63) % 10

            # if even digit (odd index)
            else:
                if checkCode[i] in numeric:
                    runningTotal += int(checkCode[i]) * 2
                else:
                    runningTotal += ((ord(checkCode[i]) - 63) % 10) * 2

        x = runningTotal % 10
        if x == 0:
            checkDigit = x
        else:
            checkDigit = 10 - x

        if checkDigit == int(code[len(code) - 1]):
            print("Check digit is correct")
            return True
        else:
            print(f"Correct format, but incorrect check digit, should be {checkDigit}, found {code[len(code) - 1]}")
            return True