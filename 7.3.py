filename = raw_input('Enter a file name: ')
try:
    filehand = open("D:\Dropbox\Study material\Python\python for informatics code\%s" % filename)
except:
    if filename == 'na na boo boo':
        print "%s TO YOU = You have been punk'd!" % filename.upper()
        exit()
    print 'File cannot be opened: %s' %filename
    exit()
count = 0
for line in filehand:
    if line.startswith('Subject: '):
        count = count + 1
print 'There were %d subject lines in %s' % (count, filename)
    
