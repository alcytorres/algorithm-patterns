# Ask Claude, Grok, ChatGPT to name the top 50 most common DSA problems you rec I know.
# In the prompt find a way to include the ones you already have pracitced



# Organize mini guides doc. Delete the bottom part that says delete

# how do you know to do this ans = [0] * n   ?
# its not something intuitive. be realistic how you would think of that or if thats just comes down to memory?

# Review slicing arrays




#   a = (b × whole times) + leftover

# n % 10   # get the last digit
# n // 10  # remove the last digit



# What is point of this from typing import List

"""
Review common_algorithms.py 

Check on CLAUDE if the examples at the bottom of 09-0_Binary Search.py are worth knowing or if the 2 I practice are enough

Run operators.py guide through Claude to make it better? maybe more examples 
"""






# Example 2: Longest Substring with At Most One "0"
"""
Finds the longest substring with at most one "0" by flipping at most one "0" to "1". 

In other words "what is the longest substring that contains at most one "0"?

Example:
    Input: s = "10101"
    Output: 3
    Explanation: "101" is the longest substring containing at most one "0".
"""


from methods import it


def longest_substring_one_zero(s):
    l = curr = ans = 0

    for r in range(len(s)):
        if s[r] == "0":
            curr += 1
        
        while curr > 1:
            if s[l] == "0":
                curr -= 1
            l += 1
        
        ans = max(ans, r-l+1)
    
    return ans

s = "10101"
print(longest_substring_one_zero(s))
# Output: 3  →  Substring "101" (length 3) is the longest with at most one "0".

Double check the explanation for time complexity. It says how each character is visited a constant number of times. I need to ask about clarifying this because the right pointer scans through every character in the string, but the left pointer also scans through them. So when it says each character is visited a constant number of times, is it okay that each character is visited, could be visited more than once if the left pointer also visits it? Just help me clarify this wording to make it crystal clear, easy to understand, consistent with the other timing complexities that have been provided. That have been provided in this project of Leaco problems.


is this another way to say it        
• l only moves forward, never backward — each character is added and removed at most once.


