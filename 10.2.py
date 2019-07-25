"""
10.2
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for
each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting
the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""
import re
#fname = input("Enter file name: ")
fname = "/Users/nlangaliya/Documents/GitHub/Python_eDX_Prog4EveryBody/mbox-short.txt"
fh = open(fname)

for line in fh:
    line = line.rstrip()
    if re.match("^From ",line):
        time_str = re.findall('dd\:dd\:dd',line)
        print(time_str)
