while True:
    filename = raw_input('Enter file name: ')
    if filename == 'done': break
    try:
        filehandle = open("D:\Dropbox\Study material\Python\python for informatics code\%s" % filename)
    except:
        print 'Unable to open file %s' %filename
        continue

    domaincounter = dict()

    for line in filehandle:
        if not line.startswith("From "): continue
        line = line.split()
        addressindex = line[1].find("@") + 1
        address = line[1][addressindex:]
        domaincounter[address] = domaincounter.get(address, 0) + 1

    print domaincounter 

        
