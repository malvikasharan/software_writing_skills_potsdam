###PART-1###

temperature = 20
if temperature >= 25:
    print "Nice weather."
else:
    print "Winter is coming!"
    
###PART-2###

temperature = 26
if temperature >= 25:
    print "Nice weather."
elif temperature < 25:
    print "Winter is coming!"
else:
    print "You gave a wrong value."
    
###PART-3###

temperature = input("The temperature is: ")
if temperature >= 25:
    print "Nice weather."
elif temperature < 25:
    print "Winter is coming!"
else:
    print "You gave a wrong value."
    
###PART-4###

temperature = input("The temperature is: ")
if temperature >= 25 and temperature < 40:
    print "Nice weather."
elif temperature < 25:
    print "Winter is coming!"
else:
    print "You gave a wrong value."
    
###Part-5###

my_list = []
if my_list:
    print "my_list is not empty"
else:
    my_list.append("something")
    
info = "James Hutton was a Scottish geologist."
if 'geologist' in info:
    print info
else:
    print "No geologist was found"
if 'geologist' in info and not 'German' in info:
    print "No German geologist was found"
    