# 189. Rotate Array
"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
    Input: nums = [1, 2, 3, 4, 5], k = 2
    Output: [4, 5, 1, 2, 3]
    Explanation:
    rotate 1 steps to the right: [5, 1, 2, 3, 4]
    rotate 2 steps to the right: [4, 5, 1, 2, 3]

Example 2:
    Input: nums = [-1, -100, 3, 99], k = 2
    Output: [3, 99, -1, -100]
    Explanation: 
    rotate 1 steps to the right: [99,-1,-100,3]
    rotate 2 steps to the right: [3,99,-1,-100]
    
Constraints:
    1 <= nums.length <= 105
    -231 <= nums[i] <= 231 - 1
    0 <= k <= 105
    
Follow up:
    Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
    Could you do it in-place with O(1) extra space?
"""

# Slice and Rebuild Rotation
def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    # Don't rotate more than needed (k can be huge)
    k = k % n
    
    # Slice and rebuild
    nums[:] = nums[-k:] + nums[:-k]

    return nums

nums = [1, 2, 3, 4, 5]
k = 2
print(rotate(nums, k))  # Output: [4, 5, 1, 2, 3]

# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
def rotate(nums, k):
    n = len(nums)              # Length of array
    k = k % n                  # Reduce k (handles k > n cases)
    
    # Slice last k elements + first (n-k) elements
    nums[:] = nums[-k:] + nums[:-k]  # Reassign to nums for in-place feel
    
    # No return needed (modifies nums in-place), but return for printing
    return nums


"""
[1, 2, 3 | 4, 5]
         ↓
[5 | 1, 2, 3, 4]
         ↓
[4, 5 | 1, 2, 3]


Time: O(N)
  - Let N = length of nums.
  - Computing k % N is O(1).
  - Slicing nums[-k:] and nums[:-k] each takes O(N).
  - Rebuilding the array with concatenation and assignment also takes O(N).
  - Overall: O(N).

Space: O(N)
  - Slicing creates new lists of size up to N.
  - Even though nums is modified in-place, extra space is used during slicing.
  - Overall: O(N).

  
Interview Answer: Worst Case

Time: O(N)
  - Build the rotated array using slicing.

Space: O(N)
  - Extra space used by sliced arrays.



---
Most IMPORTANT thing to Understand:
    • Rotating right by k means the last k numbers move to the front, and everything else shifts right.

    • The rotated order is always: (last k elements) + (first n-k elements).

    • k can be bigger than n, so k = k % n shrinks it to the “same rotation” (ex: k=8 on n=5 is same as k=3).

---
Why this code Works:
    • nums[-k:] = the exact chunk that must become the new front (the last k elements).

    • nums[:-k] = everything that stays after that chunk.

    • nums[:] = ... writes back into the same list object (true in-place update for LeetCode).

    • Efficiency: we avoid shifting one step at a time (which can be O(n*k)) and do one rebuild in O(n).

---
TLDR:
    • Compute k % n, then overwrite nums with nums[-k:] + nums[:-k].

---
Quick Example Walkthrough:

Example A:
    nums = [1, 2, 3, 4, 5], k = 2
    n = 5
    k = 2 % 5 = 2

    nums[-2:]  -> [4, 5]
    nums[:-2]  -> [1, 2, 3]

    nums[:] = [4, 5] + [1, 2, 3]
    nums becomes [4, 5, 1, 2, 3]

    Final Answer: [4, 5, 1, 2, 3]


Example B (k bigger than n):
    nums = [1, 2, 3, 4, 5], k = 7
    n = 5
    k = 7 % 5 = 2   # same as rotating by 2

    nums[-2:]  -> [4, 5]
    nums[:-2]  -> [1, 2, 3]

    Final Answer: [4, 5, 1, 2, 3]

"""




# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Three-Reversal Rotation Using Slicing
def rotate(nums, k):
    n = len(nums)
    k %= n                     # Reduce k

# Three reversals = right rotate
nums.reverse()             # Whole array
nums[:k] = nums[:k][::-1]  # First k
nums[k:] = nums[k:][::-1]  # Rest

nums = [1, 2, 3, 4, 5]
k = 2
print(rotate(nums, k))
# Output: [4, 5, 1, 2, 3]
"""
Time: O(n)
Each reverse/slice touches elements once

Space: O(n)
nums[:k][::-1] and nums[k:][::-1] create temporary lists
"""
# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
def rotate(nums, k):
    n = len(nums)              # Length of array
    k %= n                     # Reduce k (k > n is same as k % n)
    
    # Step 1: Reverse entire array
    nums.reverse()             # e.g., [1,2,3,4,5,6,7] → [7,6,5,4,3,2,1]
    
    # Step 2: Reverse first k elements
    nums[:k] = nums[:k][::-1]  # Reverse 0 to k-1 → brings last k to front in order
    
    # Step 3: Reverse remaining elements
    nums[k:] = nums[k:][::-1]  # Reverse k to end → fixes order of original front
    
    # Done! Modified in-place




# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Three-Reversal In-Place Rotation (Optimal Solution)
def rotate(nums, k):
    n = len(nums)
    k %= n
    
    def rev(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    
    rev(0, n-1)      # Reverse all
    rev(0, k-1)      # Reverse first k
    rev(k, n-1)      # Reverse rest


nums = [1, 2, 3, 4, 5]
k = 2
print(rotate(nums, k))
# Output: [4, 5, 1, 2, 3]

"""
Time: O(n)
Each element swapped a constant number of times

Space: O(1)
Only variables, no extra data structures
"""
# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
def rotate(nums, k):
    n = len(nums)              # Length of array
    k %= n                     # Reduce k (k > n unnecessary)
    
    def rev(l, r):             # Helper to reverse subarray from l to r
        while l < r:           # Swap until pointers meet
            nums[l], nums[r] = nums[r], nums[l]  # In-place swap
            l += 1             # Move left inward
            r -= 1             # Move right inward
    
    rev(0, n-1)                # Step 1: Reverse entire array
    rev(0, k-1)                # Step 2: Reverse first k elements
    rev(k, n-1)                # Step 3: Reverse remaining elements