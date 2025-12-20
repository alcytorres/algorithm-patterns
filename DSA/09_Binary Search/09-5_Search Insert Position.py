# 35. Search Insert Position
"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

# Solution: https://leetcode.com/problems/search-insert-position/description/

Example 1:
    Input: nums = [1, 3, 5, 6], target = 5
    Output: 2

Example 2:
    Input: nums = [1, 3, 5, 6], target = 2
    Output: 1

Example 3:
    Input: nums = [1, 3, 5, 6], target = 7
    Output: 4
 
Constraints:
    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums contains distinct values sorted in ascending order.
    -104 <= target <= 104
"""


def searchInsert(nums, target):
    l = 0
    r = len(nums) - 1
    
    while l <= r:
        mid = (l + r) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1                 
        else:
            r = mid - 1

    return l


nums = [1, 3, 5, 6]
target = 5
print(searchInsert(nums, target))  # Output: 2

nums = [1, 3, 5, 6]
target = 2
print(searchInsert(nums, target))  # Output: 1


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def searchInsert(nums, target):
    l = 0                 # Left boundary of search range
    r = len(nums) - 1     # Right boundary of search range
    
    while l <= r:         # Continue while search range is valid
        mid = (l + r) // 2      # Calculate middle index
        
        if nums[mid] == target:    # Target found exactly
            return mid             # Return its index
        
        elif nums[mid] < target:   # Target is larger → search right half
            l = mid + 1            # Move left boundary past mid
        
        else:                # Target is smaller → search left half
            r = mid - 1      # Move right boundary before mid
    
    return l             # Target not found → l is insertion point


"""
Time: O(log N)
  - Let N = length of nums.
  - Binary search repeatedly halves the search space.
  - Each loop iteration does O(1) work (comparison + pointer updates).
  - Maximum iterations ≈ log₂(N).
  - Overall: O(log N).

Space: O(1)
  - Uses only a few integer variables (l, r, mid).
  - No extra data structures or recursion.
  - Overall: O(1).

  
Interview Answer: Worst Case

Time: O(log N)
  - Binary search halves the array each step.

Space: O(1)
  - Constant extra space for pointers.

  

---
Overview for Each Iteration
Input: nums = [1, 3, 5, 6], target = 5

i | l | r | mid | nums[mid] | comparison | Action      | Result
--|---|---|-----|-----------|------------|-------------|-------
0 | 0 | 3 | 1   | 3         | 3 < 5      | l = 2       | continue
1 | 2 | 3 | 2   | 5         | 5 == 5     | return 2    | 2

Final: 2


---
Overview for Each Iteration
Input: nums = [1, 3, 5, 6], target = 2

i | l | r | mid | nums[mid] | comparison | Action      | Result
--|---|---|-----|-----------|------------|-------------|-------
0 | 0 | 3 | 1   | 3         | 3 > 2      | r = 0       | continue
1 | 0 | 0 | 0   | 1         | 1 < 2      | l = 1       | continue
— | 1 | 0 | —   | —         | l > r      | return l=1  | 1

Final: 1


---
Overview for Each Iteration
Input: nums = [1, 3, 5, 6], target = 7

i | l | r | mid | nums[mid] | comparison | Action      | Result
--|---|---|-----|-----------|------------|-------------|-------
0 | 0 | 3 | 1   | 3         | 3 < 7      | l = 2       | continue
1 | 2 | 3 | 2   | 5         | 5 < 7      | l = 3       | continue
2 | 3 | 3 | 3   | 6         | 6 < 7      | l = 4       | continue
— | 4 | 3 | —   | —         | l > r      | return l=4  | 4

Final: 4
  


---
Most IMPORTANT thing to Understand:
    • This is binary search, but with a twist: if the target is NOT found, we return the position where it *should* be inserted.

    • The key rule: when the binary search finishes, `l` (left pointer) ALWAYS ends up at the correct insertion index.

    • Why? Because `l` only moves forward when nums[mid] < target — meaning `l` always marks the first index where target could fit.

---
Why this code Works:
    • Standard binary search shrinks the search space using mid:
        • nums[mid] == target → return mid.
        • nums[mid] < target → move left pointer right.
        • nums[mid] > target → move right pointer left.

    • When the loop ends (target not found):
        • `l` is the first index where target is greater than all values before it.
        • `r` is behind `l`, so `l` naturally becomes the insertion position.

    • Efficiency: Same as binary search — cuts search range in half each time → O(log n).

    • Intuition: You're finding where the target *belongs* in the sorted order, even if it doesn't exist.

---
TLDR:
    • Run binary search; if target isn't found, return the final `l` pointer because it marks the correct sorted insertion index.

---
Quick Example Walkthrough:

Example A:
    nums = [1, 3, 5, 6], target = 5

    l = 0, r = 3
    mid = 1 → nums[1] = 3 < 5 → l = 2
    mid = (2+3)//2 = 2 → nums[2] = 5 → found

    Final Answer: 2


Example B:
    nums = [1, 3, 5, 6], target = 2

    l = 0, r = 3
    mid = 1 → nums[1] = 3 > 2 → r = 0
    mid = (0+0)//2 = 0 → nums[0] = 1 < 2 → l = 1
    Loop ends (l=1, r=0)

    Final Answer: 1  (correct insert position)


Example C:
    nums = [1, 3, 5, 6], target = 7

    l = 0, r = 3
    mid = 1 → 3 < 7 → l = 2
    mid = 2 → 5 < 7 → l = 3
    mid = 3 → 6 < 7 → l = 4
    Loop ends (l=4)

    Final Answer: 4  (insert at end)


"""
