# ============================================================
# Stacks
# ============================================================

# Always check if the stack is empty when about to pop() a character
# Never pop a char if the stack is empty


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Stack Declaration: we will just use a list
stack = []

# Pushing elements:
stack.append(1)
stack.append(2)
stack.append(3)

# Popping elements:
stack.pop() # 3
stack.pop() # 2

# Check if empty
not stack # Fal

# Check element at top
stack[-1] # 1

# Get size
len(stack) # 1


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Stack Operations Demo (Push, Pop, Peek, and Check Empty)

stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print(stack.pop())
print(stack.pop())
print(stack.pop())

stack.append(5)

if not stack:
    print("Stack is empty!")
else:
    print(f"Stack is not empty, top is: {stack[-1]}")



# -----------------------------------------------------------
# Stack Pattern: “Process with Memory”
"""
Used for: removing pairs, validating parentheses, monotonic stacks.
Push when needed, pop when rule breaks.
"""

def remove_adjacent_dups(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return "".join(stack)