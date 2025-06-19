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
        max_product = max(max_product, window_product)
    
    # 5️⃣ Return the result
    return max_product

print(max_product_sliding_window([1, 2, 3], 2))      # Output: 6 ([2, 3])

# print(max_product_sliding_window([1, 2, 3, 4], 2))   # Output: 12 ([3, 4])
# print(max_product_sliding_window([2, 3, 4, 5], 2))   # Output: 20 ([4, 5])


# Simple Breakdown
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
        # Update product: divide by first element of previous window, multiply by new element
        window_product = (window_product // arr[i - k] * arr[i])
        max_product = max(max_product, window_product)
    
    # 5️⃣ Return the result
    return max_product

# print(max_product_sliding_window([1, 2, 3], 2))      # Output: 6 ([2, 3])

"""
# ----------------------------------------------------------------------------------
Simple Explanation of window_product = (window_product // arr[i - k] * arr[i]):

Imagine you have a list of numbers like [1, 2, 3, 4, 5] and you’re looking at groups of 2 numbers at a time (k=2). You want to multiply those 2 numbers and find the biggest result. 

The line window_product = (window_product // arr[i - k] * arr[i]) is like sliding a window to look at the next group without starting over.

Here’s what it does, super simple:

    You have the product of the current group, say 1 * 2 = 2 for [1, 2].
    
    To get the next group [2, 3], you don’t want to multiply 2 * 3 from scratch.
    
    Instead, you undo the first number (1) by dividing (2 ÷ 1 = 2) and add the new number (3) by multiplying (2 * 3 = 6).
    
    This line does that in one step: divide by the old number (arr[i - k]) and multiply by the new number (arr[i]).
    
    Why? It’s faster! Instead of multiplying the whole group again, you just tweak the old product to get the new one, like sliding a toy car one step forward instead of building a new car each time.


Full Summary
    For [1, 2, 3, 4, 5], k=2 in max_product_sliding_window:

1. Validate: len(arr)=5 ≥ k=2, proceed.
2. First window ([1, 2]): window_product = 1 * 2 = 2, max_product = 2.
3. Slide to [2, 3]: i=2, window_product = (2 // arr[0]=1) * arr[2]=3 = 6, max_product = max(2, 6) = 6.
4. Slide to [3, 4]: i=3, window_product = (6 // arr[1]=2) * arr[3]=4 = 12, max_product = max(6, 12) = 12.
5. Slide to [4, 5]: i=4, window_product = (12 // arr[2]=3) * arr[4]=5 = 20, max_product = max(12, 20) = 20.
6. Return: max_product = 20 (from [4, 5]).
    



# ----------------------------------------------------------------------------------
Explanation: window_product = (window_product // arr[i - k]) * arr[i]

The line window_product = (window_product // arr[i - k]) * arr[i] updates the product of the current window of k elements as the window slides. Here’s a simple, concise explanation:

What it does: It calculates the product of the new window by:
    Removing the first element of the previous window (divide by arr[i - k]).
    Adding the new element at the end (multiply by arr[i]).

Why: The window slides one position right, so we drop the oldest element (arr[i - k], the element k steps back from i) and include the new element (arr[i]).

Example: For arr = [1, 2, 3, 4], k = 2:
    
    At i = 2, previous window is [1, 2] (product = 1 * 2 = 2).
    
    New window is [2, 3]:
        arr[i - k] = arr[2 - 2] = arr[0] = 1 (oldest element).
        arr[i] = arr[2] = 3 (new element).
        window_product = (2 // 1) * 3 = 2 * 3 = 6 (product of [2, 3]).

This keeps the product updated efficiently without recalculating it from scratch.


# ----------------------------------------------------------------------------------
The solution uses // (integer division) instead of / (floating-point division) to keep the product calculation simple, precise, and consistent with the integer inputs, avoiding decimal results and potential precision issues.


# ----------------------------------------------------------------------------------
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
"""



# ----------------------------------------------------------------------------------
# Solution Breakdown: Maximum Product of K Consecutive Elements

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
    window_product = 1  # window_product = 1 (initial value for multiplication)
    for num in arr[:k]:  # arr[:2] = [1, 2]
        window_product *= num  # First: window_product = 1 * 1 = 1
                               # Second: window_product = 1 * 2 = 2
    # After loop: window_product = 2 (product of [1, 2])

    # 3️⃣ Set initial result
    # Store the first window's product as the initial maximum
    # Why? We need to compare this with products of subsequent windows
    max_product = window_product  # max_product = 2

    # 4️⃣ Slide the window across the array
    # Iterate from index k to the end to process each subsequent window
    # Why? We slide the window one element at a time to check all k-sized subarrays
    for i in range(k, len(arr)):  # k = 2, len(arr) = 4, i goes from 2 to 3
        # --- Iteration 1: i = 2 ---
        # Update product: divide by first element of previous window, multiply by new element
        # Why? This efficiently updates the product without recomputing the entire window
        window_product = (window_product // arr[i - k]) * arr[i]  # i = 2, i-k = 2-2 = 0
                                                                 # arr[0] = 1, arr[2] = 3
                                                                 # window_product = (2 // 1) * 3 = 2 * 3 = 6

        # Update result if current product is larger
        # Why? We want the largest product across all windows
        max_product = max(max_product, window_product)  # max_product = max(2, 6) = 6
        # After Iteration 1: window_product = 6, max_product = 6
        # Current window: [2, 3] (product = 6)

        # --- Iteration 2: i = 3 ---
        if i == 3:
            # Update product
            window_product = (window_product // arr[i - k]) * arr[i]  # i = 3, i-k = 3-2 = 1
                                                                     # arr[1] = 2, arr[3] = 4
                                                                     # window_product = (6 // 2) * 4 = 3 * 4 = 12

            # Update result
            max_product = max(max_product, window_product)  # max_product = max(6, 12) = 12
            # After Iteration 2: window_product = 12, max_product = 12
            # Current window: [3, 4] (product = 12)

    # 5️⃣ Return the max_product
    # Why? max_product contains the largest product found in any k-sized subarray
    return max_product  # max_product = 12


print(max_product_sliding_window([1, 2, 3, 4], 2))  # Output: 12 ([3, 4])


# ----------------------------------------------------------------------------------
# Solution Output:
