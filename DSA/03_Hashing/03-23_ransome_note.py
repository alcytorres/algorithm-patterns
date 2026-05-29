# 383. Ransom Note
"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
    Input: ransomNote = "a", magazine = "b"
    Output: false

Example 2:
    Input: ransomNote = "aa", magazine = "ab"
    Output: false

Example 3:
    Input: ransomNote = "aa", magazine = "aab"
    Output: true

Constraints:
    1 <= ransomNote.length, magazine.length <= 10^5
    ransomNote and magazine consist of only lowercase English letters.

Solution: https://leetcode.com/problems/ransom-note/solutions/540284/ransom-note/
"""


from collections import Counter

def canConstruct(ransomNote: str, magazine: str) -> bool:
    counter = Counter(magazine)

    for c in ransomNote:
        counter[c] -= 1
        if counter[c] < 0:
            return False

    return True


ransomNote = "aa"
magazine = "aab"
print(canConstruct(ransomNote, magazine))  # True

# magazine Counter = ({'a': 2, 'b': 1})
# magazine Counter = ({'a': 1, 'b': 1})
# magazine Counter = ({'b': 1})


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown

from collections import Counter

def canConstruct(ransomNote: str, magazine: str) -> bool:
    counter = Counter(magazine)   # Notebook: how many of each letter magazine has
    for c in ransomNote:          # Go through each letter we need to build
        counter[c] -= 1           # Use one copy of this letter from the notebook
        if counter[c] < 0:        # Went below zero — we didn't have enough
            return False          # Cannot build the note — stop early

    return True               # Every letter was covered — we can build it


"""
Time: O(M + R)
  - Let M = length of magazine, R = length of ransomNote.

  - Step 1: Build counter from magazine → O(M).
      • Counter(magazine) scans every letter in magazine once → O(M).
      • Each letter: look up and increment count in hash map → O(1).

  - Step 2: Scan ransomNote and spend letter counts → O(R).
      • Loop goes through every letter in ransomNote once → O(R).
      • Each step: subtract 1 from counter and check if negative → O(1).

  - Combined: O(M + R).
  - Overall: O(M + R).


Space: O(U) ≈ O(1)
  - U = how many different letters show up in magazine (e.g. "aab" → U = 2, only 'a' and 'b').
  - counter stores one count per different letter — not one slot per character in magazine.

  - Overall: O(U) — extra memory grows with different letters, not string length.
  - Worst case: U ≤ 26 (only lowercase English letters), so O(1).


Interview Answer: Worst Case

Time: O(M + R)
  - Scan magazine once (M letters), then scan ransomNote once (R letters).

Space: O(1)
  - Hash map stores at most 26 letter counts; no other structures grow with input size.


---
Overview for Each Iteration
Input: ransomNote = "aa", magazine = "aab"

Step 1: Build counter from magazine
i  | ch | counter
---|----|------------------
0  | a  | {a:1}
1  | a  | {a:2}
2  | b  | {a:2, b:1}

Step 2: Spend counts on ransomNote
i  | c  | counter[c] after -1 | < 0? | Action  | counter
---|----|---------------------|------|---------|-----------
0  | a  | 1                   | no   | continue| {a:1, b:1}
1  | a  | 0                   | no   | continue| {a:0, b:1}

Final: True — both 'a' letters were available in magazine


---
Overview for Each Iteration
Input: ransomNote = "aac", magazine = "aabc"

Step 1: Build counter from magazine
i  | ch | counter
---|----|----------------
0  | a  | {a:1}
1  | a  | {a:2}
2  | b  | {a:2, b:1}
3  | c  | {a:2, b:1, c:1}

Step 2: Spend counts on ransomNote
i  | c  | counter[c] after -1 | < 0? | Action  | counter
---|----|---------------------|------|---------|----------------
0  | a  | 1                   | no   | continue| {a:1, b:1, c:1}
1  | a  | 0                   | no   | continue| {a:0, b:1, c:1}
2  | c  | 0                   | no   | continue| {a:0, b:1, c:0}

Final: True — 'a', 'a', and 'c' were all available in magazine



---
Most IMPORTANT thing to Understand:
    • Can you spell ransomNote using letters from magazine — each magazine letter used at most once?

    • counter is a notebook: one number per letter type showing how many copies magazine has.

    • For each letter in ransomNote, spend one copy (subtract 1).

    • If any count goes below 0, magazine did not have enough of that letter → return False.


---
Why this code Works:
    • Counter role:
        • Counter(magazine) counts every letter in magazine once upfront.
        • Gives instant "how many of letter X do I have left?" lookups.

    • Spend-and-check loop:
        • counter[c] -= 1 uses one copy of letter c.
        • if counter[c] < 0 catches running out — even missing letters start at 0, so -1 means "needed one we didn't have."

    • Efficiency:
        • Brute force: for each ransom letter, search/remove from magazine → O(M × R).
        • Counter: count once, spend once → O(M + R).

    • Intuition:
        • Magazine is a box of letter tiles.
        • Count tiles first, then try to build ransomNote one letter at a time.
        • Go negative = you ran out of that tile.


---
TLDR:
    • Count magazine letters, subtract one per ransomNote letter, and return False the moment any count drops below zero.


---
Quick Example Walkthrough:
    ransomNote = "aa", magazine = "aab"

    Step 1: Build counter
        counter = {'a': 2, 'b': 1}

    Step 2: Spend counts on ransomNote
        c = 'a' → counter['a'] = 1 (still have 1 left)
        c = 'a' → counter['a'] = 0 (used both 'a's, still OK)

    Step 3: Loop finished without going negative
        return True

    Final Answer: True


---
Full Example Walkthrough:
    ransomNote = "aa", magazine = "aab"

    Starting State:
        counter = Counter("aab") → {'a': 2, 'b': 1}

    Loop Iteration 1:
        c = 'a'

        Spend one copy:
            counter['a'] -= 1 → counter['a'] = 1

        Check:
            counter['a'] < 0 → 1 < 0 → False → keep going

        Now:
            counter = {'a': 1, 'b': 1}

    --------------------------------------------------

    Loop Iteration 2:
        c = 'a'

        Spend one copy:
            counter['a'] -= 1 → counter['a'] = 0

        Check:
            counter['a'] < 0 → 0 < 0 → False → keep going

        Now:
            counter = {'a': 0, 'b': 1}

    --------------------------------------------------

    Final Check:
        Loop ended — no letter went negative.
        return True

        Meaning: magazine had enough 'a' copies to build "aa".



---
🧠 First Time? Thoughts → Code

Read the problem (10 sec)
    • Can ransomNote be built using letters from magazine?

    • Each magazine letter can only be used once — duplicates matter ("aa" needs two a's).

    • Only lowercase letters — hint that counting frequencies is enough.


Start naive (totally fine)
    • For each letter in ransomNote, search magazine for that letter and "cross it off."
    • Say out loud: "Do I have this letter? OK, use it."
    • Time: O(M × R) — each ransom letter may scan all of magazine.


The one insight that unlocks the optimal code
    • You need counts, not just "is this letter present?" — two a's means you need count ≥ 2.
    • Count all magazine letters once, then spend one count per ransomNote letter.
    • If any count drops below zero, you ran out — return False early.


Why a Counter / hash map?
    • A set only answers yes/no — fails on "aa" vs "a".
    • A hash map stores how many of each letter you still have left.
    • Counter(magazine) builds those counts in one line.


Thought → line of code
    counter = Counter(magazine)
        → "Tally every letter in magazine before I start spending."

    for c in ransomNote:
        → "Walk each letter I need to build, one at a time."

    counter[c] -= 1
        → "Use one copy of this letter from my tally."

    if counter[c] < 0:
        → "Went below zero — I needed a letter I didn't have."
        → "Trick: missing letters start at 0, so subtracting gives -1."


Memory hook (one sentence)
    • Count magazine tiles first, spend one per ransom letter, negative = can't build.


Would you arrive at this cold?
    • Immediately: loop ransomNote, check if each letter is in magazine.
    • After "aa" fails with a set: realize you need frequency counts, not just membership.
    • Bookkeeping: return True at end, return False early — instinct.
    • Real insight: count once + spend counts. The decrement-then-check-negative trick is the part you'd learn from practice.



"""





# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force — List + remove (cross off letters from a copy of magazine)

def canConstruct(ransomNote: str, magazine: str) -> bool:
    available = list(magazine)

    for c in ransomNote:
        if c not in available:
            return False
        available.remove(c)

    return True

ransomNote = "aa"
magazine = "aab"
print(canConstruct(ransomNote, magazine))  # True


"""
Time: O(M × R)
  - Let M = length of magazine, R = length of ransomNote.

  - Step 1: Copy magazine into a list → O(M).

  - Step 2: For each letter in ransomNote → O(R) iterations.
      • c not in available scans the list → O(M).
      • available.remove(c) finds and removes → O(M).

  - Combined: O(M + R × M).
  - Overall: O(M × R).


Space: O(M)
  - available list stores up to M magazine letters.
  - Overall: O(M).


Interview Answer: Worst Case

Time: O(M × R)
  - Each ransom letter may scan the full list to check and remove.

Space: O(M)
  - Mutable copy of magazine as a list.
"""



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Common Logic Bug — checking == 0 AFTER decrement

from collections import Counter

def canConstruct_bug(ransomNote: str, magazine: str) -> bool:
    letters = Counter(magazine)
    for c in ransomNote:
        letters[c] -= 1          # ❌ bug: check after decrement
        if letters[c] == 0:
            return False
    return True

# Fails: ransomNote = "aa", magazine = "aa" → returns False (expected True)
# Second 'a' correctly uses the last copy → count hits 0 → wrongly treated as failure.

"""
Why it fails:
    - Start: {'a': 2}
    - First 'a': subtract → {'a': 1} ✅
    - Second 'a': subtract → {'a': 0} — valid use of last copy
    - if letters[c] == 0: return False → false failure

Root cause:
    - Checking AFTER decrement treats "used the last one" the same as "ran out."

Two correct styles (same logic):
    1. Check first:  if letters[c] <= 0: return False  then  letters[c] -= 1
    2. Our solution: letters[c] -= 1  then  if letters[c] < 0: return False
       (0 is OK — only negative means you didn't have enough)
"""


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Alternate — Frequency array (26 lowercase letters)

def canConstruct_freq(ransomNote: str, magazine: str) -> bool:
    freq = [0] * 26

    for c in magazine:
        freq[ord(c) - ord('a')] += 1

    for c in ransomNote:
        idx = ord(c) - ord('a')
        if freq[idx] == 0:
            return False
        freq[idx] -= 1

    return True


# Same time/space as Counter solution — O(M + R) time, O(1) space (fixed 26 slots).
# Use when alphabet is fixed (lowercase a–z): array index replaces hash map lookup.



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
