"""
Guide to Looping in Python for LeetCode Problems
"""

# 1. For Loop
# Best Use Case: Iterate a known number of times or over a sequence (e.g., arrays, strings).
for i in range(5):  # Example: Print 0 to 4
    print(i)

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

