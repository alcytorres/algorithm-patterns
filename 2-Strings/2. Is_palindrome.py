"""
Task: Check if a string is a palindrome (reads the same forwards and backwards).

Example 1: "racecar" → True
Example 2: "hello" → False

Why: Introduces comparison and indexing in strings.
"""

def is_palindrome(s):
    # 1️⃣ Initialize two pointers: one at start, one at end
    left = 0
    right = len(s) - 1
    
    # 2️⃣ Compare characters moving towards the center
    while left < right:
        if s[left] != s[right]:  # If mismatch found, not a palindrome
            return False
        left += 1
        right -= 1
    
    # 3️⃣ If all comparisons pass, it’s a palindrome
    return True

# Test the function
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False

# Simple Breakdown
"""
Checks if a string is a palindrome.
- Uses two pointers to compare characters from both ends.
- Time Complexity: O(n), Space Complexity: O(1).
- Simple and direct string comparison.
"""