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

print(repeatedCharacter("abccbaacz"))
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



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
def repeatedCharacter(s):
    seen = set()               # Initialize empty set for seen characters
    for c in s:                # Iterate over each character in string
        if c in seen:          # If character already in set
            return c           # Return first repeated character
        seen.add(c)            # Add character to set
    return ""                  # Return empty string if no character repeats



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
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


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
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