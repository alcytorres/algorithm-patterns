"""
Pattern Matching
Task: Replace all occurrences of a substring with another substring.

Example 1: s="hello world", old="world", new="universe" → "hello universe"
Example 2: s="aaab", old="aa", new="c" → "cab"

Why: Teaches string replacement and manipulation.
"""

def replace_substring(s, old, new):
    # 1️⃣ Initialize result list to build new string
    result = []
    i = 0
    
    # 2️⃣ Process string, checking for old substring
    while i < len(s):
        if s[i:i + len(old)] == old:  # If old substring found
            result.append(new)  # Append replacement
            i += len(old)  # Skip past the old substring
        else:
            result.append(s[i])  # Append current character
            i += 1
    
    # 3️⃣ Join result list into string and return
    return ''.join(result)

# Test the function
print(replace_substring("hello world", "world", "universe"))  # Output: "hello universe"
print(replace_substring("aaab", "aa", "c"))                   # Output: "cab"

# Simple Breakdown
"""
Replaces all occurrences of a substring with another.
- Builds result by checking for matches and appending accordingly.
- Time Complexity: O(n), Space Complexity: O(n) for the result.
- Clear and manual approach avoids built-in methods for learning.
"""