filename = raw_input('Enter a file name: ')
filehandle = open("D:\Dropbox\Study material\Python\python for informatics code\%s" %filename)
fromcounter = 0
for line in filehandle:
    if not line.startswith('From '): continue
    linelist = line.split()
    print linelist[1]
    fromcounter = fromcounter + 1
print 'There were %d lines in the file with From as the first word' %fromcounter
