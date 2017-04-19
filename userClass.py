import csv
from Portfolio import *

class User:
    def __init__(self, userID=" ", password=" "):
        self.ID = userID
        self.password = password
        #self.portfolio = Portfolio(ID)

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
        with open('users.csv', 'ab') as csvfile:
            s_list = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            s_list.writerow([userid, password])
        return True

def getUserList():
    info=[]
    with open('users.csv') as csvfile:
        fieldnames=['ID']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        users=[]
        for row in reader:
            pair=[]
            ID=row['ID']
            info=ID.split(" ")
            name=info[0]
            password=info[1]
            pair.append(name)
            pair.append(password)
            users.append(pair)
    return users
