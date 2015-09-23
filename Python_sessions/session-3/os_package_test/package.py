###part-1###

#import os
#import sys
##help(sys)
#name = sys.argv[1]
#age = sys.argv[2]
#
#print "Age of %s is %s" % (name, age)

###part-2###

import os

#make a new directory
if not os.path.exists("New_dir"):
    os.mkdir("New_dir")

#create some file there
#open('file1.txt', 'a')
#open('file2.txt', 'a')

#check files in the New_dir
#for files in os.listdir("New_dir"):
#    print files

#import os
#os.chdir("New_dir") #equivalent to Unix cd
#### if the following snippets are run after chdir,
## raises OSError
#try:
#    for files in os.listdir("New_dir"):
#        print files
#except OSError:
#    pass #do nothing

