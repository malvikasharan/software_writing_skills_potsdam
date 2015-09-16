Novice Unix Shell:
======

Introduction
------

UNIX is a computer operating systems (OS) and shell provides an interface to execute commands and programs in Unix. 

We can open shell terminal to work with some basic commands.

The first thing you will notice is a dollar sign. This is command prompt, issued by shell that suggests that the commands can be typed. A command followed by Enter key (or return key) allows shell to read and execute the command. We refer this as running a command (command + Enter/return key).

Run command `date`, to get the date and time and press Enter key:
        > `$ date`

It displays an output like this:
Wed Sep 23 10:27:19 CEST 2015

A new prompt `$` is printed after a command is executed that tells us that it's ready for more commands.

Run command whoami to get ID of the current user:
        &ensp;`$ whoami`
    
Accessing files and directories:
------

The part of OS responsible for managing files and directories (folders) is called file system. It organizes our data into files and folders. 

To identify where we are in the system, run `pwd` command, which stands for “print working directory”:
        &ensp;`$ pwd`

This displays the current working directory (path of the current location) which would look something like this:
        &ensp;`$ /Users/username…`

By default you are in the folder 'software_writing_skills'. Check what's in the current working directory by running `ls` (stands for listing):
        &ensp;`$ ls`

This displays all the files and folders in the current working directory, which are examples, shell_introduction.txt and shell_material.txt. By using the flag `-F`, we can get a more comprehensible output of the command `ls`, which adds a trailing '/' to the name of directories (examples/).
	&ensp;`$ ls -F`

There are several flags that can be used with ls. For example:
	&ensp;`$ ls -r` (r stands for reverse, lists file and folders in reverse order)
	&ensp;`$ ls -a` (a stand for all, lists everything including the special files)
	&ensp;`$ ls -s` (s stands for sort, lists files and folders in alphabetical order)
        &ensp;`$ ls -R` (R stands for recursive, lists the contents of directories recursively)
        &ensp;`$ ls -t` (t stands for time, lists things by time of last change)

Additionally, multiple flags can be used in the same command:
	&ensp;`$ ls -R -s`

A file or folder can be addressed with an absolute or a relative path. One can access the files in the current folder directly by using a relative path, which refers to the folder relative to the current path. To access files in different folder the absolute path should be provided which refers to the whole path (starts with /). For example, using `pwd` command the absolute path of the current working directory is displayed. 

By giving the name of the folder (in the current working directory or the full path of a folder somewhere else) one can see the contents of the folder:
	&ensp;`$ ls examples`

We can use `cd` followed by a directory name to change our working directory. cd stands for “change directory”, which is a bit misleading: the command doesn't change the directory; it changes the shell's idea of what directory we are in. We can change our current directory by moving to 'examples' folder.
	&ensp;`$ cd examples`

We can check the changed working directory by `pwd` and we can run `ls -F` to see the files in the current path.

To go down to the directory enclosing the current files and folders we can use `cd ..`, where `..` refers to a special directory, meaning “the directory containing this one”, or more concisely, the parent of the current directory. If we run `pwd` after running `cd ..` we're back in the last location.

The default `cd` changes the working directory to the users home directory.
	&ensp;`$ cd`

To go back to the last location of working directory we can either cd followed by the absolute path or type in `cd -`.
	&ensp;`$ cd -`

Creating and editing files and folders
------

To create a new directory in the current path run `mkdir` followed by directory name.
	&ensp;`$ mkdir first_folder`

We can change our current working folder to the newly created folder by `cd first_folder`. We can further create folder(s) into this folder by using `mkdir` followed by foldername.
	&ensp;`$ mkdir second_folder`

To create an empty file in the current path, run `touch` command followed by filename.
	&ensp;`$ touch testfile1.txt`

Or we can create a file while writing into it by using text editors like nano, Vim, Emacs etc. For example here we will use nano editor to write something into the file:
	&ensp;`$ nano testfile2.txt`

Using Control-O (+Enter key) we can write our data to disk. Once the file is saved we can use Control-X to quit the editor and return to the shell. More options are displayed at the bottom of the editor. Alternatively, we can use graphical editors like Gedit and Komodo or Notepad++ in windows for writing into the file.

Run `ls` to see the created file/files.
	&ensp;`$ ls` (this will show testfile1.txt, testfile2.txt and second_folder that you created in the current path)

An asterisk * is a wild card, which in shell stands for everything. * can be used in the commands to execute an action of everything, in this context files and folders. We can use `ls *.txt` to list all the files that comprise of .txt file extension. 

The file can be copied from one path to another by using `cp` command.
	&ensp;`$ cp testfile2.txt second_folder`

All the .txt files can be copied into the second_folder by using `*`.
	&ensp;`$ cp *.txt second_folder`

The file can be renamed while copying to another location or folder:
	&ensp;`$ cp testfile2.txt second_folder/testfile3.txt`

The file can re-named and copied into the same folder in the same manner except that the path of the folder is not required.
	&ensp;`$ cp testfile2.txt testfile4.txt`

The file can be moved to another location by using the command `mv`. The files can be renamed while moving in similar manner as mentioned above.
	&ensp;`$ mv testfile4.txt second_folder/`

The contents in the folder are removed by using `rm` followed by the name of the folder in the current path or the absolute path of the folder. 
        &ensp;`$ rm testfile1.txt`	
        &ensp;`$ rm second_folder/testfile1.txt`
	
You can check is we really deleted the file by using `ls` command. 

To delete an entire folder `-r` flag is used which stands for recursive. 
	&ensp;`$ rm -r second_folder/`

`rm *` will remove all the files in the current working directory. There us no trash bin in unix shell, which means if you delete a file or a folder, it is deleted forever and can not be restored.

These were the basic Unix shell commands. In the beginning you will have many questions about what does a command do, what are flags that can be used with a command etc. An important command `man` (stands for manual) can be used understand each commands in detail. For example, to get the documentation of `ls` command:
	&ensp;`$ ls man`

To close the manual use `q`. Additionally many tools offer help via the parameter `-h`, `-help` or `-help`.
	&ensp;`$ ls -help`

Few keyboard shortcuts that will come in handy:
	&ensp;Tab: to extend command or file/folder names
Up and down key: to call the previously used commands
	&ensp;Ctrl+l: clear the screen (optionally type clear to do the same)
	&ensp;Ctrl+A: to move to the beginning of the file
	&ensp;Ctrl+e: to move to the end of the file
	&ensp;Ctrl+c: stop the command that is currently running
        &ensp;Ctrl+z: to send the currently running command to the background. The `fg` command is used to bring the background commands to foreground.

Handling contents of the files and folders
------

Earlier we learnt the use of editors to create and edit a file. In this next part we will see what more can be done for handling a file. For this, we will work on some example files to get a better understanding. I have saved some mock files in the folder 'software_writing_skills/examples'. if you are in the folder first_folder, go the folder software_writing_skills by typing:
        &ensp;`$ cd ..`
	&ensp;`$ cd software_writing_skills/examples`

`less` and `more` commands are used to view the file content without editing. Use `q` to quit the file viewing by `less`.
	&ensp;`$ less permafrost_database.txt`
	&ensp;`$ more permafrost_database.txt`

Using `less` the file can be viewed by scrolling up and down, but by using `more` the first few lines of the files can be seen on the terminal.

To see the first or last few lines of the file, use `head` and `tail` commands respectively. 
        &ensp;`$ head permafrost_database.txt`
	&ensp;`$ tail permafrost_database.txt`

Flag `-n` with the commands `head` and `tail` is used to specify the number of lines that you want to view. For example, to view first 10 lines of the file either of the following commands can be used:
	&ensp;`$ head -n 10 permafrost_database.txt`
	&ensp;`$ head -10 permafrost_database.txt`

`cut` command is used to extract certain fields of the file. Unlike `less`, `more`, `head` and `tail` where the file can extracted horizontally, `cut` helps in extract the vertical file contents.

Show character at position 2 in each line:
	&ensp;`$ cut -c2 permafrost_database.txt`

Show characters from position 2 to position 5 in each line:
	&ensp;`$ cut -c2-5 permafrost_database.txt`

Show characters at position 2 and 5:
	&ensp;`$ cut -c2,5 permafrost_database.txt`

Show characters starting at position 2 till the end:
	&ensp;`$ cut -c2- permafrost_database.txt`

Show characters from the beginning till the position 5:
	&ensp;`$ cut -c-5 permafrost_database.txt`

The flag `-d` specifies the field delimiter used in the input file (comma, tab) and flag `-fà specifies the field (divided by the delimiter) we want to see:
	&ensp;`$ cut -d',' -f1 permafrost_database.txt`

These are different options of `cut` commands that can be used for reading files. However, the practical use of this command is in reading a file that contains table. A table comprise of values that are separated by special characters like comma `,` or tab `\t` that can be used to visualize certain column (also known as field). In the current folder we have a table geochemistry_germany_rivers.tab containing several columns that are seaparated by tab. By using `less` you can check the contents of the file. We can extract the values in the column 3:
	&ensp;`$ cut -d$'\t' -f3 geochemistry_germany_rivers.tab`

Regular expressions (for e.g.: specific strings) are searched in files by using command `grep`:
	&ensp;`$ grep permafrost permafrost_database.txt`

Count the occurrence of the string by using the flag `-c`:
	&ensp;`$ grep permafrost -c permafrost_database.txt`

To make the search case insensitive `-i` flag can be used:
	&ensp;`$ grep permafrost -c -i permafrost_database.txt`

We can extract the entire content of the file on the terminal by using `cat`.
	&ensp;`$ cat geochemistry_germany_rivers.tab`

The wide use ofthe command `cat` is to collect the entire contents of the file for further analysis like for writing the content from one file to another (in relative or absolute path).
	&ensp;`$ cat geochemistry_germany_rivers.tab > copy_germany_rivers.tab`
	&ensp;`$ cat temperature_course.txt permafrost_database.txt > abstracts.txt`

Please check the contents of abstract.txt by `less`.

To print something on the terminal, `echo` command is used.
	&ensp;`$ echo “print this!”`

`echo` can also be used to append something to a file:
	&ensp;`$ echo “Combining all the abstract files” > abstract.txt`

The `>` symbol directs the given content to the destination file, however this overwrites the contents if the destination file already exists. This you can realize by checking the abstract.txt file now, which contains only one line that you wrote by using echo command. To avoid the overwriting, `>>` is used:
	&ensp;`$ echo “Combining all the abstract files” > abstract.txt`
	&ensp;`$ echo “Abstract-1” >> abstract.txt`
	&ensp;`$ cat temperature_course.txt >> abstract.txt`
	&ensp;`$ echo “Abstract-2” >> abstract.txt`
	&ensp;`$ head -20 permafrost_database.txt >> abstract.txt`

In another example we will collect few columns (column 3 and 5) from the file geochemistry_germany_rivers.tab
	&ensp;`$ cut -d$'\t' -f3,5 geochemistry_germany_rivers.tab >> water_depth.txt`

To remove empty lines from the file use following:
	&ensp;`$ awk 'NF > 0' water_depth.txt > new_water_depth.txt`

To count the total number of lines `wc -l` command is used. For example, this command can be used for counting total number of lines in file:
	&ensp;`$ wc -l water_depth.txt`
	&ensp;`$ wc -l new_water_depth.txt`

In order to sort the content of a file the command `sort` is used. By default the sorting takes placed alphabetically but several flags can be used to specify the type of sorting, for example, `sort -n` numerical sorting, `sort -r` reverse sorting etc.
	&ensp;`$ sort new_water_depth.txt`
        &ensp;`$ sort -n new_water_depth.txt`
	&ensp;`$ sort -r new_water_depth.txt`
	&ensp;`$ sort -n new_water_depth.txt > sorted_water_depth.txt`

To view non-redundant contents of a file `uniq` command is used:
	&ensp;`$ uniq sorted_water_depth.txt`

By using the `-c` flag with `uniq`, the number of occurrence of each entry can be seen as the first field on ther terminal.
	&ensp;`$ uniq -c sorted_water_depth.txt`

Loops:
------

Wildcards `*` and keyboard shortcuts are two ways to reduce typing (and typing mistakes). Another is to tell the shell to do something over and over again when we intend to carry out same action on 1000 files, which is impractical and tiring. Instead, we can use a loop to do some operation once for each thing in a list. Here's a simple example that displays the first three lines of each file in turn (write each of the following lines one by one):
        &ensp;`$ for filename in permafrost_database.txt temperature_course.txt `
        &ensp;`> do`
        &ensp;`>    head -3 $filename`
        &ensp;`> done`

As you noticed that in the 'for-loop', each file is taken one by one as a variable filename. This variable will be referred with a `$` in the 'for-loop' ($filename). `>` in the command above shows that more commands can be written as the action is not finished.

Combining commands:
------

In Unix we can connect several commands by pipe `|` to run several actions on standard input and standard output in a stepwise manner.
	&ensp;`$ cat water_depth.txt | head -5 | tail -5 | sort`

Shell Scripts
------

Shell is a powerful programming environment because it allows us to take the commands we repeat frequently and save them in files. The file extension for Shell script is '.sh' and using this file we can re-run all the operations again by using a single command. For historical reasons, a bunch of commands saved in a file is usually called a shell script, but make no mistake: these are actually small programs. The shell scripts are run by using sh (stands for Shell) or bash (Bourne again Shell).
	&ensp;`$ bash script.sh`
