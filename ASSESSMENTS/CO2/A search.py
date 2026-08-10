import heapq

# Weighted graph
graph = {
    'S': [('A', 2), ('B', 4)],
    'A': [('C', 3)],
    'B': [('C', 2)],
    'C': [('G', 2)],
    'G': []
}

# Heuristic values
h = {
    'S': 6,
    'A': 5,
    'B': 4,
    'C': 2,
    'G': 0
}

def a_star(start, goal):

    # (f, g, node)
    open_list = []

    heapq.heappush(
        open_list,
        (h[start], 0, start)
    )

    g_cost = {start: 0}
    parent = {start: None}

    closed = set()

    while open_list:

        f, g, current = heapq.heappop(open_list)

        if current in closed:
            continue

        closed.add(current)

        print(
            "Expanded:", current,
            "g =", g,
            "h =", h[current],
            "f =", f
        )

        if current == goal:
            break

        for neighbor, cost in graph[current]:

            new_g = g + cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:

                g_cost[neighbor] = new_g
                parent[neighbor] = current

                new_f = new_g + h[neighbor]

                heapq.heappush(
                    open_list,
                    (new_f, new_g, neighbor)
                )

    # Construct path
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent.get(current)

    path.reverse()

    return path, g_cost[goal]


start = 'S'
goal = 'G'

path, cost = a_star(start, goal)

print("\nOptimal Path:", " -> ".join(path))
print("Total Cost:", cost)
