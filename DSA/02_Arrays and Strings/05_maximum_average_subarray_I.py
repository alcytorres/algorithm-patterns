# 643: Maximum Average Subarray I
# Finds the contiguous subarray of length k with the maximum average value.

# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 

# Solution: https://leetcode.com/problems/maximum-average-subarray-i/solutions/127562/maximum-average-subarray-i/


def findMaxAverage(nums, k):
    curr = 0
    for i in range(k):
        curr += nums[i]
        
    ans = curr
    
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]
        ans = max(ans, curr)
        
    return ans / k

print(findMaxAverage([1, 2, 3, 4], 2))  
# Output: 3.5  --> Subarray [3, 4] (length 2, sum 3 + 4 = 7, average 7/2 = 3.5) has the largest average for k=2.

# Time: O(n) - Builds first window in O(k), then slides n-k times with O(1) operations per iteration.
# Space: O(1) - Uses only two integer variables (curr, ans).


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
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
    
    return ans / k                 # Return maximum average



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Full Breakdown 

# Task: Find the maximum average of any contiguous subarray of length k in an array.
# Example: nums = [1, 2, 3, 4], k = 2 → Output = 3.5 (subarray [3, 4] has average (3 + 4) / 2 = 3.5)
# Why: Practices sliding window technique to compute maximum average efficiently.

def findMaxAverage(nums, k):  # Example: nums = [1, 2, 3, 4], k = 2

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
    return ans / k  # ans = 7, k = 2, 7 / 2 = 3.5


print(findMaxAverage([1, 2, 3, 4], 2))
# Output: 3.5  --> Subarray [3, 4] (length 2, sum 3 + 4 = 7, average 7/2 = 3.5) has the largest average for k=2.

