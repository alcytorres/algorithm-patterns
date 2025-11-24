# Example 2: Longest Substring with At Most One "0"

# Finds the longest substring with at most one "0" by flipping at most one "0" to "1". 

# In other words "what is the longest substring that contains at most one "0"?

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

s = "11001011"
print(longest_substring_one_zero(s))  
# Output: 4  →  Substring "1011" (length 4, one "0") is the longest with at most one "0".

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



Overview for Each Iteration
Input: s = "11001011"

Step: Find longest substring with at most one "0" using sliding window
r   | s[r] | curr | curr > 1 | l  | s[l] | Action              | ans
----|------|------|----------|----|------|---------------------|----
0   | 1    | 0    | No       | 0  | -    | ans=max(0,0-0+1)=1  | 1
1   | 1    | 0    | No       | 0  | -    | ans=max(1,1-0+1)=2  | 2
2   | 0    | 1    | No       | 0  | -    | ans=max(2,2-0+1)=3  | 3
3   | 0    | 2    | Yes      | 0  | 1    | l+=1                | 3
    |      | 2    | Yes      | 1  | 1    | l+=1                | 3
    |      | 2    | Yes      | 2  | 0    | curr-=1, l+=1       | 3
    |      | 1    | No       | 3  | -    | ans=max(3,3-3+1)=3  | 3
4   | 1    | 1    | No       | 3  | -    | ans=max(3,4-3+1)=3  | 3
5   | 0    | 2    | Yes      | 3  | 0    | curr-=1, l+=1       | 3
    |      | 1    | No       | 4  | -    | ans=max(3,5-4+1)=3  | 3
6   | 1    | 1    | No       | 4  | -    | ans=max(3,6-4+1)=3  | 3
7   | 1    | 1    | No       | 4  | -    | ans=max(3,7-4+1)=4  | 4

Final: 4 ("1011")




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




# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Task: Find the length of the longest substring with at most one "0" in a binary string.
# Example: s = "11001011" → Output = 4 (substring "1011" has one "0", length 4)
# Why: Practices sliding window technique to maintain a constraint (at most one "0").

def longest_substring_one_zero(s):  # Example: s = "11001011"

    # 1️⃣ Initialize variables
    # Initialize left pointer for the sliding window
    # Why? We use left to shrink the window when we have too many zeros
    left = 0  # left = 0

    # Initialize current count of zeros in the window
    # Why? We track the number of "0"s to ensure it doesn't exceed 1
    curr = 0  # curr = 0

    # Initialize answer to track the length of the longest valid substring
    # Why? We need to store the maximum length of substrings with at most one "0"
    ans = 0  # ans = 0

    # 2️⃣ Iterate with right pointer
    # Loop through the string with right pointer to expand the window
    # Why? We process each character to build windows and track valid substrings
    for right in range(len(s)):  # right goes from 0 to 7 (len(s) = 8)
        # --- Iteration 1: right = 0 ---
        # Check if the current character is "0" and increment count if it is
        # Why? We need to track zeros to enforce the at-most-one-zero constraint
        if s[right] == "0":  # s[0] = "1", not "0", skip
            curr += 1  # skip
        # Shrink window if we have more than one "0"
        # Why? We need to maintain at most one "0" in the window
        while curr > 1:  # curr = 0, 0 > 1 is false, skip
            if s[left] == "0":  # skip
                curr -= 1
            left += 1
        # Update the maximum length of valid substrings
        # Why? The current window length (right - left + 1) may be the longest so far
        ans = max(ans, right - left + 1)  # right = 0, left = 0, ans = max(0, 0 - 0 + 1) = 1
        # After Iteration 1: left = 0, curr = 0, ans = 1
        # Current window: "1" (0 zeros, length 1)

        # --- Iteration 2: right = 1 ---
        if right == 1:
            if s[right] == "0":  # s[1] = "1", not "0", skip
                curr += 1
            while curr > 1:  # curr = 0, 0 > 1 is false, skip
                if s[left] == "0":
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)  # right = 1, left = 0, ans = max(1, 1 - 0 + 1) = 2
            # After Iteration 2: left = 0, curr = 0, ans = 2
            # Current window: "11" (0 zeros, length 2)

        # --- Iteration 3: right = 2 ---
        if right == 2:
            if s[right] == "0":  # s[2] = "0", true
                curr += 1  # curr = 0 + 1 = 1
            while curr > 1:  # curr = 1, 1 > 1 is false, skip
                if s[left] == "0":
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)  # right = 2, left = 0, ans = max(2, 2 - 0 + 1) = 3
            # After Iteration 3: left = 0, curr = 1, ans = 3
            # Current window: "110" (1 zero, length 3)

        # --- Iteration 4: right = 3 ---
        if right == 3:
            if s[right] == "0":  # s[3] = "0", true
                curr += 1  # curr = 1 + 1 = 2
            while curr > 1:  # curr = 2, 2 > 1 is true
                if s[left] == "0":  # s[0] = "1", not "0", skip
                    curr -= 1
                left += 1  # left = 0 + 1 = 1
                # Check again: curr = 2, 2 > 1 is true
                if s[left] == "0":  # s[1] = "1", not "0", skip
                    curr -= 1
                left += 1  # left = 1 + 1 = 2
                # Check again: curr = 2, 2 > 1 is true
                if s[left] == "0":  # s[2] = "0", true
                    curr -= 1  # curr = 2 - 1 = 1
                left += 1  # left = 2 + 1 = 3
                # Check again: curr = 1, 1 > 1 is false, exit while
            ans = max(ans, right - left + 1)  # right = 3, left = 3, ans = max(3, 3 - 3 + 1) = 3
            # After Iteration 4: left = 3, curr = 1, ans = 3
            # Current window: "0" (1 zero, length 1)

        # --- Iteration 5: right = 4 ---
        if right == 4:
            if s[right] == "0":  # s[4] = "1", not "0", skip
                curr += 1
            while curr > 1:  # curr = 1, 1 > 1 is false, skip
                if s[left] == "0":
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)  # right = 4, left = 3, ans = max(3, 4 - 3 + 1) = 3
            # After Iteration 5: left = 3, curr = 1, ans = 3
            # Current window: "01" (1 zero, length 2)

        # --- Iteration 6: right = 5 ---
        if right == 5:
            if s[right] == "0":  # s[5] = "0", true
                curr += 1  # curr = 1 + 1 = 2
            while curr > 1:  # curr = 2, 2 > 1 is true
                if s[left] == "0":  # s[3] = "0", true
                    curr -= 1  # curr = 2 - 1 = 1
                left += 1  # left = 3 + 1 = 4
                # Check again: curr = 1, 1 > 1 is false, exit while
            ans = max(ans, right - left + 1)  # right = 5, left = 4, ans = max(3, 5 - 4 + 1) = 3
            # After Iteration 6: left = 4, curr = 1, ans = 3
            # Current window: "10" (1 zero, length 2)

        # --- Iteration 7: right = 6 ---
        if right == 6:
            if s[right] == "0":  # s[6] = "1", not "0", skip
                curr += 1
            while curr > 1:  # curr = 1, 1 > 1 is false, skip
                if s[left] == "0":
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)  # right = 6, left = 4, ans = max(3, 6 - 4 + 1) = 3
            # After Iteration 7: left = 4, curr = 1, ans = 3
            # Current window: "101" (1 zero, length 3)

        # --- Iteration 8: right = 7 ---
        if right == 7:
            if s[right] == "0":  # s[7] = "1", not "0", skip
                curr += 1
            while curr > 1:  # curr = 1, 1 > 1 is false, skip
                if s[left] == "0":
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)  # right = 7, left = 4, ans = max(3, 7 - 4 + 1) = 4
            # After Iteration 8: left = 4, curr = 1, ans = 4
            # Current window: "1011" (1 zero, length 4)

    # 3️⃣ Return the length of the longest valid substring
    # Why? ans contains the length of the longest substring with at most one "0"
    return ans  # ans = 4


s = "11001011"
print(longest_substring_one_zero(s))  
# Output: 4 
# Substring "1011" (length 4, one "0") is the longest with at most one "0".