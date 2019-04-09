from math import sqrt, ceil

maxPrime = 10**6

isPrime = [True] * (maxPrime + 1)
isPrime[0], isPrime[1] = False, False

for i in range(2, maxPrime + 1):
    if isPrime[i]:
        for j in range(2 * i, maxPrime + 1, i):
            isPrime[j] = False


n = int(raw_input())
numbers = raw_input().split()
answer = map(lambda x: "YES" if sqrt(int(x)) - int(sqrt(int(x))) == 0.0 and isPrime[int(sqrt(int(x)))] else "NO", numbers)
print "\n".join(answer)