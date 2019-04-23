maxPrime = 10**3

isPrime = [True] * (maxPrime + 1)
isPrime[0], isPrime[1] = False, False

for i in range(2, maxPrime + 1):
    if isPrime[i]:
        for j in range(2 * i, maxPrime + 1, i):
            isPrime[j] = False

n = int(raw_input())
primes = []
for i in range(n + 1):
    if isPrime[i]:
        primes.append(i)
multiples = []
for prime in primes:
    i = 2
    while prime ** i <= n:
        multiples.append(prime ** i)
        i += 1
answer = primes + multiples
print len(answer)
print " ".join(map(str, answer))