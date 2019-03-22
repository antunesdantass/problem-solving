n = int(raw_input())
entries = map(int, raw_input().split())
print " ".join(map(lambda x: str(x), sorted(entries)))
