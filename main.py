# Bully-Stock-Market
# ver 0.0.1
# reference: http://effbot.org/tkinterbook

import yahoo_finance
import Tkinter as tk
import csv
from Portfolio import *
from Alert_class import *
from Stock import *
from company import *
from userClass import *

#ref: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
class MainWin(tk.Tk):
	
	def __init__(self):
		tk.Tk.__init__(self)
		
		self.user = User()
		self.alerts = Alert()
		self.portfolio = Portfolio(self.user)
		
		#pack initial container, then subsequent pages
		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		
		self.frames = {}
		for F in (LoginWin, PortfolioWin, FundTransWin, StockWin):
			pageName = F.__name__
			frame = F(parent=container, controller=self)
			self.frames[pageName] = frame
			frame.grid(row=0,column=0,sticky="NSEW")
		self.showFrame("LoginWin")
		
	#reveals the wanted frame
	def showFrame(self, pageName):
		frame = self.frames[pageName]
		frame.tkraise()
		
	def storeData(self, username, password, alerts, portfolio):
		self.user = User(username, password)
		self.alerts = alerts
		self.portfolio = portfolio
	
	def getUser(self):
		return self.user
	def setUser(self, username, password):
		del self.user
		self.user = User(username, password)
		
	def getPortfolio(self):
		return self.portfolio
	def setPortfolio(self, portfolio):
		del self.portfolio
		self.portfolio = portfolio
	
	def getAlerts(self):
		return self.alerts
	def setAlerts(self, alerts):
		self.alerts = alerts


'''
Login page
links to: PortfolioWin
'''
class LoginWin(tk.Frame):

	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		self.controller = controller
		
		self.welcome = tk.Label(self, text="Welcome to Bully Stock Market")
		self.welcome.grid(row=0, columnspan=2)
		
		self.userLabel = tk.Label(self, text="Username: ")
		self.userEntry = tk.Entry(self)
		self.userLabel.grid(row=1, column=0, sticky=tk.W)
		self.userEntry.grid(row=1, column=1)
		
		self.pwdLabel = tk.Label(self, text="Password: ")
		self.pwdEntry = tk.Entry(self)
		self.pwdLabel.grid(row=2, column=0, sticky=tk.W)
		self.pwdEntry.grid(row=2, column=1)
		
		self.registerButton = tk.Button(self, text="Register", command=self.registerSubmit())
		self.loginButton = tk.Button(self, text="Login", command=self.loginSubmit())
		self.loginButton.grid(row=3, column=1)
		
	
	'''
    The following may not be necessary
	if this is covered in the User class
	'''
	def loginSubmit(self):
		#load Entry data to variables
		self.username = self.userEntry
		self.password = self.pwdEntry
		self.login()
		
  
	def registerSubmit(self):
		self.username = self.userEntry
		self.password = self.pwdEntry
		self.register()

	
	def login(self):
		#search csv file
		isUser = False
		userRow = ['\0', '\0']
		usersFile = open('users.csv', 'a+')
		users = csv.reader(usersFile)
		if users == None:
			correctLogin = False
		else:
			for row in users:
				if (row[0] == self.username):
					isUser = True
					userRow = row
					break
			
			correctLogin = False
			if isUser & (userRow[1] == self.password):
				correctLogin = True
			
		if ~correctLogin | ~isUser:
			#placeholder
			print "Username or password incorrect"
		else:
			#placeholder
			print "Login successful"
			self.controller.setUser(self.username, self.password)
			self.controller.showFrame("PortfolioWin")
	
	
	def register(self):
		userAvail = True
		usersFile = open('users.csv', 'a+')
		users = csv.reader(usersFile)
		if users == None:
			userAvail = True
			users.write("Username, Password")
		else:
			for row in users:
				if (row[0] == self.username):
					userAvail = False
		if ~userAvail:
			#placeholder
			print "Username already taken"
		else:
			#placeholder
			#need to write user data to csv file
			users.write(self.username, self.password)
			print "Account created successfully"
			self.controller.setUser = User(self.username, self.password)
			self.controller.showFrame("PortfolioWin")



'''
Portfolio page
links to: FundTransWin, SearchWin, StockWin
'''
class PortfolioWin(tk.Frame):
	
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		
		#ref: https://www.tutorialspoint.com/python/tk_panedwindow.htm
		#self.alertPane = tk.PanedWindow()
		
		self.welcomeLabel = tk.Label(self, text="Welcome, "+controller.getUsername())
		self.welcomeLabel.grid(row=0, column=0, columnspan=2)
		
		self.fundLabel = tk.Label(self, text="Current funds: "+controller.portfolio.getFunds())
		self.fundLabel.grid(row=2, column=0)
		
		self.addFundButton = tk.Button(self, text="Add/Remove Funds", function=self.controller.showFrame("FundTransWin"))
		self.addFundButton.grid(row=2, column=2)
		
		self.seeStockButton = tk.Button(self, text="See Your Stocks", function=self.controller.showFrame("StockWin"))
		self.seeStockButton.grid(row=3, column=0)
		
'''
Funds transaction page
links to: PortfolioWin
'''
class FundTransWin(tk.Frame):
	
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		
		self.titleLabel = tk.Label(self, text="Add or Remove Funds")
		self.titleLabel.grid(row=0, columnspan=2)
		
		self.valLabel = tk.Label(self, text="Enter value: ")
		self.valLabel.grid(row=1, column=0)
		
		self.enterVal = tk.Entry(self)
		self.enterVal.grid(row=1, column=1)
		
		self.addButton = tk.Button(self, text="Add Funds", function=self.addFundsWin())
		self.addButton.grid(row=2, column=0)
		self.addButton = tk.Button(self, text="Remove Funds", function=self.removeFundsWin())
		self.addButton.grid(row=2, column=1)
	
	
	#calls portfolio's addFund function
	def addFundsWin(self):
		if self.enterVal.get() != None:
			self.controller.portfolio.addFunds(self.enterVal.get())
			self.controller.showFrame("PortfolioWin")
		else:
			errorLabel = tk.Label(self, text="No value entered!")
			errorLabel.grid(row=3, column=0)
	
	
	#calls portfolio's removeFund function
	def removeFundsWin(self):
		if self.enterVal.get() != None:
			self.controller.portfolio.removeFunds(self.enterVal.get())
			self.controller.showFrame("PortfolioWin")
		else:
			errorLabel = tk.Label(self, text="No value entered!")
			errorLabel.grid(row=3, column=0)



'''
Stock sell page
links to: PortfolioWin
'''
class StockWin(tk.Frame):
	
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		self.controller = controller
		
		#used in generating stock table
		self.portfolio = controller.getPortfolio()
		
		self.nameLabel = tk.Label(self, text="Name:")
		self.nameLabel.grid(row=0, column=1)
		
		self.ownedLabel = tk.Label(self, text="Amount Owned:")
		self.ownedLabel.grid(row=0, column=2)
		
		self.currentValLabel = tk.Label(self, text="Current Value:")
		self.currentValLabel.grid(row=0, column=3)
		
		self.netGainLossLabel = tk.Label(self, text="Net Gain/Loss:")
		self.netGainLossLabel.grid(row=0, column=4)
		
		#ref: http://stackoverflow.com/questions/7300041/tkinter-create-labels-and-entrys-dynamically
		#generate list of stocks
		portfolioList = self.portfolio.showOwnedStock()
		self.radioButtonVar = ""
		x = 1
		for stock in portfolioList:
			thisStock = Stock(stock)
			
			rb = tk.Radiobutton(self, text="Select", variable=self.radioButtonVar, value=stock)
			rb.grid(row=x, column=0)
			
			#Portfolio class needs function to return amount of stock owned
			stockAmountLabel = tk.Label(self, text=self.portfolio)
			stockAmountLabel.grid(row=x, column=1)
			
			stockValLabel = tk.Label(self, text=thisStock.getCurrVal())
			stockValLabel.grid(row=x, column=2)
			
			if self.portfolio.showNetGain() > 0:
				stockNetLabel = tk.Label(self, text=self.portfolio.showNetGain())
				stockNetLabel.grid(row=x, column=3)
			elif self.portfolio.showNetLoss() > 0:
				stockNetLabel = tk.Label(self, text=self.portfolio.showNetLoss())
				stockNetLabel.grid(row=x, column=3)
		
		self.amountLabel = tk.Label(self, text="Amount to Sell: ")
		self.amountLabel.grid(row=x+1, column=0)
		
		self.amountEntry = tk.Entry(self)
		self.amountEntry.grid(row=x+1, column=1)
		
		self.sellButton = tk.Button(self, text="Sell Stock", function=self.sellStock())
		self.sellButton.grid(row=x+1, column=2)
		
		
	def sellStock(self):
		self.portfolio.sellStock(self.radioButtonVar, self.amountEntry.get())
		self.controller.showFrame("PortfolioWin")
	


'''
Company detail page
links to: ?
'''
class CompanyDetail(tk.Frame):
	
	def __init__(self, parent, controller, compTicker):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		
		stock = Stock(compTicker)
		#self.company = Company()
		

def main():
	mainWin = MainWin()
	mainWin.mainloop()


if __name__ == "__main__":
	main()