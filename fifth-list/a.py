# A - Fast Exponentiation

mod = 1000000007

def mul(a, b):
    return ((a % mod) * (b % mod)) % mod

def fastExpo(m, e):
    if e == 0:
        return 1
    elif e == 1:
        return m % mod
    elif e % 2 == 1:
        return mul(m, fastExpo(m, e - 1))
    else:
        expo = fastExpo(m, e / 2)
        return mul(expo, expo)

nOfTests = int(raw_input())
testCases = [map(int, raw_input().split()) for x in range(nOfTests)]
results = map(lambda x: str(int(fastExpo(x[0], x[1]))), testCases)
print "\n".join(results)