"""
============================================
DETAILED SOLUTION BREAKDOWN
============================================
"""

# I need a super simple, easy to follow, beginner-friendly explanation of how this LeetCode solution works. Break it down into 4 main parts: 
# "Most IMPORTANT thing to Understand", 
# "Why this code Works, 
# TLDR (why this code works in one sentence), 
# and Quick Example Walkthrough.

# Make it crystal clear, focusing on why the code finds the correct answer for the given problem. I should be able to look back at this at any time and quickly follow along and understand it. 

# ⚠️ It is important you be concise and have no fluff in your reply. You should not sacrifice clarity, but if something can be said in fewer words without losing understanding, then use fewer words. This requires a delicate balance: always aim for maximum clarity with minimum words.

# Between each bullet point skip a line to space out the breakdown and make it more easy to scan

# Make sure to reply with a .py file so I can copy and paste your response

# Here is a great template with more detail of what I'm looking that you can you as a reference. While I want you to generanlly follow this template it is not rigit. If you think adding a little more detail to a specific problem is necessary for me to fully understand make sure to do that.

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

# 1133. Largest Unique Number
"""
Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.

Example:
    Input: nums = [1, 3, 9, 4, 9, 8, 3]
    Output: 8
    Explanation: The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it is the answer.
"""

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
# Output: 8 → Number 9 is largest but appears twice, so 8 is the next largest number that occurs only once.

# counts = {1:1, 3:2, 9:2, 4:1, 8:1}


# Example breakdown to reference: 
"""
---
Most IMPORTANT thing to Understand:
    • We need to find the largest number in the array that occurs exactly once.

    • First, we count how many times each number appears.

    • Then we check which numbers are unique (count == 1) and pick the largest one.

    • If no number is unique, we return -1.

---
Why this code Works:
    • Hash map (counts): stores how many times each number appears.

    • Scan through counts:
        • If a number's count == 1 → it's unique.
        • Compare with current max_unique and update if larger.

    • Efficiency: Instead of checking subarrays or sorting, we just tally counts in O(n) and then make one pass over the results.

    • Intuition: Think of it like a vote tally — each number “gets votes.” We only want numbers that got exactly one vote, and we pick the biggest of those.

---
TLDR
    • This solution works because we count how often each number appears, then pick the largest one that occurs exactly once.
    
---
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

# Leetcode problem for you to breakdown
# Paste here











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
# Solution: Two Pointers: Sequential Character Match
def is_subsequence(s, t):
    i = j = 0           

    while i < len(s) and j < len(t):
        if s[i] == t[j]:        
            i += 1
        j += 1                  

    return i == len(s)          

s = "ace"
t = "abcde"
print(is_subsequence(s, t))
# Output: True - "ace" appears in order within "abcde" as a subsequence.


# Example breakdown to reference: 
"""
---
Most IMPORTANT thing to Understand:
    • We need to check if every character in s appears in t in the same order.

    • The characters do NOT need to be next to each other.

    • Pointer i tracks where we are in s.

    • Pointer j tracks where we are in t.

    • If s[i] matches t[j], we found the next needed character, so we move i forward.

    • j always moves forward because we keep scanning through t.

---
Why this code Works:
    • Two pointers:
        • i = character we are trying to match in s.
        • j = character we are currently checking in t.

    • If s[i] == t[j]:
        • We found the next required character from s.
        • Move i forward to look for the next character.

    • If they do not match:
        • Only move j forward.
        • Keep searching through t.

    • Efficiency:
        • We scan each string once.
        • Time: O(n), where n is len(t).
        • Space: O(1).

    • Intuition:
        • Think of s as a checklist.
        • Think of t as a long sentence.
        • Every time you find the next checklist item in order, you check it off.

---
TLDR:
    • This solution works because it scans t from left to right and checks whether all characters in s can be found in order.

---
Quick Example Walkthrough:
    s = "ace"
    t = "abcde"

    Starting State:
        i = 0
        j = 0

        i points at s[0] = "a"
        j points at t[0] = "a"

    Loop Iteration 1:
        Compare:
            s[i] == t[j]
            "a" == "a" → MATCH

        Since they match:
            i += 1

        Now:
            i = 1

        Then this line ALWAYS runs:
            j += 1

        Now:
            j = 1

        Current state:
            i points at s[1] = "c"
            j points at t[1] = "b"

    --------------------------------------------------

    Loop Iteration 2:
        Compare:
            "c" == "b" → NO MATCH

        Since there is NO match:
            i does NOT move

        But j ALWAYS moves:
            j += 1

        Now:
            i = 1
            j = 2

        Current state:
            i points at s[1] = "c"
            j points at t[2] = "c"

    --------------------------------------------------

    Loop Iteration 3:
        Compare:
            "c" == "c" → MATCH

        Since they match:
            i += 1

        Now:
            i = 2

        Then j ALWAYS moves:
            j += 1

        Now:
            j = 3

        Current state:
            i points at s[2] = "e"
            j points at t[3] = "d"

    --------------------------------------------------

    Loop Iteration 4:
        Compare:
            "e" == "d" → NO MATCH

        i stays the same.

        j moves:
            j += 1

        Now:
            i = 2
            j = 4

        Current state:
            i points at s[2] = "e"
            j points at t[4] = "e"

    --------------------------------------------------

    Loop Iteration 5:
        Compare:
            "e" == "e" → MATCH

        Move i:
            i += 1
            i = 3

        Move j:
            j += 1
            j = 5

    --------------------------------------------------

    Final Check:
        i == len(s)
        3 == 3 → True

        This means:
            We successfully matched ALL characters in s in order.
"""


# LeetCode problem for you to breakdown
# Paste here
