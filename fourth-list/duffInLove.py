maxPrime = 10**6

isPrime = [True] * (maxPrime + 1)
isPrime[0], isPrime[1] = False, False

for i in range(2, maxPrime + 1):
    if isPrime[i]:
        for j in range(2 * i, maxPrime + 1, i):
            isPrime[j] = False

