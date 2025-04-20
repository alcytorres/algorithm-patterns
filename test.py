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
        result.append(result[-1]+ arr[i])
    return result

# print(prefix_sum([1, 2, 3]))     # Output: [1, 3, 6]  → [1, 1+2, 1+2+3]
# print(prefix_sum([1, 2, 3, 4]))  # Output: [1, 3, 6, 10]  → [1, 1+2, 1+2+3 + 1+2+3+4]
# print(prefix_sum([]))            # Output: []  


# ----------------------------------------------------------------------------------
# 4. Maximum Subarray Sum of Size K
"""
Task: Find the largest sum of consecutive numbers (any subarray) in the array of size k. If array is shorter than 'k' return none
      i.e. Find the maximum sum of any subarray of size k.
Example 1: [1, 2, 3], k=2 → 5 (2 + 3)
Example 2: [7, 1, 8, 3], k=3 → 16 (7 + 1 + 8)
Why: Bridges to more complex subarray problems.
"""

def max_subarray_sum(arr, k):
    if len(arr) < k:
        return None
    prefix = prefix_sum(arr)  #[1, 10, 11]
    max_sum = prefix[k - 1]  # 10
    for i in range(2, len(arr)):  # i = 2
        current_sum = prefix[i] - prefix[k - i]  # prefix[2] - prefix[2-2] = 11-4=7
        max_sum = max(max_sum, current_sum) # max_sum = 10
    return max_sum

print(max_subarray_sum([1, 2, 3], 2))  # Output: 5 (2 + 3, largest sum of 2 consecutive numbers)
print(max_subarray_sum([4, 6, 1], 2))  # Output: 10 (4 + 6, largest sum of 2 consecutive numbers)
print(max_subarray_sum([7, 1, 8, 3], 3))  # Output: 16  (7 + 1 + 8)
