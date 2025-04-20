# 2. Range Sum Query  → Reference problem 1. Compute Prefix Sum Array 

# ----------------------------------------------------------------------------------
# *** Reference: 1. Compute Prefix Sum Array ***
"""
Task: Given an array, create a new array of its prefix sums.
Example: [1, 2, 3] → [1, 3, 6]
"""
def prefix_sum(arr):
    if not arr:
        return []
    result = [arr[0]]  # First element is the same
    for i in range(1, len(arr)):
        result.append(result[-1] + arr[i])  # Add current element to previous sum
    return result

print(prefix_sum([1, 2, 3]))  # Output: [1, 3, 6]  →  [1, 1+2, 1+2+3]
# ----------------------------------------------------------------------------------

# 2. Range Sum Query 
"""
Task: Find the sum of elements between two indices (inclusive) using prefix sums.
Example: [1, 2, 3], indices 0 to 1 → 3 (1 + 2)
Why: Teaches efficient range sum calculation.
"""
def range_sum(prefix, start, end):
    if start == 0:
        return prefix[end]  # Sum from start of array
    return prefix[end] - prefix[start - 1]  # Difference gives range sum

prefix = prefix_sum([1, 2, 3])
print(range_sum(prefix, 0, 1))  # Output: 3 
print(range_sum(prefix, 1, 2)) # Output: 5 

# Solution
def range_sum(prefix, start, end):   # Define the function that takes a prefix sum array and two indices
    """
    Computes the sum of elements between start and end indices using prefix sums.
    
    - Uses subtraction of prefix sums for efficiency.
    - Time Complexity: O(1) per query, Space Complexity: O(1).
    - Direct calculation is simple and showcases prefix sum utility.
    """
    if start == 0:      # If starting from the beginning
        return prefix[end]  # Directly return the prefix sum at 'end'
    return prefix[end] - prefix[start - 1]  # Subtract prefix sum before 'start' from prefix sum at 'end'

# Test the function
prefix = prefix_sum([1, 2, 3])
print(range_sum(prefix, 0, 1))  # Output: 3  (1+2=3)
print(range_sum(prefix, 1, 2)) # Output: 5  (2+3=5)


"""
Explanation for range_sum(prefix, 2, 2): 
The line return prefix[end] - prefix[start - 1] works because it isolates the sum of numbers from index start to end in the original array.
    - prefix[end] is the total of all numbers up to end (e.g., for end = 2, prefix[2] = 1 + 2 + 3 = 6).
    - prefix[start - 1] is the total up to just before start (e.g., start = 2, start - 1 = 1, prefix[1] = 1 + 2 = 3).
    - Subtracting them (6 - 3 = 3) gives only the numbers from start to end (just 3 here).
It is like taking a big pile of coins up to end and removing the coins before start to get what is in between.

*** Pro Tip: Actually use coins to test this problem to visually understand it ***
"""

# ----------------------------------------------------------------------------------
# Solution with output 
def range_sum(prefix, start, end):  # range_sum([1, 3, 6], 0, 1)
    if start == 0:  # True (start = 0)
        return prefix[end]  # prefix[1] = 3
    return prefix[end] - prefix[start - 1]  # skip

prefix = prefix_sum([1, 2, 3])  # → [1, 3, 6]
print(range_sum(prefix, 0, 1))  # Output: 3  

# ----------------------------------------------------------------------------------
# Solution with output 
def range_sum(prefix, start, end):  # range_sum([1, 3, 6], 1, 2)
    if start == 0:  # False (start = 1)
        return prefix[end]  # skip
    return prefix[end] - prefix[start - 1]  # prefix[2] - prefix[0] = 6 - 1 = 5

prefix = prefix_sum([1, 2, 3])  # → [1, 3, 6]
print(range_sum(prefix, 1, 2))  # Output: 5 

# ----------------------------------------------------------------------------------
# Solution with output 
def range_sum(prefix, start, end):
    if start == 0:  # False (start = 2)
        return prefix[end]  # skip
    return prefix[end] - prefix[start - 1]  # prefix[2] - prefix[1] = 6 - 3 = 3

prefix = prefix_sum([1, 2, 3])  # → [1, 3, 6]
print(range_sum(prefix, 2, 2))  # Output: 3

# ----------------------------------------------------------------------------------
# Solution with output 
def range_sum(prefix, start, end):
    if start == 0:  # False (start = 1)
        return prefix[end]  # skip
    return prefix[end] - prefix[start - 1]  # prefix[3] - prefix[1] = 10 - 1 = 9

prefix = prefix_sum([1, 2, 3, 4])  # → [1, 3, 6, 10]
print(range_sum(prefix, 1, 3))  # Output: 9

# ----------------------------------------------------------------------------------
# Solution with output 
def range_sum(prefix, start, end):
    if start == 0:  # False (start = 2)
        return prefix[end]  # skip
    return prefix[end] - prefix[start - 1]  # prefix[3] - prefix[1] = 10 - 3 = 7

prefix = prefix_sum([1, 2, 3, 4])  # → [1, 3, 6]
print(range_sum(prefix, 2, 3))  # Output: 7