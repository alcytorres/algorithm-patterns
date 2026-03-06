# Time Complexity Examples
"""
Time complexity: as the input size grows, how much longer does the algorithm take to complete?

Space complexity: as the input size grows, how much more memory does the algorithm use?
"""

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




# ––––––––––––––––––––––––––––––––––––––––––––––––
"""

Time Complexity (best → worst)
------------------------------
O(1)      | Constant      | Array index access, hash lookup
O(log n)  | Logarithmic   | Binary search, balanced BST lookup
O(n)      | Linear        | Single scan, counting, hashing
O(n log n)| Linearithmic  | Merge sort, quicksort (avg), divide & conquer
O(n^2)    | Quadratic     | Nested loops, pair comparisons
O(n^3)    | Cubic         | Triple nested loops, triplet checks
O(2^n)    | Exponential   | Subset generation, naive recursion
O(n!)     | Factorial     | Permutations of n elements

Space Complexity (best → worst)
-------------------------------
O(1)      | Constant      | Few variables, in-place operations
O(log n)  | Logarithmic   | Recursion depth (binary search, mergesort)
O(n)      | Linear        | Arrays, hash maps, recursion depth
O(n^2)    | Quadratic     | 2D grids, adjacency matrices
O(2^n)    | Exponential   | All subsets stored
O(n!)     | Factorial     | All permutations stored





---
📊 Time & Space Complexity Symbols Cheat Sheet

Symbol  | Meaning / When it Appears                          | Example
--------|----------------------------------------------------|----------------------------------
n       | Main input size (length of array, string, etc.)    | Traverse array of n elements → O(n)
m       | Second input size (two arrays, grid dimensions)    | Merge arrays of size n and m → O(n + m)
k       | Special size (window length, substring length)     | Sliding window of size k → O(n * k)
1       | Constant work, independent of input size           | Swap two variables → O(1)
log n   | Input is halved each step                          | Binary search on n elements → O(log n)
n², n³  | Nested loops (2 or 3 levels)                       | Double loop over n × n grid → O(n²)
n!      | Factorial growth (all permutations)                | Generate all permutations of n → O(n!)



---
"""
Q: When do I use O(N + M) vs O(N * M)?

🧠 Simple Rule:
  • Do one thing after another  →  ADD  →  O(N + M)
  • Do one thing FOR EACH of another  →  MULTIPLY  →  O(N * M)


--------------------------------------------------
O(N + M) — Separate loops (one after the other)
--------------------------------------------------
def print_both(arr1, arr2):
    for x in arr1:      # This loop → O(N)
        print(x)

    for y in arr2:      # This loop → O(M)
        print(y)

# Total work: first all of arr1, then all of arr2 → O(N + M)


--------------------------------------------------
O(N * M) — Nested loops (for each, do all)
--------------------------------------------------
def print_pairs(arr1, arr2):
    for x in arr1:          # Outer loop runs n times
        for y in arr2:      # Inner loop runs m times for EACH x
            print(x, y)

# Total work: n * m prints → O(n * m)


💡 Memory trick:
  • Loops in a line (one after another)         → add their sizes → O(N + M)
  • Loops inside loops (one wrapped in another) → multiply sizes → O(N * M)
"""




---
Q: “What's the difference between O(U) and O(N) in time/space complexity analysis?”

O(U) vs O(N)
    N = total number of elements.
    U = number of unique elements.
    Always: U ≤ N.

Worst case: if all elements are unique, then U = N → O(U) = O(N).

Best case: if there are many duplicates, U ≪ N → O(U) is tighter and more efficient.

Interview tip:
    • Saying O(N) is always safe.
    
    • Saying O(U) is more precise — just explain that in the worst case it's O(N), but in practice U may be much smaller.
    
    • Rule of thumb: use O(N) for clarity, use O(U) when you want to impress with precision.

    
"""

