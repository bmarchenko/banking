# -*- coding: utf-8 -*-

#! /usr/bin/python

#Що нового!
#Назви класів з Великої, визначення класів винесені вгору
#Добавлено метод restrict - обмеження в період 6 міс
#Створено словник і визначення на його основі типу депозиту
#
from math import*

class Deposit: 
        
    def __init__(self, name, depsum, depperiod):
        self.name = name
        self.depsum = depsum
        self.depperiod = depperiod

    def restrict (self):
        global depperiod
        while depperiod < 6:
            print "Dear client, deposit period must be at least 6 monthes"
            depperiod = float(raw_input ("Enter the deposit period in monthes: "))
        
        
    def calc (self):
        self.calc = depsum*depperiod*0.01+depsum

    def printDetails (self):
        print "Dear ", self.name, "your final sum after ", depperiod, " monthes will be ", self.calc, "UAH"
        
class SimpleDeposit (Deposit):
                pass
            
class CompDeposit (Deposit):
    #COMPOUNDED INTEREST
    #Quarterly compounding
    def calc (self):
        self.calc = depsum*(1.025**(depperiod*0.33))

class BonusDeposit (Deposit):

    def bonus (self):
        self.bonus = floor (depperiod/6) * depsum * 0.02

    def calc (self):
        self.calc = depsum*(1.025**(depperiod*0.33)) + float(self.bonus) 

choice = raw_input ("Choose type of deposit you'd like to make: simple, compound or bonus: ")

deplist = ['simple', 'compound', 'bonus']
while choice not in deplist:
    print "Wrong choice!"
    choice = raw_input ("Choose type of deposit you'd like to make: simple, compound or bonus: ")

depdict = {'simple':SimpleDeposit, 'compound':CompDeposit, 'bonus':BonusDeposit}
deposit = depdict[choice](name, depsum, depperiod)    

name = raw_input ("Enter your Name, please: ")
depsum = float(raw_input ("Enter the deposit sum: "))
depperiod = float(raw_input ("Enter the deposit period in monthes: "))




if SimpleDeposit:
    
    deposit.restrict()
    deposit.calc()             
    deposit.printDetails()

        
elif CompDeposit:
                            
     deposit.restrict()    
     deposit.calc()
     deposit.printDetails()
else:

    deposit.bonus()
    deposit.calc()
    deposit.printDetails()


