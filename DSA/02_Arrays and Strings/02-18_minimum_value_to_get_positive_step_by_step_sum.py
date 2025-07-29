# 1413. Minimum Value to Get Positive Step by Step Sum

# Given an array of integers nums, you start with an initial positive value startValue.

# In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

# Return the minimum positive value of startValue such that the step by step sum is never less than 1.

# Solution: https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/solutions/1513266/minimum-value-to-get-positive-step-by-step-sum/

# Video https://www.youtube.com/watch?v=QgRZcbYboxg

# Example
# Input: nums = [-3, 2, -3, 4, 2]
# Output: 5
# Step-by-step sum: startValue + nums[i]
# Track minimum running total: [-3, -1, -4, 0, 2] (min = -4)
# Minimum startValue to keep sum ≥ 1: -(-4) + 1 = 5

def minStartValue(nums):
    # We use "total" for current step-by-step total, "min_val" for minimum 
    min_val = 0
    total = 0

    # Iterate over the array and get the minimum step-by-step total.
    for num in nums:
        total += num
        min_val = min(min_val, total)

    return -min_val + 1

nums = [-3, 2, -3, 4, 2]
print(minStartValue(nums))
# Output: 5 - Returns 5 as the minimum positive startValue ensuring the step-by-step sum starting from nums[0] never falls below 1.

# Time: O(n) - In this method, we just need to traverse the array once, with O(1) operations per iteration for addition and minimum comparison.
# Space: O(1) - We just need to calculate the step-by-step total of the array and record the minimum step-by-step total, both only require constant space.



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown

def minStartValue(nums):
    # We use "total" for current step-by-step total, "min_val" for minimum 
    # step-by-step total among all sums. Since we always start with 
    # startValue = 0, therefore the initial current step-by-step total is 0, 
    # thus we set "total" and "min_val" be 0. 
    min_val = 0
    total = 0

    # Iterate over the array and get the minimum step-by-step total.
    for num in nums:
        total += num
        min_val = min(min_val, total)

    # We have to change the minimum step-by-step total to 1, 
    # by increasing the startValue from 0 to -min_val + 1, 
    # which is just the minimum startValue we want.
    return -min_val + 1



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Task: Find the minimum positive startValue such that the step-by-step sum of startValue plus array elements never falls below 1.
# Example: nums = [-3, 2, -3, 4, 2] → Output = 5 (startValue = 5 ensures step-by-step sum ≥ 1)
# Why: Practices prefix sum technique to determine the minimum starting value for a cumulative sum constraint.

def minStartValue(nums):  # Example: nums = [-3, 2, -3, 4, 2]

    # 1️⃣ Initialize variables
    # Initialize min_val to track the minimum step-by-step sum
    # Why? We need to find the lowest point of the cumulative sum to determine the required startValue
    min_val = 0  # min_val = 0

    # Initialize total to track the current step-by-step sum
    # Why? We simulate the cumulative sum starting from 0 to find the minimum
    total = 0  # total = 0

    # 2️⃣ Iterate over the array
    # Loop through each number to compute step-by-step sums
    # Why? We need to calculate the cumulative sum and track its minimum
    for num in nums:  # num takes values [-3, 2, -3, 4, 2]
        # --- Iteration 1: num = -3 ---
        # Update the step-by-step sum
        # Why? We add each element to simulate the cumulative sum
        total += num  # total = 0 + (-3) = -3
        # Update the minimum sum seen so far
        # Why? The lowest sum determines how much startValue is needed to keep sums ≥ 1
        min_val = min(min_val, total)  # min_val = min(0, -3) = -3
        # After Iteration 1: total = -3, min_val = -3

        # --- Iteration 2: num = 2 ---
        if num == 2:
            total += num  # total = -3 + 2 = -1
            min_val = min(min_val, total)  # min_val = min(-3, -1) = -3
            # After Iteration 2: total = -1, min_val = -3

        # --- Iteration 3: num = -3 ---
        if num == -3:
            total += num  # total = -1 + (-3) = -4
            min_val = min(min_val, total)  # min_val = min(-3, -4) = -4
            # After Iteration 3: total = -4, min_val = -4

        # --- Iteration 4: num = 4 ---
        if num == 4:
            total += num  # total = -4 + 4 = 0
            min_val = min(min_val, total)  # min_val = min(-4, 0) = -4
            # After Iteration 4: total = 0, min_val = -4

        # --- Iteration 5: num = 2 ---
        if num == 2:
            total += num  # total = 0 + 2 = 2
            min_val = min(min_val, total)  # min_val = min(-4, 2) = -4
            # After Iteration 5: total = 2, min_val = -4

    # 3️⃣ Compute minimum positive startValue
    # Return the value needed to offset the minimum sum to ensure all sums are ≥ 1
    # Why? If min_val is negative, we need -min_val + 1 to make the lowest sum at least 1
    return -min_val + 1  # min_val = -4, -(-4) + 1 = 4 + 1 = 5


nums = [-3, 2, -3, 4, 2]
print(minStartValue(nums))  
# Output: 5 - Returns 5 as the minimum positive startValue ensuring the step-by-step sum starting from nums[0] never falls below 1.



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Alternative solution 
def minStartValue(nums):
    # Start with startValue = 1. 
    start_value = 1

    # While we haven't found the first valid startValue
    while True:
        # The step-by-step total "total" equals startValue at the beginning.
        # Use boolean parameter "isValid" to record whether the total 
        # is larger than or equal to 1.
        total = start_value
        is_valid = True

        # Iterate over the array "nums".
        for num in nums:
            # In each iteration, calculate "total" 
            # plus the element "num" in the array.
            total += num

            # If "total" is less than 1, we shall try a larger startValue,
            # we mark "isValid" as "false" and break the current iteration.
            if total < 1:
                is_valid = False
                break

        # If "isVaild" is true, meaning "total" is never less than 1 in the
        # iteration, therefore we return this "startValue". Otherwise, we 
        # go ahead and try "startValue" + 1 as the new "startValue". 
        if is_valid:
            return start_value
        else:
            start_value += 1



