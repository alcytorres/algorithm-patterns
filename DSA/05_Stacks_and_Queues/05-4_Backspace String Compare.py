# 844. Backspace String Compare

# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

# Solution: https://leetcode.com/problems/backspace-string-compare/description/

# Example 1:
    # Input: s = "ab#c", t = "ad#c"
    # Output: true
    # Explanation: Both s and t become "ac".

# Example 2:
    # Input: s = "ab##", t = "c#d#"
    # Output: true
    # Explanation: Both s and t become "".

# Example 3:
    # Input: s = "a#c", t = "b"
    # Output: false
    # Explanation: s becomes "c" while t becomes "b".


def backspaceCompare(s, t):
    def build(s):
        stack = []

        for c in s:
            if c != "#":
                stack.append(c)
            elif stack:
                stack.pop()

        return "".join(stack)

    return build(s) == build(t)


s = "ab#c"; t = "ad#c"
print(backspaceCompare(s, t))  # Output: True 

s = "ab##"; t = "c#d#"
print(backspaceCompare(s, t))  # Output: True 

s = "a#c"; t = "b"
print(backspaceCompare(s, t))  # Output: False

s = "a"; t = "#"
print(backspaceCompare(s, t))  # Output: False

s = "a"; t = "#a"
print(backspaceCompare(s, t))  # Output: True



"""
Time: O(N + M)
  - Let N = length of string s, and M = length of string t.
  - Each string is processed once to simulate backspaces using a stack.
      • Each character is pushed or popped at most once → O(N) and O(M).
  - Final comparison of the two built strings takes O(max(N, M)).
  - Overall: O(N + M).

Space: O(N + M)
  - Two stacks (one for s and one for t) store characters that remain after backspacing.
  - In the worst case (no '#'), each stack holds all characters → O(N + M).
  - A few loop variables and helper function overhead → O(1).
  - Overall: O(N + M).

  
Interview Answer: Worst Case

Time: O(N + M)
  - Each character in both strings is processed once.

Space: O(N + M)
  - Stacks store remaining characters after processing.



---
Overview for Each Iteration
Input: s = "ab#c", t = "ad#c"

Step: Process s = "ab#c"
c   | c != '#' | stack (before) | Action         | stack (after)
----|----------|----------------|----------------|---------------
a   | True     | []             | append         | ['a']
b   | True     | ['a']          | append         | ['a', 'b']
#   | False    | ['a', 'b']     | pop            | ['a']
c   | True     | ['a']          | append         | ['a', 'c']
Result s: "ac"

Step: Process t = "ad#c"
c   | c != '#' | stack (before) | Action         | stack (after)
----|----------|----------------|----------------|---------------
a   | True     | []             | append         | ['a']
d   | True     | ['a']          | append         | ['a', 'd']
#   | False    | ['a', 'd']     | pop            | ['a']
c   | True     | ['a']          | append         | ['a', 'c']
Result t: "ac"

Final: "ac" == "ac" → return True


---
Overview for Each Iteration
Input: s = "ab##", t = "c#d#"

Step: Process s = "ab##"
c   | c != '#' | stack (before) | Action         | stack (after)
----|----------|----------------|----------------|---------------
a   | True     | []             | append         | ['a']
b   | True     | ['a']          | append         | ['a', 'b']
#   | False    | ['a', 'b']     | pop            | ['a']
#   | False    | ['a']          | pop            | []
Result s: ""

Step: Process t = "c#d#"
c   | c != '#' | stack (before) | Action         | stack (after)
----|----------|----------------|----------------|---------------
c   | True     | []             | append         | ['c']
#   | False    | ['c']          | pop            | []
d   | True     | []             | append         | ['d']
#   | False    | ['d']          | pop            | []
Result t: ""

Final: "" == "" → return True


---
Overview for Each Iteration
Input: s = "a#c", t = "b"

Step: Process s = "a#c"
c   | c != '#' | stack (before) | Action         | stack (after)
----|----------|----------------|----------------|---------------
a   | True     | []             | append         | ['a']
#   | False    | ['a']          | pop            | []
c   | True     | []             | append         | ['c']
Result s: "c"

Step: Process t = "b"
c   | c != '#' | stack (before) | Action         | stack (after)
----|----------|----------------|----------------|---------------
b   | True     | []             | append         | ['b']
Result t: "b"

Final: "c" == "b" → return False


---
Overview for Each Iteration
Input: s = "a", t = "#"

Step: Process s = "a"
c   | c != '#' | stack (before) | Action         | stack (after)
----|----------|----------------|----------------|---------------
a   | True     | []             | append         | ['a']
Result s: "a"

Step: Process t = "#"
c   | c != '#' | stack (before) | Action         | stack (after)
----|----------|----------------|----------------|---------------
#   | False    | []             | elif stack → False (empty) → skip | []
Result t: ""

Final: "a" == "" → return False


---
Overview for Each Iteration
Input: s = "a", t = "#a"

Step: Process s = "a"
c   | c != '#' | stack (before) | Action         | stack (after)
----|----------|----------------|----------------|---------------
a   | True     | []             | append         | ['a']
Result s: "a"

Step: Process t = "#a"
c   | c != '#' | stack (before) | Action         | stack (after)
----|----------|----------------|----------------|---------------
#   | False    | []             | elif stack → False (empty) → skip | []
a   | True     | []             | append         | ['a']
Result t: "a"

Final: "a" == "a" → return True





---
Most IMPORTANT thing to Understand:
    • The '#' acts like a backspace — it deletes the most recent character (if any).

    • A stack perfectly models typing and backspacing: push letters when typed, pop when '#' appears.

    • The final result is the stack's contents after processing the whole string.

---
Why this code Works:
    • Data structure: stack simulates a text editor's behavior.

    • Technique: For each char in the string:
        - If not '#', push onto stack.
        - If '#', pop one (if available).

    • After building both strings (s and t), compare the joined results.

    • Efficiency: O(N + M) time, O(N + M) space; both strings processed independently.

    • Intuition: Like typing each string into a real text editor and comparing the screens at the end.

---
TLDR:
    • Build both strings using a stack to simulate typing and backspacing, then compare the final results.

---
Quick Example Walkthroughs:

Example 1: s = "ab#c", t = "ad#c"
--------------------------------
    s → ['a','b'] → '#' removes 'b' → ['a'] → add 'c' → ['a','c'] → "ac"
    t → ['a','d'] → '#' removes 'd' → ['a'] → add 'c' → ['a','c'] → "ac"
    Compare: "ac" == "ac" ✅ → True


Example 2: s = "ab##", t = "c#d#"
--------------------------------
    s → ['a','b'] → '#' removes 'b' → ['a'] → '#' removes 'a' → [] → ""
    t → ['c'] → '#' removes 'c' → [] → add 'd' → ['d'] → '#' removes 'd' → [] → ""
    Compare: "" == "" ✅ → True


Example 3: s = "a#c", t = "b"
--------------------------------
    s → ['a'] → '#' removes 'a' → [] → add 'c' → ['c'] → "c"
    t → ['b'] → "b"
    Compare: "c" != "b" ❌ → False


---
Example 1: s = "ab#c", t = "ad#c"

s processing (build(s)):
------------------------
    Start: stack = []
    1) 'a'  → not '#' → push → stack = ['a']
    2) 'b'  → not '#' → push → stack = ['a','b']
    3) '#'  → is '#'  → pop  → stack = ['a']
    4) 'c'  → not '#' → push → stack = ['a','c']
    Result(s) = "ac"

t processing (build(t)):
------------------------
    Start: stack = []
    1) 'a'  → not '#' → push → stack = ['a']
    2) 'd'  → not '#' → push → stack = ['a','d']
    3) '#'  → is '#'  → pop  → stack = ['a']
    4) 'c'  → not '#' → push → stack = ['a','c']
    Result(t) = "ac"

Compare:
--------
"ac" == "ac" → True ✅





---
Q: Why do we use `elif stack:` instead of just `elif:` ?
    • ✅ `elif stack:` checks if the stack is NOT empty before popping.

    • If we wrote only `elif:`, it would always try to run, even when stack is empty.

    • That would cause an error (can't pop from an empty list).

    • So `elif stack:` makes sure there's at least one character to remove.

    • In short: it prevents crashes when a '#' appears at the start.

    

---
Q: Why is it `elif` instead of `else`?

  - Because we only want to pop when both are true:
    1. The character is '#'
    2. The stack is not empty

  - If we used `else`, it would run for every '#', even when the stack is empty → causes an error.

  Example:
    s = "#" → stack empty
    - `if c != "#"` → False
    - `else:` → would try to pop → ❌ error
    - `elif stack:` → safely skips since stack is empty ✅

  In short:  
  `elif stack:` = “only pop when we actually have something to remove.”



"""


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def backspaceCompare(s, t):
    def build(s):                     # Helper to process backspaces
        stack = []                    # Stack to simulate typing

        for c in s:                   # Iterate over each character
            if c != "#":              # If not backspace
                stack.append(c)       # Add character
            elif stack:               # If backspace and stack not empty
                stack.pop()           # Remove last character

        return "".join(stack)         # Convert stack to final string
    
    return build(s) == build(t)       # Compare processed strings





# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Playground 

# How Nested Functions Work – Visual flow of execution

# Example: a = 3, b = 3 → Output = True (because 3*2 == 3*2 → 6 == 6)
# ---------------------------------------------
def compareNumbers(a, b):
    def double(n):
        return n * 2

    return double(a) == double(b)

print(compareNumbers(3, 3))  # True

"""
Step order (what happens in order):
 
  1 define compareNumbers  → nothing runs yet
  2 print(compareNumbers(3, 3)) → calls compareNumbers(a=3, b=3)
  3 inside compareNumbers → define double(n)
  4 run: double(a) == double(b)
      ↳ double(3) → returns 6
      ↳ double(3) → returns 6
  5 compare 6 == 6 → True
  6 return True → print(True)

Output: True ✅ 

"""