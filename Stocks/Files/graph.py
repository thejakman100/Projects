import matplotlib.pyplot as plt
from dates import monthDet


def graph(data):
    masterList = data

    highs = (masterList[0])
    lows = (masterList[1])
    for x in range(len(highs)):
        highs[x] = float(highs[x])
        lows[x] = float(lows[x])
    days = masterList[2]

    word = masterList[5]

    plt.plot(days, lows, color="blue")
    plt.plot(days, highs, color="red")
    plt.xlabel('Calander Day')
    plt.ylabel('Stock Price in $')
    plt.title(word + "'s Stock Value in " + monthDet(int(masterList[3])))
    plt.show()
