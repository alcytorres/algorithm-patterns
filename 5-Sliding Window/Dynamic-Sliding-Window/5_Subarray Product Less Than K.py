# Subarray Product Less Than K

"""
Task: Given an array of positive integers nums and an integer K, count the number of contiguous subarrays where the product of all elements is less than K.

Example 1: nums = [1,2,3], K = 10 → Output = 6 ([1], [2], [3], [1,2], [2,3], [1,2,3])
Example 2: nums = [1,2], K = 3 → Output: 3 (subarrays: [1], [2], [1,2])
Example 3: nums = [5], K = 10 → Output: 1 (subarray: [5])
Example 4: nums = [2,2], K = 4 → Output: 4 (subarrays: [2], [2], [2,2], [2,2])
Example 5: nums = [2,3], K = 6 → Output: 3 (subarrays: [2], [3], [2,3])
"""

def numSubarrayProductLessThanK(nums, K):
    if K <= 1:
        return 0  # No product of positive integers is less than 1
    # 1️⃣ Initialize pointers & tracking variables
    left = 0
    product = 1
    count = 0
    
    # 2️⃣ Expand window by moving `right` & update conditions
    for right in range(len(nums)):
        product *= nums[right]
        
        # 3️⃣ Shrink window when condition is violated (product >= K)
        while product >= K and left <= right:
            product /= nums[left]
            left += 1
        
        # 4️⃣ Update result with current window
        count += (right - left + 1)  # Number of subarrays ending at right
    
    # 5️⃣ Return final result
    return count

print(numSubarrayProductLessThanK([10,5,2,6], 100))  # Output: 8


# ----------------------------------------------------------------------------------
# Solution FULL Breakdown

# Subarray Product Less Than K

"""
Task: Given an array of positive integers nums and an integer K, count the number of contiguous subarrays where the product of all elements is less than K.
Example for Breakdown: nums = [1,2,3], K = 10 → Output = 6 ([1], [2], [3], [1,2], [2,3], [1,2,3])
"""

def numSubarrayProductLessThanK(nums, K):    # Example: nums = [1,2,3], K = 10

    # 1️⃣ Initialize pointers & tracking variables
    # Initialize left pointer for the start of our sliding window
    # Why? We'll move this to shrink the window when the product condition is violated
    left = 0                       # left = 0 (start at beginning)

    # Track the current product of the window
    # Why? We need to check if the product is less than K
    product = 1                    # product = 1 (initially no elements)

    # Track the count of valid subarrays
    # Why? This is the result we need to return
    count = 0                      # count = 0 (no subarrays yet)

    # Edge case: if K <= 1, no subarray of positive integers has product < K
    if K <= 1:
        return 0                   # Return 0 since all products are >= 1

    # 2️⃣ Expand window by moving `right` & update conditions
    # Loop through each element as the right end of our window
    # Why? We check each element to build subarrays with product < K
    for right in range(len(nums)):  # right goes from 0 to 2 for [1,2,3]
        # --- Iteration 0: right = 0, nums[0] = 1 ---
        # Multiply the current element to the product
        # Why? We're expanding the window to include this element
        product *= nums[right]     # product = 1 * 1 = 1

        # 3️⃣ Shrink window when condition is violated (product >= K)
        # While the product is greater than or equal to K and the window is valid
        # Why? We need to maintain the product less than K
        while product >= K and left <= right:  # 1 >= 10 is false, skip
            # Divide the product by the element at left
            # Why? We're removing this element to shrink the window
            product /= nums[left]
            # Move the left pointer forward
            # Why? Shrink the window from the left
            left += 1

        # 4️⃣ Update result with current window
        # Add the number of new subarrays ending at right
        # Why? Each new right adds (right - left + 1) new subarrays
        count += (right - left + 1)  # count = 0 + (0 - 0 + 1) = 1
        # After Iteration 0: left = 0, product = 1, count = 1
        # Current window: [1] (product = 1 < 10)
        # Subarrays so far: [1]

        # --- Iteration 1: right = 1, nums[1] = 2 ---
        if right == 1:
            product *= nums[right]     # product = 1 * 2 = 2
            while product >= K and left <= right:  # 2 >= 10 is false, skip
                product /= nums[left]
                left += 1
            count += (right - left + 1)  # count = 1 + (1 - 0 + 1) = 1 + 2 = 3
            # After Iteration 1: left = 0, product = 2, count = 3
            # Current window: [1,2] (product = 2 < 10)
            # Subarrays so far: [1], [2], [1,2]

        # --- Iteration 2: right = 2, nums[2] = 3 ---
        if right == 2:
            product *= nums[right]     # product = 2 * 3 = 6
            while product >= K and left <= right:  # 6 >= 10 is false, skip
                product /= nums[left]
                left += 1
            count += (right - left + 1)  # count = 3 + (2 - 0 + 1) = 3 + 3 = 6
            # After Iteration 2: left = 0, product = 6, count = 6
            # Current window: [1,2,3] (product = 6 < 10)
            # Subarrays so far: [1], [2], [3], [1,2], [2,3], [1,2,3]

    # 5️⃣ Return final result
    # Return the total count of valid subarrays
    return count                  # count = 6

# Run the example
print(numSubarrayProductLessThanK([1,2,3], 10))  # Output: 6
