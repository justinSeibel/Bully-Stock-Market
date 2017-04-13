"""
Bully Stock Market
"""


from yahoo_finance import *
import urllib
import urllib2

class Stock():

    def __init__(self, stock):
        self.stock = str(stock)


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


    def get_symbol(self):
        return self.symbol


    def getCurrVal(self):
        return self.value

    '''
    def getName(self):
        url = urllib2.urlopen(
            'http://d.yimg.com/autoc.finance.yahoo.com/autoc?query=' + self.stock + '&region=1&lang=en&callback=YAHOO.Finance.SymbolSuggest.ssCallback')
        the_page = url.read()
        # the_page = the_page.split()
        length = len(the_page)

        for each in range(0, length):
            if the_page[each] == '"':
                if the_page[each + 1] == "n":
                    index = the_page[each + 1]
                    break

         
        #for each in range(index, length + 7):
        '''


    def getValWhenBought(self):
        return self.value









def main():
    stock = Stock('intel') #you can just change the name to search for whatever stock
    stock.search_stock()
    print
    print 'The symbol of the stock you are searching is: ', stock.get_symbol()
    print 'The current value of this stock is: ', stock.getCurrVal()
    print
    stock.getName()
main()
