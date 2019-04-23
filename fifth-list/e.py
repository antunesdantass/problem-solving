# Lucky Numbers
from math import factorial

n = int(raw_input())
total = 0
for i in range(1, n + 1):
    luckyMax = 1
    for j in range(i):
        luckyMax *= factorial(2)
    total += luckyMax

print total