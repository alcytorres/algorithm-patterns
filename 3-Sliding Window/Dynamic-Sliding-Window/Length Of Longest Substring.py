# Length of Longest Substring without Reapeating Characters

"""
Task: Given a string, find the length of the longest substring without any repeating characters.
Example 1: s = "abcabccc" → Output = 3 (substring "abc")
Example 2: s = "aa"       → Output = 1 (substring "a") 
Example 3: s = "aabbcc"   → Output = 2 (substring "ab" or "bc")
Example 4: s = "eceba"    → Output = 4 (substring "ceba") 
"""

# First approach: Using a set to track unique characters

def lengthOfLongestSubstring(s):
    
    # 1️⃣ Initialize pointers & tracking variables
    left = 0
    longest_substring = 0
    sett = set()
    n = len(s)
    
    # 2️⃣ Expand window by moving `right` & update conditions
    for right in range(n):
        while s[right] in sett:
            sett.remove(s[left])
            left += 1
        
        current_window_size = (right - left) + 1
        longest_substring = max(longest_substring, current_window_size)
        sett.add(s[right])
    
    return longest_substring

print(lengthOfLongestSubstring("abcabccc"))    # Output: 3


# Solution 1 Breakdown
"""
Task: Given a string, find the length of the longest substring without any repeating characters.
Example 1: s = "abcabccc" → Output = 3 (substring "abc")
Example 2: s = "aa"       → Output = 1 (substring "a") 
Example 3: s = "aabbcc"   → Output = 2 (substring "ab" or "bc")
Example 4: s = "eceba"    → Output = 4 (substring "ceba") 
"""

def lengthOfLongestSubstring(s):    # Example: s = "abcabccc"
    # Initialize left pointer for the start of our sliding window
    # Why? We'll slide this to shrink the window when we find repeating characters
    left = 0                       # left = 0 (start at beginning)

    # Track the longest substring length we've found
    # Why? We need to compare and update this as we find longer valid substrings
    longest_substring = 0                    # longest_substring = 0 (no substring checked yet)

    # Create a set to store characters in the current window
    # Why? Sets allow fast lookup to check for repeating characters
    sett = set()                   # sett = {} (empty set)

    # Get the length of the string
    # Why? We'll use this to loop through each character
    n = len(s)                     # n = 8 (for "abcabccc")

    # Loop through each character as the right end of our window
    # Why? We check each character to build valid substrings
    for right in range(n):         # right goes from 0 to 7
                                   # Let's follow right = 0 (s[0] = 'a')
        # If the current character is already in our set, we have a repeat
        # Why? We need to shrink the window until the repeat is gone
        while s[right] in sett:    # s[0] = 'a', sett = {}, 'a' not in sett, skip
            # Remove the leftmost character from the set
            # Why? This shrinks the window from the left
            sett.remove(s[left])   # skip (no repeat yet)
            # Move the left pointer forward
            # Why? We've removed the leftmost character, so adjust the window
            left += 1              # skip (no repeat yet)

        # Calculate the size of the current window
        # Why? This is the length of our current substring with no repeats
        current_window_size = (right - left) + 1  # right = 0, left = 0
                                                 # size = (0 - 0) + 1 = 1

        # Update the longest_substring length if the current window is bigger
        # Why? We want the maximum length of any valid substring
        longest_substring = max(longest_substring, current_window_size)  # max(0, 1) = 1
                                                    # longest_substring = 1

        # Add the current character to the set
        # Why? We've processed it, so include it in our window
        sett.add(s[right])         # sett = {'a'}

        # After right = 0: sett = {'a'}, left = 0, longest_substring = 1
        # Next iterations (briefly):
        # right = 1: s[1] = 'b', not in sett, size = 2, sett = {'a', 'b'}, longest_substring = 2
        # right = 2: s[2] = 'c', not in sett, size = 3, sett = {'a', 'b', 'c'}, longest_substring = 3
        # right = 3: s[3] = 'a', in sett, remove s[0] = 'a', left = 1, size = 3, longest_substring = 3
        # Continues until right = 7

    # Return the length of the longest_substring substring found
    return longest_substring                 # longest_substring = 3 (from substring "abc")


print(lengthOfLongestSubstring("abcabccc"))  # Output: 3 (substring "abc" has length 3)



# ----------------------------------------------------------------------------------

# Second approach: (Identical to the first solution)
def longest_substring_k_distinct(s):
    left = 0
    result = 0
    char_set = set()
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        result = max(result, right - left + 1)
    
    return result

print(longest_substring_k_distinct("abcabccc"))    # Output: 3


# ----------------------------------------------------------------------------------
# Third approach: Using a dictionary to track character positions

def lengthOfLongestSubstring(s):
    start = 0
    end = 0
    max_len = 0
    d = {}
    
    while end < len(s):
        if s[end] in d and d[s[end]] >= start:
            start = d[s[end]] + 1
        max_len = max(max_len, end - start + 1)
        d[s[end]] = end
        end += 1
    
    return max_len

print(lengthOfLongestSubstring("abcabccc"))    # Output: 3


"""
Ranking for Beginners Learning Dynamic Sliding Window:
    - First Approach (Set-Based): Simplest, clearly shows window with a set, intuitive shrinking logic. Best for beginners.
    - Second Approach (Set-Based): Identical to first, equally good but redundant.
    - Third Approach (Dictionary-Based): Efficient but complex due to index tracking, better for intermediate learners.

Are They Good? All are correct and O(n), but set-based approaches are more beginner-friendly due to clarity and simplicity.
"""
