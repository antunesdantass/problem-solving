adj = {}
vis = set()
v, e = map(int, raw_input().split())


def isCycle(node, visited, recStack):
    visited.add(node)
    recStack.add(node)
    for neighbour in adj[node]:
        if neighbour not in visited:
            if isCycle(neighbour, visited, recStack):
                return True
        elif neighbour in recStack:
            return True
    
    recStack.remove(node)
    return False

def hasCycle():
    visited = set()
    recStack = set()
    for node in adj:
        if node not in visited:
            if isCycle(node, visited, recStack):
                return True
    
    return False

def dfs(node):
    vis.add(node)
    for vizinho in adj[node]:
        if vizinho not in vis:
            dfs(vizinho)

def countComponents(graph):
    global vis
    counter = 0
    for no in graph:
        if no not in vis:
            counter += 1
            dfs(no)
    return counter
            
for i in range(e):
    o, d = map(int, raw_input().split())
    if o not in adj:
        adj[o] = []
    adj[o].append(d)
    if d not in adj:
        adj[d] = []

print "YES" if countComponents(adj) == 1 and not hasCycle() else "NO"