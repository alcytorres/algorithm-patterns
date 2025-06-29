# Python Guide
# Tutorial: https://www.youtube.com/watch?v=NakyjvSrTIQ
# Grok notes: https://grok.com/chat/d75c2885-2cd7-47e5-a46c-37e60661c914
# Environment: Examples use Google Colab, but code is compatible with any Python environment (e.g., VS Code)
# Table of Contents
# 0:00:00 Introduction
# 0:10:53 Math Operations
# 0:17:51 Variables
# 0:20:26 Booleans / Conditions
# 0:27:55 If Statements
# 0:31:10 Introduction to Lists
# 0:33:24 For Loops      ***Review Important***
# 0:41:35 While Loops
# 0:47:30 If / Elif / Else
# 0:56:40 Functions
# 1:11:15 Is             ***Review Important***
# 1:27:13 Cool Function Tricks
# 1:34:27 File Reading / Writing    ***Skipped review later***
# 1:42:33 Objects and Classes.   ***Review Important***
# 1:56:00 Comments / Docstrings
# 2:03:55 Lists in Detail
# 2:08:58 Dictionaries
# 2:17:02 Strings in Detail
# 2:27:47 Tuples
# 2:30:35 Sets
# 2:34:33 Errors / Try / Except
# 2:38:35 User Input
# 2:41:18 List Comprehension
# 2:49:13 ASCII / Ord / Chr
# 2:53:50 Modules / Pip / Packages
# 2:57:52 Python Scripts / Files
# 3:04:11 Local Python
# 3:07:38 Conclusion


# ----------------------------------------------------------------------------------
# 0:00:00 Introduction

# Key Points:
# - Python is a high-level, interpreted language used for web development, data science, and automation.
# - Strings are text data, enclosed in single ('') or double ("") quotes; they signal Python to treat content as text.
# - Google Colab is a convenient environment; no setup needed beyond creating a notebook at colab.research.google.com.
# - In Colab, the last line of a cell outputs automatically without print(), but print() is explicit and omits quotes in output.
# - Data types matter: strings ("23") are different from numbers (23), affecting operations like addition.

# Example: Printing "Hello, World" (traditional first program)
print("Hello, World")  # Outputs: Hello, World

# Strings with single or double quotes are equivalent
print('Hello, World')  # Outputs: Hello, World

# Including quotes in output requires nesting quotes
print('"Hello, World"')  # Outputs: "Hello, World"

# Mixing text and numbers in a string
print("Hello, World 7")  # Outputs: Hello, World 7

# Checking data type with type()
print(type("Hello, World 7"))  # Outputs: <class 'str'> (string)

# Strings vs. numbers: "23" is text, 23 is a number
print("23" + "4")  # Outputs: 234 (string concatenation)
print(23 + 4)      # Outputs: 27 (numeric addition)

# Errors: Unsupported operations
print("hello" - "hi")  # TypeError: unsupported operand type(s) for -: 'str' and 'str'
print("hi)  # SyntaxError: EOL while scanning string literal (missing quote)


# ----------------------------------------------------------------------------------
# 0:10:53 Math Operations

# Key Points:
# - Python supports standard math operations: addition (+), subtraction (-), multiplication (*), division (/), and exponentiation (**).
# - Division (/) always returns a float, even for whole numbers (e.g., 1/1 = 1.0).
# - Integer division (//) returns the quotient as an integer; modulo (%) returns the remainder.
# - Integers (int) are whole numbers; floats (float) are decimals.
# - Operations between strings and numbers (e.g., "23" + 4) cause errors unless types are compatible.

# Basic arithmetic
print(3 + 2)    # Outputs: 5 (int)
print(3.2 + 4.7)  # Outputs: 7.9 (float)
print(4 - 3)    # Outputs: 1 (int)
print(3.2 - 1.0)  # Outputs: 2.2 (float)
print(4 * 3)    # Outputs: 12 (int)
print(2.1 * 3.2)  # Outputs: 6.72 (float)

# Division: Always returns float
print(4 / 3)    # Outputs: 1.3333333333333333 (float)
print(1 / 1)    # Outputs: 1.0 (float)
print(3.2 / 1.6)  # Outputs: 2.0 (float)

# Integer division and modulo
print(5 // 2)   # Outputs: 2 (quotient, int)
print(5 % 2)    # Outputs: 1 (remainder, int)
print(7 % 3)    # Outputs: 1 (remainder, int)

# Exponentiation
print(5 ** 2)   # Outputs: 25 (5 squared)
print(5 ** 3)   # Outputs: 125 (5 cubed)

# Checking types
print(type(3 + 2))      # Outputs: <class 'int'>
print(type(3.2 + 4.7))  # Outputs: <class 'float'>


# ----------------------------------------------------------------------------------
# 0:17:51 Variables

# Key Points:
# - Variables store data and are created with a name (e.g., y) and value (e.g., 5) using =.
# - Variable names must be defined before use, or a NameError occurs.
# - Python is dynamically typed: variables can change types (e.g., from int to str) during execution.
# - Variables allow flexible data manipulation, unlike literals (e.g., 3 = 2 is invalid).

# Creating and using variables
y = 5
print(y)  # Outputs: 5

# Changing variable value
y = 4
print(y)  # Outputs: 4

# Changing variable type
y = "tree"
print(y)  # Outputs: tree

# Error: Using undefined variable
print(x)  # NameError: name 'x' is not defined

# Invalid assignment
3 = 2  # SyntaxError: can't assign to literal


# ----------------------------------------------------------------------------------
# 0:20:26 Booleans / Conditions

# Key Points:
# - Booleans (bool) have only two values: True or False (case-sensitive, not strings).
# - Comparison operators (<, >, <=, >=, ==, !=) produce booleans based on logical truth.
# - The not operator flips a boolean (not True = False, not False = True).
# - == checks equality; = is for assignment. Use == for comparisons to avoid errors.
# - Comparisons work for numbers and strings, but string comparisons beyond == are less common.

# Boolean values
print(True)   # Outputs: True
print(False)  # Outputs: False
print(type(True))  # Outputs: <class 'bool'>

# Comparison operators
print(4 < 3)      # Outputs: False
print(4 > 3)      # Outputs: True
print(3 >= 2)     # Outputs: True
print(3 <= 2)     # Outputs: False
print(2 <= 2)     # Outputs: True
print(2 >= 2)     # Outputs: True
print(2 != 3)     # Outputs: True
print(3 == 2)     # Outputs: False

# String comparisons
print("hi" == "hello")  # Outputs: False
print("hi" == "hi")    # Outputs: True

# Not operator
print(not True)   # Outputs: False
print(not False)  # Outputs: True

# Error: Single = in comparison
print(3 = 2)  # SyntaxError: can't assign to literal


# ----------------------------------------------------------------------------------
# 0:27:55 If Statements

# Key Points:
# - If statements execute code blocks based on a boolean condition (True = execute, False = skip).
# - Syntax: `if condition:`, followed by indented code (auto-indented in Colab; typically 4 spaces).
# - Indented code runs only if the condition is True; non-indented code runs regardless.
# - Use variables in conditions (e.g., `x > 7`) for dynamic logic, as hard-coded True/False is less practical.

# Basic if statement
if True:
    print(1)  # Outputs: 1
    print(2)  # Outputs: 2
print(3)  # Outputs: 3 (runs regardless)

# If statement with False condition
if False:
    print(1)  # Skipped
    print(2)  # Skipped
print(3)  # Outputs: 3

# If with condition and variable
x = 7
if x > 7:
    print(1)  # Skipped (7 is not > 7)
    print(2)  # Skipped
print(3)  # Outputs: 3

x = 9
if x > 7:
    print(1)  # Outputs: 1
    print(2)  # Outputs: 2
print(3)  # Outputs: 3


# ----------------------------------------------------------------------------------
# 0:31:10 Introduction to Lists

# Key Points:
# - Lists store multiple items in order, defined with square brackets: `[item1, item2, ...]`.
# - Items can be added using `append()` (modifies the list in place) or by redefining the list.
# - Lists are of type `list`; an empty list `[]` is valid.
# - Access items via indexing: `list[index]`, where index starts at 0 (e.g., `list[0]` is the first item).
# - Indexing out of range (e.g., `list[5]` for a 5-item list) raises an IndexError.

# Creating a list
grocery_list = ["banana", "orange"]
print(grocery_list)  # Outputs: ['banana', 'orange']

# Redefining the list with additional item
grocery_list = ["banana", "orange", "blueberries"]
print(grocery_list)  # Outputs: ['banana', 'orange', 'blueberries']

# Appending an item
grocery_list.append("fruit")
print(grocery_list)  # Outputs: ['banana', 'orange', 'blueberries', 'fruit']

# Checking list type
print(type(grocery_list))  # Outputs: <class 'list'>
print(type([]))  # Outputs: <class 'list'> (empty list)

# Indexing
print(grocery_list[0])  # Outputs: banana
print(grocery_list[1])  # Outputs: orange
print(grocery_list[2])  # Outputs: blueberries
print(grocery_list[3])  # Outputs: fruit
print(grocery_list[5])  # IndexError: list index out of range


# ----------------------------------------------------------------------------------
# 0:33:24 For Loops

# Key Points:
# - For loops iterate over items in a sequence (e.g., list, range).
# - Syntax: `for variable in sequence:`, followed by indented code.
# - Iterate directly over list items (`for item in list`) or indices (`for i in range(len(list))`).
# - `range(n)` generates numbers from 0 to n-1; `len(list)` gives the list's length.
# - `enumerate(list)` provides both index and item for iteration.
# - Indexing starts at 0; last valid index is `len(list) - 1`.

# Background to Know:
# range(5) is a Python object, not a list. Printing it shows range(0, 5). Convert to list with list(range(5)) to see [0, 1, 2, 3, 4].
print(range(5))        # Output: range(0, 5)

# range(5) generates numbers 0 to 4. In a for loop, for i in range(5) iterates over 0, 1, 2, 3, 4, acting like [0, 1, 2, 3, 4].
print(list(range(5)))  # Output: [0, 1, 2, 3, 4]

# len() returns the number of items in grocery_list, which is 5.
print(len(grocery_list))  # Output: 5


# Iterating over list items
grocery_list = ["banana", "orange", "blueberries", "fruit", "four"]
for item in grocery_list:
    print(item)  # Outputs: banana, orange, blueberries, fruit, four (one per line)

# Iterating over indices with list
for i in [0, 1, 2, 3, 4]:  # list of indices
    print(grocery_list[i])  # Outputs: banana, orange, blueberries, fruit, four

# Iterating over indices with range
for i in range(5):  # range(5) = [0, 1, 2, 3, 4]
    print(grocery_list[i])  # Outputs: banana, orange, blueberries, fruit, four

# Using len() for dynamic range
for i in range(len(grocery_list)):
    print(grocery_list[i])  # Outputs: banana, orange, blueberries, fruit, four

# Using enumerate for index and item
for i, item in enumerate(grocery_list):
    print(i, item)  # Outputs: 0 banana, 1 orange, 2 blueberries, 3 fruit, 4 four


# ----------------------------------------------------------------------------------
# 0:41:35 While Loops

# Key Points:
# - While loops repeat code as long as a condition is True: `while condition:`.
# - Use increment (`i += 1`) or decrement (`j -= 1`) to update loop variables to avoid infinite loops.
# - Common for index-based iteration, especially when going backwards or with custom steps.
# - Condition must eventually become False, or the loop runs indefinitely.
# - Use `len(list) - 1` for the last valid index when iterating backwards.

# Incrementing example
i = 0
print(i)  # Outputs: 0
i += 1
print(i)  # Outputs: 1
i += 1
print(i)  # Outputs: 2

# Decrementing example
i = 2
i -= 1
print(i)  # Outputs: 1
i -= 1
print(i)  # Outputs: 0

# While loop: backward iteration
j = len(grocery_list) - 1  # Last valid index (4)
while j >= 0:
    print(grocery_list[j])  # Outputs: four, fruit, blueberries, orange, banana
    j -= 1
print("end")  # Outputs: end

# While loop: forward iteration
i = 0
while i < len(grocery_list):
    print(grocery_list[i])  # Outputs: banana, orange, blueberries, fruit, four
    i += 1
print("end")  # Outputs: end


# ----------------------------------------------------------------------------------
# 0:47:30 If / Elif / Else

# Key Points:
# - `elif` (else if) checks additional conditions if prior ones are False; `else` runs if all conditions are False.
# - Only the first True condition’s block executes; others are skipped, even if True.
# - Use `and` (both conditions True) or `or` (at least one True) to combine booleans.
# - Practical example: Categorize ages with conditions to handle edge cases carefully.
# - `and` requires both sides True; `or` needs only one side True.

# Basic if/elif/else
if True:
    print(1)
elif True:
    print(2)
else:
    print(3)  # Skipped; first True condition (if) runs

if False:
    print(1)
elif True:
    print(2)  # Outputs: 2
else:
    print(3)  # Skipped

if False:
    print(1)
elif False:
    print(2)
else:
    print(3)  # Outputs: 3

# Logical operators
print(True or True)   # Outputs: True
print(False or True)  # Outputs: True
print(True or False)  # Outputs: True
print(False or False) # Outputs: False

print(True and True)   # Outputs: True
print(False and True)  # Outputs: False
print(True and False)  # Outputs: False
print(False and False) # Outputs: False

# Combined conditions
print((3 > 4) and (4 < 5))  # Outputs: False (False and True)
print((3 > 4) or (4 < 5))  # Outputs: True (False or True)

# Practical age categorization
age = 15
if age < 1:
    print("newborn")
elif age >= 13 and age <= 19:
    print("teen")  # Outputs: teen
else:
    print("adult")

age = 0
if age < 1:
    print("newborn")  # Outputs: newborn
elif age >= 13 and age <= 19:
    print("teen")
else:
    print("adult")

age = 2
if age < 1:
    print("newborn")
elif age >= 13 and age <= 19:
    print("teen")
else:
    print("not newborn and not teen")  # Outputs: not newborn and not teen

age = 20
if age < 1:
    print("newborn")
elif age >= 13 and age <= 19:
    print("teen")
else:
    print("adult")  # Outputs: adult


# ----------------------------------------------------------------------------------
# 0:56:40 Functions

# Key Points:
# - Functions are defined with `def` to encapsulate reusable code, taking parameters and optionally returning values.
# - Syntax: `def function_name(parameter):` followed by indented code block; parameters are local to the function.
# - Scope: Parameters (e.g., `s`) exist only within the function (local scope); they don’t affect or access variables outside unless explicitly referenced.
# - Arguments vs. Parameters: Arguments are values passed when calling a function (e.g., `our_print("hi2")`); parameters are variables in the function definition that receive those values.
# - Return: Functions return a value with `return`; without `return`, they implicitly return `None`, which represents "nothing" and doesn’t output unless printed.
# - Side Effects: Functions can affect the outside environment (e.g., printing to terminal, modifying a list). Functions without side effects (e.g., returning a computed value) are safer for predictable behavior.
# - Example: A print-like function (`our_print`) demonstrates basic function creation, while `times_two` shows returning a value, and `append_four_to_list` illustrates side effects by modifying a list.

# Arguments vs. Parameters:
def add_nums(a, b):  # parameters: a, b
    print(a + b)
add_nums(1, 3)  # arguments: 1, 3

# Simple function mimicking print
def our_print(s):
    print(s)          # Prints the input string
    print(s + " hello")  # Concatenates and prints
print(our_print("hi"))  # Outputs: hi, hi hello

# Scope: Parameters are local
def our_print(s):  # s inside function is separate from any external s
    print(s + "hello")  
our_print("hi")  
print(s)  # NameError: s is not defined outside function

# Scope: Parameters are local
def our_print(s):
    print(s + " hello")  # s inside function is separate from any external s
our_print("hi")  
s = 87
our_print("hi")  #  Outputs: hi, hi hello
print(s)  # Outputs: 87; external s (87) is unchanged

# Accessing external variables
z = 42
def our_print(s):
    print(z)  # Accesses external z (42)
our_print("hi")  # Outputs: 42

# Accessing external variables: NameError:
def our_print(s):
    print(tree)  # NameError: tree is not defined (no external tree exists)
our_print("hi")  


# Simple function that returns None
    # By default a function returns None. 
    # None does not show unless you use print
def our_print(s):
    print(s + " hello")  # hi hello
print(our_print("hi"))  # Outputs: None
    # The function call our_print("hi") gets replaced with None.

# Simple function that returns None
    # By default a function returns None. 
    # None does not show unless you use print
def our_print(s):
    print(s + " hello")  # hi hello
our_print("hi")  # Outputs: None (now shown)
    # The function call our_print("hi") gets replaced with None.

# Simple function that returns None
# By default a function has this implicit/hidden return None. The retrun leaves the function and returns None. It mean you did not return anything as part of the function. 
def our_print(s):
    print(s + " hello")  # hi hello
    return None  # By default return None hidden (illustrative ex.).
our_print("hi")  # Outputs: None (now shown)
    # The function call our_print("hi") gets replaced with None.


# # Function with return
def times_two(x):
    return x * 2
print(times_two(5))  # Outputs: 10 (returns 5 * 2)
    # The function call times_two(5) gets replaced with 10.

# Function with side effect (modifying a list)
# Modifies input list because lists are mutable
def append_four_to_list(lst):
    lst.append(4)  # Modifies the input list
a = [1, 2, 3]
append_four_to_list(a)
print(a)  # Outputs: [1, 2, 3, 4] (list modified due to side effect)

# Function without side effect
# Returns new value without changing input because integers are immutable
def times_two(x):
    return x * 2
b = 4
times_two(b)
print(b)  # Outputs: 4 (b unchanged; times_two only returns a value)

# Function without side effect
def our_print(s):
    print(s + " hello")  
r = "hi"
our_print(r) # output: hi hello
print(r) # Output: hi

print(our_print(r))  # Outputs: hello, hellohello, None (function returns None)


# Very important to know if a function has a side effect

# ----------------------------------------------------------------------------------
# 1:11:15 Is

# Key Points:
# - The `is` operator checks if two variables refer to the same object in memory, not just equal values (unlike `==`).
# - Lists: Assigning `b = a` makes `b` and `a` refer to the same list; modifying one (e.g., `a[0] = 7`) affects both because they share the same memory.
# - Numbers: Assigning `w = q` creates a new integer object for `w`; changing `q` (e.g., `q = 7`) doesn’t affect `w` because integers are immutable and assignments create new objects.
# - Mutability: Lists are mutable (can be modified in place, affecting all references). Integers are immutable (changing creates a new object).
# - Copying: Use `copy.deepcopy()` to create a separate list copy, so changes to one don’t affect the other.
# - In Functions: Passing a list to a function passes a reference to the same object; modifying the list inside the function affects the original. Reassigning the parameter (e.g., `x = [1, 2]`) creates a new object, leaving the original unchanged.
# - Practical Impact: Use `is` to check identity when managing shared references (e.g., ensuring a function doesn’t unintentionally modify a list). For value equality, use `==`.

# Background: Function with side effect (modifying a list)
# Defined earlier; included for context as Greg references it
def append_four_to_list(lst):
    lst.append(4)  # Modifies the input list (mutable)
a = [1, 2, 3]
append_four_to_list(a)
print(a)  # Outputs: [1, 2, 3, 4] 

# List identity with is
a = [1, 2, 3, 4]
b = a  # b refers to the same list as a
print(a == b)  # Outputs: True (same values)
print(a is b)  # Outputs: True (same object)
print(a == [1, 2, 3, 4])  # Outputs: True (same values)

# a is [1, 2, 3, 4] is False because is checks for the same memory object, but a and [1, 2, 3, 4] are different objects despite equal values.
print(a is [1, 2, 3, 4])  # Outputs: False (different objects, same values)


# Modifying shared list
a[0] = 7
print(a)  # Outputs: [7, 2, 3, 4]
print(b)  # Outputs: [7, 2, 3, 4] (same object, reflects change)
b[2] = 12
print(a)  # Outputs: [7, 2, 12, 4] (same object, reflects change)
print(b)  # Outputs: [7, 2, 12, 4]

# Copying to avoid shared changes
from copy import deepcopy
a = [1, 2, 3, 4]
b = deepcopy(a)  # Separate copy
print(a)  # Outputs: [1, 2, 3, 4]
print(b)  # Outputs: [1, 2, 3, 4]
a[0] = 14
print(a)  # Outputs: [14, 2, 3, 4]
print(b)  # Outputs: [1, 2, 3, 4] (unchanged due to separate copy)

# Integer immutability
q = 5
w = q
print(q)  # Outputs: 5
print(w)  # Outputs: 5
q = 7
print(q)  # Outputs: 7
print(w)  # Outputs: 5 (w unaffected; integers are immutable)

# Function with integer reassignment
def add_one(x):
    x + 1  # Reassigns x to a new integer
    return x
print(add_one(4))  # Outputs: 5 (returns 4 + 1)

# Function with integer reassignment to a fixed value
def add_one(x):
    x = 8  # Reassigns x to a new integer
    return x + 1
print(add_one(4))  # Outputs: 9 (returns 8 + 1)

# Function with type change
def add_one(x):
    x = [1, 2]  # Reassigns x to a new list
    return x
print(add_one(4))  # Outputs: [1, 2]


# Function with list reassignment
def add_one(x):
    x = [1, 2]  
    return x
a = [1, 2, 3]
add_one(a)  # Returns [1, 2], no console output (return ignored)
            # You can double check by printing
print(a)  # Outputs: [1, 2, 3] (a unchanged; no side effect)

# Function checking identity with list
def add_one(x):
    print(x is a)  # True (x refers to same list as a)
    x = [1, 2]  # Reassigns x to a new list
    print(x is a)  # False (x now refers to a new object)
    return x   # Returns [1, 2]

a = [1, 2, 3]
add_one(a)  # Outputs: True, False (returns [1, 2], ignored)
print(add_one(a))  # Outputs: True, False, [1, 2] (shows return value)
print(a)  # Outputs: [1, 2, 3] (a unchanged) 


# Function with list modification
def add_one(x):
    x.append(4)  # Appends 4 to the input list
    x = [1, 2]  # Reassigns x to a new list
    print(x is a)  # Output: False (x and a are different objects)
    return x  # Returns [1, 2]

a = [1, 2, 3]
add_one(a)  # Outputs: False (returns [1, 2], ignored)
print(add_one(a))  # Outputs: False, [1, 2] (shows return value)
print(a)  # Outputs: [1, 2, 3, 4, 4] (a modified by append)


# Function with list modification
def add_one(x):
    x = [1, 2]  # Reassigns x to a new list
    print(x is a)  # Outputs: False (x and a are different objects)
    x.append(4)  # Appends 4 to the new list x
    return x  # Returns [1, 2, 4]

a = [1, 2, 3]
add_one(a)  # Outputs: False (returns [1, 2, 4], no console output)
print(add_one(a))  # Outputs: False, [1, 2, 4] (shows return value)
print(a)  # Outputs: [1, 2, 3] (a unchanged)


# ----------------------------------------------------------------------------------
# 1:27:13 Cool Function Tricks

# Key Points:
# - Default Parameters: Parameters can have default values (e.g., `b=4`), making them optional. Defaults must come after required parameters to avoid errors.
# - Keyword Arguments: Specify arguments by name (e.g., `a=4`) in any order, overriding defaults. Mixing positional and keyword arguments is allowed but can cause errors if ambiguous (e.g., multiple values for a parameter).
# - Best Practice: Use either all positional arguments (in order) or all keyword arguments to avoid confusion. Mixing requires careful ordering to prevent errors like `multiple values for argument`.
# - Practical Use: Default parameters simplify function calls; keyword arguments improve readability and flexibility, especially for functions with many parameters.
# - Pitfalls: Ensure required parameters precede defaults in the function definition. Avoid mixing positional and keyword arguments unless necessary to prevent errors.

# Function with multiple parameters
def add(a, b, c):
    return a + b + c
print(add(5, 9, 2))  # Outputs: 16 (5 + 9 + 2)

# Error: Missing required argument
def add(a, b, c):
    return a + b + c
print(add(5, 9))  # TypeError: add() missing 1 required positional argument: 'c'

# Function with default parameter
def add(a, b, c=4):
    return a + b + c
print(add(5, 9))  # Outputs: 18 (5 + 9 + 4, default c=4)
print(add(5, 9, 2))  # Outputs: 16 (5 + 9 + 2, overrides c)

# Function with multiple default parameters
def add(a, b=4, c=5, d=2):
    return a + b + c + d
print(add(1))  # Outputs: 12 (1 + 4 + 5 + 2)
print(add(1, 2))  # Outputs: 10 (1 + 2 + 5 + 2)

# Error: Non-default argument after default
def add(a=2, b):
    return a + b  # SyntaxError: non-default argument follows default argument
print(add(1, 2))  # Outputs: 10 (1 + 2 + 5 + 2)

# Function with default parameter (corrected)
def add(a, b=4):
    return a + b
print(add(2))  # Outputs: 6 (2 + 4)
print(add(2, 5))  # Outputs: 7 (2 + 5, overrides b)

# Function with multiple defaults
def add(a, b=4, c=5):
    return (a * b) + c
print(add(2))  # Outputs: 13 (2 * 4 + 5)
print(add(2, 5))  # Outputs: 15 (2 * 5 + 5)
print(add(2, 5, 4))  # Outputs: 14 (2 * 5 + 4)

# # Keyword arguments
print(add(a=4))  # Outputs: 21 (4 * 4 + 5)
print(add(a=4, b=10, c=4))  # Outputs: 44 (4 * 10 + 4)
print(add(b=10, c=4, a=4))  # Outputs: 44 (4 * 10 + 4, order irrelevant)
print(add(c=2, a=5))  # Outputs: 22 (5 * 4 + 2)
print(add(10, c=4))  # Outputs: 44 (10 * 4 + 4)

# Error: Multiple values for argument
print(add(10, a=4))  # TypeError: add() got multiple values for argument 'a'
print(add(10, c=4, a=4))  # TypeError: add() got multiple values for argument 'a'

# Correct mixing of positional and keyword
def add(a, b=4, c=5):
    return (a * b) + c
print(add(10, 3))  # Outputs: 35 (10 * 3 + 5)
print(add(a=10, b=3))  # Outputs: 35 (10 * 3 + 5)
print(add(10, b=4, c=4))  # Outputs: 44 (10 * 4 + 4)


# ----------------------------------------------------------------------------------
# 1:34:27 File Reading / Writing

# Key Points:
# - Reading Files: Use `with open(path, 'r') as f:` to safely read files. `f.readlines()` returns a list of lines (including `\n`); `f.read()` returns the entire file as a string; looping (`for line in f`) reads line by line, ideal for large files.
# - Writing Files: Use `with open(path, 'w') as f:` to overwrite a file with `f.write()`. Use `'a'` mode to append instead of overwriting.
# - Newlines: Files don’t automatically add `\n` when writing; add explicitly for new lines. Use `line.rstrip()` to remove trailing `\n` when reading line by line.
# - File Paths: In Colab, use simple paths (e.g., `a_test.txt`) if files are in the current directory. Use `!ls` to check available files.
# - Best Practices: Always use `with` to ensure files are properly closed. Append mode (`'a'`) preserves existing content; write mode (`'w'`) overwrites. Line-by-line reading is memory-efficient for large files.
# - Setup: The example assumes a file `a_test.txt` with content: "hello there\n42\n35\n76\n,is comma the end".

# Reading a file
    # Opens a_test.txt in read mode and prints all lines as a list of strings, including newlines.
p = "a_test.txt"
with open(p, 'r') as f:
    print(f.readlines())  # Outputs: ['hello there\n', '42\n', '35\n', '76\n', ',is comma the end\n']

# Reading entire file as a string
with open(p, 'r') as f:
    print(f.read())  # Outputs: hello there\n42\n35\n76\n,is comma the end

# Reading lines iteratively
with open(p, 'r') as f:
    for line in f:
        print(line)  # Outputs: hello there, 42, 35, 76, ,is comma the end (one per line)

# Reading lines without trailing newlines
with open(p, 'r') as f:
    for line in f:
        print(line.rstrip())  # Outputs: hello there, 42, 35, 76, ,is comma the end (no trailing \n)

# Writing to a file
with open("newfile.txt", 'w') as f:
    f.write("hello")  # Overwrites file with "hello"
# File content: hello

# Overwriting file content
with open("newfile.txt", 'w') as f:
    f.write("hi")  # Overwrites file with "hi"
# File content: hi

# Appending to file
with open("newfile.txt", 'a') as f:
    f.write("hello")  # Appends "hello" to file
# File content: hihello

# Appending with newline
with open("newfile.txt", 'a') as f:
    f.write("\nhello")  # Appends "\nhello" to file
# File content: hi\nhello


# ----------------------------------------------------------------------------------
# 1:42:33 Objects and Classes

# Key Points:
# - A class is a blueprint (or "factory") for creating objects, which are instances of the class.
# - Objects are instances of a class, holding data (attributes) and behaviors (methods).
# - Syntax: `class ClassName:` defines a class; `__init__` is the constructor method to initialize objects.
# - self: Refers to the instance of the class within its methods, allowing access to its attributes (e.g., `self._age`).
# - Attributes (e.g., `_age`, `_name`) store data; methods (e.g., `__str__`, `older_younger_than`) define actions.
# - Special Methods: `__str__` and `__repr__` control string representations for `print()` and direct output (e.g., in Colab).
# - Dot Notation: Access attributes/methods with `object.attribute` or `object.method()`.
# - Underscores: Single underscores (e.g., `_age`) suggest private attributes (convention, not enforced); double underscores (e.g., `__str__`) are special methods.
# - Practical Use: Classes model real-world entities (e.g., a `Human` with name and age); methods add functionality (e.g., comparing ages).
# - Pitfalls: Forgetting `self` in methods causes errors; string concatenation with non-strings (e.g., integers) requires conversion (e.g., `str()`).
# - Example: The `Human` class demonstrates creating objects with attributes and methods, including custom string output and age comparison.

# Defining Human class with basic constructor
class Human:
    def __init__(self, age, name):  # Initialize object with age and name attributes
        self._age = age  # Store age as attribute
        self._name = name  # Store name as attribute

# Creating a Human object
h = Human(age=4, name="greg")  # Instantiate Human with age 4 and name "greg"
print(h)  # Outputs: <main.Human object at ...> (default representation)

# Adding __str__ method
class Human:
    def __init__(self, age, name):
        self._age = age
        self._name = name
    
    def __str__(self):
        return "hi"  # Temporary string representation

# Creating a Human object
h = Human(age=4, name="greg")  
print(h)  # Outputs: hi (if redefined)

# Adding __repr__ method --> For Google Colabs 
# class Human:
#     def __init__(self, age, name):
#         self._age = age
#         self._name = name
    
#     def __str__(self):
#         return "hi"
    
#     def __repr__(self):
#         return "hi"
# print(h)  # Outputs: hi (in Colab, uses __repr__)

# Updating __str__ and __repr__ with name
class Human:
    def __init__(self, age, name):
        self._age = age
        self._name = name
    
    def __str__(self):
        return f"A human with name {self._name}."

h = Human(age=4, name="greg")
print(h)  # Outputs: A human with name greg.

# Adding age to __str__ and __repr__
class Human:
    def __init__(self, age, name):
        self._age = age
        self._name = name
    
    def __str__(self):
        return f"A human with name {self._name}. their age is {self._age}."
    
h = Human(age=4, name="greg")
print(h)  # Outputs: A human with name greg. their age is 4.

# Adding age to __str__ and __repr__ w Concatenation
# With OUT str(self._age) you get:
    # TypeError: can only concatenate str (not "int") to str
    # Fix: Convert age to string
class Human:
    def __init__(self, age, name):
        self._age = age
        self._name = name
    
    def __str__(self):
        return "A human with name " + self._name + "." + " Their age is " + str(self._age) + "."
    
h = Human(age=4, name="greg")
print(h)  # Outputs: a human with name greg. their age is 4.


# Breakdown: Defining Human class
class Human:  # Creates Human class for storing age and name
              # Think of it like a factory that makes humans.
    def __init__(self, age, name):  # Initializes age and name attributes
        self._age = age  # Sets age attribute
        self._name = name  # Sets name attribute
    
    def __str__(self):  # Defines string representation of Human
        return f"A human with name {self._name}. their age is {self._age}."  # Returns formatted description
    
# Using Human object
h = Human(age=4, name="greg")  # Creates Human with age 4, name "greg"
                               # h is an object of class Human.
print(h)  # Outputs: A human with name greg. their age is 4.

# Explanation: How a Class works:
# The Human class is like a factory that builds human objects with age and name.
# 1. Class as Blueprint:
#    - The Human class defines a template for creating humans with two attributes: age and name.
# 2. Creating a Human:
#    - When we write h = Human(age=4, name="greg"), we tell the factory to make a human.
#    - The constructor (__init__) runs to set up this human.
#    - self is *this specific human* (greg), automatically set by Python.
#    - self._age = 4 and self._name = "greg" store these as attributes (data) for this human.
#    - The underscore (_) in _age and _name is a convention to suggest these attributes are private.
# 3. Printing a Human:
#    - When we print(h), Python calls __str__ to get a string description of this human.
#    - __str__ uses self._name ("greg") and self._age (4) to return: "A human with name greg. their age is 4."
# 4. Understanding self:
#    - self refers to the particular human object we’re working with (here, greg).
#    - It lets us access this human’s attributes (self._age, self._name) in methods like __init__ and __str__.
# This code creates a human named greg, age 4, stores their attributes, and prints a friendly description!


# Accessing attributes
print(h._age)  # Outputs: 4
print(h._name)  # Outputs: greg
print(h.__str__())  # Outputs: a human with name greg. their age is 4.
                    # "You would never actually do this - 1:52:55"

# Adding a method
class Human:
    def __init__(self, age, name):
        self._age = age
        self._name = name
    
    def __str__(self):
        return f"a human with name {self._name}. their age is {str(self._age)}."
    
    def older_younger_than(self, age):
        if self._age > age:
            print("our age is bigger than their age.")
        elif self._age == age:
            print("our age is equal to their age.")
        else:
            print("our age is less than their age.")

h = Human(age=4, name="greg")
h.older_younger_than(3)  # Outputs: our age is bigger than their age.
h.older_younger_than(4)  # Outputs: our age is equal to their age.
h.older_younger_than(5)  # Outputs: our age is less than their age.


# ----------------------------------------------------------------------------------
# 1:56:00 Comments / Docstrings

# Key Points:
# - Comments: Lines starting with `#` are ignored by Python, used for human-readable notes (e.g., explaining code purpose).
# - Docstrings: Triple-quoted strings (`'''` or `"""`) at the start of functions, classes, or modules provide documentation, accessible via `help()`.
# - Docstrings describe purpose, parameters, and return values; they’re critical for reusable code and libraries.
# - The `help()` function displays docstrings for functions, classes, or objects, aiding debugging and collaboration.
# - Practical Use: Comments clarify code logic; docstrings document APIs for users (e.g., specifying parameter types).
# - Pitfalls: Poor docstrings (e.g., vague descriptions) reduce code usability; avoid duplicating obvious code details in comments.
# - Example: A function with a docstring and `help()` demonstrates documentation; docstrings on classes provide class-level info.

# Basic comment
# The following is a function that multiplies two numbers
def mult(a, b):
    return a * b

# Using help on built-in function
help(print)  # Outputs: Documentation for print function

# Adding docstring to function
def mult(a, b):
    '''
    mult(a, b) is a function which returns the multiplication of a and b.

    a must be a number.
    b must be a number.
    '''
    return a * b
help(mult)  # Outputs: mult(a, b) is a function which returns...

# Invalid input for mult
mult("friend", [1, 2, 3])  # TypeError: can't multiply sequence by non-int

# Valid input for mult
print(mult(4, -3.2))  # Outputs: -12.8 (4 * -3.2)


# Docstring for Human class
class Human:
    '''
    A class that represents a very simplified human.
    
    It takes their age as an int and their name as a str.
    '''
    def __init__(self, age, name):
        self._age = age
        self._name = name
    
    def __str__(self):
        return f"a human with name {self._name}. their age is {str(self._age)}."
    
    def older_younger_than(self, age):
        if self._age > age:
            print("our age is bigger than their age.")
        elif self._age == age:
            print("our age is equal to their age.")
        else:
            print("our age is less than their age.")

h = Human(age=4, name="greg")

# Help on Human Class
help(Human)  # Outputs: A class that represents a very simplified human...

# Help on Human object
help(h)  # Outputs: Same as help(Human)

# Help on Class and Object is the same
    # help(Human) shows the class docstring and details, and help(h) shows the same since h is a Human instance.

# # Help on integer
a = 4
help(a)  # Outputs: Documentation for int class
help(6)  # Outputs: Documentation for int class (literal)

# You can ask help on almost everything.


# ----------------------------------------------------------------------------------
# 2:03:55 Lists in Detail

# Key Points:
# - Lists are mutable, ordered sequences of items, defined with square brackets `[item1, item2, ...]`.
# - Methods: `append(item)` adds an item; `insert(index, item)` inserts at index; `count(item)` counts occurrences; `reverse()` reverses order; `remove(item)` removes first occurrence.
# - Most methods below have sife effects, modifying the list in place and return None; count() returns an integer.
# - Lists support indexing (`list[index]`) and iteration (`for item in list`); indices start at 0.
# - Mutability: Lists can be modified in place (e.g., `list[0] = 5`), affecting all references to the list (see `is` operator).
# - Practical Use: Lists are ideal for ordered, dynamic collections; methods like `append` and `remove` simplify manipulation.
# - Pitfalls: Modifying a list in a function affects the original (side effect); use `deepcopy` to avoid. Out-of-range indices cause `IndexError`.
# - Example: Nested loops demonstrate complex list-building logic, requiring careful analysis to understand output.

# Most methods below have sife effects, modifying the list in place and return None; count() returns an integer.

# Basic list methods
l = [1, 2, 3]
l.append(4)
print(l)  # Outputs: [1, 2, 3, 4]

l.insert(0, "hi")
print(l)  # Outputs: ['hi', 1, 2, 3, 4]

l.append(4)
print(l)  # Outputs: ['hi', 1, 2, 3, 4, 4]

print(l.count(4))  # Outputs: 2
print(l.count("hi"))  # Outputs: 1
print(l.count(7))  # Outputs: 0

l.reverse()
print(l)  # Outputs: [4, 4, 3, 2, 1, 'hi']

l.remove(3)
print(l)  # Outputs: [4, 4, 2, 1, 'hi']

# Understanding list append and print
# Demonstrates the difference between printing a method's return value and the list itself.
l = [1, 2, 3]
print(l.append(4))  # Outputs: None (append modifies list, returns None)
print(l)  # Outputs: [1, 2, 3, 4] (shows modified list)

# Guide: Why print(l.append(4)) outputs None but print(l) shows [1, 2, 3, 4]
# This explains how append works and why the outputs differ.
# 1. append(4) modifies the list:
#    - append(4) adds 4 to l, changing it to [1, 2, 3, 4].
#    - It’s a mutating method with a side effect (changes l in place).
#    - It returns None, meaning "no value," not the list.
# 2. print(l.append(4)) shows None:
#    - Python evaluates l.append(4) first, which returns None.
#    - print() then outputs None, not the list’s contents.
# 3. print(l) shows the list:
#    - After append(4), l is [1, 2, 3, 4].
#    - print(l) directly shows the list’s current state: [1, 2, 3, 4].
# 4. Key takeaway:
#    - append() changes the list but returns None.
#    - Use print(l) to see the list, not print(l.append()).
# Analogy: Think of append(4) as adding a toy to a box (l). The action updates the box but doesn’t give you the box—it says “Done!” (None). Asking “What’s in the box?” (print(l)) shows [1, 2, 3, 4].

# Printing a method's return value
l = [1, 2, 3]
print(l.append(4))      # Outputs: None
print(l.insert(0, "hi")) # Outputs: None
print(l.reverse())      # Outputs: None
print(l.remove(1))      # Outputs: None
print(l.count(2))       # Outputs: 1 (not None)


# Complex nested loop example
l = []
for i in range(5):
    for j in range(3):
        if (i + j) % 2 == 0:
            l.append(i + j)
print(l)  # Outputs: [0, 2, 2, 2, 4, 4, 4, 6]
# Explanation: Appends i+j when i+j is even; i=0..4, j=0..2; e.g., (0,0)=0, (0,2)=2, (1,1)=2, (2,0)=2, (2,2)=4, (3,1)=4, (4,0)=4, (4,2)=6.


# ----------------------------------------------------------------------------------
# 2:07:15 List Slicing  --> Greg skipped this in video

#  Use my Index and Slicing Guide 


# ----------------------------------------------------------------------------------
# 2:08:58 Dictionaries

# Key Points:
# - Dictionaries are unordered key-value pair collections, defined with curly braces `{key: value, ...}`.
# - Keys must be hashable (e.g., strings, integers); values can be any type (e.g., strings, lists, objects).
# - Operations: Lookup (`dict[key]`), update (`dict[key] = value`), delete (`del dict[key]`).
# - Iteration: `for k in dict.keys():` loops through keys; access values with `dict[k]`.
# - Side Effects: Updating or deleting keys modifies the dictionary in place.
# - Practical Use: Dictionaries provide fast key-based lookups (O(1) complexity), ideal for mappings (e.g., word definitions, rankings).
# - Pitfalls: Non-hashable keys (e.g., lists) cause `TypeError`; missing keys raise `KeyError`; use consistent key types (e.g., all strings).
# - Example: A fruit dictionary demonstrates key-value operations; an integer-key dictionary shows alternative key types.

# Dictionary operations
d = {"apple": "it's a fruit that is high in vitamin c"}
print(d)  # Outputs: {'apple': "it's a fruit that is high in vitamin c"}

d["banana"] = "it's a fruit that is high in potassium"
print(d)  # Outputs: {'apple': "...", 'banana': "..."}

d["banana"] = "it's a vegetable that is high in potassium"
print(d)  # Outputs: {'apple': "...", 'banana': "..."}

del d["banana"]
print(d)  # Outputs: {'apple': "..."}

d["cucumber"] = "this is a long cylindrical fruit with a boring taste"
print(d)  # Outputs: {'apple': "...", 'cucumber': "..."}

# Iterating through dictionary
for k in d.keys():
    v = d[k]
    print(k, v)  # Outputs: apple it's a fruit..., cucumber this is a long...

# Integer-key dictionary
d2 = {0: "greg", 1: "sarah", 2: "tom"}
print(d2)  # Outputs: {0: 'greg', 1: 'sarah', 2: 'tom'}
print(d2[1])  # Outputs: sarah


# ----------------------------------------------------------------------------------
# 2:17:02 Strings in Detail

# Key Points:
# - **Strings** are immutable sequences of characters, defined with single (`'`) or double (`"`) quotes.
# - **Immutability**: Strings cannot be modified in place (e.g., `s[0] = 't'` raises `TypeError`); methods like `upper()` return new strings.
# - **F-strings**: `f"string {variable}"` embed expressions in strings, automatically calling `str()` on non-strings (e.g., numbers, objects).
# - **Format Method**: `string.format(var1, var2)` inserts values into `{0}`, `{1}` placeholders; less common than f-strings but useful for repeated patterns.
# - Methods: `split(sep)` splits into a list; `isnumeric()` checks if string represents a number; `lower()`/`upper()` convert case; `rstrip()` removes trailing characters (e.g., `\n`).
# - Indexing: Strings support `s[index]` (0-based); `len(s)` gives length.
# - Practical Use: F-strings simplify dynamic string creation; methods like `split` and `isnumeric` are useful for parsing user input.
# - Pitfalls: String immutability requires creating new strings for modifications; mixing types in concatenation requires `str()`.
# - Example: F-strings and `format()` show dynamic string creation; string methods demonstrate common operations.

# F-string examples
name = "greg"
fave_num = 23
print(f"hey {name} how is it going?")  # Outputs: hey greg how is it going?
print(f"my favorite number is {fave_num}")  # Outputs: my favorite number is 23

h = Human(4, "greg")
print(f"my favorite person is {h}")  # Outputs: my favorite person is a human with name greg. their age is 4.

# Format method
print("hey {0} how is it going? my favorite person is {1}".format(name, h))
# Outputs: hey greg how is it going? my favorite person is a human...

# String methods
s = "my name is greg"
print(s.split(" "))  # Outputs: ['my', 'name', 'is', 'greg']

print("greg".isnumeric())  # Outputs: False
print("452".isnumeric())  # Outputs: True
print("4g6".isnumeric())  # Outputs: False

print("HELLO there".lower())  # Outputs: hello there
print("hello THERE".upper())  # Outputs: HELLO THERE

# String indexing
s = "hello"
print(s[0])  # Outputs: h
print(s[1])  # Outputs: e
print(len(s))  # Outputs: 5

# Immutability
l = [1, 2]
l[0] = 5
print(l)  # Outputs: [5, 2]

s = "hello"
# s[0] = 't'  # TypeError: 'str' object does not support item assignment
s = s.upper()  # Creates new string
print(s)  # Outputs: HELLO (original s unchanged until reassigned)


# ----------------------------------------------------------------------------------
# 2:27:47 Tuples

# Key Points:
# - **Tuples** are immutable, ordered sequences defined with parentheses `(item1, item2, ...)`, similar to lists but unchangeable.
# - Syntax: `(0, 1)` creates a tuple; access items with `tuple[index]` (0-based); iterate with `for item in tuple`.
# - **Immutability**: Tuples cannot be modified (e.g., no `append`, no item assignment), raising `TypeError` if attempted (like strings).
# - Practical Use: Tuples ensure data integrity when immutability is desired (e.g., fixed coordinates, constant data). They’re lighter than lists in memory and often used as dictionary keys (unlike lists, which are unhashable).
# - Comparison to Lists: Lists are mutable (`list[0] = 5` works), while tuples are not (`tuple[0] = 5` fails). Lists have methods like `append`; tuples have fewer methods (e.g., `count`, `index`).
# - Pitfalls: Attempting to modify a tuple raises `TypeError`. Tuples with one item need a trailing comma (e.g., `(1,)`); otherwise, it’s treated as a scalar (e.g., `(1)` is just `1`).
# - Example: Tuples demonstrate indexing and iteration; immutability parallels strings, contrasting with mutable lists (see Integer vs. List Immutability example).

# Creating and accessing tuples
t = (0, 1)
print(t)  # Outputs: (0, 1)
print(t[0])  # Outputs: 0
print(t[1])  # Outputs: 1

# Iterating over tuple
for item in t:
    print(item)  # Outputs: 0, 1 (one per line)

# Immutability error
# t[0] = 5  # TypeError: 'tuple' object does not support item assignment


# ----------------------------------------------------------------------------------
# 2:30:35 Sets

# Key Points:
# - **Sets** are unordered, mutable collections of unique items, defined with braces `{item1, item2, ...}` or `set(iterable)`.
# - Uniqueness: Sets automatically remove duplicates (e.g., `{1, 1, 2}` becomes `{1, 2}`).
# - Unordered: No indexing (e.g., `set[0]` raises `TypeError`); order in output is not guaranteed.
# - Practical Use: Sets are ideal for removing duplicates (e.g., unique characters in a string) or performing mathematical operations (e.g., union, intersection).
# - Syntax: `{1, 2}` creates a set; `set()` creates an empty set (note: `{}` creates an empty dictionary).
# - Pitfalls: Using `{}` for an empty set creates a dictionary; use `set()`. Sets only store hashable items (e.g., numbers, strings, not lists).
# - Example: Sets remove duplicates from strings or lists; `sorted()` returns a sorted list from any iterable (no side effect).

# Creating a set
s = {1, 1, 2, -4}
print(s)  # Outputs: {1, 2, -4} (duplicates removed, order may vary)

# Removing duplicates from a string
print(set("greg is a great guy"))  # Outputs: {' ', 'a', 'e', 'g', 'i', 'r', 's', 't', 'u', 'y'} (unique characters)

# Removing duplicates from a list
print(set([1, 1, 2, 2, 3, -5, 6, 4]))  # Outputs: {1, 2, 3, 4, -5, 6} (unique numbers)

# Empty set
print(type({}))  # Outputs: <class 'dict'> (empty dictionary)
print(type(set()))  # Outputs: <class 'set'> (empty set)

# Sorting an iterable
print(sorted([2, 1, 4]))  # Outputs: [1, 2, 4] (returns new list, no side effect)


# ----------------------------------------------------------------------------------
# 2:34:33 Errors / Try / Except

# Key Points:
# - **Exceptions**: Errors (e.g., `TypeError`, `SyntaxError`) halt execution unless handled.
# - **Try/Except**: `try:` runs code that might raise an error; `except:` catches specific errors (e.g., `except TypeError:`) or all errors (`except:`) to prevent program crashes.
# - Execution Flow: If an error occurs in `try`, execution jumps to `except`; subsequent `try` code is skipped. Non-indented code after `try/except` runs regardless.
# - Practical Use: Use `try/except` to handle invalid user input, file errors, or operations like tuple assignment that may fail.
# - Pitfalls: Catching all errors (`except:`) can hide unexpected issues; specify error types when possible. `SyntaxError` cannot be caught in `try/except` as it’s a compile-time error.
# - Example: Catching a `TypeError` for tuple assignment prevents program crashes; specific error handling improves robustness.

# Basic try/except
try:
    print("hi")
    t = (1, 2, 3)
    t[0] = 1  # Raises TypeError
    print("hello")  # Skipped
except TypeError:
    print("caught it")  # Outputs: hi, caught it

# Catching wrong error type
try:
    t = (1, 2, 3)
    t[0] = 1  # Raises TypeError
except SyntaxError:
    print("caught it")  # TypeError: not caught, program crashes

# Syntax error cannot be caught
# try:
#     t[0] === 1  # SyntaxError: invalid syntax (cannot be caught)
# except SyntaxError:
#     print("caught it")


# ----------------------------------------------------------------------------------
# 2:38:35 User Input

# Key Points:
# - **Input**: The `input(prompt)` function displays a prompt and returns user input as a string.
# - Practical Use: Combine with `isnumeric()` to validate numeric input or `try/except` to handle invalid input gracefully.
# - **F-strings**: Useful for formatting input results dynamically (e.g., `f"result is {result}"`).
# - Pitfalls: Input is always a string, even for numbers (e.g., `"32"`); use `int()` or `float()` for conversion, but validate first to avoid `ValueError`.
# - Example: Prompting for a number and checking if it’s numeric demonstrates basic input validation.

# Getting user input
result = input("hey please give us a number: ")
print(f"the result is {result}.")  # Outputs: the result is 32. (if user enters 32)
print(type(result))  # Outputs: <class 'str'>

# Validating input
print(result.isnumeric())  # Outputs: True (if "32"), False (if "hi")


# ----------------------------------------------------------------------------------
# 2:41:18 List Comprehension

# Key Points:
# - **List Comprehension**: A concise way to create lists: `[expression for var in iterable if condition]`.
# - Syntax: `[x for x in range(5)]` generates a list from `x` values; add `if` for filtering (e.g., `x % 2 == 0` for evens); use `if/else` before `for` for conditional expressions.
# - **Zip**: `zip(iter1, iter2)` pairs elements from multiple iterables, enabling multi-variable iteration (e.g., `for a, b in zip(range(3), range(4, 7))`).
# - **Dictionary Comprehension**: Similar to list comprehension, `{key: value for var in iterable}` creates dictionaries (e.g., `{a: b for a, b in zip(...)}`).
# - Practical Use: List comprehensions are fast and readable for generating lists (e.g., squares, filtered values); used heavily in data science. Dictionary comprehensions create key-value mappings efficiently.
# - Pitfalls: Incorrect syntax (e.g., `if` before `for` without `else`) raises `SyntaxError`. Complex comprehensions can reduce readability; use sparingly for clarity.
# - Example: List comprehensions create lists of squares or evens; `zip` pairs values; dictionary comprehension builds key-value pairs.

# Basic list comprehension
l = [x for x in range(5)]
print(l)  # Outputs: [0, 1, 2, 3, 4]

# List comprehension with expression
l = [x**2 for x in range(5)]
print(l)  # Outputs: [0, 1, 4, 9, 16]

# List comprehension with condition
l = [x for x in range(5) if x % 2 == 0]
print(l)  # Outputs: [0, 2, 4]

# List comprehension with if/else
l = [x if x % 2 == 0 else 5 for x in range(5)]
print(l)  # Outputs: [0, 5, 2, 5, 4]

# Error: Invalid syntax
# l = [x if x % 2 == 0 for x in range(5)]  # SyntaxError: invalid syntax
# l = [x else 5 for x in range(5) if x % 2 == 0]  # SyntaxError: invalid syntax

# List concatenation and multiplication
print([0] * 5)  # Outputs: [0, 0, 0, 0, 0]
print([1, 2] + [5, 4, 7])  # Outputs: [1, 2, 5, 4, 7]

# Zip function
for a, b in zip(range(3), range(4, 7)):
    print(a, b)  # Outputs: 0 4, 1 5, 2 6

# List comprehension with zip
l = [(a, b) for a, b in zip(range(3), range(4, 7))]
print(l)  # Outputs: [(0, 4), (1, 5), (2, 6)]

# Dictionary comprehension
d = {a: b for a, b in zip(range(3), range(4, 7))}
print(d)  # Outputs: {0: 4, 1: 5, 2: 6}


# ----------------------------------------------------------------------------------
# 2:49:13 ASCII / Ord / Chr

# Key Points:
# - **ASCII**: A standard mapping where each character is represented by an integer (e.g., 'A' is 65, 'a' is 97).
# - **chr()**: Converts an integer to its ASCII character (e.g., `chr(65)` returns 'A').
# - **ord()**: Converts a single character to its ASCII integer (e.g., `ord('A')` returns 65).
# - Practical Use: Useful for character manipulation, encoding/decoding, or creating mappings (e.g., alphabet dictionary).
# - Combined with dictionary comprehension, `chr()` and `ord()` can generate mappings like alphabet positions (1 to 'a', 2 to 'b', etc.).
# - Pitfalls: `chr()` expects integers in valid ASCII range (0-127 for standard ASCII); `ord()` expects a single character. Incorrect inputs raise errors (e.g., `ValueError` for invalid integers).
# - Example: Create a dictionary mapping numbers 1-26 to lowercase letters 'a' to 'z' using `chr()` and comprehension, leveraging ASCII values starting at 97.

# ASCII character and integer conversion
print(chr(65))  # Outputs: A
print(chr(97))  # Outputs: a
print(ord('A'))  # Outputs: 65
print(ord('a'))  # Outputs: 97

# Dictionary comprehension for alphabet
d = {k: chr(k + 96) for k in range(1, 27)}  # Maps 1->a, 2->b, ..., 26->z
print(d)  # Outputs: {1: 'a', 2: 'b', ..., 26: 'z'}

# Error: Zip length mismatch (demonstrated but fixed)
# d = {k: v for k, v in zip(range(1, 27), range(3))}  # Stops at shorter range (length 3)


# ----------------------------------------------------------------------------------
# 2:53:45 Lambda Function 


# ----------------------------------------------------------------------------------
# 2:53:50 Modules / Pip / Packages

# Key Points:
# - **Modules**: Reusable Python files or libraries containing functions, classes, or variables (e.g., `copy` module with `deepcopy`).
# - **Importing**: Use `import module` or `from module import item` to access module contents; `as` renames modules (e.g., `import numpy as np`).
# - **Pip**: Python’s package manager; `pip list` shows installed packages. Colab includes many pre-installed packages (e.g., `numpy`, `tensorflow`), unlike a fresh local Python install.
# - Practical Use: Modules enable code reuse and access to powerful libraries (e.g., `numpy` for numerical operations). Importing specific items reduces namespace clutter.
# - Pitfalls: Missing modules raise `ModuleNotFoundError`; ensure packages are installed via `pip install`. Colab’s pre-installed packages may not be available locally.
# - Example: Importing `deepcopy` from `copy` module demonstrates module usage; `pip list` shows available packages in Colab.

# Importing a module
from copy import deepcopy
a = [1, 2, 3]
b = deepcopy(a)
print(b)  # Outputs: [1, 2, 3]
print(a is b)  # Outputs: False (deepcopy creates a new object)

# Importing with alias
import copy as cp
b = cp.deepcopy(a)
print(b)  # Outputs: [1, 2, 3]

# Listing installed packages (Colab-specific)
# !pip list  # Outputs: List of packages (e.g., tensorboard, tensorflow)

# Importing numpy (pre-installed in Colab)
import numpy as np
print(np)  # Outputs: <module 'numpy' ...>


# ----------------------------------------------------------------------------------
# 2:57:52 Python Scripts / Files

# Key Points:
# - **Python Scripts**: Files with `.py` extension containing Python code, executed top-to-bottom (unlike Colab notebooks, which retain variables between cells).
# - **Running Scripts**: Use `python filename.py` in a terminal or `!python filename.py` in Colab to execute.
# - **Importing Scripts**: Place reusable code (e.g., classes) in a `.py` file and import it (e.g., `from human import Human`) to use in other scripts.
# - Practical Use: Scripts are ideal for standalone programs or reusable modules. Importing allows modular code organization, avoiding code duplication.
# - Pitfalls: Scripts don’t retain variables after execution (unlike Colab cells). Ensure imported files are in the same directory or specify the path.
# - Example: A `test.py` script validates user input; a `human.py` file contains the `Human` class, imported into `test.py` for reuse.

# Content of test.py (simulated here)
"""
# test.py
from human import Human
l = [1, 2, 3]
u = input("Give us a number please: ")
if u.isnumeric():
    print(f"Thank you for the number {u}")
else:
    print("Hey, why didn't you give us a number??")
print(Human)  # Outputs: <class '__main__.Human'>
"""
# Run with: !python test.py
# Input: 45
# Outputs: Thank you for the number 45
#          <class '__main__.Human'>

# Content of human.py (simulated here)
"""
# human.py
class Human:
    def __init__(self, age, name):
        self._age = age
        self._name = name
    def __str__(self):
        return f"a human with name {self._name}. their age is {str(self._age)}."
    def __repr__(self):
        return f"a human with name {self._name}. their age is {str(self._age)}."
    def older_younger_than(self, age):
        if self._age > age:
            print("our age is bigger than their age.")
        elif self._age == age:
            print("our age is equal to their age.")
        else:
            print("our age is less than their age.")
"""


# ----------------------------------------------------------------------------------
# 3:04:11 Local Python

# Key Points:
# - **Local Setup**: Install Python from python.org (e.g., version 3.8 for stability, not the latest 3.10). Use a terminal to run scripts (`python filename.py`).
# - **File Management**: Place `.py` files in a working directory (e.g., `test` folder); use `dir` (Windows) or `ls` (Linux/Mac) to verify files; navigate with `cd`.
# - **Editors**: Use VS Code, Notepad++, or any text editor to write `.py` files. Ensure correct indentation and file extensions.
# - Practical Use: Local Python enables running scripts without Colab, ideal for production or offline work. Virtual environments (not covered here) manage package dependencies.
# - Pitfalls: Local Python has fewer pre-installed packages than Colab; install needed packages via `pip`. Incorrect file paths or missing Python installation cause errors.
# - Example: Running `test.py` locally mirrors Colab execution, assuming `human.py` is in the same directory.

# Simulating local execution (same as test.py above)
# In terminal:
# 1. Create test folder: mkdir test
# 2. Navigate: cd test
# 3. Create test.py and human.py (as above)
# 4. Run: python test.py
# Input: 67
# Outputs: Thank you for the number 67
#          <class '__main__.Human'>

# Checking local packages
# !pip list  # Outputs: Smaller list locally (e.g., pip, setuptools) compared to Colab

# ----------------------------------------------------------------------------------
# 3:07:38 Conclusion

# Key Points:
# - This tutorial covers Python basics: data types (int, float, str, bool, list, tuple, set, dict), control structures (if, loops), functions, classes, file I/O, error handling, and list comprehensions.
# - Practical Advice: Use Colab for learning due to pre-installed libraries; transition to local Python for standalone scripts or production.
# - Next Steps: Explore virtual environments for package management (see Greg’s recommended video). Practice by experimenting with scripts and modules.
# - Takeaway: Python’s simplicity and powerful features (e.g., list comprehensions, modules) make it ideal for data science, automation, and more.
