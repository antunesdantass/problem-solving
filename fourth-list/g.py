## Soldier and Number Game

maxPrime = 10**6

isPrime = [True] * (maxPrime + 1)
isPrime[0], isPrime[1] = False, False
primes = []

for i in range(2, maxPrime + 1):
    if isPrime[i]:
        for j in range(2 * i, maxPrime + 1, i):
            isPrime[j] = False
        primes.append(i)

def factorial(x, y):
    if x == y:
        return 0
    total = x
    x -= 1
    while x > y:
        total *= x
        x -= 1
    return total

def primeFactors(x):
    global primes
    factors = []
    index = 0
    PF = primes[index]
    while (x > 1 and PF * PF <= x):
        while (x % PF == 0):
            x /= PF
            factors.append(PF)
        index += 1
        PF = primes[index] if index < len(primes) -1 else PF + 1
    if x > 1:
        factors.append(x)
    return factors

nOfEntries = int(raw_input())
entries = [map(int, raw_input().split()) for x in range(nOfEntries)]
answers = map(lambda x: str(len(primeFactors(factorial(x[0], x[1])))), entries)
print "\n".join(answers)