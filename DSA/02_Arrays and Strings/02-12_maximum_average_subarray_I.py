# 643. Maximum Average Subarray I
# Finds the contiguous subarray of length k with the maximum average value.

# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 

# Solution: https://leetcode.com/problems/maximum-average-subarray-i/solutions/127562/maximum-average-subarray-i/

# Example
    # Input: nums = [4, -2, 1, 7, -1], k = 2
    # Output: 4
    # Explanation: Maximum average is (1 + 7) / 2 = 8 / 2 = 4

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
# Output: 4  --> Subarray [1, 7] (length 2, sum 1 + 7 = 8, average 8/2 = 4) has the largest average for k=2.

# Time: O(n)
# - Initial sum of the first k elements: O(k).
# - Sliding the window across the array: O(n) total, since each step adds one element and removes one element in O(1) time.
# - Overall time is O(n) because O(n) dominates O(k).

# Space: O(1)
# - Only a constant number of variables (curr, ans, i) are used.
# - No additional data structures.
# - Overall: O(1) space.


"""
Overview for Each Iteration
Input: nums = [4, -2, 1, 7, -1], k = 2
Step 1: Calculate initial sum for first window of size k
i   | curr    | ans
----|---------|----
-   | 0       | 0
0   | 4       | 4
1   | 2 (4-2) | 2

Step 2: Slide window and compute maximum sum
i   | curr          | nums[i] | nums[i-k] | ans
----|---------------|---------|-----------|---------------
2   | -1 (2+1-4)    | 1       | 4         | 2 (max(2, -1))
3   | 8 (-1+7-(-2)) | 7       | -2        | 8 (max(2, 8))
4   | 6 (8-1-7)     | -1      | 1         | 8 (max(8, 6))
Final: 8/2 = 4 ([1, 7])



Most IMPORTANT thing to Understand:
    • We want the subarray of length k with the highest average.

    • Instead of recalculating every sum, we keep a running sum of the current window of size k.

    • Average = (best sum) ÷ k. So maximizing the sum also maximizes the average.

    
Why this code Works:
    • Running sum curr: tracks the sum of the current window.

    • Sliding window: when moving forward, add the new element and remove the one that just left.

    • Efficiency: avoids recalculating each window in O(k). Total = O(n), space = O(1).

    • Intuition: Like moving a magnifying glass over the array — you don't recheck everything, just swap one number out and one in.

TLDR
    • Keep a rolling sum of each k-sized window, track the largest sum, then divide by k.

Quick Example Walkthrough:
    nums = [4, -2, 1, 7, -1], k = 2

    Step 1: First window [4, -2], sum = 2 → ans = 2

    Step 2: Slide to [ -2, 1 ], sum = 2 - 4 + 1 = -1 → ans = 2

    Step 3: Slide to [1, 7], sum = -1 - (-2) + 7 = 8 → ans = 8

    Step 4: Slide to [7, -1], sum = 8 - 1 - 7 = 6 → ans = 8

Final Answer: 8 ÷ 2 = 4 (best subarray = [1,7])



    
⚠️ Caution:
    • I verified this solution is correct, but LeetCode may deny it unless the last line is: return float(ans) / k

Why?
    • In Python 2, "ans / k" does integer division if both are ints.
    • In Python 3, "/" always returns a float (e.g., 12 / 4 = 3.0).
    • LeetCode sometimes runs code with Python 2 by default, so explicitly casting to float ensures the result matches the expected floating-point output.

"""


# ––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
def findMaxAverage(nums, k):
    curr = 0          # Tracks sum of current window
   
    # Build first window of size k
    for i in range(k):  # Iterate over first k elements
        curr += nums[i]  # Add to window sum
    
    ans = curr        # Initialize answer with first window's sum
    
    # Slide window, maintaining size k
    for i in range(k, len(nums)):  # Start from index k
        curr += nums[i] - nums[i - k] # Add the new element, subtract the leftmost element
        ans = max(ans, curr)       # Update max sum
    
    return float(ans) / k          # Return maximum average


# ––––––––––––––––––––––––––––––––––––––––––––––
# Best Solution

def findMaxAverage(nums, k):
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

nums = [1, 2, 3, 4]
k = 2
print(solution.findMaxAverage(nums, k))  
# Output: 3.5  --> Subarray [3, 4] (length 2, sum 3 + 4 = 7, average 7/2 = 3.5) has the largest average for k=2.

"""
Overview for Each Iteration
Input: nums = [1, 2, 3, 4], k = 2
Step 1: Calculate initial sum for first window of size k
i   | curr      | ans
----|-----------|----
-   | 0         | 0
0   | 1         | 1
1   | 3 (1+2)   | 3

Step 2: Slide window and compute maximum sum
i   | curr      | nums[i] | nums[i-k] | ans
----|-----------|---------|-----------|--------------
2   | 5 (3+3-1) | 3       | 1         | 5 (max(3, 5))
3   | 7 (5+4-2) | 4       | 2         | 7 (max(5, 7))
Final: 7/2 = 3.5 ([3, 4])

"""





# ––––––––––––––––––––––––––––––––––––––––––––––
# Full Breakdown 

# Task: Find the maximum average of any contiguous subarray of length k in an array.
# Example: nums = [1, 2, 3, 4], k = 2 → Output = 3.5 (subarray [3, 4], sum = 7, average = 7/2 = 3.5)
# Why: Practices sliding window technique to compute maximum average efficiently.

class Solution(object):
    def findMaxAverage(self, nums, k):  # Example: nums = [1, 2, 3, 4], k = 2
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # 1️⃣ Initialize first window sum
        # Initialize current sum to track the sum of the window
        # Why? We need to compute the sum of the first k elements
        curr = 0  # curr = 0
        for i in range(k):  # i goes from 0 to 1 (k = 2)
            curr += nums[i]  # First: i = 0, nums[0] = 1, curr = 0 + 1 = 1
                             # Second: i = 1, nums[1] = 2, curr = 1 + 2 = 3
        # After loop: curr = 3 (sum of [1, 2])

        # 2️⃣ Initialize answer with first window's sum
        # Set the initial maximum sum to the first window's sum
        # Why? We need to compare this with sums of subsequent windows before computing the final average
        ans = curr  # ans = 3

        # 3️⃣ Slide window, maintaining size k
        # Iterate from index k to the end to process each subsequent window
        # Why? We slide the window one element at a time to check all k-sized subarrays
        for i in range(k, len(nums)):  # k = 2, len(nums) = 4, i goes from 2 to 3
            # --- Iteration 1: i = 2 ---
            # Update sum: add new element, subtract the first element of the previous window
            # Why? This efficiently updates the sum without recomputing the entire window
            curr += nums[i] - nums[i - k]  # i = 2, nums[2] = 3, i-k = 2-2 = 0, nums[0] = 1
                                           # curr = 3 + 3 - 1 = 5

            # Update maximum sum if the current sum is larger
            # Why? We want the largest sum to compute the maximum average later
            ans = max(ans, curr)  # ans = max(3, 5) = 5
            # After Iteration 1: curr = 5, ans = 5
            # Current window: [2, 3] (sum = 5)

            # --- Iteration 2: i = 3 ---
            if i == 3:
                # Update sum
                curr += nums[i] - nums[i - k]  # i = 3, nums[3] = 4, i-k = 3-2 = 1, nums[1] = 2
                                               # curr = 5 + 4 - 2 = 7

                # Update maximum sum
                ans = max(ans, curr)  # ans = max(5, 7) = 7
                # After Iteration 2: curr = 7, ans = 7
                # Current window: [3, 4] (sum = 7)

        # 4️⃣ Return maximum average
        # Divide the maximum sum by k to get the average
        # Why? The problem asks for the maximum average, not the sum
        return ans / k  # ans = 7, k = 2, float(7) / 2 = 3.5


solution = Solution()
nums = [1, 2, 3, 4]
k = 2
print(solution.findMaxAverage(nums, k)) 
# Output: 3.5  --> Subarray [3, 4] (length 2, sum 3 + 4 = 7, average 7/2 = 3.5) has the largest average for k=2.
