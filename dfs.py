def dfs(graph, node, visited=None):
    if visited is None:
        visited = []
    
    visited.append(node)
    
    for n in graph[node]:
        if n not in visited:
            dfs(graph, n, visited)
            
    return visited

example_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(dfs(example_graph, 'A'))