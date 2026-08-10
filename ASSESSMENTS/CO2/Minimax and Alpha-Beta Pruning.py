import math

# Game Tree
tree = {
    'A': [3, 5],
    'B': [6, 9],
    'C': [1, 2],
    'D': [0, 7]
}


# Minimax Function
def minimax(node, is_max):

    # Leaf node
    if isinstance(node, int):
        return node

    if is_max:
        return max(minimax(x, False) for x in tree[node])
    else:
        return min(minimax(x, True) for x in tree[node])


# Alpha-Beta Function
def alphabeta(node, alpha, beta, is_max):

    # Leaf node
    if isinstance(node, int):
        return node

    if is_max:

        value = -math.inf

        for x in tree[node]:
            value = max(
                value,
                alphabeta(x, alpha, beta, False)
            )

            alpha = max(alpha, value)

            if alpha >= beta:
                print("Pruned")
                break

        return value

    else:

        value = math.inf

        for x in tree[node]:
            value = min(
                value,
                alphabeta(x, alpha, beta, True)
            )

            beta = min(beta, value)

            if alpha >= beta:
                print("Pruned")
                break

        return value


# Main Game Tree
#              MAX
#             /   \
#           A       B
#         MIN     MIN
#        /  \     /  \
#       3    5   6    9

print("MINIMAX")

A = minimax('A', False)
B = minimax('B', False)

print("Value of A:", A)
print("Value of B:", B)

best = max(A, B)

print("Best value:", best)

if A > B:
    print("Best move: A")
else:
    print("Best move: B")


print("\nALPHA-BETA PRUNING")

A = alphabeta('A', -math.inf, math.inf, False)
B = alphabeta('B', -math.inf, math.inf, False)

best = max(A, B)

print("Value of A:", A)
print("Value of B:", B)
print("Best value:", best)

if A > B:
    print("Best move: A")
else:
    print("Best move: B")
