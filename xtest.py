# # Using enumerate to get index and item
# fruits = ["apple", "banana", "cherry"]
# for index, fruit in enumerate(fruits):
#     # print(index, fruit)
# # Outputs:
# # 0 apple
# # 1 banana
# # 2 cherry



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
