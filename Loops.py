"""
Guide to Looping in Python for LeetCode Problems
"""

# 1. For Loop
# For loops are key for iterating over arrays, strings, or ranges in LeetCode problems.

# 1.1 Basic Patterns
# for i in range(5)
# Use Case: Iterate a fixed number of times (e.g., 5 iterations) over a seqeunce (e.g., arrays, strings).
for i in range(5):  # i = 0, 1, 2, 3, 4
    print(i)  # Output: 0 1 2 3 4

# for i in range(k, len(arr))
# Use Case: Iterate from index k to the end of an array.
arr = [10, 20, 30, 40]
k = 1
for i in range(k, len(arr)):  # i = 1, 2, 3
    print(arr[i])  # Output: 20 30 40

# for i in range(k)
# Use Case: Iterate k times, starting from 0.
k = 3
for i in range(k):  # i = 0, 1, 2
    print(i)  # Output: 0 1 2

# for key in hash:
# Use Case: Iterate over keys in a hash map (dictionary).
hash_map = {'x': 1, 'y': 2}
for key in hash_map:  # key = 'x', 'y'
    print(key, hash_map[key])  # Output: x 1, y 2

# 1.2 Two-Pointer Pattern
# for left in range(len(arr))
# Use Case: Iterate with a left pointer, paired with right for pairs or windows.
arr = [1, 2, 3]
for left in range(len(arr)):  # left = 0, 1, 2
    for right in range(left + 1, len(arr)):  # right starts after left
        print(arr[left], arr[right])  # Output: 1 2, 1 3, 2 3

# 1.3 Prefix Sum Pattern
# for i in range(1, len(arr))
# Use Case: Build a prefix sum array, starting from index 1.
arr = [1, 2, 3]
prefix = [arr[0]]  # Start with first element
for i in range(1, len(arr)):  # i = 1, 2
    prefix.append(prefix[-1] + arr[i])  # Output: [1, 3, 6]
print(prefix)

# 1.4 Sliding Window (Dynamic) Pattern
# for right in range(len(arr))
# Use Case: Expand a window with right pointer, adjust left dynamically.
arr = [1, 2, 3, 4]
target = 5
left = 0
window_sum = 0
for right in range(len(arr)):  # right = 0, 1, 2, 3
    window_sum += arr[right]
    while window_sum > target:  # Shrink window if sum exceeds target
        window_sum -= arr[left]
        left += 1
print(f"Window sum <= {target} from index {left} to {right}")

# 1.5 Sliding Window (Fixed) Pattern
# for i in range(len(arr) - k + 1)
# Use Case: Iterate over all windows of fixed size k.
arr = [1, 2, 3, 4]
k = 2
for i in range(len(arr) - k + 1):  # i = 0, 1, 2
    print(arr[i:i + k])  # Output: [1, 2], [2, 3], [3, 4]



# 2. While Loop
# Best Use Case: Iterate until a condition is met (e.g., binary search, dynamic termination).
count = 0
while count < 5:  # Example: Print 0 to 4
    print(count)
    count += 1

# 3. Nested Loops
# Best Use Case: Process multi-dimensional data (e.g., matrices, 2D arrays).
matrix = [[1, 2], [3, 4]]
for i in range(2):
    for j in range(2):  # Example: Print all elements
        print(matrix[i][j])

# 4. Looping with Index
# Best Use Case: Access both index and value (e.g., two-pointer problems).
nums = [10, 20, 30]
for idx, val in enumerate(nums):  # Example: Print index and value
    print(f"Index: {idx}, Value: {val}")

# 5. Looping Backwards
# Best Use Case: Reverse traversal (e.g., reversing arrays, palindrome checks).
arr = [1, 2, 3]
for i in range(len(arr)-1, -1, -1):  # Example: Print 3 to 1
    print(arr[i])

# 6. List Comprehensions
# Best Use Case: Concise list creation/transformations (e.g., filtering, mapping).
evens = [x for x in range(10) if x % 2 == 0]  # Example: [0, 2, 4, 6, 8]

# 7. Looping with Conditions
# Best Use Case: Skip/process elements conditionally (e.g., skip duplicates).
nums = [1, 2, 3, 4]
for num in nums:
    if num % 2 == 0:  # Example: Print only odds
        continue
    print(num)

# 8. Infinite Loops with Break
# Best Use Case: Run until a complex condition (e.g., sliding window termination).
i = 0
while True:  # Example: Print 0 to 4
    print(i)
    i += 1
    if i == 5:
        break

# 9. Looping Over Dictionaries
# Best Use Case: Handle key-value pairs (e.g., hash map problems).
d = {'a': 1, 'b': 2}
for key, value in d.items():  # Example: Print key-value pairs
    print(f"{key}: {value}")

# 10. Zipping Loops
# Best Use Case: Parallel iteration over multiple lists (e.g., comparing two arrays).
list1 = [1, 2, 3]
list2 = [4, 5, 6]
for a, b in zip(list1, list2):  # Example: Print pairs (1, 4), (2, 5), (3, 6)
    print(a, b)

