#1. start: set initial value of total_score to 0
#and create a vovel list
total_score = 0
vowels = ['a', 'e', 'i', 'o', 'u']

#2. Ask player's name
name = input("Please enter your name\n")

#3. Is there a character to check (for loop)
for chars in name:
    #4. If the character vowel subtract 1 score
    #else add 1
    if chars in vowels:
        total_score -= 1 
    else:
        total_score += 1
#5. Print total score
print "Your total score is %s." % total_score