import Stock
import csv

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
        stck = Stock.Stock(stock)
        if((stck.getValWhenBought() * stock_num) > self.currentFunds):
            print("Unable to purchase stocks.  Insufficient funds.")
            return False
        else:
            self.currentFunds = self.currentFunds - (stck.getValWhenBought() * stock_num)
            for i in range(stock_num):
                self.ownedStock.append(stck)
            self.ownedStock.sort()
            with open('Stock_List.csv', 'wb') as csvfile:
                s_list = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for item in self.ownedStock:
                    s_list.writerow([item.getName(), item.getValWhenBought()])
            print("Stock purchased.")
            return True

    def sellStock(self, stock, stock_num):
        num = 0
        for item in self.ownedStock:
            if item.getName() == stock:
                num += 1
        if(stock_num > num):
            print("Unable to sell stock.  Insufficient number of stock.")
            return False
        else:
            self.netGain = 0
            self.netLoss = 0
            for i in range(stock_num):
                for item in self.ownedStock:
                    if(item.getName() == stock):
                        if item.getCurrVal() > item.getValWhenBought():
                            self.netGain = self.netGain + (item.getCurrVal() - item.getValWhenBought())
                        else:
                            self.netLoss = self.netLoss + (item.getValWhenBought() - item.getCurrVal())
                        self.currentFunds = self.currentFunds + item.getCurrVal()
                        self.ownedStock.remove(item)
                        break
            if(self.showNetGain() >= self.showNetLoss()):
                print("Stock sold for a net gain of $", (self.netGain - self.NetLoss), ".")
            else:
                print("Stock sold for a net loss of $", (self.NetLoss - self.NetGain), ".")
            with open('Stock_List.csv', 'wb') as csvfile:
                s_list = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for item in self.ownedStock:
                    s_list.writerow([item.getName(), item.getValWhenBought()])
            return True

    def showOwnedStock(self):
        ret_list = []
        for item in self.ownedStock:
            ret_list.append(item.getName())
            ret_list.append(item.getValWhenBought())
        return ret_list

    def showNetGain(self):
        self.netGain = 0
        for stock in self.ownedStock:
            if(stock.getValWhenBought() > stock.getCurrVal()):
                self.netGain = self.netGain + (stock.getValWhenBought() - stock.getCurrVal())
        return self.netGain

    def showNetLoss(self):
        self.netLoss = 0
        for stock in self.ownedStock:
            if (stock.getValWhenBought() < stock.getCurrVal()):
                self.netGain = self.netLoss + (stock.getCurrVal() - stock.getValWhenBought())
        return self.netLoss

    def ret_list(self):
        with open('Stock_List.csv', 'rb') as csvfile:
            s_list = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in s_list:
                stck = Stock.Stock(s_list[0])
                stck.setValWhenBought(int(s_list[1]))
                self.ownedStock.append(stck)
        return