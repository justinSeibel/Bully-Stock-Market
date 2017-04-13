
"""
Bully Stock Market
"""


from yahoo_finance import *

class Stock():

    def __init__(self, stock):
        self.stock = str(stock)
        self.yahoo = Share(self.stock)
        self.value = self.yahoo.get_price()


    def setValWhenBought(self, price = 0.0):
        self.value = self.yahoo.get_price()
        if(price != 0.0):
            self.value = float(price)

    def getCurrVal(self):
        return self.value

    def getName(self):
        return self.stock

    def getValWhenBought(self):
        return self.value
