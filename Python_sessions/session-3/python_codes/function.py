##PART-1###

def  my_function():
    print "Do something"
my_function()

##PART-2###
def say_hi():
    print "hi!"
say_hi()

##PART-3###
def say_hi(name):
    comment = "Hi %s!" % name
    return comment

name = 'Greg'
print say_hi(name)

name2 = 'Wilson'
new_comment = say_hi(name2)
print "Use %s here" % new_comment



