number = int(raw_input()) 

for i in range(9, 0, -1):
	if (number % i) == 0 and (number != i or number == 1):
		print number / i
		print " ".join(map(lambda x: str(i), range(number / i)))
		break
