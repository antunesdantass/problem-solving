EH_BURACO = '@'

def dfs(no):
    vis[no] = True
    for vizinho in adj[no]:
        if not vis[vizinho]:
            dfs(vizinho)

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
                if i < len(data - 1):
                    if data[i + 1][j] == EH_BURACO:
                        adj[index].append(str(i + 1) + str(j))
                    if j < len(data[i + 1] - 1):
                        if []
                if j > 0:
                    if data[i][j - 1] == EH_BURACO:
                        adj[index].append(str(i) + str(j - 1))
                if j < len(data[i] - 1):
                    if data[i][j + 1] == EH_BURACO:
                        adj[index].append(str(i) + str(j + 1))


m, n = map(int, raw_input().split())
while m != 0:
    data = []
    for i in range(m):
        data.append(map(lambda x: x, raw_input()))
    
    m, n = map(int, raw_input().split())
    
print data