# 1004. Max Consecutive Ones III 
"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example:
    Input: nums = [1, 0, 1, 1, 0], k = 1
    Output: 4
    Explanation: nums[1] was flipped from 0 to 1. We are left with [1, 1, 1, 1] 

Solution: https://leetcode.com/problems/max-consecutive-ones-iii/solutions/409192/max-consecutive-ones-iii/
"""

# Solution: Sliding Window: Shrink Window When Zero Count Exceeds k

def longestOnes(nums, k):
    l = ans = curr = 0

    for r in range(len(nums)):
        if nums[r] == 0:
            curr += 1
        
        while curr > k:
            if nums[l] == 0:
                curr -= 1
            l += 1
        
        ans = max(ans, r - l + 1)
    
    return ans

nums = [1, 0, 1, 1, 0]
k = 1
print(longestOnes(nums, k))
# Output: 4 → By flipping at most 1 zero, the longest consecutive stretch of 1s is 4

# 1 Valid Subarrays:
    #  [1, 1, 1, 1], formed by flipping the zero at index 1


# ––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def longestOnes(nums, k):
    left = ans = curr = 0  # Left bound, max length, count of 0's in window
    
    for right in range(len(nums)):  # Iterate right pointer over array
        if nums[right] == 0:        # If current element is 0
            curr += 1               # Increment 0's count
        
        while curr > k:            # Shrink window if 0's exceed k
            if nums[left] == 0:    # If leftmost element is 0
                curr -= 1          # Decrement 0's count
            left += 1              # Move left pointer forward
        
        ans = max(ans, right - left + 1)  # Update max window size
    
    return ans   # Return the maximum length of consecutive 1's possible


"""
Time: O(N)
  - Let N = number of elements in nums.
  - The right pointer scans through the array once → O(N).
  - The left pointer also only moves forward, never backward → O(N) total across the whole algorithm.
  - Each element is added to the window once and removed from the window at most once.
  - Combined: O(N + N).
  - Overall: O(N).


Space: O(1)
  - Only a few variables are used: left, right, ans, and curr.
  - No extra data structures are created.
  - Overall: O(1).


Interview Answer: Worst Case

Time: O(N)
  - Sliding window scans the array once with the right pointer.
  - The left pointer also moves forward at most N times total.

Space: O(1)
  - Only pointer and counter variables are used.



---
Overview for Each Iteration
Input: nums = [1, 0, 1, 1, 0], k = 1

Expand the sliding window with r.
If zero count exceeds k, shrink window from the left.

r | nums[r] | l | curr(0s) | Action / Decision        | ans | Window
--|---------|---|----------|--------------------------|-----|---------
- | -       | 0 | 0        | Start                    | 0   | []
0 | 1       | 0 | 0        | Valid window             | 1   | [1]
1 | 0       | 0 | 1        | Include 0 (<= k)         | 2   | [1,0]
2 | 1       | 0 | 1        | Valid window             | 3   | [1,0,1]
3 | 1       | 0 | 1        | Valid window             | 4   | [1,0,1,1]
4 | 0       | 2 | 1        | curr > k → shrink window | 4   | [1,1,0]

Shrink Process at r = 4

l move | Removed | curr(0s) | New l | Window
-------|---------|-----------|-------|----------
0 → 1  | 1       | 2         | 1     | [0,1,1,0]
1 → 2  | 0       | 1         | 2     | [1,1,0]

Final: 4



---
Most IMPORTANT thing to Understand:
    • We are looking for the longest window of 1s, that contains at most k zeros.

    • A zero inside the window represents a number we can flip into a 1.

    • curr tracks how many zeros are currently inside the window.

    • If curr > k, the window is no longer valid, so we shrink it from the left.

---
Why this code Works:
    • Sliding window:
        • right expands the window.
        • left shrinks the window only when there are too many zeros.

    • curr:
        • Counts how many zeros are in the current window.

    • Valid window:
        • A window is valid when curr <= k.
        • This means we can flip all zeros in that window into 1s.

    • ans:
        • Stores the longest valid window length seen so far.

    • Efficiency:
        • Each pointer only moves forward.
        • No repeated checking of every subarray.

---
TLDR:
    • This works because it keeps the biggest window that has at most k zeros.
    • Whenever the window has too many zeros, it shrinks until it becomes valid again.

---
Quick Example Walkthrough:

nums = [1, 0, 1, 1, 0]
k = 1

Step 1:
    Start with left = 0, curr = 0, ans = 0.

Step 2:
    Expand right through the array.

    • Window [1] has 0 zeros → valid → ans = 1

    • Window [1, 0] has 1 zero → valid → ans = 2

    • Window [1, 0, 1] has 1 zero → valid → ans = 3

    • Window [1, 0, 1, 1] has 1 zero → valid → ans = 4

    • Window [1, 0, 1, 1, 0] has 2 zeros → invalid

Step 3:
    Shrink from the left until there is only 1 zero again.

Final Answer:
    4

    The longest valid window is [1, 0, 1, 1].
    Flip the zero at index 1 to get [1, 1, 1, 1].


---
Full Example Walkthrough:

nums = [1, 0, 1, 1, 0]
k = 1

Starting State:
    left = 0
    ans = 0
    curr = 0

--------------------------------------------------

Loop Iteration 1:
    right = 0
    nums[right] = 1

    Since nums[right] is not 0:
        curr stays 0

    curr <= k:
        0 <= 1 → valid window

    Window:
        nums[0:1] = [1]

    Update ans:
        ans = max(0, 0 - 0 + 1)
        ans = 1

--------------------------------------------------

Loop Iteration 2:
    right = 1
    nums[right] = 0

    Since nums[right] is 0:
        curr += 1
        curr = 1

    curr <= k:
        1 <= 1 → valid window

    Window:
        nums[0:2] = [1, 0]

    Update ans:
        ans = max(1, 1 - 0 + 1)
        ans = 2

--------------------------------------------------

Loop Iteration 3:
    right = 2
    nums[right] = 1

    Since nums[right] is not 0:
        curr stays 1

    curr <= k:
        1 <= 1 → valid window

    Window:
        nums[0:3] = [1, 0, 1]

    Update ans:
        ans = max(2, 2 - 0 + 1)
        ans = 3

--------------------------------------------------

Loop Iteration 4:
    right = 3
    nums[right] = 1

    Since nums[right] is not 0:
        curr stays 1

    curr <= k:
        1 <= 1 → valid window

    Window:
        nums[0:4] = [1, 0, 1, 1]

    Update ans:
        ans = max(3, 3 - 0 + 1)
        ans = 4

--------------------------------------------------

Loop Iteration 5:
    right = 4
    nums[right] = 0

    Since nums[right] is 0:
        curr += 1
        curr = 2

    curr > k:
        2 > 1 → invalid window

    Shrink from the left:

        nums[left] = nums[0] = 1
        This is not 0, so curr stays 2.
        left += 1
        left = 1

    Still curr > k:
        2 > 1 → still invalid

        nums[left] = nums[1] = 0
        This is 0, so curr -= 1.
        curr = 1

        left += 1
        left = 2

    Now curr <= k:
        1 <= 1 → valid window again

    Window:
        nums[2:5] = [1, 1, 0]

    Update ans:
        ans = max(4, 4 - 2 + 1)
        ans = 4

--------------------------------------------------

Final Answer:
    return ans
    return 4

    The longest stretch of 1s after flipping at most 1 zero is 4.





--- REVIEW
Q: Which subarray of length 6 is the final answer?
    • Both [4..9] (flip nums[4] & nums[5]) and [5..10] (flip nums[5] & nums[10]) give a streak of 6 ones.

    • LeetCode's official explanation shows [5..10] as the answer (flipping nums[5] and nums[10]).

	• The algorithm only returns the max length (6), not which subarray produced it.

"""

