
#! /usr/bin/python

from math import*

#basic banking deposit class
class deposit: #1% a month simple interest
        
    def __init__(self, name, depsum, depperiod):
        self.name = name
        self.depsum = depsum
        self.depperiod = depperiod
        

    def calc (self):
        self.calc = depsum*depperiod*0.01+depsum

    def printDetails (self):
        print "Dear ", self.name, "your final sum after ", self.depperiod, " monthes will be ", self.calc, "UAH"
        


choice = raw_input ("Choose type of deposit you'd like to make: simple, compound or bonus: ")

if choice == "simple":
        #simple interest as basic
        #restriction of deposit period not less than 6 monthes
        
        class simpledeposit (deposit):
                pass
        
        name = raw_input ("Enter your Name, please: ")
        depsum = float(raw_input ("Enter the deposit sum: "))
        depperiod = float(raw_input ("Enter the deposit period in monthes: "))
        while depperiod < 6:
            print "Dear client, deposit period must be at least 6 monthes"
            depperiod = float(raw_input ("Please, enter the deposit period in month: "))
        Deposit = simpledeposit (name, depsum, depperiod)

        Deposit.calc()

        print Deposit.printDetails()

        
elif choice == "compound":
        #COMPOUNDED INTEREST
        #Quarterly compounding
        class compdeposit (deposit):
            def calc (self):
                self.calc = depsum*(1.025**(depperiod*0.33))
                
        name = raw_input ("Enter your Name, please: ")
        depsum = float(raw_input ("Enter the deposit sum: "))
        depperiod = float(raw_input ("Enter the deposit period in monthes: "))
        Deposit = compdeposit (name, depsum, depperiod)

        Deposit.calc()
        
        print Deposit.printDetails()

elif choice == "bonus":
        #bonus  2% of initial sum after every 6 monthes
        class bonusdeposit (deposit):
            def bonus (self):
                self.bonus = floor (depperiod/6) * depsum * 0.02
            def calc (self):
                self.calc = depsum*(1.025**(depperiod*0.33)) + self.bonus 
        name = raw_input ("Dear client, enter your Name, please: ")
        depsum = float(raw_input ("Please, enter the deposit sum: "))
        depperiod = float(raw_input ("Please, enter the deposit period in month: "))
        Deposit = bonusdeposit (name, depsum, depperiod)

        Deposit.bonus()
        Deposit.calc()
        
        print Deposit.printDetails()


