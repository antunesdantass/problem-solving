n, m = map(int, raw_input().split())

magics = 0
while n < m:
	if m % 2 == 0 and (m / 2) % n == 0:
		m = m / 2
		magics += 1
	elif m % 3 == 0 and (m / 3) % n == 0:
		magics += 1
		m = m / 3
	else:
		magic = -1
		break
print magics if n == m else "-1"
