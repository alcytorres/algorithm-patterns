# 383. Ransom Note

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Example:
    # Input: ransomNote = "a", magazine = "b"
    # Output: false


# Solution: https://leetcode.com/problems/ransom-note/solutions/540284/ransom-note/







# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown





# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force 






# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Alternate Solutions



# Approach 1: Simulation
    # Solution 2 and 3 are more optimized 

def canConstruct(self, ransomNote: str, magazine: str) -> bool:
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

def canConstruct(self, ransomNote: str, magazine: str) -> bool:

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
# Approach 3: One HashMap

def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    
    # Check for obvious fail case.
    if len(ransomNote) > len(magazine): return False

    # In Python, we can use the Counter class. It does all the work that the
    # makeCountsMap(...) function in our pseudocode did!
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


