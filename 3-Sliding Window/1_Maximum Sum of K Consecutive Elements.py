# 3. Sliding Window
"""
Foundational Skills
   - Array/string manipulation
   - Loop control
   - Conditional statements
Potential Knowledge Gaps
   - Managing window size (fixed vs. variable)
   - Adjusting the window dynamically (e.g., shrinking or expanding)
"""

# ----------------------------------------------------------------------------------
# 1. Maximum Sum of K Consecutive Elements
"""
Maximum Sum of K Consecutive Elements
Task: Find the maximum sum of any k consecutive elements in an array.
Example: [1, 2, 3, 4], k=2 → 7 (3 + 4)
Why: Introduces fixed-size window sliding, key for Maximum Average Subarray I.
"""

def max_sum_k_consecutive(arr, k):
    if len(arr) < k:
        return None
    window_sum = sum(arr[:k])  # Sum of first window
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]  # Slide window
        max_sum = max(max_sum, window_sum)
    return max_sum


print(max_sum_k_consecutive([1, 2, 3, 4], 2))  # Output: 7 (3 + 4)


# Solution
def max_sum_k_consecutive(arr, k):   # Define the function that takes an array 'arr' and integer 'k'
    """
    Finds the maximum sum of any k consecutive elements.
    
    - Uses a fixed-size sliding window to compute sums efficiently.
    - Time Complexity: O(n), Space Complexity: O(1).
    - Sliding window is intuitive and beginner-friendly for fixed sizes.
    """
    if len(arr) < k:       # Check if the array is shorter than 'k'
        return None        # Return None since we can't form a window of size 'k'
    window_sum = sum(arr[:k])  # Calculate the sum of the first k elements (first window)
    max_sum = window_sum   # Set the initial maximum sum to the first window's sum
    for i in range(k, len(arr)):  # Loop from index k to the end of the array
        window_sum = window_sum - arr[i - k] + arr[i]  # Slide the window: subtract the leftmost element, add the new right element
        max_sum = max(max_sum, window_sum)  # Update max_sum if the current window sum is larger
    return max_sum         # Return the maximum sum found

# Test the function
print(max_sum_k_consecutive([1, 2, 3, 4], 2))  # Output: 7 (3 + 4)


# ----------------------------------------------------------------------------------
# Solution with output 

def max_sum_k_consecutive(arr, k):                 # arr = [1, 2, 3, 4], k = 2
    if len(arr) < k:                               # 4 < 2 → False
        return None                                # skip
    window_sum = sum(arr[:k])                      # arr[:2] = [1, 2] → window_sum = 1 + 2 = 3
    max_sum = window_sum                           # max_sum = 3
    for i in range(k, len(arr)):                   # range(2, 4) → i = 2, 3
        window_sum = window_sum - arr[i - k] + arr[i]  # i = 2: 3 - arr[0] + arr[2] = 3 - 1 + 3 = 5
                                                       # i = 3: 5 - arr[1] + arr[3] = 5 - 2 + 4 = 7
        max_sum = max(max_sum, window_sum)         # i = 2: max(3, 5) = 5
                                                   # i = 3: max(5, 7) = 7
    return max_sum                                 # Return 7


print(max_sum_k_consecutive([1, 2, 3, 4], 2))  # Output: 7 (3 + 4)
