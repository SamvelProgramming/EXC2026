def prim(nodes, graph, start_node):
    mst_weight = 0
    visited = {start_node}
    edges = []
    
    while len(visited) < len(nodes):
        min_edge = None
        for i, j, w in graph:
            if i in visited and j not in visited:
                if min_edge is None or w < min_edge[2]:
                    min_edge = (i, j, w)
            elif j in visited and i not in visited:
                if min_edge is None or w < min_edge[2]:
                    min_edge = (j, i, w)
        
        if min_edge:
            i, v, w = min_edge
            visited.add(v)
            mst_weight += w
            edges.append((i, v, w))
            
    return edges, mst_weight

nodes = [1, 2, 3, 4, 5]
graph = [(4, 5, 20), (5, 3, 10), (3, 2, 5), (2, 1, 2), (4, 3, 5)]
print("Prim's MST Edges:", prim(nodes, graph, 4))