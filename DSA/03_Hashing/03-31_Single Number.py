# 136. Single Number
"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
    Input: nums = [2, 2, 1]
    Output: 1

Example 2:
    Input: nums = [4, 1, 2, 1, 2]
    Output: 4

Example 3:
    Input: nums = [1]
    Output: 1

Constraints:
    1 <= nums.length <= 3 * 104
    -3 * 104 <= nums[i] <= 3 * 104
    Each element in the array appears twice except for one element which appears only once.

Solution: https://leetcode.com/problems/single-number/
"""

# Solution: XOR (bit manipulation)
def singleNumber(nums):
    ans = 0

    for num in nums:
        ans ^= num

    return ans

nums = [2, 2, 1]
print(singleNumber(nums))
# Output: 1

nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))
# Output: 4

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
def singleNumber(nums):
    ans = 0                   # Start at 0 — XOR with 0 leaves any number unchanged

    for num in nums:          # Go through each number in the list
        ans ^= num            # XOR in this number — pairs cancel, single one stays

    return ans                # Return the only number that never got canceled out

"""
Time: O(N)
  - Let N = number of elements in nums.
  - One pass through nums → O(N).
  - Each iteration does one XOR operation → O(1).
  - Overall: O(N).

Space: O(1)
  - Only one extra variable (ans) is used.
  - No hash map, set, or other data structures.
  - Overall: O(1).


Interview Answer: Worst Case

Time: O(N)
  - Single loop XORs every number once.

Space: O(1)
  - Only the ans variable is used.
  - No extra data structures.


---
Most IMPORTANT thing to Understand:

    • XOR has a cancel-out rule: any number XORed with itself becomes 0 (e.g., 2 ^ 2 = 0).

    • XOR with 0 does nothing: a ^ 0 = a.

    • XOR order does not matter — pairs always cancel no matter where they appear in the list.

    • ans starts at 0 and collects every number; duplicates wipe each other out, leaving only the single number.

---
Why this code Works:

    • ans role:
        • ans is a running XOR accumulator — it holds the combined XOR of every number seen so far.
        • Each new num gets folded in with ans ^= num.

    • Cancel-out idea:
        • When the same number appears twice, it XORs itself away (a ^ a = 0).
        • The one number that appears only once never gets canceled.

    • Efficiency:
        • One pass through nums → O(N) time.
        • Only one variable (ans) → O(1) space.
        • Beats hash map approaches that need O(N) extra memory.

    • Intuition:
        • Like pairing up socks in a laundry basket.
        • Every matching pair gets tossed out.
        • The one sock with no match is what is left in ans.

---
TLDR:

    • XOR every number into ans — duplicates cancel to 0, and the lone number is all that remains.


---
Quick Example Walkthrough:

    nums = [2, 2, 1]

    Step 1: Start
        ans = 0

    Step 2: XOR each number in
        • ans ^= 2  →  ans = 2
        • ans ^= 2  →  ans = 0   (2 and 2 canceled)
        • ans ^= 1  →  ans = 1

    Final Answer: 1


---
Full Example Walkthrough:

    nums = [2, 2, 1]

    Starting State:
        ans = 0
        nums = [2, 2, 1]

    Loop Iteration 1:
        num = 2

        XOR:
            ans ^= num
            0 ^ 2 = 2

        Now:
            ans = 2

        Meaning:
            ans now holds the first 2.

    --------------------------------------------------

    Loop Iteration 2:
        num = 2

        XOR:
            ans ^= num
            2 ^ 2 = 0

        Now:
            ans = 0

        Meaning:
            The second 2 canceled the first 2. ans is back to 0.

    --------------------------------------------------

    Loop Iteration 3:
        num = 1

        XOR:
            ans ^= num
            0 ^ 1 = 1

        Now:
            ans = 1

        Meaning:
            1 appeared only once, so nothing cancels it.

    --------------------------------------------------

    Final Check:
        return ans
        return 1

        This means:
            1 is the only number that never got paired and canceled out.


---
Overview for Each Iteration
Input: nums = [2, 2, 1]

XOR each number into ans — pairs cancel out

i | num | ans | XOR    | Note
--|-----|-----|--------|------------------
- | -   | 0   | start  | ans begins at 0
0 | 2   | 2   | 0^2    | store first 2
1 | 2   | 0   | 2^2    | pair canceled
2 | 1   | 1   | 0^1    | lone number stays

Final: 1


---
Overview for Each Iteration
Input: nums = [4, 1, 2, 1, 2]

XOR each number into ans — pairs cancel out

i | num | ans | XOR    | Note
--|-----|-----|--------|------------------
- | -   | 0   | start  | ans begins at 0
0 | 4   | 4   | 0^4    | store 4
1 | 1   | 5   | 4^1    | fold in 1
2 | 2   | 7   | 5^2    | fold in 2
3 | 1   | 6   | 7^1    | second 1 cancels first
4 | 2   | 4   | 6^2    | second 2 cancels first

Final: 4

"""






# Solution: Frequency counter (hash map) — best starting point
from collections import Counter

def singleNumber(nums):
    counts = Counter(nums)
    for num, count in counts.items():
        if count == 1:
            return num

nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))
# Output: 4

"""
Time: O(N)
  - Counter(nums) scans once → O(N).
  - Loop over counts → O(U), U ≤ N → O(N).

Space: O(U) ≈ O(N)
  - Counter stores one entry per unique number.


Interview Answer: Worst Case

Time: O(N)
  - One pass to count, one pass over unique keys.

Space: O(N)
  - Hash map stores counts for up to N numbers.
"""


# Solution: Set “pair cancellation”
def singleNumber(nums):
    seen = set()
    for num in nums:
        if num in seen:
            seen.remove(num)   # pair found → cancel out
        else:
            seen.add(num)
    return seen.pop()            # only the single number remains

nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))
# Output: 4

"""
Time: O(N)
  - One pass: add/remove per number → O(1) average each.

Space: O(U) ≈ O(N)
  - Set holds unpaired numbers seen so far (at most ~N/2 during loop).


Interview Answer: Worst Case

Time: O(N)
  - Single loop with O(1) set add/remove/lookup.

Space: O(N)
  - Set can grow to ~N/2 unpaired entries mid-loop.
"""