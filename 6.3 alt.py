def count_character(wordtoparse, tolookfor):
	counter = 0
	for char in wordtoparse:
		if char == tolookfor:
			counter = counter + 1
	print "The letter %s appears in %s %d times" % (tolookfor, wordtoparse, counter)
