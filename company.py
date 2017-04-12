class Company:
    def __init__(self, name, tag, data, funds):
        #Would "name" not be given but instead found from the API based on the tag given?
        self.companyName = name
        self.companyTag = tag
        #Would "data" not be given but instead found from the API based on the tag given? Or how in general would this
        #work?
        self.stockData = data
        #Would "funds" not be given but instead found from the program based on the user in question? Or how in general
        #would this work?
        self.userFundsInvested = funds

    def updateData(self):
        #I forget what this one's supposed to do
        pass

    def getName(self):
        return self.companyName

    def getTag(self):
        return self.companyTag

    def getStock(self):
        return self.stockData

    def getUFI(self):
        return self.userFundsInvested

    def setName(self, name):
        self.companyName = name
        return True

    def setTag(self, tag):
        self.companyTag = tag
        return True

    def setStock(self, data):
        self.stockData = data
        return True

    def setUFI(self, funds):
        self.userFundsInvested = funds
        return True