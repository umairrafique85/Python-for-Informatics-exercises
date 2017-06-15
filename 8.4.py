romeofilehandle = open("D:/Dropbox/Study material/Python/python for informatics code/romeo.txt")
masterlist = []
for line in romeofilehandle:
    linelist = line.split()
    for word in linelist:
        if word in masterlist:
            continue
        masterlist.append(word)
masterlist.sort()
print masterlist
