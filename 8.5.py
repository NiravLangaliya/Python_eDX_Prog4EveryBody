"""
8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the
person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
"""
import re
fname = input("Enter file name: ")
#fname = "/Users/nlangaliya/Documents/GitHub/Python_eDX_Prog4EveryBody/mbox-short.txt"
fh = open(fname)
counter=0
for line in fh:
    if re.match("^From:",line.rstrip()):
        continue
    elif re.match("^From",line.rstrip()):
        words = re.split(' ',line.rstrip())
        counter=counter+1
        print (words[1])
#print ("There were {0} lines in the file with From as the first word").format(counter)
print("There were", counter, "lines in the file with From as the first word")
fh.close()