# Example 2: 2270. Number of Ways to Split Array

# Given an integer array nums, find the number of ways to split the array into two parts so that the first section has a sum greater than or equal to the sum of the second section. The second section should have at least one number.

# Solution: https://leetcode.com/problems/number-of-ways-to-split-array/solutions/6209795/number-of-ways-to-split-array/

def waysToSplitArray(nums): 
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(prefix[-1] + nums[i])

    ans = 0
    for i in range(len(nums) - 1):
        left_section = prefix[i]
        right_section = prefix[-1] - prefix[i]
        if left_section >= right_section:
            ans += 1
    
    return ans

nums = [10, 4, -8, 7]  # -> [10, 14, 6, 13]
print(waysToSplitArray(nums))
# Output: 2

# Time: O(n) - Builds prefix sum array in O(n) and iterates n-1 times for comparisons, each O(1).
# Space: O(n) - Uses a prefix sum array of size n, plus a constant number of variables.


"""
There are three ways of splitting nums into two non-empty parts:
- Split nums at index 0. Then, the first part is [10], and its sum is 10. The second part is [4,-8,7], and its sum is 3. Since 10 >= 3, i = 0 is a valid split.
- Split nums at index 1. Then, the first part is [10,4], and its sum is 14. The second part is [-8,7], and its sum is -1. Since 14 >= -1, i = 1 is a valid split.
- Split nums at index 2. Then, the first part is [10,4,-8], and its sum is 6. The second part is [7], and its sum is 7. Since 6 < 7, i = 2 is not a valid split.
Thus, the number of valid splits in nums is 2.
"""


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
def waysToSplitArray(nums): 
    prefix = [nums[0]]       # Initialize prefix with first element
    for i in range(1, len(nums)):  # Iterate from index 1
        prefix.append(prefix[-1] + nums[i])  # Add current element to previous sum
    
    ans = 0                  # Count of valid splits
    for i in range(len(nums) - 1):  # Iterate up to second-to-last index
        left_section = prefix[i]    # Sum of left section up to i
        right_section = prefix[-1] - prefix[i]  # Sum of right section from i+1 to end
        if left_section >= right_section:  # Check if left sum >= right sum
            ans += 1         # Increment count for valid split
    
    return ans               # Return total number of ways


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––




# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Alternative Better Solution: No array needed

def waysToSplitArray(self):
    ans = left_section = 0
    total = sum(nums)

    for i in range(len(nums) - 1):
        left_section += nums[i]
        right_section = total - left_section
        if left_section >= right_section:
            ans += 1

    return ans

nums = [10, 4, -8, 7]  
print(waysToSplitArray(nums))
# Output: 2

# Time: O(n) - Computes total sum in O(n) and iterates n-1 times with O(1) operations per iteration.
# Space: O(1) - Uses only three integer variables (ans, left_section, right_section), excluding input.