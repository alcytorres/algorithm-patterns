# 1941. Check if All Characters Have Equal Number of Occurrences

# Example 3: 
# Given a string s, determine if all characters have the same frequency.

# A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

# For example, given s = "abacbc", return true, because all characters appear twice. Given s = "aaabb", return false. "a" appears 3 times, "b" appears 2 times. 3 != 2.

# Example:
# Input: s = "abacbc"
# Output: True
# Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.

# Solution: https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/solutions/


from collections import defaultdict

def areOccurrencesEqual(s):
    counts = defaultdict(int)
    for c in s:
        counts[c] += 1
    
    frequencies = counts.values()
    return len(set(frequencies)) == 1

string = "abacbc"
print(areOccurrencesEqual(string))







# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# My attempt at a solution which is wrong

from collections import defaultdict

def areOccurrencesEqual(s):
    counts = defaultdict(int)
    for right in range(len(s)):
        counts[s[right]] += 1
    
    seen = set(s)
    for c in seen:
        if c == 2:
            return True
        return False

string = "abacbc"
print(areOccurrencesEqual(string))


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# My attempt at a solution which is wrong
from collections import defaultdict

def areOccurrencesEqual(s):
    counts = defaultdict(int)
    for right in range(len(s)):
        counts[s[right]] += 1
    
    if counts['c'] == 2:
        return True
    return False


string = "abacbc"
print(areOccurrencesEqual(string))