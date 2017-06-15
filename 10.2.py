while True:
    filename = raw_input('Enter file name: ')
    if filename == 'done': break
    try:
        filehandle = open("D:\Dropbox\Study material\Python\python for informatics code\%s" % filename)
    except:
        print 'Unable to open file %s' %filename
        continue

    #handle = open("D:\Dropbox\Study material\Python\python for informatics code\mbox-short.txt")
    hourcount = dict()
    for line in filehandle:
        if not line.startswith("From "): continue
        line = line.split()
        hour = line[5].split(":")[0]
        hourcount[hour] = hourcount.get(hour, 0) + 1

    output = sorted([(key, count) for key, count in hourcount.items()])
    for item, val in output:
        print item, val
    break
