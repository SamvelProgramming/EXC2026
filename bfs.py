def bfs(graph, start_node):
    visited = [start_node]
    queue = [start_node]
    result = []

    while queue:
        vertex = queue.pop(0)
        result.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    
    return result

example_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(bfs(example_graph, 'A'))