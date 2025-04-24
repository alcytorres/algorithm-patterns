# Minimum Subarray Sum of Size K
"""
Task: Given an integer array nums and an integer k, find the minimum sum of any contiguous subarray of size k. If the array has fewer than k elements, return None.
Example 1: nums = [1, 2, 3], k = 2 → 3
Example 2: nums = [7, 3, 2], k = 2 → 5
"""

# Fixed-size sliding window
def min_sum_sliding_window(arr, k):

    # Input Validation 
    if len(arr) < k:
        return None

    # Initialize
    window_sum = 0
    
    # Set up the initial window
    for i in range(k):
        window_sum += arr[i]
    
    min_result = window_sum  # Initialize result
    
    # Slide the window across the array
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # Add new element, remove old element
        min_result = min(min_result, window_sum)  # Update max_result
    
    return min_result

print(min_sum_sliding_window([1, 2, 3], 2))  # Output: 3 ([1, 2])
print(min_sum_sliding_window([7, 3, 2], 2))  # Output: 5 ([3, 2])

