# Bear and Poker 

nOfPlayers = int(raw_input())
bids = map(int, raw_input().split())

def minimo(x):
    while x % 2 == 0 or x % 3 == 0:
        if x % 2 == 0:
            x /= 2
        else:
            x /= 3
    return x

bids = map(minimo, bids)
print "Yes" if len(set(bids)) == 1 else "No"