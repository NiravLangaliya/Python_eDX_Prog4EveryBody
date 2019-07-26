import re
#fname="/Users/nlangaliya/Documents/GitHub/Python_eDX_Prog4EveryBody/regex_sum_42.txt"
fname="/Users/nlangaliya/Documents/GitHub/Python_eDX_Prog4EveryBody/regex_sum_267294.txt"
fh = open(fname)
line_list=list()
for line in fh:
    line = line.rstrip()
    if re.search("[0-9]+",line):
        line_list.append(sum([int(x) for x in re.findall("[0-9]+",line)]))
print(sum(line_list))
fh.close()