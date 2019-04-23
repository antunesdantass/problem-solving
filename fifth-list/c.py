# Pocket Book 

mod = 1000000007

def mul(a, b):
    return ((a % mod) * (b % mod)) % mod

n, i = map(int, raw_input().split())
words = [raw_input() for x in range(n)]
column = []
for i in range(i):
    columnI = []
    for j in range(n):
        columnI.append(words[j][i])
    column.append(columnI)

result = 1
for i in range(len(column)):
    result = mul(result, len(set(column[i])))

print result