# Maximum Subarray Sum of Size K

"""
Task: Given an integer array nums and an integer k, find the maximum sum of any contiguous subarray of size k.
Example 1: [1, 2, 3, 4], k=2 → 7 ([3, 4])
Example 2: [5, 1, 2], k=2 → 6 ([5, 1])
"""

# Fixed-size sliding window
def max_sum_sliding_window(arr, k):

    # Input Validation 
    if len(arr) < k:
        return None

    # Initialize
    window_sum = 0
    
    # Set up the initial window
    for i in range(k):     
        window_sum += arr[i]
    
    max_result = window_sum  # Initialize result  
    
    # Slide the window across the array
    for i in range(k, len(arr)):  # i = 2
        window_sum += arr[i] - arr[i - k]  # Add new element, remove old element   
        max_result = max(max_result, window_sum)  # Update max_result              
    
    return max_result

print(max_sum_sliding_window([1, 2, 3, 4], 2))  # Output: 7 ([3, 4])
print(max_sum_sliding_window([5, 1, 2], 2))     # Output: 6 ([5, 1])

