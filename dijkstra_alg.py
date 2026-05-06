nodes = [1, 2, 3, 4, 5]
graph = [(4, 5, 20), (5, 3, 10), (3, 2, 5), (2, 1, 2), (4, 3, 5)]

neighbor = {n: [] for n in nodes}
for i, j, x in graph:
    neighbor[i].append((j, x))

dist = {n: float('inf') for n in nodes}
dist[4] = 0
queue = [4]

while queue:
    curr = min(queue, key=lambda x: dist[x])
    queue.remove(curr)

    for neighbor_node, weight in neighbor[curr]:
        new_dist = dist[curr] + weight
        if new_dist < dist[neighbor_node]:
            dist[neighbor_node] = new_dist
            if neighbor_node not in queue:
                queue.append(neighbor_node)

print(dist)