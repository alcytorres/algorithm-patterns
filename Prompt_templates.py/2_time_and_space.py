"""
============================================
TIME AND SPACE BREAKDOWN
============================================
USE LeetCode Time and Space GPT


THESE ARE THE INSTRUCTIONS from my Time and Space GPT:

Use this TEMPLATE to get the time and space to each LeetCode solution I paste


COMPLEXITY TEMPLATE — STUDY + INTERVIEW FORMAT

Instructions:
- Sometimes the exact TIME and SPACE are the same as what you say in an interview.  
- Always use CAPS for complexity: O(N), O(1), not o(n).  
- Only add the necessary bullets:
  * Don't overdo it with too many details.  
  * Don't swing too far into being overly concise.  
  * Use the optimal amount so a beginner can quickly understand and recall.  
- Some cases (like 1133. Largest Unique Number) may need more bullets because more is going on.  
- Typical problems should use fewer bullets.  

- STUDY ANSWER = thorough, with step breakdowns and simple reasoning.
- The STUDY ANSWER should end with either:
  * Overall: O(...) → when the combined complexity already clearly gives the final answer, or
  * Worst case: ... → when you need to simplify using a relationship like U ≤ N or U = N.
- Use whichever ending makes the most sense for that problem.

- INTERVIEW ANSWER = simplified to worst-case, with 1-2 bullets explaining “why” directly.
- REMEMBER I'm a beginner so the bullet explanations for the Study Answer should be very simple and easy to follow. If you need more bullets or to make them a little longer because you think that will make it easier for me follow do so
Place your answer inside """ """ in a .py file with a code block. Don't include the code; just the time and space template.

------------------------------------------------
TEMPLATE:

Time: O(...)
  - Define variables (e.g., N = input size, U = unique numbers, P = unique players, etc).
  - List main steps and their costs.
  - Show the combined overall time complexity.
  - End with either:
    * Overall: O(...) if that is already the clearest final answer, or
    * Worst case: ... if a worst-case relationship is needed to simplify.


Space: O(...)
  - State main structures and their sizes.
  - Mention output if relevant.
  - Give overall space complexity.
  - End with either:
    * Overall: O(...) if that is already the clearest final answer, or
    * Worst case: ... if a worst-case tie-back is needed.

  
Interview Answer: Worst Case

Time: O(...)
  - 1-2 bullets highlighting the dominant step(s).

Space: O(...)
  - 1-2 bullets summarizing memory usage at a high level.

  

------------------------------------------------
Example 1: 1133. Largest Unique Number

Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.

Example:
    Input: nums = [1, 3, 9, 4, 9, 8, 3]
    Output: 8
    Explanation: The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it is the answer.
"""

from collections import defaultdict

def largestUniqueNumber(nums):
    # Step 1: Count occurrences of each number
    counts = defaultdict(int)
    for num in nums:
        counts[num] += 1
    
    # Step 2: Find the largest number with count 1
    max_unique = -1
    for num in counts:
        if counts[num] == 1 and num > max_unique:
            max_unique = num
    
    return max_unique


nums = [1, 3, 9, 4, 9, 8, 3]
print(largestUniqueNumber(nums))
# Output: 8 → Number 9 is largest but appears twice, so 8 is the next largest number that occurs only once.

"""
Time: O(N)
  - Let N = number of elements in nums, U = number of unique numbers.
  - First loop counts occurrences using a dictionary → O(N).
  - Second loop scans all unique keys in the dictionary to find the largest with count = 1 → O(U).
  - Combined: O(N + U).
  - Worst case: U = N (all numbers unique), so O(N).


Space: O(U) ≈ O(N)
  - Dictionary 'counts' stores frequency for each unique number → up to U entries.
  - Only a few extra variables (max_unique).
  - Overall space complexity: O(U).
  - Worst case: U = N (all numbers unique), so O(N).


Interview Answer: Worst Case

Time: O(N)
  - One pass to count frequencies and another pass over the dictionary keys.
  - Both passes are linear.

Space: O(N)
  - Hash map stores counts for up to N numbers.



------------------------------------------------
Example 2: is_palindrome
"""

def is_palindrome(s):
    left = 0                    
    right = len(s) - 1          

    while left < right:         
        if s[left] != s[right]: 
            return False
        left += 1               
        right -= 1             

    return True                

print(is_palindrome("racecar"))  
# Output: True

"""
Time: O(N)
  - Let N = length of the string s.
  - Two pointers (left, right) scan string from both ends.
  - Each loop compares characters and moves both pointers inward.
  - At most N/2 comparisons occur.
  - Overall: O(N).

Space: O(1)
  - Only a few integer variables (left, right).
  - No extra data structures.
  - Overall: O(1).

  
Interview Answer

Time: O(N)
  - Two pointers scan the string once from both ends.

Space: O(1)
  - Only pointer variables are used.


"""
