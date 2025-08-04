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


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
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