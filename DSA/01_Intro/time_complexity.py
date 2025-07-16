# Time Complexity Examples

# Time complexity: as the input size grows, how much longer does the algorithm take to complete?

# Space complexity: as the input size grows, how much more memory does the algorithm use?


# O(n) - Linear time: Single loop printing array elements
def print_array(arr):
    for num in arr:
        print(num)

# O(n) - Linear time: Nested loop with constant inner iterations
def print_array_constant(arr):
    for num in arr:
        for _ in range(500000):
            print(num)

print(print_array_constant([1, 2, 3]))

# O(n^2) - Quadratic time: Nested loops iterating over array
def print_product(arr):
    for num1 in arr:
        for num2 in arr:
            print(num1 * num2)

# O(n + m) - Linear time: Multiple sequential loops over two arrays
def print_arrays(arr, arr2):
    for num in arr:
        print(num)
    for num in arr:
        print(num)
    for num in arr2:
        print(num)

# O(n^2) - Quadratic time: Triangular nested loops summing pairs
def print_sums(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            print(arr[i] + arr[j])


# Space Complexity Examples

# O(1) - Constant space: Only uses a single variable
def print_array_space(arr):
    for num in arr:
        print(num)

# O(n) - Linear space: Stores doubled values in new array
def double_array(arr):
    doubled_nums = []
    for num in arr:
        doubled_nums.append(num * 2)
    return doubled_nums

# O(n) - Linear space: Stores 1% of array
def store_one_hundredth(arr):
    nums = []
    one_hundredth = len(arr) // 100
    for i in range(one_hundredth):
        nums.append(arr[i])
    return nums

# O(n * m) - Quadratic space: Creates a grid of size n * m
def create_grid(arr, arr2):
    n, m = len(arr), len(arr2)
    grid = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            grid[i][j] = arr[i] * arr2[j]
    return grid




