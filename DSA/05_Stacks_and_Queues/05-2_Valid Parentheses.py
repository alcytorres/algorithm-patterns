# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
    # 1. Open brackets must be closed by the same type of brackets.
    # 2. Open brackets must be closed in the correct order.
    # 3. Every close bracket has a corresponding open bracket of the same type.

# Solution: https://leetcode.com/problems/valid-parentheses/description/

# Example 1:
    # Input: s = "()"
    # Output: true

# Example 2:
    # Input: s = "()[]{}"
    # Output: true

# Example 3:
    # Input: s = "(]"
    # Output: false

# Example 4:
    # Input: s = "([])"
    # Output: true

# Example 5:
    # Input: s = "([)]"
    # Output: false




def isValid(self, s: str) -> bool:
    stack = []
    matching = {"(": ")", "[": "]", "{": "}"}
    
    for c in s:
        if c in matching: # if c is an opening bracket
            stack.append(c)
        else:
            if not stack:
                return False
            
            previous_opening = stack.pop()
            if matching[previous_opening] != c:
                return False

    return not stack


s = "([])"
print(isValid(s))  # Output: True

s = "([)"
print(isValid(s))  # Output: False