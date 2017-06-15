def count_character(wordtoparse, tolookfor):
	counter = 0
	for char in wordtoparse:
		if char == tolookfor:
			counter = counter + 1
	print "The letter", tolookfor, "appears in", wordtoparse, counter, "times"
