def countback(wordtopars):
	cursor = 1
	while cursor < len(wordtopars)+1:
		print wordtopars[-cursor]
		cursor = cursor + 1
		
