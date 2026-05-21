# ––––––––––––––– Prompts –––––––––––––––



# ––––––––––––––––––––––––––––––––––––––––
# GET OUTPUT FOR LEETCODE SOLUTIONS
# ––––––––––––––––––––––––––––––––––––––––
# For this code provide the additional code required so that I can run and verify the output of the examples provided

# For this code provide the additional code required so that I can run and verify the output of a basic simple example you recommend that fully shows all funcitonality of the code





# ––––––––––––––––––––––––––––––––––––––––
# LEETCODE SOLUTIONS
# –––––––––––––––––––––––––––––––––––––––

# –––––––––––––––––––––––––––––––––––––––
#  What is the best efficient simple solution? 
# –––––––––––––––––––––––––––––––––––––––
# What is the absolute best, basic, simple, memorable, easy to follow for a beginner top 2 solution for this problem that is efficient thar you rec for someone practicting for entry level SWE technical interviews?  Not targetting FAANG companies. Just want to get my first door at where ever will hire me
# Justify your answer

# What is the absolute best, basic, simple, memorable, easy to follow for a beginner solution for this problem that is efficient? Justify your answer

# Which of the following is the absolute best, basic, simple, memorable, easy to follow for a beginner solution for this problem that is efficient? Justify your answer


# The goal is clarity and learning for a beginner to easily follow along



# ––––––––––––––––––––––––––––––––––––––––
# Which of the following is more easy to understand and remember and follow along for a beginner


# ––––––––––––––––––––––––––––––––––––––––
# Give me excellent in line annotations for this code




# –––––––––––––––––––––––––––––––––––––––––––––––
# FULL: What is the best efficient simple solution? 
# –––––––––––––––––––––––––––––––––––––––––––––––
"""
Q: What is the best efficient simple solution for a beginner to understand this problem?

The goal is:
• Clarity: easy-to-follow explanation.
• Learning: helps me actually understand the reasoning.
• Retention: highest probability I remember the solution later.

Instructions for you (the LLM):
    1. Reflect on 3-4 different possible efficeint approaches. Don't pick brute force that will be done later. Show the code for each solution.

    2. Distill those down into the top 1-2 candidate solutions, and explain why they’re better than the others.

    3. Pick the one solution that you think is best for my use case (beginner-friendly + efficient).

    4. Explain it excellently with:
        • The key idea in plain language.
        • Why it works.
        • Why it's simpler/better for a beginner than the alternatives.
        • Small example to illustrate.

    5. Justify your choice so I can understand the tradeoffs.

    The solution needs to maximize retention — meaning the highest chance I’ll actually remember it later. For that to work, I prefer the code to stay concise, but never at the expense of simplicity.

"""

# –––––––––––––––––––––––––––––––––––––––––––––––





# –––––––––––––––––––––––––––––––––––––––––––––––
# Give me a excellent one sentence explanation of the output like this:
# –––––––––––––––––––––––––––––––––––––––––––––––

    # Output: 3.5 → Subarray [3, 4] (length 2, sum 3 + 4 = 7, average 7/2 = 3.5) has the largest average for k=2.

    # Output: 2 → Valid splits after indices [0, 1]:
    # - Split 0 → left = 10, right = 3 ✅
    # - Split 1 → left = 14, right = -1 ✅
    # - Split 2 → left = 6, right = 7 ❌

# for this code




# –––––––––––––––––––––––––––––––––––––––––––––––
# Prompt for Visual for LeetCode Solutions 




# –––––––––––––––––––––––––––––––––––––––––––––––
# Give me a concise GUIDE on XYZ 
# –––––––––––––––––––––––––––––––––––––––––––––––
# Give me a concise, simple, excellent for beginner GUIDE on XYZ as was used in this LeetCode problem. Show a basic example and then an example within a function

# Here is an example
# Copy the same format


# Guide
"""
📘 Tutorial: sum(condition for x in items)

- You can use sum() with a generator expression to count matches.
- Each condition produces True (1) or False (0).
- sum() adds them up → count of items where condition is True.
"""

# Example: condition for x in items:
nums = [1, 2, 3, 4]
evens = sum(x % 2 == 0 for x in nums)
print(evens)   # Output 2 (since 2 and 4 are even)


# Example: condition for x in items:
def fn(nums):
    return sum(num % 2 == 0 for num in nums)

nums = [1, 2, 3, 4]
print(fn(nums))   # Output 2 (since 2 and 4 are even)


# Guide
"""
Tutorial: .split() + .join() in LeetCode

  - .split() turns string into list of parts
  - .join() turns list back into string with separator
  
  - Use together to clean, reorder, or rebuild strings
"""

# Example 1: Reverse Words
def reverse_words(s):
    words = s.split()           # → ['sky', 'is', 'blue']
    words.reverse()             # → ['blue', 'is', 'sky']
    return " ".join(words)      # → "blue is sky"

print(reverse_words("sky is blue"))


# Example 2: Remove Extra Spaces
def clean_spaces(s):
    words = s.split()           # → ['hello', 'world'] (removes extra spaces)
    return " ".join(words)      # → "hello world"

print(clean_spaces("  hello   world  "))


# Example 3: Build Path from string
def build_path(s):
    parts = s.split("/")           # → ['', 'home', 'user', 'docs']
    parts = [p for p in parts if p]  # remove empty
    return "/" + "/".join(parts)

print(build_path("/home/user/docs/"))  # "/home/user/docs"


# Example 3: Build Path from string (no list comprehension)
def build_path(s):
    parts = s.split("/")           # ['', 'home', 'user', 'docs']
    stack = []
    for p in parts:
        if p:                      # skip empty strings
            stack.append(p)
    return "/" + "/".join(stack)

print(build_path("/home/user/docs/"))  # "/home/user/docs"







# –––––––––––––––––––––––––––––––––––––––––––––––
# Give me a simple, easy to understand, concise reply in bullets and set up with a question as the header for the prior response XYZ. 

# Provide your reply in a .py file with """

# Here is an example

"""
---
Q: Why do we use `while head and head.next:` instead of `while head:`?
    • Each swap needs a pair of nodes — the current node (`head`) and the next one (`head.next`).
    
    • If we only check `while head:`, the last single node (when list length is odd) would try to swap with `None` → causes an error.
    
    • `while head and head.next:` safely stops when fewer than 2 nodes remain.

    • This ensures all valid pairs are swapped without breaking the list.

"""


# –––––––––––––––––––––––––––––––––––––––––––––––
# Get a better step by step walkthru
# –––––––––––––––––––––––––––––––––––––––––––––––
# For this code:


# Is there a better, concise, simple, super easy to follow for a beginner walkthru of the code for each iteration. Justify your answer. I want it to be crystal clear and easy to follow. Also it should be concise so i can quickly follow and scan the flow. 


# Reply in a .py file with """






# ===============================================
# My TOP PREFERENCES FOR GUIDES
# ===============================================
"""
My Preferences for my Guides:

- Structured, readable, and visually clear — with clear section headers (🧩, 📦, 💡, 🔁, etc.).

- Intuitive and beginner-friendly, written in plain English with simple analogies (like boxes or train cars).

- Formatted for scanning — tables, bullet points, and “mental picture” sections.

- Concise but complete — no jargon, no redundancy, every section should feel necessary and educational.

- Chronological and visual — you like seeing the flow of code execution (step-by-step or line-by-line).

- Repeat key takeaways at the end (like the TL;DR cheat sheet) for quick future review.

"""