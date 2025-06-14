# Maximum Product of K Consecutive Elements
"""
Task: Given an integer array nums and an integer k, find the maximum product of any contiguous subarray of size k. If the array has fewer than k elements, return None.

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
    max_product = 1
    for num in arr[:k]:  # First k elements
        max_product *= num
    
    # 3️⃣ Set initial result
    result = max_product
    
    # 4️⃣ Slide the window across the array
    for i in range(k, len(arr)):
        # Update product: divide by first element of previous window, multiply by new element
        max_product = (max_product // arr[i - k]) * arr[i]
        result = max(result, max_product)
    
    # 5️⃣ Return the result
    return result

print(max_product_sliding_window([1, 2, 3], 2))      # Output: 6 ([2, 3])
print(max_product_sliding_window([1, 2, 3, 4], 2))   # Output: 12 ([3, 4])
print(max_product_sliding_window([2, 3, 4, 5], 2))   # Output: 20 ([4, 5])




"""
Explanation: window_product = window_product // arr[i - k] * arr[i]

The line max_product = (max_product // arr[i - k]) * arr[i] updates the product of the current window of k elements as the window slides. Here’s a simple, concise explanation:

What it does: It calculates the product of the new window by:
    Removing the first element of the previous window (divide by arr[i - k]).
    Adding the new element at the end (multiply by arr[i]).

Why: The window slides one position right, so we drop the oldest element (arr[i - k], the element k steps back from i) and include the new element (arr[i]).

Example: For arr = [1, 2, 3, 4], k = 2:
    
    At i = 2, previous window is [1, 2] (product = 1 * 2 = 2).
    
    New window is [2, 3]:
        arr[i - k] = arr[2 - 2] = arr[0] = 1 (oldest element).
        arr[i] = arr[2] = 3 (new element).
        max_product = (2 // 1) * 3 = 2 * 3 = 6 (product of [2, 3]).

Note: // is integer division, assuming no zeros (if zeros are possible, a different approach is needed to avoid division errors).

This keeps the product updated efficiently without recalculating it from scratch.




Why I chose to use 2 loops for this Sliding Window Product Problem 

Two Loops for max_product_sliding_window
    - Why Optimal: Initializing the product requires a loop over k elements (no prod function in Python).
    - Clarity: Separating initialization from sliding enhances readability.
    - Performance: Single loop adds complex conditionals without improving O(n) time complexity.

One Loop for max_sum_sliding_window (This is a differnt problem: find the maximum sum of any contiguous subarray of size k)
    - Why Optimal: sum(arr[:k]) simplifies initialization to one line.
    - Integration: Sliding (addition/subtraction) flows naturally into a single loop, improving conciseness.
    - Clarity: Avoids unnecessary loop separation.

Why Different
    - Operation Nature: Product needs a loop for initialization; sum uses sum for simplicity.
    - Readability: Loop choice optimizes clarity for each problem’s operation.
    - Performance: Both achieve O(n) time complexity, but structure enhances maintainability.
"""



# ----------------------------------------------------------------------------------
# Solution Breakdown: Maximum Product of K Consecutive Elements

# Task: Find the maximum product of any group of k consecutive elements in an array. If the array has fewer than k elements, return None.

# Example: arr = [1, 2, 3, 4], k = 2 → Output = 12 (subarray [3, 4] has product 3 * 4 = 12)

def max_product_sliding_window(arr, k):  # Example: arr = [1, 2, 3, 4], k = 2

    # 1️⃣ Input Validation
    # Check if the array has fewer than k elements
    # Why? We can't form a subarray of size k if the array is too small
    if len(arr) < k:  # len(arr) = 4, k = 2, 4 < 2 is false, proceed
        return None  # skip

    # 2️⃣ Initialize the first window
    # Compute the product of the first k elements
    # Why? We need the product of the first subarray as the starting point
    max_product = 1  # max_product = 1 (initial value for multiplication)
    for num in arr[:k]:  # arr[:2] = [1, 2]
        max_product *= num  # First: max_product = 1 * 1 = 1
                            # Second: max_product = 1 * 2 = 2
    # After loop: max_product = 2 (product of [1, 2])

    # 3️⃣ Set initial result
    # Store the first window's product as the initial maximum
    # Why? We need to compare this with products of subsequent windows
    result = max_product  # result = 2

    # 4️⃣ Slide the window across the array
    # Iterate from index k to the end to process each subsequent window
    # Why? We slide the window one element at a time to check all k-sized subarrays
    for i in range(k, len(arr)):  # k = 2, len(arr) = 4, i goes from 2 to 3
        # --- Iteration 1: i = 2 ---
        # Update product: divide by first element of previous window, multiply by new element
        # Why? This efficiently updates the product without recomputing the entire window
        max_product = (max_product // arr[i - k]) * arr[i]  # i = 2, i-k = 2-2 = 0
                                                           # arr[0] = 1, arr[2] = 3
                                                           # max_product = (2 // 1) * 3 = 2 * 3 = 6

        # Update result if current product is larger
        # Why? We want the largest product across all windows
        result = max(result, max_product)  # result = max(2, 6) = 6
        # After Iteration 1: max_product = 6, result = 6
        # Current window: [2, 3] (product = 6)

        # --- Iteration 2: i = 3 ---
        if i == 3:
            # Update product
            max_product = (max_product // arr[i - k]) * arr[i]  # i = 3, i-k = 3-2 = 1
                                                               # arr[1] = 2, arr[3] = 4
                                                               # max_product = (6 // 2) * 4 = 3 * 4 = 12

            # Update result
            result = max(result, max_product)  # result = max(6, 12) = 12
            # After Iteration 2: max_product = 12, result = 12
            # Current window: [3, 4] (product = 12)

    # 5️⃣ Return the result
    # Why? result contains the largest product found in any k-sized subarray
    return result  # result = 12


print(max_product_sliding_window([1, 2, 3, 4], 2))  # Output: 12 ([3, 4])


# ----------------------------------------------------------------------------------
# Solution Output:
