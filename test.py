# Maximum Difference (max -min) in K Consecutive Elements
"""
Task: Given an array of numbers and an integer k, find the maximum difference between the largest and smallest numbers in any group of k numbers that are next to each other in the list. If the array has fewer than k numbers, return None.

Example 1: [1, 2, 5], k = 2 → 3 (subarray [2, 5] has max 5, min 2, difference 5 - 2 = 3)
Example 2: [5, 2, 1], k = 2 → 3 (subarray [2, 5] has max 5, min 2, difference 5 - 2 = 3)
Example 3: [1, 4, 2, 8], k = 2 → 6 (subarray [2, 8] has max 8, min 2, difference 8 - 2 = 6)
"""


# Solution Breakdown 
def max_difference_sliding_window(arr, k):    # arr = [1, 2, 5], k = 2 (window size is 2)
    # Check if array is too short
    if len(arr) < k:                         # Is length of arr (3) less than k (2)? No
        return None                          # If yes, return None (not enough elements)
    
    # Set up the first window
    window = arr[:k]                         # Take first k elements: arr[:2] = [1, 2]
    max_diff = max(window) - min(window)     # Find max(1, 2) = 2, min(1, 2) = 1, so 2 - 1 = 1
    
    # Slide the window to check other subarrays
    for i in range(k, len(arr)):             # k = 2, len(arr) = 3, so i goes from 2 to 2
                                             # Only one iteration: i = 2
        window = arr[i - k + 1:i + 1]        # New window: arr[1:3] = [2, 5] (slide right)
        current_diff = max(window) - min(window)  # max(2, 5) = 5, min(2, 5) = 2, so 5 - 2 = 3
        max_diff = max(max_diff, current_diff)    # Compare: max(1, 3) = 3, so max_diff = 3
    
    return max_diff                          # Return 3 (largest difference found)


print(max_difference_sliding_window([1, 2, 6, 12], 3))  # Output: 
