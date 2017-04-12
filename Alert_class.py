#to do!: implement timer function to check values with thresholds once logged in and every 10 minutes while logged in
#use stock class to implement if statements
#use company class to implement if statements
#use user class to indicate new alerts

class Alert:
    threshold = 0
    def __init__(self, threshold):
        self.threshold = threshold

    def getThreshold(self):
        self.threshold = input("Enter the threshold value: ")
        self.percentthresh = float(self.threshold / 100.00)
        print(self.threshold, self.percentthresh)
        #use threshold times current price when bought to determine threshold value

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
    
    #When a user's net profit/loss reaches threshold (profit/loss based on ALL user funds)
    class Net_alert:
        def __init__(self, obsComp):
            self.company = obsComp

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
