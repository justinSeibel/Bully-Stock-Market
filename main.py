# Bully-Stock-Market
# ver 0.0.1
# reference: http://effbot.org/tkinterbook

import yahoo_finance
from Tkinter import *
import csv

#ref: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
class MainWin(Tk):
	
	def __init__(self):
		Tk.__init__(self)
		
		self.username = self.password = self.portfolio = None
		
		#pack initial container, then subsequent pages
		container = Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		
		self.frames = {}
		for F in (LoginWin):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0,column=0,sticky=NSEW)
		self.showFrame("LoginWin")
		
	#reveals the wanted frame
	def showFrame(self, pageName):
		frame = self.frames[pageName]
		frame.tkraise()
		
	def storeData(self, username, password, portfolio):
		self.username = username
		self.password = password
		
		#portfolio = filename? may be redundant
		self.portfolio = portfolio
	
	def getUsername(self):
		return self.username
	def setUsername(self, username):
		self.username = username
		
	def getPortfolio(self):
		return self.portfolio
	def setPortfolio(self, portfolio):
		self.portfolio = portfolio


'''
Login page
links to: PortfolioWin
'''
class LoginWin(Frame):

	def __init__(self, parent, controller):

		Frame.__init__(parent)
		self.controller = controller
		
		self.welcome = Label(self, text="Welcome to Bully Stock Market")
		self.welcome.grid(row=0, columnspan=2)
		
		self.userLabel = Label(self, text="Username: ")
		self.userEntry = Entry(self)
		self.userLabel.grid(row=1, column=0, sticky=W)
		self.userEntry.grid(row=1, column=1)
		
		self.pwdLabel = Label(self, text="Password: ")
		self.pwdEntry = Entry(self)
		self.pwdLabel.grid(row=2, column=0, sticky=W)
		self.pwdEntry.grid(row=2, column=1)
		
		self.registerButton = Button(self, text="Register", command=self.registerSubmit())
		self.loginButton = Button(self, text="Login", command=self.loginSubmit())
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
		userRow = None
		usersFile = open('users.csv')
		users = csv.reader(usersFile)
		for row in users:
			if (row[0] == self.username):
				isUser = True
				userRow = row
				break
		correctLogin = False
		if (userRow[1] == self.password):
			correctLogin = True
		if ~correctLogin | ~isUser:
			#placeholder
			print "Username or password incorrect"
		else:
			#placeholder
			print "Login successful"
			self.controller.showFrame("PortfolioWin")
	
	
	def register(self):
		userAvail = True
		usersFile = open('users.csv', 'a')
		users = csv.reader(usersFile)
		for row in users:
			if (row[0] == self.username):
				userAvail = False
		if ~userAvail:
			#placeholder
			print "Username already taken"
		else:
			#placeholder
			#need to write user data to csv file
			print "Account created successfully"
			self.controller.showFrame("PortfolioWin")



'''
Portfolio page
links to: FundTransWin, SearchWin, Logout(?)
'''
class PortfolioWin(Frame):
	
	def __init__(self, parent, controller):
		Frame.__init__(parent)
		self.controller = controller
		
		self.welcomeLabel = Label(self, text="Welcome, "+controller.getUsername())
		self.welcomeLabel.pack(grid=0, columnspan=2)
		
		self.fundLabel = Label(self, text="Current funds: "+controller.portfolio.currentFunds)
		self.fundLabel.pack(grid=2, column=0)
		
		self.addFundButton = Button(self, text="Add/Remove Funds", function=self.controller.showFrame("FundTransWin"))
		self.addFundButton.pack(grid=2, column=2)
		
		
'''
Funds transaction page
links to: PortfolioWin
'''
class FundTransWin(Frame):
	
	def __init__(self, parent, controller):
		Frame.__init__(parent)
		self.controller = controller
		
		self.titleLabel = Label(self, text="Add or Remove Funds")
		self.titleLabel.pack(grid=0, columnspan=2)
		
		self.valLabel = Label(self, text="Enter value: ")
		self.valLabel.pack(grid=1, column=0)
		
		self.enterVal = Entry(self)
		self.enterVal.pack(grid=1, column=1)
		
		self.addButton = Button(self, text="Add Funds", function=self.addFundsWin())
		self.addButton.pack(grid=2, column=0)
		self.addButton = Button(self, text="Remove Funds", function=self.removeFundsWin())
		self.addButton.pack(grid=2, column=1)
	
	
	#calls portfolio's addFund function
	def addFundsWin(self):
		if self.enterVal.get() != None:
			self.controller.portfolio.addFunds(self.enterVal.get())
			self.controller.showFrame("PortfolioWin")
		else:
			errorLabel = Label(self, text="No value entered!")
			errorLabel.pack(grid=3, column=0)
	
	
	#calls portfolio's removeFund function
	def removeFundsWin(self):
		if self.enterVal.get() != None:
			self.controller.portfolio.removeFunds(self.enterVal.get())
			self.controller.showFrame("PortfolioWin")
		else:
			errorLabel = Label(self, text="No value entered!")
			errorLabel.pack(grid=3, column=0)



def main():
	mainWin = MainWin()
	mainWin.mainloop()


if __name__ == "__main__":
	main()