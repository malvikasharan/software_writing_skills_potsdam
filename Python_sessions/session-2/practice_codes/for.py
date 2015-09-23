###PART-1###

my_list = [1, 2, 'C', 4, 'E']
for i in my_list:
    print i

###PART-2###

#range creates a list of values
for entry in range(1, 5):
    print entry * 237
    
###PART-3###

#print lists of keys and values
my_dict = {'name' : 'Khaleesi', 'age' : 20}
print my_dict.keys(), my_dict.values()
#print all the key-value pairs
for j in my_dict.items():
    print j
#print all the values by accessing keys
for j in my_dict.keys():
    print my_dict[j]
