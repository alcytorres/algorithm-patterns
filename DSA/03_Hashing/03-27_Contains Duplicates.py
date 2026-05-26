# 217. Contains Duplicate
"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
    Input: nums = [1, 2, 3, 1]
    Output: true
    Explanation:
    The element 1 occurs at the indices 0 and 3.

Example 2:
    Input: nums = [1, 2, 3, 4]
    Output: false
    Explanation:
    All elements are distinct.
 
Constraints:
    1 <= nums.length <= 105
    -109 <= nums[i] <= 109

Solution: https://leetcode.com/problems/contains-duplicate/submissions/2013652533/
"""

# Solution 1: Set Early-Exit Duplicate Check

def containsDuplicate(nums):
    seen = set()
    
    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False

nums =  [1, 2, 3, 1]
print(containsDuplicate(nums))  # Output True

# seen = {1, 2, 3}

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
def containsDuplicate(nums):
    seen = set()           # Empty set to track numbers we've seen
    
    for num in nums:       # Go through each number once
        if num in seen:    # If we've seen this number before
            return True    # Duplicate found → return True immediately
        seen.add(num)      # Otherwise, mark this number as seen
    
    return False           # No duplicates found after full scan


"""
Time: O(N)
  - Let N = length of nums.
  - Loop through nums once.
      • Checking membership in a set is O(1) average.
      • Adding to the set is O(1) average.
  - Early return if a duplicate is found, but worst case still scans all N numbers.
  - Overall: O(N).

Space: O(N)
  - One extra structure: set `seen` (numbers we've already seen).
  - Worst case: all numbers are unique (e.g. [1, 2, 3, 4]) → no early return, so the set stores all N numbers.
  - The set is what uses the extra memory — not the loop (num) variable.
  - Overall: O(N).


Interview Answer: Worst Case

Time: O(N)
  - One pass through nums; each set check/add is O(1) average.

Space: O(N)
  - Set holds up to N unique numbers when no duplicate is found.


---
Overview for Each Iteration
Input: nums = [1, 2, 3, 1]

i | num | num in seen | seen (before) | Action         | seen (after)
--|-----|-------------|---------------|----------------|--------------
0 | 1   | False       | {}            | add 1          | {1}
1 | 2   | False       | {1}           | add 2          | {1, 2}
2 | 3   | False       | {1, 2}        | add 3          | {1, 2, 3}
3 | 1   | True        | {1, 2, 3}     | → return True

Final: True (duplicate found)



---
Most IMPORTANT thing to Understand:
    • We just need to detect if ANY number appears more than once.

    • A set is perfect for this because it stores only unique values.

    • If a number is already in the set when we see it again → it's a duplicate.

---
Why this code Works:
    • Data structure: a set tracks which numbers we've seen so far.

    • Technique: For each number, check membership in O(1).  
      If it's already there → duplicate found immediately.

    • Efficiency: Avoids O(N²) comparisons. Single pass + O(1) lookups.

    • Intuition: Like checking attendance—if someone's name appears twice on the list, you catch it instantly.

---
TLDR:
    • Add numbers to a set; if you ever see one that's already inside, return True.

---
Quick Example Walkthrough:

    nums = [1, 2, 3, 1]

    Start: seen = {}

    1 → not in seen → add → seen = {1}
    2 → not in seen → add → seen = {1, 2}
    3 → not in seen → add → seen = {1, 2, 3}
    1 → already in seen → return True

Final Answer: True


"""




# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Solution 2: Dictionary Frequency Counting Approach
from collections import defaultdict

def containsDuplicate(nums):
    count = defaultdict(int)
    
    for num in nums:
        count[num] += 1

    for key, val in count.items():
        if val > 1:
            return True
    return False
    

nums =  [1, 2, 3, 1]
print(containsDuplicate(nums))  # Output True



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Solution 3: Quick Set-Length Trick (One-Liner Solution)
def containsDuplicate(nums):
    return True if len(set(nums)) < len(nums) else False

nums =  [1, 2, 3, 1]
print(containsDuplicate(nums))  # Output True
