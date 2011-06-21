choice = raw_input ("Dear client, choose type of deposit you'd like to make: simple, compound or bonus: ")

while (choice != "simple") or (choice != "compound") or (choice != "bonus"):
    print "Wrong choice!"
    choice = raw_input ("Dear client, choose type of deposit you'd like to make: simple, compound or bonus: ")
else:
    print "Good"
        
