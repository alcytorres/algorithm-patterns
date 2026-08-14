"""
============================================
TOP 2 EFFICIENT SOLUTIONS (ENTRY-LEVEL)
============================================

I am practicing for entry-level SWE interviews (not FAANG).
I just want to get my foot in the door at wherever will hire me.

Give me the top 2 efficient solutions for this problem.
Maximize: simple, memorable, easy to follow, efficient enough.

--------------------------------------------------
THINKING (show this in the chat reply)

1. List 3–4 efficient approaches. Skip brute force — that comes later.
2. For each: one-line idea + why it is or isn't the pick.
3. Distill to the top 2.
4. Mark which one to memorize, and justify for a beginner.

--------------------------------------------------
NAMING

Name each solution like:
    # Solution 1: Two Pointers + Skip-One Helper  ← memorize this one
    # Solution 2: Two Pointers + Slice Remaining

Style:
    • Pattern / technique first, then the core intuition
    • Easy to skim later in notes
    • Match titles like:
        - Single Pass: Track Min Price + Max Profit
        - Two Pointers In-Place
        - Simple Palindrome Check (Build String → Two Pointers)

--------------------------------------------------
CODE (write into my .py file)

    • Keep the problem statement at the top
    • Use class Solution (LeetCode / interview style)
    • Solution 1 first (the one to memorize)
    • After each solution, run ALL examples from the problem like this:

solution = Solution()
s = "aba"
print(solution.validPalindrome(s))
# Output: True

s = "abca"
print(solution.validPalindrome(s))
# Output: True → mismatch at 'b' vs 'c'; skip 'c' and "aba" is a palindrome

s = "abc"
print(solution.validPalindrome(s))
# Output: False → skip 'a' → "bc" no; skip 'c' → "ab" no

    • Short "why this output" on the comment — not a full walkthrough
    • Concise code, never at the expense of simplicity
    • Prefer interview-safe code over clever one-liners

--------------------------------------------------
REPLY

Chat: show the thinking, name both, pick one, justify.
File: both solutions + runnable examples.
"""
