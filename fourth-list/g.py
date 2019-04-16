## Soldier and Number Game

def factorial(x, y):
    total = x
    x -= 1
    while x > y:
        total *= x
        x -= 1
    
    return x

def factorator(x, primes):
    

maxPrime = 10**6

isPrime = [True] * (maxPrime + 1)
isPrime[0], isPrime[1] = False, False

for i in range(2, maxPrime + 1):
    if isPrime[i]:
        for j in range(2 * i, maxPrime + 1, i):
            isPrime[j] = False

nOfEntries = int(raw_input())
entries = [map(int, raw_input().split()) for x in range(nOfEntries)]