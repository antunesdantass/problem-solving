hours =  int(raw_input())
schedule = raw_input().split()

consecutiveHours = 0
actual = 0
nTimesRun = 0
i = 0
while i < hours and nTimesRun < 2:
	if schedule[i] == "1":
		actual += 1
	elif schedule[i] == "0":
		consecutiveHours = actual if actual > consecutiveHours else consecutiveHours
		actual = 0
	if i == (hours - 1):
		if schedule[i] == "1":
			nTimesRun += 1
			i = 0
		else:
			break
	else:
		i += 1

print consecutiveHours
	
