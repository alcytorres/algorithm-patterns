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

# Time: O(n) - Single pass through n elements with O(1) hash operations.
# Space: O(n) - Stores up to n elements in the hash map.


# Trace Overview
# i           0  1  2   3
# num         3  1  7   4
# complement: 2  4  -2  1
# As soon as a compliment matches a num you found the answer. In this case that compliment is 1. 

# d = {3: 0, 1: 1, 7: 2, 4: 2}

