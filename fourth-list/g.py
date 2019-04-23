## Soldier and Number Game

def primeFactors(n):
    global primes
    factors = 0
    index = 0
    PF = primes[index]
    while n > 1 and PF**2 <= n:
        while n % PF == 0:
            n /= PF
            factors += 1
        index += 1
        PF = primes[index]
    if n > 1:
        factors += 1
    
    return factors

maxPrime = (10**6) * 5

isPrime = [True] * (maxPrime + 1)
isPrime[0], isPrime[1] = False, False
primes = []

for i in range(2, maxPrime + 1):
    if isPrime[i]:
        for j in range(2 * i, maxPrime + 1, i):
            isPrime[j] = False
        primes.append(i)

nOfEntries = int(raw_input())
entries = [map(int, raw_input().split()) for x in range(nOfEntries)]
answers = []
fatores = {}
for entry in entries:
    a = entry[0]
    b = entry[1]
    total = 0
    while a > b:
        # if a not in fatores:
        #     fatores[a] = primeFactors(a)
        
        total += primeFactors(a)
        a -= 1
    answers.append(str(total))

print "\n".join(answers)