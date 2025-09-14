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





# ––––––––––––––––––––––––––––––––––––––––––––––

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



# ––––––––––––––––––––––––––––––––––––––––––––––
# Option 1

def maxProduct(nums):
    if not nums:
        return 0
    
    max_so_far = nums[0]  # Tracks the overall maximum product
    curr_max = nums[0]    # Maximum product ending at current index
    curr_min = nums[0]    # Minimum product ending at current index
    
    for i in range(1, len(nums)):
        # Store curr_max for use in curr_min calculation
        temp_max = curr_max
        # Maximum product at current index is either the current number,
        # or the product of the current number with previous max/min
        curr_max = max(nums[i], max(curr_max * nums[i], curr_min * nums[i]))
        # Minimum product at current index
        curr_min = min(nums[i], min(temp_max * nums[i], curr_min * nums[i]))
        # Update global maximum
        max_so_far = max(max_so_far, curr_max)
    
    return max_so_far

# Test cases
print(maxProduct([2, 3, -2, 4]))  # Output: 6
print(maxProduct([-2, 0, -1]))    # Output: 0
print(maxProduct([-2, 3, -4]))    # Output: 24

nums = [2, 3, -2, 4]
print(maxProduct(nums))
# Output: 6




# ––––––––––––––––––––––––––––––––––––––––––––––
# Option 2

def maxProduct(nums):
    if len(nums) == 0:
        return 0

    max_so_far = nums[0]
    min_so_far = nums[0]
    result = max_so_far

    for i in range(1, len(nums)):
        curr = nums[i]
        temp_max = max(curr, max(max_so_far * curr, min_so_far * curr))
        min_so_far = min(curr, min(max_so_far * curr, min_so_far * curr))

        # Update max_so_far after updates to min_so_far to avoid overwriting it
        max_so_far = temp_max
        # Update the result with the maximum product found so far
        result = max(max_so_far, result)

    return result

nums = [2, 3, -2, 4]
print(maxProduct(nums))
# Output: 6
