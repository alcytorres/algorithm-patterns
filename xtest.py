# 268. Missing Number

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Solution: https://leetcode.com/problems/missing-number/editorial/

def missingNumber(nums):
    seen = set(nums)
    for i in range(len(nums) + 1):
        if i not in seen:
            return i

l = [3, 0, 1]
print(missingNumber(l))
# Output: 2