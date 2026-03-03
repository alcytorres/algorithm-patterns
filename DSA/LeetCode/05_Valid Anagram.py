# 242. Valid Anagram
"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
 
Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:
    Input: s = "rat", t = "car"
    Output: false

Constraints:
    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all original letters exactly once. 
    
Solution: https://leetcode.com/problems/valid-anagram/description/?envType=problem-list-v2&envId=oizxjoit

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
    • My python solutions already support Unicode because sorting and dictionaries work with all Unicode characters.

    • No code changes are required for the follow-up in Python.

    • The follow-up mainly targets Java/C++ solutions that use fixed 26-length arrays, which break for Unicode.    
"""

# Option 1: One Dictionary Frequency Check
from collections import defaultdict

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    count = defaultdict(int)
    for c in s:
        count[c] += 1

    for c in t:
        count[c] -= 1
        if count[c] < 0:
            return False
    return True

s = "anagram"
t = "nagaram"
print(isAnagram(s, t))  # Output: True

# {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1})

# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
from collections import defaultdict

def isAnagram(s, t):
    if len(s) != len(t):      # If lengths differ → can't be anagram
        return False          # Early exit
    
    count = defaultdict(int)  # Dictionary: char → frequency in s
    
    # Step 1: Count characters in string s
    for c in s:               # Go through each char in s
        count[c] += 1         # Increase count for this character
    
    # Step 2: Decrease counts using string t
    for c in t:               # Go through each char in t
        count[c] -= 1         # Use up one occurrence of this char
        
        if count[c] < 0:     # If we used more than we had
            return False     # t has extra char → not anagram
    
    return True              # All counts zero → perfect anagram!



"""
Time: O(N)
  - Let N = length of the strings (they must be equal length to be anagrams).
  - Step 1: Count characters in s → O(N).
  - Step 2: Subtract counts while scanning t → O(N).
      • If any count becomes negative, return early.
  - No sorting or nested loops.
  - Overall: O(N).

Space: O(1)
  - count dictionary stores frequencies of lowercase English letters.
  - Maximum distinct keys = 26 → constant space.
  - A few loop variables use O(1).
  - Overall: O(1) if input is restricted to lowercase English.
  - If Unicode letters allowed, space becomes O(U), where U = number of unique characters.

  
Interview Answer: Worst Case

Time: O(N)
  - Build counts from s, subtract using t.

Space: O(1) for lowercase English letters
  - Hash map holds at most 26 keys.



---
Overview for Each Iteration
Input: s = "anagram", t = "nagaram"

Step 1: Build frequency map from s
c | count[c] before | Action | count after
--|-----------------|--------|----------------------------
a | 0 → 1           | +1     | {'a':1}
n | 0 → 1           | +1     | {'a':1,'n':1}
a | 1 → 2           | +1     | {'a':2,'n':1}
g | 0 → 1           | +1     | {'a':2,'n':1,'g':1}
r | 0 → 1           | +1     | {'a':2,'n':1,'g':1,'r':1}
a | 2 → 3           | +1     | {'a':3,'n':1,'g':1,'r':1}
m | 0 → 1           | +1     | {'a':3,'n':1,'g':1,'r':1,'m':1}

Step 2: Subtract using t
c | count[c] before | Action | count after | <0? | Result
--|-----------------|--------|-------------|-----|----------
n | 1 → 0           | -1     | ...'n':0    | No  | continue
a | 3 → 2           | -1     | ...'a':2    | No  | continue
g | 1 → 0           | -1     | ...'g':0    | No  | continue
a | 2 → 1           | -1     | ...'a':1    | No  | continue
r | 1 → 0           | -1     | ...'r':0    | No  | continue
a | 1 → 0           | -1     | ...'a':0    | No  | continue
m | 1 → 0           | -1     | ...'m':0    | No  | continue

All counts ≥ 0 → return True


---
Overview for Each Iteration
Input: s = "rat", t = "car"

Step 1: Build frequency map from s
count after s: {'r':1, 'a':1, 't':1}

Step 2: Subtract using t
c | count before | Action | count after | <0? | Result
--|--------------|--------|-------------|-----|--------
c | 0            | -1     | -1          | Yes | → return False

Final: False



---
Most IMPORTANT thing to Understand:
    • An anagram means both strings must use the exact same characters the exact same number of times.

    • We count how many times each character appears in s, then subtract those counts while scanning t.

    • If any character in t causes the count to go negative, the strings cannot be anagrams.

---
Why this code Works:
    • Hash map role: count[c] tracks how many of each character we still “expect” to see.

    • Technique: Add +1 for each char in s, then -1 for each char in t; all counts must end at zero.

    • Efficiency: One pass to build counts, one pass to reduce them → O(N), no sorting required.

    • Intuition: Think of it like checking out items at a store — s “stocks the shelves,” t “removes them.”  
      If you try to remove something that's not there → not an anagram.

---
TLDR:
    • Count characters from s, subtract using t, and if no count goes negative, the words are anagrams.

---
Quick Example Walkthrough:

    s = "anagram"
    t = "nagaram"

    Step 1 — Build counts from s:
        {'a':3, 'n':1, 'g':1, 'r':1, 'm':1}

    Step 2 — Process t:
        'n' → count becomes 0
        'a' → 3 → 2
        'g' → 1 → 0
        'a' → 2 → 1
        'r' → 1 → 0
        'a' → 1 → 0
        'm' → 1 → 0

    No negative counts → valid anagram.

    Final Output: True

    


---
Q: Why is the time complexity O(N) instead of O(N + M) even though there are two loops?

------------------------------------------------------------
1. Inside THIS LeetCode problem ("Valid Anagram")
------------------------------------------------------------
  • The algorithm only runs both loops when s and t have the same length.
  • If lengths differ, the function returns immediately and does NOT run the loops.
  • So in the only case that matters for Big-O, we have N = M.
  • The loops then run N times each → O(N + N) → O(2N) → O(N).

→ For this problem: O(N), because the full work only happens when lengths match.


------------------------------------------------------------
2. Outside this problem (general case, no length check)
------------------------------------------------------------
  • If the early length check were removed, both loops would always run.

      if len(s) != len(t):
        return False

  • Then the true time would be O(N + M), since you'd scan both strings fully.

→ General case: O(N + M).  
→ LeetCode problem: O(N), because the mismatch case exits early.




---
Q: Why do we say this solution uses O(1) space 
   (even though we're using a dictionary / hashmap to count characters)?

A: Because of the problem rules!

  • The constraints say: only lowercase English letters (a-z).
  • That means just 26 possible characters — ever.
  • No matter how long the strings are (even n = 50,000 or 5 million),
  your dictionary can have **at most 26 keys**.
  • 26 is a fixed number. It does **not** grow when the input (n) gets bigger.

  → Fixed small set of characters → max 26 entries → O(1) space! (super efficient) 👍

  
Follow-up question people ask: 
  • "What if the strings had Unicode characters (emoji, Chinese, symbols, etc.)?"

Answer for beginners:
  • Then there could be millions of different possible characters.

  • In the worst case, a long string could use a new character almost every time.

  • → The dictionary could grow as big as the string length (up to O(n) space).

  • But in LeetCode 242, we don't have to worry — it's only a-z, so O(1) is correct and safe.

Most interview / LeetCode problems like this limit to lowercase letters → so we happily say O(1) space. 😄



---
Q: What limits this to lowercase English letters (not Unicode)?

A: The problem constraints — not the code.

  • "s and t consist of lowercase English letters" (only a-z, 26 chars).
  • Dict max 26 keys → O(1) space guaranteed.
  • Code handles Unicode fine, but inputs won't have it.

(Full Unicode → could be O(n) worst-case.)






Q: What happens to time and space complexity if we remove 
   the line: if len(s) != len(t): return False

A: Time stays O(n), space stays O(1).

Time complexity:
- Still O(n): We loop through both strings once (2n steps total).
- We just do a tiny bit more unnecessary work when lengths differ 
  (count all of s, then subtract t and eventually find negatives or leftover positives).

Space complexity:
- Still O(1): Dict max 26 keys (only a-z allowed by constraints).
- Removing the length check doesn't change how many keys we store.
Bottom line: Removing it makes the code slightly slower in worst case 
(when lengths differ), but big-O remains exactly the same: O(n) time, O(1) space.


"""




# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Sorting-Based Anagram Check 
def isAnagram(s, t):
    # If lengths are different → impossible to be anagram
    if len(s) != len(t):
        return False
    
    # Count how many times each letter appears in both strings
    # and compare the counts
    return sorted(s) == sorted(t)

s = "anagram"
t = "nagaram"
print(isAnagram(s, t))  # Output: True

# Time: O(n log n)
# Space: O(n)


# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Counter-Based Solution
from collections import Counter

def isAnagram(s, t):
    # 1. Essential Length Check
    if len(s) != len(t):
        return False
    
    # 2. Create frequency counts for both strings
    # Counter does the entire counting loop for you
    s_counts = Counter(s)
    t_counts = Counter(t)
    
    # 3. Compare the two Counter objects
    # This checks if every character key has the exact same count value
    return s_counts == t_counts

s = "anagram"
t = "nagaram"
print(isAnagram(s, t))  # Output: True

# Time: O(n)
# Space: O(1)


# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Two-Dictionary Comparison
def isAnagram(s, t):
    # If lengths differ, they can't be anagrams
    if len(s) != len(t):
        return False

    # Dictionary to count letters in s
    count_s = {}
    for c in s:
        if c in count_s:
            count_s[c] += 1
        else:
            count_s[c] = 1

    # Dictionary to count letters in t
    count_t = {}
    for c in t:
        if c in count_t:
            count_t[c] += 1
        else:
            count_t[c] = 1

    # Compare both dictionaries
    return count_s == count_t

# Time: O(n)
# Space: O(1)








# ============================================================
# 26-Letter Array – Works only for a-z, crashes on Unicode"
# ============================================================
def isAnagram(s, t):
    if len(s) != len(t):
        return False

    counts = [0] * 26  # assumes only lowercase English letters

    for c in s:
        counts[ord(c) - ord('a')] += 1

    for c in t:
        counts[ord(c) - ord('a')] -= 1
        if counts[ord(c) - ord('a')] < 0:
            return False

    return True

s = "resume"
t = "résumé"
print(isAnagram(s, t))  # Output: IndexError: list index out of range

# ============================================================
# Valid Anagram — Follow-Up Summary
# ============================================================
"""
FOLLOW-UP: What if the inputs contain Unicode characters?

Key Issue:
    Some solutions assume the alphabet is ONLY 'a'-'z'.  
    These break when Unicode characters are allowed.

------------------------------------------------------------
1. ASCII-Only Solution (NOT Unicode-Safe)
------------------------------------------------------------
A common approach in C++/Java:

    counts = [0] * 26
    for c in s:
        counts[ord(c) - ord('a')] += 1
    for c in t:
        counts[ord(c) - ord('a')] -= 1
        if counts[ord(c) - ord('a')] < 0:
            return False

Why it fails:
    - Only works for 26 lowercase English letters.
    - Unicode has thousands of characters (é, Ü, 你, 🙂, etc.).
    - Cannot map all Unicode characters into [0..25].

Space:
    - O(1) only because alphabet is fixed size 26.

------------------------------------------------------------
2. Sorting and Dictionary Solutions (Unicode-Safe)
------------------------------------------------------------
Your Python solutions:

    sorted(s) == sorted(t)
    OR
    count[c] += 1 / count[c] -= 1

Why they work automatically:
    - Python strings and sorting fully support Unicode.
    - Dictionaries can use any Unicode character as a key.

Space Impact:
    - For ASCII-only: O(1) space (max 26 letters).
    - For Unicode: O(k) space, where k = number of distinct characters.

------------------------------------------------------------
THE KEY TAKEAWAY
------------------------------------------------------------
The only solution that *doesn't* work for Unicode is the fixed 26-length array version.

Your sorting and dictionary solutions already handle Unicode without any code changes — only the space complexity changes from O(1) to O(k).

"""
