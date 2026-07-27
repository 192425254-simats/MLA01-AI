from queue import PriorityQueue

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 2,
    'E': 1,
    'F': 1,
    'G': 0
}

def greedy(start, goal):
    pq = PriorityQueue()
    pq.put((heuristic[start], start))
    visited = set()

    while not pq.empty():
        h, node = pq.get()
        if node in visited:
            continue
        print(node, end=" ")
        visited.add(node)

        if node == goal:
            break

        for i in graph[node]:
            if i not in visited:
                pq.put((heuristic[i], i))

greedy('A', 'G')
