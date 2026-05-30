# 2351. First Letter to Appear Twice
"""
Given a string s consisting of lowercase English letters, return the first letter to appear twice.

Note:
    A letter 'a' appears twice before another letter 'b' if the second occurrence of 'a' is before the second occurrence of 'b'.

    s will contain at least one letter that appears twice.

Example
    Input: s = "abccd"
    Output: "c"

Solution: https://leetcode.com/problems/first-letter-to-appear-twice/description/
"""

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


# ––––––––––––––––––––––––––––––––––––––––––––––– 
# Breakdown
def repeatedCharacter(s):
    seen = set()          # Initialize empty set for seen characters
    for c in s:           # Iterate over each character in string
        if c in seen:     # If character already in set
            return c      # Return first repeated character
        seen.add(c)       # Add character to set
    return ""             # Return empty string if no character repeats


"""
Time: O(N)
  - Let N = length of string s.
  - Loop through s once → O(N).
      • Check if each character is in the set → O(1) average.
      • Add character to set if not seen → O(1).
  - Stops early once a duplicate is found, but worst case still O(N).
  - Overall: O(N).

Space: O(1)
  - One extra structure: set `seen` (letters we've already seen).
  - Only lowercase English letters exist → the set can hold at most 26 entries.
  - Even if N is huge, the set never grows with string length — it caps at 26.
  - Overall: O(1).


Interview Answer: Worst Case

Time: O(N)
  - One pass through s; each set check/add is O(1) average.

Space: O(1)
  - Alphabet is fixed at 26 letters → set never exceeds 26 entries.


---
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


---
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


