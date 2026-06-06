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

Provide the **simple brute force Python solution**.

Rules for the brute force code:
- Prefer nested loops, try-all-combinations, or straightforward exhaustive search when natural
- Prefer simple logic a beginner would actually write
- Avoid advanced tricks (no prefix sums, sliding window, bit tricks, etc.)
- Code should be easy for someone learning algorithms to understand

Add the complexity explanation inside a """ """ block, matching the study + interview format:

Time: O(...)
  - Define variables (e.g., N = input size).
  - Step 1: ... → O(...).
  - Step 2: ... → O(...).
  - Combined / Overall: O(...).

Space: O(...)
  - State main structures or variables.
  - Overall: O(...).

Interview Answer: Worst Case

Time: O(...)
  - 1-2 bullets highlighting the dominant step(s).

Space: O(...)
  - 1-2 bullets summarizing memory usage.


Add a final section inside the same """ """ block:
---
Overview for Each Iteration

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

--------------------------------------------------
"""

# Example 1: Brute force EXISTS (is_palindrome — O(N²) → O(N))

# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force
def is_palindrome_bruteforce(s):
    # Reverse the string and compare
    reversed_s = ""
    
    for c in s:
        reversed_s = c + reversed_s
    
    if reversed_s == s:
        return True
    return False


s = "racecar"
print(is_palindrome_bruteforce(s))
# Output: True

"""
Time: O(N²)
  - Let N = length of the string s.

  - Step 1: Build reversed string → O(N²).
      • Loop runs N times (once per character).
      • Each step: reversed_s = c + reversed_s creates a new string → O(N).

  - Step 2: Compare reversed_s == s → O(N).

  - Combined: O(N² + N).
  - Overall: O(N²).


Space: O(N)
  - reversed_s stores up to N characters.
  - Overall: O(N).


Interview Answer: Worst Case

Time: O(N²)
  - Each prepend builds a new string; N prepends → quadratic time.

Space: O(N)
  - Reversed copy of the string.


---
Overview for Each Iteration
s = "racecar"

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


# Example 2: NO natural brute force (Build Array from Permutation — O(N) is already optimal)

# ––––––––––––––––––––––––––––––––––––––––––––––
# No Natural Brute Force Solution
"""
    • The problem gives the formula directly: ans[i] = nums[nums[i]]. There is no simpler approach with worse complexity.

    • Optimal complexity: Time O(N), Space O(N).

    • Any "two-step" version (index_to_look_at = nums[i], then nums[index_to_look_at]) is the same O(N) algorithm — just more verbose. Collapsing into nums[nums[i]] is a style change, not an optimization.

    • Recommendation: Focus on understanding the optimal solution clearly and move on.
"""
