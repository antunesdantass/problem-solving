# F - Two Buttons

n, m = map(int, raw_input().split())
minimum = 0

if n < m:
    while n < m:
        if m % 2 == 0:
            m /= 2
        else:
            m += 1
        minimum += 1

minimum += n - m

print minimum