import Stock_RT
import csv

class Portfolio:
    def __init__(self, user):
        self.currentFunds = 0.0
        self.ownedStock = []
        self.netGain = 0.0
        self.netLoss = 0.0
        self.user_name = user

    def getFunds(self):
        return self.currentFunds

    def addFunds(self, addition):
        if(addition < 0):
            print("Unable to add given amount.")
            return False
        else:
            self.currentFunds += addition
            with open(self.user_name + '_$.csv', 'wb') as csvfile:
                fund = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                fund.writerow([self.currentFunds])
            print("Funds added.")
            return True

    def removeFunds(self, subtraction):
        if(subtraction < 0 or subtraction > self.currentFunds):
            print("Unable to remove given amount.")
            return False
        else:
            self.currentFunds -= subtraction
            with open(self.user_name + '_$.csv', 'wb') as csvfile:
                fund = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                fund.writerow([self.currentFunds])
            print("Funds removed.")
            return True

    def buyStock(self, stock, stock_num = 1):
        stck = Stock_RT.Stock(stock)
        print(stck.getValWhenBought())
        print(self.getFunds())
        print(float(stck.getValWhenBought()) * float(stock_num))
        if (float(stck.getValWhenBought()) * float(stock_num)) > self.getFunds():
            print("Unable to purchase stocks.  Insufficient funds.")
            return False
        else:
            self.currentFunds = self.currentFunds - (float(stck.getValWhenBought()) * float(stock_num))
            for i in range(stock_num):
                self.ownedStock.append(stck)
            with open(self.user_name + '.csv', 'wb') as csvfile:
                s_list = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for item in self.ownedStock:
                    s_list.writerow([item.getName(), item.getValWhenBought()])
            with open(self.user_name + '_$.csv', 'wb') as csvfile:
                fund = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                fund.writerow([self.currentFunds])
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
                        if float(item.getCurrVal()) > float(item.getValWhenBought()):
                            self.netGain = self.netGain + (float(item.getCurrVal()) - float(item.getValWhenBought()))
                        else:
                            self.netLoss = self.netLoss + (float(item.getValWhenBought()) - float(item.getCurrVal()))
                        self.currentFunds = self.currentFunds + float(item.getCurrVal())
                        self.ownedStock.remove(item)
                        break
            if(self.showNetGain() >= self.showNetLoss()):
                print("Stock sold for a net gain of $" + str(float(self.netGain - self.netLoss)) + ".")
            else:
                print("Stock sold for a net loss of $" + str(float(self.netLoss - self.netGain)) + ".")
            with open(self.user_name + '.csv', 'wb') as csvfile:
                s_list = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for item in self.ownedStock:
                    s_list.writerow([item.getName(), item.getValWhenBought()])
            with open(self.user_name + '_$.csv', 'wb') as csvfile:
                fund = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                fund.writerow([self.currentFunds])
            return True

    def showOwnedStock(self):
        ret_list = []
        for item in self.ownedStock:
            ret_list.append(str(item.getName()))
            ret_list.append(str(item.getValWhenBought()))
        return ret_list

    def showAmtStock(self):
        ret_dic = {}
        for item in self.ownedStock:
            if item.getName() not in ret_dic:
                ret_dic[item.getName()] = 1
            else:
                ret_dic[item.getName()] += 1
        return ret_dic

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

    def ret_data(self):
        with open(self.user_name + '.csv', 'rb') as csvfile:
            s_list = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in s_list:
                stck = Stock_RT.Stock(row[0])
                stck.setValWhenBought(float(row[1]))
                self.ownedStock.append(stck)
        with open(self.user_name + '_$.csv', 'rb') as csvfile:
            fund = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in fund:
                self.currentFunds = float(row[0])
        return