# 1480. Running Sum of 1d Array
"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]). Return the running sum of nums.

Example
    Input: nums = [1, 2, 3, 4, 5]
    Output:       [1, 3, 6, 10, 15]
    Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4, 1+2+3+4+5].

Solution: https://leetcode.com/problems/running-sum-of-1d-array/description/
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


---
Most IMPORTANT thing to Understand:
    • Each position stores the total sum from the beginning of the array up to that index.

    • prefix[-1] always represents the latest running total.

    • We build the answer step-by-step by taking the previous running sum and adding the current number.

---
Why this code Works:
    • prefix array:
        • Stores the running sums as we build them.

    • prefix[-1]:
        • Gives the most recent running total.
        • This avoids recalculating sums from the start every time.

    • Core idea:
        • Current running sum =
            previous running sum + current number

    • Efficiency:
        • Instead of repeatedly summing earlier numbers,
          we reuse the previous total.

    • Intuition:
        • Think of it like keeping a bank balance.
        • Each new number gets added onto the previous total.

---
TLDR:
    • This works because each new running sum is built from the previous running sum plus the current value.
    • We keep updating the total as we move through the array once.

---
Quick Example Walkthrough:

nums = [1, 2, 3, 4, 5]

Step 1:
    Start prefix with the first number:
        prefix = [1]

Step 2:
    Add each new number to the latest running total.

    • 1 + 2 = 3   → [1, 3]
    • 3 + 3 = 6   → [1, 3, 6]
    • 6 + 4 = 10  → [1, 3, 6, 10]
    • 10 + 5 = 15 → [1, 3, 6, 10, 15]

Final Answer:
    [1, 3, 6, 10, 15]

---
Full Example Walkthrough:

nums = [1, 2, 3, 4, 5]

Starting State:
    prefix = [1]

    This means:
        Running sum up to index 0 is 1

--------------------------------------------------

Loop Iteration 1:
    i = 1
    nums[i] = 2

    Previous running sum:
        prefix[-1] = 1

    Compute new running sum:
        1 + 2 = 3

    Append to prefix:
        prefix = [1, 3]

--------------------------------------------------

Loop Iteration 2:
    i = 2
    nums[i] = 3

    Previous running sum:
        prefix[-1] = 3

    Compute new running sum:
        3 + 3 = 6

    Append to prefix:
        prefix = [1, 3, 6]

--------------------------------------------------

Loop Iteration 3:
    i = 3
    nums[i] = 4

    Previous running sum:
        prefix[-1] = 6

    Compute new running sum:
        6 + 4 = 10

    Append to prefix:
        prefix = [1, 3, 6, 10]

--------------------------------------------------

Loop Iteration 4:
    i = 4
    nums[i] = 5

    Previous running sum:
        prefix[-1] = 10

    Compute new running sum:
        10 + 5 = 15

    Append to prefix:
        prefix = [1, 3, 6, 10, 15]

--------------------------------------------------

Final Answer:
    return prefix

    return [1, 3, 6, 10, 15]

    Each index stores the sum of all numbers from the start up to that position.
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