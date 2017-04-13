import Stock_RT
import csv

class Portfolio:
    # This function will set up the basis of a Portfolio.
    # Only requirement is a passed in string for the desired username.
    def __init__(self, user):
        self.currentFunds = 0.0
        self.ownedStock = []
        self.netGain = 0.0
        self.netLoss = 0.0
        self.user_name = user

    # This function will return a value for the current funds a portfolio has.
    # It would be recommended to change the value to a float when it is received.
    def getFunds(self):
        return self.currentFunds

    # This function will add any desired funds to the current amount.
    # Only requirement is a passed in integer or float for the desired amount.
    # I have not tested yet to see if a passed in float or integer will make a difference.
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

    # This function will subtract any desired funds to the current amount.
    # Only requirement is a passed in integer or float for the desired amount.
    # I have not tested yet to see if a passed in float or integer will make a difference.
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

    # This function will take a stock symbol and the designated number wanted to add.
    # Within a single instance, all the stock info will be placed in a list.
    # The ret_data method will allow the retrieval of previously created csv files.
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

    # This function will take a stock symbol and the designated number wanted to remove.
    # This function checks the instance's list and removes the first instance of the desired stock it sees.
    # The ret_data method will allow the retrieval of previously created csv files.
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

    # Returns a list of the stock symbols and their values from the current list of the instance.
    def showOwnedStock(self):
        ret_list = []
        for item in self.ownedStock:
            ret_list.append(str(item.getName()))
            ret_list.append(str(item.getValWhenBought()))
        return ret_list

    # Returns a dictionary of the stock symbols and the amount of how many there are.
    # Key:Value pair is {Stock Symbol:Amount}.
    def showAmtStock(self):
        ret_dic = {}
        for item in self.ownedStock:
            if item.getName() not in ret_dic:
                ret_dic[item.getName()] = 1
            else:
                ret_dic[item.getName()] += 1
        return ret_dic

    # Returns a value of the determined net gain across the current list of stocks and their values.
    def showNetGain(self):
        self.netGain = 0
        for stock in self.ownedStock:
            if(stock.getValWhenBought() > stock.getCurrVal()):
                self.netGain = self.netGain + (stock.getValWhenBought() - stock.getCurrVal())
        return self.netGain

    # Returns a value of the determined net loss across the current list of stocks and their values.
    def showNetLoss(self):
        self.netLoss = 0
        for stock in self.ownedStock:
            if (stock.getValWhenBought() < stock.getCurrVal()):
                self.netGain = self.netLoss + (stock.getCurrVal() - stock.getValWhenBought())
        return self.netLoss

    # This method searches the desired instance's past information through previously created csv files.
    # Adjusts the self.ownedStock and self.currentFunds attributes.
    # Csv files used are (passed in username).csv and (passed in username)_$.csv
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