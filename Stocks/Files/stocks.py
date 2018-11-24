import datetime
from symbol2 import symbol2
from graph import graph

# This method takes information sent from stocks.ask() which was created in
# symbol2.symbol2()and turns it into graphable data for the wanted stock.


def getPriceHistory(stockAndName, now):
    # Lines 13 - 16 Takes all variables from stockAndName (Which was created in
    # stocks.ask() based off of the data taken from symbol2.symbol2()) and
    # turns them into their own variables. The stock symbol is also printed.
    a = stockAndName[0]
    print(a)
    stockName = stockAndName[1]
    stockInfo = stockAndName[2]
    # Lines 19 - 21 initializes a list for all the stocks high values,
    # low values, and the days the stock was recorded into the API.
    datasetHigh = []
    datasetLow = []
    dataDays = []
    # The for loop below searchs the json stockInfo and applies its highs and
    # lows to the high and low matracies created above and records which days
    # there is stock information for, which is recorded in dataDays[].
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
    # The remaining lines puts the information found into one list called
    # data[] and is then returned to stocks.ask().
    data = [datasetHigh, datasetLow, dataDays, now.month, stockName, a]
    return data

# This method asks for the intial search to find stocks. It also sends the
# stock info taken from symbol2.symbol2() and sends it to stocks.getPriceHistory() to be readied
# for graphing. This code also takes that data created in stocks.getPriceHistory()
# and sends it to graph.graph().


def ask():
    # Introduces current time as a variable
    now = datetime.datetime.now()
    # Asks for wanted stock
    print("Which stock would you like to check? (Keep it simple)")
    a = input()
    # Lines 55 - 58 sends the information from symbol2.symbol2(), sends it to
    # stocks.getPriceHistory() to be used for graphing information, which then returns
    # back and is sent to graph.graph().
    stockAndName = symbol2(a)
    print("")
    graphData = getPriceHistory(stockAndName, now)
    graph(graphData)

# The line below initializes the program by running stocks.ask().


print(ask())
