# What is point of this from typing import List



"""
Review common_algorithms.py 

Check on CLAUDE if the examples at the bottom of 09-0_Binary Search.py are worth knowing or if the 2 I practice are enough

Run operators.py guide through Claude to make it better? maybe more examples 
"""




class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return s
        
        
        s = ["h","e","l","l","o"]
        print(reversString(s))
        # Output: ["0","l","l","e","h"]
        