# Bully-Stock-Market
# ver 0.0.1
# reference: http://effbot.org/tkinterbook

import yahoo_finance
from Tkinter import *

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
        
        
        self.button = Button(self.frame, text="test", command=self.test )
        self.button.grid(row=3, columnspan=2)


    def test(self):
        lab = Label(self.frame, text="Hello world!")
        lab.grid(row=4, columnspan=2)


def main():
    root = Tk()
    mainWin = MainWin(root)
    root.mainloop()


if __name__ == "__main__":
    main()
    
