"""
9.4
Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times
they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum
loop to find the most prolific committer.
"""
import re
fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"
fh = open(fname)
words_list=dict()
for line in fh:
    if re.match("^From ",line.rstrip()):
        if  words_list.has_key(re.split(' ',line.rstrip())[1]):
            words_list[re.split(' ', line.rstrip())[1]] = words_list[re.split(' ', line.rstrip())[1]] + 1
        else:
            words_list[re.split(' ', line.rstrip())[1]]=int(1)
maximum_number=0
for key,value in words_list.items():
    if maximum_number < value:
        maximum_number = value
        profile_committer=key
print(profile_committer,maximum_number)
fh.close()
