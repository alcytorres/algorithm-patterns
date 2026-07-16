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

Solution: https://leetcode.com/problems/move-zeroes/description/
"""

# Solution: Two Pointers In-Place

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
print(moveZeroes(nums))
# Output: [1, 3, 6, 0, 0] → Phase 1 packs non-zeros to the front; Phase 2 fills the rest with 0


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
    
    return nums       # Modified in-place


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
    • We keep two pointers: slow marks the next spot to place a non-zero, fast scans every element.

    • Every time fast finds a non-zero, we copy it to the slow spot and move slow forward.

    • After the first pass, all non-zeros sit at the front in their original order, and slow points to the first "leftover" spot.

    • Whatever positions come after slow must become 0, so a second pass fills them with zeros.

---
Why this code Works:
    • Two pointers role:
        • slow = the write position (next place a non-zero belongs).
        • fast = the read position (currently inspected element).

    • If nums[fast] != 0:
        • We found a non-zero, so write it at slow and advance slow.
        • This "packs" non-zeros toward the front without breaking their order.

    • If nums[fast] == 0:
        • Do nothing, only fast moves on.
        • We simply skip zeros during the packing phase.

    • Second pass:
        • Everything from slow to the end is filler.
        • Set those positions to 0 to complete the move.

    • Efficiency:
        • Phase 1 scans the array once → O(N).
        • Phase 2 fills the tail once → O(N).
        • Time: O(N). Space: O(1), all in-place.

    • Intuition:
        • Think of slow as a "shelf pointer" where you neatly stack every non-zero book you pick up.
        • Once all books are stacked, you fill the empty shelf space with zeros.

---
TLDR:
    • It packs every non-zero to the front in order with a write pointer, then fills the remaining tail with zeros — all in-place in O(N).


---
Quick Example Walkthrough:
    nums = [0, 1, 0, 3, 6]

    Step 1: Initialize slow = 0, then scan with fast
        • fast=0, nums[0]=0 → zero, skip
        • fast=1, nums[1]=1 → non-zero, nums[0]=1, slow=1
        • fast=2, nums[2]=0 → zero, skip
        • fast=3, nums[3]=3 → non-zero, nums[1]=3, slow=2
        • fast=4, nums[4]=6 → non-zero, nums[2]=6, slow=3

    Step 2: Array after packing → [1, 3, 6, 3, 6], slow=3

    Step 3: Fill from index slow(3) to end with 0
        • nums[3]=0, nums[4]=0

    Final Answer: [1, 3, 6, 0, 0]


---
Full Example Walkthrough:
    nums = [0, 1, 0, 3, 6]

    Starting State:
        slow = 0
        nums = [0, 1, 0, 3, 6]

    Phase 1 — Pack non-zeros to the front:

    Loop Iteration 1:
        Compare:
            nums[fast] != 0 → nums[0] = 0 → NO (it IS zero)

        Since it is zero:
            slow does NOT move
            nothing is written

        Now:
            slow = 0, fast = 0
            nums = [0, 1, 0, 3, 6]

    --------------------------------------------------

    Loop Iteration 2:
        Compare:
            nums[1] = 1 != 0 → YES (non-zero)

        Since it is non-zero:
            nums[slow] = nums[fast] → nums[0] = 1
            slow += 1 → slow = 1

        Now:
            slow = 1, fast = 1
            nums = [1, 1, 0, 3, 6]

    --------------------------------------------------

    Loop Iteration 3:
        Compare:
            nums[2] = 0 != 0 → NO (it IS zero)

        slow stays the same, nothing written.

        Now:
            slow = 1, fast = 2
            nums = [1, 1, 0, 3, 6]

    --------------------------------------------------

    Loop Iteration 4:
        Compare:
            nums[3] = 3 != 0 → YES (non-zero)

        Since it is non-zero:
            nums[slow] = nums[fast] → nums[1] = 3
            slow += 1 → slow = 2

        Now:
            slow = 2, fast = 3
            nums = [1, 3, 0, 3, 6]

    --------------------------------------------------

    Loop Iteration 5:
        Compare:
            nums[4] = 6 != 0 → YES (non-zero)

        Since it is non-zero:
            nums[slow] = nums[fast] → nums[2] = 6
            slow += 1 → slow = 3

        Now:
            slow = 3, fast = 4
            nums = [1, 3, 6, 3, 6]

    --------------------------------------------------

    Phase 2 — Fill the rest with zeros (from index slow = 3):

        nums[3] = 0 → [1, 3, 6, 0, 6]
        nums[4] = 0 → [1, 3, 6, 0, 0]

    --------------------------------------------------

    Final Check:
        Return nums → [1, 3, 6, 0, 0]

        This means:
            All non-zeros kept their original order at the front,
            and every zero was pushed to the end — done in-place.

"""



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Same pattern as Remove Element (02-26) — slow/fast = write/read

def moveZeroes(nums):
    write = 0
    
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1
    
    for i in range(write, len(nums)):
        nums[i] = 0

    return nums

"""
slow / fast  vs  write / read  — same idea, different names

    • fast  = read   → scans the whole array (looks at each element)
    • slow  = write  → next spot to place a "keeper" at the front

    • fast finds what to look at; slow finds where to put what you keep


Same pattern as Remove Element (27):
    Move Zeroes (this file)              Remove Element (02-26)
    ─────────────────────                ────────────────────────
    fast scans nums                      fast scans nums
    slow = where next keeper goes        slow = where next keeper goes
    keep if nums[fast] != 0              keep if nums[fast] != val
    nums[slow] = nums[fast]              nums[slow] = nums[fast]
    slow += 1                            slow += 1

    • Move Zeroes: Phase 2 fills the tail with 0s — judge needs the full array correct.
    • Remove Element: no Phase 2 — return slow; judge only checks nums[:slow], tail is junk.

    • Phase 1 of Move Zeroes IS Remove Element with val = 0 (if you stopped before Phase 2).

    • Both: one pass to pack keepers at the front, O(N) time, O(1) space.

Memory hook:
    If you know this slow/fast loop, you already know Remove Element — same loop, just "!= val" and skip Phase 2.

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
print(moveZeroes_Optimized(nums))
# Output: [1, 3, 12, 0, 0] → Swap each non-zero forward with slow; fewer writes than copy + fill

# Time:  O(n)  — each element processed once, swaps only when needed
# Space: O(1)  — in-place



