numberlist = []
inputnumber = None
while inputnumber != 'done':
    inputnumber = raw_input('Enter a number: ')
    try:
        numberint = int(inputnumber)
    except:
        print "Invalid input"
        continue
    numberlist.append(numberint)
print 'Maximum: ', max(numberlist)
print 'Minimum: ', min(numberlist)
