"""
Pattern Matching
Task: Find the starting indices of all occurrences of a substring in a string.

Example 1: s="hello", sub="ll" → [2]
Example 2: s="aaaa", sub="aa" → [0, 1, 2]

Why: Teaches basic string searching and indexing.
"""

def find_substring_occurrences(s, sub):
    # 1️⃣ Initialize list to store indices
    indices = []
    
    # 2️⃣ Check each possible starting position
    for i in range(len(s) - len(sub) + 1):
        if s[i:i + len(sub)] == sub:  # If substring matches at this position
            indices.append(i)  # Record the starting index
    
    # 3️⃣ Return all found indices
    return indices

# Test the function
print(find_substring_occurrences("hello", "ll"))  # Output: [2]
print(find_substring_occurrences("aaaa", "aa"))   # Output: [0, 1, 2]

# Simple Breakdown
"""
Finds all occurrences of a substring in a string.
- Checks each position for a match using string slicing.
- Time Complexity: O(n*m), Space Complexity: O(k) where k is number of occurrences.
- Brute-force approach is beginner-friendly and clear.
"""