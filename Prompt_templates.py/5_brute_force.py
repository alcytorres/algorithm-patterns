"""
============================================
BRUTE FORCE SOLUTION TEMPLATE
============================================
Your task: Create the **simplest brute force solution** that logically leads to the optimized solution.

I may provide an efficient solution to a LeetCode problem for you to dervive the brute force. If I do NOT just give me the simplest brute force solution. 

Follow these rules strictly.

--------------------------------------------------
FORMAT THE OUTPUT EXACTLY LIKE THIS STRUCTURE

Provide the **simple brute force Python solution**.

Rules for the brute force code:
- Prefer nested loops
- Prefer simple logic
- Avoid advanced tricks
- Avoid hash maps unless absolutely necessary
- The goal is the most **intuitive beginner solution**
- Code should be easy for someone learning algorithms to understand


Add the complexity explanation inside a """ """ block, matching the study + interview format used in optimized solutions:

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
IMPORTANT STYLE RULES

• Keep the brute force solution SIMPLE  
• Prefer clarity over cleverness  
• Avoid optimized techniques (no prefix sums, no sliding window, etc.)  
• Assume this brute force solution comes BEFORE the optimized version in learning

--------------------------------------------------
"""

# Use this example as a reference 

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

"""
