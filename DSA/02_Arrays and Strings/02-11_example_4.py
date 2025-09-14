# Example 4: Largest Sum of Subarray with Fixed Length k

# Finds the subarray of length k with the largest sum.

# Example:
    # Input: [1, 4, 6, 2]
    # Output: 10  --> Subarray [4, 6] (length 2, sum 4 + 6 = 10) is the largest sum for k=2.

def find_best_subarray(nums, k):
    curr = 0    
    
    for i in range(k): 
        curr += nums[i]  
    
    ans = curr       
    
    # Slide window, maintaining size k
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i-k]   
        ans = max(ans, curr) 
    
    return ans 

nums = [1, 4, 6, 2]
k = 2
print(find_best_subarray(nums, k))  
# Output: 10  --> Subarray [4, 6] (length 2, sum 4 + 6 = 10) is the largest sum for k=2.

# Time: O(n)
# - Initial sum of the first k elements: O(k).
# - Sliding the window across the array: O(n) total, since each step adds one element and removes one element in O(1) time.
# - Overall time is O(n) because O(n) dominates O(k).

# Space: O(1)
# - Only a constant number of variables (curr, ans, i) are used.
# - No additional data structures.
# - Overall: O(1) space.

"""
# Overview for Each Iteration
# Input: nums = [1, 4, 6, 2], k = 2
# Step 1: Calculate initial sum for first window of size k
# i | curr    | ans
# - | 0       | -
# 0 | 1       | -
# 1 | 5 (1+4) | 5

# Step 2: Slide window, maintaining size k
# i | curr       | nums[i] | nums[i-k] | ans
# 2 | 10 (5+6-1) | 6       | 1         | 10 (max(5, 10))
# 3 | 8 (10+2-4) | 2       | 4         | 10 (max(10, 8))
# Final: 10 ([4, 6])

"""

# –––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def find_best_subarray(nums, k):
    curr = 0          # Tracks sum of current window
    
    # Build first window of size k
    for i in range(k):  # Iterate over first k elements
        curr += nums[i]  # Add to window sum
    
    ans = curr       # Initialize answer with first window's sum
    
    # Slide window, maintaining size k
    for i in range(k, len(nums)):  # Start from index k
        curr += nums[i] - nums[i-k]     # Add the new element, subtract the leftmost element
        ans = max(ans, curr)  # Update max sum
    
    return ans  # Returns the maximum sum


# –––––––––––––––––––––––––––––––––––––––––––––––––––
# Task: Find the maximum sum of any contiguous subarray of size k in an array.
# Example: nums = [1, 4, 6, 2], k = 2 → Output = 10 (subarray [4, 6] has sum 4 + 6 = 10)
# Why: Practices sliding window technique to compute maximum sum efficiently.

def find_best_subarray(nums, k):  # Example: nums = [1, 4, 6, 2], k = 2

    # 1️⃣ Initialize current sum
    # Initialize current sum to track the sum of the window
    # Why? We need to compute the sum of the first k elements and update it as we slide
    curr = 0  # curr = 0

    # 2️⃣ Build first window of size k
    # Iterate over the first k elements to compute initial window sum
    # Why? We need the sum of the first subarray as the starting point
    for i in range(k):  # i goes from 0 to 1 (k = 2)
        curr += nums[i]  # First: i = 0, nums[0] = 1, curr = 0 + 1 = 1
                         # Second: i = 1, nums[1] = 4, curr = 1 + 4 = 5
    # After loop: curr = 5 (sum of [1, 4])

    # 3️⃣ Initialize answer with first window's sum
    # Set the initial maximum sum to the first window's sum
    # Why? We need to compare this with sums of subsequent windows
    ans = curr  # ans = 5

    # 4️⃣ Slide window, maintaining size k
    # Iterate from index k to the end to process each subsequent window
    # Why? We slide the window one element at a time to check all k-sized subarrays
    for i in range(k, len(nums)):  # k = 2, len(nums) = 4, i goes from 2 to 3
        # --- Iteration 1: i = 2 ---
        # Update sum: add new element, subtract the first element of the previous window
        # Why? This efficiently updates the sum without recomputing the entire window
        curr += nums[i] - nums[i - k]  # i = 2, nums[2] = 6, i-k = 2-2 = 0, nums[0] = 1
                                       # curr = 5 + 6 - 1 = 10

        # Update maximum sum if the current sum is larger
        # Why? We want the largest sum across all windows
        ans = max(ans, curr)  # ans = max(5, 10) = 10
        # After Iteration 1: curr = 10, ans = 10
        # Current window: [4, 6] (sum = 10)

        # --- Iteration 2: i = 3 ---
        if i == 3:
            # Update sum
            curr += nums[i] - nums[i - k]  # i = 3, nums[3] = 2, i-k = 3-2 = 1, nums[1] = 4
                                           # curr = 10 + 2 - 4 = 8

            # Update maximum sum
            ans = max(ans, curr)  # ans = max(10, 8) = 10
            # After Iteration 2: curr = 8, ans = 10
            # Current window: [6, 2] (sum = 8)

    # 5️⃣ Return the maximum sum
    # Why? ans contains the largest sum found in any k-sized subarray
    return ans  # ans = 10


nums = [1, 4, 6, 2]
k = 2
print(find_best_subarray(nums, k))  
# Output: 10  --> Subarray [4, 6] (length 2, sum 4 + 6 = 10) is the largest sum for k=2.
