import re
inp = raw_input('Enter a regular expression: ')
filepath = "D:\Dropbox\Study material\Python\python for informatics code\mbox.txt"
handle = open(filepath)
finallist = list()
for line in handle:
    x = re.findall(inp, line)
    if len(x) > 0:
        finallist.append(x)
print "mbox.txt had %d lines that matched %s" %(len(finallist), inp)

    
