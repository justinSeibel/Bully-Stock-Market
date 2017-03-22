class User:
    def __init__(self, userID=" ", password=" ", userPortfolio=" "):
        self.ID = userID
        self.password = password
        self.portfolio = userPortfolio

    def setUserID(self, newID):
        self.ID=newID
    def getUserID(self):
        return self.ID

    def setPassword(self, newPassword):
        self.password=newPassword
    def getPassword(self):
        return self.password

    def setPortfolio(self, portfolio):
        self.portfolio=portfolio
    def getPortfolio(self):
        return self.portfolio
