import heapq

# Graph
graph = {
    'S': ['A', 'B'],
    'A': ['C'],
    'B': ['C'],
    'C': ['G'],
    'G': []
}

# Heuristic values
h = {
    'S': 7,
    'A': 6,
    'B': 4,
    'C': 2,
    'G': 0
}

def greedy_best_first_search(start, goal):
    open_list = []
    heapq.heappush(open_list, (h[start], start))

    parent = {start: None}
    visited = set()

    while open_list:
        _, current = heapq.heappop(open_list)

        if current in visited:
            continue

        visited.add(current)

        print("Expanded:", current, "h =", h[current])

        if current == goal:
            break

        for neighbor in graph[current]:
            if neighbor not in visited:
                parent[neighbor] = current
                heapq.heappush(
                    open_list,
                    (h[neighbor], neighbor)
                )

    # Construct path
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent.get(current)

    path.reverse()

    return path


start = 'S'
goal = 'G'

path = greedy_best_first_search(start, goal)

print("\nFinal Path:", " -> ".join(path))
