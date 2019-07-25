"""
9.4
Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times
they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum
loop to find the most prolific committer.
"""
import re
#fname = input("Enter file name: ")
fname = "/Users/nlangaliya/Documents/GitHub/Python_eDX_Prog4EveryBody/mbox-short.txt"
fh = open(fname)
words_list={}
for line in fh:
    if re.match("^From",line.rstrip()):
        if words_list[re.split(' ',line.rstrip())[1]]
            words_list[re.split(' ',line.rstrip())[1]]=re.split(' ',line.rstrip())[1]+1
        else:
            words_list[re.split(' ',line.rstrip())[1]]

for k,v in word_list():
    print (k,v)
fh.close()
