import urllib.request
import json
import datetime


now = datetime.datetime.now()


def getPriceHistory(a, months):
    url = "https://www.alphavantage.co/query?"
    function = "function=TIME_SERIES_DAILY"
    symbol = "symbol=" + a
    interval = "interval=1min"
    apikey = "apikey=MINCN67P0HGU1H6Q"
    fullURL = url + function + "&" + symbol + "&" + interval + "&" + apikey
    resp = urllib.request.urlopen(fullURL)
    result = json.loads(resp.read())
    graph = []
    stringYear = str(int(now.year) - (months//12))
    stringMonth = now.month - months
    while stringMonth > 1:
        stringMonth += 12
    stringMonth = str(stringMonth)
    stringDate = stringYear + "-" + stringMonth + "-" + "28"
    for x in range((int(now.year) * 12 + int(now.month)) - months):
        graph.append("Time Series (Daily)", result[stringDate])


def ask():
    print("Which stock would you like to check? (By Symbol)")
    a = input()
    print("")
    print("How long ago would you like to browse? (In Months) (Anytime After 01/01/2000)")
    months = int(input())
    totalMonths = (int(now.year) * 12) + int(now.month)
    subtractedMonths = totalMonths - months
    pastDateM = int(subtractedMonths) % 12
    if pastDateM == 0:
        pastDateM = 12
    pastDateY = int(subtractedMonths//12)
    b = str(pastDateM) + "/" + str(now.day) + "/" + str(pastDateY)
    print("")
    print(getPriceHistory(a, months))


print(ask())
