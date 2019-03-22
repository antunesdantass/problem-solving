def step(distance, options, currentSteps):
	while distance >= options[0]:
		distance = distance - options[0]
		currentSteps = currentSteps + 1
	if distance == 0:
		return currentSteps
	else:
		return step(distance, options[1:], currentSteps)

possible_steps = [5, 4, 3, 2, 1]
distance = int(raw_input())
print step(distance, possible_steps, 0)
