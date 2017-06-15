filename = raw_input('Enter file to parse: ')
filehandle = open("D:\Dropbox\Study material\Python\python for informatics code\%s" %filename)

daycount = dict()

for line in filehandle:
    if not line.startswith("From "): continue
    line = line.split()
    daycount[line[2]] = daycount.get(line[2], 0) + 1

print daycount
