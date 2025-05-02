# Maximum Product of K Consecutive Elements
"""
Task: Given an integer array nums and an integer k, find the maximum product of any contiguous subarray of size k. If the array has fewer than k elements, return None.
Example 1: [1, 2, 3],    k = 2 → 6 ([2, 3])
Example 1: [1, 2, 3, 4], k = 2 → 12 ([3, 4])
Example 3: [2, 3, 4, 5], k = 2 → 20 ([4, 5])
"""

def max_product_sliding_window(arr, k):

    # Input Validation 
    if len(arr) < k:
        return None
    
    # Initialize
    window_product = 1

    # Initialize the first window
    for i in range(k):         # i = 0, 1
        window_product *= arr[i]   #  window_product = 1*1=1 | 1*2=2
    
    max_result = window_product    # max_result = 2

    # Slide the window across the array
    for i in range(k, len(arr)):  # i = 2
        window_product = window_product // arr[i - k] * arr[i]  # 2 / 1 * 3 = 6
        max_result = max(max_result, window_product)
    
    return max_result


print(max_product_sliding_window([1, 2, 3], 2))       # Output: 6 ([2, 3])
print(max_product_sliding_window([1, 2, 3, 4], 2))    # Output: 12 ([3, 4])
print(max_product_sliding_window([2, 3, 4, 5], 2))    # Output: 20 ([4, 5])


"""
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

def max_product_sliding_window(arr, k):    # Example: arr = [1, 2, 3], k = 2
    # Check if the array is too short to have a subarray of size k
    if len(arr) < k:                       # len(arr) = 3, k = 2, so 3 >= 2, skip this
        # Return None since no subarrays of size k are possible
        return None                        # skip
    
    # Initialize a variable to hold the product of the window
    # Why? We need a starting point to multiply numbers
    window_product = 1                 # window_product = 1 (neutral for multiplication)
    
    # Multiply the first k numbers to get the first window's product
    # Why? This is the first possible product we can check
    for i in range(k):                 # k = 2, so i goes from 0 to 1
                                       # i = 0
        window_product *= arr[i]       # window_product = 1 * arr[0] = 1 * 1 = 1
                                       # i = 1
        window_product *= arr[i]       # window_product = 1 * arr[1] = 1 * 2 = 2
    
    # Set the maximum product to our first window's product
    # Why? It's the biggest product we know so far (we just started!)
    max_result = window_product        # max_result = 2 (first window [1, 2])
    
    # Slide the window across the array, one step at a time
    # Why? To check every possible group of k numbers
    for i in range(k, len(arr)):       # k = 2, len(arr) = 3, so i goes from 2 to 2
                                       # Iteration 1: i = 2
        # Update the product: divide out the old number, multiply by the new one
        # Why? This slides our window over by one spot efficiently
        window_product = window_product // arr[i - k] * arr[i]  # arr[2] = 3, arr[2-2] = arr[0] = 1
                                                               # window_product = (2 // 1) * 3 = 2 * 3 = 6 (new window [2, 3])
        
        # Update the maximum if our new product is bigger
        # Why? We want the biggest product we find across all windows
        max_result = max(max_result, window_product)  # max(2, 6) = 6, so max_result = 6
    
    # Give back the biggest product we found
    return max_result                  # max_result = 6 (from window [2, 3])


print(max_product_sliding_window([1, 2, 3], 2))  # Output: 6 ([2, 3] has product = 2 * 3 = 6)


"""
Explanation: window_product = window_product // arr[i - k] * arr[i]

The line `window_product = window_product // arr[i - k] * arr[i]` updates the product of a sliding window by removing the old element (`arr[i - k]`) and adding the new one (`arr[i]`). For example, if the current product is 2 (from `[1,2]`), the old element is 1, and the new element is 3, it does `(2 // 1) * 3 = 6` (new window `[2,3]`).

Why it works:
    - Product update: To slide the window, you divide by the element leaving (`arr[i - k]`) and multiply by the element entering (`arr[i]`). This keeps the product correct for the new window.
    - Integer division (`//`): Uses `//` to keep results as integers (since inputs are integers). For example, `2 // 1 = 2`, which is the same as regular division here.
    - How it’s done: First divides (`window_product // arr[i - k]`), then multiplies by `arr[i]` to get the new product.

Why different from sum:
    - For sums, you use `window_sum += arr[i] - arr[i - k]` because you add the new element and subtract the old one to update the sum. For products, adding/subtracting doesn’t work—you need to multiply and divide to adjust the product correctly.
"""

# ----------------------------------------------------------------------------------
# Solution Output:

def max_product_sliding_window(arr, k):    # arr = [1, 2, 3], k = 2
    # Input Validation 
    if len(arr) < k:                      # Is len(arr) = 3 < k = 2? No
        return None                       # Skip
    
    # Initialize
    window_product = 1                    # Starting product for the window

    # Set up the initial window
    for i in range(k):                    # i = 0 to 1
        window_product *= arr[i]          # i=0: 1 * arr[0] = 1 * 1 = 1
                                          # i=1: 1 * arr[1] = 1 * 2 = 2 (window [1,2])
    
    max_result = window_product           # max_result = 2 (product of [1,2])

    # Slide the window across the array
    for i in range(k, len(arr)):          # i = 2 to 2
                                          # Iteration 1: i = 2
        window_product = window_product // arr[i - k] * arr[i]  # window_product = (2 // arr[0]) * arr[2] = (2 // 1) * 3 = 2 * 3 = 6 (window [2,3])
        max_result = max(max_result, window_product)  # max(2, 6) = 6, max_result = 6
    
    return max_result                     # Return 6 (highest product found, from [2,3])

print(max_product_sliding_window([1, 2, 3], 2))  # Output: 6 ([2, 3])


# ----------------------------------------------------------------------------------
# Solution Output:

def max_product_sliding_window(arr, k):    # arr = [1, 2, 3, 4], k = 2
    # Input Validation 
    if len(arr) < k:                      # Is len(arr) = 4 < k = 2? No
        return None                       # Skip
    
    # Initialize
    window_product = 1                    # Starting product for the window

    # Set up the initial window
    for i in range(k):                    # i = 0 to 1
        window_product *= arr[i]          # i=0: 1 * arr[0] = 1 * 1 = 1
                                          # i=1: 1 * arr[1] = 1 * 2 = 2 (window [1,2])
    
    max_result = window_product           # max_result = 2 (product of [1,2])

    # Slide the window across the array
    for i in range(k, len(arr)):          # i = 2 to 3
                                          # Iteration 1: i = 2
        window_product = window_product // arr[i - k] * arr[i]  # window_product = (2 // arr[0]) * arr[2] = (2 // 1) * 3 = 2 * 3 = 6 (window [2,3])
        max_result = max(max_result, window_product)  # max(2, 6) = 6, max_result = 6
                                          # Iteration 2: i = 3
        window_product = window_product // arr[i - k] * arr[i]  # window_product = (6 // arr[1]) * arr[3] = (6 // 2) * 4 = 3 * 4 = 12 (window [3,4])
        max_result = max(max_result, window_product)  # max(6, 12) = 12, max_result = 12
    
    return max_result                     # Return 12 (highest product found, from [3,4])

print(max_product_sliding_window([1, 2, 3, 4], 2))  # Output: 12 ([3, 4])

# ----------------------------------------------------------------------------------
# Solution Output:

def max_product_sliding_window(arr, k):    # arr = [2, 3, 4, 5], k = 2
    # Input Validation 
    if len(arr) < k:                      # Is len(arr) = 4 < k = 2? No
        return None                       # Skip
    
    # Initialize
    window_product = 1                    # Starting product for the window

    # Set up the initial window
    for i in range(k):                    # i = 0 to 1
        window_product *= arr[i]          # i=0: 1 * arr[0] = 1 * 2 = 2
                                          # i=1: 2 * arr[1] = 2 * 3 = 6 (window [2,3])
    
    max_result = window_product           # max_result = 6 (product of [2,3])

    # Slide the window across the array
    for i in range(k, len(arr)):          # i = 2 to 3
                                          # Iteration 1: i = 2
        window_product = window_product // arr[i - k] * arr[i]  # window_product = (6 // arr[0]) * arr[2] = (6 // 2) * 4 = 3 * 4 = 12 (window [3,4])
        max_result = max(max_result, window_product)  # max(6, 12) = 12, max_result = 12
                                          # Iteration 2: i = 3
        window_product = window_product // arr[i - k] * arr[i]  # window_product = (12 // arr[1]) * arr[3] = (12 // 3) * 5 = 4 * 5 = 20 (window [4,5])
        max_result = max(max_result, window_product)  # max(12, 20) = 20, max_result = 20
    
    return max_result                     # Return 20 (highest product found, from [4,5])

print(max_product_sliding_window([2, 3, 4, 5], 2))  # Output: 20 ([4, 5])
