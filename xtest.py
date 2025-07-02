# Basic try/except
t = (1, 2, 3)
try:
    t[0] = 1  # Raises TypeError
except:
    print("caught it")  # Outputs: caught it

# Try/except with multiple statements
try:
    print("hi")
    t[0] = 1  # Raises TypeError
    print("hello")  # Skipped
except:
    print("caught it")  # Outputs: hi, caught it

# Specific error catching
try:
    t[0] = 1  # Raises TypeError
except TypeError:
    print("caught it")  # Outputs: caught it

# Wrong error type
try:
    t[0] = 1  # Raises TypeError
except SyntaxError:
    print("caught it")  # TypeError: not caught, program crashes

# Syntax error cannot be caught
try:
    t[0] === 1  # SyntaxError: invalid syntax (cannot be caught)
except SyntaxError:
    print("caught it")
