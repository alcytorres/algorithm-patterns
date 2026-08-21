"""
============================================
BRUTE FORCE SOLUTION TEMPLATE
============================================

Your task: Determine whether a **natural brute force solution** exists for this problem.
If it does, provide it. If it does not, say so clearly — that is still useful information.

I may provide an efficient solution for you to derive the brute force from.
If I do NOT, derive the standard optimal approach first, then check for brute force.

Follow these rules strictly.

--------------------------------------------------
WHAT COUNTS AS BRUTE FORCE (required)

A brute force solution must be ALL of the following:

1. **Simpler to reason about** than the optimal approach (more obvious first attempt).
2. **Strictly worse time OR space complexity** than the optimal solution.
3. A natural stepping stone that **logically leads to** the optimization.

Example shape: O(N²) nested loops → O(N) direct access. That is real brute force.

--------------------------------------------------
WHAT DOES NOT COUNT AS BRUTE FORCE (do NOT provide these)

• Same time and space complexity as the optimal solution.
• Same algorithm with more variables, clearer naming, or verbose steps.
• Same algorithm written in a more readable way.
• Artificially adding nested loops or extra work just to create a slower version.
• A "first draft" that is only a stylistic difference (e.g. two explicit steps vs one chained expression).

If the only difference is code style, there is no brute force — just learn the optimal solution and move on.

--------------------------------------------------
STEP 1: CHECK FIRST — does a natural brute force exist?

Before writing any code, ask:
    • Is there a simpler approach a beginner would try first?
    • Is that approach strictly slower (worse Big-O) than the optimal solution?
    • Would optimizing away from it teach a real insight (not just "write it in fewer lines")?

If NO to any of these → skip brute force code entirely. Use the "No Brute Force" format below.

--------------------------------------------------
FORMAT A — when a natural brute force EXISTS
(Steps 2, 3, and 4 below are all required.)

Provide the **simple brute force Python solution**.

Rules for the brute force code:
- Prefer nested loops, try-all-combinations, or straightforward exhaustive search when natural
- Prefer simple logic a beginner would actually write
- Avoid advanced tricks (no prefix sums, sliding window, bit tricks, etc.)
- Code should be easy for someone learning algorithms to understand

--------------------------------------------------
STEP 2: REQUIRED — inline cost annotations ON the code

Add a short `# O(...)` comment on every line whose cost is NOT obviously O(1).

This is the most important part of the brute force write-up. The whole point of
brute force is to see WHERE the slowness lives, and the slow line is usually a
short, innocent-looking one-liner. A loop can look linear while the real cost is
hidden inside a built-in method.

Annotate lines like these:

    x in some_list          → # O(N) scan
    some_list.remove(x)     → # O(N) find + shift
    some_list.index(x)      → # O(N) scan
    some_list.pop(0)        → # O(N) shift
    s = c + s   (in a loop) → # O(N) builds a new string
    sorted(x) / x.sort()    → # O(N log N)
    max/min/sum(collection) → # O(N)
    s[i:j]  (slice)         → # O(K) copy
    the loop header itself  → # O(N) iterations

Do NOT annotate obvious O(1) lines (`count += 1`, `return c`, `left = 0`).
Keep each annotation to ~2-5 words after the O(...).
Align the comments in a column so the code stays easy to read.

--------------------------------------------------
STEP 3: the complexity block

Add the complexity explanation inside a """ """ block.

Pick ONE of the two forms below.


FORM 1 — MULTIPLY-OUT (use this whenever the cost is "loop × expensive work inside")

Use this when a loop contains a non-O(1) operation — including when the loop
LOOKS linear because nothing is visibly nested. This is the default for brute force.

Time: O(...)
  - Define variables (e.g., N = input size).

  - <setup line before the loop> → O(...)

  - The loop runs O(...) times.
    Inside each loop:
      • <slow line 1> → O(...)
      • <slow line 2> → O(...)

  - Work inside one loop:
      O(...) + O(...) = O(...)

  - That O(...) work happens O(...) times:
      O(...) × O(...) = O(...)

  - Including the setup:
      O(...) + O(...) = O(...)

  - Overall: O(...).

Why this form matters: seeing "each piece is O(N)" is NOT enough. The step that
must be written out explicitly is iterations × work per iteration. Never compress
that into a single line like "Combined: O(N + N × N)".


FORM 2 — STEP LIST (use only when there is no expensive work inside a loop)

Use this when the brute force is just a sequence of separate O(1)/O(N) passes and
the extra cost is memory, not nesting.

Time: O(...)
  - Define variables (e.g., N = input size).
  - Step 1: ... → O(...).
  - Step 2: ... → O(...).
  - Combined: O(...) + O(...) = O(...).
  - Overall: O(...).


BOTH FORMS then end with:

Space: O(...)
  - State main structures or variables.
  - Overall: O(...).

Interview Answer: Worst Case

Time: O(...)
  - 1-2 bullets highlighting the dominant step(s).
  - When Form 1 was used, one bullet should name BOTH pieces:
    the number of iterations AND the work done inside each iteration.
  - Do NOT put the multiply-out chain here. Keep the interview answer short.

Space: O(...)
  - 1-2 bullets summarizing memory usage.

--------------------------------------------------
STEP 4: REQUIRED — Overview for Each Iteration

Always include this. Never drop it.
The complexity block explains WHY it is slow; the Overview explains WHAT happens.
I need both.

Add a final section inside the same """ """ block:
---
Overview for Each Iteration
Input: ...

Show a **simple high-level walkthrough** of how the algorithm works on the example input.

Use a readable step format like:

    i = ...
    j = ...
    value being checked
    result / update

End with:
Final: [answer]

The goal of the Overview is to quickly show how the answer is reached.

--------------------------------------------------
FORMAT B — when NO natural brute force exists

Do NOT invent a fake brute force solution.

Instead, provide this inside a """ """ block:

---
No Natural Brute Force Solution

    • [1-2 sentences: why no slower natural approach exists for this problem.]

    • Optimal complexity: Time O(...), Space O(...).

    • [1-2 sentences: what the "optimization" actually is, if any — e.g. "the problem gives the formula directly; the only step is translating it to code."]

    • Recommendation: Focus on understanding the optimal solution clearly and move on.

--------------------------------------------------
IMPORTANT STYLE RULES

• Only include brute force when it teaches a real slow → fast optimization path.
• Do NOT provide multiple solutions with identical complexity — that adds unnecessary mental overhead.
• Prefer clarity over cleverness.
• Assume brute force comes BEFORE the optimized version in learning — but only when it genuinely exists.
• ALWAYS annotate the slow lines with # O(...) — abstract "Step 2" wording alone is not enough.
• ALWAYS write out iterations × work-per-iteration as its own step (Form 1).
• ALWAYS keep the Overview for Each Iteration section.
• Point at the specific line that causes the slowness, not just the overall Big-O.

--------------------------------------------------
"""

# Example 1: Brute force EXISTS (is_palindrome — O(N²) → O(N))
# Uses FORM 1 (multiply-out): the loop looks linear, but string building is O(N) inside.

# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force — Reverse the string and compare
def is_palindrome_bruteforce(s):
    reversed_s = ""

    for c in s:                       # O(N) iterations
        reversed_s = c + reversed_s   # O(N) builds a new string

    if reversed_s == s:               # O(N) compare
        return True
    return False


s = "racecar"
print(is_palindrome_bruteforce(s))
# Output: True

"""
Time: O(N²)
  - Let N = length of the string s.

  - reversed_s = "" → O(1)

  - The loop runs O(N) times.
    Inside each loop:
      • reversed_s = c + reversed_s → O(N)
        (strings are immutable, so Python builds a brand-new string every time)

  - Work inside one loop:
      O(N)

  - That O(N) work happens O(N) times:
      O(N) × O(N) = O(N²)

  - Final compare reversed_s == s → O(N)

  - Including the compare:
      O(N²) + O(N) = O(N²)

  - Overall: O(N²).


Space: O(N)
  - reversed_s stores up to N characters.
  - Overall: O(N).


Interview Answer: Worst Case

Time: O(N²)
  - N loop iterations, and each prepend rebuilds the whole string → O(N) work inside.

Space: O(N)
  - Reversed copy of the string.


---
Overview for Each Iteration
Input: s = "racecar"

    reversed_s starts = ""

    read 'r' → reversed_s = "r"
    read 'a' → reversed_s = "ar"
    read 'c' → reversed_s = "car"
    read 'e' → reversed_s = "ecar"
    read 'c' → reversed_s = "cecar"
    read 'a' → reversed_s = "acecar"
    read 'r' → reversed_s = "racecar"

    compare reversed_s == s
    "racecar" == "racecar" → True

Final: True
"""


# Example 2: Brute force EXISTS (389. Find the Difference — O(N²) → O(N))
# Uses FORM 1 (multiply-out) with TWO slow lines inside one loop.
# This is the clearest example of hidden cost: the loop has no nested loop in it,
# but `in` and `.remove()` each scan the whole list.

# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force — List + remove (cross off letters from a copy of s)

def findTheDifference_bruteforce(s, t):
    available = list(s)          # O(N) copy

    for c in t:                  # O(N) iterations
        if c not in available:   # O(N) scan
            return c
        available.remove(c)      # O(N) find + shift


s = "abca"
t = "abcae"
print(findTheDifference_bruteforce(s, t))
# Output: "e"


"""
Time: O(N²)
  - Let N = length of s. t has N + 1 letters.

  - available = list(s) → O(N)

  - The loop runs O(N) times.
    Inside each loop:
      • c not in available → O(N)
      • available.remove(c) → O(N)

  - Work inside one loop:
      O(N) + O(N) = O(N)

  - That O(N) work happens O(N) times:
      O(N) × O(N) = O(N²)

  - Including the initial copy:
      O(N) + O(N²) = O(N²)

  - Overall: O(N²).


Space: O(N)
  - available stores a copy of the N letters in s.
  - Overall: O(N).


Interview Answer: Worst Case

Time: O(N²)
  - O(N) loop iterations, with O(N) list work inside each iteration.
  - Each letter in t may scan the full list to check and remove.

Space: O(N)
  - Stores a mutable copy of s as a list.


---
Overview for Each Iteration
Input: s = "abca", t = "abcae"

    available starts = ['a', 'b', 'c', 'a']

    c = 'a' → in list → remove → ['b', 'c', 'a']
    c = 'b' → in list → remove → ['c', 'a']
    c = 'c' → in list → remove → ['a']
    c = 'a' → in list → remove → []
    c = 'e' → NOT in list → return 'e'

Final: "e"
"""


# Example 3: NO natural brute force (Build Array from Permutation — O(N) is already optimal)

# ––––––––––––––––––––––––––––––––––––––––––––––
# No Natural Brute Force Solution
"""
    • The problem gives the formula directly: ans[i] = nums[nums[i]]. There is no simpler approach with worse complexity.

    • Optimal complexity: Time O(N), Space O(N).

    • Any "two-step" version (index_to_look_at = nums[i], then nums[index_to_look_at]) is the same O(N) algorithm — just more verbose. Collapsing into nums[nums[i]] is a style change, not an optimization.

    • Recommendation: Focus on understanding the optimal solution clearly and move on.
"""
