# Maximum Product of K Consecutive Elements
"""
Task: Given an integer array nums and an integer k, find the maximum product of any contiguous subarray of size k. If the array has fewer than k elements, return None.
Example 1: [1, 2, 3],    k = 2 → 6 ([2, 3])
Example 1: [1, 2, 3, 4], k = 2 → 12 ([3, 4])
Example 3: [2, 3, 4, 5], k = 2 → 20 ([4, 5])
"""

def max_product_sliding_window(arr, k):

    # Input Validation 
    if len(arr) < k:
        return None
    
    # Initialize the first window
    window_product = 1

    # Compute initial result for first window    
    window = arr[:k]     # [1, 2]
    max_result = window[0] * window[1]    # max_result = 2

    # Slide the window across the array
    for i in range(k, len(arr)):  # i = 2 out of 2
        window_product =  max_result // arr[i - k] * arr[i]  # 2 / 1 * 3 = 6
        max_result = max(max_result, window_product)
    
    return max_result


print(max_product_sliding_window([1, 2, 3], 2))       # Output: 6 ([2, 3])




def max_product_sliding_window(arr, k):

    # Input Validation 
    if len(arr) < k:
        return None
    
    # Initialize
    window_product = 1

    # Set up the initial window
    for i in range(k):         # i = 0, 1
        window_product *= arr[i]   #  window_product = 1*1=1 | 1*2=2
    
    max_result = window_product    # max_result = 2

    # Slide the window across the array
    for i in range(k, len(arr)):  # i = 2
        window_product = window_product // arr[i - k] * arr[i]  # 2 / 1 * 3 = 6
        max_result = max(max_result, window_product)
    
    return max_result


print(max_product_sliding_window([1, 2, 3], 2))       # Output: 6 ([2, 3])