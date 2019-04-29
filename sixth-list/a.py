EH_BURACO = '@'
vis = set()

def dfs(adj, no):
    vis.add(no)
    for vizinho in adj[no]:
        if vizinho not in vis:
            dfs(adj, vizinho)

def countComponents(graph):
    global vis
    counter = 0
    for no in graph:
        if no not in vis:
            counter += 1
            dfs(graph, no)
    return counter
        

def buildGraph(data):
    adj = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == EH_BURACO:
                index = (i, j)
                if index not in adj:
                    adj[index] = []
                if i > 0:
                    if data[i - 1][j] == EH_BURACO:
                        adj[index].append((i - 1, j))
                    if j > 0:
                        if data[i - 1][j - 1] == EH_BURACO:
                            adj[index].append((i - 1, j - 1))
                    if j < len(data[i - 1]) - 1:
                        if data[i - 1][j + 1] == EH_BURACO:
                            adj[index].append((i - 1, j + 1))
                if i < len(data) - 1:
                    if data[i + 1][j] == EH_BURACO:
                        adj[index].append((i + 1, j))
                    if j < len(data[i + 1]) - 1:
                        if data[i + 1][j + 1] == EH_BURACO:
                            adj[index].append((i + 1, j + 1))
                    if j > 0:
                        if data[i + 1][j - 1] == EH_BURACO:
                            adj[index].append((i + 1, j - 1))
                if j > 0:
                    if data[i][j - 1] == EH_BURACO:
                        adj[index].append((i, j - 1))
                if j < len(data[i]) - 1:
                    if data[i][j + 1] == EH_BURACO:
                        adj[index].append((i, j + 1))

    return adj


m, n = list(map(int, input().split()))
resultados = []
while m != 0:
    data = []
    for i in range(m):
        data.append(list(map(lambda x: x, input())))
    resultados.append(countComponents(buildGraph(data)))
    data = []
    vis = set()
    
    m, n = list(map(int, input().split()))
    
for resultado in resultados:
    print(resultado)