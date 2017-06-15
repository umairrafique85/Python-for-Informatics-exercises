inp = None
accumulator = 0
counter = 0
while inp != "done":
    inp = raw_input("Enter a number: ")
    try:
        danumber = int(inp)
    except:
        print "Invalid input"
        continue
    counter = counter+1
    accumulator = accumulator + danumber
print accumulator, counter, float(accumulator)/counter
