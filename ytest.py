# ––––––––––––––– Prompts –––––––––––––––


# ––––––––––––––––––––––––––––––––––––––––
# LEETCODE SOLUTIONS EXPLANATIONS CONCISE
# ––––––––––––––––––––––––––––––––––––––––
# Explain this in a simple, very easy to understand, intuitive, memorable way so that in future I can quickly read/scan through and understand

# ---
# Super simple, beginner-friendly Leetocde FULL breakdown

# I need a super simple, beginner-friendly explanation of how this LeetCode solution works, as if explaining to a 12-year-old who’s just learning to code. Break it down crystal clear, focusing on why the code finds the correct answer for the given problem. 

# Use the provided example input and output to walk through the solution step by step, showing how each part of the code contributes to the final result. Include a simple analogy to make it relatable. If the solution uses a loop, provide a concise iteration overview (like a table) showing key variable changes for each step.


# ––––––––––––––––––––––––––––––––––––––––
# GET OUTPUT FOR LEETCODE SOLUTIONS
# ––––––––––––––––––––––––––––––––––––––––
# For this code provide the additional code required so that I can run and verify the output of the examples provided

# For this code provide the additional code required so that I can run and verify the output of a basic simple example you recommend that fully shows all funcitonality of the code


# ––––––––––––––––––––––––––––––––––––––––
# LEETCODE SOLUTIONS EXPLANATIONS FULL
# ––––––––––––––––––––––––––––––––––––––––
# I need a super simple, easy to follow, very beginner-friendly explanation of how this LeetCode solution works. Break it down into 4 main parts: "Most IMPORTANT thing to Understand", "Why this code Works, TLDR (why this code works in one sentence), and Quick Example Walkthrough.

# Make it crystal clear, focusing on why the code finds the correct answer for the given problem. I should be able to look back at this at any time and quickly follow along and understand it. 

# ⚠️ It is important you be concise and have no fluff in your reply. You should not sacrifice clarity, but if something can be said in fewer words without losing understanding, then use fewer words. This requires a delicate balance: always aim for maximum clarity with minimum words.

# Between each bullet point skip a line to space out the breakdown and make it more easy to scan

# Here is a great template with more detail of what I'm looking that you can you as a reference. While I want you to generally follow this template it is not rigid. If you think adding a little more detail to a specific problem is necessary for me to fully understand make sure to do that.

"""
Most IMPORTANT thing to Understand:
    • [Key intuition in 2-3 bullets — e.g., what the main variable tracks or what the core idea is]

    • [State the condition that guarantees we've found a valid answer, in plain words]

    • [If applicable, point out what the hash map / set / pointer is doing in simple terms]

Why this code Works:
    • Hash map / data structure role: [Explain what it stores and why it's useful]

    • Prefix sum / sliding window / two pointers idea: [Explain how the technique applies here]

    • Efficiency: [1-2 bullets on why this avoids brute force, O(n) vs O(n^2)]

    • Intuition: [Beginner analogy — “like tallying votes”, “like keeping a running score”, etc.]

Quick Example Walkthrough:
    nums = [example input], k = [value if relevant]

    Step 1: [Describe what happens as you process elements one by one, how key variables (like curr, odd, counts, etc.) change]

    Step 2: [Show the subarrays / result as they're discovered]

    Final Answer: [Result]
"""


# Example to reference: 
from collections import defaultdict

def largestUniqueNumber(nums):
    # Step 1: Count occurrences of each number
    counts = defaultdict(int)
    for num in nums:
        counts[num] += 1
    # Step 2: Find the largest number with count 1
    max_unique = -1
    for num in counts:
        if counts[num] == 1 and num > max_unique:
            max_unique = num
    return max_unique

nums = [1, 3, 9, 4, 9, 8, 3]
print(largestUniqueNumber(nums))
# Output: 8


# Example breakdown to reference: 
"""
Most IMPORTANT thing to Understand:
    • We need to find the largest number in the array that occurs exactly once.

    • First, we count how many times each number appears.

    • Then we check which numbers are unique (count == 1) and pick the largest one.

    • If no number is unique, we return -1.

Why this code Works:
    • Hash map (counts): stores how many times each number appears.

    • Scan through counts:
        • If a number's count == 1 → it's unique.
        • Compare with current max_unique and update if larger.

    • Efficiency: Instead of checking subarrays or sorting, we just tally counts in O(n) and then make one pass over the results.

    • Intuition: Think of it like a vote tally — each number “gets votes.” We only want numbers that got exactly one vote, and we pick the biggest of those.

TLDR
    • This solution works because we count how often each number appears, then pick the largest one that occurs exactly once.
    
Quick Example Walkthrough:
    nums = [1, 3, 9, 4, 9, 8, 3]

    Step 1: Count frequencies
        counts = {1:1, 3:2, 9:2, 4:1, 8:1}

    Step 2: Check unique numbers
        • 1 → count=1, max_unique = 1
        • 3 → count=2, skip
        • 9 → count=2, skip
        • 4 → count=1, max_unique = 4
        • 8 → count=1, max_unique = 8

    Final Answer: 8
"""


# LeetCode problem for you to breakdown



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
# TIME AND SPACE SOLUTION
# –––––––––––––––––––––––––––––––––––––––––––––––
# Give me the time and space for the following in this format:
    # Format like this
    # Time: O(n)
    # - Loop through nums once: O(n) iterations.
    # - Dictionary lookups and updates ('counts[curr - k]', 'counts[curr] += 1') are O(1) on average.
    # - No nested loops, so total time is O(n).

    # Space: O(n)
    # - Dictionary 'counts' can store up to n different prefix sums in the worst case: O(n) space.
    # - A few variables (curr, ans, num) take O(1) space.
    # - Overall: O(n) total space.




# –––––––––––––––––––––––––––––––––––––––––––––––
# Overview for Each Iteration
# –––––––––––––––––––––––––––––––––––––––––––––––
# Give me the overview of each iteration of this code
# Provide your answer in a .py file so i can copy it into the write up for this problem
# Only reply with the Overview for Each Iteration

# Here is a great example.
# Note you can choose the format you think is best for the overview depending on the problem. You dont always have to do a 2 steps breakdown. In this example it just really made sense. 
# The goal is clarity and learning for a beginner to easily follow along


from collections import defaultdict

def largestUniqueNumber(nums):
    # Step 1: Count occurrences of each number
    counts = defaultdict(int)
    for num in nums:
        counts[num] += 1
    
    # Step 2: Find the largest number with count 1
    max_unique = -1
    for num in counts:
        if counts[num] == 1 and num > max_unique:
            max_unique = num
    
    return max_unique

nums = [1, 3, 9, 4, 9, 8, 3]
print(largestUniqueNumber(nums))
# Output: 8

# counts = {1:1, 3:2, 9:2, 4:1, 8:1}


# Overview for Each Iteration
# Step 1: Count occurrences
# i   | num | counts
# ----|-----|----------------------------
# -   | -   | {}
# 0   | 1   | {1:1}
# 1   | 3   | {1:1, 3:1}
# 2   | 9   | {1:1, 3:1, 9:1}
# 3   | 4   | {1:1, 3:1, 9:1, 4:1}
# 4   | 9   | {1:1, 3:1, 9:2, 4:1}
# 5   | 8   | {1:1, 3:1, 9:2, 4:1, 8:1}
# 6   | 3   | {1:1, 3:2, 9:2, 4:1, 8:1}

# Step 2: Find largest unique number
# num | counts[num] | max_unique
# ----|-------------|-------------
# -   | -           | -1
# 1   | 1           | 1 (updated)
# 3   | 2           | 1 (skipped)
# 9   | 2           | 1 (skipped)
# 4   | 1           | 4 (updated)
# 8   | 1           | 8 (updated)
# Final: 8




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
# Prompt for Guides
# –––––––––––––––––––––––––––––––––––––––––––––––
# Here is a guide on sliding windows I have based on the section of my dsa course on sliding windows

# Give me a guide now for prefix sum that follows the format of the sliding window guide exactly in terms of spacing / format/ etc. Im going to copy and paste your answer into a .py file

# Use of lines to separate example problems

# as you will notice my guide is almost entirely just based of the pseudocode and examples given
# you can include additional information. if you choose to do this include at a cheatsheet at the bottom of the guide after the examples and only include the absolute. most important info concisely in a simple excellent way for me to quickly understand the most important things you think i should have 




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