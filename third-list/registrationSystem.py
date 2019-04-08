n = int(raw_input())
requests = [raw_input() for x in range(n)]
newNames = []
database = {}

for username in requests:
    if username not in database:
        database[username] = 0
        newNames.append("OK")
    else:
        database[username] = database[username] + 1
        newNames.append(username + str(database[username]))

for name in newNames:
    print name