# 1832. Check if the Sentence Is Pangram
"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

Example:
    Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
    Output: True
    Explanation: sentence contains at least one of every letter of the English alphabet.

Solution: https://leetcode.com/problems/check-if-the-sentence-is-pangram/editorial/
"""

def checkIfPangram(sentence):
    seen = set(sentence)
    return len(seen) == 26

sentence = "thequickbrownfoxjumpsoverthelazydog"
print(checkIfPangram(sentence))
# Output: True

# seen = {'w', 'f', 'y', 'h', 'j', 'r', 'v', 'l', 'z', 't', 'i', 'n', 'm', 's', 'e', 'k', 'x', 'a', 'g', 'p', 'c', 'd', 'q', 'b', 'u', 'o'}


# ––––––––––––––––––––––––––––––––––––––––––––––– 
# Breakdown

def checkIfPangram(sentence):
    # Add every letter of 'sentence' to hash set 'seen'.
    seen = set(sentence)
    # If the size of 'seen' is 26, then 'sentence' is a pangram.
    return len(seen) == 26


"""
Time: O(N)
  - Let N = length of sentence.
  - Step 1: Build a set from all characters in the sentence → O(N).
      • Each character is inserted once, with O(1) average per insertion.
  - Step 2: Compare set size to 26 → O(1).
  - Overall: O(N).

Space: O(1)
  - One extra structure: set `seen` (unique letters found).
  - Only lowercase English letters exist → the set holds at most 26 entries.
  - Set size is capped by the alphabet, not by N.
  - Overall: O(1).


Interview Answer: Worst Case

Time: O(N)
  - One pass through sentence to build the set.

Space: O(1)
  - Alphabet is fixed at 26 letters → set never exceeds 26 entries.


---
Most IMPORTANT thing to Understand:
    • A pangram must contain every lowercase English letter at least once.

    • We only care about which letters appear — not how many times each one shows up.

    • A set automatically removes duplicates, so we can just count how many unique letters we found.

    • If the set has exactly 26 unique letters, every letter a–z is present → it's a pangram.


---
Why this code Works:
    • Data structure: a set stores only unique characters from the sentence.

    • Technique: `set(sentence)` collects every distinct letter in one pass.

    • Final check: if `len(seen) == 26`, all 26 alphabet letters were found.

    • Efficiency: One pass through the string. Set insert and size check are O(1) average.

    • Intuition: Like collecting unique stamps — if your album has all 26 letters of the alphabet, the sentence is a pangram.


---
TLDR:
    • Put all unique letters into a set; if the set has 26 entries, the sentence is a pangram.


---
Quick Example Walkthrough:

    sentence = "thequickbrownfoxjumpsoverthelazydog"

    Step 1: Build set from sentence
        seen = {'t', 'h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 'l', 'a', 'z', 'y', 'd', 'g'}

    Step 2: Check size
        len(seen) = 26
        26 == 26 → True

Final Answer: True


---
Full Example Walkthrough:
    sentence = "thequickbrownfoxjumpsoverthelazydog"

    Starting State:
        seen = {} (empty set)

    Building set — Python loops through each character:
        't' → add → seen = {'t'}
        'h' → add → seen = {'t', 'h'}
        'e' → add → seen = {'t', 'h', 'e'}
        'q' → add → seen = {'t', 'h', 'e', 'q'}
        ...
        (duplicates like extra 'e', 'o', 'u' are ignored — sets only keep one copy)
        ...
        'g' → add → seen = {all 26 letters}

    Final Check:
        len(seen) == 26
        26 == 26 → True

        This means:
            Every letter a-z appears at least once in the sentence.

"""



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

# Time: O(N) — one pass to build set + O(1) size check.
# Space: O(1) — set holds at most 26 letters.

# ––––––––––––––––––––––––––––––––––––––––––––––––
# My original solution

def checkIfPangram(sentence: str) -> bool:
    seen = set()
    for c in sentence:
        seen.add(c)
    return len(seen) == 26

sentence = "thequickbrownfoxjumpsoverthelazydog"
print(checkIfPangram(sentence))
# Output: True

# Time: O(N) — loop each char once, O(1) add per char.
# Space: O(1) — set holds at most 26 letters.


# ––––––––––––––––––––––––––––––––––––––––––––––––
# Robust Pangram Check: Filters Non-Letters, Handles Duplicates and Spaces
def checkIfPangram(sentence):
    seen = set(c for c in sentence if c.isalpha())
    return len(seen) == 26

s = "thequickbrownfoxjumpsoverthelazydog"
print(checkIfPangram(s))
# Output: True

# Time: O(N) — one pass; isalpha() and set insert are O(1) each.
# Space: O(1) — set holds at most 26 letters.

