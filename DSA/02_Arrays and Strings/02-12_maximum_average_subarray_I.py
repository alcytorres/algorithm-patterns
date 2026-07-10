# 643. Maximum Average Subarray I
"""
You are given an integer array nums consisting of n elements, and an integer k.

Find the maximum average of any contiguous subarray of length k in nums. Return this value. 

Example
    Input: nums = [4, -2, 1, 7, -1], k = 2
    Output: 4
    Explanation: Maximum average is (1 + 7) / 2 = 8 / 2 = 4

Constraints:
    n == nums.length
    1 <= k <= n <= 105
    -104 <= nums[i] <= 104

Solution: https://leetcode.com/problems/maximum-average-subarray-i/description/
"""

# Solution: Sliding Window: Fixed-Size Maximum Average

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curr = 0
        
        for i in range(k):
            curr += nums[i]

        ans = curr

        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            ans = max(ans, curr)

        return ans / k

# Create instance and call method
solution = Solution()
nums = [4, -2, 1, 7, -1]
k = 2
print(solution.findMaxAverage(nums, k))  
# Output: 4  →  Subarray [1, 7] (length 2, sum 1 + 7 = 8, average 8/2 = 4) has the largest average for k=2

# ––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
def findMaxAverage(nums, k):
    curr = 0             # Tracks sum of current window
   
    # Build first window of size k
    for i in range(k):   # Iterate over first k elements
        curr += nums[i]  # Add to window sum
    
    ans = curr           # Initialize answer with first window's sum
    
    # Slide window, maintaining size k
    for i in range(k, len(nums)):  # Start from index k
        curr += nums[i] - nums[i - k] # Add the new element, subtract the leftmost element
        ans = max(ans, curr)       # Update max sum
    
    return float(ans) / k          # Return maximum average

"""
Time: O(N)
  - Let N = length of nums.
  - Step 1: Compute the sum of the first k elements → O(k).
  - Step 2: Slide the window across the array → O(N - k).
      • Add the next element and remove the element leaving the window → O(1) per step.
  - Each element is processed at most twice (once added, once subtracted).
  - Overall: O(N).

Space: O(1)
  - Only integer and float variables are used (curr, ans, loop counters).
  - No additional data structures are created.
  - Overall: O(1).

  
Interview Answer: Worst Case

Time: O(N)
  - Sliding window computes all subarray sums in one pass.

Space: O(1)
  - Constant space for running total and average calculation.



---
Most IMPORTANT thing to Understand:
    • We need the highest average of any contiguous subarray of exactly length k.

    • Average = sum / k, and k is fixed — so the subarray with the biggest sum also has the biggest average.

    • Instead of recomputing each window's sum from scratch, we slide one window across the array and update the sum in O(1).

    • `curr` tracks the sum of the current window. `ans` tracks the best (largest) window sum seen so far.

---
Why this code Works:
    • Sliding window (fixed size k):
        • First loop builds the initial window: sum of nums[0] through nums[k-1].
        • Second loop slides the window one index at a time.

    • Each slide:
        • Add the new right element: nums[i]
        • Remove the old left element: nums[i - k]
        • `curr += nums[i] - nums[i - k]` keeps the window size exactly k.

    • `ans = max(ans, curr)` remembers the best window sum as we slide.

    • Return `ans / k` because max sum ÷ k = max average.

    • Efficiency:
        • Brute force: nested loops try every start, re-summing k elements each time → O(N × k).
        • Sliding window processes each element once → O(N).
        • Space: O(1) — only `curr`, `ans`, and loop counters.

    • Intuition:
        • Like a moving frame of width k sliding across the array.
        • You only adjust the edges — drop the left number, add the right number — instead of recounting everything inside.

---
TLDR:
    • Build the first window sum, then slide it across the array while tracking the max sum. Divide by k to get the max average.


---
Quick Example Walkthrough:
    nums = [4, -2, 1, 7, -1], k = 2

    Step 1: Build first window (indices 0-1)
        curr = 4 + (-2) = 2
        ans = 2

    Step 2: Slide the window
        • i=2: curr = 2 + 1 - 4 = -1  → ans stays 2
        • i=3: curr = -1 + 7 - (-2) = 8 → ans = 8  (window [1, 7])
        • i=4: curr = 8 + (-1) - 1 = 6  → ans stays 8

    Step 3: Return average
        ans / k = 8 / 2 = 4

    Final Answer: 4


---
Full Example Walkthrough:
    nums = [4, -2, 1, 7, -1]
    k = 2

    Starting State:
        curr = 0
        ans = (not set yet)

    --------------------------------------------------

    Build First Window (i = 0 to 1):
        i = 0: curr += nums[0] = 4        → curr = 4
        i = 1: curr += nums[1] = -2       → curr = 2

        ans = curr = 2
        Current window: [4, -2], sum = 2, average = 1

    --------------------------------------------------

    Loop Iteration 1 (i = 2):
        Slide: add nums[2], remove nums[0]
            curr += nums[2] - nums[0]
            curr += 1 - 4 = -3
            curr = 2 + (-3) = -1

        Compare:
            ans = max(2, -1) = 2

        Current window: [-2, 1], sum = -1, average = -0.5

    --------------------------------------------------

    Loop Iteration 2 (i = 3):
        Slide: add nums[3], remove nums[1]
            curr += nums[3] - nums[1]
            curr += 7 - (-2) = 9
            curr = -1 + 9 = 8

        Compare:
            ans = max(2, 8) = 8

        Current window: [1, 7], sum = 8, average = 4

    --------------------------------------------------

    Loop Iteration 3 (i = 4):
        Slide: add nums[4], remove nums[2]
            curr += nums[4] - nums[2]
            curr += (-1) - 1 = -2
            curr = 8 + (-2) = 6

        Compare:
            ans = max(8, 6) = 8

        Current window: [7, -1], sum = 6, average = 3

    --------------------------------------------------

    Final Check:
        return ans / k
        8 / 2 = 4

        This means:
            The subarray [1, 7] has the largest average of any length-2 contiguous subarray.


---
Overview for Each Iteration
Input: nums = [4, -2, 1, 7, -1], k = 2

Phase 1: Build first window
i | curr | ans | window      | Action
--|------|-----|-------------|----------------------------------
0 | 4    | -   | [4]         | curr += nums[0]
1 | 2    | 2   | [4, -2]     | curr += nums[1], ans = curr

Phase 2: Slide window
i | curr | ans | window      | Action
--|------|-----|-------------|----------------------------------
2 | -1   | 2   | [-2, 1]     | +nums[2] -nums[0], ans stays 2
3 | 8    | 8   | [1, 7]      | +nums[3] -nums[1], ans = max(2,8)
4 | 6    | 8   | [7, -1]     | +nums[4] -nums[2], ans stays 8

Final: ans / k = 8 / 2 = 4



---
🧠 First Time? Thoughts → Code

Read the problem (10 sec)
    • Find the highest average of any contiguous subarray of exactly length k.

    • k is fixed for every window — so max average = max sum ÷ k. Track the biggest sum, divide once at the end.

    • "Contiguous" + fixed length k → windows slide across the array.


Start naive (totally fine)
    • Try every starting index, inner loop sums the next k elements, keep the best.
        → Nested loops.

    • O(N × k) — works, but re-sums almost the same elements every time.


The one insight that unlocks the optimal code
    • Adjacent windows share k − 1 elements. Don't re-add them — just update the edges.

    • Slide right: add the new element coming in, subtract the one leaving.

    • One running sum (`curr`), updated in O(1) per step → whole scan is O(N).


Why sliding window?
    • Window size never changes — classic fixed-size sliding window.

    • Each step only 2 numbers change (one enters, one exits). Everything in the middle stays.


Thought → line of code
    • `for i in range(k): curr += nums[i]`
        → Build the first full window before sliding.
        → Can't use the slide formula until you have a starting sum.

    • `ans = curr`
        → First window counts — initialize max with it.

    • `for i in range(k, len(nums))`
        → `i` is the new right edge entering the window.
        → Start at k, not 0 — first k elements already summed.

    • `curr += nums[i] - nums[i - k]`
        → The whole trick in one line: add right, drop left.
        → `nums[i - k]` is the element leaving — not obvious until you picture the window shifting.

    • `ans = max(ans, curr)`
        → Track best sum. Divide by k only at the end since k is constant.

    • `return ans / k`
        → Max sum ÷ k = max average. One division, not per window.


Memory hook (one sentence)
    • Build the first window, then slide: add the new right, drop the old left, track the best sum.


Would you arrive at this cold?
    • Immediately: nested loops — "try every start, sum k elements." O(N × k) without studying.

    • After asking "what does the input buy me?": fixed size + contiguous → sliding window; adjacent windows overlap almost completely.

    • Bookkeeping: `curr`, `ans`, two loops, the add-minus slide line.

    • Real insight: update the running sum at the edges — that's what kills the inner loop.

"""























# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force
def findMaxAverage_bruteforce(nums, k):
    ans = float('-inf')

    for i in range(len(nums) - k + 1):
        curr = 0
        for j in range(k):
            curr += nums[i + j]
        ans = max(ans, curr)

    return ans / k


nums = [4, -2, 1, 7, -1]
k = 2
print(findMaxAverage_bruteforce(nums, k))
# Output: 4 → Try every length-k subarray, sum each from scratch, return max average.

"""
Time: O(N × k)
  - Let N = length of nums.

  - Step 1: Outer loop tries every valid starting index → O(N).
      • There are N - k + 1 possible windows.

  - Step 2: Inner loop sums k elements for each start → O(k).
      • Each window is recomputed from scratch.

  - Combined: O(N × k).
  - Overall: O(N × k).


Space: O(1)
  - Only ans, curr, and loop counters are used.
  - No additional data structures.
  - Overall: O(1).


Interview Answer: Worst Case

Time: O(N × k)
  - Every starting position re-sums all k elements in its window.

Space: O(1)
  - Constant extra variables only.


---
Overview for Each Iteration
nums = [4, -2, 1, 7, -1], k = 2

    ans starts = -inf

    i = 0 → sum nums[0..1] = 4 + (-2) = 2  → ans = 2
    i = 1 → sum nums[1..2] = -2 + 1 = -1   → ans = 2
    i = 2 → sum nums[2..3] = 1 + 7 = 8     → ans = 8
    i = 3 → sum nums[3..4] = 7 + (-1) = 6  → ans = 8

    return ans / k
    8 / 2 = 4

Final: 4

"""
