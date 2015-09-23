## To run a specific part please comment rest of teh code by CTRL+3
## To uncomment use CTRL+2

###Part-1###

#open a file by open()
#create and empty file name empty.txtby 'a'
file1 = open("empty.txt", 'a')

###Part-2###

#open a file for writing into it by 'w'
file_handle1 = open("introduction.txt", 'w')
file_handle1.write("James Hutton was a Scottish geologist.")
file_handle1.write("He originated the theory of uniformitarianism; a fundamental principle of geology.\n")
file_handle1.write('''He explained the features of the Earth's crust by means of natural processes over geologic time.
Hutton's work established geology as a proper science, and thus he is often referred to as the Father of Modern Geology.\n-Wikipidia\n''')
file_handle1.close() #close the open file by close()

###Part-3###

#open file by 'with open()', closes the file when you go out of the loop
with open("James_Hutton.csv", 'w') as file_handle2:
    file_handle2.write("Name:\tJames Hutton\n")
    file_handle2.write("Date of birth:\t3 June 1726\n")
    file_handle2.write("Theory of earth:\t1899\n")
    file_handle2.write("Date of death:\t26 March 1797\n")

###Part-4###

#read a file by 'r'
with open("introduction.txt", 'r') as file_handle3:
    with open("introduction_copy.txt", 'w') as file_handle4:
        #For loop to read the contents of the file
        #Entry in newline is considered as next entry
        for entry in file_handle3:
            print entry
            file_handle4.write(entry)
        #write something at the end of the file
        file_handle4.write("\n\nThis is a copy of introduction.txt")

###Part-5###

#read a tab separated file
#there is a more sophisticated way to read such files
#We will discuss that later in the course
with open("James_Hutton.csv", 'r') as file_handle5:
    for jh_entry in file_handle5:
        if 'Name' in jh_entry:
            #use split() to split a sring into list and access the item in position 2
            name = jh_entry.split('\t')[1] 
            print "Name is", name
        elif 'Date' in jh_entry:
            #If you want to serach for a string in a case INsensitive manner
            #use lower() to decapitalize the string
            #try running this string without .lower()
            #Search for BIRTH in jh_entry.upper()
            if 'birth' in jh_entry:
                column_name = jh_entry.split('\t')[0]
                birth = jh_entry.split('\t')[1]
                print column_name, "\t", birth
            elif 'death' in jh_entry:
                column_name = jh_entry.split('\t')[0]
                death = jh_entry.split('\t')[1]
                #use {} and .format() for writing ordered position of strings
                print "{}\t{}".format(column_name, death)
        else:
            column_name = jh_entry.split('\t')[0]
            information = jh_entry.split('\t')[1]
            #use %s for writing ordered position of strings
            print "Other information, %s\t%s" % (column_name, information)
            
            