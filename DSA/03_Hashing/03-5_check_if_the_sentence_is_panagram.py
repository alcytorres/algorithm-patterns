# 1832. Check if the Sentence Is Pangram

# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

# Solution: https://leetcode.com/problems/check-if-the-sentence-is-pangram/editorial/


# Example:
    # Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
    # Output: True
    # Explanation: sentence contains at least one of every letter of the English alphabet.


def checkIfPangram(sentence):
    seen = set(sentence)
    return len(seen) == 26

s = "thequickbrownfoxjumpsoverthelazydog"
print(checkIfPangram(s))
# Output: True

# Time: O(n)
# - Creating the set from the sentence: O(n), where n is the length of the sentence.
# - Checking the length of the set is O(1).
# - Overall: O(n) time.

# Space: O(1)
# - Set 'seen' can store at most 26 letters (constant size), so O(1) space.
# - A few variables (sentence, seen) take O(1) space.
# - Overall: O(1) space.


"""
Overview for Each Iteration
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"

Step: Create set of unique characters and check length
seen = set(sentence)
seen = {'t', 'h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 'l', 'a', 'z', 'y', 'd', 'g'}
len(seen) = 26

Final: True (26 unique letters, including all alphabet letters)

"""


# ––––––––––––––––––––––––––––––––––––––––––––––– 
# Breakdown

def checkIfPangram(sentence):
    # Add every letter of 'sentence' to hash set 'seen'.
    seen = set(sentence)
    # If the size of 'seen' is 26, then 'sentence' is a pangram.
    return len(seen) == 26

s = "thequickbrownfoxjumpsoverthelazydog"
print(checkIfPangram(s))
# Output: True



# ––––––––––––––––––––––––––––––––––––––––––––––– 
# Task: Check if a string is a pangram (contains every lowercase English letter at least once).
# Example: sentence = "thequickbrownfoxjumpsoverthelazydog" → Output = True (contains all 26 letters)
# Why: Practices set usage to efficiently track unique characters.

def checkIfPangram(sentence):  # Example: sentence = "thequickbrownfoxjumpsoverthelazydog"

    # 1️⃣ Create a set of unique characters
    # Convert sentence to a set to get unique characters
    # Why? We need to count distinct letters, ignoring duplicates and non-letters
    seen = set(sentence)  # seen = {'t', 'h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 'l', 'a', 'z', 'y', 'd', 'g'}

    # 2️⃣ Check if set contains all 26 letters
    # Return True if the set has exactly 26 elements
    # Why? A pangram has all 26 lowercase English letters; non-letters don't affect the count
    return len(seen) == 26  # len(seen) = 26, 26 == 26 is True


# Test the function
s = "thequickbrownfoxjumpsoverthelazydog"
print(checkIfPangram(s))  # Output: True






# ––––––––––––––––––––––––––––––––––––––––––––––––
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


# ––––––––––––––––––––––––––––––––––––––––––––––––
# Robust Pangram Check: Filters Non-Letters, Handles Duplicates and Spaces
def checkIfPangram(sentence):
    seen = set(c for c in sentence if c.isalpha())
    return len(seen) == 26

s = "thequickbrownfoxjumpsoverthelazydog"
print(checkIfPangram(s))
# Output: True