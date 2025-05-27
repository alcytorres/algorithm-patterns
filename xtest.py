# 4. Maximum Subarray Sum of Size K   → Reference problem 1. Compute Prefix Sum Array 

# ----------------------------------------------------------------------------------
# *** Reference: 1. Compute Prefix Sum Array ***
"""
Task: Given an array, create a new array of its prefix sums.
Example: [1, 2, 3] → [1, 3, 6]
"""
def prefix_sum(arr):
    # 1️⃣ Handle empty array case
    if not arr:
        return []
    
    # 2️⃣ Initialize result with the first element
    result = [arr[0]]  

    # 3️⃣ Compute prefix sums for remaining elements
    for i in range(1, len(arr)):
        result.append(result[-1] + arr[i])  # Add current element to previous sum

    # 4️⃣ Return the prefix sum array
    return result

# print(prefix_sum([1, 2, 3]))  # Output: [1, 3, 6]  →  [1, 1+2, 1+2+3]
# ----------------------------------------------------------------------------------

# 4. Maximum Subarray Sum of Size K
"""
Task: Find the largest sum of consecutive numbers (any subarray) in the array of size k. If array is shorter than 'k' return none
      i.e. "Find the maximum sum of any continous subarray of size k."
      
Example 1: [1, 2, 3],     k=2 → 5 (2 + 3)
Example 2: [1, 2, 3, 4],  k=2 → 7 (3 + 4)
Example 3: [1, 4, 6, 1],  k=2 → 10 (4 + 6)
Example 4: [7, 1, 8, 3],  k=3 → 16 (7 + 1 + 8)

Why: Bridges to more complex subarray problems.
"""

def max_subarray_sum(arr, k):

    # 1️⃣ Check if array length is sufficient
    if len(arr) < k:
        return None
    
    # 2️⃣ Compute prefix sums
    prefix = prefix_sum(arr) # [1, 5, 11, 12]

    # 3️⃣ Initialize maximum sum with first window
    max_sum = prefix[k - 1]  # 5

    # 4️⃣ Iterate through remaining window
    for i in range(k, len(arr)):   # why start at k?
        current_sum = prefix[i] - prefix[i - k]   # 11-1 = 10  12-5=7 
        max_sum = max(current_sum, max_sum)       # 10

    # 5️⃣ Return the maximum sum
    return max_sum



print(max_subarray_sum([1, 4, 6, 1], 2))  # Output: 10 (largest sum of 2 consecutive numbers)


print(max_subarray_sum([1, 2, 3], 2))     # Output: 5 (2 + 3)
print(max_subarray_sum([1, 2, 3, 4], 2))  # Output: 7 (3 + 4)
print(max_subarray_sum([4, 6, 1], 2))     # Output: 10 (4 + 6)
print(max_subarray_sum([1, 6, 7, 3], 3))  # Output: 16 (6 + 7 + 3)
