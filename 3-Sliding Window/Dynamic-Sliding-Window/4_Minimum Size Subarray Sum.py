# Minimum Size Subarray Sum

"""
Task: Given an array of positive integers nums and a positive integer S, find the length of the smallest contiguous subarray whose sum is at least S (sum >= S). If no such subarray exists, return 0.

Example 1: nums = [1,3,4,3,1], S = 7 → Output = 2 (subarray [4,3])
Example 2: nums = [1,2,3,4,5], S = 15 → Output = 5 (subarray [1,2,3,4,5])
Example 3: nums = [1,2,3], S = 10 → Output = 0 (no subarray sums to 10 or more)
Example 4: nums = [1,2,10], S = 6 → Output: 1 (subarray [10] sums to 10)
"""

def minSubArrayLen(S, nums):
    # 1️⃣ Initialize pointers & tracking variables
    left = 0
    min_length = float('inf')  # Use infinity to handle no valid subarray case
    current_sum = 0
    
    # 2️⃣ Expand window by moving `right` & update conditions
    for right in range(len(nums)):
        current_sum += nums[right]
        
        # 3️⃣ Shrink window when condition is satisfied (sum >= S)
        while current_sum >= S and left <= right:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1
    
    # 5️⃣ Return final result
    return min_length if min_length != float('inf') else 0

print(minSubArrayLen(7, [2,3,1,2,4,3]))  # Output: 2


# ----------------------------------------------------------------------------------
# Solution FULL Breakdown

"""
Task: Given an array of positive integers nums and a positive integer S, find the length of the smallest contiguous subarray whose sum is at least S (sum >= S). If no such subarray exists, return 0.
Example for Breakdown: nums = [1,3,4,3,1], S = 7 → Output = 2 (subarray [4,3])
"""

def minSubArrayLen(S, nums):    # Example: S = 7, nums = [1,3,4,3,1]

    # 1️⃣ Initialize pointers & tracking variables
    # Initialize left pointer for the start of our sliding window
    # Why? We'll move this to shrink the window when the sum condition is met
    left = 0                       # left = 0 (start at beginning)

    # Track the smallest subarray length that meets the condition
    # Why? We need to find the minimum length, so we start with a large value
    min_length = float('inf')      # min_length = infinity (to handle no valid subarray)

    # Track the current sum of the window
    # Why? We need to check if the sum is at least S
    current_sum = 0                # current_sum = 0 (no elements yet)

    # 2️⃣ Expand window by moving `right` & update conditions
    # Loop through each element as the right end of our window
    # Why? We check each element to build subarrays with sum >= S
    for right in range(len(nums)):  # right goes from 0 to 4 for [1,3,4,3,1]
        # --- Iteration 0: right = 0, nums[0] = 1 ---
        # Add the current element to the sum
        # Why? We're expanding the window to include this element
        current_sum += nums[right]     # current_sum = 0 + 1 = 1

        # 3️⃣ Shrink window when condition is satisfied (sum >= S)
        # While the current sum is greater than or equal to S and the window is valid
        # Why? We want the smallest subarray, so we shrink from the left
        while current_sum >= S and left <= right:  # 1 >= 7 is false, skip
            # Update the minimum length with the current window size
            # Why? This is a valid subarray, so we check if it's the smallest
            min_length = min(min_length, right - left + 1)
            # Subtract the element at left from the sum
            # Why? We're removing this element to shrink the window
            current_sum -= nums[left]
            # Move the left pointer forward
            # Why? Shrink the window from the left
            left += 1

        # After Iteration 0: left = 0, current_sum = 1, min_length = infinity
        # Current window: [1] (sum = 1 < 7)

        # --- Iteration 1: right = 1, nums[1] = 3 ---
        if right == 1:
            current_sum += nums[right]     # current_sum = 1 + 3 = 4
            while current_sum >= S and left <= right:  # 4 >= 7 is false, skip
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
            # After Iteration 1: left = 0, current_sum = 4, min_length = infinity
            # Current window: [1,3] (sum = 4 < 7)

        # --- Iteration 2: right = 2, nums[2] = 4 ---
        if right == 2:
            current_sum += nums[right]     # current_sum = 4 + 4 = 8
            while current_sum >= S and left <= right:  # 8 >= 7 and 0 <= 2 → true
                # Update min_length with current window size
                min_length = min(min_length, 2 - 0 + 1)  # min(inf, 3) = 3
                # Subtract nums[left] = 1 from sum
                current_sum -= nums[left]     # current_sum = 8 - 1 = 7
                # Move left to 1
                left += 1                     # left = 1
                # Check again: 7 >= 7 and 1 <= 2 → true
                min_length = min(min_length, 2 - 1 + 1)  # min(3, 2) = 2
                current_sum -= nums[left]     # current_sum = 7 - 3 = 4
                left += 1                     # left = 2
                # Check again: 4 >= 7 is false, exit while
            # After Iteration 2: left = 2, current_sum = 4, min_length = 2
            # Current window: [4] (sum = 4 < 7)

        # --- Iteration 3: right = 3, nums[3] = 3 ---
        if right == 3:
            current_sum += nums[right]     # current_sum = 4 + 3 = 7
            while current_sum >= S and left <= right:  # 7 >= 7 and 2 <= 3 → true
                # Update min_length with current window size
                min_length = min(min_length, 3 - 2 + 1)  # min(2, 2) = 2
                # Subtract nums[left] = 4 from sum
                current_sum -= nums[left]     # current_sum = 7 - 4 = 3
                # Move left to 3
                left += 1                     # left = 3
                # Check again: 3 >= 7 is false, exit while
            # After Iteration 3: left = 3, current_sum = 3, min_length = 2
            # Current window: [3] (sum = 3 < 7)

        # --- Iteration 4: right = 4, nums[4] = 1 ---
        if right == 4:
            current_sum += nums[right]     # current_sum = 3 + 1 = 4
            while current_sum >= S and left <= right:  # 4 >= 7 is false, skip
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
            # After Iteration 4: left = 3, current_sum = 4, min_length = 2
            # Current window: [3,1] (sum = 4 < 7)

    # 5️⃣ Return final result
    # If min_length was updated, return it; otherwise, return 0
    return min_length if min_length != float('inf') else 0  # min_length = 2


print(minSubArrayLen(7, [1,3,4,3,1]))  # Output: 2 (subarray [4,3])
