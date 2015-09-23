#this script gives its opinion on weather
temperature = input("The temperature is: ")
if temperature >= 25 and temperature <= 38:
    print "Nice weather."
elif temperature < 25 and temperature >= 0:
    print "Winter is coming!"
elif temperature > 38 and temperature <= 50:
    print "Hot as hell!"
elif temperature < 0 and not temperature < -40:
    print "Hell freezes over!"
elif temperature <= -89.2:
    print "This is lower than recorded lowest temperature."
elif temperature >= 56.7:
    print "This is higher than recorded highest temperature."
else:
    print "This is an extreme or invalid temperature."