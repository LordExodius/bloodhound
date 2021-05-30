# practice webscraping
import requests
from bs4 import BeautifulSoup


def searchFunction(query):
    url = "https://docs.python.org/3/library/functions.html"
    page = requests.get(url)

    print(page.status_code)

    soup = BeautifulSoup(page.content, "html.parser")

    allFunctions = soup.find(id = "built-in-functions")

    functionList = allFunctions.find_all("dl", class_="function")

    funcNames = [func.find("dt").text.rstrip("¶") for func in functionList]

    if query == "help":
        for name in funcNames:
            print(name)

    for func in functionList:
        funcName = func.find("code", class_ = "sig-name descname")
        if funcName.text == query:
            funcHeader = func.find("dt")
            print(funcHeader.text.rstrip("¶"))
            print()
            funcDesc = func.find("dd")
            print(funcDesc.text)
            return True
    
    else:
        print("Function not found.")
        return False

query = ""
print("Search python built-in functions. Enter \"help\" to get a list of all functions.")
while query != "q":
    query = input("Enter a function to search for: ").lower()
    searchFunction(query)
