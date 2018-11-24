import matplotlib.pyplot as plt
from dates import monthDet

# This program takes all of the information created in stocks.getPriceHistory()
# and graphs it on a plotself.


def graph(data):
    # Lines 10 - 12 takes information sent to this function and splits it into
    # multiple lists.
    masterList = data
    highs = (masterList[0])
    lows = (masterList[1])
    # The for loop below turns all stock values in highs[] and lows[] and turns
    # them into float values from Strings so they can be graphed correctly.
    for x in range(len(highs)):
        highs[x] = float(highs[x])
        lows[x] = float(lows[x])
    # Lines 20 - 21 creates more lists based on the data sent to this function.
    days = masterList[2]
    word = masterList[5]
    # The remaining lines take all the points and graphs the stock values for
    # the current month. One line for the high values and one for the low ones.
    # It also creates titles for each axis and a title for the graph.
    plt.plot(days, lows, color="blue")
    plt.plot(days, highs, color="red")
    plt.xlabel('Calander Day')
    plt.ylabel('Stock Price in $')
    # Line 30 calls dates.monthDet, which will return a String for the current
    # month based of the int value sent. EX: 11 -> "November".
    plt.title(word + "'s Stock Value in " + monthDet(int(masterList[3])))
    plt.show()
