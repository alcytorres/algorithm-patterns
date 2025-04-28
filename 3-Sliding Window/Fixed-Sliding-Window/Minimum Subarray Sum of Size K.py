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
    
    # Set up the first window
    window_sum = sum(arr[:k])   
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
# Solution 1 Breakdown: 

def min_sum_sliding_window(arr, k):    # Define the function that takes an array 'arr' and integer 'k'
    
    # Input Validation 
    if len(arr) < k:                   # Check if the array is too short for a window of size k
        return None                    # Return None since no subarrays of size k are possible
    
    # Set up the first window
    window_sum = sum(arr[:k])          # Calculate the sum of the first k elements (first window)
    min_sum = window_sum               # Set the minimum sum to the first window’s sum
                                       # Why? It’s the smallest sum we’ve seen so far
    # Slide the window across the array
    for i in range(k, len(arr)):       # Loop from index k to the end of the array
        window_sum += arr[i] - arr[i-k]  # Slide the window: add the new element, subtract the old one
                                       # Why? This updates the sum for the next window efficiently
        min_sum = min(min_sum, window_sum)  # Update min_sum if the new window sum is smaller
                                       # Why? We want the smallest sum across all windows
    return min_sum                     # Return the smallest sum found


# ----------------------------------------------------------------------------------
# Solution 1 Output: 

def min_sum_sliding_window(arr, k):    # arr = [1, 4, 3, 8], k = 2

    # Input Validation 
    if len(arr) < k:                   # len(arr) = 4, k = 2, so 4 >= 2, skip this
        return None                    # skip
    
    # Set up the first window
    window_sum = sum(arr[:k])          # arr[:2] = [1, 4], sum = 1 + 4 = 5
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


# ----------------------------------------------------------------------------------
# Minimum Subarray Sum of Size K

def min_sum_sliding_window(arr, k):

    # Input Validation 
    if len(arr) < k:
        return None

    # Initialize
    window_sum = 0
    
    # Set up the initial window
    for i in range(k):
        window_sum += arr[i]
    
    min_sum = window_sum  # Initialize result
    
    # Slide the window across the array
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # Add new element, remove old element
        min_sum = min(min_sum, window_sum)  # Update min_sum
    
    return min_sum

print(min_sum_sliding_window([1, 2, 3], 2))     # Output: 3 → 1+2 = 3
print(min_sum_sliding_window([1, 4, 3, 8], 2))  # Output: 5 → 1+4 = 5

# print(min_sum_sliding_window([6, 4, 3], 2))     # Output: 7 → 3+4 = 7
# print(min_sum_sliding_window([3, 4, 6], 2))     # Output: 7 → 3+4 = 7
# print(min_sum_sliding_window([1, 2], 2))        # Output: 3 → 1+2 = 3


# ----------------------------------------------------------------------------------
# Solution 2 Breakdown: 

def min_sum_sliding_window(arr, k):    # Define the function that takes an array 'arr' and integer 'k'

    # Input Validation 
    if len(arr) < k:                   # Check if the array is too short for a window of size k
        return None                    # Return None since no subarrays of size k are possible
    
    # Initialize
    window_sum = 0                     # Initialize a variable to hold the window’s sum
                                       # Why? We’ll build the first window sum manually
    # Set up the initial window
    for i in range(k):                 # Loop through the first k elements
        window_sum += arr[i]           # Add each element to the window sum
                                       # Why? This creates the sum of the first window
    min_sum = window_sum               # Set the minimum sum to the first window’s sum
                                       # Why? It’s the smallest sum we’ve seen so far
    # Slide the window across the array
    for i in range(k, len(arr)):       # Loop from index k to the end of the array
        window_sum += arr[i] - arr[i - k]  # Slide the window: add the new element, subtract the old one
                                       # Why? This updates the sum for the next window efficiently
        min_sum = min(min_sum, window_sum)  # Update min_sum if the new window sum is smaller
                                       # Why? We want the smallest sum across all windows
    return min_sum                  # Return the smallest sum found


# ----------------------------------------------------------------------------------
# Solution 2 Output: 

# Minimum Subarray Sum of Size K
def min_sum_sliding_window(arr, k):    # arr = [1, 4, 3, 8], k = 2

    # Input Validation 
    if len(arr) < k:                   # len(arr) = 4, k = 2, so 4 >= 2, skip this
        return None                    # skip
    
    # Initialize
    window_sum = 0                     # window_sum = 0 (start with zero)

    # Set up the initial window
    for i in range(k):                 # i goes from 0 to 1 (k = 2)
                                       # i = 0
        window_sum += arr[i]           # window_sum = 0 + arr[0] = 0 + 1 = 1
                                       # i = 1
        window_sum += arr[i]           # window_sum = 1 + arr[1] = 1 + 4 = 5
    min_sum = window_sum            # min_sum = 5 (first window [1, 4])
    
    # Slide the window across the array
    for i in range(k, len(arr)):       # k = 2, len(arr) = 4, so i goes from 2 to 3
                                       # Iteration 1: i = 2
        window_sum += arr[i] - arr[i - k]  # arr[2] = 3, arr[2-2] = arr[0] = 1
                                           # window_sum = 5 + 3 - 1 = 7 (new window [4, 3])
        min_sum = min(min_sum, window_sum)  # min(5, 7) = 5, so min_sum = 5
                                       # Iteration 2: i = 3
        window_sum += arr[i] - arr[i - k]  # arr[3] = 8, arr[3-2] = arr[1] = 4
                                           # window_sum = 7 + 8 - 4 = 11 (new window [3, 8])
        min_sum = min(min_sum, window_sum)  # min(5, 11) = 5, so min_sum = 5
    
    return min_sum                  # min_sum = 5 (from window [1, 4])


print(min_sum_sliding_window([1, 4, 3, 8], 2))  # Output: 5 ([1, 4] has sum = 1 + 4 = 5)
