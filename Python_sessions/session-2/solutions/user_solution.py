#1. Start, get user's name
user_name = input("Please provide your name: ")

#2. check if the name is Rowen (if true, ask for password else print "Access denied")
if user_name == 'Rowen':
    #3. if the password is correct write 'welcome' else print 'incorrect'
    #lets assume the password is 123456
    password = input("Please provide your password: ")
    if password == 123456:
        print "Welcome"
    else:
        print "Incorrect"
else:
    print "Access denied"