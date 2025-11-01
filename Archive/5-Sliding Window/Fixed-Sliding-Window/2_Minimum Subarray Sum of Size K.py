# Minimum Subarray Sum of Size K
"""
Task: Given an integer array nums and an integer k, find the minimum sum of any contiguous subarray of size k. If the array has fewer than k elements, return None.

Example 1: [1, 2, 3, 4],  k = 2 → 3
Example 1: [1, 4, 3, 8],  k = 2 → 5
Example 3: [6, 4, 3],     k = 2 → 7

Why: Practices sliding window technique to compute sums efficiently.
"""

def min_sum_sliding_window(arr, k):

    # 1️⃣ Input Validation
    if len(arr) < k:
        return None
    
    # 2️⃣ Initialize the first window
    window_sum = sum(arr[:k])

    # 3️⃣ Compute initial result for first window
    min_sum = window_sum 
    
    # 4️⃣ Slide the window across the array
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]  
        min_sum = min(min_sum, window_sum)
    
    # 5️⃣ Return min_sum
    return min_sum

print(min_sum_sliding_window([1, 2, 3, 4], 2))   # Output: 3 → 1+2 = 3
print(min_sum_sliding_window([1, 4, 3, 8], 2))   # Output: 5 → 1+4 = 5

# print(min_sum_sliding_window([6, 4, 3], 2))     # Output: 7 → 3+4 = 7
# print(min_sum_sliding_window([3, 4, 6], 2))     # Output: 7 → 3+4 = 7
# print(min_sum_sliding_window([1, 2], 2))        # Output: 3 → 1+2 = 3



# ----------------------------------------------------------------------------------
# Solution Breakdown: Minimum Subarray Sum of Size K

# Task: Find the minimum sum of any contiguous subarray of size k in an array.
# If the array has fewer than k elements, return None.

def min_sum_sliding_window(arr, k):  # Example: arr = [1, 2, 3, 4], k = 2

    # 1️⃣ Input Validation
    # Check if the array has fewer than k elements
    # Why? We can't form a subarray of size k if the array is too small
    if len(arr) < k:  # len(arr) = 4, k = 2, 4 < 2 is false, proceed
        return None  # skip

    # 2️⃣ Initialize the first window
    # Compute the sum of the first k elements
    # Why? We need the sum of the first subarray as the starting point
    window_sum = sum(arr[:k])  # arr[:2] = [1, 2], window_sum = 1 + 2 = 3

    # 3️⃣ Compute initial result for first window
    # Set the first window's sum as the initial minimum
    # Why? We need to compare this with sums of subsequent windows
    min_sum = window_sum  # min_sum = 3

    # 4️⃣ Slide the window across the array
    # Iterate from index k to the end to process each subsequent window
    # Why? We slide the window one element at a time to check all k-sized subarrays
    for i in range(k, len(arr)):  # k = 2, len(arr) = 4, i goes from 2 to 3
        # --- Iteration 1: i = 2 ---
        # Update sum: add new element, subtract the first element of the previous window
        # Why? This efficiently updates the sum without recomputing the entire window
        window_sum += arr[i] - arr[i - k]  # i = 2, arr[2] = 3, i-k = 2-2 = 0, arr[0] = 1
                                           # window_sum = 3 + 3 - 1 = 5

        # Update minimum sum if the current sum is smaller
        # Why? We want the smallest sum across all windows
        min_sum = min(min_sum, window_sum)  # min_sum = min(3, 5) = 3
        # After Iteration 1: window_sum = 5, min_sum = 3
        # Current window: [2, 3] (sum = 5)

        # --- Iteration 2: i = 3 ---
        if i == 3:
            # Update sum
            window_sum += arr[i] - arr[i - k]  # i = 3, arr[3] = 4, i-k = 3-2 = 1, arr[1] = 2
                                               # window_sum = 5 + 4 - 2 = 7

            # Update minimum sum
            min_sum = min(min_sum, window_sum)  # min_sum = min(3, 7) = 3
            # After Iteration 2: window_sum = 7, min_sum = 3
            # Current window: [3, 4] (sum = 7)

    # 5️⃣ Return min_sum
    # Why? min_sum contains the smallest sum found in any k-sized subarray
    return min_sum  # min_sum = 3


print(min_sum_sliding_window([1, 2, 3, 4], 2))  # Output: 3 → 1+2 = 3