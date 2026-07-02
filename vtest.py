# What is point of this from typing import List


"""
Review common_algorithms.py 

Check on CLAUDE if the examples at the bottom of 09-0_Binary Search.py are worth knowing or if the 2 I practice are enough

Run operators.py guide through Claude to make it better? maybe more examples 
"""





# 344. Reverse String
"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
    Input: s = ["h","e","l","l","o"]
    Output:    ["o","l","l","e","h"]
 
Solution: https://leetcode.com/problems/reverse-string/editorial/
"""

# Solution: Two Pointers In-Place Reverse

def reverseString(s):
    l = 0
    r = len(s) - 1

    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    
    return s

s = ["h", "e", "l", "l", "o"]
print(reverseString(s))  
# Output: ["o", "l", "l", "e", "h"]


# l 0 | 1|2
# r 4 | 3|2
# condition T|T

# s
# ["h", "e", "l", "l", "o"]
# ["o", "e", "l", "l", "h"]
# ["o", "l", "l", "e", "h"]