# ----------------------------------------------------------------------------------
# 1. Compute Prefix Sum Array
"""
Task: Given an array, create a new array of its prefix sums. Return an empty array if input is empty
Example: [1, 2, 3] → [1, 3, 6]
Why: Direct practice for Running Sum of 1d Array.
"""

def prefix_sum(arr):
    if not arr:
        return []
    result = [arr[0]]
    for i in range(1, len(arr)):
        result.append(result[-1] + arr[i])
    return result


# Test the function
print(prefix_sum([1, 2, 3, 4]))  # Output: [1, 3, 6]  →  [1, 1+2, 1+2+3]
# print(prefix_sum([]))  # Output: []  



# ----------------------------------------------------------------------------------
# 4. Maximum Subarray Sum of Size K
"""
Task: Find the largest sum of consecutive numbers (for any subarray) in the array of size k.
      i.e. Find the maximum sum of any subarray of size k.
Example 1: [1, 2, 3, 4], k=2 → 7 (3 + 4)
Example 2: [7, 1, 8, 3], k=3 → 16 (7 + 1 + 8)
Why: Bridges to more complex subarray problems.
"""

def max_subarray_sum(arr, k):
    if len(arr) < 2:
        return None
    prefix = prefix_sum(arr)   # prefix = [1, 3, 6]
    max_sum = prefix[k - 1]    # max_sum = 3 
    for i in range(k, len(arr)):
        current_sum = prefix[i] - prefix[i - k]
        max_sum = max(max_sum, current_sum)
    return max_sum

# Test the function
print(max_subarray_sum([1, 2, 3], 2))  # Output: 5 (2 + 3, largest sum of 2 consecutive numbers)
print(max_subarray_sum([1, 2, 3, 4], 2))  # Output: 7 (3 + 4)
print(max_subarray_sum([7, 1, 8, 3], 3))  # Output: 16



# def max_subarray_sum(arr, k):
#     if len(arr) < 2:
#         return None
#     prefix = prefix_sum(arr)   # prefix = [1, 3, 6]
#     max_sum = prefix[k - 1]
#     for i in range(k, len(arr)):
#         current_sum = prefix[i] - prefix[i - k]
#         max_sum = max(max_sum, current_sum)
#     return max_sum
        

# Test the function
print(max_subarray_sum([1, 2, 3], 2))  # Output: 5 (2 + 3, largest sum of 2 consecutive numbers)
print(max_subarray_sum([1, 2, 3, 4], 2))  # Output: 7 (3 + 4)
print(max_subarray_sum([7, 1, 8, 3], 3))  # Output: 16
