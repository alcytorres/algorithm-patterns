# Time Complexity Examples

# Time complexity: as the input size grows, how much longer does the algorithm take to complete?

# Space complexity: as the input size grows, how much more memory does the algorithm use?


# O(n) - Linear time: Single loop printing array elements
def fn(arr):
    for num in arr:
        print(num)

nums = [1, 2, 3]
fn(nums)
# Output: 
# 1
# 2
# 3


# O(n) - Linear time: Nested loop with constant inner iterations
def fn(arr):
    for num in arr:
        for _ in range(500000):   # _ is a placeholder for unused loop variable; same as using 'i'
            print(num)

nums = [1, 2]
fn(nums)
# Output: 
# 1 (printed 500,000 times)
# 2 (printed 500,000 times)


# O(n^2) - Quadratic time: Nested loops iterating over array
def fn(arr):
    for num1 in arr:
        for num2 in arr:
            print(num1 * num2)

nums = [2, 3]
fn(nums)
# Output:
# 4
# 6
# 6
# 9


# O(n + m) - Linear time: Multiple sequential loops over two arrays
def fn(arr1, arr2):
    for num in arr1:
        print(num)
    for num in arr1:
        print(num)
    for num in arr2:
        print(num)

nums1, nums2 = [1, 2], [3]
fn(nums1, nums2)
# Output:
# 1
# 2
# 1
# 2
# 3


# O(n^2) - Quadratic time: Triangular nested loops summing pairs
def fn(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            print(arr[i] + arr[j])

nums = [1, 2]
fn(nums)
# Output:
# 2
# 3
# 4



# ––––––––––––––––––––––––––––––––––––––––––––––––
# Space Complexity Examples

# Space complexity: as the input size grows, how much more memory does the algorithm use?


# O(1) - Constant space: Only uses a single variable
def fn(arr):
    for num in arr:
        print(num)

nums = [1, 2, 3]
fn(nums)
# Output:
# 1
# 2
# 3
# None


# O(n) - Linear space: Stores doubled values in new array
def fn(arr):
    doubled_nums = []
    for num in arr:
        doubled_nums.append(num * 2)
    return doubled_nums

nums = [1, 2, 3]
print(fn(nums))
# Output:
# [2, 4, 6]


# O(n) - Linear space: Stores 1% of array
def fn(arr):
    nums = []
    one_hundredth = len(arr) // 100

    for i in range(one_hundredth):
        nums.append(arr[i])
    return nums

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 10  # 100 elements
print(fn(nums))
# Output:
# [1]


# O(n * m) - Quadratic space: Creates a grid of size n * m
def fn(arr, arr2):
    n, m = len(arr), len(arr2)
    grid = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            grid[i][j] = arr[i] * arr2[j]
    return grid

nums1, nums2 = [2, 3], [4]
print(fn(nums1, nums2))
# Output:
# [[8], [12]]


