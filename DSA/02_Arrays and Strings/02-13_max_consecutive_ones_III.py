# 1004. Max Consecutive Ones III 

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# Example:
    # Input: nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2
    # Output: 6
    # Explanation: nums[5] and nums[10] were flipped from 0 to 1. We are left with [1, 1, 1, 1, 1, 1] 

# Solution: https://leetcode.com/problems/max-consecutive-ones-iii/solutions/409192/max-consecutive-ones-iii/

def longestOnes(nums, k):
    left = ans = curr = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            curr += 1
        
        while curr > k:
            if nums[left] == 0:
                curr -= 1
            left += 1
        
        ans = max(ans, right - left + 1)
    
    return ans

nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
print(longestOnes(nums, k))
# Output: 6 → The longest stretch of 1s after flipping at most 2 zeros is 6:

# 2 Valid Subarrays:
    #  [0, 0, 1, 1, 1, 1], formed by flipping the zeros at indices 4 and 5
    #  [0, 1, 1, 1, 1, 0], formed by flipping the zeros at indices 5 and 10


"""
Time: O(N)
  - Let N = length of nums.
  - The right pointer expands the window across the array → O(N).
  - The left pointer only moves forward when more than k zeros are in the window.
  - Each element is visited at most twice (once added, once removed).
  - Overall: O(N).

Space: O(1)
  - Only a few integer variables (left, right, curr, ans) are used.
  - No extra data structures are needed.
  - Overall: O(1).

  
Interview Answer: Worst Case

Time: O(N)
  - Sliding window examines each element at most twice.

Space: O(1)
  - Constant space for pointers and zero counter.



Overview for Each Iteration
Input: nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2

Step: Find max consecutive 1's with at most k flips using sliding window
r | nums[r] | curr | curr > k | l | nums[l] | Action              | ans
--|---------|------|----------|---|---------|---------------------|------
- | -       | 0    | -        | 0 | -       | -                   | 0
0 | 1       | 0    | No       | 0 | -       | ans=max(0,0-0+1)=1  | 1
1 | 1       | 0    | No       | 0 | -       | ans=max(1,1-0+1)=2  | 2
2 | 1       | 0    | No       | 0 | -       | ans=max(2,2-0+1)=3  | 3
3 | 0       | 1    | No       | 0 | -       | ans=max(3,3-0+1)=4  | 4
4 | 0       | 2    | No       | 0 | -       | ans=max(4,4-0+1)=5  | 5
5 | 0       | 3    | Yes      | 0 | 1       | l+=1                | 5
  |         | 3    | Yes      | 1 | 1       | l+=1                | 5
  |         | 3    | Yes      | 2 | 1       | l+=1                | 5
  |         | 3    | Yes      | 3 | 0       | curr-=1, l+=1       | 5
  |         | 2    | No       | 4 | -       | ans=max(5,5-4+1)=5  | 5
6 | 1       | 2    | No       | 4 | -       | ans=max(5,6-4+1)=5  | 5
7 | 1       | 2    | No       | 4 | -       | ans=max(5,7-4+1)=5  | 5
8 | 1       | 2    | No       | 4 | -       | ans=max(5,8-4+1)=5  | 5
9 | 1       | 2    | No       | 4 | -       | ans=max(6,9-4+1)=6  | 6
10| 0       | 3    | Yes      | 4 | 0       | curr-=1, l+=1       | 6
  |         | 2    | No       | 5 | -       | ans=max(6,10-5+1)=6 | 6

Final: 6

2 Valid Subarrays:
    • [0, 0, 1, 1, 1, 1] → formed by flipping the zeros at indices 4 and 5
    • [0, 1, 1, 1, 1, 0] → formed by flipping the zeros at indices 5 and 10


Most IMPORTANT thing to Understand:
    • We want the longest stretch of 1s, but we can flip at most k zeros into 1s.

    • We use a sliding window: expand with right, shrink with left if too many zeros are inside.

    • The current window is always valid (≤ k zeros), and we track the maximum length.

    
Why this code Works:
    • curr: counts how many zeros are in the current window.

    • Sliding window: grow window by moving right; if curr > k, shrink window from the left until valid.

    • Efficiency: each element is added/removed once → O(n) time, O(1) space.

    • Intuition: Like stretching a rubber band over the array — expand until it breaks the “≤ k zeros” rule, then pull in the left side to fix it.

    
TLDR
    • Keep a window with at most k zeros. Expand right, shrink left if needed. Track the largest valid window size.

    
Quick Example Walkthrough:
    nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2

    Step 1: Expand → [1,1,1,0,0], zeros = 2 → window length = 5.

    Step 2: Add next 0 → zeros = 3 → shrink left until zeros = 2.

    Step 3: Expand with [1,1,1,1] → zeros = 2 → window length = 6 (best).

    Step 4: Add final 0 → zeros = 3 → shrink again, still best = 6.

Final Answer: 6 (subarray [1, 1, 1, 1, 1, 1]).



---
Q: Which subarray of length 6 is the final answer?
    • Both [4..9] (flip nums[4] & nums[5]) and [5..10] (flip nums[5] & nums[10]) give a streak of 6 ones.

    • LeetCode's official explanation shows [5..10] as the answer (flipping nums[5] and nums[10]).

	• The algorithm only returns the max length (6), not which subarray produced it.

"""


# ––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def longestOnes(nums, k):
    left = ans = curr = 0  # Left bound, max length, count of 0's in window
    
    for right in range(len(nums)):  # Iterate right pointer over array
        if nums[right] == 0:       # If current element is 0
            curr += 1              # Increment 0's count
        
        while curr > k:            # Shrink window if 0's exceed k
            if nums[left] == 0:    # If leftmost element is 0
                curr -= 1          # Decrement 0's count
            left += 1              # Move left pointer forward
        
        ans = max(ans, right - left + 1)  # Update max window size
    
    return ans   # Return the maximum length of consecutive 1's possible



# ––––––––––––––––––––––––––––––––––––––––––––––
# Best Solution

def longestOnes(nums, k):
    left = ans = curr = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            curr += 1
        
        while curr > k:
            if nums[left] == 0:
                curr -= 1
            left += 1
        
        ans = max(ans, right - left + 1)
    
    return ans

nums = [1, 0, 0, 1, 1, 0, 1]
k = 2
print(longestOnes(nums, k))
# Output: 5 → The longest stretch of 1s after flipping at most 2 zeros is 5:

# 2 valid Subarrays:
    #  [1, 0, 0, 1, 1] → formed by flipping the zeros at indices 1 and 2
    #  [0, 1, 1, 0, 1] → formed by flipping the zeros at indices 2 and 5


"""
Overview for Each Iteration
Input: nums = [1, 0, 0, 1, 1, 0, 1], k = 2

Step: Find max consecutive 1's with at most k flips using sliding window
r  | nums[r] | curr | curr > k | l  | nums[l] | Action              | ans
---|---------|------|----------|----|---------|---------------------|----
0  | 1       | 0    | False    | 0  | -       | ans=max(0,0-0+1)=1  | 1
1  | 0       | 1    | False    | 0  | -       | ans=max(1,1-0+1)=2  | 2
2  | 0       | 2    | False    | 0  | -       | ans=max(2,2-0+1)=3  | 3
3  | 1       | 2    | False    | 0  | -       | ans=max(3,3-0+1)=4  | 4
4  | 1       | 2    | False    | 0  | -       | ans=max(4,4-0+1)=5  | 5
5  | 0       | 3    | True     | 0  | 1       | l+=1                | 5
   |         | 3    | True     | 1  | 0       | curr-=1, l+=1       | 5
   |         | 2    | False    | 2  | -       | ans=max(5,5-2+1)=5  | 5
6  | 1       | 2    | False    | 2  | -       | ans=max(5,6-2+1)=5  | 5

Final: 5

2 valid Subarrays:
    [1, 0, 0, 1, 1] → formed by flipping the zeros at indices 1 and 2
    [0, 1, 1, 0, 1] → formed by flipping the zeros at indices 2 and 5
"""



# ––––––––––––––––––––––––––––––––––––––––––––––
# Task: Find the maximum length of consecutive 1's in a binary array after flipping at most k 0's.

# Why: Practices sliding window technique to maximize consecutive 1's with a constraint on flips.

def longestOnes(nums, k):  # Example: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2

    # 1️⃣ Initialize variables
    # Initialize left pointer for the sliding window
    # Why? We use left to shrink the window when we exceed k zeros
    left = 0  # left = 0

    # Initialize answer to track the maximum length of consecutive 1's
    # Why? We need to store the longest valid window
    ans = 0  # ans = 0

    # Initialize current count of zeros in the window
    # Why? We track zeros to ensure we don't use more than k flips
    curr = 0  # curr = 0

    # 2️⃣ Iterate with right pointer
    # Loop through the array with right pointer to expand the window
    # Why? We process each element to build windows and track valid subarrays
    for right in range(len(nums)):  # right goes from 0 to 10 (len(nums) = 11)
        # --- Iteration 1: right = 0 ---
        # Increment curr if the current element is 0
        # Why? We need to count zeros to enforce the k-flip limit
        if nums[right] == 0:  # nums[0] = 1, not 0, skip
            curr += 1  # skip
        # Shrink window if we have more than k zeros
        # Why? We need to maintain at most k zeros in the window
        while curr > k:  # curr = 0, k = 2, 0 > 2 is false, skip
            if nums[left] == 0:
                curr -= 1
            left += 1
        # Update maximum length of valid window
        # Why? The window length (right - left + 1) may be the longest so far
        ans = max(ans, right - left + 1)  # right = 0, left = 0, ans = max(0, 0 - 0 + 1) = 1
        # After Iteration 1: left = 0, curr = 0, ans = 1
        # Current window: [1] (0 zeros, length 1)

        # --- Iteration 2: right = 1 ---
        if right == 1:
            if nums[right] == 0:  # nums[1] = 1, not 0, skip
                curr += 1
            while curr > k:  # curr = 0, k = 2, 0 > 2 is false, skip
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)  # right = 1, left = 0, ans = max(1, 1 - 0 + 1) = 2
            # After Iteration 2: left = 0, curr = 0, ans = 2
            # Current window: [1, 1] (0 zeros, length 2)

        # --- Iteration 3: right = 2 ---
        if right == 2:
            if nums[right] == 0:  # nums[2] = 1, not 0, skip
                curr += 1
            while curr > k:  # curr = 0, k = 2, 0 > 2 is false, skip
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)  # right = 2, left = 0, ans = max(2, 2 - 0 + 1) = 3
            # After Iteration 3: left = 0, curr = 0, ans = 3
            # Current window: [1, 1, 1] (0 zeros, length 3)

        # --- Iteration 4: right = 3 ---
        if right == 3:
            if nums[right] == 0:  # nums[3] = 0, true
                curr += 1  # curr = 0 + 1 = 1
            while curr > k:  # curr = 1, k = 2, 1 > 2 is false, skip
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)  # right = 3, left = 0, ans = max(3, 3 - 0 + 1) = 4
            # After Iteration 4: left = 0, curr = 1, ans = 4
            # Current window: [1, 1, 1, 0] (1 zero, length 4)

        # --- Iteration 5: right = 4 ---
        if right == 4:
            if nums[right] == 0:  # nums[4] = 0, true
                curr += 1  # curr = 1 + 1 = 2
            while curr > k:  # curr = 2, k = 2, 2 > 2 is false, skip
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)  # right = 4, left = 0, ans = max(4, 4 - 0 + 1) = 5
            # After Iteration 5: left = 0, curr = 2, ans = 5
            # Current window: [1, 1, 1, 0, 0] (2 zeros, length 5)

        # --- Iteration 6: right = 5 ---
        if right == 5:
            if nums[right] == 0:  # nums[5] = 0, true
                curr += 1  # curr = 2 + 1 = 3
            while curr > k:  # curr = 3, k = 2, 3 > 2 is true
                if nums[left] == 0:  # nums[0] = 1, not 0, skip
                    curr -= 1
                left += 1  # left = 0 + 1 = 1
                # Check again: curr = 3, k = 2, 3 > 2 is true
                if nums[left] == 0:  # nums[1] = 1, not 0, skip
                    curr -= 1
                left += 1  # left = 1 + 1 = 2
                # Check again: curr = 3, k = 2, 3 > 2 is true
                if nums[left] == 0:  # nums[2] = 1, not 0, skip
                    curr -= 1
                left += 1  # left = 2 + 1 = 3
                # Check again: curr = 3, k = 2, 3 > 2 is true
                if nums[left] == 0:  # nums[3] = 0, true
                    curr -= 1  # curr = 3 - 1 = 2
                left += 1  # left = 3 + 1 = 4
                # Check again: curr = 2, k = 2, 2 > 2 is false, exit while
            ans = max(ans, right - left + 1)  # right = 5, left = 4, ans = max(5, 5 - 4 + 1) = 5
            # After Iteration 6: left = 4, curr = 2, ans = 5
            # Current window: [0, 0] (2 zeros, length 2)

        # --- Iteration 7: right = 6 ---
        if right == 6:
            if nums[right] == 0:  # nums[6] = 1, not 0, skip
                curr += 1
            while curr > k:  # curr = 2, k = 2, 2 > 2 is false, skip
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)  # right = 6, left = 4, ans = max(5, 6 - 4 + 1) = 5
            # After Iteration 7: left = 4, curr = 2, ans = 5
            # Current window: [0, 0, 1] (2 zeros, length 3)

        # --- Iteration 8: right = 7 ---
        if right == 7:
            if nums[right] == 0:  # nums[7] = 1, not 0, skip
                curr += 1
            while curr > k:  # curr = 2, k = 2, 2 > 2 is false, skip
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)  # right = 7, left = 4, ans = max(5, 7 - 4 + 1) = 5
            # After Iteration 8: left = 4, curr = 2, ans = 5
            # Current window: [0, 0, 1, 1] (2 zeros, length 4)

        # --- Iteration 9: right = 8 ---
        if right == 8:
            if nums[right] == 0:  # nums[8] = 1, not 0, skip
                curr += 1
            while curr > k:  # curr = 2, k = 2, 2 > 2 is false, skip
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)  # right = 8, left = 4, ans = max(5, 8 - 4 + 1) = 5
            # After Iteration 9: left = 4, curr = 2, ans = 5
            # Current window: [0, 0, 1, 1, 1] (2 zeros, length 5)

        # --- Iteration 10: right = 9 ---
        if right == 9:
            if nums[right] == 0:  # nums[9] = 1, not 0, skip
                curr += 1
            while curr > k:  # curr = 2, k = 2, 2 > 2 is false, skip
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)  # right = 9, left = 4, ans = max(5, 9 - 4 + 1) = 6
            # After Iteration 10: left = 4, curr = 2, ans = 6
            # Current window: [0, 0, 1, 1, 1, 1] (2 zeros, length 6)

        # --- Iteration 11: right = 10 ---
        if right == 10:
            if nums[right] == 0:  # nums[10] = 0, true
                curr += 1  # curr = 2 + 1 = 3
            while curr > k:  # curr = 3, k = 2, 3 > 2 is true
                if nums[left] == 0:  # nums[4] = 0, true
                    curr -= 1  # curr = 3 - 1 = 2
                left += 1  # left = 4 + 1 = 5
                # Check again: curr = 2, k = 2, 2 > 2 is false, exit while
            ans = max(ans, right - left + 1)  # right = 10, left = 5, ans = max(6, 10 - 5 + 1) = 6
            # After Iteration 11: left = 5, curr = 2, ans = 6
            # Current window: [0, 1, 1, 1, 1, 0] (2 zeros, length 6)

    # 3️⃣ Return the maximum length
    # Why? ans contains the length of the longest window with at most k zeros
    return ans  # ans = 6


nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
print(longestOnes(nums, 2)) 
# Output: 6