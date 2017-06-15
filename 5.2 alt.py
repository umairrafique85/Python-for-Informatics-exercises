maxinp = None
mininp = None
counter = 0
accumulator = 0
inp = None
while inp != "done":
    inp = raw_input("Enter a number: ")
    try:
        danumber = int(inp)
    except:
        print "bad input"
        continue
    if maxinp == None or maxinp < danumber:
        maxinp = danumber
    if mininp == None or mininp > danumber:
        mininp = danumber
    counter = counter+1
    accumulator = accumulator+danumber
print accumulator, counter, maxinp, mininp
