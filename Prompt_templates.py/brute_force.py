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


Add the complexity explanation exactly like this style:

# Time: O(...)
# - Explain why in simple bullets
# - Mention loop counts or operations

# Space: O(...)
# - Mention variables or structures used
# - Keep explanation concise


Add a final section:
# Overview for Each Iteration

Show a **simple high-level walkthrough of how the algorithm works** on the example input.

Use a readable step format like:

# i = ...
# j = ...
# subarray / substring / value being checked
# updates to ans

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

# Time: O(N^2)
# - The loop runs n times.
# - Each time we do: reversed_s = c + reversed_s
# - String concatenation creates a new string each time (O(N)).
# - Overall: O(N * N) = O(N^2) time.

# Space: O(N)
# - We create a new string 'reversed_s' the same size as s.
# - Overall: O(N) space.


# Overview for Each Iteration
# s = "racecar"

# reversed_s starts = ""

# read 'r' → reversed_s = "r"
# read 'a' → reversed_s = "ar"
# read 'c' → reversed_s = "car"
# read 'e' → reversed_s = "ecar"
# read 'c' → reversed_s = "cecar"
# read 'a' → reversed_s = "acecar"
# read 'r' → reversed_s = "racecar"

# compare reversed_s == s
# "racecar" == "racecar" → True
