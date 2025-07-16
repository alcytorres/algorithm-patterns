# 344: Reverse a String

# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 
# Solution: https://leetcode.com/problems/reverse-string/editorial/


def reverseString(s):
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

string = ["h","e","l","l","o"]
print(reverseString(string))


# Time: O(n) - Performs n/2 swaps for an array of length n, with each swap being O(1).
# Space: O(1) - Uses only two integer pointers (left, right), modifying the input array in-place with no additional data structures.


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Shortcut solution

def reverseString(s):
    s.reverse    
    return s

string = ["h","e","l","l","o"]
print(reverseString(string))


# Time: O(n) - Python's list.reverse() method processes n elements, performing n/2 swaps internally, each O(1).
# Space: O(1) - Modifies the input array in-place, using only a constant amount of auxiliary space for internal operations.