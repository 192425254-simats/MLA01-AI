import heapq

# Warehouse grid
# 0 = free
# 1 = obstacle

grid = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

start = (0, 0)
goal = (3, 3)

# Possible movements
moves = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1), # Left
    (0, 1)   # Right
]


def heuristic(position):
    x, y = position
    gx, gy = goal

    return abs(x - gx) + abs(y - gy)


def get_neighbors(position):

    x, y = position

    neighbors = []

    for dx, dy in moves:

        nx = x + dx
        ny = y + dy

        if (
            0 <= nx < len(grid)
            and 0 <= ny < len(grid[0])
            and grid[nx][ny] == 0
        ):
            neighbors.append((nx, ny))

    return neighbors


def find_path(start):

    queue = []

    heapq.heappush(
        queue,
        (heuristic(start), start, [start])
    )

    visited = set()

    while queue:

        _, current, path = heapq.heappop(queue)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return path

        for neighbor in get_neighbors(current):

            if neighbor not in visited:

                heapq.heappush(
                    queue,
                    (
                        heuristic(neighbor),
                        neighbor,
                        path + [neighbor]
                    )
                )

    return None


current = start

print("Robot Starting Position:", current)

while current != goal:

    path = find_path(current)

    if path is None:
        print("No path available!")
        break

    print("Current Path:", path)

    # Move one step
    if len(path) > 1:
        current = path[1]

    print("Robot moved to:", current)

    # Dynamic obstacle appears
    if current == (0, 1):

        print("\nObstacle detected!")

        grid[0][2] = 1

        print("Path blocked.")
        print("Replanning...\n")

print("\nRobot reached goal:", current)
