# 1480. Running Sum of 1d Array

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]). Return the running sum of nums.

# Example
# Input: nums = [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

def runningSum(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(prefix[-1] + nums[i])

    return prefix

nums = [1, 2, 3, 4]
print(runningSum(nums))
# Output: [1, 3, 6, 10]

# Time: O(n)
# - Loop through nums once to build the prefix sum array: O(n).
# - Each append is O(1), so total time is O(n).

# Space: O(n)
# - Prefix sum array stores n values: O(n) space.
# - A few variables (i) take O(1) space.
# - Overall: O(n) total space.
# - If we exclude the output array, extra working space is O(1).


