# ----------------------------------------------------------------------------------
# 1. Compute Prefix Sum Array  → Reference this solution [1, 3, 6, 10)] for Maximum Subarray Sum of Size K
"""
Task: Given an array, create a new array of its prefix sums.
Example: [1, 2, 3] → [1, 3, 6]
Why: Direct practice for Running Sum of 1d Array.
"""

def prefix_sum(arr):   # Define the function that takes an array 'arr' as input
    if not arr:         # Check if the array is empty
        return []       # Return an empty array if input is empty
    result = [arr[0]]   # Start the result with the first element of 'arr'
    for i in range(1, len(arr)):  # Loop from the second element to the end
        result.append(result[-1] + arr[i])  # Add the previous sum to the current element
    return result       # Return the prefix sum array

# Test the function
# print(prefix_sum([1, 2, 3]))  # Output: [1, 3, 6)]  →  [1, 1+2=3, 1+2+3=6)]
# print(prefix_sum([1, 2, 3, 4]))  # Output: [1, 3, 6, 10)]  →  [1, 1+2=3, 1+2+3=6 1+3+6=10)]



# 4. Maximum Subarray Sum of Size K
"""
Task: Find the maximum sum of any subarray of size k.

Find the largest sum of k consecutive numbers in the array.******

Example: [1, 2, 3, 4], k=2 → 7 (3 + 4)
Why: Bridges to more complex subarray problems.
"""

# Solution
def max_subarray_sum(arr, k):  # Define the function that takes an array 'arr' and integer 'k'
    """
    Finds the maximum sum of any subarray of size k.
    
    - Uses prefix sums to compute subarray sums efficiently.
    - Time Complexity: O(n), Space Complexity: O(n) for prefix array.
    - Prefix sum approach is simpler than sliding window for beginners here.
    """
    if len(arr) < k:      # If array is shorter than 'k'
        return None       # Cannot form a subarray of size 'k'
    prefix = prefix_sum(arr)      # prefix = [1, 3, 6, 10)] 
    max_sum = prefix[k - 1]       # max_sum = 3
    for i in range(k, len(arr)):  # for i in range(2, 4), i = 2  |  i = 3
        current_sum = prefix[i] - prefix[i - k]  # current_sum = 3-1=2  |  10-3=7
        max_sum = max(max_sum, current_sum)      #  max_sum = 3  |  7
    return max_sum                               # 7

# Test the function
print(max_subarray_sum([100, 20, 30, 40], 2))  # Output: 7 (3 + 4)