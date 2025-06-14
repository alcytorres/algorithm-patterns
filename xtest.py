# Maximum Product of K Consecutive Elements
"""
Task: Given an integer array nums and an integer k, find the maximum product of any contiguous subarray of size k. If the array has fewer than k elements, return None.

Example 1: [1, 2, 3],    k = 2 → 6 ([2, 3])
Example 1: [1, 2, 3, 4], k = 2 → 12 ([3, 4])
Example 3: [2, 3, 4, 5], k = 2 → 20 ([4, 5])
"""

def max_product_sliding_window(arr, k):
    # 1️⃣ Input Validation
    if len(arr) < k:
        return None
    
    # 2️⃣ Initialize the first window
    max_product = 1
    for num in arr[:k]:  # First k elements
        max_product *= num
    
    # 3️⃣ Set initial result
    result = max_product
    
    # 4️⃣ Slide the window across the array
    for i in range(k, len(arr)):
        # Update product: divide by first element of previous window, multiply by new element
        max_product = (max_product // arr[i - k]) * arr[i]
        # Update result if current product is larger
        result = max(result, max_product)
    
    # 5️⃣ Return the result
    return result


print(max_product_sliding_window([1, 2, 3, 4], 2))   # Output: 12 ([3, 4])
