# 704. Binary Search
"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

Example 2:
    Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1

Constraints:
    1 <= nums.length <= 104
    -104 < nums[i], target < 104
    All the integers in nums are unique.
    nums is sorted in ascending order.
"""
# Solution: https://leetcode.com/problems/binary-search/description/

# Approach 1: Find the Exact Value
def search(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1                 
        else:
            right = mid - 1
    
    return -1

nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(search(nums, target))  # Output: 4


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def search(nums, target):
    left = 0                   # Left boundary of search range
    right = len(nums) - 1      # Right boundary of search range
    
    while left <= right:       # Continue while search range is valid
        mid = (left + right) // 2   # Find middle index (integer division)
        
        if nums[mid] == target:     # Found target exactly
            return mid              # Return its index
        
        elif nums[mid] < target:    # Target is in right half
            left = mid + 1          # Discard left half (including mid)
        
        else:                       # Target is in left half
            right = mid - 1         # Discard right half (including mid)
    
    return -1                  # Target not found after search


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
def search(nums, target):
    # Set the left and right boundaries
    left = 0
    right = len(nums) - 1
    
    # Under this condition
    while left <= right:
        # Get the middle index and the middle value.
        mid = (left + right) // 2
        
        # Case 1, return the middle index.
        if nums[mid] == target:
            return mid
        # Case 2, discard the smaller half.
        elif nums[mid] < target:
            left = mid + 1                 
        # Case 3, discard the larger half.         
        else:
            right = mid - 1
    
    # If we finish the search without finding target, return -1.
    return -1

nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(search(nums, target))  # Output: 4


"""
Time: O(log N)
  - Let N = length of nums.
  - Each iteration of the while loop cuts the search space in half.
  - Comparisons and pointer updates inside the loop are O(1).
  - Maximum number of iterations is log₂(N).
  - Overall: O(log N).

Space: O(1)
  - Uses only a few integer variables: left, right, mid.
  - No additional data structures or recursion.
  - Overall: O(1).

  
Interview Answer: Worst Case

Time: O(log N)
  - Binary search halves the array each step.

Space: O(1)
  - Constant extra space for pointers.


---
Overview for Each Iteration
Input: nums = [-1, 0, 3, 5, 9, 12], target = 9

i | l | r | mid | nums[mid] | nums[mid] vs target | Action      | Search range after
--|---|---|-----|-----------|---------------------|-------------|---------------------
0 | 0 | 5 | 2   | 3         | 3 < 9               | l = mid + 1 | [3, 5] (indices 3-5)
1 | 3 | 5 | 4   | 9         | 9 == 9              | return 4    | —

Final: 4


---
Most IMPORTANT thing to Understand:
    • Binary search repeatedly cuts the search space in half — that's why it is O(log n).

    • We always compare the target to the middle element:
        • If equal → found.
        • If smaller → search left half.
        • If larger → search right half.

    • The loop continues while left ≤ right — meaning the search range is still valid.

---
Why this code Works:
    • Data structure requirement: nums **must be sorted**, or the mid comparison logic would not work.

    • Technique: Halve the search space each time by moving either left or right pointer based on mid comparison.

    • Efficiency: Each step eliminates half the remaining elements → O(log n), far faster than scanning linearly.

    • Intuition: Like looking up a word in a dictionary — check the midpoint and decide which half to continue searching.

---
TLDR:
    • Repeatedly check the middle of the array and shrink the search range based on whether the target is bigger or smaller.

---
Quick Example Walkthrough:

    nums = [-1, 0, 3, 5, 9, 12], target = 9

    Initial:
        left = 0, right = 5

    Step 1:
        mid = (0 + 5) // 2 = 2
        nums[2] = 3
        3 < 9 → target is in the RIGHT half
        left = 3

    Step 2:
        left = 3, right = 5
        mid = (3 + 5) // 2 = 4
        nums[4] = 9
        Found target → return 4

    Final Answer: 4

    




---
Q: Why do we use `while l <= r:` in exact-value binary search?

    • `l` and `r` define the remaining search range.

    • When `l == r`, there is one last element that could be the target.

    • `while l <= r:` ensures this final element is checked.

    • Using `while l < r:` would stop early and skip it.

    • Skipping that check can miss a valid target.

→ Therefore, `while l <= r:` guarantees every possible index is examined.
    


---
Walkthrough: Why `while l <= r` matters:

Goal: find target = 3 in nums = [1, 3]
    Index:   0  1
    nums =  [1, 3]

------------------------------------------------------------
Correct loop: `while l <= r`
------------------------------------------------------------
Start:
    l = 0
    r = 1

Step 1:
    l <= r  → 0 <= 1  ✅ keep going
    mid = (0 + 1) // 2 = 0
    nums[mid] = nums[0] = 1

    1 < 3, so the target must be on the RIGHT side.
    Move l:
        l = mid + 1 = 1

Step 2:
    l <= r  → 1 <= 1 ✅ keep going (this is the IMPORTANT part!)
    mid = (1 + 1) // 2 = 1
    nums[mid] = nums[1] = 3

    3 == 3 ✅ found it!
    return 1

So we correctly return index 1.

------------------------------------------------------------
Wrong loop: `while l < r`
------------------------------------------------------------
Start:
    l = 0
    r = 1

Step 1:
    l < r  → 0 < 1 ✅ keep going
    mid = (0 + 1) // 2 = 0
    nums[mid] = 1

    1 < 3, so move l:
        l = mid + 1 = 1

Step 2:
    l < r  → 1 < 1 ❌ False → STOP LOOP

We STOP without ever checking nums[1] (which is 3).
Then we return -1 (not found) ❌ WRONG

------------------------------------------------------------
Takeaway
------------------------------------------------------------
  • When l == r, there is 1 last box left to open.
  • `l <= r` opens that last box.
  • `l < r` stops early and skips it.


"""











# Approach 2: Find Upper bound
def search(nums, target):
    # Set the left and right boundaries
    left = 0
    right = len(nums)
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid

    if left > 0 and nums[left - 1] == target:
        return left - 1
    else:
        return -1
        
nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(search(nums, target))  # Output: 4


# Approach 3: Find Lower bound
def search(nums, target):
    # Set the left and right boundaries
    left = 0
    right = len(nums)
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    
    if left < len(nums) and nums[left] == target:
        return left
    else:
        return -1
        
nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(search(nums, target))  # Output: 4


# Approach 4: Use built-in tools.
import bisect

def search(nums, target):
    # Find the insertion position `idx`.
    idx = bisect.bisect_right(nums, target)

    if idx > 0 and nums[idx - 1] == target:
        return idx - 1
    else:
        return -1
    
nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(search(nums, target))  # Output: 4
