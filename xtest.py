# -----------------------------------------------------------------
# # Cocise explain the difference 

# # Validating user input with try/except
# try:
#     user_input = input("Enter a number: ")  # Gets user input as string
#     number = int(user_input)  # Tries to convert to integer
#     print(f"Success! Your number is {number}.")  # Outputs integer
# except ValueError:
#     print("Error: Please enter a valid number, not text.")  # Catches non-integer input

# # Validating user input with isnumeric()
# user_input = input("Enter a number: ")  # Gets user input as string
# if user_input.isnumeric():  # Checks if input is numeric digits
#     print(f"Success! Your number is {user_input}.")  # Outputs string
# else:
#     print("Error: Please enter a valid number, not text.")  # Handles non-numeric input



# -----------------------------------------------------------------
# Stack Guide: From Zero to Proficiency
# A beginner-friendly guide to mastering the Stack data structure in Python.

# Definition and Purpose
# A Stack is a Last In, First Out (LIFO) data structure, like a pile of plates where you add and remove from the top.
# Used for tasks requiring reversal, backtracking, or tracking recent items (e.g., undo feature, function call stack).

# Key Operations
# - Push: Add item to top (O(1))
# - Pop: Remove and return top item (O(1))
# - Peek: View top item without removing (O(1))
# - Is Empty: Check if stack is empty (O(1))

# Simple Implementation
# Uses Python list as a stack with append() for push and pop() for pop.
class Stack:
    def __init__(self):  # Initialize empty stack
        self.items = []
    
    def push(self, item):  # Add item to top
        self.items.append(item)
    
    def pop(self):  # Remove and return top item
        if not self.is_empty():  # Handle empty stack
            return self.items.pop()
        raise IndexError("Pop from empty stack")
    
    def peek(self):  # View top item
        if not self.is_empty():  # Handle empty stack
            return self.items[-1]
        raise IndexError("Peek from empty stack")
    
    def is_empty(self):  # Check if stack is empty
        return len(self.items) == 0

# Example usage
stack = Stack()
stack.push(1)  # Push 1
stack.push(2)  # Push 2
print(stack.pop())  # Outputs: 2 (removes top item)
print(stack.peek())  # Outputs: 1 (views top item)
print(stack.is_empty())  # Outputs: False (stack not empty)
stack.pop()  # Remove 1
print(stack.is_empty())  # Outputs: True (stack now empty)

# DSA Applications
# Stacks are used in algorithms for:
# 1. Expression Parsing: Evaluate expressions like "3 + (4 * 5)" using a stack to track parentheses.
# 2. Backtracking: Solve problems like maze navigation by storing previous steps.
# Example LeetCode Problems:
# - Valid Parentheses (LeetCode #20): Check if brackets are balanced.
#   Solution: Push opening brackets, pop to match closing brackets.

def isValid(s):
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in brackets.values():
            stack.append(c)
        elif c in brackets and (not stack or stack.pop() != brackets[c]):
            return False
    return not stack
print(isValid("()[]{}"))  # Outputs: True

# - Min Stack (LeetCode #155): Design a stack with O(1) minimum element retrieval.
#   Solution: Use two stacks—one for values, one for tracking minimums.

# Pros and Cons
# Pros:
# - Simple and fast (O(1) for push, pop, peek).
# - Ideal for LIFO tasks like undo or recursion.
# Cons:
# - Limited access (only top item available).
# - Not suitable for searching or random access (use lists or arrays instead).

# Practice Problems
# 1. Valid Parentheses (LeetCode #20): Check if a string of brackets is balanced.
# 2. Min Stack (LeetCode #155): Implement a stack that tracks the minimum element.
# 3. Reverse Polish Notation (LeetCode #150): Evaluate expressions using a stack.



# -----------------------------------------------------------------
# longest_unique_substring.py

"""
# Longest Substring with At Most K Distinct Characters
Task: Given a string s and an integer k, find the length of the longest substring that contains at most k distinct characters. If the string is empty or k is 0, return 0.

Example 1: s = "eceba", k = 2 → 3 (substring "ece" has 2 distinct characters: 'e', 'c')

Example 2: s = "aa", k = 1 → 2 (substring "aa" has 1 distinct character: 'a')

Example 3: s = "aabbcc", k = 2 → 4 (substring "aabb" or "bbcc" has 2 distinct characters: 'a', 'b' or 'b', 'c')

    Generic dynamic sliding-window template.
    - arr: list of ints (or chars, as numbers)
    - K: problem parameter (e.g. target sum, max distinct count, etc.)
    Returns:
    - result: depends on problem (max window length, min window length, count, sum, etc.)
"""

# Test cases
print(longest_substring_k_distinct("eceba", 2))    # Output: 3
print(longest_substring_k_distinct("aa", 1))       # Output: 2
print(longest_substring_k_distinct("aabbcc", 2))   # Output: 4



def length_of_longest_substring(s):
  
    # 1️⃣ Initialize pointers & tracking variables
    left = 0
    max_len = 0
    char_count = {}  # freq map: char → how many times it appears in window

    # 2️⃣ Expand window by moving `right`
    for right in range(len(s)):
        current_char = s[right]
        # └── include s[right] in our window
        char_count[current_char] = char_count.get(current_char, 0) + 1

        # 3️⃣ Shrink window while it’s invalid (we have a duplicate)
        while char_count[current_char] > 1:
            # └── remove s[left] before we move left forward
            left_char = s[left]
            char_count[left_char] -= 1
            left += 1

        # 4️⃣ Update result for a max-length problem
        window_len = right - left + 1
        if window_len > max_len:
            max_len = window_len

    # 5️⃣ Return final answer
    return max_len


print(length_of_longest_substring("abcabccc"))  # Output: 3 ("abc")
print(length_of_longest_substring("aa"))        # Output: 1 ("a")
print(length_of_longest_substring("aabbcc"))    # Output: 2 ("ab" or "bc")
print(length_of_longest_substring("eceba"))     # Output: 4 ("ceba")



