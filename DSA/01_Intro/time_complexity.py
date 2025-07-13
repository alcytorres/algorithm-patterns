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
























# a = [1, 2]
# a.extend([3, 4])  # Adds 3 and 4 individually
# print(a)  # Output: [1, 2, 3, 4]

# a.extend((5, 6))  # Works with tuples too
# print(a)  # Output: [1, 2, 3, 4, 5, 6]

# a = [1, 2]
# a.append([3, 4])  # Adds [3, 4] as a single item
# print(a)  # Output: [1, 2, [3, 4]]

# fruits = ["apple", "banana"]
# more_fruits = ["orange", "grape"]
# fruits.extend(more_fruits)
# print(fruits)  # Output: ["apple", "banana", "orange", "grape"]


# fruits = ["apple", "banana"]
# more_fruits = ["orange", "grape"]
# fruits.append(more_fruits)
# print(fruits)  # Output: ['apple', 'banana', ['orange', 'grape']]


# range(start, stop)
# What it does: Generates a sequence of numbers from 'start' to 'stop-1'.
# Why use it: Creating loops or sequences for iteration (common in algorithms).
# Syntax:
# range(start, stop)  # Returns a range object; 'start' is inclusive, 'stop' is exclusive
# Example:
# print(list(range(1, 4)))  # Output: [1, 2, 3]








# SET METHODS
# .add()
# What it does: Adds a single element to a set if it’s not already present.
# Why use it: Building a collection of unique items efficiently.
# Syntax:
# set.add(element)  # Modifies the set in place, adding 'element'
# Example:
unique = {1, 2}
unique.add(5)
print(unique)  # Output: {1, 2, 3}


# set()
# What it does: Creates a set from an iterable or an empty set, storing unique elements.
# Why use it: Removing duplicates or performing set operations (e.g., union, intersection).
# Syntax:
# set(iterable)  # Returns a new set; 'iterable' is optional
# Example:
nums = [1, 2, 2, 2, 3, 3]
print(set(nums))  # Output: {1, 2, 3}







