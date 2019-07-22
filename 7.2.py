"""
7.2 Write a program that prompts for a file name,
then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines
and compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
when you are testing below enter mbox-short.txt as the file name.
"""
# Use the file name mbox-short.txt as the file name
import re
fname = input("Enter file name: ")
#fname = "/Users/nlangaliya/Documents/GitHub/Python_eDX_Prog4EveryBody/mbox-short.txt"
fh = open(fname)
decimal_value_list=[]
total_decimal_value = 0.0
i = 0
for line in fh:
    if  re.match("^X-DSPAM-Confidence:",line) :
        decimal_value = re.findall("\d*\.\d+",line.rstrip())
        decimal_value_list = decimal_value_list + decimal_value
        i=i+1

decimal_value_list=map(float,decimal_value_list)


for decimal_v in decimal_value_list:
    total_decimal_value = total_decimal_value + float(decimal_v)

total_avg = round(total_decimal_value/len(decimal_value_list),12)
print("Average spam confidence:", total_avg)
