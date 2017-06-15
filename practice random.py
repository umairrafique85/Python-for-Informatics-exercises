import urllib
filehand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

for line in filehand:
    print line.strip()

    
