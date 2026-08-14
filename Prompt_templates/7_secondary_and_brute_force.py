"""
============================================
SECONDARY SOLUTIONS + BRUTE FORCE
============================================

NOT for the top solution I will memorize (that already has the full write-up).

This is for Solution 2 / 3 / 4 and brute force.
Usually: one extra efficient solution + brute force. Add more only if the problem truly needs them.

Write them into my .py file after Solution 1.
Keep them short. They must still stand alone — I should understand each one without rereading Solution 1.

This was inspired by NeetCode's solution write ups with my own preferrences applied.
Here is an example: https://neetcode.io/solutions/valid-palindrome-ii

--------------------------------------------------
EVERY extra solution uses this skeleton

# Solution N: Pattern + Core Idea
# One plain-English line: what this version does and why it exists.

class Solution:
    ...

solution = Solution()
# run the problem's examples
print(...)
# Output: ... → short why


Intuition
    • 2–4 bullets. Explain THIS code in plain words.
    • A first-time reader should get it with no prior notes.
    • No jargon unless you spell it out (e.g. Time Limit Exceeded (TLE)).
    • If a constraint is 10⁵, write: n = 10⁵ means 100,000.
    • Do NOT say "same skip as Solution 1"
      Show the leftover as a string when that helps ("aca").

How it works
    • 3–5 short steps that map to the code.

Interview Answer: Worst Case

Time: O(...)
  - 1–2 bullets.

Space: O(...)
  - 1–2 bullets.


---
Quick Example Walkthrough:

    s = "abca"

    Step 1: ...
    Step 2: ...
    Step 3: ...

    Final Answer: ...


--------------------------------------------------
RULES

    • Same skeleton for every extra solution so they scan the same way.
    • class Solution (LeetCode / interview style).
    • Interview time/space only — no long study complexity block.
    • No Breakdown, no Most IMPORTANT, no Thoughts → Code, no Full Walkthrough.
    • Quick Example: one main example is enough (the one that shows the idea).
    • Brute force: say it is correct, why it is too slow, and what the two-pointer / optimal versions do instead.
    • Extra efficient solution: say how it differs from Solution 1 (usually extra memory or a simpler picture).
    • Concise. Crystal clear. Future-me should reread this in under a minute.
"""
