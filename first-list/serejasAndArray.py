arraySize, op = map(int, raw_input().split())
array = map(int, raw_input().split())
ops = []
for operator in range(op):
	operation = raw_input()
	if len(ops) > 0:
		if ops[-1].split()[0] == operation.split()[0] == "2":
			ops[-1] = "2 %i" % (int(ops[-1].split()[1]) + int(operation.split()[1]))
		else:
			ops.append(operation)
	else:
		ops.append(operation)

def actions(action, array):
	action = action.split()
	if int(action[0]) == 1:
		array[int(action[1]) - 1] = int(action[2])
	elif int(action[0]) == 2:
		array = map(lambda x: x + int(action[1]), array)
	else:
		print array[int(action[1]) - 1]
	return array

for operation in ops:
	array = actions(operation, array)
