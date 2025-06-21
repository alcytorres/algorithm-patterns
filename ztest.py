# Maximum Product of K Consecutive Elements
"""
Task: Given an integer array nums and an integer k, find the maximum product of any contiguous subarray of size k. 
    - If the array has fewer than k elements, return None.

Example 1: [1, 2, 3],    k = 2 → 6 ([2, 3])
Example 1: [1, 2, 3, 4], k = 2 → 12 ([3, 4])
Example 3: [2, 3, 4, 5], k = 2 → 20 ([4, 5])

# Why: Practices sliding window technique to compute products efficiently.
"""

def max_product_sliding_window(arr, k):
    
    # 1️⃣ Input Validation
    if len(arr) < k:
        return None
    
    # 2️⃣ Initialize the first window
    window_product = 1
    for num in arr[:k]:
        window_product *= num

    # 3️⃣ Set initial result
    max_product = window_product
    
    # 4️⃣ Slide the window across the array
    for i in range(k, len(arr)):
        window_product = (window_product // arr[i - k] * arr[i])
        max_product = max(window_product, max_product)
    
    # 5️⃣ Return the result
    return max_product

print(max_product_sliding_window([1, 2, 3], 2))      # Output: 6 ([2, 3])
