"""
Task: Count the frequency of each character in a string.

Example 1: "hello" → {'h':1, 'e':1, 'l':2, 'o':1}
Example 2: "world" → {'w':1, 'o':1, 'r':1, 'l':1, 'd':1}

Why: Introduces dictionaries for counting and basic iteration.
"""

def count_characters(s):
    # 1️⃣ Initialize an empty dictionary to store frequencies
    freq = {}
    
    # 2️⃣ Iterate through string, counting each character
    for char in s:
        if char in freq:
            freq[char] += 1  # Increment count if character exists
        else:
            freq[char] = 1   # Initialize count if character is new
    
    # 3️⃣ Return the frequency dictionary
    return freq

# Test the function
print(count_characters("hello"))  # Output: {'h':1, 'e':1, 'l':2, 'o':1}
print(count_characters("world"))  # Output: {'w':1, 'o':1, 'r':1, 'l':1, 'd':1}

# Simple Breakdown
"""
Counts character frequencies in a string.
- Uses a dictionary to track occurrences of each character.
- Time Complexity: O(n), Space Complexity: O(k) where k is unique characters.
- Teaches dictionary usage in string processing.
"""