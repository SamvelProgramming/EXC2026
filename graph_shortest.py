nodes = [1, 2, 3, 4, 5]
graph = [(4, 5, 20), (5, 3, 10), (3, 2, 5), (2, 1, 2), (4, 3, 5)]

in_degree = {}
for i in nodes:
    in_degree[i] = 0
for r, c, i in graph:
    in_degree[c] += 1
queue = []
for i in nodes:
    if in_degree[i] == 0:
        queue.append(i)
sort = []
while queue:
    i = queue.pop(0)
    sort.append(i)
    for r, c, j in graph:
        if r == i:
            in_degree[c] -= 1
            if in_degree[c] == 0:
                queue.append(c)
distances = {}
for i in nodes:
    distances[i] = None
distances[sort[0]] = 0
for i in sort:
    if distances[i] is not None:
        for r, c, j in graph:
            if r == i:
                if distances[c] is None or distances[i] + j < distances[c]:
                    distances[c] = distances[i] + j
path = [(i, distances[i]) for i in nodes]
print("Topological Sort:", sort)
print("Shortest Path Distances:", path)