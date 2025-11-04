

# Declaration: we will just use a list
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