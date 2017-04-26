#to do!: implement timer function to check values with thresholds once logged in and every 10 minutes while logged in
#use stock class to implement if statements
#use company class to implement if statements
#use user class to indicate new alerts
from Stock import*
from threading import Timer
import time
"""
def timeout():
    print("Timeout!: pull newest data to check thresholds")
    #code here to pull newest data to check with thresholds

t = Timer(1 * 10, timeout)
t.start()
"""
class Alert:
    
    #threshold: % value set by user.
    threshold = 0
    #typenum: 1 if stock alert, 2 if company alert, and 3 if net_alert
    typenum = 0
    #newalerts: 0 if no new alerts need to be sent and 1 if new alerts are ready to send
    newalerts = 0
    
    
    def __init__(self, typename):
        #self.threshold = threshold
        self.typename = str(typename)
        self.setType()

    def getThreshold(self):
        self.threshold = input("Enter the threshold % value: ")
        self.percentthresh = float(self.threshold / 100.00)
        print(self.threshold, self.percentthresh)  
        #use threshold times current price when bought to determine threshold value


    def setType(self):
        if self.typename == "stock":
            
            #Stock_alert(self)
            typenum = 1
            print("Type of alert set to Stock_alert", typenum)
            
        if self.typename == "company":
            #Company_alert(self)
            typenum = 2
            print("Type of alert set to Company_alert")
            
        if self.typename == "net":
            #Net_alert(self)
            typenum = 3
            print("Type of alert set to Net_alert")
    
            
    #clear alert
    def ClearAlert(self):
        del self

    #When a Company's stock reaches threshold ()  
    class Company_alert:
        def __init__(self, obsComp):
            self.company = obsComp

    #When Stock price reaches threshold (stock price) -> sendAlert 
    class Stock_alert:
        def __init__(self, obsStock):
            self.stock = obsStock
            print(obsStock.getCurrVal())
            currvalstock = obsStock.getCurrVal()
            #print(self.stock.getName)
    
    #When a user's net profit/loss reaches threshold (profit/loss based on ALL user funds)
    class Net_alert:
        def __init__(self, obsPortfolio):
            self.portfolio = obsPortfolio

    #Sends an alert to the user with the alert enabled when the threshold is reached.
    #def SendAlert():
            #flip the flag in user profile to show new notifications are available
            #print message for alert
            #if stockalert ("The Stock you invested in has reached its set threshold")
            #if companyalert ("The Company you are following has reached its set threshold")
            #if netalert ("Your net funds have reached the current set threshold")

    #if stock alert threshold reached
    #get current stock data
    #compare to threshold
            #sendalert()
    #if company alert threshold reached
    #get current company trend
    #check with threshold set
            #sendalert()
    #if net profit/loss threshold reached
    #get current profit/loss data
    #check with the threshold
            #sendalert()
   
    

    #def setThreshold_Stock():
        #set alert type to a stockalert
        #set threshold for that stockalert

    #def setThreshold_Company():
        #set alert type to a companyalert
        #set threshold for that companyalert

    #def setThreshold_Net():
        #set alert type to a netalert
        #set threshold for that netalert
