x = int(raw_input())
y = int(raw_input())
median = (x + y) / 2
print sum(range(1, abs(median - x) + 1)) + sum(range(1, abs(median - y) + 1))