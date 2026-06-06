# Example 4: Largest Sum of Subarray with Fixed Length k
"""
Finds the subarray of length k with the largest sum.

Example:
    Input: [1, 4, 6, 2]
    Output: 10  --> Subarray [4, 6] (length 2, sum 4 + 6 = 10) is the largest sum for k=2.
"""

# Solution: Sliding Window: Fixed-Size Max Sum

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
# Output: 10  →  Subarray [4, 6] (length 2, sum 4 + 6 = 10) is the largest sum for k=2.

# –––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def find_best_subarray(nums, k):
    curr = 0             # Tracks sum of current window
    
    # Build first window of size k
    for i in range(k):   # Iterate over first k elements
        curr += nums[i]  # Add to window sum
    
    ans = curr       # Initialize answer with first window's sum
    
    # Slide window, maintaining size k
    for i in range(k, len(nums)):     # Start from index k
        curr += nums[i] - nums[i-k]   # Add the new element, subtract the leftmost element
        ans = max(ans, curr)  # Update max sum
    
    return ans  # Returns the maximum sum

"""
Time: O(N)
  - Let N = length of nums.
  - Step 1: Compute the initial sum of the first k elements → O(k).
  - Step 2: Slide the window across the array → O(N - k).
      • For each new element, add one and remove one → O(1) per step.
  - Each element is processed a constant number of times.
  - Overall: O(N).

Space: O(1)
  - Only a few integer variables are used: curr, ans, and loop counters.
  - No extra data structures are created.
  - Overall: O(1).

  
Interview Answer: Worst Case

Time: O(N)
  - Fixed-size sliding window, single pass through array.

Space: O(1)
  - Constant space for running sum and best value.
  

---
Overview for Each Iteration
Input: nums = [1, 4, 6, 2], k = 2

Step 1: Calculate initial sum for first window of size k
i | curr    | ans
--|---------|-----
- | 0       | -
0 | 1       | -
1 | 5 (1+4) | 5

Step 2: Slide window, maintaining size k
i | curr       | nums[i] | nums[i-k] | ans
--|------------|---------|-----------|----------------
2 | 10 (5+6-1) | 6       | 1         | 10 (max(5, 10))
3 | 8 (10+2-4) | 2       | 4         | 10 (max(10, 8))

Final: 10 ([4, 6])


---
Most IMPORTANT thing to Understand:
    • We want the maximum sum of any subarray of size k.

    • Instead of recalculating sums every time, we keep a running sum of the current window of size k.

    • When we slide the window forward, subtract the element leaving and add the new one coming in.

--- 
Why this code Works:
    • Running sum curr tracks the sum of the current window.

    • Sliding window: update sum in O(1) per step by adding the new element and removing the old one.

    • Efficiency: avoids recomputing each window in O(k). Total time = O(n), space = O(1).

    • Intuition: Like moving a window over text — you don’t reread all letters, just swap one out and add one in.

--- 
TLDR
    • Keep a rolling sum of size k, slide it across the array, and track the maximum.

---
Quick Example Walkthrough:
    nums = [1, 4, 6, 2], k = 2

    Step 1: First window = [1,4], sum = 5 → ans=5

    Step 2: Slide to [4,6], update sum = 5 - 1 + 6 = 10 → ans=10

    Step 3: Slide to [6,2], update sum = 10 - 4 + 2 = 8 → ans=10

Final Answer: 10 (best subarray is [4,6])

"""




