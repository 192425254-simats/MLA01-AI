def sum_n(n):
    if n == 1:         
        return 1
    else:              
        return n + sum_n(n - 1)

# Input
n = int(input("Enter a number: "))

# Function call
result = sum_n(n)

# Output
print("Sum of first", n, "natural numbers is:", result)
