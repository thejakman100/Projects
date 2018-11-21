import urllib.request
import json
import datetime
from symbol import symbol


def getPriceHistory(a, now):
    url = "https://www.alphavantage.co/query?"
    function = "function=TIME_SERIES_DAILY"
    symbol = "symbol=" + a
    interval = "interval=1min"
    apikey = "apikey=MINCN67P0HGU1H6Q"
    fullURL = url + function + "&" + symbol + "&" + interval + "&" + apikey
    resp = urllib.request.urlopen(fullURL)
    result = json.loads(resp.read())
    datasetHigh = []
    datasetLow = []
    for x in range(now.day):
        day = str(int(now.day) - x)
        if 10 > int(now.day) - x:
            day = "0" + day
        date = str(now.year) + "-" + str(now.month) + "-" + day
        if date in result['Time Series (Daily)']:
            datasetHigh.append(date)
            datasetHigh.append(result['Time Series (Daily)'][date]['2. high'])
            datasetLow.append(date)
            datasetLow.append(result['Time Series (Daily)'][date]['3. low'])

    print(datasetHigh)
    print('')
    print(datasetLow)


def ask():
    now = datetime.datetime.now()
    print("Which stock would you like to check?")
    a = input()
    stock = symbol(a)
    print("")
    getPriceHistory(stock, now)


print(ask())
