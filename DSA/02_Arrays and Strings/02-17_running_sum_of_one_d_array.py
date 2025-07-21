# 1480. Running Sum of 1d Array

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]). Return the running sum of nums.

# Example
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])

        return prefix

        # nums = [1,2,3,4]
        # print(runningSum(nums))
        # Output: [1,3,6,10]

# Time: O(n) - Iterates through n elements once to build the prefix sum array with O(1) operations per iteration.
# Space: O(n) - Uses a prefix sum array of size n to store the running sums, excluding input.


