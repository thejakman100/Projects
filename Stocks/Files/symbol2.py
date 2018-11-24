import urllib.request
import json
from searchResults import searchResults

# This class finds the stocks that might apply to what keyword was choosen in
# stocks.ask(). It also allows you to choose which one you want to graph.


def symbol2(a):
    # Imports keyword from stock.ask()
    term = a
    termCheck = []
    strTermCheck = ""
    # The for loops below take all spaces out of the keyword
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
    # Lines 27-30 take the keyword and turn it into a url to access the API
    url = "https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={0}&apikey=MINCN67P0HGU1H6Q".format(
        term)
    resp = urllib.request.urlopen(url)
    data = json.loads(resp.read())
    # Lines 33-52 checks if there is stock information for the given keyword.
    # If none exists, the code allows you to try a different keyword.
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
    # Lines 59 - 64 Takes all applicable stocks and checks if there is any available
    # price information by calling searchResults.searchResults(). This then returns
    # three lists, one that tells the program which stocks have information (test[]),
    # one that gives all list indexes for the dictionary "stockData" (ints[]),
    # and one that contains the information of all working stocks (Info[]).
    stockData = data['bestMatches']
    print(" ")
    correctResults = searchResults(stockData)
    test = correctResults[0]
    ints = correctResults[1]
    info = correctResults[2]
    # Lines 67 - 83 Displays all stocks that have price information based on
    # the keyword and allows the user to choose the stock they want.
    skip = 0
    newCounter = 0
    for x in range(len(test)):
        if test[x] == 0:
            skip += 1
        else:
            newCounter += 1
            print(str(x + 1 - skip) + "." + "Company Name: " + stockData[x]["2. name"])
            print("  " + "Symbol:       " + stockData[x]["1. symbol"])
            print("  " + "Region:       " + stockData[x]["4. region"])
            print(" ")
    print("Please choose from the stocks above.")
    choose = int(input())
    while (choose - 1) < 0 or (choose) > newCounter:
        print(" ")
        print("Please type a valid number index.")
        choose = int(input())
    # The remaining lines create "choice", which is a String that contains the
    # symbol for the choosen stock, "name" contains the name of the stock that
    # was chosen, and "realChoice" contains the choosen stocks information.
    # And then returns these values to stocks.ask().
    choice = stockData[ints[choose-1]]["1. symbol"]
    name = stockData[ints[choose-1]]["2. name"]
    realChoice = info[choose-1]
    return choice, name, realChoice
