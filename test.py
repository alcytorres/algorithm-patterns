# 3. Sliding Window

# ----------------------------------------------------------------------------------
# 1. Maximum Sum of K Consecutive Elements
"""
Task: Find the maximum sum of any k consecutive elements in an array. .
Example 1: [1, 2, 3],    k=2 → 5 (2 + 3)
Example 2: [1, 2, 3, 4], k=2 → 7 (3 + 4)
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

print(max_sum_k_consecutive([1, 4, 6, 2], 2))  # Output: 10 


