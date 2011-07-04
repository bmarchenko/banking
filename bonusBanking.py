#! /usr/bin/python

from bankingParent import*
from math import*

class bonusdeposit (deposit):
    def __init__(self, name, depsum, depperiod, depfinal, interest, bonus):
        self.name = name
        self.depsum = depsum
        self.depperiod = depperiod
        self.depfinal = depfinal
        self.interest = interest
        self.bonus = bonus
        
    def printDetails (self):
        print "Dear ", self.name, "your final sum after ", self.depperiod, " monthes will be ", self.depfinal, "UAH"
        print "DETAILS: "
        print "Name: ", self.name
        print "Deposit period, monthes: ", self.depperiod
        print "Initial deposit sum: ", self.depsum
        print "Final deposit sum: ", self.depfinal
        print "Interest sum: ", self.interest
        print "Bonus:", self.bonus
name = raw_input ("Dear client, enter your Name, please: ")
depsum = float(raw_input ("Please, enter the deposit sum: "))
depperiod = float(raw_input ("Please, enter the deposit period in month: "))
bonus = floor (depperiod/6) * depsum * 0.02
interest = depperiod*depsum*0.01
depfinal = depsum+interest+bonus
Deposit = bonusdeposit (name, depsum, depperiod, depfinal, interest, bonus)


print Deposit.printDetails()

  
