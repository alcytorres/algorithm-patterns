

# What is point of this from typing import List


# ––––––––––––––––––––––––––––––––––––––––––––––
# EverQuote Interview Question

"""
Task: Parse a string containing infix operators and values, do the math evaluation and print the result

Example input: 1 + 2 * 10  |  output: 21

Inflix operators can be only + or * or -

expr = expression 
"""

def fn(s):
    return eval(s)

# Example usage
s = "1 + 3 * 10"
print(fn(s))  # Output: 31

# Time complexity:O(n) – where n is the length of the string
# Space complexity:O(1) – constant extra space (not counting the input string)




def fn(s):
    s = s.replace(' ', '')        # "1 + 3* 10" → "1+3*10"
    parts = s.split('+')          # ["1", "3*10"]
    total = 0
    for part in parts:
        if '*' in part:
            nums = part.split('*')  # "3*10" → ["3", "10"]
            val = 1
            for n in nums:
                val *= int(n)       # 3 * 10 = 30
            total += val
        else:
            total += int(part)      # just add the number
    return total

# === Test ===
s = "1 + 3 * 10"
print(fn(s))  # 31

# More examples:
# print(fn("2 + 5"))         # 7
# print(fn("4 * 5 + 2 * 3")) # 26
# print(fn("10"))            # 10


# Time: O(n) – we look at each character once.
# Space: O(n) – we keep two short lists that together are at most the size of the input.





# def fn(s):
#     # Find the operator (+, -, *, /)
#     for op in "+-*/":
#         if op in s:
#             left, right = s.split(op)
#             left, right = int(left), int(right)

#             if op == "+": return left + right
#             if op == "-": return left - right
#             if op == "*": return left * right
#             if op == "/": return left // right  # integer division

# # Example
# print(fn("1+2"))   # 3
# print(fn("7*5"))   # 35
# print(fn("10-3"))  # 7
# print(fn("8/2"))   # 4


