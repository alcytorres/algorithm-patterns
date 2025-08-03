# 1832. Check if the Sentence Is Pangram

# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

# Solution: https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4601/

# Example:
# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.


def checkIfPangram(sentence):
    # Add every letter of 'sentence' to hash set 'seen'.
    seen = set(sentence)
    # If the size of 'seen' is 26, then 'sentence' is a pangram.
    return len(seen) == 26

s = "thequickbrownfoxjumpsoverthelazydog"
print(checkIfPangram(s))
# Output: True

# Time: O(n)
# Space: O



# My original solution
def checkIfPangram(sentence):
    seen = set(sentence)
    if len(seen) == 26:
        return True
    return False

s = "thequickbrownfoxjumpsoverthelazydog"
print(checkIfPangram(s))
# Output: True

# Time: O(n)
# Space: O



# Robust Pangram Check: Filters Non-Letters, Handles Duplicates and Spaces
def checkIfPangram(sentence):
    seen = set(c for c in sentence if c.isalpha())
    return len(seen) == 26

s = "thequickbrownfoxjumpsoverthelazydog"
print(checkIfPangram(s))
# Output: True