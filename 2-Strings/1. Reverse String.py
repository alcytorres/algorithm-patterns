"""
String Manipulation
Task: Reverse a string.

Example 1: "hello" → "olleh"
Example 2: "world" → "dlrow"

Why: Teaches basic string manipulation and Python’s immutability workaround.
"""

def reverse_string(s):
    # 1️⃣ Convert string to list since strings are immutable in Python
    s_list = list(s)
    
    # 2️⃣ Initialize two pointers for swapping
    left = 0
    right = len(s_list) - 1
    
    # 3️⃣ Swap characters from ends towards the center
    while left < right:
        s_list[left], s_list[right] = s_list[right], s_list[left]
        left += 1
        right -= 1
    
    # 4️⃣ Join list back to string and return
    return ''.join(s_list)

# Test the function
print(reverse_string("hello"))  # Output: "olleh"
print(reverse_string("world"))  # Output: "dlrow"

# Simple Breakdown
"""
Reverses a string.
- Converts to list, swaps characters with two pointers, then rejoins.
- Time Complexity: O(n), Space Complexity: O(n) for the list.
- Clear introduction to string manipulation.
"""