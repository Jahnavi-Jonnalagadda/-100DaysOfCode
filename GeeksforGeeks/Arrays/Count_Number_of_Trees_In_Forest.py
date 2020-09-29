def add_edge(u, v):
    vertices[u].append(v)
    vertices[v].append(u)

def find_connected_comps(vertices, n):
    visited = [False]*n
    final_tree_list = []
    for v in range(n):
        if(visited[v] == False):
            tree_list = []
            get_connected_comps(vertices, v, visited, tree_list)
            final_tree_list.append(tree_list)
    print(final_tree_list)
    return len(final_tree_list)

def get_connected_comps(vertices, src, visited, tree_list):
    visited[src] = True
    tree_list.append(src)
    for edge in vertices[src]:
        if(visited[edge] == False):
            get_connected_comps(vertices, edge, visited, tree_list)

n = 7
nodes = [[0, 1], [2, 3], [4, 5], [5, 6], [4, 6]]
vertices = {}
for i in range(n):
    vertices[i] = []
for item in nodes:
    add_edge(item[0], item[1])


print(find_connected_comps(vertices, n))
                


