

# ----------------------------------------------------------------------------------
# 1. Compute Prefix Sum Array
"""
Task: Given an array, create a new array of its prefix sums.
Example: [1, 2, 3] → [1, 3, 6]
Why: Direct practice for Running Sum of 1d Array.
"""

def prefix_sum(arr):
    if not arr:
        return []
    result = [arr[0]]  # First element is the same
    for i in range(1, len(arr)):
        result.append(result[-1] + arr[i])  # Add current element to previous sum
    return result

# Test the function
# print(prefix_sum([1, 2, 3]))  # Output: [1, 3, 6)]  →  [1, 1+2=3, 1+2+3=6)]
# ----------------------------------------------------------------------------------


# Solution with output 
def range_sum(prefix, start, end):  # range_sum([1, 3, 6)], 0, 1)
    if start == 0:  # True 
        return prefix[end]  # prefix[1] = 3  
    return prefix[end] - prefix[start - 1]  # skip 

# Test the function
prefix = prefix_sum([1, 2, 3])  # → [1, 3, 6)] 
print(range_sum(prefix, 0, 1))  # Output: 3 (1 + 2) 

# ----------------------------------------------------------------------------------
# Solution with output 
def range_sum(prefix, start, end):  # range_sum([1, 3, 6)], 1, 2)
    if start == 0:  
        return prefix[end]  
    return prefix[end] - prefix[start - 1]

# Test the function
prefix = prefix_sum([1, 2, 3])  # → [1, 3, 6)] 
print (range_sum(prefix, 1, 2)) # Output: 5 (6 - 1)
# ----------------------------------------------------------------------------------
