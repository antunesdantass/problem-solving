n = int(raw_input())
schedule = sorted([map(int, raw_input().split()) for x in range(n)], key=lambda x: x[0])

def scheduler(schedule):
    tv1, tv2 = [], []
    for tvshow in schedule:
        if len(tv1) == 0:
            tv1.append(tvshow)
        elif tvshow[0] > tv1[-1][1]:
            tv1.append(tvshow)
        elif len(tv2) == 0:
            tv2.append(tvshow)
        elif tvshow[0] > tv2[-1][1]:
            tv2.append(tvshow)
        else:
            return "NO"
    
    return "YES"

print scheduler(schedule)