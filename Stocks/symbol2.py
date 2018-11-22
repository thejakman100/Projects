import urllib.request
import json


def symbol2(a):
    term = a
    termCheck = []
    strTermCheck = ""
    for x in range(len(term)):
        if x == len(term) - 1:
            termCheck.append(term[x:len(term)])
        else:
            termCheck.append(term[x:(-len(term)+x+1)])
    for x in range(len(termCheck)):
        if termCheck[x] == " ":
            pass
        else:
            strTermCheck += termCheck[x]
    term = strTermCheck
    url = "https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={0}&apikey=MINCN67P0HGU1H6Q".format(
        term)
    resp = urllib.request.urlopen(url)
    data = json.loads(resp.read())
    while len(data['bestMatches']) == 0:
        print(" ")
        print("Cannot retrive information for that company, please select another one.")
        term = input()
        termCheck = []
        strTermCheck = ""
        for x in range(len(term)):
            if x == len(term) - 1:
                termCheck.append(term[x:len(term)])
            else:
                termCheck.append(term[x:(-len(term)+x+1)])
        for x in range(len(termCheck)):
            if termCheck[x] == " ":
                pass
            else:
                strTermCheck += termCheck[x]
        term = strTermCheck
        url = "https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={0}&apikey=MINCN67P0HGU1H6Q".format(
            term)
        resp = urllib.request.urlopen(url)
        data = json.loads(resp.read())
    stockData = data['bestMatches']
    print(" ")
    for x in range(len(stockData)):
        print(str(x + 1) + "." + "Company Name: " + stockData[x]["2. name"])
        print("  " + "Symbol:       " + stockData[x]["1. symbol"])
        print("  " + "Region:       " + stockData[x]["4. region"])
        print(" ")
    print("Please from the stocks above.")
    choose = int(input())
    while (choose - 1) < 0 or (choose - 1) > len(stockData):
        print(" ")
        print("Please type a valid number index.")
        choose = input()
    choice = stockData[choose-1]["1. symbol"]
    name = stockData[x]["2. name"]
    return choice, name
