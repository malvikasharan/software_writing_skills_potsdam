hello = "Hi Human, I am B.O.B. "
question1 = "What is your name? "
response1 = "Thats a lovely name! "
input(hello+question1)
print response1

answer_type = "Please answer in 'yes' of 'no'. "
question2 = "Can I help you? "
response2 = "I am a computer, not a human. "
goodbye = "Great. Goodbye! "
question3 = "Did you like that information? "
answer2 = input(question2+answer_type)
if answer2 == 'yes':
    print "I can't help you.", response2
    answer3 = input(question3+answer_type)
    if answer3 == 'yes':
        print goodbye
    elif answer3 == 'no':
        print "Sorry!"
    else:
        print "I did not understand you."
elif answer2 == 'no':
    print goodbye
else:
    print "I did not understand you."


