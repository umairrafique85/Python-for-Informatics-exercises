counter = 0
accumulator = 0
while True:
    inp = raw_input("Enter a number: ")
    if inp == "done":
        break
    else:
        try:
            danumber = int(inp)
        except:
            print "Invalid input"
            continue
        counter = counter + 1
        accumulator = accumulator + danumber
print accumulator, counter, float(accumulator)/counter
        
