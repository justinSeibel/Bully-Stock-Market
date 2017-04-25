from UserClass import *
my_user = User("justin", "password")
my_user.setUserList()

user2=User("johnDoe", "fancypassword")
user2.setUserList()

user_information = getUserList()


for each in user_information:
    print("userID: "+each[0])
    print("user password: "+each[1])
