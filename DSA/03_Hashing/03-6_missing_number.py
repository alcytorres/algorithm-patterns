# 268. Missing Number
"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Example
    Input: nums = [3, 0, 1]
    Output: 2
    Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0, 3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:
    Input: nums = [0, 1]
    Output: 2
    Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0, 2]. 2 is the missing number in the range since it does not appear in nums.

Constraints:
    n == nums.length
    1 <= n <= 104
    0 <= nums[i] <= n
    All the numbers of nums are unique. 

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

Solution: https://leetcode.com/problems/missing-number/editorial/
"""

def missingNumber(nums):
    n = len(nums)
    seen = set(nums)
    
    for num in range(n+1):
        if num not in seen:
            return num

nums = [0, 1]
print(missingNumber(nums))
# Output: 2 → In the range [0, 2], the numbers present are [0, 1], so 2 is the only missing number.


# ––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 

def missingNumber(nums):
    seen = set(nums)       # Convert array to set for O(1) lookups
    n = len(nums) + 1      # Range of expected numbers (0 to n)
    
    for num in range(n):     # Iterate over numbers 0 to n
        if num not in seen:  # If number missing from set
            return num       # Return first missing number
        

"""
Time: O(N)
  - Let N = length of nums.
  - Step 1: Build set from nums → O(N).
      • Each element is added once → O(1) average per insert.
  - Step 2: Loop through numbers 0 to N → O(N).
      • N + 1 iterations (range(n + 1)).
      • Each `num not in seen` check → O(1) average.
  - Combined: O(N + N) = O(N).
  - Overall: O(N).

Space: O(N)
  - Set `seen` stores all N numbers from nums (all unique per constraints).
  - Only a few extra variables (n, num) → O(1).
  - Overall: O(N).


Interview Answer: Worst Case

Time: O(N)
  - One pass to build the set, one pass to check numbers 0 through N.
  - Both passes are linear.

Space: O(N)
  - Set holds all N numbers from the array for O(1) lookups.


---
Overview for Each Iteration
    Input: nums = [0, 1]

    Step 1: Determine range and create set
    n = len(nums) = 2
    seen = {0, 1}

    Step 2: Check each number in range(n + 1) → [0, n] inclusive
    num | num in seen | Action
    ----|-------------|----------
    0   | True        | Continue
    1   | True        | Continue
    2   | False       | Return 2

Final: 2


---
Most IMPORTANT thing to Understand:

    • The full range is [0, n] where n = len(nums).

    • Exactly one number from that range is missing from the array.

    • Put all array numbers into a set so you can check "is this number here?" in O(1) time.

    • Loop through every number from 0 to n — the first one not in the set is the answer.

---
Why this code Works:

    • Set role:
        • seen = set(nums) stores every number in the array.
        • num not in seen is a fast lookup — no need to scan the whole array each time.

    • Loop idea:
        • range(n + 1) checks every number the array should contain: 0, 1, 2, ..., n.
        • The moment you find one that's not in seen, return it — that's the missing number.

    • Efficiency:
        • Building the set: O(N).
        • Checking N + 1 numbers: O(N).
        • No nested loops — avoids O(N²) brute force.

    • Intuition:
        • Like an attendance roll call.
        • Write down everyone who showed up (the set).
        • Read names 0 through n from the master list — whoever isn't on your list is missing.

---
TLDR:

    • Convert the array to a set, then check each number from 0 to n. The first number not in the set is the missing one.

---
Quick Example Walkthrough:

    nums = [0, 1]

    Step 1: Determine range and create set
        n = 2
        seen = {0, 1}

    Step 2: Check each number in range [0, 2] inclusive
        • num = 0 → 0 in seen → keep going
        • num = 1 → 1 in seen → keep going
        • num = 2 → 2 not in seen → return 2

    Final Answer: 2

---
Quick Example Walkthrough:
    nums = [3, 0, 1]

    Step 1: Determine range and create set
        n = 3
        seen = {3, 0, 1}

    Step 2: Check each number in range [0, 3] inclusive
        • num = 0 → 0 in seen → keep going
        • num = 1 → 1 in seen → keep going
        • num = 2 → 2 not in seen → return 2

    Final Answer: 2

---
Full Example Walkthrough:

    nums = [0, 1]

    Starting State:
        n = len(nums) = 2
        seen = set(nums) = {0, 1}

    Loop Iteration 1:
        Check:
            num = 0
            0 in seen? → YES

        Action:
            Continue loop

        Now:
            num moves to next value (1)

    --------------------------------------------------

    Loop Iteration 2:
        Check:
            num = 1
            1 in seen? → YES

        Action:
            Continue loop

        Now:
            num moves to next value (2)

    --------------------------------------------------

    Loop Iteration 3:
        Check:
            num = 2
            2 in seen? → NO

        Action:
            return 2

    --------------------------------------------------

    Final Check:
        Return value: 2

        This means:
            2 is the only number in range [0, 2] that was not in the array.



---
Q: Why use `n = len(nums) + 1` and loop `for num in range(n)`?

  • Because the valid range is 0..n, which includes one extra number beyond the array length.

  • Using +1 ensures we check the final value `n`, which might be the missing number.

  • Example: nums = [0, 1, 2] → length = 3 → missing number is 3, so we must include it in the loop.

"""



# Solution: O(1) Extra Space Complexity
# ––––––––––––––––––––––––––––––––––––––––––––––––

def missingNumber(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2   # what 0 + 1 + 2 + ... + n should equal
    actual_sum = sum(nums)       # what the array actually adds up to
    return expected_sum - actual_sum  # the gap is the missing number

nums = [0, 1]
print(missingNumber(nums))
# Output: 2 → In the range [0, 2], the numbers present are [0, 1], so 2 is the only missing number.


# ––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 

def missingNumber(nums):
    n = len(nums)                      # n = array length (problem n)
    expected_sum = n * (n + 1) // 2    # Sum of full range 0 + 1 + ... + n
    actual_sum = sum(nums)             # Sum of numbers actually in array
    return expected_sum - actual_sum   # Missing number = the gap


"""
Time: O(N)
  - Let N = length of nums.
  - Step 1: Get n = len(nums) → O(1).
  - Step 2: Calculate expected_sum with formula → O(1).
  - Step 3: sum(nums) loops through all N elements → O(N).
  - Step 4: Subtract and return → O(1).
  - Combined: O(N).
  - Overall: O(N).

Space: O(1)
  - Only a few scalar variables (n, expected_sum, actual_sum).
  - No extra data structures.
  - Overall: O(1).


Interview Answer: Worst Case

Time: O(N)
  - One pass through nums with sum(nums).
  - Formula and subtraction are O(1).

Space: O(1)
  - Only three number variables — no set or array.


---
Most IMPORTANT thing to Understand:

    • The full range [0, n] should add up to a known total: n * (n + 1) // 2.

    • The array is missing exactly one number, so its sum will be smaller by that amount.

    • expected_sum - actual_sum gives you the missing number directly.

    • No set needed — just basic addition and subtraction.

---
Why this code Works:

    • Formula role:
        • n * (n + 1) // 2 is the sum of 0 + 1 + 2 + ... + n.
        • This is the total if every number in the range were present.

    • Sum idea:
        • sum(nums) adds up only the numbers that exist in the array.
        • Since one number is missing, actual_sum is exactly that number less than expected_sum.

    • Efficiency:
        • sum(nums): O(N) — one pass through the array.
        • Formula and subtraction: O(1).
        • No extra storage — meets the O(1) space follow-up.

    • Intuition:
        • Like counting money in a cash register.
        • You know the drawer should have $10 total.
        • You count and only find $8.
        • The missing $2 bill is the difference.

---
TLDR:

    • Calculate what the full range should sum to, subtract what the array actually sums to — the difference is the missing number.

---
Quick Example Walkthrough:

    nums = [0, 1]

    Step 1: Set up
        n = 2
        expected_sum = 2 * 3 // 2 = 3   (0 + 1 + 2 = 3)
        actual_sum = 0 + 1 = 1

    Step 2: Find the gap
        expected_sum - actual_sum = 3 - 1 = 2

    Final Answer: 2

---
Quick Example Walkthrough:
    nums = [3, 0, 1]

    Step 1: Set up
        n = 3
        expected_sum = 3 * 4 // 2 = 6   (0 + 1 + 2 + 3 = 6)
        actual_sum = 3 + 0 + 1 = 4

    Step 2: Find the gap
        expected_sum - actual_sum = 6 - 4 = 2

    Final Answer: 2

---
Full Example Walkthrough:

    nums = [0, 1]

    Starting State:
        nums = [0, 1]

    Step 1: Get n
        n = len(nums) = 2

    --------------------------------------------------

    Step 2: Calculate expected sum
        expected_sum = n * (n + 1) // 2
        expected_sum = 2 * 3 // 2 = 3

        This equals 0 + 1 + 2 = 3 (full range sum)

    --------------------------------------------------

    Step 3: Calculate actual sum
        actual_sum = sum(nums)
        actual_sum = 0 + 1 = 1

    --------------------------------------------------

    Step 4: Return the gap
        return expected_sum - actual_sum
        return 3 - 1 = 2

    --------------------------------------------------

    Final Check:
        Return value: 2

        This means:
            2 is the only number in range [0, 2] that was not in the array.

"""
