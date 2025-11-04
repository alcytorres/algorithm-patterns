# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
    # 1. Open brackets must be closed by the same type of brackets.
    # 2. Open brackets must be closed in the correct order.
    # 3. Every close bracket has a corresponding open bracket of the same type.

# Solution: https://leetcode.com/problems/valid-parentheses/description/

# Example 1:
    # Input: s = "()"
    # Output: true

# Example 2:
    # Input: s = "()[]{}"
    # Output: true

# Example 3:
    # Input: s = "(]"
    # Output: false

# Example 4:
    # Input: s = "([])"
    # Output: true

# Example 5:
    # Input: s = "([)]"
    # Output: false

def isValid(s):
    stack = []
    matching = {"(": ")", "[": "]", "{": "}"}
    
    for c in s:
        if c in matching: # if c is an opening bracket
            stack.append(c)
        else:
            if not stack:
                return False
            
            last_open = stack.pop()
            if matching[last_open] != c:
                return False

    return not stack

s = "()"
print(isValid(s))  # Output: True

s = "(["
print(isValid(s))  # Output: False

s = "([])"
print(isValid(s))  # Output: True

s = "([)"
print(isValid(s))  # Output: False

s = "()[]{}"
print(isValid(s))  # Output: True


"""
Time: O(N)
  - Let N = length of string s.
  - Each character is processed exactly once.
      • Opening brackets are pushed onto the stack → O(1) per operation.
      • Closing brackets cause at most one pop and comparison → O(1) per operation.
  - Overall: O(N).

Space: O(N)
  - Stack stores unmatched opening brackets.
  - In the worst case (all opening brackets), stack size grows to N.
  - Dictionary 'matching' is constant-sized → O(1).
  - Overall: O(N).

  
Interview Answer: Worst Case

Time: O(N)
  - Single pass, each character pushed or popped once.

Space: O(N)
  - Stack holds up to all opening brackets.



---
Overview for Each Iteration
Input: s = "()"

Step: Validate parentheses using stack
c   | c in matching | stack          | Action
----|---------------|----------------|------------------
(   | True          | []             | stack.append('(') → ['(']
)   | False         | ['(']          | pop '(', matching['('] = ')', c = ')', match → continue

Final: stack = [], return True


---
Overview for Each Iteration
Input: s = "([])"

Step: Validate parentheses using stack
c   | c in matching | stack          | Action
----|---------------|----------------|------------------
(   | True          | []             | stack.append('(') → ['(']
[   | True          | ['(']          | stack.append('[') → ['(', '[']
]   | False         | ['(', '[']     | pop '[', matching['['] = ']', c = ']', match → ['(']
)   | False         | ['(']          | pop '(', matching['('] = ')', c = ')', match → []

Final: stack = [], return True


---
Overview for Each Iteration
Input: s = "(["

Step: Validate parentheses using stack
c   | c in matching | stack          | Action
----|---------------|----------------|------------------
(   | True          | []             | stack.append('(') → ['(']
[   | True          | ['(']          | stack.append('[') → ['(', '[']

Final: stack = ['(', '['], return False (not empty)


---
Overview for Each Iteration
Input: s = "([)"

Step: Validate parentheses using stack
c   | c in matching | stack          | Action
----|---------------|----------------|------------------
(   | True          | []             | stack.append('(') → ['(']
[   | True          | ['(']          | stack.append('[') → ['(', '[']
)   | False         | ['(', '[']     | pop '[', matching['['] = ']', c = ')', no match → return False

Final: False




Most IMPORTANT thing to Understand:
    • We use a stack to keep track of open brackets — each closing bracket must match the last unclosed opening one.

    • The order matters: the most recent open bracket must be closed first (LIFO → Last In, First Out).

    • A string is valid only if all opens are properly closed and no unmatched brackets remain at the end.

---
Why this code Works:
    • Data structure: stack keeps track of unclosed brackets.

    • Process:
        - When we see an opening bracket, push it on the stack.
        - When we see a closing bracket, pop from stack and check if it matches the correct type.
        - If mismatch or stack is empty → invalid.

    • Final check (`return not stack`): ensures no unmatched opening brackets are left.

    • Efficiency: O(N) time (each char visited once), O(N) space (worst case — all opens).

    • Intuition: Like checking nested boxes — each new box opened must be the next one closed.

---
TLDR (one sentence):
    • Use a stack to push open brackets and ensure each close matches the most recent open; valid if stack is empty at the end.

---
Quick Example Walkthroughs:

Example 1: s = "()"
--------------------------------
    stack = []
    '(' → open → push → ['(']
    ')' → close → pop '(' → matches ✓
    End: stack = [] → valid ✅

    Output: True


Example 2: s = "(]"
--------------------------------
    stack = []
    '(' → push ['(']
    ']' → close → pop '(' → mismatch ✗
    Return False immediately ❌

    Output: False


Example 3: s = "([])"
--------------------------------
    stack = []
    '(' → push ['(']
    '[' → push ['(', '[']
    ']' → pop '[' ✓
    ')' → pop '(' ✓
    End: stack = [] → valid ✅

    Output: True


Example 4: s = "([)"
--------------------------------
    stack = []
    '(' → push ['(']
    '[' → push ['(', '[']
    ')' → close → pop '[' ✗ (expected '(')
    Return False ❌

    Output: False


Example 5: s = "()[]{}"
--------------------------------
    stack = []
    '(' → push ['(']
    ')' → pop '(' ✓
    '[' → push ['[']
    ']' → pop '[' ✓
    '{' → push ['{']
    '}' → pop '{' ✓
    End: stack = [] → valid ✅

    Output: True



---
Q: What happens in this loop?
"""

matching = {"(": ")", "[": "]", "{": "}"}
for c in matching:
    print(c)

"""
  • matching is a dictionary — it stores key-value pairs.
     • Keys: "(", "[", "{"
     • Values: ")", "]", "}"

  • When you do `for c in matching:`, Python automatically loops ONLY over the KEYS of the dictionary.
    • So it goes through: "(", "[", "{"
    • It does NOT loop through the values (")", "]", "}").

  • The print(c) line would print:
    (
    [
    {

  • If you wanted to loop through both keys and values, you'd use:
    for key, value in matching.items():
    print(key, value)

---
Q: How does this relate to the full `isValid` function?

  • Inside the `isValid` function, the condition `if c in matching:` checks if the current character is one of the opening brackets — the dictionary keys.

  • If it is, the code pushes it to the stack.
    - Example: when c = "(" → it's a key in `matching`, so it gets added to the stack.

  • Later, when a closing bracket is found, the function uses the dictionary to verify that it matches the right type of opening bracket.

---
In short:
  • `for c in matching:` or `if c in matching:` only looks at the dictionary's keys (the opening brackets).




---
Q: Why does the code use `if not stack: return False`?
  • It checks if the stack is empty before trying to pop.  

  • If the stack is empty, it means there's a closing bracket without a matching opening one.  

  • `not stack` → True when stack is empty, so we return False because it's invalid syntax.  

  • Equivalent to: `if len(stack) == 0: return False`  

  • Simpler and more Pythonic — avoids errors and keeps the code clean.



---
Q: Why does the solution end with `return not stack`?
  • It checks if the stack is empty at the end.

  • If the string is valid, all opening brackets were matched and popped — so stack should be empty.

  • `not stack` → True when stack is empty, False otherwise.

  • Equivalent to: `return len(stack) == 0`

  • Simpler and more Pythonic — shorter and easier to read.
  


---
Q: How do you test if something is truthy or falsy in Python?
  • You can use a simple `if` statement — Python automatically checks truthiness.
"""

# Examples:
# -----------
x = []        # empty list → falsy
y = [1, 2, 3] # non-empty list → truthy

if x:
    print("x is truthy")
else:
    print("x is falsy")  # prints this

if y:
    print("y is truthy")  # prints this
else:
    print("y is falsy")

"""
Notes:
-------
  • Falsy values: `0`, `""`, `[]`, `{}`, `set()`, `None`, `False`
  • Truthy values: everything else (non-empty strings, non-zero numbers, non-empty containers, etc.)

"""







# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def isValid(s):
    stack = []                          # Stack to track opening brackets
    matching = {"(": ")", "[": "]", "{": "}"}  # Map opening to closing bracket
   
    for c in s:                         # Iterate over each character
        if c in matching:               # If character is opening bracket
            stack.append(c)             # Push onto stack

        else:                           # If character is closing bracket
            if not stack:               # If stack empty (no opening)
                return False            # Invalid: closing without opening
           
            last_open = stack.pop()       # Pop last opening bracket
            if matching[last_open] != c:  # If not matching pair
                return False              # Invalid: wrong closing bracket
    
    return not stack                    # Valid only if all brackets matched

s = "()"
print(isValid(s))  # Output: True

s = "([])"
print(isValid(s))  # Output: True

s = "(["
print(isValid(s))  # Output: False




# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Playground 
d = {'a': 1, "b": 2}
for c in d:
    print(c)

matching = {"(": ")", "[": "]", "{": "}"}
for c in matching:
    print(c)


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# LIST METHOD: 
.pop()
# What it does: Removes and returns element at index (default last).
# Why use it: Removes while retrieving value.
# How it works: Shifts if not last; modifies in place.
# When to use: Implementing stacks or queues.
# Time/Space: O(1) for last, O(n) otherwise, O(1) space.

# Syntax:
list.pop(index)  # Removes/returns at 'index' (optional, defaults -1)

# Basic Example 1 (Pop Last):
lst = [1, 2, 3]
item = lst.pop()
print(item, lst)  # Output: 3 [1, 2]

# Basic Example 2 (Pop Index):
lst = [1, 2, 3]
item = lst.pop(1)
print(item, lst)  # Output: 2 [1, 3]

# Basic Example 3 (Empty List):
# lst = []
# lst.pop()  # Raises IndexError

# DSA Example (Stack Pop):
stack = [1, 2, 3]
last = stack.pop()
print(last, stack)  # Output: 3 [1, 2]



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Same solution rewritten

def isValid(s):
    stack = []
    matching = {"(": ")", "[": "]", "{": "}"}
    
    for c in s:
        if c in matching: # if c is an opening bracket
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            
            last_open = stack.pop()
            if matching[last_open] != c:
                return False

    return len(stack) == 0

