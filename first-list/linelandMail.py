nOfCities = int(raw_input())
locations = map(int, raw_input().split())

for i in range(nOfCities):
	nearest = 0	
	if i == 0:
		nearest = locations[1]
	elif i == (nOfCities - 1):
		nearest = locations[-2]
	else:
		distanceLeft = abs(locations[i] - locations[i-1])
		distanceRight = abs(locations[i] - locations[i+1])
		nearest = locations[i-1] if distanceLeft < distanceRight else locations[i+1]
	
	furtherLeft = abs(locations[i] - locations[0])
	furtherRight = abs(locations[i] - locations[-1])
	
	furthest = locations[0] if furtherLeft > furtherRight else locations[-1]
	
	print "%i %i" % (abs(locations[i] - nearest), abs(locations[i] - furthest))
