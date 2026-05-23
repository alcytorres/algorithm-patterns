# 1413. Minimum Value to Get Positive Step by Step Sum
"""
Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.

Example 1
    Input: nums = [-3, 2, -3, 4, 2]
    Output: 5
    Step-by-step sum: startValue + nums[i]
    Track minimum running total: [-3, -1, -4, 0, 2] (min = -4)
    Minimum startValue to keep sum ≥ 1: -(-4) + 1 = 5

Example 2
    Input: nums = [3, 2, 1]
    Output: 1

Example 3
    Input: nums = [-1, -2, -3]
    Output: 7

Video https://www.youtube.com/watch?v=QgRZcbYboxg

Solution: https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/solutions/1513266/minimum-value-to-get-positive-step-by-step-sum/
"""

# Solution — Minimum Value to Get Positive Step by Step Sum

def minStartValue(nums):
    min_val = 0
    total = 0

    for num in nums:
        total += num
        min_val = min(min_val, total)

    return -min_val + 1

nums = [-3, 2, -3, 4, 2]
print(minStartValue(nums))
# Output: 5 → Returns 5 as the minimum positive startValue ensuring the step-by-step sum starting from nums[0] never falls below 1.


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def minStartValue(nums):
    min_val = 0    # Tracks the lowest running sum seen so far
    total = 0      # Current running sum (starts as if startValue=0)
    
    for num in nums:    # One pass through the array
        total += num    # Update running sum with next number
        min_val = min(min_val, total)   # Update min if this sum is lower
    
    # If min_val is negative (e.g., -4), we dipped below 1.
    # To lift the lowest point to exactly 1, add -min_val + 1.
    # Example: min_val = -4 → startValue = 4 + 1 = 5
    return -min_val + 1


"""
Time: O(N)
  - Let N = length of nums.
  - One pass through nums array → O(N).
  - Each iteration:
      • Update running sum (total) → O(1)
      • Update minimum running sum (min_val) → O(1)
  - Final calculation: -min_val + 1 → O(1)
  - Overall: O(N).

Space: O(1)
  - Only scalar variables used: total and min_val.
  - No extra data structures are created.
  - Overall: O(1).

  
Interview Answer: Worst Case

Time: O(N)
  - One pass through the nums array.
  - Each number is processed one time.

Space: O(1)
  - Only total and min_val variables are used. 
  - No extra data structures.


---
Overview for Each Iteration
Input: nums = [-3, 2, -3, 4, 2]

Step: Calculate step-by-step sum and track minimum total
i   | num  | total | min_val
----|------|-------|-----------------
-   | -    | 0     | 0
0   | -3   | -3    | -3 (min(0, -3))
1   | 2    | -1    | -3 (min(-3, -1))
2   | -3   | -4    | -4 (min(-3, -4))
3   | 4    | 0     | -4 (min(-4, 0))
4   | 2    | 2     | -4 (min(-4, 2))

Final: -(-4) + 1 = 5



---
Most IMPORTANT thing to Understand

    • We pretend the starting value is 0 first.

    • As we move through nums:
        • We track the running sum.

    • The MOST IMPORTANT thing:
        • Find the LOWEST running sum we ever reach.

    • If the running sum drops to -4:
        • We need a startValue big enough so:
            -4 becomes at least 1.

    • Formula:
        startValue = -minimum_running_sum + 1

    • This guarantees:
        • Every step-by-step sum stays >= 1.

---
Why this code Works

    • total:
        • Tracks the running prefix sum.

    • min_val:
        • Stores the LOWEST running sum seen so far.

    • Why we track the minimum:
        • The lowest dip is the dangerous point.
        • If we can fix the lowest point, all higher points are automatically safe.

    • Example:
        Running sums:
            [-3, -1, -4, 0, 2]

        Lowest value:
            -4

        We need:
            startValue + (-4) >= 1

        Solve:
            startValue >= 5

    • Why "-min_val + 1" works:
        • If min_val = -4:
            • Add 4 to bring it to 0
            • Add 1 more so it becomes 1

        Final:
            5

    • Efficiency:
        • Only one pass through nums.
        • Time: O(N)
        • Space: O(1)

    • Intuition:
        • Think of the running sum like walking downhill.
        • min_val is the deepest hole you fall into.
        • startValue is how high you must start so you never go below height 1.

---
TLDR
    • This solution finds the lowest running sum while traversing the array.

    • Then it calculates the minimum startValue needed to lift that lowest point up to at least 1.

---
Quick Example Walkthrough

    nums = [-3, 2, -3, 4, 2]

    Step 1:
        Start with running sum = 0

    Step 2:
        Build running sums:
            -3
            -1
            -4
            0
            2

    Step 3:
        Lowest running sum:
            -4

    Step 4:
        We need:
            startValue + (-4) >= 1

        So:
            startValue = 5

    Final Answer:
        5

---
Full Example Walkthrough

    nums = [-3, 2, -3, 4, 2]

    Starting State:
        total = 0
        min_val = 0

--------------------------------------------------

    Loop Iteration 1:
        num = -3

        Update running sum:
            total += -3
            total = -3

        Update minimum:
            min_val = min(0, -3)
            min_val = -3

        Current State:
            total = -3
            min_val = -3

--------------------------------------------------

    Loop Iteration 2:
        num = 2

        Update running sum:
            total += 2
            total = -1

        Update minimum:
            min_val = min(-3, -1)
            min_val = -3

        Current State:
            total = -1
            min_val = -3

--------------------------------------------------

    Loop Iteration 3:
        num = -3

        Update running sum:
            total += -3
            total = -4

        Update minimum:
            min_val = min(-3, -4)
            min_val = -4

        Current State:
            total = -4
            min_val = -4

--------------------------------------------------

    Loop Iteration 4:
        num = 4

        Update running sum:
            total += 4
            total = 0

        Update minimum:
            min_val = min(-4, 0)
            min_val = -4

        Current State:
            total = 0
            min_val = -4

--------------------------------------------------

    Loop Iteration 5:
        num = 2

        Update running sum:
            total += 2
            total = 2

        Update minimum:
            min_val = min(-4, 2)
            min_val = -4

        Current State:
            total = 2
            min_val = -4

--------------------------------------------------

Final Calculation

    Lowest running sum:
        min_val = -4

    We need:
        startValue + (-4) >= 1

    Solve:
        startValue >= 5

    Return:
        -min_val + 1
        = -(-4) + 1
        = 4 + 1
        = 5

--------------------------------------------------

Final Answer

    5

    This means:
        Starting with 5 guarantees every running total stays at least 1.

"""


# ––––––––––––––––––––––––––––––––––––––––––––––––
# Q: Why min_val = 0 (not float('inf'))

"""
Can I use min_val = float('inf')?
    • Technically the loop still runs.
    • But you can get the WRONG answer when nums never dips below 0.

Example: nums = [3, 2, 1]  →  answer should be 1

    With min_val = 0:
        total: 3 → 5 → 8
        min_val stays 0  (0 is still the lowest point)
        return -0 + 1 = 1  ✅

    With min_val = float('inf'):
        min_val becomes 3 → 3 → 3  (never remembers 0)
        return -3 + 1 = -2  ❌


Why min_val must start at 0
    • total starts at 0 = "pretend startValue is 0, sum so far is 0"
    • Before you add any nums, the running sum is already 0
    • That starting point might be the lowest the path ever gets
    • min_val tracks the lowest running sum seen — including that start


First time seeing the problem — how you'd figure it out
    • Read: step-by-step sum must never drop below 1
    • Ask: "How low could the sum go if startValue were 0?"
          → Walk nums left to right, add each number, watch total dip
    • The danger is the deepest dip (minimum prefix sum)
    • You haven't moved yet → dip starts at 0, not at infinity
    • So initialize min_val = 0 to include "before the first element"

Memory hook
    • total = path with startValue 0
    • min_val = lowest point on that path (including the start at 0)
    • Answer lifts that lowest point to 1:  -min_val + 1
"""



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Solution — Minimum Value to Get Positive Step by Step Sum
# More Examples

def minStartValue(nums):
    total = 0
    min_val = 0

    for num in nums:
        total += num
        min_val = min(min_val, total)
    
    return -min_val + 1

nums = [3, 2, 1]
print(minStartValue(nums))
# Output: 1



def minStartValue(nums):
    total = 0
    min_val = 0

    for num in nums:
        total += num
        min_val = min(min_val, total)
    
    return -min_val + 1

nums = [-1, -2, -3]
print(minStartValue(nums))
# Output: 7




# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Alternative solution 
class Solution:
    def minStartValue(self, nums: list[int]) -> int:

        total = 0
        min_value = 0
        
        for num in nums:
            total += num 
            if total < min_value:
                min_value = total

        return -min_value + 1


solution = Solution()
nums = [-3, 2, -3, 4, 2]
print(solution.minStartValue(nums))
# Output: 5





# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Alternative solution 
def minStartValue(nums):
    # Start with startValue = 1. 
    start_value = 1

    # While we haven't found the first valid startValue
    while True:
        # The step-by-step total "total" equals startValue at the beginning.
        # Use boolean parameter "isValid" to record whether the total 
        # is larger than or equal to 1.
        total = start_value
        is_valid = True

        # Iterate over the array "nums".
        for num in nums:
            # In each iteration, calculate "total" 
            # plus the element "num" in the array.
            total += num

            # If "total" is less than 1, we shall try a larger startValue,
            # we mark "isValid" as "false" and break the current iteration.
            if total < 1:
                is_valid = False
                break

        # If "isVaild" is true, meaning "total" is never less than 1 in the
        # iteration, therefore we return this "startValue". Otherwise, we 
        # go ahead and try "startValue" + 1 as the new "startValue". 
        if is_valid:
            return start_value
        else:
            start_value += 1
