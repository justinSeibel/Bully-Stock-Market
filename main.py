# Bully-Stock-Market
# ver 0.0.1
# reference: http://effbot.org/tkinterbook

import yahoo_finance
from Tkinter import *
import csv

class MainWin:

	def __init__(self, master):

		self.frame = Frame(master)
		self.frame.pack()
		
		self.welcome = Label(self.frame, text="Welcome to Bully Stock Market")
		self.welcome.grid(row=0, columnspan=2)
		
		self.userLabel = Label(self.frame, text="Username: ")
		self.userEntry = Entry(self.frame)
		self.userLabel.grid(row=1, column=0, sticky=W)
		self.userEntry.grid(row=1, column=1)
		
		self.pwdLabel = Label(self.frame, text="Password: ")
		self.pwdEntry = Entry(self.frame)
		self.pwdLabel.grid(row=2, column=0, sticky=W)
		self.pwdEntry.grid(row=2, column=1)
		
		self.registerButton = Button(self.frame, text="Register", command=self.registerSubmit())
		self.loginButton = Button(self.frame, text="Login", command=self.loginSubmit())
		self.loginButton.grid(row=3, column=1)

        
	def loginSubmit(self):
		#todo
		#load Entry data to variables
		self.username = self.userEntry
		self.password = self.pwdEntry
		#call login function
		
  
	def registerSubmit(self):
		#todo
		self.username = self.userEntry
		self.password = self.pwdEntry
		#call register function
	
	#WIP
	def login(self):
		#search csv file
		isUser = False
		usersFile = open('users.csv')
		users = csv.reader(usersFile)
		for row in users:
			if (row == self.username):
				isUser = True
				userRow = row
		correctLogin = False
		if (row[1] == self.password):
			correctLogin = True
		

def main():
	root = Tk()
	mainWin = MainWin(root)
	root.mainloop()


if __name__ == "__main__":
	main()