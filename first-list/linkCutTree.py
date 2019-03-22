import math

l, r, k = map(int, raw_input().split())

i = l if l <= 1 else int(math.log(l, k))
j = r if r <= 1 else int(math.ceil(math.log(r, k)))

values = filter(lambda x: int(x) >= l and int(x) <= r, map(lambda exp: str(int(math.pow(k, exp))), range(i, j + 2)))

print "-1" if values == [] else " ".join(values)
