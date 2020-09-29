def journeyToMoon(n, astronaut):
    G = buildGraph(n, astronaut)
    visited = [False]*n
    connectedComps = findConnectedComps(G, n, 0, visited)
    pairs = 0
    prod = 1
    for i in range(len(connectedComps)):
        for j in range(i+1, len(connectedComps)):
            prod = len(connectedComps[i]) * len(connectedComps[j])
            pairs += prod
    return pairs

def buildGraph(n, arr):
    G = {}
    for i in range(n):
        G[i] = []
    for item in arr:
        add_edge(G, item[0], item[1])
    return G

def add_edge(G, u, v):
    G[u].append(v)
    G[v].append(u)

def findConnectedComps(G, n, src, visited):
    connectedComps = []
    for v in range(n):
        if(visited[v] == False):
            comps = []
            getConnectedComps(G, v, visited, comps)
            connectedComps.append(comps)
    print(connectedComps)
    return connectedComps

def getConnectedComps(G, src, visited, comps):
    visited[src] = True
    comps.append(src)
    print(comps)
    for edge in G[src]:
        if(visited[edge] == False):
            getConnectedComps(G, edge, visited, comps)

n = int(input())
astronaut = list(map(int, input().split()))
print(journeyToMoon(n, astronaut))
