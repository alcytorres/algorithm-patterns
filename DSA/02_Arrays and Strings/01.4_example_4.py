# Check if String s is a Subsequence of String t
# Example 4: Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

def is_subsequence(s, t):
    i = j = 0           

    while i < len(s) and j < len(t):
        if s[i] == t[j]:        
            i += 1
        j += 1                  

    return i == len(s)          

string1 = "ace"
string2 = "abcde"
print(is_subsequence(string1, string2))
# Output: True - "ace" appears in order within "abcde" as a subsequence.


# Time: O(n + m) - Scans string t (length m) once while checking for characters of s (length n), with O(1) comparisons per iteration.
# Space: O(1) - Uses only two integer pointers (i, j) for tracking positions in s and t.


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def is_subsequence(s, t):
    i = j = 0            # Pointer for string s, and t starts at index 0

    while i < len(s) and j < len(t):  # Continue until s or t is exhausted
        if s[i] == t[j]:        # Match found, move s pointer
            i += 1
        j += 1                  # Always move t pointer

    return i == len(s)          # True if all characters in s were found



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Task: Check if string s is a subsequence of string t (characters of s appear in order in t).
# Example: s = "ace", t = "abcde" → Output = True (s appears in order within t)
# Why: Practices two-pointer technique to efficiently check for subsequence.

def is_subsequence(s, t):  # Example: s = "ace", t = "abcde"

    # 1️⃣ Initialize pointers
    # Initialize pointer i for string s
    # Why? Tracks the current character in s we need to find in t
    i = 0  # i = 0

    # Initialize pointer j for string t
    # Why? Scans through t to find characters matching s
    j = 0  # j = 0

    # 2️⃣ Iterate while both pointers are within bounds
    # Continue while we haven't reached the end of s or t
    # Why? We need to check all characters of s against t
    while i < len(s) and j < len(t):  # i = 0, len(s) = 3, j = 0, len(t) = 5
        # --- Iteration 1 ---
        # Check if current characters match
        # Why? If they match, we advance in s to look for the next character
        if s[i] == t[j]:  # s[0] = 'a', t[0] = 'a', 'a' == 'a' is true
            i += 1  # i = 0 + 1 = 1
        # Always advance j to check the next character in t
        # Why? We must scan through all of t to find s's characters in order
        j += 1  # j = 0 + 1 = 1
        # After Iteration 1: i = 1, j = 1
        # Current chars: s[1] = 'c', t[1] = 'b'

        # --- Iteration 2 ---
        if i == 1 and j == 1:
            if s[i] == t[j]:  # s[1] = 'c', t[1] = 'b', 'c' == 'b' is false
                i += 1  # skip
            j += 1  # j = 1 + 1 = 2
            # After Iteration 2: i = 1, j = 2
            # Current chars: s[1] = 'c', t[2] = 'c'

        # --- Iteration 3 ---
        if i == 1 and j == 2:
            if s[i] == t[j]:  # s[1] = 'c', t[2] = 'c', 'c' == 'c' is true
                i += 1  # i = 1 + 1 = 2
            j += 1  # j = 2 + 1 = 3
            # After Iteration 3: i = 2, j = 3
            # Current chars: s[2] = 'e', t[3] = 'd'

        # --- Iteration 4 ---
        if i == 2 and j == 3:
            if s[i] == t[j]:  # s[2] = 'e', t[3] = 'd', 'e' == 'd' is false
                i += 1  # skip
            j += 1  # j = 3 + 1 = 4
            # After Iteration 4: i = 2, j = 4
            # Current chars: s[2] = 'e', t[4] = 'e'

        # --- Iteration 5 ---
        if i == 2 and j == 4:
            if s[i] == t[j]:  # s[2] = 'e', t[4] = 'e', 'e' == 'e' is true
                i += 1  # i = 2 + 1 = 3
            j += 1  # j = 4 + 1 = 5
            # After Iteration 5: i = 3, j = 5
            # Loop exits: i = 3, len(s) = 3, condition i < len(s) is false

    # 3️⃣ Check if all characters of s were found
    # Return True if i reached the end of s, False otherwise
    # Why? If i == len(s), all characters of s were found in order in t
    return i == len(s)  # i = 3, len(s) = 3, 3 == 3 is True


string1 = "ace"
string2 = "abcde"
print(is_subsequence(string1, string2)) 
# Output: True - "ace" appears in order within "abcde" as a subsequence.
