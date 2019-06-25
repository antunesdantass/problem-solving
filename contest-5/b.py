n = int(raw_input())
bits = [int(x) for x in raw_input()]
zeros = bits.count(0)
ones = n - zeros
print n - min(zeros, ones) * 2