### Most of these functions are very small to be written as function
### Use these for practice and understanding only

###if.py###

def check_temperature(temperature):
    temperature = input("The temperature is: ")
    if temperature >= 25 and temperature < 40:
        print "Nice weather."
    elif temperature < 25:
        print "Winter is coming!"
    else:
        print "You gave a wrong value."

temperature = 26
#check_temperature(temperature)
#
#temperature_2 = input("The temperature is: ")
#check_temperature(temperature_2)

###for.py###

###PART-1###
def print_my_list_items(my_list):
    for i in my_list:
        print i
        
my_list = [1, 2, 'C', 4, 'E']
#print_my_list_items(my_list)

##function implemented on dict
my_dict = {'name' : 'Khaleesi', 'age' : 20}
for items in my_dict.items():
    ''
    #print "New item:"
    #print_my_list_items(items)

###PART-2###    
#range creates a list of values

def multiply(range1, range2, multiplier):
    for entry in range(int(range1), int(range2)):
        print entry * float(multiplier)

#multiply(1, 5, 237)
#multiply(197, 57, 1237)

###PART-3###

#return lists of keys and values
def return_key_val_lists(my_dict):
    ## more than two values can be returned
    return my_dict.keys(), my_dict.values() 

#return all the key-value pairs 
def print_key_val_pair(my_dict):
    for j in my_dict.items():
        print j
        
#return all the values by accessing keys
def return_values_from_keys(my_dict, j):
        return my_dict[j]
    
my_dict = {'name' : 'Khaleesi', 'age' : 20}

key_list, value_list = return_key_val_lists(my_dict)
print "Key list is %s and value list is %s" % (
    key_list, value_list)

lists = return_key_val_lists(my_dict)
print "\nKey list is %s and value list is %s" % (
    lists[0], lists[1])

print "\nKey value pairs are:"
key_val_pairs = print_key_val_pair(my_dict)

for j in my_dict.keys():
    print return_values_from_keys(my_dict, j)
