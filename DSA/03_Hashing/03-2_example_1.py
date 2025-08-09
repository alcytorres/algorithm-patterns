# 1. Two Sum

# Example 1
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example:
# Input: nums = [3, 1, 7, 4, -6], target = 5
# Output: [1, 3]
# Explanation: Because nums[1] + nums[3] == 5, we return [1, 3] or [3, 1].

# Solution: https://leetcode.com/problems/two-sum/description/

def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num

        if complement in d:
            return [i, d[complement]]
        
        d[num] = i

    return []

nums = [3, 1, 7, 4, -6]
target = 5
print(twoSum(nums, target))
# Output: [3, 1] or [1, 3] -> 1 + 4 = 5

# Time: O(n)
# - Loop through nums once: O(n) iterations.
# - Dictionary lookups ('if complement in d') and inserts ('d[num] = i') are O(1) on average.
# - No nested loops, so total time is O(n).

# Space: O(n)
# - Dictionary 'd' can store up to n elements in the worst case (when no match is found until the end), O(n) space.
# - A few integer variables (i, num, complement) take O(1) space.
# - Overall: O(n) total space.
# - If we exclude the dictionary from consideration (not typical here since it's part of the algorithm), extra space is O(1).



# Trace Overview
# i           0  1  2   3
# num         3  1  7   4
# complement: 2  4  -2  1
# As soon as a compliment matches a num you found the answer. In this case that compliment is 1. 

# d = {3: 0, 1: 1, 7: 2, 4: 2}


# ––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def twoSum(nums, target):
    d = {}                     # Initialize empty dictionary for number-to-index mapping
    for i in range(len(nums)): # Iterate over array indices
        num = nums[i]          # Current number
        complement = target - num  # Calculate complement needed for target

        if complement in d:    # If complement exists in dictionary
            return [i, d[complement]]  # Return current index and complement's index
        
        d[num] = i             # Store current number and its index in dictionary
        
    return []                  # Return empty list if no solution found


# ––––––––––––––––––––––––––––––––––––––––––––––––
# Task: Find the indices of two numbers in an array that add up to a target sum.
# Assume exactly one solution exists, and the same element cannot be used twice.
# Example: nums = [3, 1, 7, 4, -6], target = 5 → Output = [1, 3] (nums[1] + nums[3] = 1 + 4 = 5)
# Why: Practices efficient hash map usage for finding pairs with a specific sum.

def twoSum(nums, target):  # Example: nums = [3, 1, 7, 4, -6], target = 5

    # 1️⃣ Initialize hash map
    # Create a dictionary to store number-to-index mappings
    # Why? We need to quickly check if a number's complement (target - num) exists
    d = {}  # d = {}

    # 2️⃣ Iterate through the array
    # Loop through the array with index
    # Why? We need both the number and its index to find the pair and return indices
    for i in range(len(nums)):  # i goes from 0 to 4
        # --- Iteration 1: i = 0 ---
        # Get the current number
        num = nums[i]  # num = nums[0] = 3
        # Calculate the complement needed to reach the target
        # Why? We need to find if target - num exists in the hash map
        complement = target - num  # target = 5, num = 3, complement = 5 - 3 = 2
        # Check if the complement exists in the hash map
        # Why? If found, we have a pair that sums to the target
        if complement in d:  # complement = 2, d = {}, 2 not in d, skip
            return [i, d[complement]]  # skip
        # Store the current number and its index
        # Why? We track numbers we've seen for future complement checks
        d[num] = i  # d = {3: 0}
        # After Iteration 1: d = {3: 0}

        # --- Iteration 2: i = 1 ---
        if i == 1:
            num = nums[i]  # num = nums[1] = 1
            complement = target - num  # target = 5, num = 1, complement = 5 - 1 = 4
            if complement in d:  # complement = 4, d = {3: 0}, 4 not in d, skip
                return [i, d[complement]]
            d[num] = i  # d = {3: 0, 1: 1}
            # After Iteration 2: d = {3: 0, 1: 1}

        # --- Iteration 3: i = 2 ---
        if i == 2:
            num = nums[i]  # num = nums[2] = 7
            complement = target - num  # target = 5, num = 7, complement = 5 - 7 = -2
            if complement in d:  # complement = -2, d = {3: 0, 1: 1}, -2 not in d, skip
                return [i, d[complement]]
            d[num] = i  # d = {3: 0, 1: 1, 7: 2}
            # After Iteration 3: d = {3: 0, 1: 1, 7: 2}

        # --- Iteration 4: i = 3 ---
        if i == 3:
            num = nums[i]  # num = nums[3] = 4
            complement = target - num  # target = 5, num = 4, complement = 5 - 4 = 1
            if complement in d:  # complement = 1, d = {3: 0, 1: 1, 7: 2}, 1 in d, true
                return [i, d[complement]]  # return [3, d[1]] = [3, 1]
            d[num] = i  # skip (return statement executes)
            # After Iteration 4: return [3, 1]

        # --- Iteration 5: i = 4 ---
        # Not reached due to return in Iteration 4

    # 3️⃣ Return empty list if no solution is found
    # Why? The problem assumes exactly one solution, so this is not reached
    return []  # skip


nums = [3, 1, 7, 4, -6]
target = 5
print(twoSum(nums, target))  # Output: [3, 1]