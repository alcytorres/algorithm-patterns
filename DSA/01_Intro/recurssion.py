# Iterative: Print 1 to 10
def print_iterative():
    for i in range(1, 11):
        print(i)

# Recursive: Print 1 to 10 with base case
def print_recursive(i):           # Define function taking parameter i (starting number)
    if i > 10:                    # Base case: if i exceeds 10, stop recursion
        return None               # Exit the function, return None (no value)
    print(i)                      # Print current value of i
    print_recursive(i + 1)        # Recursive call with i incremented by 1

# Recursive: Print 1 to 3 with end-of-call messages
def print_recursive_with_end(i):
    if i > 3:
        return
    print(i)
    print_recursive_with_end(i + 1)
    print(f"End of call where i = {i}")
    return

# Recursive: Fibonacci number (0-indexed)
def fibonacci(n):
    if n <= 1:
        return n
    one_back = fibonacci(n - 1)
    two_back = fibonacci(n - 2)
    return one_back + two_back