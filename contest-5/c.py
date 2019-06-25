distances = sorted(map(int, raw_input().split()))
total = distances[1] - distances[0] + distances[2] - distances[1]
print total