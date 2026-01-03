# 1480. Running Sum of 1d Array
"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]). Return the running sum of nums.

Example
    Input: nums = [1, 2, 3, 4, 5]
    Output:       [1, 3, 6, 10, 15]
    Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4, 1+2+3+4+5].
"""

def runningSum(nums):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(prefix[-1] + nums[i])

    return prefix

nums = [1, 2, 3, 4, 5]
print(runningSum(nums))
# Output: [1, 3, 6, 10, 15]

"""
Time: O(N)
  - Let N = length of nums.
  - Step 1: Initialize prefix array with the first element → O(1).
  - Step 2: Iterate through the remaining N - 1 elements.
      • For each i, compute prefix[i] = prefix[i - 1] + nums[i] → O(1) per element.
  - Overall: O(N).

Space: O(N)
  - The prefix list stores N running sums.
  - Only a few loop variables and temporary values use O(1) space.
  - Overall: O(N).

  
Interview Answer: Worst Case

Time: O(N)
  - Single pass builds running sum array.

Space: O(N)
  - Output array of size N stores cumulative sums.
"""




# ––––––––––––––––––––––––––––––––––––––––––––––
# 🔄 Equivalent Ways to Document Types in Python


# 📝 Old docstring style (Sphinx style)
def runningSum(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(prefix[-1] + nums[i])

    return prefix


# 🆕 Modern type hints (PEP 484 style)
from typing import List

def runningSum(nums: List[int]) -> List[int]:
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(prefix[-1] + nums[i])

    return prefix