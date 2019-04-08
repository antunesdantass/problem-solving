totalNumbers = int(raw_input())
stripe = map(int, raw_input().split())
stripeSum = sum(stripe)

waysi, waysj = 0, 0
i, j = 0, totalNumbers - 1
sumi, sumj = 0, 0

while i < totalNumbers - 1 and j > 0 and stripeSum % 2 == 0:
    sumi += stripe[i]
    sumj += stripe[j]
    if sumi == stripeSum / 2:
        waysi += 1
    if sumj == stripeSum / 2:
        waysj += 1
    i += 1
    j -= 1

print max(waysi, waysj)