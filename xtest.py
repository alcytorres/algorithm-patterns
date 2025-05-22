# 2. Range Sum Query  → Reference problem 1. Compute Prefix Sum Array 

# ----------------------------------------------------------------------------------
# *** Reference: 1. Compute Prefix Sum Array ***
"""
Task: Given an array, create a new array of its prefix sums.
Example: [1, 2, 3, 4] → [1, 3, 6, 10]
"""
def prefix_sum(arr):
    if not arr:
        return []
    
    result = [arr[0]]  

    for i in range(1, len(arr)):
        result.append(result[-1] + arr[i]) 

    return result

print(prefix_sum([1, 2, 3, 4]))  # Output: [1, 3, 6, 10]  →  [1, 1+2, 1+2+3, 1+2+3+4]
# ----------------------------------------------------------------------------------

# 2. Range Sum Query 
"""
Task: Find the sum of elements between two indices (inclusive) using prefix sums.

Example 1: [1, 2, 3, 4], indices 1 to 3 → 9 (2 + 3 + 5)
Example 2: [1, 2, 3, 4], indices 0 to 2 → 6 (1 + 2 + 3)

Why: Teaches efficient range sum calculation.
"""
def range_sum(prefix, start, end):

    # 1️⃣ Handle case where range starts at index 0
    if start == 0: 
        return prefix[end]
    
    # 2️⃣ Compute range sum for non-zero start index
    return prefix[end] - prefix[start - 1]


prefix = prefix_sum([1, 2, 3, 4])    # [1, 3, 6. 10]

print(range_sum(prefix, 1, 3))  # Output: 9 

# prefix[3] - prefix[1]
# 10 - 3
# 7

# prefix[3] - prefix[1] - 1
# 10 - 1
# 9