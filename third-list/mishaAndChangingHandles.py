n = int(raw_input())
users = {}
for i in range(n):
    old, new = raw_input().split()
    if old not in users:
        users[new] = old
    else:
        original = users[old]
        del users[old]
        users[new] = original

print len(users)
for user in users:
    print "%s %s" % (users[user], user)