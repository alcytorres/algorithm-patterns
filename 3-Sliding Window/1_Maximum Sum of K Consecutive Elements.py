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
Task: Find the maximum sum of any k consecutive elements in an array. ***If the length of the array is
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
    window_sum = sum(arr[:k])  # Sum of first window

    # 3️⃣ Initialize maximum sum
    max_sum = window_sum

    # 4️⃣ Iterate through remaining windows
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]  # Slide window
        max_sum = max(max_sum, window_sum)

    # 5️⃣ Return the maximum sum
    return max_sum

print(max_sum_k_consecutive([1, 2, 3], 2))  # Output: 5 (2 + 3)
print(max_sum_k_consecutive([1, 2, 3, 4], 2))  # Output: 7 (3 + 4)


# Simple Breakdown
def max_sum_k_consecutive(arr, k):   # Define the function that takes an array 'arr' and integer 'k'
    """
    Finds the maximum sum of any k consecutive elements.
    
    - Uses a fixed-size sliding window to compute sums efficiently.
    - Time Complexity: O(n), Space Complexity: O(1).
    - Sliding window is intuitive and beginner-friendly for fixed sizes.
    """
    # 1️⃣ Check if array length is sufficient
    if len(arr) < k:       # Check if the array is shorter than 'k'
        return None        # Return None since we can't form a window of size 'k'
    
    # 2️⃣ Initialize window sum for first k elements
    window_sum = sum(arr[:k])  # Calculate the sum of the first k elements (first window)

    # 3️⃣ Initialize maximum sum
    max_sum = window_sum   # Set the initial maximum sum to the first window's sum

    # 4️⃣ Iterate through remaining windows
    for i in range(k, len(arr)):  # Loop from index k to the end of the array
        window_sum = window_sum - arr[i - k] + arr[i]  # Slide the window: subtract the leftmost element, add the new right element
        max_sum = max(max_sum, window_sum)  # Update max_sum if the current window sum is larger

    # 5️⃣ Return the maximum sum
    return max_sum         # Return the maximum sum found


print(max_sum_k_consecutive([1, 2, 3], 2))  # Output: 5 (2 + 3)


# ----------------------------------------------------------------------------------
# Solution with output Full Breakdown 

def max_sum_k_consecutive(arr, k):  # Example: arr = [1, 4, 6, 2], k = 2

    # 1️⃣ Check if array length is sufficient
    # Verify if the array has at least k elements
    # Why? If len(arr) < k, no subarray of size k is possible
    if len(arr) < k:               # len(arr) = 4, k = 2, 4 < 2 → False
        return None                # Skip (array length is sufficient)
    # After check: Proceed since len(arr) >= k

    # 2️⃣ Initialize window sum for first k elements
    # Compute the sum of the first k elements
    # Why? This is the sum of the first consecutive k-element window
    window_sum = sum(arr[:k])      # arr[:2] = [1, 4], window_sum = 1 + 4 = 5
    # After computation: window_sum = 5 (sum of arr[0:2] = [1, 4])

    # 3️⃣ Initialize maximum sum
    # Set max_sum to the first window's sum
    # Why? The first window is our initial candidate for the maximum sum
    max_sum = window_sum           # max_sum = 5
    # After initialization: max_sum = 5, representing sum of first window [1, 4]

    # 4️⃣ Iterate through remaining windows
    # Loop through array to compute sums of subsequent k-sized windows
    # Why? We slide the window and compare sums to find the maximum
    for i in range(k, len(arr)):   # k = 2, len(arr) = 4, range(2, 4) → i = 2, 3
        
        # --- Iteration 1: i = 2 ---
        # Slide window by removing first element of previous window and adding current element
        # Why? This efficiently updates the sum for the new k-element window
        window_sum = window_sum - arr[i - k] + arr[i]  # i = 2, i - k = 2 - 2 = 0
                                                       # arr[0] = 1, arr[2] = 6
                                                       # window_sum = 5 - 1 + 6 = 10
                                                       # (sum of arr[1:3] = [4, 6])
        
        # Update max_sum if current window_sum is larger
        # Why? We want the largest sum among all k-sized subarrays
        max_sum = max(max_sum, window_sum)  # max(5, 10) = 10
                                            # max_sum = 10
        # After Iteration 1: i = 2, max_sum = 10
        # Current window: [4, 6], sum = 10

        # --- Iteration 2: i = 3 ---
        if i == 3:                          # Check for clarity
            window_sum = window_sum - arr[i - k] + arr[i]  # i = 3, i - k = 3 - 2 = 1
                                                           # arr[1] = 4, arr[3] = 2
                                                           # window_sum = 10 - 4 + 2 = 8
                                                           # (sum of arr[2:4] = [6, 2])
            max_sum = max(max_sum, window_sum)  # max(10, 8) = 10
                                                # max_sum = 10
        # After Iteration 2: i = 3, max_sum = 10
        # Current window: [6, 2], sum = 8

    # 5️⃣ Return the maximum sum
    # Why? max_sum is the largest sum of any k consecutive elements
    return max_sum                 # Return max_sum = 10
    # Final state: max_sum = 10 (from subarray [4, 6])
    # Conclusion: Successfully found maximum sum of k=2 consecutive elements

print(max_sum_k_consecutive([1, 4, 6, 2], 2))  # Output: 10 (4 + 6)



# ----------------------------------------------------------------------------------
# Solution with output 

def max_sum_k_consecutive(arr, k):  # Example: arr = [1, 2, 3, 4, 5], k = 3

    # 1️⃣ Check if array length is sufficient
    # Verify if the array has at least k elements
    if len(arr) < k:               # len(arr) = 5, k = 3, 5 < 3 → False
        return None                # Skip (array length is sufficient)
    # After check: Proceed since len(arr) >= k

    # 2️⃣ Initialize window sum for first k elements
    # Compute the sum of the first k elements
    window_sum = sum(arr[:k])      # arr[:3] = [1, 2, 3], window_sum = 1 + 2 + 3 = 6
    # After computation: window_sum = 6 (sum of arr[0:3] = [1, 2, 3])

    # 3️⃣ Initialize maximum sum
    # Set max_sum to the first window's sum
    max_sum = window_sum           # max_sum = 6
    # After initialization: max_sum = 6, representing sum of first window [1, 2, 3]

    # 4️⃣ Iterate through remaining windows
    # Loop through array to compute sums of subsequent k-sized windows
    for i in range(k, len(arr)):   # k = 3, len(arr) = 5, range(3, 5) → i = 3, 4
        
        # --- Iteration 1: i = 3 ---
        # Slide window by removing first element of previous window and adding current element
        window_sum = window_sum - arr[i - k] + arr[i]  # i = 3, i - k = 3 - 3 = 0
                                                       # arr[0] = 1, arr[3] = 4
                                                       # window_sum = 6 - 1 + 4 = 9
                                                       # (sum of arr[1:4] = [2, 3, 4])
        
        # Update max_sum if current window_sum is larger
        max_sum = max(window_sum, max_sum)  # max(9, 6) = 9
                                            # max_sum = 9
        # After Iteration 1: i = 3, max_sum = 9
        # Current window: [2, 3, 4], sum = 9

        # --- Iteration 2: i = 4 ---
        if i == 4:                          # Check for clarity
            window_sum = window_sum - arr[i - k] + arr[i]  # i = 4, i - k = 4 - 3 = 1
                                                           # arr[1] = 2, arr[4] = 5
                                                           # window_sum = 9 - 2 + 5 = 12
                                                           # (sum of arr[2:5] = [3, 4, 5])
            max_sum = max(window_sum, max_sum)  # max(12, 9) = 12
                                                # max_sum = 12
        # After Iteration 2: i = 4, max_sum = 12
        # Current window: [3, 4, 5], sum = 12

    # 5️⃣ Return the maximum sum
    return max_sum                 # Return max_sum = 12
    # Final state: max_sum = 12 (from subarray [3, 4, 5])

print(max_sum_k_consecutive([1, 2, 3, 4, 5], 3))  # Output: 12 (3 + 4 + 5)