# 2351. First Letter to Appear Twice

# Example 2
    # Given a string s consisting of lowercase English letters, return the first letter to appear twice.

# Note:
    # A letter 'a' appears twice before another letter 'b' if the second occurrence of 'a' is before the second occurrence of 'b'.

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
# Output: "c" → The letter 'c' is the first to appear twice

"""
Time: O(N)
  - Let N = length of string s.
  - Loop through s once → O(N).
      • Check if each character is in the set → O(1) average.
      • Add character to set if not seen → O(1).
  - Stops early once a duplicate is found, but worst case still O(N).
  - Overall: O(N).

Space: O(1)
  - The set 'seen' can store at most 26 lowercase English letters (constant bound).
  - A few variables (loop variable c) use O(1) space.
  - Overall: O(1).

  
Interview Answer: Worst Case

Time: O(N)
  - Each character checked once with O(1) set operations.

Space: O(1)
  - Set stores at most 26 letters, constant space.


Overview for Each Iteration
Input: s = "abccbaacz"

Step 1: Find first letter to appear twice
i  | c  | seen       | c in seen | Action
---|----|------------|-----------|----------------
0  | a  | {a}        | False     | Add 'a' to seen
1  | b  | {a, b}     | False     | Add 'b' to seen
2  | c  | {a, b, c}  | False     | Add 'c' to seen
3  | c  | {a, b, c}  | True      | Return 'c'

Final: "c"



Most IMPORTANT thing to Understand:
    • We need the first character that repeats in the string.

    • A repeat means: we see the same letter twice as we scan left to right.

    • Once we find a letter already seen before, we return it immediately.

    
Why this code Works:
    • seen (a set) stores letters we've already visited.

    • As soon as a letter is already in seen, that's the first repeat (because we're going left to right).

    • Efficiency: one pass through the string, O(n) time, O(n) space.

    • Intuition: Like checking off names on a guest list — the first person who shows up twice is the answer.

    
TLDR
    • Keep a set of letters, return the first one that shows up twice while scanning.

    
Quick Example Walkthrough:
s = "abccbaacz"

    See 'a' → not in set, add → seen = {a}
    See 'b' → not in set, add → seen = {a, b}
    See 'c' → not in set, add → seen = {a, b, c}
    See 'c' again → already in set → return 'c'

Final Answer: "c"

"""



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

"""
Overview for Each Iteration
Input: s = "abccbaacz"

Step: Find first letter to appear twice using brute force
i   | c   | j   | s[j] | s[j] == c | Action
----|-----|-----|------|-----------|----------------
0   | a   | -   | -    | -         | No comparison
1   | b   | 0   | a    | False     | Continue
2   | c   | 0   | a    | False     | Continue
2   | c   | 1   | b    | False     | Continue
3   | c   | 0   | a    | False     | Continue
3   | c   | 1   | b    | False     | Continue
3   | c   | 2   | c    | True      | Return 'c'

Final: "c"

"""


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