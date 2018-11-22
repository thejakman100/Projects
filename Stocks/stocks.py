import urllib.request
import json
import datetime
from symbol2 import symbol2
from graph import graph


def getPriceHistory(stockAndName, now):
    a = stockAndName[0]
    stockName = stockAndName[1]
    url = "https://www.alphavantage.co/query?"
    function = "function=TIME_SERIES_DAILY"
    symbol1 = "symbol=" + a
    interval = "interval=1min"
    apikey = "apikey=MINCN67P0HGU1H6Q"
    fullURL = url + function + "&" + symbol1 + "&" + interval + "&" + apikey
    resp = urllib.request.urlopen(fullURL)
    result = json.loads(resp.read())
    datasetHigh = []
    datasetLow = []
    dataDays = []
    for x in range(now.day):
        day = str(int(now.day) - x)
        dayint = int(now.day) - x
        if 10 > int(now.day) - x:
            day = "0" + day
        date = str(now.year) + "-" + str(now.month) + "-" + day
        if date in result['Time Series (Daily)']:
            datasetHigh.append(result['Time Series (Daily)'][date]['2. high'])
            datasetLow.append(result['Time Series (Daily)'][date]['3. low'])
            dataDays.append(dayint)
    data = [datasetHigh, datasetLow, dataDays, now.month, stockName]
    return data


def ask():
    now = datetime.datetime.now()
    print("Which stock would you like to check? (Keep it simple)")
    a = input()
    stockAndName = symbol2(a)
    print("")
    graphData = getPriceHistory(stockAndName, now)
    graph(graphData)


print(ask())
