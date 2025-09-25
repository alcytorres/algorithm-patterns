# 383. Ransom Note

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Solution: https://leetcode.com/problems/ransom-note/solutions/540284/ransom-note/

# Example 1:
    # Input: ransomNote = "a", magazine = "b"
    # Output: false

# Example 2:
    # Input: ransomNote = "aa", magazine = "ab"
    # Output: false

# Example 3:
    # Input: ransomNote = "aa", magazine = "aab"
    # Output: true


from collections import Counter

def canConstruct(ransomNote, magazine):
    
    # Check for obvious fail case.
    if len(ransomNote) > len(magazine):
        return False

    letters = Counter(magazine)
    
    # For each character, c, in the ransom note:
    for c in ransomNote:
        # If there are none of c left, return False.
        if letters[c] <= 0:
            return False
        # Remove one of c from the Counter.
        letters[c] -= 1
    # If we got this far, we can successfully build the note.
    return True

ransomNote = "aac"
magazine = "aabc"
print(canConstruct(ransomNote, magazine))
# Output: True


"""
Time: O(M + N)
  - Let N = length of ransomNote, M = length of magazine.
  - Step 1: Build Counter from magazine → O(M).
  - Step 2: Iterate through ransomNote → O(N).
    * Dictionary lookup and decrement → O(1) each.
  - Overall: O(M + N).

Space: O(1) (bounded by alphabet size)
  - Counter 'letters' stores counts of at most 26 lowercase letters.
  - A few loop variables and integers are O(1).
  - Overall: O(1).

  
Interview Answer: Worst Case

Time: O(M + N)
  - Build counts from magazine and check ransomNote.

Space: O(1)
  - Counter stores at most 26 letters.


Overview for Each Iteration
Input: ransomNote = "aac", magazine = "aabc"
Step 1: Check length condition
len(ransomNote) = 3, len(magazine) = 4, 3 <= 4, proceed

Step 2: Create Counter from magazine
letters = Counter({'a':2, 'b':1, 'c':1})

Step 3: Process each character in ransomNote
c   | letters[c] | letters[c] <= 0 | Action         | letters
----|------------|-----------------|----------------|----------------------
a   | 2          | False           | letters[a]-=1  | {'a':1, 'b':1, 'c':1}
a   | 1          | False           | letters[a]-=1  | {'a':0, 'b':1, 'c':1}
c   | 1          | False           | letters[c]-=1  | {'a':0, 'b':1, 'c':0}
Final: True




Most IMPORTANT thing to Understand:
    We just need to check if magazine has at least as many of each letter as ransomNote needs.
    If any letter in ransomNote is missing or runs out in magazine, answer is False.
    A Counter (hash map) stores how many of each letter magazine provides; we decrement as we “use” letters.

    
Why this code Works:
    • Data structure: Counter(magazine) holds counts for each letter so we can check availability in O(1) per letter.

    • Technique: One pass over ransomNote; for each char, verify count > 0, then decrement to mark it used.

    • Efficiency: Build counts in O(M), check in O(N), with constant-time map operations → O(M + N) time, O(1) space (fixed alphabet).

    • Intuition: Like filling a shopping list from pantry stock—if any item hits zero before you finish, you can't complete the list.

TLDR (one sentence):
    • Count letters in magazine and spend them while scanning ransomNote; if any needed letter is unavailable, return False, else True.

    
Quick Example Walkthrough:

    ransomNote = "aac", magazine = "aabc"

    Build counts: {'a':2, 'b':1, 'c':1}

    Use letters in order:

    need 'a' → have 2 → now {'a':1, 'b':1, 'c':1}
    need 'a' → have 1 → now {'a':0, 'b':1, 'c':1}
    need 'c' → have 1 → now {'a':0, 'b':1, 'c':0}

    No shortages occurred → True.

    


-----------------------------------------------------------
Q: Why doesn't using `letters[c] <= 0` vs. `letters[c] == 0` affect the outcome in `canConstruct`?

    • TLDR: the `len(ransomNote) > len(magazine)` check and decrementing after the if letters[c] <= 0: condition

A: 
    • The `if len(ransomNote) > len(magazine): return False` check stops the function early if `ransomNote` needs more characters than `magazine` provides.

    • For valid cases, the condition (`letters[c] <= 0` or `== 0`) is checked **before** decrementing `letters[c]`. If `letters[c] = 0`, both conditions trigger `return False`, stopping the loop before negative counts occur.

    • Example: `ransomNote = "aa"`, `magazine = "aab"`, `letters = {'a': 2, 'b': 1}`:
        • First 'a': `letters['a'] = 2`, both conditions `False`, decrement to 1.
        • Second 'a': `letters['a'] = 1`, both conditions `False`, decrement to 0.
        • Returns `True`.
    
    • Since the check precedes the decrement, both `<= 0` and `== 0` catch exhausted characters at the same point, making them equivalent in this code.

"""



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
from collections import Counter

def canConstruct(ransomNote: str, magazine: str):
    if len(ransomNote) > len(magazine): return False  # Early exit if note longer than magazine

    # In Python, we can use the Counter class. It does all the work that the makeCountsMap(...) function in our pseudocode did!
    letters = Counter(magazine)  # Count frequencies in magazine

    # For each character, c, in the ransom note:
    for c in ransomNote:       # Iterate over each character in note
        # If there are none of c left, return False.
        if letters[c] <= 0:    # If character unavailable
            return False       # Cannot construct note
        # Remove one of c from the Counter.
        letters[c] -= 1        # Decrement count for used character
                


    return True                # All characters available, can construct



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force 





# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Playground
"""
📘 Quick Tutorial: collections.Counter

Counter is a dictionary subclass for counting hashable objects.
It automatically tallies how many times each item appears.

Main use case: counting characters, words, or elements.
"""

from collections import Counter

# Example: Count letters in a word
word = "mississippi"
letter_counts = Counter(word)

print(letter_counts)
# Output:
# Counter({'i':4, 's':4, 'p':2, 'm':1})

# Example: Count words in a list
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_counts = Counter(words)

print(word_counts)
# Output:
# Counter({'apple':3, 'banana':2, 'orange':1})




# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Best Solution Using 'letters[c] == 0'
from collections import Counter
def canConstruct(ransomNote: str, magazine: str):
    letters = Counter(magazine)

    for c in ransomNote:
        letters[c] -= 1
        if letters[c] == 0:   # <-- only checking for == 0
            return False
    
    return True

# Example where this FAILS:
ransomNote = "aaa"   # needs 3 'a'
magazine   = "aa"    # only has 2 'a'
print(canConstruct(ransomNote, magazine))  
# Output False with == 0 check: True (WRONG!)

# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Best Solution Using 'letters[c] <= 0'
from collections import Counter
def canConstruct(ransomNote, magazine):

    if len(ransomNote) > len(magazine):
        return False
    letters = Counter(magazine)

    for c in ransomNote:
        if letters[c] <= 0:  # <-- checking for <= 0
            return False
        letters[c] -= 1
    return True

# Example where this FAILS
ransomNote = "aaa"   # needs 3 'a'
magazine   = "aa"    # only has 2 'a'
print(canConstruct(ransomNote, magazine))
# Output: False

"""
Overview for Each Iteration
Input: ransomNote = "aaa", magazine = "aa"
Step 1: Create Counter from magazine
letters = Counter({'a': 2})

Case 1: Using 'letters[c] == 0'
c  | letters[c] before | letters[c]-=1 | letters[c] after | letters[c] == 0? | Action
---|-------------------|---------------|------------------|------------------|---------------------------
a  | 2                 | subtract 1    | 1                | False            | continue
a  | 1                 | subtract 1    | 0                | True             | return False (correct stop)
a  | 0                 | subtract 1    | -1               | False            | BUG: missed failure
Final: False (Incorrectly returns True due to flawed == 0 check)

Simple Explanation for Beginners:
    - Goal: Check if `ransomNote` can be built using letters from `magazine`.
    - Process: Count each letter in `magazine` (e.g., "aa" has 2 'a's). For each letter in `ransomNote`, use one from the count.
    - Bug: The code checks `letters[c] == 0` after subtracting. It stops only when a letter's count hits exactly 0, missing cases where the count goes negative (e.g., needing 3 'a's but having only 2).
    - Issue: For `ransomNote = "aaa"`, `magazine = "aa"`, it stops correctly at the second 'a' (count = 0), but if it continued, it would allow negative counts and wrongly return `True`. 
    - Result: The `== 0` check makes the code unreliable for inputs requiring more letters than available.


Case 2: Using 'letters[c] <= 0'
c  | letters[c] before | letters[c]-=1 | letters[c] after | letters[c] <= 0? | Action
---|-------------------|---------------|------------------|------------------|---------------------------
a  | 2                 | subtract 1    | 1                | False            | continue
a  | 1                 | subtract 1    | 0                | True             | return False (correct stop)
a  | 0                 | subtract 1    | -1               | True             | return False (still safe)
Final: Returns False (CORRECT)

Simple Explanation for Beginners:
    - Goal: Check if `ransomNote` can be built using letters from `magazine`.
    - Process: Count each letter in `magazine` (e.g., "aa" has 2 'a's). For each letter in `ransomNote`, use one from the count.
    - Fix: The code checks `letters[c] <= 0` after subtracting, stopping if the count is 0 or negative (not enough letters).
    - Example: For `ransomNote = "aaa"`, `magazine = "aa"`, it stops at the second 'a' (count = 0), returning `False` because 3 'a's are needed but only 2 are available.
    - Result: The `<= 0` check ensures the code correctly handles all cases, returning `False` when there aren't enough letters.

"""






# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Alternate Solutions


# Approach 1: Simulation
    # Solution 2 and 3 are more optimized 

def canConstruct(ransomNote: str, magazine: str):
    # For each character, c,  in the ransom note.
    for c in ransomNote:
        # If there are none of c left in the String, return False.
        if c not in magazine:
            return False
        # Find the index of the first occurrence of c in the magazine.
        location = magazine.index(c)
        # Use splicing to make a new string with the characters 
        # before "location" (but not including), and the characters 
        #after "location". 
        magazine = magazine[:location] + magazine[location + 1:]
    # If we got this far, we can successfully build the note.
    return True


# Time Complexity : O(m⋅n)
# Space Complexity : O(m)



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Approach 2: Two HashMaps

def canConstruct(ransomNote: str, magazine: str):

    # Check for obvious fail case.
    if len(ransomNote) > len(magazine): return False

    # In Python, we can use the Counter class. It does all the work that the
    # makeCountsMap(...) function in our pseudocode did!
    magazine_counts = collections.Counter(magazine)
    ransom_note_counts = collections.Counter(ransomNote)
    
    # For each *unique* character in the ransom note:
    for char, count in ransom_note_counts.items():
        # Check that the count of char in the magazine is equal
        # or higher than the count in the ransom note.
        magazine_count = magazine_counts[char]
        if magazine_count < count:
            return False
            
    # If we got this far, we can successfully build the note.
    return True


# Time Complexity : O(m)
# Space Complexity : O(k) / O(1)



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Approach 3: One HashMap: SELECTED SOLUTION

def canConstruct(ransomNote: str, magazine: str):
    
    # Check for obvious fail case.
    if len(ransomNote) > len(magazine): 
        return False

    # In Python, we can use the Counter class. It does all the work that the makeCountsMap(...) function in our pseudocode did!
    letters = collections.Counter(magazine)
    
    # For each character, c, in the ransom note:
    for c in ransomNote:
        # If there are none of c left, return False.
        if letters[c] <= 0:
            return False
        # Remove one of c from the Counter.
        letters[c] -= 1
    # If we got this far, we can successfully build the note.
    return True


# Time Complexity : O(m)
# Space Complexity : O(k) / O(1)
