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
"""

# Bit Manipulation Solution
def singleNumber(nums):
    a = 0
    for i in nums:
        a ^= i
    return a

nums = [2, 2, 1]
print(singleNumber(nums))  # Output 1


# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
def singleNumber(nums):
    a = 0                 # Start with neutral element (0 for XOR)
    for i in nums:        # Go through every number once
        a ^= i            # XOR it with running result
    
    return a              # The single number survives


"""
Time: O(N)
  - Let N = length of nums.
  - Loop through nums once → O(N).
  - Each XOR operation (a ^= i) is O(1).
  - Overall: O(N).

Space: O(1)
  - Uses only one variable (a) to track the XOR result.
  - No additional data structures are created.
  - Overall: O(1).

  
Interview Answer: Worst Case

Time: O(N)
  - Single pass applying XOR to all elements.

Space: O(1)
  - Constant space using one accumulator variable.


  
---
Most IMPORTANT thing to Understand:
    • XOR has two critical properties:
        • x ^ x = 0  (a number cancels itself)
        • x ^ 0 = x  (0 does nothing)

    • Since every number appears exactly twice except one, all pairs cancel out.

    • The remaining value after XOR-ing everything is the single number.

---
Why this code Works:
    • Data structure: None needed — XOR itself handles counting implicitly.

    • Technique: Bit manipulation with XOR across the entire array.

    • Efficiency: Instead of tracking counts with a hash map (O(n) space), XOR solves it in one pass with constant space.

    • Intuition: Like flipping a light switch — flip it twice and it ends up off;
      only the switch flipped once stays on.

---
TLDR:
    • XOR all numbers together — pairs cancel out and the unique number remains.

---
Quick Example Walkthrough:

Example 1:
    nums = [2, 2, 1]

    Start: a = 0
    a = 0 ^ 2 = 2
    a = 2 ^ 2 = 0   (pair cancels)
    a = 0 ^ 1 = 1

    Final Answer: 1


Example 2:
    nums = [4, 1, 2, 1, 2]

    Start: a = 0
    a = 0 ^ 4 = 4
    a = 4 ^ 1 = 5
    a = 5 ^ 2 = 7
    a = 7 ^ 1 = 6   (1 cancels)
    a = 6 ^ 2 = 4   (2 cancels)

    Final Answer: 4


Example 3:
    nums = [1]

    a = 0 ^ 1 = 1

    Final Answer: 1
"""



# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Hash Table
from collections import defaultdict

def singleNumber(nums):
    count = defaultdict(int)
    for num in nums:
        count[num] += 1
    
    for key in count:
        if count[key] == 1:
            return key      

nums = [2, 2, 1]
print(singleNumber(nums))  # Output 1


"""
Time: O(N)
  - Let N = length of nums.
  - Step 1: Count frequencies using a hash map → O(N).
      • Each insertion/update is O(1) average.
  - Step 2: Scan the hash map to find the element with count 1 → O(U),
    where U = number of unique elements and U ≤ N.
  - Overall: O(N).

Space: O(N)
  - Hash map stores counts for up to N unique numbers.
  - A few loop variables use O(1).
  - Overall: O(N).

  
Interview Answer: Worst Case

Time: O(N)
  - One pass to count, one pass to find the single element.

Space: O(N)
  - Hash map stores frequency of each number.
"""
