
class deposit: #1% a month simple interest
    def __init__(self, name, depsum, depperiod, depfinal, interest):
        self.name = name
        self.depsum = depsum
        self.depperiod = depperiod
        self.depfinal = depfinal
        self.interest = interest
        print "Created a profile for "+ name

    def printDetails (self):
        print "Dear ", self.name, "your final sum after ", self.depperiod, " monthes will be ", self.depfinal, "UAH"
        print "DETAILS: "
        print "Name: ", self.name
        print "Deposit period, monthes: ", self.depperiod
        print "Initial deposit sum: ", self.depsum
        print "Final deposit sum: ", self.depfinal
        print "Interest sum: ", self.interest
        
name = raw_input ("Dear client, enter your Name, please: ")
depsum = float(raw_input ("Please, enter the deposit sum: "))
depperiod = float(raw_input ("Please, enter the deposit period in month: "))
interest = depperiod*depsum*0.01
depfinal = depsum+interest
Deposit = deposit (name, depsum, depperiod, depfinal, interest)


print Deposit.printDetails()
