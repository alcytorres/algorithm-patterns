# Example 2: 2270. Number of Ways to Split Array

# Given an integer array nums, find the number of ways to split the array into two parts so that the first section has a sum greater than or equal to the sum of the second section. The second section should have at least one number.

# Solution: https://leetcode.com/problems/number-of-ways-to-split-array/solutions/6209795/number-of-ways-to-split-array/

# Example 
    # Input: nums = [10, 4, -8, 7]
    # Output: 2
    # i=0: left=10, right=3 (10>=3) valid
    # i=1: left=14, right=-1 (14>=-1) valid
    # i=2: left=6, right=7 (6<7) invalid

# ––––––––––––––––––––––––––––––––––––––––––––––
# Best Solution: No array needed

def waysToSplitArray(self):
    total = sum(nums)
    left = count = 0

    n = len(nums)

    for i in range(n - 1):   # Ensure right part non-empty
        left += nums[i]
        right = total - left

        if left >= right:
            count += 1

    return count

nums = [10, 4, -8, 7]  
print(waysToSplitArray(nums))
# Output: 2 → Valid splits after indices [0, 1]:
# - Split 0 → left = 10, right = 3 ✅
# - Split 1 → left = 14, right = -1 ✅
# - Split 2 → left = 6, right = 7 ❌

"""
Time: O(N)
  - Let N = length of nums.
  - Step 1: Compute total sum of array → O(N).
  - Step 2: Iterate through nums (except last index) → O(N - 1).
      • Update running left sum in O(1).
      • Compute right sum as total - left in O(1).
      • Check condition (left >= right) in O(1).
  - Overall: O(N + N) = O(N).

Space: O(1)
  - Only a few scalar variables used: total, left, right, count.
  - No additional data structures are created.
  - Overall: O(1).

  
Interview Answer: Worst Case

Time: O(N)
  - Single pass computes total and evaluates each split.

Space: O(1)
  - Constant extra space for running sums and counter.



Overview for Each Iteration
Input: nums = [10, 4, -8, 7]

Step 1: Compute total sum
total = sum(nums) = 10 + 4 + (-8) + 7 = 13

Step 2: Count valid splits where left sum >= right sum
i   | nums[i] | l         | r (total - l) | l >= r | count
----|---------|-----------|---------------|--------|-------
0   | 10      | 10        | 3 (13 - 10)   | True   | 1
1   | 4       | 14 (10+4) | -1 (13 - 14)  | True   | 2
2   | -8      | 6 (14-8)  | 7 (13 - 6)    | False  | 2

Final: 2



Most IMPORTANT thing to Understand:
    • We split the array into left and right parts.

    • A split is valid if sum(left) >= sum(right).

    • The right side must have at least one number → we stop at n-1.


Why this code Works:

    • total: total sum of all numbers.

    • l: running sum of the left part.

    • r: right sum = total - l.

    • At each split, check if l >= r. If yes, count it.

    • Efficiency: one pass, O(n) time, O(1) space.

    • Intuition: Like walking through the array while carrying a “left bag.” At each step, compare your bag vs. the rest.


TLDR
    • Keep a running left sum, compute right as total - left, and count how many times left ≥ right.

    
Quick Example Walkthrough:
nums = [10, 4, -8, 7]

    Total = 13

    i=0 → left=10, right=3 → valid ✅

    i=1 → left=14, right=-1 → valid ✅

    i=2 → left=6, right=7 → not valid ❌

Final Answer: 2



---
Q: How do we determine the number of valid splits in nums = [10, 4, -8, 7]?
	•  Split at i = 0 → left [10] = 10, right [4, -8, 7] = 3 → 10 ≥ 3 → valid.

	•  Split at i = 1 → left [10, 4] = 14, right [-8, 7] = -1 → 14 ≥ -1 → valid.

	•  Split at i = 2 → left [10, 4, -8] = 6, right [7] = 7 → 6 < 7 → not valid.

	•  ✅ Total valid splits = 2.

"""


# ––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def waysToSplitArray(nums):
    total = sum(nums)    # Precompute total sum of entire array
    left = count = 0     # left: sum of left part, count: valid split
    n = len(nums)        # Length of input array
    
    for i in range(n - 1):   # Try every possible split point (except last)
        left += nums[i]      # Grow left part by adding current element
        right = total - left   # Right part = everything not yet in left
        
        if left >= right:  # Valid split: left section >= right section
            count += 1     # Count this valid position
    
    return count           # Total number of ways to split array



# ––––––––––––––––––––––––––––––––––––––––––––––
# Solution 2: Prefix Sum Array

def waysToSplitArray(nums):
    # Build prefix sum array
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(prefix[-1] + nums[i])
    
    # Count valid splits where left sum >= right sum
    count = 0
    n = len(nums)  # 4

    for i in range(n - 1):
        left = prefix[i]
        right = prefix[-1] - left
        
        if left >= right:
            count += 1
    
    return count

nums = [10, 4, -8, 7]   # -> [10, 14, 6, 13]
print(waysToSplitArray(nums))
# Output: 2 → Valid splits after indices [0, 1]:
# - Split 0 → left = 10, right = 3 ✅
# - Split 1 → left = 14, right = -1 ✅
# - Split 2 → left = 6, right = 7 ❌

"""
Time: O(N)
  - Build prefix sum array: O(n).
  - Loop through array once to check split conditions: O(n).
  - Overall: O(n) time.

Space: O(N)
  - Prefix sum array stores n values: O(n) space.
  - A few variables (i, ans, left, right) take O(1) space.
  - Overall: O(n) total space.
  - If we exclude the prefix sum array, extra working space is O(1).


Overview for Each Iteration
Input: nums = [10, 4, -8, 7]
Step 1: Build prefix sum array
i  | nums[i] | prefix
---|---------|----------------
-  | -       | [10]
1  | 4       | [10, 14]
2  | -8      | [10, 14, 6]
3  | 7       | [10, 14, 6, 13]

Step 2: Count valid splits where left sum >= right sum
i  | l  | r (prefix[-1] - prefix[i]) | left >= right | ans
---|----|----------------------------|---------------|-----
0  | 10 | 3 (13 - 10)                | True          | 1
1  | 14 | -1 (13 - 14)               | True          | 2
2  | 6  | 7 (13 - 6)                 | False         | 2

Final: 2


"""


# ––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
def waysToSplitArray(nums):
    # Build prefix sum array
    prefix = [nums[0]]               # Start with first element
    for i in range(1, len(nums)):    # For each remaining element
        prefix.append(prefix[-1] + nums[i])  # Add it to previous sum
    
    count = 0           # Counter for valid splits
    n = len(nums)       # Length of array
    
    # Try every possible split point (except last index)
    for i in range(n - 1):
        left  = prefix[i]           # Sum of elements from 0 to i
        right = prefix[-1] - left   # Sum of elements from i+1 to end
        
        if left >= right:  # Valid split if left part >= right part
            count += 1     # Count this split
    
    return count             # Total number of valid splits



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
# Output: 2 → Valid splits after indices [0, 1]:
# - Split 0 → left = 10, right = 3 ✅
# - Split 1 → left = 14, right = -1 ✅
# - Split 2 → left = 6, right = 7 ❌