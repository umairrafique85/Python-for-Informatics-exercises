filename = raw_input('Enter a file name: ')
try:
    filehand = open("D:\Dropbox\Study material\Python\Python for informatics code\%s" %filename)
except:
    print 'cannot open file %s' %filename
    exit()
spamcounter = 0
spamaccumulator = 0
for line in filehand:
    if not line.startswith('X-DSPAM-Confidence: '):
        continue
    spamcounter = spamcounter + 1
    valueofinterest = line[line.find(' '):]
    spamaccumulator = spamaccumulator + float(valueofinterest)
print 'Average spam confidence: ', spamaccumulator/spamcounter
    
