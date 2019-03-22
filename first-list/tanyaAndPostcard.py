tanyas = raw_input()
journals = raw_input()

def createIndex(char):
	data = {}
	for letter in char:
		if letter not in data:
			data[letter] = 1
		else:
			data[letter] = data[letter] + 1
	
	return data

setJ = createIndex(journals)
setT = createIndex(tanyas)

yay = 0
wow = 0

def opposite(char):
	return char.upper() if char.lower() == char else char.lower()
	
for char in setT:
	if char in setJ and setT[char] > 0:
		if setJ[char] >= setT[char]:
			yay = yay + setT[char]
			setJ[char] = setJ[char] - setT[char]
			setT[char] = 0
		else:
			yay = yay + setJ[char]
			setT[char] = setT[char] - setJ[char]
			setJ[char] = 0
			
for char in setT:
	ochar = opposite(char)
	if ochar in setJ and setT[char] > 0:
		if setJ[ochar] >= setT[char]:
			wow = wow + setT[char]
			setJ[ochar] = setJ[ochar] - setT[char]
			setT[char] = 0
		else:
			wow = wow + setJ[char]

print "%i %i" % (yay, wow)
