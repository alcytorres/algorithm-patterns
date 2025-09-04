# 2351. First Letter to Appear Twice

# Example 2
# Given a string s consisting of lowercase English letters, return the first letter to appear twice.

# Note:
    # A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.

    # s will contain at least one letter that appears twice.

# Example
    # Input: s = "abccd"
    # Output: "c"

# Solution: https://leetcode.com/problems/first-letter-to-appear-twice/description/

def repeatedCharacter(s):
    seen = set()
    for c in s:
        if c in seen:
            return c
        seen.add(c)

    return ""

s = "abccbaacz"
print(repeatedCharacter(s))
# Output: c

# Time: O(n)
# - Loop through the string once: O(n) iterations.
# - Set lookups ('if c in seen') and inserts ('seen.add(c)') are O(1) on average.
# - No nested loops, so total time is O(n).

# Space: O(n)
# - Set 'seen' can store up to n characters in the worst case (when no repeat is found until the end), O(n) space.
# - A few variables (c) take O(1) space.
# - Overall: O(n) total space.
# - If we exclude the set from consideration, extra working space is O(1).


# Overview for Each Iteration
# Input: s = "abccbaacz"
# Step: Find first letter to appear twice
# i  | c   | seen            | Action
# 0  | a   | {a}            | Add 'a' to seen
# 1  | b   | {a, b}         | Add 'b' to seen
# 2  | c   | {a, b, c}      | Add 'c' to seen
# 3  | c   | {a, b, c}      | Found 'c' in seen, return 'c'
# Final: "c"


# ––––––––––––––––––––––––––––––––––––––––––––––– 
# # Breakdown
def repeatedCharacter(s):
    seen = set()               # Initialize empty set for seen characters
    for c in s:                # Iterate over each character in string
        if c in seen:          # If character already in set
            return c           # Return first repeated character
        seen.add(c)            # Add character to set
    return ""                  # Return empty string if no character repeats



# ––––––––––––––––––––––––––––––––––––––––––––––––
# Task: Find the first letter in a string that appears twice (second occurrence comes before any other letter's second occurrence).
# Example: s = "abccbaacz" → Output = "c" (c appears at indices 2 and 3, first to repeat)
# Why: Practices hash set usage to efficiently track character occurrences.

def repeatedCharacter(s):  # Example: s = "abccbaacz"

    # 1️⃣ Initialize a set to track seen characters
    # Create an empty set to store characters we've encountered
    # Why? We need to check if a character has appeared before in O(1) time
    seen = set()  # seen = {}

    # 2️⃣ Iterate through the string
    # Loop through each character in the string
    # Why? We need to find the first character that repeats
    for c in s:  # c takes values ['a', 'b', 'c', 'c', 'b', 'a', 'a', 'c', 'z']
        # --- Iteration 1: c = 'a' ---
        # Check if the current character is in the set
        # Why? If it's in the set, it's the first character to appear twice
        if c in seen:  # c = 'a', seen = {}, 'a' not in seen, skip
            return c  # skip
        # Add the current character to the set
        # Why? We track characters to detect future repeats
        seen.add(c)  # seen = {'a'}
        # After Iteration 1: seen = {'a'}

        # --- Iteration 2: c = 'b' ---
        if c == 'b':
            if c in seen:  # c = 'b', seen = {'a'}, 'b' not in seen, skip
                return c
            seen.add(c)  # seen = {'a', 'b'}
            # After Iteration 2: seen = {'a', 'b'}

        # --- Iteration 3: c = 'c' ---
        if c == 'c' and len(seen) == 2:
            if c in seen:  # c = 'c', seen = {'a', 'b'}, 'c' not in seen, skip
                return c
            seen.add(c)  # seen = {'a', 'b', 'c'}
            # After Iteration 3: seen = {'a', 'b', 'c'}

        # --- Iteration 4: c = 'c' ---
        if c == 'c' and len(seen) == 3:
            if c in seen:  # c = 'c', seen = {'a', 'b', 'c'}, 'c' in seen, true
                return c  # return 'c'
            seen.add(c)  # skip (return statement executes)
            # After Iteration 4: return 'c' (loop exits)

        # --- Remaining iterations ---
        # Not reached due to return in Iteration 4

    # 3️⃣ Return empty string if no repeat is found
    # Why? The problem guarantees a repeat, so this is not reached
    return ""  # skip


print(repeatedCharacter("abccbaacz"))  # Output: "c"






# ––––––––––––––––––––––––––––––––––––––––––––––––
# My Original Solution
def repeatedCharacter(s):
    seen = set()
    for i in range(len(s)):
        c = s[i]
        if c in seen:
            return c
        seen.add(c)

    return ""

print(repeatedCharacter("abccbaacz"))
# Output: c

# Time: O(n) - Single pass through string of length n.
# Space: O(n) - Set stores up to n unique characters.


# ––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force
def repeatedCharacter(s):
    for i in range(len(s)):
        c = s[i]
        for j in range(i):
            if s[j] == c:
                return c
    return ""

print(repeatedCharacter("abccbaacz"))
# Output: c

# Time: O(n^2)
# Space: 