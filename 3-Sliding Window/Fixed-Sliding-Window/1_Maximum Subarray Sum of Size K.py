# Maximum Subarray Sum of Size K 
"""
Task: Given an array of numbers and an integer k, find the maximum sum of any contiguous subarray of size k. If the array has fewer than k numbers, return None.

Example 1: [1, 2, 3],    k = 2 → 5  
Example 2: [1, 4, 3, 8], k = 2 → 11  
Example 3: [4, 5, 6, 7], k = 3 → 18  
"""

def max_sum_sliding_window(arr, k):

    # 1️⃣ Input Validation  
    if len(arr) < k:
        return None
    
    # 2️⃣ Initialize the first window
    window_sum = sum(arr[:k])   

    # 3️⃣ Compute initial result for first window
    max_sum = window_sum 
    
    # 4️⃣ Slide the window across the array
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]  
        max_sum = max(max_sum, window_sum)
    
    # 5️⃣ Return max_result
    return max_sum


print(max_sum_sliding_window([1, 2, 3], 2))     # Output: 5   → 2+3 = 5
print(max_sum_sliding_window([1, 4, 3, 8], 2))  # Output: 11  → 3+11 = 11
print(max_sum_sliding_window([4, 5, 6, 7], 3))  # Output: 18  → 5+6+7 = 18

# print(max_sum_sliding_window([1, 2], 2))        # Output: 3  → 1+2 = 5
# print(max_sum_sliding_window([1, 2, 5], 2))     # Output: 7  → 2+5 = 7
# print(max_sum_sliding_window([5, 2, 1], 2))     # Output: 7  → 2+5 = 7


# ----------------------------------------------------------------------------------
# Solution Breakdowwn: Maximum Subarray Sum of Size K

def max_sum_sliding_window(arr, k):    # Example: arr = [1, 2, 3], k = 2
    # Check if the array is too short to have a subarray of size k
    if len(arr) < k:                   # len(arr) = 3, k = 2, so 3 >= 2, skip this
        # Return None since no subarrays of size k are possible
        return None                    # skip
    
    # Add up the first k numbers as our starting group (window)
    # Why? This is the first possible sum we can check
    window_sum = sum(arr[:k])          # arr[:2] = [1, 2], sum = 1 + 2 = 3
    
    # Set the maximum sum to our first window's sum
    # Why? It's the biggest sum we know so far (we just started!)
    max_sum = window_sum               # max_sum = 3 (first window [1, 2])
    
    # Slide the window across the array, one step at a time
    # Why? To check every possible group of k numbers
    for i in range(k, len(arr)):       # k = 2, len(arr) = 3, so i goes from 2 to 2
                                       # Iteration 1: i = 2
        # Update the sum: add the new number, subtract the old one
        # Why? This slides our window over by one spot efficiently
        window_sum += arr[i] - arr[i - k]  # arr[2] = 3, arr[2-2] = arr[0] = 1
                                           # window_sum = 3 + 3 - 1 = 5 (new window [2, 3])
        
        # Update the maximum if our new sum is bigger
        # Why? We want the biggest sum we find across all windows
        max_sum = max(max_sum, window_sum)  # max(3, 5) = 5, so max_sum = 5
    
    # Give back the biggest sum we found
    return max_sum                     # max_sum = 5 (from window [2, 3])


print(max_sum_sliding_window([1, 2, 3], 2))  # Output: 5 ([2, 3] has sum = 2 + 3 = 5)


# ----------------------------------------------------------------------------------
# Solution Output: 

def max_sum_sliding_window(arr, k):    # arr = [1, 2, 3], k = 2 
    if len(arr) < k:                   # len(arr) = 3, k = 2, so 3 >= 2, skip this
        return None                    # skip
    
    # Initialize the first window
    window_sum = sum(arr[:k])          # arr[:2] = [1, 2], sum = 1 + 2 = 3
   
    # Compute initial result for first window
    max_sum = window_sum               # max_sum = 3 (first window [1, 2])
    
    # Slide the window across the array
    for i in range(k, len(arr)):       # k = 2, len(arr) = 3, so i goes from 2 to 2
                                       # Iteration 1: i = 2
        window_sum += arr[i] - arr[i - k]  # arr[2] = 3, arr[2-2] = arr[0] = 1
                                           # window_sum = 3 + 3 - 1 = 5 (new window [2, 3])
        max_sum = max(max_sum, window_sum) # max(3, 5) = 5, so max_sum = 5
    
    return max_sum                     # max_sum = 5 (from window [2, 3])


print(max_sum_sliding_window([1, 2, 3], 2))  # Output: 5 ([2, 3] has sum = 2 + 3 = 5)


# ----------------------------------------------------------------------------------
# Solution Output:

def max_sum_sliding_window(arr, k):    # arr = [1, 4, 3, 8], k = 2
    if len(arr) < k:                   # len(arr) = 4, k = 2, so 4 >= 2, skip this
        return None                    # skip
    
    # Initialize the first window
    window_sum = sum(arr[:k])          # arr[:2] = [1, 4], sum = 1 + 4 = 5
   
    # Compute initial result for first window
    max_sum = window_sum               # max_sum = 5 (first window [1, 4])
    
    # Slide the window across the array
    for i in range(k, len(arr)):       # k = 2, len(arr) = 4, so i goes from 2 to 3
                                       # Iteration 1: i = 2
        window_sum += arr[i] - arr[i - k]  # arr[2] = 3, arr[2-2] = arr[0] = 1
                                           # window_sum = 5 + 3 - 1 = 7 (new window [4, 3])
        max_sum = max(max_sum, window_sum) # max(5, 7) = 7, so max_sum = 7
                                       # Iteration 2: i = 3
        window_sum += arr[i] - arr[i - k]  # arr[3] = 8, arr[3-2] = arr[1] = 4
                                           # window_sum = 7 + 8 - 4 = 11 (new window [3, 8])
        max_sum = max(max_sum, window_sum) # max(7, 11) = 11, so max_sum = 11
    
    return max_sum                     # max_sum = 11 (from window [3, 8])


print(max_sum_sliding_window([1, 4, 3, 8], 2))  # Output: 11 ([3, 8] has sum = 3 + 8 = 11)
