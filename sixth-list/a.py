EH_BURACO = '@'
vis = set()

def dfs(adj, no):
    vis.add(no)
    for vizinho in adj[no]:
        if vizinho not in vis:
            dfs(adj, vizinho)

def countComponents(graph):
    global vis
    sets = []
    for no in graph:
        dfs(graph, no)
        contains = False
        for i in sets:
            if i == vis:
                contains = True
                break
        if not contains:
            sets.append(vis)
        vis = set()
    return len(sets)
        

def buildGraph(data):
    adj = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == EH_BURACO:
                index = str(i) + str(j)
                if index not in adj:
                    adj[index] = []
                if i > 0:
                    if data[i - 1][j] == EH_BURACO:
                        adj[index].append(str(i - 1) + str(j))
                    if j > 0:
                        if data[i - 1][j - 1] == EH_BURACO:
                            adj[index].append(str(i - 1) + str(j - 1))
                    if j < len(data[i - 1]) - 1:
                        if data[i - 1][j + 1] == EH_BURACO:
                            adj[index].append(str(i - 1) + str(j + 1))
                if i < len(data) - 1:
                    if data[i + 1][j] == EH_BURACO:
                        adj[index].append(str(i + 1) + str(j))
                    if j < len(data[i + 1]) - 1:
                        if data[i + 1][j + 1] == EH_BURACO:
                            adj[index].append(str(i + 1) + str(j + 1))
                    if j > 0:
                        if data[i + 1][j - 1] == EH_BURACO:
                            adj[index].append(str(i + 1) + str(j - 1))
                if j > 0:
                    if data[i][j - 1] == EH_BURACO:
                        adj[index].append(str(i) + str(j - 1))
                if j < len(data[i]) - 1:
                    if data[i][j + 1] == EH_BURACO:
                        adj[index].append(str(i) + str(j + 1))

    return adj


m, n = list(map(int, input().split()))
resultados = []
while m != 0:
    data = []
    for i in range(m):
        data.append(list(map(lambda x: x, input())))
    resultados.append(countComponents(buildGraph(data)))
    data = []
    
    m, n = list(map(int, input().split()))
    
for resultado in resultados:
    print(resultado)