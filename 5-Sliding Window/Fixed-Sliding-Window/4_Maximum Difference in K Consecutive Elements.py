# Maximum Difference (max -min) in K Consecutive Elements
"""
Task: Given an array of numbers and an integer k, find the maximum difference between the largest and smallest numbers in any group of k numbers that are next to each other in the list. 
    - If the array has fewer than k numbers, return None.

Example 1: [1, 2, 6], k = 2 → 4 (subarray [2, 6] has max 6, min 2, difference 6 - 2 = 4)

Example 2: [6, 2, 1], k = 2 → 4 (subarray [2, 6] has max 6, min 2, difference 6 - 2 = 4)

Example 3: [1, 2, 8, 10], k = 2 → 6 (subarray [2, 8] has max 8, min 2, difference 8 - 2 = 6)

Why: Practices sliding window technique to compute differences efficiently.
"""

def max_difference_sliding_window(arr, k):  

    # 1️⃣ Input Validation
    if len(arr) < k:                         
        return None                         
    
    # 2️⃣ Initialize the first window
    window = arr[:k]                         

    # 3️⃣ Compute initial result for first window
    max_diff = max(window) - min(window)     
    
    # 4️⃣ Slide the window across the array and update result
    for i in range(k, len(arr)):         
        window = arr[i - k + 1:i + 1]       
        current_diff = max(window) - min(window)  
        max_diff = max(max_diff, current_diff)    
    
    # 5️⃣ Return the maximum difference
    return max_diff                        


print(max_difference_sliding_window([1, 2, 6], 2))  # Output: 4 ([2, 6] has max=6, min=2, diff=6-2=4)

print(max_difference_sliding_window([1, 2, 8, 10], 2))  # Output: 6 ([2, 8] has max=8, min=2, diff=8-2=6)


"""
Simple explanation of arr[i - k + 1:i + 1]:

The line window = arr[i - k + 1:i + 1] grabs a group of k numbers from the array, sliding one step at a time. Imagine looking through a window that shows k numbers, and you move it right to see the next group. Let’s use [1, 2, 8, 10] with k = 2 to see how it works, step by step, like you’re 10.

Pattern
    Each time, window moves one step right, grabbing k=2 numbers:
    [1, 2] → [2, 8] → [8, 10].
        i - k + 1 is the start of the window, i + 1 is just past the end (Python slices stop before the end).
    For each window, we find max - min and keep the biggest difference.

It’s like sliding a magnifying glass over 2 numbers at a time, checking how far apart the biggest and smallest are!




Understanding arr[1:3] in [1, 2, 6]:

You're confused because you think arr[1:3] tries to access index 3, which seems out of bounds for an array [1, 2, 6] with indices 0, 1, 2. Here's the key:

    In Python, a slice arr[start:end] includes elements from index start up to, but not including, index end.

    So, arr[1:3] means "take elements from index 1 to index 2" (not index 3).

    For [1, 2, 6]:
        Index 1 = 2, index 2 = 6.

        arr[1:3] = [2, 6] (only indices 1 and 2, not 3).

The slice stops before index 3, so it’s not out of bounds. It grabs exactly the 2 elements at indices 1 and 2, which is why window = [2, 6] is correct.

*** Even tho there is no value at index 3 in this array [1, 2, 6] that is fine 
    arr[1:3] only cares about grabing [2, 6] i.e  Index 1 = 2, index 2 = 6 *** 


    

Walkthrough of Why `max_difference_sliding_window` Works:

    1. First Window: It takes the first `k` elements (`[1, 2]`) and computes the difference (`max(1, 2) - min(1, 2) = 2 - 1 = 1`). This is the initial `max_diff`.

    2. Slide Window: It slides the window across the array, checking each `k`-sized subarray. For `i=2`, it forms `[2, 6]`, computes `max(2, 6) - min(2, 6) = 6 - 2 = 4`, and updates `max_diff = max(1, 4) = `.

    3. Track Maximum Difference: It keeps the largest difference found. For `[1, 2, 6]`, the differences are `1` (`[1, 2]`) and `4` (`[2, 6]`), so it returns `4`.
    
"""




# ----------------------------------------------------------------------------------
# Solution Output:

# Task: Find the maximum difference (max - min) in any group of k consecutive elements in an array.If the array has fewer than k elements, return None.


def max_difference_sliding_window(arr, k):  # Example: arr = [1, 2, 8, 10], k = 2

    # 1️⃣ Input Validation
    # Check if the array has fewer than k elements
    # Why? We can't form a subarray of size k if the array is too small
    if len(arr) < k:  # len(arr) = 4, k = 2, 4 < 2 is false, proceed
        return None  # skip

    # 2️⃣ Initialize the first window
    # Take the first k elements as the initial window
    # Why? We need to compute the difference for the first subarray of size k
    window = arr[:k]  # arr[:2] = [1, 2], window = [1, 2]

    # 3️⃣ Compute initial result for first window
    # Calculate the difference between max and min of the first window
    # Why? This is the starting point for comparing differences across all windows
    max_diff = max(window) - min(window)  # max([1, 2]) = 2, min([1, 2]) = 1
                                         # max_diff = 2 - 1 = 1

    # 4️⃣ Slide the window across the array and update result
    # Iterate from index k to the end to process each subsequent window
    # Why? We slide the window one element at a time to check all k-sized subarrays
    for i in range(k, len(arr)):  # k = 2, len(arr) = 4, i goes from 2 to 3
        # --- Iteration 1: i = 2 ---
        # Get the next window of k elements
        # Why? We need the current subarray to compute its max-min difference
        window = arr[i - k + 1:i + 1]  # i = 2, i-k+1 = 2-2+1 = 1, i+1 = 3
                                       # arr[1:3] = [2, 8], window = [2, 8]

        # Compute the difference for the current window
        # Why? We need to compare this window's difference with the maximum found
        current_diff = max(window) - min(window)  # max([2, 8]) = 8, min([2, 8]) = 2
                                                 # current_diff = 8 - 2 = 6

        # Update the maximum difference if the current difference is larger
        # Why? We want the largest difference across all windows
        max_diff = max(max_diff, current_diff)  # max(1, 6) = 6
                                                # max_diff = 6
        # After Iteration 1: max_diff = 6, window = [2, 8]

        # --- Iteration 2: i = 3 ---
        if i == 3:
            # Get the next window of k elements
            window = arr[i - k + 1:i + 1]  # i = 3, i-k+1 = 3-2+1 = 2, i+1 = 4
                                           # arr[2:4] = [8, 10], window = [8, 10]

            # Compute the difference for the current window
            current_diff = max(window) - min(window)  # max([8, 10]) = 10, min([8, 10]) = 8
                                                     # current_diff = 10 - 8 = 2

            # Update the maximum difference
            max_diff = max(max_diff, current_diff)  # max(6, 2) = 6
                                                    # max_diff = 6
            # After Iteration 2: max_diff = 6, window = [8, 10]

    # 5️⃣ Return the maximum difference
    # Why? max_diff contains the largest difference found in any k-sized subarray
    return max_diff  # max_diff = 6



print(max_difference_sliding_window([1, 2, 8, 10], 2))  # Output: 6
# ([2, 8] has max=8, min=2, diff=8-2=6)



# ----------------------------------------------------------------------------------
# Solution Breakdown: Maximum Difference in K Consecutive Elements  

# Task: Find the maximum difference (max - min) in any group of k consecutive elements in an array. If the array has fewer than k elements, return None.


def max_difference_sliding_window(arr, k):  # Example: arr = [1, 2, 6], k = 2

    # 1️⃣ Input Validation
    # Check if the array has fewer than k elements
    # Why? We can't form a subarray of size k if the array is too small
    if len(arr) < k:  # len(arr) = 3, k = 2, 3 < 2 is false, proceed
        return None  # skip

    # 2️⃣ Initialize the first window
    # Take the first k elements as the initial window
    # Why? We need to compute the difference for the first subarray of size k
    window = arr[:k]  # arr[:2] = [1, 2], window = [1, 2]

    # 3️⃣ Compute initial result for first window
    # Calculate the difference between max and min of the first window
    # Why? This is the starting point for comparing differences across all windows
    max_diff = max(window) - min(window)  # max([1, 2]) = 2, min([1, 2]) = 1
                                         # max_diff = 2 - 1 = 1

    # 4️⃣ Slide the window across the array and update result
    # Iterate from index k to the end to process each subsequent window
    # Why? We slide the window one element at a time to check all k-sized subarrays
    for i in range(k, len(arr)):  # k = 2, len(arr) = 3, i goes from 2 to 2
        # --- Iteration 1: i = 2 ---
        # Get the next window of k elements
        # Why? We need the current subarray to compute its max-min difference
        window = arr[i - k + 1:i + 1]  # i = 2, i-k+1 = 2-2+1 = 1, i+1 = 3
                                       # arr[1:3] = [2, 6], window = [2, 6]

        # Compute the difference for the current window
        # Why? We need to compare this window's difference with the maximum found
        current_diff = max(window) - min(window)  # max([2, 6]) = 6, min([2, 6]) = 2
                                                 # current_diff = 6 - 2 = 4

        # Update the maximum difference if the current difference is larger
        # Why? We want the largest difference across all windows
        max_diff = max(max_diff, current_diff)  # max(1, 4) = 4
                                                # max_diff = 4
        # After Iteration 1: max_diff = 4, window = [2, 6]

    # 5️⃣ Return the maximum difference
    # Why? max_diff contains the largest difference found in any k-sized subarray
    return max_diff  # max_diff = 4


print(max_difference_sliding_window([1, 2, 6], 2))  # Output: 4
# ([2, 6] has max=6, min=2, diff=6-2=4)



# ----------------------------------------------------------------------------------
# Alternative Solution:

def max_difference_in_k_window(arr, k):
    # Edge case: Not enough elements
    if len(arr) < k:
        return None

    max_diff = float('-inf')

    # Slide the window of size k
    for i in range(len(arr) - k + 1):
        window = arr[i:i+k]                     # Get the current window
        current_max = max(window)               # Find max in the window
        current_min = min(window)               # Find min in the window
        diff = current_max - current_min        # Compute the difference
        max_diff = max(max_diff, diff)          # Update max_diff if needed

    return max_diff

print(max_difference_in_k_window([1, 2, 5], 2))      # Output: 3
print(max_difference_in_k_window([1, 4, 2, 8], 2))   # Output: 6
print(max_difference_in_k_window([1, 3, 7, 9], 3))   # Output: 8 (window [1,3,7] → diff = 6, [3,7,9] → diff = 6, [1,3,7,9] has no more)

"""
Why this works
You move a fixed-size window of size k across the array.

For each window, you just:

Find the max and min,

Compute the difference,

Track the maximum difference found.

Time complexity is O(n * k) since max() and min() are O(k) in each iteration.
"""