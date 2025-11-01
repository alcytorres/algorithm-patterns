"""
Pattern Matching
Task: Check if a string is a subsequence of another string.

Example 1: s="abc", t="ahbgdc" → True
Example 2: s="axc", t="ahbgdc" → False

Why: Introduces the concept of subsequences and two-pointer technique.
"""

def is_subsequence(s, t):
    # 1️⃣ Initialize pointers for both strings
    i = 0  # Pointer for subsequence
    j = 0  # Pointer for main string
    
    # 2️⃣ Traverse both strings
    while i < len(s) and j < len(t):
        if s[i] == t[j]:  # If characters match
            i += 1  # Move subsequence pointer
        j += 1  # Always move main string pointer
    
    # 3️⃣ Check if entire subsequence was matched
    return i == len(s)

# Test the function
print(is_subsequence("abc", "ahbgdc"))  # Output: True
print(is_subsequence("axc", "ahbgdc"))  # Output: False

# Simple Breakdown
"""
Checks if one string is a subsequence of another.
- Uses two pointers to match characters in order.
- Time Complexity: O(n), Space Complexity: O(1).
- Simple and effective for subsequence checking.
"""