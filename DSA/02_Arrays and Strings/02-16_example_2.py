# Example 2: 2270. Number of Ways to Split Array

# Given an integer array nums, find the number of ways to split the array into two parts so that the first section has a sum greater than or equal to the sum of the second section. The second section should have at least one number.

# Solution: https://leetcode.com/problems/number-of-ways-to-split-array/solutions/6209795/number-of-ways-to-split-array/

# Example 
    # Input: nums = [10, 4, -8, 7]
    # Output: 2
    # i=0: left=10, right=3 (10>=3) valid
    # i=1: left=14, right=-1 (14>=-1) valid
    # i=2: left=6, right=7 (6<7) invalid

def waysToSplitArray(nums): 
    # Build prefix sum array
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(prefix[-1] + nums[i])

    # Count valid splits where left sum >= right sum
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

# Time: O(n)
# - Build prefix sum array: O(n).
# - Loop through array once to check split conditions: O(n).
# - Overall: O(n) time.

# Space: O(n)
# - Prefix sum array stores n values: O(n) space.
# - A few variables (i, ans, left_section, right_section) take O(1) space.
# - Overall: O(n) total space.
# - If we exclude the prefix sum array, extra working space is O(1).



"""
# Overview for Each Iteration
# Input: nums = [10, 4, -8, 7]
# Step 1: Build prefix sum array
# i  | nums[i] | prefix
# -  | -       | [10]
# 1  | 4       | [10, 14]
# 2  | -8      | [10, 14, 6]
# 3  | 7       | [10, 14, 6, 13]

# Step 2: Count valid splits where left sum >= right sum
# i  | left_section | right_section (prefix[-1] - prefix[i]) | left >= right | ans
# 0  | 10           | 3 (13 - 10)                            | True          | 1
# 1  | 14           | -1 (13 - 14)                           | True          | 2
# 2  | 6            | 7 (13 - 6)                             | False         | 2
# Final: 2




Q: How do we determine the number of valid splits in nums = [10, 4, -8, 7]?
	•	Split at i = 0 → left [10] = 10, right [4, -8, 7] = 3 → 10 ≥ 3 → valid.
	•	Split at i = 1 → left [10, 4] = 14, right [-8, 7] = -1 → 14 ≥ -1 → valid.
	•	Split at i = 2 → left [10, 4, -8] = 6, right [7] = 7 → 6 < 7 → not valid.
	•	✅ Total valid splits = 2.
"""

# ––––––––––––––––––––––––––––––––––––––––––––––
# Concise Solution I came up with while redoing this problem

def waysToSplitArray(nums): 
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(prefix[-1] + nums[i])

    ans = 0
    for i in range(len(nums) - 1):
        if prefix[i] > prefix[-1] - prefix[i]:
            ans += 1

    return ans

nums = [10, 4, -8, 7]  # -> [10, 14, 6, 13]
print(waysToSplitArray(nums))
# Output: 2




# ––––––––––––––––––––––––––––––––––––––––––––––
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



# ––––––––––––––––––––––––––––––––––––––––––––––
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