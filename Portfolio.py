import Stock

class Portfolio:
    def __int__(self):
        self.currentFunds = 0.0
        self.ownedStock = []
        self.netGain = 0.0
        self.netLoss = 0.0

    def addFunds(self, addition):
        if(addition < 0):
            print("Unable to add given amount.")
            return False
        else:
            self.currentFunds += addition
            print("Funds added.")
            return True

    def removeFunds(self, subtraction):
        if(subtraction < 0 or subtraction > self.currentFunds):
            print("Unable to remove given amount.")
            return False
        else:
            self.currentFunds -= subtraction
            print("Funds removed.")
            return True

    def buyStock(self, stock, stock_num):
        stock = Stock.Stock(stock)
        if((stock.valueWhenBought() * stock_num) > self.currentFunds):
            print("Unable to purchase stocks.  Insufficient funds.")
            return False
        else:
            self.currentFunds = self.currentFunds - (stock.valueWhenBought() * stock_num)
            self.ownedStock.append(stock)
            self.ownedStock.sort()
            print("Stock purchased.")
            return True

    def sellStock(self, stock, stock_num):
        num = 0
        for item in self.ownedStock:
            if item == stock:
                num += 1
        if(stock not in self.ownedStock or stock_num > num):
            print("Unable to sell stock.  Insufficient number of stock.")
            return False
        else:
            self.netGain = 0
            self.netLoss = 0
            for i in range(stock_num):
                for item in self.ownedStock:
                    if(item == stock):
                        if item.getCurrVal() > item.valueWhenBought:
                            self.netGain = self.netGain + (item.getCurrVal() - item.valueWhenBought)
                        else:
                            self.netLoss = self.netLoss + (item.valueWhenBought - item.getCurrVal())
                        self.currentFunds = self.currentFunds + item.getCurrVal()
                        self.ownedStock.remove(item)
                        break
            if(self.showNetGain() > self.showNetLoss()):
                print("Stock sold for a net gain of ", (self.showNetGain() - self.showNetLoss()), ".")
            else:
                print("Stock sold for a net loss of ", (self.showNetLoss() - self.showNetGain()), ".")
            return True

    def showNetGain(self):
        return self.netGain

    def showNetLoss(self):
        return self.netLoss