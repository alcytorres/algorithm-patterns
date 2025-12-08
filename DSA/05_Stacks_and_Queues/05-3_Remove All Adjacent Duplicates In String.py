# 1047. Remove All Adjacent Duplicates In String

# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

# We repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

# Solution: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/

# Example 1:
    # Input: s = "abbaca"
    # Output: "ca"
    # Explanation: 
    # For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

# Example 2:
    # Input: s = "azxxzy"
    # Output: "ay"

def removeDuplicates(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    
    return "".join(stack)

s = "abbc"
print(removeDuplicates(s))  # Output: ac

s = "abbaca"
print(removeDuplicates(s))  # Output: ca

s = "azxxzy"
print(removeDuplicates(s))  # Output: ay


"""
Time: O(N)
  - Let N = length of string s.
  - Each character is pushed onto or popped from the stack at most once.
  - Stack operations (append, pop, check last element) are O(1) each.
  - Joining the final stack into a string takes O(N).
  - Overall: O(N).

Space: O(N)
  - Stack may store up to N characters in the worst case (no duplicates).
  - A few variables (c, loop counters) use O(1).
  - Overall: O(N).

  
Interview Answer: Worst Case

Time: O(N)
  - Each character added or removed from the stack once.

Space: O(N)
  - Stack stores remaining non-duplicate characters.


---
Overview for Each Iteration
Input: s = "abbaca"

Step: Remove adjacent duplicates using stack
c   | stack (before) | stack[-1] == c | Action | stack (after)
----|----------------|----------------|--------|---------------
a   | []             | -              | append | ['a']
b   | ['a']          | False          | append | ['a', 'b']
b   | ['a', 'b']     | True           | pop    | ['a']
a   | ['a']          | True           | pop    | []
c   | []             | -              | append | ['c']
a   | ['c']          | False          | append | ['c', 'a']

Final: "ca"



---
Most IMPORTANT thing to Understand:
    • The stack keeps track of characters that are not yet part of a duplicate pair.

    • Whenever the current character matches the top of the stack, both are removed — simulating “adjacent duplicate removal.”

    • We repeat this until the whole string is processed; the stack naturally collapses duplicates as they appear.

---
Why this code Works:
    • Data structure: stack — ideal for removing pairs in LIFO order (last added gets compared first).

    • Process:
        - For each character c:
            • If the stack's top == c → pop (remove duplicate pair).
            • Else → push c onto the stack.
        - Join stack at the end to rebuild final string.

    • Efficiency: O(N) time, O(N) space; each char added/removed once.

    • Intuition: Like undoing pairs — imagine typing letters and hitting “backspace” whenever you see two same letters side by side.

---
TLDR:
    • Push characters to a stack, and remove the top when the same character appears — duplicates cancel each other out.

---
Quick Example Walkthroughs:

Example 1: s = "abbc"
--------------------------------
    stack = []
    'a' → push ['a']
    'b' → push ['a','b']
    'b' → top == 'b' → pop → ['a']
    'c' → push ['a','c']
    Final stack = ['a','c']
    Result: "ac"

    Output: "ac" ✅

    
Example 2: s = "abbaca"
--------------------------------
    stack = []
    'a' → push ['a']
    'b' → push ['a','b']
    'b' → top == 'b' → pop → ['a']
    'a' → top == 'a' → pop → []
    'c' → push ['c']
    'a' → push ['c','a']
    Final stack = ['c','a']
    Result: "ca"

    Output: "ca" ✅


Example 3: s = "azxxzy"
--------------------------------
    stack = []
    'a' → push ['a']
    'z' → push ['a','z']
    'x' → push ['a','z','x']
    'x' → top == 'x' → pop → ['a','z']
    'z' → top == 'z' → pop → ['a']
    'y' → push ['a','y']
    Final stack = ['a','y']
    Result: "ay"

    Output: "ay" ✅


    


---
Q: What does `if stack and stack[-1] == c:` do?

  • Checks 2 things in one line:
      1. `if stack` → makes sure the stack is not empty (avoids error if we try to access stack[-1])

      2. `stack[-1] == c` → checks if the last character in the stack is the same as the current one

  • If both are true → it means we found two adjacent duplicates, so we remove the last one using `stack.pop()`.

  • In short: "If there's something in the stack and it matches the current character, remove it."


---
Q: Why do we need `if stack`?
  • To make sure the stack is NOT empty before checking stack[-1].

Example: s = "a"

Without `if stack`:
--------------------
  • stack = []
  • 'a' → check stack[-1] == 'a' → ❌ ERROR (stack is empty!)

With `if stack`:
--------------------
  • stack = []
  • 'a' → stack is empty → skip comparison → push → stack = ['a']

✅ Prevents error when trying to access stack[-1] on an empty stack.

"""







# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def removeDuplicates(s):
    stack = []                        # Stack to build result
    
    for c in s:                       # Iterate over each character
        if stack and stack[-1] == c:  # If current char matches top of stack
            stack.pop()               # Remove the pair (cancel out)
        else:                         # Otherwise, no match
            stack.append(c)           # Add char to stack

    return "".join(stack)             # Convert stack to final string





# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Playgorund

stack = ['a', 'c']
print("".join(stack))  # ac











# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Approach 2: Replace

from string import ascii_lowercase

def removeDuplicates(S):
    # generate 26 possible duplicates
    duplicates = {2 * ch for ch in ascii_lowercase}
    
    prev_length = -1
    while prev_length != len(S):
        prev_length = len(S)
        for d in duplicates:
            S = S.replace(d, '')
            
    return S