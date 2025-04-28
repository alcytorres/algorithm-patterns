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


print(max_difference_sliding_window([1, 2, 5], 2))  # Output: 3 ([2, 5] has max=5, min=2, diff=5-2=3)


"""
Walkthrough of Why `max_difference_sliding_window` Works:

The `max_difference_sliding_window` function finds the maximum difference between the largest and smallest elements in any contiguous subarray of size `k`. Here’s why it works for `[1, 2, 5], k=2`, explained simply:

    1. Check Array Size: It ensures the array has at least `k` elements. For `[1, 2, 5], k=2`, length `3 ≥ 2`, so proceed.

    2. First Window: It takes the first `k` elements (`[1, 2]`) and computes the difference (`max(1, 2) - min(1, 2) = 2 - 1 = 1`). This is the initial `max_diff`.

    3. Slide Window: It slides the window across the array, checking each `k`-sized subarray. For `i=2`, it forms `[2, 5]`, computes `max(2, 5) - min(2, 5) = 5 - 2 = 3`, and updates `max_diff = max(1, 3) = 3`.

    4. Track Maximum Difference: It keeps the largest difference found. For `[1, 2, 5]`, the differences are `1` (`[1, 2]`) and `3` (`[2, 5]`), so it returns `3`.

Explanation of `window = arr[i - k + 1:i + 1]`:
    - What It Does: This line creates a new window of `k` elements by taking a slice of the array from index `i - k + 1` to `i` (inclusive). For `i=2, k=2`, it computes `i - k + 1 = 2 - 2 + 1 = 1`, so `arr[1:3] = [2, 5]`, the subarray from index `1` to `2`.

    - Why It Works: It ensures the window is exactly `k` elements long (from `i - k + 1` to `i` spans `k` indices, e.g., `3 - 1 = 2` elements). As `i` increases, it slides the window right, dropping the oldest element (`arr[i - k]`) and adding the new one (`arr[i]`), correctly forming each consecutive `k`-sized subarray (e.g., `[2, 5]` after `[1, 2]`).

Why the Solution Works: The sliding window efficiently checks every `k`-sized subarray by updating the window with a slice, computing the max-min difference, and tracking the largest difference. For `[1, 2, 5], k=2`, it correctly identifies `[2, 5]` (difference = `3`) as the maximum, returning `3`. The approach is simple, uses O(n) time, and handles all cases accurately.
"""


# ----------------------------------------------------------------------------------
# Solution Maximum Difference in K Consecutive Elements  [1, 2, 5]

def max_difference_sliding_window(arr, k):    # arr = [1, 2, 5], k = 2
    # Input Validation 
    if len(arr) < k:                         # Is len(arr) = 3 < k = 2? No
        return None                          # Skip
    
    # Initialize
    window = arr[:k]                         # Initial window: arr[:2] = [1, 2]
    max_diff = max(window) - min(window)     # max([1, 2]) - min([1, 2]) = 2 - 1 = 1
    
    # Slide the window across the array
    for i in range(k, len(arr)):             # i = 2 to 2
                                             # Iteration 1: i = 2
        window = arr[i - k + 1:i + 1]        # New window: arr[1:3] = [2, 5]
        current_diff = max(window) - min(window)  # max([2, 5]) - min([2, 5]) = 5 - 2 = 3
        max_diff = max(max_diff, current_diff)    # max(1, 3) = 3, max_diff = 3
    
    return max_diff                          # Return 3 (highest difference found, from [2, 5])

print(max_difference_sliding_window([1, 2, 5], 2))  # Output: 3 ([2, 5])


# ----------------------------------------------------------------------------------
# Solution Maximum Difference in K Consecutive Elements  [5, 2, 1]

def max_difference_sliding_window(arr, k):    # arr = [5, 2, 1], k = 2
    # Input Validation 
    if len(arr) < k:                         # Is len(arr) = 3 < k = 2? No
        return None                          # Skip
    
    # Initialize
    window = arr[:k]                         # Initial window: arr[:2] = [5, 2]
    max_diff = max(window) - min(window)     # max([5, 2]) - min([5, 2]) = 5 - 2 = 3
    
    # Slide the window across the array
    for i in range(k, len(arr)):             # i = 2 to 2
                                             # Iteration 1: i = 2
        window = arr[i - k + 1:i + 1]        # New window: arr[1:3] = [2, 1]
        current_diff = max(window) - min(window)  # max([2, 1]) - min([2, 1]) = 2 - 1 = 1
        max_diff = max(max_diff, current_diff)    # max(3, 1) = 3, max_diff = 3
    
    return max_diff                          # Return 3 (highest difference found, from [5, 2])

print(max_difference_sliding_window([5, 2, 1], 2))  # Output: 3 ([5, 2])


# ----------------------------------------------------------------------------------
# Solution Finds the maximum difference (max - min) in any subarray of size k  [1, 4, 2, 8]

def max_difference_sliding_window(arr, k):    # arr = [1, 4, 2, 8], k = 2 (window size is 2)
    # Check if array is too short
    if len(arr) < k:                         # Is length of arr (4) less than k (2)? No
        return None                          # If yes, return None (not enough elements)
    
    # Set up the first window
    window = arr[:k]                         # Take first k elements: arr[:2] = [1, 4]
    max_diff = max(window) - min(window)     # Find max(1, 4) = 4, min(1, 4) = 1, so 4 - 1 = 3
    
    # Slide the window to check other subarrays
    for i in range(k, len(arr)):             # k = 2, len(arr) = 4, so i goes from 2 to 3
                                             # Iteration 1: i = 2
        window = arr[i - k + 1:i + 1]        # New window: arr[1:3] = [4, 2]
        current_diff = max(window) - min(window)  # max(4, 2) = 4, min(4, 2) = 2, so 4 - 2 = 2
        max_diff = max(max_diff, current_diff)    # Compare: max(3, 2) = 3, so max_diff = 3
                                             # Iteration 2: i = 3
        window = arr[i - k + 1:i + 1]        # New window: arr[2:4] = [2, 8]
        current_diff = max(window) - min(window)  # max(2, 8) = 8, min(2, 8) = 2, so 8 - 2 = 6
        max_diff = max(max_diff, current_diff)    # Compare: max(3, 6) = 6, so max_diff = 6
    
    return max_diff                          # Return 6 (largest difference found)


print(max_difference_sliding_window([1, 4, 2, 8], 2))  # Output: 6 ([2, 8] has max=8, min=2, diff=8-2=6)
