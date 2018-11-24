import urllib.request
import json

# This code takes the keyword from symbol2.symbol2() and checks which stock results
# have actual values assigned to them. The code then sends the list of usable
# stocks back with information on how to display the stocks in symbol2.symbol2() and
# also returns the save data of all the usable stocks.


def searchResults(stockData):
    # Lines 12 -19 creates the initial link to start ruling out stocks.
    url = "https://www.alphavantage.co/query?"
    function = "function=TIME_SERIES_DAILY"
    interval = "interval=1min"
    apikey = "apikey=MINCN67P0HGU1H6Q"
    test = []
    a = " "
    symbol1 = "symbol=" + a
    fullURL = url + function + "&" + symbol1 + "&" + interval + "&" + apikey
    # Lines 21 - 23 Creates variables that will collectivly keep track of which stocks work.
    counter = 0
    track = []
    info = []
    # The remaining lines below goes through 4 of the top stock results and decides
    # Which ones have values. It then keeps track of the index in which the stock
    # information will be stored in and sends that information back to symbol2.symbol2().
    for x in range(len(stockData)):
        if counter == 4:
            break
        a = stockData[x]["1. symbol"]
        symbol1 = "symbol=" + a
        fullURL = url + function + "&" + symbol1 + "&" + interval + "&" + apikey
        resp = urllib.request.urlopen(fullURL)
        result = json.loads(resp.read())
        if 'Time Series (Daily)' in result:
            track.append(x)
            counter += 1
            test.insert(x, 1)
            info.append(result)
        else:
            counter += 1
            test.insert(x, 0)
    return test, track, info
