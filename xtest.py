# 152. Maximum Product Subarray

# Given an integer array nums, find a subarray that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# Example 1:
    # Input: nums = [2, 3, -2, 4]
    # Output: 6
    # Explanation: [2,3] has the largest product 6.

# Example 2:
    # Input: nums = [-2, 0, -1]
    # Output: 0
    # Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


# Solution: https://leetcode.com/problems/maximum-product-subarray/solutions/738529/maximum-product-subarray/



def maxProduct(nums):
    hi = lo = best = nums[0]
    for x in nums[1:]:
        if x < 0: hi, lo = lo, hi
        hi = max(x, hi * x)
        lo = min(x, lo * x)
        best = max(best, hi)
    return best

nums = [2, 3, -2, 4]
print(maxProduct(nums))
# Output: 6
