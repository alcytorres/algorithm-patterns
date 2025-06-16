# Maximum Subarray Sum of Size K 
"""
Foundational Skills
   - Array/string manipulation
   - Loop control
   - Conditional statements
Potential Knowledge Gaps
   - Managing window size (fixed vs. variable)
   - Adjusting the window dynamically (e.g., shrinking or expanding)

   
Task: Given an array of numbers and an integer k, find the maximum sum of any contiguous subarray of size k. 
If the array has fewer than k numbers, return None.

Example 1: [1, 2, 3, 4]     k=2 → 7 (3 + 4)
Example 2: [1, 4, 6, 2]     k=2 → 10 (4 + 6)
Example 3: [1, 2, 3, 4, 5]  k=3 → 12 (3 + 4 + 5)

Why: Practices sliding window technique to compute sums efficiently.
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
    
    # 5️⃣ Return max_sum
    return max_sum


print(max_sum_sliding_window([1, 2, 3, 4], 2))  # Output: 7   → 3+4 = 7
print(max_sum_sliding_window([1, 4, 6, 2], 2))  # Output: 10  → 4+6 = 10

# print(max_sum_sliding_window([1, 2], 2))        # Output: 3  → 1+2 = 5
# print(max_sum_sliding_window([1, 2, 5], 2))     # Output: 7  → 2+5 = 7
# print(max_sum_sliding_window([5, 2, 1], 2))     # Output: 7  → 2+5 = 7



# Simple Breakdown
def max_sum_sliding_window(arr, k):   # Define the function that takes an array 'arr' and integer 'k'
    """
    Finds the maximum sum of any k consecutive elements.
    
    - Uses a fixed-size sliding window to compute sums efficiently.
    - Time Complexity: O(n), Space Complexity: O(1).
    - Sliding window is intuitive and beginner-friendly for fixed sizes.
    """
    # 1️⃣ Input Validation
    if len(arr) < k:       # Check if the array is shorter than 'k'
        return None        # Return None since we can't form a window of size 'k'
    
    # 2️⃣ Initialize the first window
    window_sum = sum(arr[:k])  # Sum of first window

    # 3️⃣ Compute initial result for first window
    max_sum = window_sum   # Set the initial maximum sum to the first window's sum

    # 4️⃣ Slide the window across the array
    for i in range(k, len(arr)):  # Loop from index k to the end of the array
        window_sum = window_sum - arr[i - k] + arr[i]  # Slide the window: subtract the leftmost element, add the new right element
        max_sum = max(max_sum, window_sum)  # Update max_sum if the current window sum is larger

    # 5️⃣ Return max_sum
    return max_sum         # Return the maximum sum found


print(max_sum_sliding_window([1, 2, 3, 4], 2))  # Output: 7 (3 + 4)


# ----------------------------------------------------------------------------------
# Solution Breakdowwn: Maximum Subarray Sum of Size K

# Task: Find the maximum sum of any contiguous subarray of size k in an array.
# If the array has fewer than k elements, return None.


def max_sum_sliding_window(arr, k):  # Example: arr = [1, 2, 3, 4], k = 2

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
    # Set the first window's sum as the initial maximum
    # Why? We need to compare this with sums of subsequent windows
    max_sum = window_sum  # max_sum = 3

    # 4️⃣ Slide the window across the array
    # Iterate from index k to the end to process each subsequent window
    # Why? We slide the window one element at a time to check all k-sized subarrays
    for i in range(k, len(arr)):  # k = 2, len(arr) = 4, i goes from 2 to 3
        # --- Iteration 1: i = 2 ---
        # Update sum: add new element, subtract the first element of the previous window
        # Why? This efficiently updates the sum without recomputing the entire window
        window_sum += arr[i] - arr[i - k]  # i = 2, arr[2] = 3, i-k = 2-2 = 0, arr[0] = 1
                                           # window_sum = 3 + 3 - 1 = 5

        # Update maximum sum if the current sum is larger
        # Why? We want the largest sum across all windows
        max_sum = max(max_sum, window_sum)  # max_sum = max(3, 5) = 5
        # After Iteration 1: window_sum = 5, max_sum = 5
        # Current window: [2, 3] (sum = 5)

        # --- Iteration 2: i = 3 ---
        if i == 3:
            # Update sum
            window_sum += arr[i] - arr[i - k]  # i = 3, arr[3] = 4, i-k = 3-2 = 1, arr[1] = 2
                                               # window_sum = 5 + 4 - 2 = 7

            # Update maximum sum
            max_sum = max(max_sum, window_sum)  # max_sum = max(5, 7) = 7
            # After Iteration 2: window_sum = 7, max_sum = 7
            # Current window: [3, 4] (sum = 7)

    # 5️⃣ Return max_sum
    # Why? max_sum contains the largest sum found in any k-sized subarray
    return max_sum  # max_sum = 7


print(max_sum_sliding_window([1, 2, 3, 4], 2))  # Output: 7 → 3+4 = 7



# ----------------------------------------------------------------------------------
# Solution with output Full Breakdown 

# Task: Find the maximum sum of any contiguous subarray of size k in an array.
# If the array has fewer than k elements, return None.


def max_sum_sliding_window(arr, k):  # Example: arr = [1, 4, 6, 2], k = 2

    # 1️⃣ Input Validation
    # Check if the array has fewer than k elements
    # Why? We can't form a subarray of size k if the array is too small
    if len(arr) < k:  # len(arr) = 4, k = 2, 4 < 2 is false, proceed
        return None  # skip

    # 2️⃣ Initialize the first window
    # Compute the sum of the first k elements
    # Why? We need the sum of the first subarray as the starting point
    window_sum = sum(arr[:k])  # arr[:2] = [1, 4], window_sum = 1 + 4 = 5

    # 3️⃣ Compute initial result for first window
    # Set the first window's sum as the initial maximum
    # Why? We need to compare this with sums of subsequent windows
    max_sum = window_sum  # max_sum = 5

    # 4️⃣ Slide the window across the array
    # Iterate from index k to the end to process each subsequent window
    # Why? We slide the window one element at a time to check all k-sized subarrays
    for i in range(k, len(arr)):  # k = 2, len(arr) = 4, i goes from 2 to 3
        # --- Iteration 1: i = 2 ---
        # Update sum: add new element, subtract the first element of the previous window
        # Why? This efficiently updates the sum without recomputing the entire window
        window_sum += arr[i] - arr[i - k]  # i = 2, arr[2] = 6, i-k = 2-2 = 0, arr[0] = 1
                                           # window_sum = 5 + 6 - 1 = 10

        # Update maximum sum if the current sum is larger
        # Why? We want the largest sum across all windows
        max_sum = max(max_sum, window_sum)  # max_sum = max(5, 10) = 10
        # After Iteration 1: window_sum = 10, max_sum = 10
        # Current window: [4, 6] (sum = 10)

        # --- Iteration 2: i = 3 ---
        if i == 3:
            # Update sum
            window_sum += arr[i] - arr[i - k]  # i = 3, arr[3] = 2, i-k = 3-2 = 1, arr[1] = 4
                                               # window_sum = 10 + 2 - 4 = 8

            # Update maximum sum
            max_sum = max(max_sum, window_sum)  # max_sum = max(10, 8) = 10
            # After Iteration 2: window_sum = 8, max_sum = 10
            # Current window: [6, 2] (sum = 8)

    # 5️⃣ Return max_sum
    # Why? max_sum contains the largest sum found in any k-sized subarray
    return max_sum  # max_sum = 10


print(max_sum_sliding_window([1, 4, 6, 2], 2))  # Output: 10 → 4+6 = 10
