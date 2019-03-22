sizeFirst, sizeSecond = map(int, raw_input().split())
first = raw_input().split();
second = raw_input().split();

def procuraMenor(array):
	menor = int(array[0])
	for i in array:
		if int(i) < menor:
			menor = int(i)
	return menor

intersect = set(first).intersection(set(second))
	
menor1 = procuraMenor(first)
menor2 = procuraMenor(second)

if len(intersect) > 0:
	print procuraMenor(list(intersect))
else:
	print "%i%i" % (min(menor1, menor2), max(menor1, menor2))
