# Max Consecutive Ones III

"""
Task: Given a binary array and an integer K, return the maximum number of consecutive 1's if you can flip at most K 0's.
Example 1: nums = [1,1,0,0,1,1,0], K = 2 → Output = 6 (flip 0's at indices 2 and 3)
Example 2: nums = [0,0,1,1,0,1], K = 1 → Output = 4 (flip 0 at index 4)
Example 3: nums = [1,1,1,1], K = 1 → Output = 4 (no flip needed)
"""

def longestOnes(nums, K):
    # 1️⃣ Initialize pointers & tracking variables
    left = 0
    max_length = 0
    zero_count = 0
    
    # 2️⃣ Expand window by moving `right` & update conditions
    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        
        # 3️⃣ Shrink window when condition is violated (more than K zeros)
        while zero_count > K and left <= right:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        
        # 4️⃣ Update result with current window
        current_length = right - left + 1
        max_length = max(max_length, current_length)
    
    # 5️⃣ Return final result
    return max_length

print(longestOnes([1,1,0,0,1,1,0], 2))  # Output: 6


# ----------------------------------------------------------------------------------
# Solution FULL Breakdown

"""
Task: Given a binary array and an integer K, return the maximum number of consecutive 1's if you can flip at most K 0's.
Example for Breakdown: nums = [1,1,0,0,1,1,0], K = 2 → Output = 6 (flip 0's at indices 2 and 3)
"""

def longestOnes(nums, K):    # Example: nums = [1,1,0,0,1,1,0], K = 2

    # 1️⃣ Initialize pointers & tracking variables
    # Initialize left pointer for the start of our sliding window
    # Why? We'll move this to shrink the window when we have too many zeros
    left = 0                       # left = 0 (start at beginning)

    # Track the longest subarray length with at most K zeros
    # Why? We need to update this whenever we find a longer valid subarray
    max_length = 0                 # max_length = 0 (no subarray checked yet)

    # Track the number of zeros in the current window
    # Why? We need to ensure the window has at most K zeros
    zero_count = 0                 # zero_count = 0 (no zeros yet)

    # 2️⃣ Expand window by moving `right` & update conditions
    # Loop through each element as the right end of our window
    # Why? We check each element to build subarrays with at most K zeros
    for right in range(len(nums)):  # right goes from 0 to 6 for [1,1,0,0,1,1,0]
        # --- Iteration 0: right = 0, nums[0] = 1 ---
        # If the current element is 0, increment the zero count
        # Why? We need to track how many zeros are in the window
        if nums[right] == 0:        # nums[0] = 1 == 0 → false, skip
            zero_count += 1         # zero_count remains 0

        # 3️⃣ Shrink window when condition is violated (more than K zeros)
        # While the number of zeros exceeds K and the window is valid
        # Why? We need to maintain at most K zeros in the window
        while zero_count > K and left <= right:  # 0 > 2 is false, skip
            # If the element at left is 0, decrement the zero count
            # Why? We're removing this element from the window
            if nums[left] == 0:
                zero_count -= 1
            # Move the left pointer forward
            # Why? Shrink the window from the left
            left += 1

        # 4️⃣ Update result with current window
        # Calculate the size of the current window
        # Why? This is the length of our current subarray
        current_length = right - left + 1  # 0 - 0 + 1 = 1
        # Update the maximum length if the current window is larger
        # Why? We want the longest subarray with at most K zeros
        max_length = max(max_length, current_length)  # max(0, 1) = 1
        # After Iteration 0: left = 0, zero_count = 0, max_length = 1
        # Current window: [1] (length 1, 0 zeros)

        # --- Iteration 1: right = 1, nums[1] = 1 ---
        if right == 1:
            if nums[right] == 0:    # nums[1] = 1 == 0 → false
                zero_count += 1     # zero_count remains 0
            while zero_count > K and left <= right:  # 0 > 2 is false, skip
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            current_length = right - left + 1  # 1 - 0 + 1 = 2
            max_length = max(max_length, current_length)  # max(1, 2) = 2
            # After Iteration 1: left = 0, zero_count = 0, max_length = 2
            # Current window: [1,1] (length 2, 0 zeros)

        # --- Iteration 2: right = 2, nums[2] = 0 ---
        if right == 2:
            if nums[right] == 0:    # nums[2] = 0 == 0 → true
                zero_count += 1     # zero_count = 1
            while zero_count > K and left <= right:  # 1 > 2 is false, skip
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            current_length = right - left + 1  # 2 - 0 + 1 = 3
            max_length = max(max_length, current_length)  # max(2, 3) = 3
            # After Iteration 2: left = 0, zero_count = 1, max_length = 3
            # Current window: [1,1,0] (length 3, 1 zero)

        # --- Iteration 3: right = 3, nums[3] = 0 ---
        if right == 3:
            if nums[right] == 0:    # nums[3] = 0 == 0 → true
                zero_count += 1     # zero_count = 2
            while zero_count > K and left <= right:  # 2 > 2 is false, skip
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            current_length = right - left + 1  # 3 - 0 + 1 = 4
            max_length = max(max_length, current_length)  # max(3, 4) = 4
            # After Iteration 3: left = 0, zero_count = 2, max_length = 4
            # Current window: [1,1,0,0] (length 4, 2 zeros)

        # --- Iteration 4: right = 4, nums[4] = 1 ---
        if right == 4:
            if nums[right] == 0:    # nums[4] = 1 == 0 → false
                zero_count += 1     # zero_count remains 2
            while zero_count > K and left <= right:  # 2 > 2 is false, skip
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            current_length = right - left + 1  # 4 - 0 + 1 = 5
            max_length = max(max_length, current_length)  # max(4, 5) = 5
            # After Iteration 4: left = 0, zero_count = 2, max_length = 5
            # Current window: [1,1,0,0,1] (length 5, 2 zeros)

        # --- Iteration 5: right = 5, nums[5] = 1 ---
        if right == 5:
            if nums[right] == 0:    # nums[5] = 1 == 0 → false
                zero_count += 1     # zero_count remains 2
            while zero_count > K and left <= right:  # 2 > 2 is false, skip
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            current_length = right - left + 1  # 5 - 0 + 1 = 6
            max_length = max(max_length, current_length)  # max(5, 6) = 6
            # After Iteration 5: left = 0, zero_count = 2, max_length = 6
            # Current window: [1,1,0,0,1,1] (length 6, 2 zeros)

        # --- Iteration 6: right = 6, nums[6] = 0 ---
        if right == 6:
            if nums[right] == 0:    # nums[6] = 0 == 0 → true
                zero_count += 1     # zero_count = 3
            while zero_count > K and left <= right:  # 3 > 2 and 0 <= 6 → true
                if nums[left] == 0:  # nums[0] = 1 == 0 → false
                    zero_count -= 1  # skip
                left += 1            # left = 1
                # Check again: 3 > 2 and 1 <= 6 → true
                if nums[left] == 0:  # nums[1] = 1 == 0 → false
                    zero_count -= 1  # skip
                left += 1            # left = 2
                # Check again: 3 > 2 and 2 <= 6 → true
                if nums[left] == 0:  # nums[2] = 0 == 0 → true
                    zero_count -= 1  # zero_count = 2
                left += 1            # left = 3

                # Check again: 2 > 2 is false, exit while

            current_length = right - left + 1  # 6 - 3 + 1 = 4
            max_length = max(max_length, current_length)  # max(6, 4) = 6
            # After Iteration 6: left = 3, zero_count = 2, max_length = 6
            # Current window: [0,1,1,0] (from index 3 to 6, length 4, 2 zeros)

    # 5️⃣ Return final result
    # Return the length of the longest subarray found
    return max_length                  # max_length = 6


print(longestOnes([1,1,0,0,1,1,0], 2))  # Output: 6