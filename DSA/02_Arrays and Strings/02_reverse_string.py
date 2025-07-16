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


# Complexity
# Time: O(n) - Performs n/2 swaps to reverse n elements.
# Space: O(1) - Uses two pointers, modifying list in-place with no extra space used.




# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Shortcut solution

def reverseString(s):
    s.reverse    
    return s

string = ["h","e","l","l","o"]
print(reverseString(string))


# Complexity
# Time: O(n) - Reverses n elements with n/2 swaps.
# Space: O(1) - Modifies list in-place with constant extra space.


