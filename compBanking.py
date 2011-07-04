
#COMPOUNDED INTEREST
#Quarterly compounding
#deposit limit >10 UAH
from bankingParent import*
class compdeposit (deposit):
    pass
name = raw_input ("Dear client, enter your Name, please: ")
depsum = float(raw_input ("Please, enter the deposit sum: "))
depperiod = float(raw_input ("Please, enter the deposit period in month: "))
interest = depsum*(1.025**(depperiod*0.33))-depsum
depfinal = depsum+interest
Deposit = deposit (name, depsum, depperiod, depfinal, interest)


print Deposit.printDetails()

