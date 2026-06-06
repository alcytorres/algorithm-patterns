# Example 1: Longest Subarray with Sum Less Than or Equal to k
"""
Finds the length of the longest subarray with sum <= k using sliding window.

Example 1: nums = [1, 1, 2, 2, 4, 2], k = 8
Output: 4 (subarray [1, 1, 2, 2], sum = 6)

Example 1: nums = [1, 3, 3, 6], k = 8
Output: 3 (subarray [1, 3, 3], sum = 7)
"""

# Solution: Sliding Window: Shrink Window When Sum Exceeds k

def longest_subarray_sum(nums, k):
    left = curr = ans = 0        
    
    for right in range(len(nums)): 
        curr += nums[right]         
        
        while curr > k:            
            curr -= nums[left]     
            left += 1             
            
        ans = max(ans, right - left + 1)  
    
    return ans


nums = [1, 1, 2, 2, 4, 2]
k = 8
print(longest_subarray_sum(nums, k))
# Output: 4  →  Subarray [1, 1, 2, 2] (length 4, sum 6) is the longest subarray with sum <= 8.


"""
Time: O(N)
  - Let N = length of nums.
  - The right pointer expands the window once per element → O(N).
  - The left pointer only moves forward when sum exceeds k, and never moves backward → total O(N) steps.
  - Each element is added and removed from the running sum at most once.
  - Overall: O(N).

Space: O(1)
  - Only a few integer variables used: left, right, curr, ans.
  - No additional data structures are created.
  - Overall: O(1).

  
Interview Answer: Worst Case

Time: O(N)
  - Sliding window processes each element at most twice (once added, once removed).

Space: O(1)
  - Constant extra space for variables.

  
---
Overview for Each Iteration
Input: nums = [1, 1, 2, 2, 4, 2], k = 8

Step: Find longest subarray with sum <= k using sliding window
r | num | curr | l | window          | length | ans
--+-----+------+---+-----------------+--------+----
0 | 1   | 1    | 0 | [1]             | 1      | 1
1 | 1   | 2    | 0 | [1,1]           | 2      | 2
2 | 2   | 4    | 0 | [1,1,2]         | 3      | 3
3 | 2   | 6    | 0 | [1,1,2,2]       | 4      | 4   ← max
4 | 4   | 10   | 0 | [1,1,2,2,4]     | 5      | 4
  |     | 10>8 | 1 | remove 1 → 9    |        | 
  |     | 9>8  | 2 | remove 1 → 8    |        | 
  |     | 8≤8  | 2 | [2,2,4]         | 3      | 4
5 | 2   | 10   | 2 | [2,2,4,2]       | 4      | 4
  |     | 10>8 | 3 | remove 2 → 8    |        | 
  |     | 8≤8  | 3 | [2,4,2]         | 3      | 4

Final answer: 4



---
Most IMPORTANT thing to Understand:
    • We want the longest stretch of numbers where the sum ≤ k.

    • Use a sliding window: expand with right, shrink with left when sum goes over k.

    • Condition: whenever curr <= k, the window [left..right] is valid.

Why this code Works:
    • No hash map needed — just track current window sum (curr).

    • Sliding window idea: add the new element on the right, and if sum is too big, subtract elements from the left until valid.

    • Efficiency: each number is added once and removed once → O(n) total.

    • Intuition: like pouring water into a glass — if it overflows (sum > k), you pour some out from the left until it fits again.

TLDR:
    • This works because we grow a window until the sum breaks the rule, then shrink it until valid again, always keeping track of the longest valid window.

    
Quick Example Walkthrough:
nums = [1, 1, 2, 2, 4, 2], k = 8

    Start: left=0, curr=0, ans=0

    Right=0 → curr=1 ≤ 8 → ans=1
    Right=1 → curr=2 ≤ 8 → ans=2
    Right=2 → curr=4 ≤ 8 → ans=3
    Right=3 → curr=6 ≤ 8 → ans=4

    Right=4 → curr=10 > 8 → shrink:
        subtract 1 → curr=9
        subtract 1 → curr=8 (valid again)
        left now at index 2 → ans stays 4

    Right=5 → curr=10 > 8 → shrink:
        subtract 2 → curr=8 (valid again)
        left now at index 3 → ans stays 4

Final Answer: 4 → longest subarray is [1, 1, 2, 2] (sum = 6)


---
Q: Why use for right in range(len(nums)) and NOT 
   for right in len(nums) ?

    • for right in range(len(nums)):
        Iterates over indices (0 to len(nums)-1).
        Enables accessing array elements via nums[right].

    • for right in len(nums):
        Invalid syntax.
        len(nums) is a single integer, not an iterable.

        
---   
Q: Why is left += 1 always executed when shrinking the window (aka why is it inside the while loop)?


    • The only way to reduce the window sum is by removing elements from the left.  

    • So whenever curr > k, left must move forward—no exceptions.  

    • This guarantees the window actually shrinks each time it becomes too large.

"""


# ––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def longest_subarray_sum(nums, k):
    left = 0          # Left bound of the window
    curr = 0          # Tracks sum of current window
    ans = 0           # Tracks length of longest valid subarray
    
    for right in range(len(nums)):  # Iterate right pointer over array
        curr += nums[right]         # Add element to window sum
        
        while curr > k:            # Shrink window while sum exceeds k
            curr -= nums[left]     # Remove leftmost element from sum
            left += 1              # Move left pointer forward
            
        ans = max(ans, right - left + 1)  # Update max window size
    
    return ans   # Return length of longest subarray




# ===============================================
# Correct vs. Incorrect Sliding Window: Why l += 1 Must Stay Inside the While Loop
# ===============================================

# ––––––––––––––––––––––––––––––––––––––––––––––––
 # Correct Solution

def longest_subarray_sum(nums, k):
    l = curr = ans = 0

    for r in range(len(nums)):
        curr += nums[r]

        while curr >= k:
            curr -= nums[l]
            l += 1

        ans = max(ans, r - l + 1)
    
    return ans

nums = [1, 2, 3]
k = 5
print(longest_subarray_sum(nums, k))
# Output: 2  --> Subarray [2, 3] (length 2, sum 5) is the longest subarray with sum <= 6.


"""
Overview for Each Iteration
Input: nums = [1, 2, 3], k = 5

Step: Find longest subarray with sum <= k using sliding window
r | nums[r] | curr | l | curr > k | ans
- | -       | 0    | 0 | -        | 0
0 | 1       | 1    | 0 | No       | 1
1 | 2       | 3    | 0 | No       | 2
2 | 3       | 6    | 1 | Yes      | 2
  |         | 5    | 2 | No       | 2

Final: 2 ([2, 3])

"""

# ––––––––––––––––––––––––––––––––––––––––––––––––
# Incorrect: demonstrates the bug caused by moving l += 1 outside the while loop

def longest_subarray_sum(nums, k):
    l = curr = ans = 0

    for r in range(len(nums)):
        curr += nums[r]

        while curr >= k:
            curr -= nums[l]

        l += 1  # Error, should be inside while loop

        ans = max(ans, r - l + 1)
    
    return ans

nums = [1, 2, 3]
k = 5
print(longest_subarray_sum(nums, k))
# Output: 0


"""
Overview for Each Iteration
Input: nums = [1, 2, 3], k = 5

Step: Find longest subarray with sum <= k using sliding window
r | nums[r] | curr | l | curr >= k | ans
- | -       | 0    | 0 | -         | 0
0 | 1       | 1    | 1 | No        | 0
1 | 2       | 3    | 2 | No        | 0
2 | 3       | 6    | 2 | Yes       | 0
  |         | 3    | 3 | No        | 0
  
Final: 0

"""



