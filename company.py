class Company:
    def __init__(self, name, tag, data, funds):
        self.companyName = name
        self.companyTag = tag
        self.stockData = data
        self.userFundsInvested = funds

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