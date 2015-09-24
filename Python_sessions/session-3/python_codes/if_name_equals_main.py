
#define a function that you can call later
def function_name(variable_1, variable_2):
'''this tells what the program does'''
    if variable_1 >= variable_2:
        print "Do something"
    elif variable_1 < variable_2:
        print "Do something different"
    else:
        print "Something's wrong"

if __name__ == '__main__': 
##this physically separates the functions from executions
## since everything in the left most position is read while running the program
## Python now reads everything below __name__ == '__main__'

    variable_1 = sys.argv[1] #user provides this on the commandline "Python script_name.py variable_1"
    variable_2 = sys.argv[2] #user provides this on the commandline "Python script_name.py variable_1 variable_2"
    #call_function
    function_name(variable_1, variable_2)
    
