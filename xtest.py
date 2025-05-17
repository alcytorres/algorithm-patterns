# ----------------------------------------------------------------------------------
# 1. Maximum Sum of K Consecutive Elements
"""
Task: Find the maximum sum of any k consecutive elements in an array. ***If the length of the array is return None
Example 1: [1, 2, 3, 4]     k=2 → 7 (3 + 4)
Example 2: [1, 4, 6, 2]     k=2 → 10 (4 + 6)
Example 3: [1, 2, 3, 4, 5]  k=3 → 12 (3 + 4 + 5)
Why: Introduces fixed-size window sliding, key for Maximum Average Subarray I.
"""

def max_sum_k_consecutive(arr, k):

    # 1️⃣ Check if array length is sufficient
    if len(arr) < k:
        return None
    
    # 2️⃣ Initialize window sum for first k elements
    window_sum = sum(arr[:k])

    # 3️⃣ Initialize maximum sum
    max_sum = window_sum

    # 4️⃣ Iterate through remaining windows
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(window_sum, max_sum)

    # 5️⃣ Return the maximum sum
    return max_sum

print(max_sum_k_consecutive([1, 2, 3], 2))  # Output: 5 (2 + 3)
print(max_sum_k_consecutive([1, 2, 3, 4], 2))  # Output: 7 (3 + 4)