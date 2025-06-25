# Subarray Manipulation: Max Subarray Sum
"""
Task: Find the maximum sum of a contiguous subarray.
    - Input is a non-empty array of integers

Example 1: [-2, 7, -3, 4] → 8 (from [7, -3, 4])
Example 2: [1] → 1

Why: Introduces Kadane’s algorithm for efficient subarray sum calculation.

https://www.youtube.com/watch?v=hLPkqd60-28
"""

def max_subarray_sum(arr):
    # Initialize max_sum to a very small number
    max_sum = float('-inf')
    current_sum = 0
    
    # Loop through the array
    for num in arr:
        current_sum += num

        # Update max_sum if the current_sum is larger
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0
    
    # Return the maximum sum
    return max_sum

print(max_subarray_sum([-2, 7, -3, 4]))  # Output: 8


"""
Simple Breakdown
    - Uses Kadane’s algorithm to track the maximum sum ending at each position.
    - Time Complexity: O(n), Space Complexity: O(1).
    - Efficient and fundamental for subarray problems.


'-inf' Explained:
    
    is a string that Python uses to mean "negative infinity," a super tiny number smaller than any other number. 

    When we write float('-inf'), Python turns that string into a number so small it’s like the lowest possible score. 

    It’s in quotes because '-inf' is like a word that Python understands as "make this a huge negative number."
"""


# ----------------------------------------------------------------------------------
# Task: Find the maximum sum of a contiguous subarray in a non-empty array of integers.

def max_subarray_sum(arr):  # Example: arr = [-2, 7, -3, 4]

    # 1️⃣ Initialize variables
    # Set max_sum to a very small number to handle negative sums
    # Why? We need to track the largest sum found, and this ensures any sum is larger initially
    max_sum = float('-inf')  # max_sum = -∞

    # Initialize current_sum to track the sum of the subarray ending at the current position
    # Why? Kadane’s algorithm builds subarrays by adding elements and decides whether to reset
    current_sum = 0  # current_sum = 0

    # 2️⃣ Loop through the array
    # Iterate through each number in the array
    # Why? We process each element to build and evaluate subarrays
    for num in arr:  # num takes values [-2, 7, -3, 4]
        # --- Iteration 1: num = -2 ---
        # Add the current number to the current subarray sum
        # Why? We extend the subarray by including the current element
        current_sum += num  # current_sum = 0 + (-2) = -2

        # Update max_sum if the current_sum is larger
        # Why? The current_sum represents a potential maximum subarray sum ending here
        max_sum = max(max_sum, current_sum)  # max_sum = max(-∞, -2) = -2
        # Check if current_sum is negative
        # Why? If negative, it’s better to start a new subarray from the next element
        if current_sum < 0:  # current_sum = -2, -2 < 0 is true
            current_sum = 0  # current_sum = 0 (reset to start new subarray)
        # After Iteration 1: current_sum = 0, max_sum = -2

        # --- Iteration 2: num = 7 ---
        if num == 7:
            current_sum += num  # current_sum = 0 + 7 = 7
            max_sum = max(max_sum, current_sum)  # max_sum = max(-2, 7) = 7
            if current_sum < 0:  # current_sum = 7, 7 < 0 is false, skip
                current_sum = 0
            # After Iteration 2: current_sum = 7, max_sum = 7
            # Current subarray: [7] (sum = 7)

        # --- Iteration 3: num = -3 ---
        if num == -3:
            current_sum += num  # current_sum = 7 + (-3) = 4
            max_sum = max(max_sum, current_sum)  # max_sum = max(7, 4) = 7
            if current_sum < 0:  # current_sum = 4, 4 < 0 is false, skip
                current_sum = 0
            # After Iteration 3: current_sum = 4, max_sum = 7
            # Current subarray: [7, -3] (sum = 4)

        # --- Iteration 4: num = 4 ---
        if num == 4:
            current_sum += num  # current_sum = 4 + 4 = 8
            max_sum = max(max_sum, current_sum)  # max_sum = max(7, 8) = 8
            if current_sum < 0:  # current_sum = 8, 8 < 0 is false, skip
                current_sum = 0
            # After Iteration 4: current_sum = 8, max_sum = 8
            # Current subarray: [7, -3, 4] (sum = 8)

    # 3️⃣ Return the maximum sum
    # Why? max_sum contains the largest sum of any contiguous subarray
    return max_sum  # max_sum = 8

print(max_subarray_sum([-2, 7, -3, 4]))  # Output: 8



# ----------------------------------------------------------------------------------
# Textbook Kadane solution
def max_subarray_sum(arr):    
    # 1️⃣ Initialize current and global max sums with first element
    max_current = max_global = arr[0]
    
    # 2️⃣ Iterate through array, applying Kadane’s algorithm
    for num in arr[1:]:
        max_current = max(num, max_current + num)  # Choose between starting new or extending
        if max_current > max_global:
            max_global = max_current  # Update global max if current is larger
    
    # 3️⃣ Return the maximum subarray sum
    return max_global

print(max_subarray_sum([-2, 7, -3, 4]))  # Output: 8

