import math

def minimax(depth, nodeIndex, maximizingPlayer, values, maxDepth):
    if depth == maxDepth:
        return values[nodeIndex]

    if maximizingPlayer:
        return max(
            minimax(depth + 1, nodeIndex * 2, False, values, maxDepth),
            minimax(depth + 1, nodeIndex * 2 + 1, False, values, maxDepth)
        )
    else:
        return min(
            minimax(depth + 1, nodeIndex * 2, True, values, maxDepth),
            minimax(depth + 1, nodeIndex * 2 + 1, True, values, maxDepth)
        )

values = [3, 5, 2, 9, 12, 5, 23, 23]
treeDepth = int(math.log2(len(values)))

result = minimax(0, 0, True, values, treeDepth)

print("Optimal Value:", result)
