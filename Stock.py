"""
Bully Stock Market
"""


from yahoo_finance import *
import urllib
import urllib2

class Stock:

    def __init__(self, stock):
        self.stock = str(stock)


    '''
    The search_stcok method takes the name of the stock the user gives and uses the URL
    to get the symbol for that stock and the price. 
    '''

    def search_stock(self):
        url = urllib2.urlopen('http://d.yimg.com/autoc.finance.yahoo.com/autoc?query=' + self.stock +'&region=1&lang=en&callback=YAHOO.Finance.SymbolSuggest.ssCallback')
        the_page = url.read()
        #the_page = the_page.split()
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

        symbol = ''.join(symbol)

        self.symbol = symbol
        self.yahoo = Share(self.symbol)
        self.value = self.yahoo.get_price() #sets Value at which the stock is bought
        print the_page


    #Returns the symbol
    def get_symbol(self):
        return self.symbol

    #returns the current value
    def getCurrVal(self):
        return self.value


    def getName(self):
        url = urllib2.urlopen(
            'http://d.yimg.com/autoc.finance.yahoo.com/autoc?query=' + self.stock + '&region=1&lang=en&callback=YAHOO.Finance.SymbolSuggest.ssCallback')
        the_page = url.read()
        # the_page = the_page.split()
        length = len(the_page)

        for each in range(0, length):
            if the_page[each] == '"':
                if the_page[each + 1] == "n":
                    index = each + 1
                    break

        name = []
        for each in range(index + 7, length):
            if the_page[each] != '"':
                name.append(the_page[each])

            if the_page[each] == '"':
                break

        name = ''.join(name)
        return name
        
        self.yahoo = Share(self.stock)
        self.value = self.yahoo.get_price()




    #returns the value of the stock when bought
    def getValWhenBought(self):
        return self.value








<<<<<<< HEAD
#Used this to test the methods in the class
=======

>>>>>>> refs/remotes/origin/master
def main():
    stock = Stock('aapl') #you can just change the name to search for whatever stock or you can type in the symbol to get the name
    stock.search_stock()
    print
    print 'The symbol of the stock you are searching is: ', stock.get_symbol()
    print 'The current value of this stock is: ', stock.getCurrVal()
    print
    print 'The name of this stock is: ', stock.getName()
main()
