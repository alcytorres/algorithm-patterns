# Minimum Subarray Sum of Size K
"""
Task: Given an integer array nums and an integer k, find the minimum sum of any contiguous subarray of size k. If the array has fewer than k elements, return None.
Example 1: [1, 2, 3],    k = 2 → 3
Example 1: [1, 4, 3, 8], k = 2 → 5
Example 3: [6, 4, 3],    k = 2 → 7
"""

def min_sum_sliding_window(arr, k):

    # Input Validation 
    if len(arr) < k:
        return None
    
    # Initialize the first window
    window_sum = sum(arr[:k])

    # Compute initial result for first window   
    min_sum = window_sum 
    
    # Slide the window across the array
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]  
        min_sum = min(min_sum, window_sum)
    
    return min_sum

print(min_sum_sliding_window([1, 2, 3], 2))     # Output: 3 → 1+2 = 3
print(min_sum_sliding_window([1, 4, 3, 8], 2))  # Output: 5 → 1+4 = 5

# print(min_sum_sliding_window([6, 4, 3], 2))     # Output: 7 → 3+4 = 7
# print(min_sum_sliding_window([3, 4, 6], 2))     # Output: 7 → 3+4 = 7
# print(min_sum_sliding_window([1, 2], 2))        # Output: 3 → 1+2 = 3


# ----------------------------------------------------------------------------------
# Solution Breakdown: Minimum Subarray Sum of Size K

def min_sum_sliding_window(arr, k):    # Example: arr = [1, 2, 3], k = 2
    # Check if the array is too short to have a subarray of size k
    if len(arr) < k:                   # len(arr) = 3, k = 2, so 3 >= 2, skip this
        # Return None since no subarrays of size k are possible
        return None                    # skip
    
    # Add up the first k numbers as our starting group (window)
    # Why? This is the first possible sum we can check
    window_sum = sum(arr[:k])          # arr[:2] = [1, 2], sum = 1 + 2 = 3
    
    # Set the minimum sum to our first window's sum
    # Why? It's the smallest sum we know so far (we just started!)
    min_sum = window_sum               # min_sum = 3 (first window [1, 2])
    
    # Slide the window across the array, one step at a time
    # Why? To check every possible group of k numbers
    for i in range(k, len(arr)):       # k = 2, len(arr) = 3, so i goes from 2 to 2
                                       # Iteration 1: i = 2
        # Update the sum: add the new number, subtract the old one
        # Why? This slides our window over by one spot efficiently
        window_sum += arr[i] - arr[i-k]  # arr[2] = 3, arr[2-2] = arr[0] = 1
                                         # window_sum = 3 + 3 - 1 = 5 (new window [2, 3])
        
        # Update the minimum if our new sum is smaller
        # Why? We want the smallest sum we find across all windows
        min_sum = min(min_sum, window_sum)  # min(3, 5) = 3, so min_sum = 3
    
    # Give back the smallest sum we found
    return min_sum                     # min_sum = 3 (from window [1, 2])


print(min_sum_sliding_window([1, 2, 3], 2))  # Output: 3 ([1, 2] has sum = 1 + 2 = 3)


# ----------------------------------------------------------------------------------
# Solution Output: 

def min_sum_sliding_window(arr, k):    # arr = [1, 4, 3, 8], k = 2

    # Input Validation 
    if len(arr) < k:                   # len(arr) = 4, k = 2, so 4 >= 2, skip this
        return None                    # skip
    
    # Initialize the first window
    window_sum = sum(arr[:k])          # arr[:2] = [1, 4], sum = 1 + 4 = 5

    # Compute initial result for first window   
    min_sum = window_sum               # min_sum = 5 (first window [1, 4])
    
    # Slide the window across the array
    for i in range(k, len(arr)):       # k = 2, len(arr) = 4, so i goes from 2 to 3
                                       # Iteration 1: i = 2
        window_sum += arr[i] - arr[i-k]  # arr[2] = 3, arr[2-2] = arr[0] = 1
                                         # window_sum = 5 + 3 - 1 = 7 (new window [4, 3])
        min_sum = min(min_sum, window_sum)  # min(5, 7) = 5, so min_sum = 5
                                       # Iteration 2: i = 3
        window_sum += arr[i] - arr[i-k]  # arr[3] = 8, arr[3-2] = arr[1] = 4
                                         # window_sum = 7 + 8 - 4 = 11 (new window [3, 8])
        min_sum = min(min_sum, window_sum)  # min(5, 11) = 5, so min_sum = 5
    
    return min_sum                     # min_sum = 5 (from window [1, 4])


print(min_sum_sliding_window([1, 4, 3, 8], 2))  # Output: 5 ([1, 4] has sum = 1 + 4 = 5)

