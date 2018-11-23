import urllib.request
import json
import datetime
from symbol2 import symbol2
from graph import graph


def getPriceHistory(stockAndName, now):
    a = stockAndName[0]
    print(a)
    stockName = stockAndName[1]
    stockInfo = stockAndName[2]
    datasetHigh = []
    datasetLow = []
    dataDays = []
    for x in range(now.day):
        day = str(int(now.day) - x)
        dayint = int(now.day) - x
        if 10 > int(now.day) - x:
            day = "0" + day
        date = str(now.year) + "-" + str(now.month) + "-" + day
        if date in stockInfo['Time Series (Daily)']:
            datasetHigh.append(stockInfo['Time Series (Daily)'][date]['2. high'])
            datasetLow.append(stockInfo['Time Series (Daily)'][date]['3. low'])
            dataDays.append(dayint)
    data = [datasetHigh, datasetLow, dataDays, now.month, stockName, a]
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
