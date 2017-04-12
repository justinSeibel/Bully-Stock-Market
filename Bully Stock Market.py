"""
Bully Stock Market
"""


from yahoo_finance import *

class Stock():

    def __init__(self, stock):
        self.stock = str(stock)
        self.yahoo = Share(self.stock)
        self.value = self.yahoo.get_price()


    def setValWhenBought(self):
        self.value = self.yahoo.get_price()
        

    def setCurrVal(self):
        self.value = value


    def getCurrVal(self):
        return self.value

    def getName(self):
        return self.stock
        







def main():
    stock  = Stock('AGTK')
    print stock.getCurrVal()
    
main()
