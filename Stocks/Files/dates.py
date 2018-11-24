# This code takes the int value sent from graph.graph() and sends back the name
# of the month corrisponding with that number.


def monthDet(a):
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    return months[a-1]
