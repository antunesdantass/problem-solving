from math import sqrt, ceil

maxPrime = 10**5

crivo = [True] * (maxPrime + 1)
crivo[0], crivo[1] = False, False
primos = []

for i in range(2, maxPrime + 1):
    if crivo[i]:
        for j in range(2 * i, maxPrime + 1, i):
            crivo[j] = False
        primos.append(i)

def isPrime(n):
    global primos
    if n == 2:
        return True
    elif n % 2 == 0 or n < 2:
        return False
    else:
        for primo in primos:
            if n % primo == 0 or primo > n:
                return False
    
    return True

ninputs = int(raw_input())
inputs = [map(int, raw_input().split()) for x in range(ninputs)]

answers = []
for query in inputs:
    n = query[0]
    m = query[1]
    primes = []
    for i in range(n, m + 1):
        if isPrime(i):
            primes.append(i)
    answers.append(primes)
        

for answer in answers:
    print "\n".join(map(str, answer))
    print