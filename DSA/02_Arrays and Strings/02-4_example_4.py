# 392. Is Subsequence
"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

Assume the len(t) >= len(s) , and both are strings with valid characters.

Example 1:
    Input: s = "abc", t = "abcde"
    Output: True

Constraints:
    0 <= s.length <= 100
    0 <= t.length <= 104
    s and t consist only of lowercase English letters.

Solution: https://leetcode.com/problems/is-subsequence/
"""

# Solution: Two Pointers: Sequential Character Match
def is_subsequence(s, t):
    i = j = 0           

    while i < len(s) and j < len(t):
        if s[i] == t[j]:        
            i += 1
        j += 1                  

    return i == len(s)          

s = "ace"
t = "abcde"
print(is_subsequence(s, t))
# Output: True - "ace" appears in order within "abcde" as a subsequence.

# ––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def is_subsequence(s, t):
    i = j = 0            # Pointer for string s, and t starts at index 0

    while i < len(s) and j < len(t):  # Continue until s or t is exhausted
        if s[i] == t[j]:        # Match found, move s pointer
            i += 1
        j += 1                  # Always move t pointer

    return i == len(s)          # True if all characters in s were found. Same as saying return True


"""
Time: O(T)
  - Let S = length of s, T = length of t.
  - Two pointers (i for s, j for t) traverse both strings.
  - Each iteration advances j by 1 → total T iterations.
  - Pointer i only advances when characters match (≤ S times).
  - Overall: O(T).

Space: O(1)
  - Only uses a few integer variables (i, j).
  - No additional data structures are created.
  - Overall: O(1).

  
Interview Answer: Worst Case

Time: O(T)
  - Single pass through t while checking each character of s.

Space: O(1)
  - Constant extra memory (just two pointers).


---
Most IMPORTANT thing to Understand:
    • We need to check if every character in s appears in t in the same order.

    • The characters do NOT need to be next to each other.

    • Pointer i tracks where we are in s.

    • Pointer j tracks where we are in t.

    • If s[i] matches t[j], we found the next needed character, so we move i forward.

    • j always moves forward because we keep scanning through t.

---
Why this code Works:
    • Two pointers:
        • i = character we are trying to match in s.
        • j = character we are currently checking in t.

    • If s[i] == t[j]:
        • We found the next required character from s.
        • Move i forward to look for the next character.

    • If they do not match:
        • Only move j forward.
        • Keep searching through t.

    • Efficiency:
        • We scan each string once.
        • Time: O(n), where n is len(t).
        • Space: O(1).

    • Intuition:
        • Think of s as a checklist.
        • Think of t as a long sentence.
        • Every time you find the next checklist item in order, you check it off.

---
TLDR:
    • This solution works because it scans t from left to right and checks whether all characters in s can be found in order.

---
Full Example Walkthrough:
    s = "ace"
    t = "abcde"

    Starting State:
        i = 0
        j = 0

        i points at s[0] = "a"
        j points at t[0] = "a"

    Loop Iteration 1:
        Compare:
            s[i] == t[j]
            "a" == "a" → MATCH

        Since they match:
            i += 1

        Now:
            i = 1

        Then this line ALWAYS runs:
            j += 1

        Now:
            j = 1

        Current state:
            i points at s[1] = "c"
            j points at t[1] = "b"

    --------------------------------------------------

    Loop Iteration 2:
        Compare:
            "c" == "b" → NO MATCH

        Since there is NO match:
            i does NOT move

        But j ALWAYS moves:
            j += 1

        Now:
            i = 1
            j = 2

        Current state:
            i points at s[1] = "c"
            j points at t[2] = "c"

    --------------------------------------------------

    Loop Iteration 3:
        Compare:
            "c" == "c" → MATCH

        Since they match:
            i += 1

        Now:
            i = 2

        Then j ALWAYS moves:
            j += 1

        Now:
            j = 3

        Current state:
            i points at s[2] = "e"
            j points at t[3] = "d"

    --------------------------------------------------

    Loop Iteration 4:
        Compare:
            "e" == "d" → NO MATCH

        i stays the same.

        j moves:
            j += 1

        Now:
            i = 2
            j = 4

        Current state:
            i points at s[2] = "e"
            j points at t[4] = "e"

    --------------------------------------------------

    Loop Iteration 5:
        Compare:
            "e" == "e" → MATCH

        Move i:
            i += 1
            i = 3

        Move j:
            j += 1
            j = 5

    --------------------------------------------------

    Final Check:
        i == len(s)
        3 == 3 → True

        This means:
            We successfully matched ALL characters in s in order.


---
Overview for Each Iteration
Input: s = "ace", t = "abcde"

Step: Check if s is a subsequence of t
i | j | s[i] | t[j] | Match? | Action
- | - | -    | -    | -      | Initialize i=0, j=0
0 | 0 | a    | a    | Yes    | i+=1, j+=1 (i=1, j=1)
1 | 1 | c    | b    | No     | j+=1 (i=1, j=2)
1 | 2 | c    | c    | Yes    | i+=1, j+=1 (i=2, j=3)
2 | 3 | e    | d    | No     | j+=1 (i=2, j=4)
2 | 4 | e    | e    | Yes    | i+=1, j+=1 (i=3, j=5)

End: i=3, len(s)=3, return True



---------------------------------------------------
Q: Why do we use while i < len(s) and j < len(t):?
    • To make sure we never go out of range for either string.

    • We stop when we've checked all characters in s (success) or all in t (failure).

    • It's a safe condition that keeps both pointers within bounds.


Q: What if we already know len(t) >= len(s)?
    • Then while i < len(s) alone would technically work — because t will never run out before s.

    • But we still use and j < len(t) as good practice, in case that assumption changes.

    • It makes the function more robust and reusable.

"""





# ============================================
# Reading Loops + If Statements Correctly
# ============================================

# =========================================================
# The Common Beginner Mistake
# =========================================================

# Code:
while i < len(s) and j < len(t):

    if s[i] == t[j]:
        i += 1

    j += 1


# Common mistake:
#
# Thinking Python does this:
#
# 1. Check if condition
# 2. Run i += 1
# 3. Jump BACK to the if condition again
# 4. Then eventually run j += 1
#
# That is NOT what happens.


# =========================================================
# What Actually Happens
# =========================================================

# Python reads code TOP TO BOTTOM.
#
# Inside ONE loop iteration:
#
# 1. Check loop condition
# 2. Run code line-by-line downward
# 3. Reach bottom of loop body
# 4. THEN start next iteration


# =========================================================
# Important Insight
# =========================================================

# if statements are NOT loops.
#
# An if statement is only:
#
# "If this condition is true, run this block ONCE."
#
# Then Python continues downward normally.


# =========================================================
# The Actual Execution Order
# =========================================================

# Code:
while i < len(s) and j < len(t):

    if s[i] == t[j]:
        i += 1

    j += 1


# Real execution order:
#
# 1. Check while condition
# 2. Check if condition
# 3. If match:
#       run i += 1
# 4. Continue downward
# 5. Run j += 1
# 6. Reach bottom of loop
# 7. Start NEXT iteration


# =========================================================
# SUPER Important Detail
# =========================================================

# This line:

j += 1


# is OUTSIDE the if statement.
#
# That means it ALWAYS runs.


# Example:

if True:
    print("Inside if")

print("Always runs")


# Output:
# Inside if
# Always runs


# =========================================================
# Tiny Example
# =========================================================

i = 0

while i < 3:
    print("A")

    if i == 1:
        print("B")

    print("C")

    i += 1

# Output:
# A
# C
#
# A
# B
# C
#
# A
# C


# Important:
#
# After the if statement finishes,
# Python CONTINUES downward.
#
# It does NOT jump back upward.


# =========================================================
# Easy Mental Model
# =========================================================

# Think of ONE loop iteration like reading a page.
#
# Python starts at the top.
#
# It reads downward line-by-line.
#
# ONLY after reaching the bottom
# does the next iteration begin.


# =========================================================
# Beginner Strategy for Reading Loops
# =========================================================

# Step 1:
# Find the loop.
#
# for ...
# while ...
#
# Everything indented below repeats.


# Step 2:
# Ignore the fact that it loops.
#
# Read ONLY ONE iteration slowly
# from top to bottom.


# Step 3:
# Ask:
#
# What variables changed?
#
# Those updated values are what
# the NEXT iteration starts with.


# =========================================================
# Applying This to Is Subsequence
# =========================================================

# Code:

def is_subsequence(s, t):
    i = j = 0

    while i < len(s) and j < len(t):

        if s[i] == t[j]:
            i += 1

        j += 1

    return i == len(s)


# Key idea:
#
# i only moves when characters match.
#
# j ALWAYS moves.
#
# So:
#
# i = tracks progress through s
# j = scans through t


# This line:
#
#     j += 1
#
# being OUTSIDE the if statement
# is the entire trick.
#
# It means:
#
# "Keep scanning through t no matter what."
