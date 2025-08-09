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


# ––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
def countElements(arr):
    hash_set = set(arr)       # Convert array to set for O(1) lookups
    count = 0                 # Initialize counter for elements with x+1
    for x in arr:             # Iterate over each element in array
        if x + 1 in hash_set: # Check if x+1 exists in set
            count += 1        # Increment counter if x+1 found
    return count              # Return total count of valid elements


# ––––––––––––––––––––––––––––––––––––––––––––––––
# Task: Count elements x in an array such that x + 1 is also in the array, counting duplicates separately.
# Example: arr = [1, 2, 3] → Output = 2 (1 and 2 are counted because 2 and 3 are in the array)
# Why: Practices hash set usage for efficient lookup to check for x + 1.

def countElements(arr):  # Example: arr = [1, 2, 3]

    # 1️⃣ Create a hash set from the array
    # Convert arr to a set for O(1) lookup
    # Why? We need to quickly check if x + 1 exists in the array
    hash_set = set(arr)  # hash_set = {1, 2, 3}

    # 2️⃣ Initialize counter
    # Initialize count to track elements x where x + 1 is in the array
    # Why? We need to count each valid x, including duplicates
    count = 0  # count = 0

    # 3️⃣ Iterate through the array
    # Check each element to see if x + 1 exists in the hash set
    # Why? We need to count each x where x + 1 is present
    for x in arr:  # x takes values [1, 2, 3]
        # --- Iteration 1: x = 1 ---
        # Check if x + 1 is in the hash set
        # Why? If x + 1 exists, x is a valid element to count
        if x + 1 in hash_set:  # x = 1, x + 1 = 2, hash_set = {1, 2, 3}, 2 in hash_set is True
            count += 1  # count = 0 + 1 = 1
        # After Iteration 1: count = 1

        # --- Iteration 2: x = 2 ---
        if x == 2:
            if x + 1 in hash_set:  # x = 2, x + 1 = 3, hash_set = {1, 2, 3}, 3 in hash_set is True
                count += 1  # count = 1 + 1 = 2
            # After Iteration 2: count = 2

        # --- Iteration 3: x = 3 ---
        if x == 3:
            if x + 1 in hash_set:  # x = 3, x + 1 = 4, hash_set = {1, 2, 3}, 4 not in hash_set, False
                count += 1  # skip
            # After Iteration 3: count = 2

    # 4️⃣ Return the count
    # Why? count contains the number of elements x where x + 1 is in the array
    return count  # count = 2


arr = [1, 2, 3]
print(countElements(arr))  # Output: 2






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




