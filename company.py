import Stock

class Company:
    def __init__(self, data, funds):
        # Initializer function. Takes in "data" (a Stock object) for stockData, then uses the object to set companyName
        # and companyTag. Currently also takes in "funds" (float) for userFundsInvested (should this start as 0 or
        # otherwise be pulled from the user in question?)
        self.stockData = data

        self.companyName = self.stockData.getName()
        self.companyTag = self.stockData.get_symbol()

        # Todo: Figure out how userFundsInvested is actually collected
        self.userFundsInvested = funds

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
        # Todo: Error checking to ensure invalid inputs are blocked and setter returns False instead
        self.stockData = data
        return True

    def setUFI(self, funds):
        # Setter to return UserFundsInvested, returns True if successful
        # Todo: Error checking to ensure invalid inputs are blocked and setter returns False instead
        self.userFundsInvested = funds
        return True
