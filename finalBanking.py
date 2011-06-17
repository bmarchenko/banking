
#! /usr/bin/python

choice = raw_input ("Dear client, choose type of deposit you'd like to make: simple, compound or bonus: ")
if choice == "simple":
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

elif choice == "compound":
        #COMPOUNDED INTEREST
        #Quarterly compounding
        from bankingParent import*
        class compdeposit (deposit):
            pass
        name = raw_input ("Dear client, enter your Name, please: ")
        depsum = float(raw_input ("Please, enter the deposit sum: "))
        depperiod = float(raw_input ("Please, enter the deposit period in month: "))
        interest = depsum*(1.025**(depperiod*0.33))-depsum
        depfinal = depsum+interest
        Deposit = compdeposit (name, depsum, depperiod, depfinal, interest)

        print Deposit.printDetails()

elif choice == "bonus":
        #bonus  2% of initial sum after every 6 monthes
        from bankingParent import*
        from math import*

        class bonusdeposit:
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

else:
    print "Wrong choice, take care!"
