# 283. Move Zeroes
"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
    Input: nums = [0, 1, 0, 3, 6]
    Output: [1, 3, 6, 0, 0]

Example 2:
    Input: nums = [0]
    Output: [0]
 
Constraints:
    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1
 
Follow up: Could you minimize the total number of operations done?
    • The Two-Pointer solution already minimizes the number of operations.
"""

# Two Pointers In-Place Solution
def moveZeroes(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
    
    for i in range(slow, len(nums)):
        nums[i] = 0

    return nums

nums = [0, 1, 0, 3, 6]
print(moveZeroes(nums))  # Output: [1, 3, 6, 0, 0]


# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
def moveZeroes(nums):
    slow = 0       # Points to next position to place a non-zero
    
    # Phase 1: Move all non-zero elements to the front
    for fast in range(len(nums)):     # fast scans entire array
        if nums[fast] != 0:           # If we find a non-zero number
            nums[slow] = nums[fast]   # Place it at 'slow' position
            slow += 1                 # Reserve next spot for next non-zero
    
    # Phase 2: Fill the remaining positions with zeros
    for i in range(slow, len(nums)):   # From where non-zeros ended...
        nums[i] = 0                    # ...to the end → set to 0
    
    return nums       # Modified in-place (not required to return)


"""
Time: O(N)
  - Let N = length of nums.
  - Step 1: Single pass with two pointers → O(N).
      • fast scans every element once.
      • slow advances only when a non-zero is found.
  - Step 2: Fill remaining positions with zeros → O(N - slow) ≤ O(N).
  - Overall: O(N).

Space: O(1)
  - Operation is done in-place on the input array.
  - Only a few integer variables (slow, fast, i) are used.
  - Overall: O(1).

  
Interview Answer: Worst Case

Time: O(N)
  - One pass compacts non-zeros, one pass fills zeros.

Space: O(1)
  - In-place modification using constant extra space.

  
---
Overview for Each Iteration
Input: nums = [0, 1, 0, 3, 6]

Phase 1: Move non-zeros forward
fast | nums[fast] | !=0? | slow | Action            | Array state
-----|------------|------|------|-------------------|----------------
0    | 0          | No   | 0    | skip              | [0, 1, 0, 3, 6]
1    | 1          | Yes  | 0    | nums[0]=1, slow=1 | [1, 1, 0, 3, 6]
2    | 0          | No   | 1    | skip              | [1, 1, 0, 3, 6]
3    | 3          | Yes  | 1    | nums[1]=3, slow=2 | [1, 3, 0, 3, 6]
4    | 6          | Yes  | 2    | nums[2]=6, slow=3 | [1, 3, 6, 3, 6]

Phase 2: Fill tail with zeros (i from slow=3 to end)
i | Action       | Final array
--|--------------|-----------------
3 | nums[3]=0    | [1, 3, 6, 0, 6]
4 | nums[4]=0    | [1, 3, 6, 0, 0]

Final: [1, 3, 6, 0, 0]  


---
Most IMPORTANT thing to Understand:
    • We must keep all non-zero numbers in their original order — no rearranging allowed.

    • The goal is to shift all non-zero elements to the front, then fill the rest with zeros.

    • The slow pointer marks where the next non-zero should be placed.

---
Why this code Works:
    • Data structure idea: Two-pointer scan — fast reads, slow writes.

    • Technique: Copy all non-zeros forward (preserves order), then overwrite leftover positions with zeros.

    • Efficiency: Avoids extra arrays and avoids unnecessary swaps → optimal O(N) time, O(1) space.

    • Intuition: It's like packing a suitcase — slide all useful items to the front, then fill extra space with padding (zeros).

---
TLDR:
    • Move all non-zero values forward using a slow pointer, then fill remaining slots with zeros.

---
Quick Example Walkthrough:

    nums = [0, 1, 0, 3, 6]

    Phase 1 — Move non-zeros forward:

        fast=0 → 0  → skip

        fast=1 → 1  → place at slow=0 → nums = [1, 1, 0, 3, 6], slow=1

        fast=2 → 0  → skip

        fast=3 → 3  → place at slow=1 → nums = [1, 3, 0, 3, 6], slow=2
        
        fast=4 → 6  → place at slow=2 → nums = [1, 3, 6, 3, 6], slow=3

    Phase 2 — Fill remaining positions with zero:

        positions 3, 4 → set to 0  
        nums = [1, 3, 6, 0, 0]

    Final Output: [1, 3, 6, 0, 0]

"""







# Two-Pointer Swap (Minimizes Operations)
def moveZeroes_Optimized(nums):
    slow = 0  # Pointer tracking the position of the next ZERO to be swapped

    # fast pointer iterates through the whole array looking for non-zeroes
    for fast in range(len(nums)):
        if nums[fast] != 0:
            # If fast finds a non-zero number, swap it with the element at slow
            # The swap only happens if fast and slow are at different positions.
            if slow != fast:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            
            # Advance slow to track the next zero position
            slow += 1

nums = [0, 1, 0, 3, 12]
print(moveZeroes(nums))

# Time:  O(n)  — each element processed once, swaps only when needed
# Space: O(1)  — in-place




# # Snowball Method (Shift Non-Zeros Forward)
# def moveZeroes(nums):
#     snowball = 0
#     for i in range(len(nums)):
#         if nums[i] == 0:
#             snowball += 1
#         else:
#             nums[i - snowball] = nums[i]
    
#     for i in range(len(nums) - snowball, len(nums)):
#         nums[i] = 0

#     return nums

# nums = [0, 1, 0, 3, 12]
# print(moveZeroes(nums))

# # Time:  O(n)   — one pass to shift, one pass to write zeros
# # Space: O(1)   — in-place
