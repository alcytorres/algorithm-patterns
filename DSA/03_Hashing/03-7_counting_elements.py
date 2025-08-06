# 1426. Counting Elements

# Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr. If there are duplicates in arr, count them separately.

# Example:
# Input: arr = [1, 2, 3]
# Output: 2
# Explanation: 1 and 2 are counted cause 2 and 3 are in arr.

# Solution: https://leetcode.com/problems/counting-elements/solutions/567376/counting-elements/


# Optimized Approach: Search with HashSet
def countElements(arr):
    hash_set = set(arr)
    count = 0
    for x in arr:
        if x + 1 in hash_set:
            count += 1
    return count

arr = [1, 2, 3]
print(countElements(arr))
# Output: 2


# Time: O(n)
# - Creating the set from arr: O(n).
# - Loop through arr once: O(n) iterations.
# - Set lookups ('x + 1 in hash_set') are O(1) on average.
# - Overall: O(n) time.

# Space: O(n)
# - Set 'hash_set' stores up to n elements: O(n) space.
# - A few variables (count, x) take O(1) space.
# - Overall: O(n) total space.


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
def countElements(arr):
    hash_set = set(arr)       # Convert array to set for O(1) lookups
    count = 0                 # Initialize counter for elements with x+1
    for x in arr:             # Iterate over each element in array
        if x + 1 in hash_set: # Check if x+1 exists in set
            count += 1        # Increment counter if x+1 found
    return count              # Return total count of valid elements



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute forece: Approach: Search with Array
def countElements(arr):
    count = 0
    for x in arr:
        if x + 1 in arr:
            count += 1
    return count

arr = [1, 2, 3]
print(countElements(arr))
# Output: 2


# Time: O(n^2)
# - Outer loop iterates over all n elements: O(n).
# - 'x + 1 in arr' is a list lookup, which takes O(n) in the worst case.
# - Overall: O(n * n) = O(n^2) time.

# Space: O(1)
# - Only a constant number of variables (count, x) are used.
# - No additional data structures.
# - Overall: O(1) space.


