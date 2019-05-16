import sys

def minDistance(distance, sptSet):
    min = sys.maxint
    min_index = (0, 0)
    for v in distance:
        if distance[v] < min and v not in sptSet:
            min = distance[v]
            min_index = v
    return min_index

def shortest_path(graph, origin):
    dist = {}
    for vertex in graph:
        dist[vertex] = sys.maxint
    dist[origin] = 0
    sptSet = set()
    for vertex in graph:
        u = minDistance(dist, sptSet)
        sptSet.add(u)
        for a in graph[vertex]:
            if a not in sptSet and dist[a] > dist[u]:
                dist[a] = dist[u]
    return dist
 
def buildGraph(data):
    EH_PAREDE = "#"
    adj = {}
    iH = (0, 0)
    iE = (0, 0)
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != EH_PAREDE:
                index = (i, j)
                if index not in adj:
                    adj[index] = []
                if i > 0:
                    if data[i - 1][j] != EH_PAREDE:
                        adj[index].append((i - 1, j))
                if i < len(data) - 1:
                    if data[i + 1][j] != EH_PAREDE:
                        adj[index].append((i + 1, j))
                if j > 0:
                    if data[i][j - 1] != EH_PAREDE:
                        adj[index].append((i, j - 1))
                if j < len(data[i]) - 1:
                    if data[i][j + 1] != EH_PAREDE:
                        adj[index].append((i, j + 1))
                if data[i][j] == "H":
                    iH = (i, j)
                elif data[i][j] == "E":
                    iE = (i, j)

    return (adj, iH, iE)

i, j = map(int, raw_input().split())
matrix = []
for line in range(i):
    column = []
    for char in raw_input():
        column.append(char)
    matrix.append(column)
adj, iH, iE = buildGraph(matrix)
print shortest_path(adj, iH)