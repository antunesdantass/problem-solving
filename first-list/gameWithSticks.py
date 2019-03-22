player1 = "Akshat"
player2 = "Malvika"

lines, columns = map(int, raw_input().split())
sticks = lines + columns

currentPlayer = player1

while lines > 0 and columns > 0:
	lines = lines - 1
	columns = columns - 1
	currentPlayer = player1 if currentPlayer == player2 else player2
	
print player1 if currentPlayer == player2 else player2
