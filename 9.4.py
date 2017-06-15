 
filename = raw_input('Enter file name: ')
try:
    filehandle = open("D:\Dropbox\Study material\Python\python for informatics code\%s" %filename)
except:
    print 'Unable to open file: %s' %filename
    exit()

fromcounter = dict()

for line in filehandle:
    if not line.startswith('From '): continue
    line =  line.split()
    fromcounter[line[1]] = fromcounter.get(line[1], 0) + 1

maxcount = None
maxaddress = None
for address in fromcounter:
    if maxcount is None or fromcounter[address] > maxcount:
        maxcount = fromcounter[address]
        maxaddress = address

print maxaddress, maxcount

