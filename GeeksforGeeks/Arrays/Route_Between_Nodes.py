# Approach - 1: Breadth-First Search
def checkForPath(G, src, dst):
    q, visited = [], []
    q.append(src)
    visited.append(src)
    while(len(q) > 0):
        u = q.pop(0)
        if(u == dst):
            return True
        for v in G[u]:
            if v not in visited:
                visited.append(v)
                q.append(v)
    return False

# Approach - 2: Depth-First Search
def checkForPath(G, src, dst, visited):
    if(src in visited):
        return False
    visited.append(src)
    if(src == dst):
        return True
    for u in G[src]:
        if(checkForPath(G, u, dst, visited)):
            return True
    return False

'''
Sample Input:
G = {
     "A": ["B", "C"],
     "B": ["D", "E"],
     "C": ["F"],
     "D": [],
     "E": ["F"],
     "F": []
     }
BFS - print(checkForPath(G, "A", "K"))
DFS - print(checkForPath(G, "A", "K", []))'''
     
