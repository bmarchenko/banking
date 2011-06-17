#! /usr/bin/python

#simple interest as basic
#restriction of deposit period not less than 6 monthes
from bankingParent import*
class simpledeposit (deposit):
  pass
name = raw_input ("Dear client, enter your Name, please: ")
depsum = float(raw_input ("Please, enter the deposit sum: "))
depperiod = float(raw_input ("Please, enter the deposit period in month: "))
while depperiod < 6:
    print "Dear client, deposit period must be at least 6 monthes"
    depperiod = float(raw_input ("Please, enter the deposit period in month: "))
interest = depperiod*depsum*0.01
depfinal = depsum+interest
Deposit = simpledeposit (name, depsum, depperiod, depfinal, interest)


print Deposit.printDetails()
  
