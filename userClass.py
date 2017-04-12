import csv

class User:
    def __init__(self, userID=" ", password=" "):
        self.ID = userID
        self.password = password

    def setUserID(self, newID):
        self.ID=newID
    def getUserID(self):
        return self.ID

    def setPassword(self, newPassword):
        self.password=newPassword
    def getPassword(self):
        return self.password

    def setUserList(self):
        userid=self.getUserID()
        password=self.getPassword()
        with open('user_portfolio.csv', 'ab') as csvfile:
            s_list = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            s_list.writerow([userid, password])
        return True

    def getUserList(self):
        info=[]
        with open('user_portfolio.csv') as csvfile:
            fieldnames=['ID']
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            for row in reader:
                ID=row['ID']
                info.append(ID.split(" "))
        return info
        
