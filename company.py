from Stock import *
from Portfolio import *
from yahoo_finance import *

class Company:
    def __init__(self, data, folio):
        # Initializer function. Takes in "data" (a Stock object) for stockData, then uses the object to set companyName
        # and companyTag. Takes in "folio" (the User's Portfolio) to calculate userFundsInvested. Also, does this
        # need to be error-checked or do we assume the initializer will be correct?

        # Error-checks for data being type Stock, will raise TypeError exception if not.
        # Todo: Whatever code creates Company objects will need to have exception handling for if the initializer returns TypeError
        # Todo: Fix error-checking for data's type ( type(data) returns 'instance', not 'Stock')
        self.stockData = data

        # Currently pulling companyName from Stock's Yahoo API get_name() function. Once Stock class has its own getName
        # function working, replace this call with that.
        self.companyName = self.stockData.yahoo.get_name()
        # self.companyName = self.stockData.getName()
        self.companyTag = self.stockData.get_symbol()

        userStock = folio.showOwnedStock()
        userVal = 0.0
        for i in range(0,len(userStock),2):
            if userStock[i] == self.companyTag:
                userVal = float(userStock[i+1])
                break
        if userVal != 0.0:
            userNum = folio.showAmtStock()
            numStock = userNum[self.companyTag]
            self.userFundsInvested = userVal * numStock
        else:
            self.userFundsInvested = 0.0

    def updateData(self):
        # I forget what this one's supposed to do
        pass

    def getName(self):
        # Getter to return companyName
        return self.companyName

    def getTag(self):
        # Getter to return companyTag
        return self.companyTag

    def getStock(self):
        # Getter to return stockData
        return self.stockData

    def getUFI(self):
        # Getter to return userFundsInvested
        return self.userFundsInvested

    def setName(self, name):
        # Setter to set companyName, returns True if successful
        # Todo: Error checking to ensure invalid inputs are blocked and setter returns False instead
        self.companyName = name
        return True

    def setTag(self, tag):
        # Setter to return companyTag, returns True if successful
        # Todo: Error checking to ensure invalid inputs are blocked and setter returns False instead
        self.companyTag = tag
        return True

    def setStock(self, data):
        # Setter to return stockData, returns True if successful
        # Todo: Redo error-checking for type of data ( type(data) returns 'instance', not 'Stock')
        '''
        if type(data) != Stock:
        # Error-checking for non-Stock "data" passed
        return False
        '''
        self.stockData = data
        return True

    def setUFI(self, funds):
        # Setter to return UserFundsInvested, returns True if successful
        try:
            # Theoretically should trip TypeError if invalid variable type for "funds" passed
            ifunds = float(funds)

            if ifunds < 0:
                # Error-checking for negative value for "funds" passed
                return False

            else:
                self.userFundsInvested = ifunds
                return True

        except (TypeError,ValueError):
            # Error-checking for non-float "funds" passed
            return False

        except:
            # Broad error-checking to catch anything else (will still raise the error but will tell us that it's not
            # one we're set up to catch
            print "Unexpected error"
            raise


# Bare-bones main function to test company class
def main():
    test = Stock('sony')
    test.search_stock()
    testc = Company(test,0)
    print testc.getName()
    print testc.getTag()
    print testc.getStock()
    print testc.getUFI()
    print
    tbool = testc.setUFI('dafsadfadf')
    print tbool
    print testc.getUFI()
    tbool = testc.setUFI(-42)
    print tbool
    print testc.getUFI()
    print 'done with bad example'
    print
    print
    test = Stock('microsoft')
    test.search_stock()
    testc = Company(test,250)
    print testc.getName()
    print testc.getTag()
    print testc.getStock()
    print testc.getUFI()
    print
    tbool = testc.setUFI(500)
    print tbool
    print testc.getUFI()
    test = Stock('nintendo')
    tbool = testc.setStock(test)
    print tbool
    print testc.getStock()
    input('done with good example')
main()
