# 383. Ransom Note

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Example 1:
    # Input: ransomNote = "a", magazine = "b"
    # Output: false

# Example 2:
    # Input: ransomNote = "aa", magazine = "ab"
    # Output: false

# Example 3:
    # Input: ransomNote = "aa", magazine = "aab"
    # Output: true

# Solution: https://leetcode.com/problems/ransom-note/solutions/540284/ransom-note/


from collections import Counter

def canConstruct(ransomNote, magazine):
    
    # Check for obvious fail case.
    if len(ransomNote) > len(magazine):
        return False

    # Count frequency of each character in magazine
    letters = Counter(magazine)
    
    # For each character, c, in the ransom note:
    for c in ransomNote:
        # If there are none of c left, return False.
        if letters[c] == 0:
            return False
        # Remove one of c from the Counter.
        letters[c] -= 1
    # If we got this far, we can successfully build the note.
    return True

ransomNote = "aac"
magazine = "aabc"
print(canConstruct(ransomNote, magazine))
# Output: True → "aac" can be built from "aabc" (magazine has enough letters: 2 'a' and 1 'c', with 'b' unused).


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


---
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



---
Most IMPORTANT thing to Understand:
    We just need to check if magazine has at least as many of each letter as ransomNote needs.

    If any letter in ransomNote is missing or runs out in magazine, answer is False.

    A Counter (hash map) stores how many of each letter magazine provides; we decrement as we “use” letters.

---  
Why this code Works:
    • Data structure: Counter(magazine) holds counts for each letter so we can check availability in O(1) per letter.

    • Technique: Scan through each char in the ransom note once; if a letter's count in the magazine hits 0, return False — otherwise, decrement it to mark one used.

    • Efficiency: Build counts in O(M), check in O(N), with constant-time map operations → O(M + N) time, O(1) space (fixed alphabet).

    • Intuition: Like filling a shopping list from pantry stock—if any item hits zero before you finish, you can't complete the list.

---
TLDR:
    • Count letters in magazine and spend them while scanning ransomNote; if any needed letter is unavailable, return False, else True.

---
Quick Example Walkthrough:

    ransomNote = "aac", magazine = "aabc"

    Build counts: {'a':2, 'b':1, 'c':1}

    Use letters in order:

    need 'a' → have 2 → now {'a':1, 'b':1, 'c':1}
    need 'a' → have 1 → now {'a':0, 'b':1, 'c':1}
    need 'c' → have 1 → now {'a':0, 'b':1, 'c':0}

    No shortages occurred → True.


"""



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
from collections import Counter

def canConstruct(ransomNote, magazine):
    if len(ransomNote) > len(magazine): 
        return False  # Early exit if note longer than magazine

    # In Python, we can use the Counter class.

    # Count frequency of each character in magazine
    letters = Counter(magazine)  

    # For each character, c, in the ransom note:
    for c in ransomNote:       # Iterate over each character in note
        # If there are none of c left, return False.
        if letters[c] == 0:    # If character unavailable
            return False       # Cannot build note
        
        # Remove one of c from the Counter.
        letters[c] -= 1        # Decrement count for used character

    return True                # All characters available, can build




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
# Ransom Note — Common Logic Bug When Using Counters (Checking After Decrement)
# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
from collections import Counter

def canConstruct(ransomNote, magazine):
    letters = Counter(magazine)

    for c in ransomNote:
        letters[c] -= 1   # ❌ Bug: checking after decrement causes false failure when count hits zero
        if letters[c] == 0:   
            return False
    
    return True

# Example where this FAILS:
ransomNote = "aa"    # needs 2 'a'
magazine   = "aa"    # has 2 'a'
print(canConstruct(ransomNote, magazine))  
# Output


"""
❌ Why the Original Code Fails

Example
    ransomNote = "aa"
    magazine   = "aa"

    Expected: True  
    Actual:   False

---
Step-by-Step Explanation
    - Start: letters = {'a': 2}
    - First 'a': subtract 1 → {'a': 1} ✅ still fine
    - Second 'a': subtract 1 → {'a': 0} ⚠️ hits zero  
    - The code said:
        if letters[c] == 0: return False
    → so it returned False even though we used the last available 'a' correctly.

---
Root Cause
  • The condition was checked AFTER decrementing, so the last valid letter triggered a false failure.
  • It should instead check BEFORE subtracting — confirm availability first, then use one.

---
✅ Correct Fix
    Move the check BEFORE decrementing:
    if counts[c] == 0:
        return False
    counts[c] -= 1


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