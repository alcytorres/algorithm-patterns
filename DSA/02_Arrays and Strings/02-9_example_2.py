# Example 2: Longest Substring with At Most One "0"
"""
Finds the longest substring with at most one "0" by flipping at most one "0" to "1". 

In other words "what is the longest substring that contains at most one "0"?
"""

def longest_substring_one_zero(s):
    left = curr = ans = 0        
        
    for right in range(len(s)): 
        if s[right] == "0":     
            curr += 1            
        
        while curr > 1:          
            if s[left] == "0":   
                curr -= 1        
            left += 1            
            
        ans = max(ans, right - left + 1)  
    
    return ans

s = "10101"
print(longest_substring_one_zero(s))
# Output: 3  →  Substring "101" (length 3) is the longest with at most one "0".


"""
Time: O(N)
  - Let N = length of string s.
  - The right pointer (r) expands the window one character at a time → O(N).
  - The left pointer (l) only moves forward when more than one '0' is in the window.
  - Each character is processed (added and possibly removed) at most once.
  - Overall: O(N).

Space: O(1)
  - Only integer counters (l, r, curr, ans) are used.
  - No extra data structures are created.
  - Overall: O(1).

  
Interview Answer: Worst Case

Time: O(N)
  - Sliding window scans each character once.

Space: O(1)
  - Constant extra space for pointers and counters.


---
Overview for Each Iteration
Input: s = "10101"

Step: Find longest substring with at most one "0" using sliding window

r   | s[r] | curr | curr > 1 | l  | s[l] | Action                    | ans
----|------|------|----------|----|------|---------------------------|----
0   | 1    | 0    | No       | 0  | -    | ans=max(0,0-0+1)=1        | 1
1   | 0    | 1    | No       | 0  | -    | ans=max(1,1-0+1)=2        | 2
2   | 1    | 1    | No       | 0  | -    | ans=max(2,2-0+1)=3        | 3
3   | 0    | 2    | Yes      | 0  | 1    | l+=1                      | 3
    |      | 2    | Yes      | 1  | 0    | curr-=1, l+=1             | 3
    |      | 1    | No       | 2  | -    | ans=max(3,3-2+1)=3        | 3
4   | 1    | 1    | No       | 2  | -    | ans=max(3,4-2+1)=3        | 3

Final: 3 ("101")



---
Q: Why is l += 1 outside the if s[l] == "0": block?

  Because we always need to move the left pointer (l) forward when shrinking the window — whether the character is "0" or "1".

    • If it's a "0", we also reduce curr (since that zero leaves the window).

    • If it's a "1", we still move l because we're shrinking the window until it's valid again (curr <= 1).

    • Putting l += 1 outside ensures that the left side always moves, one step at a time.

"""



# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def longest_substring_one_zero(s):
    left = 0          # Left bound of the window
    curr = 0          # Tracks count of "0"s in current window
    ans = 0           # Tracks length of longest valid substring
    
    for right in range(len(s)):  # Iterate right pointer over string
        if s[right] == "0":      # If current character is "0"
            curr += 1            # Increment zero count
        
        while curr > 1:          # Shrink window while zeros exceed 1
            if s[left] == "0":   # If leftmost character is "0"
                curr -= 1        # Decrement zero count
            left += 1            # Move left pointer forward
            
        ans = max(ans, right - left + 1)  # Update max window size
    
    return ans  # Returns the length of the longest substring

