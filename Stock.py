"""
Bully Stock Market
"""


from yahoo_finance import *
import urllib2


class Stock:

    def __init__(self, stock):
        self.stock = str(stock)
        incorrect = True
        while incorrect:
            try:
                self.yahoo = Share(self.stock)
                self.value = self.yahoo.get_price()
                self.symbol = stock

            except Exception:
                print "Invalid stock name."
                self.stock = input("Please enter a valid stock name: ")

            else:
                incorrect = False
    '''
    The search_stock method takes the name of the stock the user gives and uses the URL
    to get the symbol for that stock and the price. 
    '''

    def search_stock(self):
        incorrect = True
        while incorrect:
            try:
                url = urllib2.urlopen('http://d.yimg.com/autoc.finance.yahoo.com/autoc?query=' + self.stock + '&region=1&lang=en&callback=YAHOO.Finance.SymbolSuggest.ssCallback')
                the_page = url.read()
                length = len(the_page)

                for each in range(0, length):
                    if the_page[each] == '"':
                        if the_page[each + 1] == 's':
                            index = each + 1
                            break

                symbol = []
                for each in range(index + 9, length):
                    if the_page[each] != '"':
                        symbol.append(the_page[each])
                    if the_page[each] == '"':
                        break
                '''symbol is defined here just in case the user typed the name instead'''
                self.symbol = ''.join(symbol)
                self.yahoo = Share(self.symbol)
                self.value = self.yahoo.get_price()

            except Exception:
                print "Stock not found."
                self.stock = input(str("Retype the name or symbol of stock searching for in single quotes: "))

            else:
                incorrect = False

    '''Returns the symbol'''
    def get_symbol(self):
        return self.symbol

    '''returns the current value'''
    def getCurrVal(self):
        return self.value


    def getName(self):
        self.yahoo = Share(self.symbol)
        name = self.yahoo.get_name()
        return name

    '''returns the value of the stock when bought'''
    def getValWhenBought(self):
        return self.value









#Used this to test the methods in the class


'''main is for testing purposes'''

def main():
    name = input(str("Type in the name of the stock you would like to search for: "))#You have to put it in quotes
    stock = Stock(name)
    stock.search_stock()
    print
    print 'The symbol of the stock you are searching is: ', stock.get_symbol()
    print 'The current value of this stock is: ', stock.getCurrVal()
    print

    print 'The name of this stock is: ', stock.getName()
main()
