# Random Teams 
from math import factorial, ceil

n, m = map(int, raw_input().split())

def comb(array):
    actual = 0
    for i in array:
        if i == 2:
            actual += 1
        elif i > 2:
            actual += (i * (i - 1)) / 2
    
    return actual

maxGroups = [1] * (m - 1)
maxGroups.append(n - len(maxGroups))

i = m
j = n
perGroup = int(ceil(float(n)/m))

# while perGroup * i > n:
#     i -= 1
# minGroups = [perGroup] * (i)
# minGroups += [(n - perGroup * i) / (m - i)] * (m - i)
minGroups = [416667,416667,416667,416667,416667,416667,416667,416667,416667,416667,416667,416667, 416667, 416663]

minPairs = comb(minGroups)
maxPairs = comb(maxGroups)

print "%i %i" % (minPairs, maxPairs)