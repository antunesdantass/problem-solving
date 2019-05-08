# Itinerary of Santa Claus
import random

def find(parent, i):
    if parent[i] == i:
        return i
    else:
        return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    side = random.random() > 0.5
    if side:
        parent[xroot] = yroot
    else:
        parent[yroot] = xroot

n, m = raw_input().split()
while n != 0 and m != 0:
    