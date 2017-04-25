from Portfolio import *
from Alert_class import *
from Stock import *
from company import *
from userClass import *


#users login
def login(username, password):
	isUser = False
	userRow = ['\0', '\0']
	usersFile = open('users.csv', 'a+')
	users = csv.reader(usersFile)
	if users == None:
		correctLogin = False
	else:
		for row in users:
			if (row[0] == username):
				isUser = True
				userRow = row
				break
		
		correctLogin = False
		if isUser & (userRow[1] == password):
			correctLogin = True
	
	if not correctLogin | (not isUser):
		print "Username or password incorrect"
		return None
	else:
		print "Login successful"
		return User(username, password)


#user registration
def register(username, password):
	userAvail = True
	usersFileRead = open('users.csv', 'rb')
	
	#userWrite = csv.writer(usersFile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	users = csv.reader(usersFileRead)
	if users == None:
		userAvail = True
		#users.write("Username, Password")
	else:
		for row in users:
			if (row[0] == username):
				userAvail = False
				break
	if not userAvail:
		print "Username already taken"
		return None
	else:
		# need to write user data to csv file
		usersFileRead.close()
		usersFileWrite = open('users.csv', 'wb')
		userWrite = csv.writer(usersFileWrite, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		userWrite.writerow([username, password])
		print "Account created successfully"
		return User(username, password)



def main():
	print 'Welcome to Bully Stock Market!'
	thisUser = None
	
	while (thisUser == None):
		choice = raw_input("1 - Login\t2 - Register")
		username = raw_input("Enter username: ")
		password = raw_input("Enter password: ")
		if choice == '1':
			thisUser = login(username, password)
		elif choice == '2':
			thisUser = register(username, password)
		else:
			print "Enter value 1 or 2"
	
	#generate portfolio info
	thisPortfolio = Portfolio(thisUser)
	thisPortfolio.ret_data()
	
	choice = '0'
	#main loop
	while (choice != '9'):
		print "Current Funds: " + thisPortfolio.getFunds()
		
		print "Choose one of the following commands: "
		print "1 - Add Funds\t2 - Remove Funds\t3 - See Stocks"
		print "4 - Show Net Gain\t5 - Show Net Loss\t6 - Sell Stock"
		print "7 - Search Stock\t8 - See Alerts\t9 - Quit"
		choice = raw_input()
		
		#"switch" statement
		if choice == '1':
			amount = raw_input("Enter amount to add to account: ")
			thisPortfolio.addFunds(amount)
		elif choice == '2':
			amount = input("Enter amount to remove from account: ")
			thisPortfolio.removeFunds(amount)
		elif choice == '3':
			thisPortfolio.showOwnedStock()
		elif choice == '4':
			print "Stock Net Gain: " + thisPortfolio.showNetGain()
		elif choice == '5':
			print "Stock Net Loss: " + thisPortfolio.showNetLoss()
		elif choice == '6':
			stock = input("Enter stock to sell: ")
			amount = input("Enter amount of stock to sell: ")
			thisPortfolio.sellStock(stock, amount)
		elif choice == '7':
			search = input("Enter search: ")
			stock = Stock(search)
			stock.search_stock()
			#display stock info
		elif choice == '8':
			print "Which type of Alert do you want to set?"
			alertType = 1
			alert = None
			while alertType == 1 | alertType == 2 | alertType == 3:
				alertType = input("1 - Stock Alert\t2 - Company Alert\t3 - Net Alert")
				if alertType == 1:
					alert = Alert("stocks")
				elif alertType == 2:
					alert = Alert("company")
				elif alertType == 3:
					alert = Alert("net")
				else:
					print "Enter a number between 1 and 3"
			#really sets threshold?
			alert.getThreshold()
			
		elif choice == '9':
			print "Logging out..."
			break
		else:
			print "Please enter a choice between 1 and 9"
		


if __name__ == "__main__":
	main()