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

# Solution 1: One Dictionary Frequency Check
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

# Count = {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1})

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
  - Maximum distinct keys = 26 → constant space (doesn't grow with N).
  - A few loop variables use O(1).
  - Overall: O(1) because of the "only a-z" constraint.

  If Unicode were allowed:
  - Space would be O(U), where U = number of unique characters.
  - Worst case: U ≈ N (if every char is different) → up to O(N) space.

  
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
Q: Why do we say this solution uses O(1) space 
   (even though we're using a dictionary / hashmap to count characters)?

A: The problem constraints limit us to ONLY 26 possible characters!

  • The rules say: "only lowercase English letters (a-z)".
  • That means just 26 possible characters.
  • No matter how long the strings are (even n = 5 million),
  your dictionary can have at MOST 26 keys.
  • 26 is a fixed number. It does NOT grow when the input (N) gets bigger.

  → Fixed small set of characters → max 26 entries → O(1) space! 👍

  
Follow-up question people ask: 
  • "What if the strings had Unicode characters (emoji, Chinese, symbols, etc.)?"

Answer for beginners:
  • Then there could be millions of different possible characters.

  • In the worst case, a long string could use a new character almost every time.

  • → The dictionary could grow as big as the string length (up to O(N) space).

  • But in LeetCode 242, we don't have to worry — it's only a-z, so O(1) is correct and safe.

Most interview / LeetCode problems like this limit to lowercase letters → so we happily say O(1) space. 😄




---
Q: Why is time O(N) with 2 loops instead of O(N + M)? 

A: Because in this problem, both strings are the same length whenever we actually run the loops!

  • If lengths differ → we return False immediately. No loops happen!

  • So the only time we do both loops is when N = M → N steps + N steps = 2N steps → O(2N) = O(N).



---
Q: What happens to time and space if we remove the length check?
   `if len(s) != len(t): return False`...?

A: Big-O stays O(N) either way, but the length check makes it faster in practice by skipping unnecessary work.

  • Without it, we'd always run both loops → still O(N) time (2N steps), but wasted effort when lengths differ.

  • Space stays O(1) — dict still has max 26 keys.

  Toy box example:
  Two toy boxes with the same toys?

  • Sizes different? Stop fast (like the length check — no counting needed).
  • Sizes same? Count every toy in both boxes → O(N) time.

Bottom line: 
The length check makes the code faster in real life when lengths mismatch, but Big-O time stays O(N) either way for this problem.


"""








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
FOLLOW-UP: What if inputs had Unicode characters (emoji, accents, Chinese, etc.)?

Key points:

1. Fixed 26-array solution (common in C++/Java):
   counts = [0] * 26
   counts[ord(c) - ord('a')] += 1
   → Breaks! Only works for a-z. Emoji or "é" causes crash (index error).

2. Your Python solutions (sorting or dictionary):
   - sorted(s) == sorted(t)
   - or count[c] += 1 / count[c] -= 1
   → Work perfectly with any Unicode — no changes needed!

Space difference:
  •  Only a-z → O(1) space (max 26 keys)
  • Full Unicode → O(k) space (k = number of different characters, worst case O(n) if all unique)

Takeaway:
  • Most Python solutions are Unicode-safe automatically.  

"""
