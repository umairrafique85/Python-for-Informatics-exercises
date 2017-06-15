filename = raw_input('Enter a file name: ')
try:
    filehand = open("D:\Dropbox\Study material\Python\Python for informatics code\%s" %filename)
except:
    print "cannot open file %s" %filename
    exit()
for line in filehand:
    line = line.upper()
    print line
    
