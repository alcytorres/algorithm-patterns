"""
===========================================================
STACKS & STRING PROBLEMS — PRACTICAL, HIGH-ROI MINI-GUIDE
===========================================================

Scope:
  • Based strictly on your provided content (Stacks + String problems).
  • Focused on what actually shows up in non-FAANG entry-level interviews.
  • No filler. Clear patterns, tiny templates, and quick mental models.

Contents:
1) 🧩 What is a Stack (LIFO) — mental picture + when to use it
2) ⚙️ Python Interface (list-based stack) — push/pop/peek
3) 🧠 Pattern Recognition — why stacks fit certain string problems
4) 💻 Coding Templates (3 core problems)
   - 20. Valid Parentheses
   - 1047. Remove All Adjacent Duplicates in String
   - 844. Backspace String Compare
5) ⏱️ Complexity Cheatsheet
6) 🔁 Quick Review (TL;DR)
"""


# ------------------------------------------------------------
# 1) 🧩 What is a Stack (LIFO) — mental picture + when to use it
# ------------------------------------------------------------
"""
Plain English:
  • Stack = add/remove from the SAME end (top). Last in, first out (LIFO).
  • Think kitchen plates: you put one on top, you take from the top.

Why it appears in string questions:
  • You often need a short-term "history" of prior characters to decide
  what to do with the current character (match, delete, compare).
  
  • That "most recent thing" you added is exactly what you want to inspect
  or remove first → LIFO → stack.

Recursion note:
  • Function calls use a call stack internally (push on call, pop on return).
"""


# -----------------------------------------
# 2) ⚙️ Python Interface (list as a stack)
# -----------------------------------------
"""
Use Python list as a stack (dynamic array):
    stack = []
    stack.append(x)     # push (O(1) amortized)
    top = stack[-1]     # peek (O(1))   — only if stack not empty
    x = stack.pop()     # pop (O(1))    — only if stack not empty
    empty = not stack   # True if empty
    size = len(stack)   # O(1)
"""

def _stack_demo():
    stack = []

    stack.append(1)
    stack.append(2)
    stack.append(3)
    
    a = stack.pop()   # 3
    b = stack.pop()   # 2
    stack.append(5)

    top = stack[-1] if stack else None
    return a, b, top, bool(stack)  # (3, 2, 5, True)