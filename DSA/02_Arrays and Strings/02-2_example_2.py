# Find Pair with Target Sum in Sorted Array
"""
Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise. 

This problem is similar to Two Sum. (In Two Sum, the input is not sorted).

Example
    Input: nums = [1, 3, 4, 6, 8, 10, 12], target = 14
    Output: True
    Explanation: nums[2] + nums[5] = 4 + 10 = 14 matches the target.
"""

# Solution: Two Pointers: Target Sum Pair Search

def find_pair_sum(nums, target):
    left = 0                    
    right = len(nums) - 1       

    while left < right:         
        curr = nums[left] + nums[right]  

        if curr == target:   
            return True
        elif curr < target:  
            left += 1
        else:                
            right -= 1

    return False   

nums = [1, 3, 4, 6, 8, 10, 12]
target = 14
print(find_pair_sum(nums, target))  
# Output: True -> nums[2] + nums[5] = 4 + 10 = 14 matches the target.


# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
  
def find_pair_sum(nums, target):
    left = 0                 # Start left pointer at index 0
    right = len(nums) - 1    # Start right pointer at last index

    while left < right:      # Continue until pointers meet
        
        # curr is the current sum
        curr = nums[left] + nums[right]  # Sum of elements at pointers

        if curr == target:   # Found a pair
            return True
        elif curr < target:  # Sum too small, need larger number
            left += 1
        else:                # Sum too large, need smaller number
            right -= 1

    return False             # No pair found


"""
Time: O(N)
  - Let N = length of nums.

  - Step 1: Set left = 0 and right = N - 1 → O(1).

  - Step 2: Two pointers scan toward the center → O(N).
      • Loop runs while left < right.
      • Each iteration: compute curr = nums[left] + nums[right] → O(1).
      • Move left or right one step inward → O(1).
      • Each pointer moves at most N times total → at most O(N) iterations.

  - Overall: O(N).


Space: O(1)
  - Only a few integer variables (left, right, curr).
  - No extra data structures.
  - Overall: O(1).


Interview Answer: Worst Case

Time: O(N)
  - Two pointers move inward at most once each — linear scan.

Space: O(1)
  - Only pointer variables are used.


---
Overview for Each Iteration
Input: nums = [1, 3, 4, 6, 8, 10, 12], target = 14

Two pointers squeeze inward: compare curr to target, move left or right.

i | l | r | curr | vs target | Action    | Result
--|---|---|------|-----------|-----------|-------------------
0 | 0 | 6 | 13   | < 14      | left+=1   | continue (l=1, r=6)
1 | 1 | 6 | 15   | > 14      | right-=1  | continue (l=1, r=5)
2 | 1 | 5 | 13   | < 14      | left+=1   | continue (l=2, r=5)
3 | 2 | 5 | 14   | == 14     | return True | True (4+10=14)

Final: True — nums[2] + nums[5] = 4 + 10 = 14


---
Most IMPORTANT thing to Understand:
    • Find any two numbers in a sorted array that add up to target.

    • left starts at the smallest value, right at the largest.

    • curr = nums[left] + nums[right] is the current pair sum.

    • Too small → move left right (need a bigger number).

    • Too big → move right left (need a smaller number).

    • Equal to target → pair found → return True.


---
Why this code Works:
    • Two pointers:
        • left = smallest candidate still in play.
        • right = largest candidate still in play.

    • Sorted array unlocks the move rules:
        • curr < target → every pair with current left is too small if we keep same left with smaller rights — so increase left.
        • curr > target → every pair with current right is too big if we keep same right with larger lefts — so decrease right.

    • Efficiency:
        • Brute force checks all pairs → O(N²).
        • Two pointers eliminate impossible pairs each step → O(N).

    • Intuition:
        • Like squeezing a range — shrink from the side that can't work.


---
TLDR:
    • Start at both ends of the sorted array; if the sum is too small move left up, too big move right down, equal means you found a pair.


---
Quick Example Walkthrough:
    nums = [1, 3, 4, 6, 8, 10, 12], target = 14

    Step 1: left = 0, right = 6

    Step 2: Adjust pointers
        • 1 + 12 = 13 < 14 → left = 1
        • 3 + 12 = 15 > 14 → right = 5
        • 3 + 10 = 13 < 14 → left = 2
        • 4 + 10 = 14 == target → return True

    Final Answer: True (4 + 10 = 14)


---
Full Example Walkthrough:
    nums = [1, 3, 4, 6, 8, 10, 12], target = 14

    Starting State:
        left = 0, right = 6
        nums[left] = 1, nums[right] = 12

    Loop Iteration 1:
        curr = 1 + 12 = 13
        13 < 14 → sum too small → left += 1

        Now:
            left = 1, right = 6
            nums[1] = 3, nums[6] = 12

    --------------------------------------------------

    Loop Iteration 2:
        curr = 3 + 12 = 15
        15 > 14 → sum too large → right -= 1

        Now:
            left = 1, right = 5
            nums[1] = 3, nums[5] = 10

    --------------------------------------------------

    Loop Iteration 3:
        curr = 3 + 10 = 13
        13 < 14 → sum too small → left += 1

        Now:
            left = 2, right = 5
            nums[2] = 4, nums[5] = 10

    --------------------------------------------------

    Loop Iteration 4:
        curr = 4 + 10 = 14
        14 == target → return True

        Meaning: nums[2] + nums[5] = 4 + 10 = 14 — pair found.


---
🧠 First Time? Thoughts → Code

Read the problem (10 sec)
    • Does any pair in the array add up to target?

    • Array is sorted — that's the hint that unlocks two pointers (not required for brute force, but changes everything).


Start naive (totally fine)
    • Check every pair with nested loops.
    • Say out loud: "Try nums[i] + nums[j] for all i and j."
    • Time: O(N²).


The one insight that unlocks the optimal code
    • Sorted order means the smallest + largest sum tells you which direction to go.
    • Too small → you need a bigger number → move left pointer right.
    • Too big → you need a smaller number → move right pointer left.
    • You never need to recheck pairs you ruled out.


Why two pointers?
    • Only works because the array is sorted — you know what's "next bigger" and "next smaller."
    • Unsorted array → hash map (Two Sum) instead.


Thought → line of code
    right = len(nums) - 1
        → "Start with smallest + largest — widest possible range."

    curr = nums[left] + nums[right]
        → "What's the current pair sum?"

    elif curr < target: left += 1
        → "Sum too small — drop the small end, try a bigger left value."

    else: right -= 1
        → "Sum too big — drop the large end, try a smaller right value."


Memory hook (one sentence)
    • Sorted array + two ends: too small move left up, too big move right down.


Would you arrive at this cold?
    • Immediately: nested loops O(N²), or hash map if you've seen Two Sum.
    • After noticing "sorted": opposite-end pointers instead of hash map.
    • Bookkeeping: left=0, right=len-1, curr comparison — standard setup.
    • Real insight: sorted order lets you eliminate half the search space each step.



---------------------------------------------------
Q: When does the loop stop and return True?
    • When nums[left] + nums[right] == target.

    • At that moment, the function immediately returns True and exits — no further pairs are checked.

    
Q: When does the loop stop and return False?
    • When the left and right pointers cross (left >= right).

    • This means every possible pair has been checked, and no pair sums to the target.

"""



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force — Nested loops (check every pair)

def find_pair_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return True

    return False


nums = [1, 3, 4, 6, 8, 10, 12]
target = 14
print(find_pair_sum_brute(nums, target))  # True


"""
Time: O(N²)
  - Let N = length of nums.

  - Step 1: Outer loop picks first index i → O(N).

  - Step 2: Inner loop picks second index j > i → O(N) per i.
      • Check nums[i] + nums[j] == target → O(1).

  - Combined: O(N × N).
  - Overall: O(N²).


Space: O(1)
  - Only loop indices i and j.
  - Overall: O(1).


Interview Answer: Worst Case

Time: O(N²)
  - Every pair of indices is checked in the worst case.

Space: O(1)
  - Only index variables.


---
Overview for Each Iteration
nums = [1, 3, 4, 6, 8, 10, 12], target = 14

    i = 0, j = 1 → 1 + 3 = 4 ≠ 14
    i = 0, j = 2 → 1 + 4 = 5 ≠ 14
    ... (keep trying pairs with i = 0)

    i = 1, j = 2 → 3 + 4 = 7 ≠ 14
    i = 1, j = 3 → 3 + 6 = 9 ≠ 14
    ... (keep trying pairs with i = 1)

    i = 2, j = 3 → 4 + 6 = 10 ≠ 14
    i = 2, j = 4 → 4 + 8 = 12 ≠ 14
    i = 2, j = 5 → 4 + 10 = 14 == target → return True

Final: True — nums[2] + nums[5] = 4 + 10 = 14

"""

