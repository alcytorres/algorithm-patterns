# Python Full Course For Beginners: Zero to Hero in 3 Hours
# Video: https://www.youtube.com/watch?v=NakyjvSrTIQ
# Grok notes: https://grok.com/chat/d75c2885-2cd7-47e5-a46c-37e60661c914
# Transcript: https://tactiq.io/tools/run/youtube_transcript?yt=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DNakyjvSrTIQ
# Environment: Examples use Google Colab, but code is compatible with any Python environment (e.g., VS Code)

# Table of Contents
# 0:00:00 Introduction
# 0:10:53 Math Operations
# 0:17:51 Variables
# 0:20:26 Booleans / Conditions
# 0:27:55 If Statements
# 0:31:10 Introduction to Lists
# 0:33:24 For Loops             ***Review Important***
# 0:41:35 While Loops
# 0:47:30 If / Elif / Else
# 0:56:40 Functions
# 1:11:15 Is                    ***Review Important***
# 1:27:13 Cool Function Tricks
# 1:34:27 File Reading / Writing    ***Skipped review later***
# 1:42:33 Objects and Classes.  ***Review Important***
# 1:56:00 Comments / Docstrings
# 2:03:55 Lists in Detail
# 2:08:58 Dictionaries          ***Review Important***
# 2:17:02 Strings in Detail     ***Review Important***
# 2:27:47 Tuples                ***Review Important***
# 2:30:35 Sets                  ***Review Important***
# 2:34:33 Errors / Try / Except
# 2:38:35 User Input
# 2:41:18 List Comprehension    ***Review Important***
# 2:49:13 ASCII / Ord / Chr
# 2:53:50 Modules / Pip / Packages
# 2:57:52 Python Scripts / Files
# 3:04:11 Local Python
# 3:07:38 Conclusion

# Stack
# Queue 
# Linked List
# Linked List


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

# Updating __str__ with name
class Human:
    def __init__(self, age, name):
        self._age = age
        self._name = name
    
    def __str__(self):
        return f"A human with name {self._name}."

h = Human(age=4, name="greg")
print(h)  # Outputs: A human with name greg.

# Adding age to __str__ 
class Human:
    def __init__(self, age, name):
        self._age = age
        self._name = name
    
    def __str__(self):
        return f"A human with name {self._name}. Their age is {self._age}."
    
h = Human(age=4, name="greg")
print(h)  # Outputs: A human with name greg. Their age is 4.

# Adding age to __str__  w Concatenation
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


# --------------------------------------------------------------------------
# Example: Creating and manipulating a Human object with age and name
# This code defines a Human class, creates an object, compares its age, and prints attributes.

class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    
    def __str__(self):
        return f"A human with name {self.name}. Their age is {self.age}."

    def older_younger_than(self, age):
        if self.age > age:
            print("our age is bigger than their age.")
        elif self.age == age:
            print("our age is equal to their age.")
        else:
            print("our age is less than their age.")

h = Human(25, "John")
h.older_younger_than(30)
print(h.age)
print(h.name)


# Class definition
class Human:
    # def __init__(self, age, name):
    # - Defines the initializer method __init__ to set up a new Human object.
    # - __init__: Special method (double underscores __ mark built-in Python methods) called automatically when creating an object.
    # - self: Refers to the object being created (e.g., 'h' later).
    # - age, name: Parameters passed when creating the object (e.g., 25, "John").
    def __init__(self, age, name):
        # self.age = age
        # - Assigns the 'age' parameter to the object's 'age' attribute.
        # - self.age: Creates a variable tied to the object (e.g., h.age = 25).
        # - Stores 'age' for later use (e.g., in __str__).
        self.age = age
        # self.name = name
        # - Assigns the 'name' parameter to the object's 'name' attribute.
        # - self.name: Creates a variable tied to the object (e.g., h.name = "John").
        # - Stores 'name' for later use.
        self.name = name

    # def __str__(self):
    # - Defines the __str__ method to control how the object is shown as a string when printed.
    # - __str__: Special method (double underscores __ indicate it’s built-in) called by print() or str().
    # - self: Refers to the object being printed (e.g., 'h').
    # - Why print() uses __str__: print() calls __str__ to get a human-readable string for the object. Without __str__, print() would show a default, less useful string (e.g., "<__main__.Human object at 0x...>").
    def __str__(self):
        # return f"A human with name {self.name}. Their age is {self.age}."
        # - Returns a formatted string describing the object.
        # - self.name, self.age: Access the object’s stored 'name' and 'age' (e.g., "John", 25).
        # - f-string: Inserts self.name and self.age into the string (e.g., "A human with name John. Their age is 25.").
        return f"A human with name {self.name}. Their age is {self.age}."

    # def older_younger_than(self, age):
    # - Defines a method to compare the object’s age with a given age.
    # - self: Refers to the object calling the method (e.g., 'h').
    # - age: Parameter for the age to compare against (e.g., 30).
    def older_younger_than(self, age):
        # if self.age > age:
        # - Checks if the object’s age (e.g., h.age = 25) is greater than the given age (e.g., 30).
        if self.age > age:
            # print("our age is bigger than their age.")
            # - Prints message if object’s age is greater (e.g., 25 > 30 is False, so this doesn’t run).
            print("our age is bigger than their age.")
        # elif self.age == age:
        # - Checks if the object’s age equals the given age (e.g., 25 == 30 is False).
        elif self.age == age:
            # print("our age is equal to their age.")
            # - Prints message if ages are equal (doesn’t run here).
            print("our age is equal to their age.")
        # else:
        # - Runs if neither condition above is true (e.g., 25 < 30).
        else:
            # print("our age is less than their age.")
            # - Prints message if object’s age is less (e.g., 25 < 30 is True, so this runs).
            print("our age is less than their age.")


# Creating a Human instance and verifying __str__ behavior
h = Human(25, "John")
# - Creates a new Human object, calling __init__(25, "John").
# - h: Variable storing the object.
# - Human(25, "John"): Passes 25 as 'age' and "John" as 'name' to __init__.
# - self in __init__ refers to 'h', so h.age = 25 and h.name = "John".

# - Calls h.__str__() to get the string representation of 'h'.
print(h)
# - __str__ returns "A human with name John. Their age is 25.".
# - print() outputs: A human with name John. Their age is 25.

# Explicitly calling str() to verify __str__ behavior
print(str(h))             # Outputs: A human with name John. Their age is 25.
# - str(h) explicitly invokes h.__str__() to get the string representation of 'h'.
# - __str__ returns "A human with name John. Their age is 25.".
# - print() outputs: A human with name John. Their age is 25.


# Accessing instance attributes directly
print(h.age)              # Outputs: 25
print(h.name)             # Outputs: John

# Test older_younger_than method with different ages
h.older_younger_than(30)  # Outputs: our age is less than their age.
h.older_younger_than(25)  # Outputs: our age is equal to their age.
h.older_younger_than(10)  # Outputs: our age is more than their age.

# Modifying an instance attribute and rechecking behavior
h.age = 40
print(h)                  # Outputs: A human with name John. Their age is 40.
h.older_younger_than(50)  # Outputs: our age is less than their age.
h.older_younger_than(40)  # Outputs: our age is equal to their age.
h.older_younger_than(35)  # Outputs: our age is more than their age.

# Creating a second instance with different attributes
h2 = Human(15, "Alice")
print(h2)                 # Outputs: A human with name Alice. Their age is 15.
h2.older_younger_than(10) # Outputs: our age is bigger than their age.

# Creating another instance and modifying its attributes
h3 = Human(30, "Bob")
h3.name = "Robert"
print(h3)                 # Outputs: A human with name Robert. Their age is 30.

# Comparing ages between two Human instances
h.older_younger_than(h2.age)  # Outputs: our age is bigger than their age. (40 > 15)

# Reassigning an instance and checking its state
h = Human(23, "Jane")     # Reassign h to a new Human instance
print(h)                  # Outputs: A human with name Jane. Their age is 23.



# Why it works: The code creates a Human object with age and name, stores them as attributes using self, and defines how to print the object with __str__. When print(h) runs, it shows a custom string using the stored age and name.

# In Python, __ (double underscores) denotes special methods (like __init__ or __str__) that have built-in functionality and are automatically called by the interpreter during specific operations, such as object creation or string conversion.


# General, Simple Description of __init__ and __str__:
# - __init__(self, ...): Sets up a new object when created. It’s like filling out a form for the object (e.g., setting age and name). Runs automatically when you make a new object (e.g., Human(25, "John")).
# - __str__(self): Defines how the object looks when printed. It’s like giving the object a name tag to show a clear description (e.g., "A human with name John. Their age is 25.").

# Are str() and __str__(self) the same? No.
# - str(): A built-in Python function that converts an object to a string by calling the object’s __str__ method. It’s used outside the class (e.g., str(h)).
# - __str__(self): A method you define inside a class to say what string the object should produce when str() or print() is called. It’s the class’s way of customizing str().
# - Difference: str() is a function that triggers __str__. __str__ is the class’s internal rule for what string to return. You write __str__ to control str()’s output for your object.

# Why __str__(self) is used by print():
# - print() needs a string to display. It calls __str__ to get that string from the object. This lets you customize what print() shows (e.g., a readable description instead of a memory address).



# Explanation of print(h) vs print(str(h)) in the Human class
# The __str__ method returns a string like "A human with name John. Their age is 25."
# It's a special method Python calls automatically when a string representation is needed.

# When you use print(h):
# - print() needs a string, so Python calls h's __str__ method automatically.
# - __str__ returns "A human with name John. Their age is 25.", which print() outputs.
# - This implicitly invokes __str__.

# When you use print(str(h)):
# - str(h) explicitly calls h's __str__ method to get the string.
# - __str__ returns "A human with name John. Their age is 25.", which print() outputs.
# - This directly triggers __str__.

# Why the same output?
# Both print(h) and print(str(h)) output "A human with name John. Their age is 25."
# because they both use __str__. print(h) calls it implicitly; str(h) calls it explicitly.
# Matching outputs confirm print(h) uses __str__, reinforcing how special methods work.



# Accessing Methods and Attributes with Dot Notation
    # Use the dot (.) to access or invoke methods and attributes of an object, connecting the instance to its class-defined functionality.


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


# Sorted returns a new list 
    # 2:30:15  --> Shown in Tuple section, move it here.
nums = [2, 1, 4]
print(sorted(nums))  
# Outputs: [1, 2, 4] (sorted() returns a new sorted list, no side effect on original)

print(nums)
# Outputs: [2, 1, 4]
# original nums list remains unchanged 

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

# Creating a dictionary
d = {"apple": "it's a fruit that is high in vitamin c"}
print(d)  # Outputs: {'apple': "it's a fruit that is high in vitamin c"}

# Adding a key-value pair
d["banana"] = "it's a fruit that is high in potassium"
print(d)  # Outputs: {'apple': "...", 'banana': "..."}

# Updating a key's value
d["banana"] = "it's a vegetable that is high in potassium"
print(d)  # Outputs: {'apple': "...", 'banana': "..."}

# Looking up values
print(d["apple"])  # Outputs: it's a fruit that is high in vitamin c
print(d["banana"])  # Outputs: it's a vegetable that is high in potassium

# Deleting a key
del d["banana"]
print(d)  # Outputs: {'apple': "..."}

# Adding a new key-value pair
d["cucumber"] = "this is a long cylindrical fruit with a boring taste"
print(d)  # Outputs: {'apple': "...", 'cucumber': "..."}

# Iterating through dictionary
for k in d.keys():
    v = d[k]
    print(k, v)  # Outputs: apple it's a fruit..., cucumber this is a long...

# Hashable in Python: 
    # An object is hashable if it’s immutable (like int, str, or tuple) and can be assigned a unique, fixed number (hash) for quick lookup.

    # Keys Must Be Hashable: Dictionary keys need to be hashable so Python can use their fixed hash to store and find them fast; mutable objects like list can’t be keys because they can change.

# Integer-key dictionary
# Dictionaries can use any hashable type as keys, like integers.
d = {0: "greg", 1: "sarah", 2: "tom"}  # Creates dictionary with integer keys
print(d)  # Outputs: {0: 'greg', 1: 'sarah', 2: 'tom'}
print(d[1])  # Outputs: sarah (access value for key 1)

# Iterating with keys()
# Loops over keys to access values manually using dictionary indexing.
for k in d.keys():  # Iterates over keys: 0, 1, 2
    v = d[k]  # Gets value for key k (e.g., d[0] = "greg")
    print(k, v)  # Outputs: 0 greg, 1 sarah, 2 tom

# Simpler iteration with items()
# Directly loops over key-value pairs for cleaner code.
for k, v in d.items():  # Iterates over pairs: (0, "greg"), (1, "sarah"), (2, "tom")
    print(k, v)  # Outputs: 0 greg, 1 sarah, 2 tom

# Exercise: Iterating a book dictionary
# Practice iterating and filtering dictionary data.
books = {
    "The Hobbit": 1937,
    "Harry Potter": 1997,
    "The Da Vinci Code": 2003,
    "The Hunger Games": 2008
}

# Print all books and years
for k in books.keys():  # Iterates over book titles
    v = books[k]  # Gets year for book k
    print(k, v)  # Outputs: The Hobbit 1937, Harry Potter 1997, ...

# Print books after 2000
for k in books.keys():  # Iterates over book titles
    v = books[k]  # Gets year for book k
    if v > 2000:  # Filters for years > 2000
        print(k, v)  # Outputs: The Da Vinci Code 2003, The Hunger Games 2008

# Hashable keys explained
# - Hashable: An immutable object (e.g., int, str, tuple) with a fixed hash value for quick lookup.
# - Why keys must be hashable: Dictionaries use hashes to store and retrieve keys efficiently.
# - Example: Integers (0, 1, 2) and strings ("greg", "apple") are hashable, so they work as keys.
# - Mutable objects (e.g., lists) can’t be keys because their hash could change.


# ----------------------------------------------------------------------------------
# 2:17:02 Strings in Detail

# Key Points:
# - Strings are immutable sequences of characters, defined with single (`'`) or double (`"`) quotes.
# - Immutability: Strings cannot be modified in place (e.g., `s[0] = 't'` raises `TypeError`); methods like `upper()` return new strings.
# - F-strings: `f"string {variable}"` embed expressions in strings, automatically calling `str()` on non-strings (e.g., numbers, objects).
# - Format Method: `string.format(var1, var2)` inserts values into `{0}`, `{1}` placeholders; less common than f-strings but useful for repeated patterns.
# - Methods: `split(sep)` splits into a list; `isnumeric()` checks if string represents a number; `lower()`/`upper()` convert case; `rstrip()` removes trailing characters (e.g., `\n`).
# - Indexing: Strings support `s[index]` (0-based); `len(s)` gives length.
# - Practical Use: F-strings simplify dynamic string creation; methods like `split` and `isnumeric` are useful for parsing user input.
# - Pitfalls: String immutability requires creating new strings for modifications; mixing types in concatenation requires `str()`.
# - Example: F-strings and `format()` show dynamic string creation; string methods demonstrate common operations.

# F-string Error: Undefined variable
print(f"Hey {name} how is it going?")  # NameError: name 'name' is not defined

# F-string with variable
name = "greg"
print(f"Hey {name} how is it going?")  # Outputs: Hey greg how is it going?

# F-string with varaible and number
name = "greg"
fave_num = 23
print(f"Hey {name} how is it going? My favorite number is {fave_num}")  
# Outputs: Hey greg how is it going? My favorite number is 23

# String Concatenation Error
print("My favorite number is " + fav_num)
# Output: NameError: name 'fav_num' is not defined.


# ----------------------------------------------------------------------------
# Objects in Python

# Class from prior section 
class Human:
    def __init__(self, age, name):
        self._age = age
        self._name = name
    
    def __str__(self):
        return f"A human with name {self._name}. Their age is {str(self._age)}."
    
h = Human(age=4, name="greg")
# print(h)

# F-string with object
# Uses the Human object's __str__ method to format it as a string.
h = Human(4, "greg")
print(f"My favorite person is {h}")  
# Outputs: My favorite person is A human with name greg. Their age is 4.

# F-string with numbers and strings
# Everything in Python is an object, including numbers like 4.
name = "greg"
fave_num = 23
print(f"Hey {name} how is it going? My favorite number is {4}")  
# Outputs: Hey greg how is it going? My favorite number is 4

# Explanation: Objects in Python
# In Python, everything is an object, meaning every value (numbers, strings, custom classes) has associated methods and properties.
# 1. Objects and f-strings:
#    - In f-strings (e.g., f"...{h}"), Python calls the object's __str__ method to convert it to a string.
#    - For h (a Human object), __str__ returns "a human with name greg. their age is 4."
# 2. Numbers as objects:
#    - Even a number like 4 is an object (an int). Its __str__ method returns "4" for printing.
#    - In f"...{4}", Python uses 4's __str__ to include "4" in the output.
# 3. Why this matters:
#    - Objects like numbers, strings, or Human instances can be used in f-strings because they know how to describe themselves as strings.
#    - This makes Python flexible: you can print or format any object, from simple numbers to complex classes.
# Example: Try print(f"Num: {42}, Person: {h}") to see how different objects work together!

print(f"Num: {42}, Person: {h}")
# Output: Num: 42, Person: A human with name greg. their age is 4.


# ----------------------------------------------------------------------------
# Format method
print("Hey {0} how is it going? my favorite person is {1}".format(name, h))
# Outputs: Hey greg how is it going? My favorite person is A human with name greg. Their age is 4.

# The .format() method is preferred over f-strings when reusing the same template multiple times, as it avoids repeatedly writing long variable names, using concise numeric indices (e.g., {0}) instead, which reduces clunkiness.


# Iterating over string characters
# Loops through each character in a string.
for c in "Greg":  # Iterates over characters: G, r, e, g
    print(c)  # Outputs: G, r, e, g (one per line)

# Checking character types
for c in "Greg":  # Iterates over characters: G, r, e, g
    print(type(c))  # Outputs: <class 'str'> (four times, one per character)

# String methods
print("my name is greg".split(" "))  # Outputs: ['my', 'name', 'is', 'greg']
    # Split() instantly transforms a string into a list of substrings, enabling easy manipulation of text data.

print("greg".isnumeric())  # Outputs: False
print("452".isnumeric())  # Outputs: True
print("4g6".isnumeric())  # Outputs: False

print("HELLO there".lower())  # Outputs: hello there
print("hello there".lower())  # Outputs: hello there
print("HELLO there".upper())  # Outputs: HELLO THERE
print("hello THERE".upper())  # Outputs: HELLO THERE

# String indexing
s = "hello"
print(s[0])  # Outputs: h
print(s[1])  # Outputs: e
print(s[2])  # Outputs: l
print(s[3])  # Outputs: l
print(s[4])  # Outputs: o
print(s[5])  # Outputs: IndexError: string index out of range
print(len(s))  # Outputs: 5

# List mutability
l = [1, 2]
l[0] = 5
print(l)  # Outputs: [5, 2]

# String immutability
s = "hello"
s[0] = 't'  # TypeError: 'str' object does not support item assignment
    # Strings are immutable, so you can't change individual characters like with lists.

# String method with no side effect
s = "hello"
print(s.upper())  # Outputs: HELLO (new string, no side effect)
print(s)  # Outputs: hello (original unchanged)
# upper() returns a new string; it doesn’t modify s (no side effect, unlike list methods).


# ----------------------------------------------------------------------------------
# 2:27:47 Tuples

# Key Points:
# - Tuples are immutable, ordered sequences defined with parentheses `(item1, item2, ...)`, similar to lists but unchangeable.
# - Syntax: `(0, 1)` creates a tuple; access items with `tuple[index]` (0-based); iterate with `for item in tuple`.
# - Immutability: Tuples cannot be modified (e.g., no `append`, no item assignment), raising `TypeError` if attempted (like strings).
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
t[0] = 5  # TypeError: 'tuple' object does not support item assignment

# Tuples exist primarily to provide an immutable, lightweight data structure for grouping related data
    # Use when you want to make something constant and secure


# Single-item tuple
t_single = (42,)  # Needs trailing comma to be a tuple
print(t_single)  # Outputs: (42,)
print(type(t_single))  # Outputs: <class 'tuple'>
print(type((42)))  # Outputs: <class 'int'> (no comma, not a tuple)
# Use a trailing comma for single-item tuples to avoid scalar confusion.

# Nested tuples
nested = ((1, 2), (3, 4))
print(nested[0])  # Outputs: (1, 2) (first tuple)
print(nested[0][1])  # Outputs: 2 (second item of first tuple)
# Use nested tuples to group related data hierarchically, like coordinates.

# Tuples as dictionary keys
d = {(1, 2): "point A", (3, 4): "point B"}  # Tuples are hashable, so can be keys
print(d[(1, 2)])  # Outputs: point A
# Tuples work as dictionary keys because they’re immutable and hashable, unlike lists.

# Common use cases
# - Coordinates: Store (x, y) pairs, e.g., (10, 20), to ensure unchangeable positions.
# - Function Returns: Return multiple values, e.g., def get_info(): return (name, age).
# - Data Integrity: Use tuples for constant data (e.g., days of week) to prevent accidental changes.
# Example: Store a fixed point and use in a dictionary.
point = (5, 10)  # Fixed coordinate
locations = {point: "Home"}
print(locations[point])  # Outputs: Home

# Practice problems
# 1. Create a tuple of 3 colors and print the second one.
# 2. Use a tuple as a dictionary key to map a coordinate to a name.
# 3. Write a function that returns a tuple of (min, max) from a list of numbers.
# Example solution for problem 3:
def min_max(numbers):
    return (min(numbers), max(numbers))
print(min_max([1, 5, 3]))  # Outputs: (1, 5)



# ----------------------------------------------------------------------------------
# 2:30:35 Sets

# Key Points:
# - Sets are unordered, mutable collections of unique items, defined with braces `{item1, item2, ...}` or `set(iterable)`.
# - Uniqueness: Sets automatically remove duplicates (e.g., `{1, 1, 2}` becomes `{1, 2}`).
# - Unordered: No indexing (e.g., `set[0]` raises `TypeError`); order in output is not guaranteed.
# - Practical Use: Sets are ideal for removing duplicates (e.g., unique characters in a string) or performing mathematical operations (e.g., union, intersection).
# - Syntax: `{1, 2}` creates a set; `set()` creates an empty set (note: `{}` creates an empty dictionary).
# - Pitfalls: Using `{}` for an empty set creates a dictionary; use `set()`. Sets only store hashable items (e.g., numbers, strings, not lists).
# - Example: Sets remove duplicates from strings or lists; `sorted()` returns a sorted list from any iterable (no side effect).


# What does hashable mean?

# In Python, a hashable object is one that can't be changed (immutable) and can be given a unique number (called a hash) to identify it quickly, like a fingerprint. This is important for things like dictionary keys, which need to stay consistent for fast lookups.

# String (immutable, hashable)
name = "Greg"
print(hash(name))  # Outputs: a unique number, e.g., 594372991234
d = {name: 25}    # Works: "Greg" is hashable, used as a dictionary key
print(d["Greg"])   # Outputs: 25

# List (mutable, not hashable)
numbers = [1, 2]
d[numbers] = 10  # Error: lists can't be keys because they're not hashable

# Easy Analogy: Think of a hashable object like a labeled, sealed box (e.g., a string like "Greg"). Its label (hash) never changes, so Python can find it fast in a dictionary. A list is like an unsealed box—its contents can change, so it can’t have a reliable label and isn’t hashable.


# -----------------------------------------------------------------------------
# Creating a set
s = {1, 1, 2, -4}
print(s)  # Outputs: {1, 2, -4} (duplicates removed, order may vary)

# Python recognizes {1, 1, 2, -4} as a set because {} with comma-separated values (without colons like in dictionaries) indicates a set, unlike () which defines a tuple.

# Convert string to a set and remove duplicate characters
print(set("Greg is a great guy"))  
# Outputs: {' ', 'a', 'e', 'g', 'i', 'r', 's', 't', 'u', 'y'}
# Creates a set from the string, keeping only unique characters.
# Unordered: set order varies each run, as sets don’t maintain a fixed sequence.

# Removing duplicates from a list
print(set([1, 1, 2, 2, 3, -5, 6, 4]))  # Outputs: {1, 2, 3, 4, -5, 6}

# Empty set vs. dictionary
print(type({}))     # Outputs: <class 'dict'> (creates an empty dictionary)
print(type(set()))  # Outputs: <class 'set'> (creates an empty set)
# {} defaults to an empty dictionary; use set() to create an empty set.

# Sorting an iterable
print(sorted([2, 1, 4]))  # Outputs: [1, 2, 4] (returns new list, no side effect)


# Set operations: Union and Intersection
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 | s2)  # Outputs: {1, 2, 3, 4} (union: all unique elements)
print(s1 & s2)  # Outputs: {2, 3} (intersection: common elements)
# Use | for combining sets, & for finding shared items.

# Adding and removing items
s = {1, 2}
s.add(3)  # Adds 3 to set
print(s)  # Outputs: {1, 2, 3}
s.remove(2)  # Removes 2; raises KeyError if not found
print(s)  # Outputs: {1, 3}
# Use add() to include items, remove() to delete; items must be hashable.

# Membership testing
s = {1, 2, 3}
print(2 in s)  # Outputs: True (checks if 2 is in set)
print(4 in s)  # Outputs: False (4 not in set)
# Sets are fast for checking if an item exists (O(1) on average).

# Common use cases
# - Unique Items: Remove duplicates from lists or strings (e.g., unique user IDs).
# - Membership Testing: Quickly check if an item exists (e.g., valid coupon codes).
# - Set Operations: Find common or combined elements (e.g., shared tags between users).
# Example: Find unique words in a sentence.
sentence = "hello world hello"
unique_words = set(sentence.split())
print(unique_words)  # Outputs: {'hello', 'world'}

# Practice problems
# 1. Create a set of 3 numbers and add a fourth using add().
# 2. Find the intersection of two sets of names.
# 3. Remove duplicates from a list of emails using a set.
# Example solution for problem 2:
names1 = {"Alice", "Bob"}
names2 = {"Bob", "Charlie"}
print(names1 & names2)  # Outputs: {'Bob'} (common names)


# -----------------------------------------------------------------------------
# Types Review
s = {1, 1, 2, -4}
print(type(s))

t = (1, 1, 2, -4)
print(type(t))

l = [1, 1, 2, -4]
print(type(l))

d = {1: 'a', 2: 'b', 3: 'c'}
print(type(d))


# -----------------------------------------------------------------------------
# Empty instances of main Python data types

# List: Ordered collection (mutable)
empty_list = []  # Creates an empty list

# Tuple: Ordered collection (immutable)
empty_tuple = ()  # Creates an empty tuple
t = (1, "hello", 3.5)  # Tuple with basic data

# Dictionary: Key-value pairs (mutable)
empty_dict = {}  # Creates an empty dictionary
d = {"name": "Alice", "age": 25, "score": 90}  # Dict with basic data

# Set: Unordered collection of unique elements (mutable)
empty_set = set()  # Creates an empty set (note: {} creates a dict)
s = {1, "hello", 3.5}  # Set with basic data

# Integer: Whole number (immutable)
empty_int = 0  # Represents an "empty" or zero integer

# Float: Floating-point number (immutable)
empty_float = 0.0  # Represents an "empty" or zero float

# String: Sequence of characters (immutable)
empty_string = ""  # Creates an empty string

# Boolean: True/False value (immutable)
empty_bool = False  # Represents a default "empty" boolean (False is often used)


# ----------------------------------------------------------------------------------
# 2:34:33 Errors / Try / Except

# Key Points:
# - Exceptions: Errors (e.g., `TypeError`, `SyntaxError`) halt execution unless handled.
# - Try/Except: `try:` runs code that might raise an error; `except:` catches specific errors (e.g., `except TypeError:`) or all errors (`except:`) to prevent program crashes.
# - Execution Flow: If an error occurs in `try`, execution jumps to `except`; subsequent `try` code is skipped. Non-indented code after `try/except` runs regardless.
# - Practical Use: Use `try/except` to handle invalid user input, file errors, or operations like tuple assignment that may fail.
# - Pitfalls: Catching all errors (`except:`) can hide unexpected issues; specify error types when possible. `SyntaxError` cannot be caught in `try/except` as it’s a compile-time error.
# - Example: Catching a `TypeError` for tuple assignment prevents program crashes; specific error handling improves robustness.

# Tuple TypeError:
t = (1, 2, 3)
t[0] = 1  # Raises TypeError: 'tuple' object does not support item assignment

# Basic try/except
t = (1, 2, 3)
try:
    t[0] = 1  # Raises TypeError
except:
    print("caught it")  # Outputs: caught it

# Try/except with multiple statements
t = (1, 2, 3)
try:
    print("hi")
    t[0] = 1  # Raises TypeError
    print("hello")  # Skipped
except:
    print("caught it")  # Outputs: hi, caught it

# Specific error catching
t = (1, 2, 3)
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
    t[0] ==== 1  # SyntaxError: invalid syntax (cannot be caught)
except SyntaxError:
    print("caught it")
# Note there are some syntax errors that Try/except does NOT work with.


# -----------------------------------------------------------------------------
# Most Common Python Errors
SyntaxError
# Occurs when Python cannot parse code due to incorrect syntax (e.g., missing colon or parentheses).
# Example: print("hello"  # Missing closing parenthesis

TypeError
# Happens when an operation is applied to an incompatible type (e.g., adding a string and integer).
# Example: "2" + 2  # Cannot add str and int

NameError
# Raised when a variable or name is used but not defined.
# Example: print(x)  # x is not defined

IndexError
# Occurs when accessing a list, tuple, or string index that doesn’t exist.
# Example: lst = [1, 2]; print(lst[2])  # Index 2 is out of range

KeyError
# Happens when accessing a dictionary key that doesn’t exist.
# Example: d = {"a": 1}; print(d["b"])  # Key "b" not found

ValueError
# Raised when a function gets an argument of the correct type but an invalid value.
# Example: int("abc")  # Cannot convert "abc" to integer

AttributeError
# Occurs when an object doesn’t have the attribute or method being accessed.
# Example: s = "hello"; s.append("!")  # Strings have no append method

ZeroDivisionError
# Happens when dividing a number by zero.
# Example: 5 / 0  # Division by zero is undefined

FileNotFoundError
# Raised when trying to open a file that doesn’t exist.
# Example: open("missing.txt")  # File "missing.txt" not found

IndentationError
# Occurs when code blocks have incorrect or inconsistent indentation.
# Example: def func(): print("hi")  # Missing indentation for print


# ----------------------------------------------------------------------------------
# 2:38:35 User Input

# Key Points:
# - Input: The `input(prompt)` function displays a prompt and returns user input as a string.
# - Practical Use: Combine with `isnumeric()` to validate numeric input or `try/except` to handle invalid input gracefully.
# - F-strings: Useful for formatting input results dynamically (e.g., `f"result is {result}"`).
# - Pitfalls: Input is always a string, even for numbers (e.g., `"32"`); use `int()` or `float()` for conversion, but validate first to avoid `ValueError`.
# - Example: Prompting for a number and checking if it’s numeric demonstrates basic input validation.

# Getting user input
result = input("Hey please give us a number: ")
print(f"The result is {result}.")  
# Outputs: The result is 32. (if user enters 32)

# User input stored as a string
print(type(result))  # Outputs: <class 'str'>

# Validating input
print(result.isnumeric())  # Outputs: True (if "32"), False (if "hi")


# Validating user input with try/except
# Prompts for a number, checks if valid, and handles errors.
try:
    user_input = input("Enter a number: ")  # Gets user input as string
    number = int(user_input)  # Tries to convert input to integer
    print(f"Success! Your number is {number}.")  # Proceeds if valid
except ValueError:
    print("Error: Please enter a valid number, not text.")  # Informs user if invalid

# Choosing try/except vs. if/else
    # Use try/except for robust error handling when testing operations that might fail (e.g., type conversions); 
    # Use if/else for simple, predictable condition checks (e.g., validating specific patterns).


# ----------------------------------------------------------------------------------
# 2:41:18 List Comprehension

# Key Points:
# - List Comprehension: A concise way to create lists: `[expression for var in iterable if condition]`.
# - Syntax: `[x for x in range(5)]` generates a list from `x` values; add `if` for filtering (e.g., `x % 2 == 0` for evens); use `if/else` before `for` for conditional expressions.
# - Zip: `zip(iter1, iter2)` pairs elements from multiple iterables, enabling multi-variable iteration (e.g., `for a, b in zip(range(3), range(4, 7))`).
# - Dictionary Comprehension: Similar to list comprehension, `{key: value for var in iterable}` creates dictionaries (e.g., `{a: b for a, b in zip(...)}`).
# - Practical Use: List comprehensions are fast and readable for generating lists (e.g., squares, filtered values); used heavily in data science. Dictionary comprehensions create key-value mappings efficiently.
# - Pitfalls: Incorrect syntax (e.g., `if` before `for` without `else`) raises `SyntaxError`. Complex comprehensions can reduce readability; use sparingly for clarity.
# - Example: List comprehensions create lists of squares or evens; `zip` pairs values; dictionary comprehension builds key-value pairs.

# Basic list comprehension
l = [x for x in range(5)]
print(l)  # Outputs: [0, 1, 2, 3, 4]

# Standard For Loop
l = []
for x in range(5):
    l.append(x)
print(l)  # Outputs: [0, 1, 2, 3, 4]


# List comprehension with expression
l = [x**2 for x in range(5)]
print(l)  # Outputs: [0, 1, 4, 9, 16]


# List comprehension with condition
l = [x for x in range(5) if x % 2 == 0]
print(l)  # Outputs: [0, 2, 4]

# Error: Invalid syntax (if without else)
l = [x if x % 2 == 0 for x in range(5)]  
# SyntaxError: 'if' needs 'else' when before 'for' 

# Error: Invalid syntax (if with else)
l = [x for x in range(5) if (x%2) == 0 else 5]  
# SyntaxError: 'else' can't follow 'if' after 'for' 

# List comprehension with if/else
l = [x if x % 2 == 0 else 5 for x in range(5)]
print(l)  # Outputs: [0, 5, 2, 5, 4]


# List comprehension with different iterable
l = [x if x % 2 == 0 else 5 for x in [4, 1, 6, 12]]
print(l)  # Outputs: [4, 5, 6, 12]


# List multiplication
print([0] * 5)  # Outputs: [0, 0, 0, 0, 0]

# List concatenation
print([1, 2] + [5, 4, 7])  # Outputs: [1, 2, 5, 4, 7]


# Zip function with loop
# Pairs elements from two iterables and iterates over them together.
for a, b in zip(range(3), range(4, 7)):
    print(a, b)  # Outputs: 0 4, 1 5, 2 6
# zip(range(3), range(4, 7)) pairs [0, 1, 2] with [4, 5, 6].
# The loop unpacks each pair (e.g., (0, 4)) into a, b and prints them.
# Use this to iterate over multiple sequences in parallel.

# List comprehension with zip
# Creates a list of tuples by pairing elements from two iterables.
l = [(a, b) for a, b in zip(range(3), range(4, 7))]
print(l)  # Outputs: [(0, 4), (1, 5), (2, 6)]
# zip(range(3), range(4, 7)) creates pairs: (0, 4), (1, 5), (2, 6).
# The list comprehension collects these pairs into a list of tuples.
# Use this to build a list of paired values from multiple sequences.

# Dictionary comprehension with zip
# Creates a dictionary by pairing keys and values from two iterables.
d = {a: b for a, b in zip(range(3), range(4, 7))}
print(d)  # Outputs: {0: 4, 1: 5, 2: 6}
# zip(range(3), range(4, 7)) pairs [0, 1, 2] with [4, 5, 6].
# The dictionary comprehension uses a as key, b as value to build a dict.
# Use this to create a dictionary from two sequences paired together.


# ----------------------------------------------------------------------------------
# 2:49:13 ASCII / Ord / Chr

# Key Points:
# - ASCII: A standard mapping where each character is represented by an integer (e.g., 'A' is 65, 'a' is 97).
# - chr(): Converts an integer to its ASCII character (e.g., `chr(65)` returns 'A').
# - ord(): Converts a single character to its ASCII integer (e.g., `ord('A')` returns 65).
# - Practical Use: Useful for character manipulation, encoding/decoding, or creating mappings (e.g., alphabet dictionary).
# - Combined with dictionary comprehension, `chr()` and `ord()` can generate mappings like alphabet positions (1 to 'a', 2 to 'b', etc.).
# - Pitfalls: `chr()` expects integers in valid ASCII range (0-127 for standard ASCII); `ord()` expects a single character. Incorrect inputs raise errors (e.g., `ValueError` for invalid integers).
# - Example: Create a dictionary mapping numbers 1-26 to lowercase letters 'a' to 'z' using `chr()` and comprehension, leveraging ASCII values starting at 97.

# ASCII conversions
print(chr(65))  # Outputs: A
print(chr(97))  # Outputs: a
print(ord('A'))  # Outputs: 65
print(ord('a'))  # Outputs: 97
print(chr(66))  # Outputs: B
print(chr(98))  # Outputs: b
print(chr(67))  # Outputs: C

# Dictionary comprehension with zip (mismatched lengths)
d = {k: v for k, v in zip(range(1, 27), range(4, 7))}
print(d)  # Outputs: {1: 4, 2: 5, 3: 6} (stops at shorter range)

# Dictionary comprehension with zip (matched lengths)
d = {k: v for k, v in zip(range(1, 27), range(1, 27))}
print(d)  # Outputs: {1: 1, 2: 2, ... 25: 25, 26: 26}

# Dictionary comprehension for alphabet
d = {k: chr(k) for k in range(1, 27)}
print(d)  # Outputs: {1: '\x01', 2: '\x02', ...} (non-printable characters)

d = {k: chr(k + 64) for k in range(1, 27)}
print(d)  # Outputs: {1: 'A', 2: 'B', ..., 26: 'Z'}


# ----------------------------------------------------------------------------------
# 2:53:45 Lambda Function 


# ----------------------------------------------------------------------------------
# 2:53:50 Modules / Pip / Packages

# Key Points:
# - Modules: Reusable Python files or libraries containing functions, classes, or variables (e.g., `copy` module with `deepcopy`).
# - Importing: Use `import module` or `from module import item` to access module contents; `as` renames modules (e.g., `import numpy as np`).
# - Pip: Python’s package manager; `pip list` shows installed packages. Colab includes many pre-installed packages (e.g., `numpy`, `tensorflow`), unlike a fresh local Python install.
# - Practical Use: Modules enable code reuse and access to powerful libraries (e.g., `numpy` for numerical operations). Importing specific items reduces namespace clutter.
# - Pitfalls: Missing modules raise `ModuleNotFoundError`; ensure packages are installed via `pip install`. Colab’s pre-installed packages may not be available locally.
# - Example: Importing `deepcopy` from `copy` module demonstrates module usage; `pip list` shows available packages in Colab.


# A module is a file containing reusable code (functions, classes, variables) that you can import to use in other programs.

# Importing the math module
import math  # Loads the math module with mathematical functions
print(math.sqrt(16))  # Uses the sqrt function from the math module to calculate the square root of 16.
# Outputs: 4.0

# Importing specific function from module
from copy import deepcopy
a = [1, 2, 3]
b = deepcopy(a)
print(a is b)  # Outputs: False (b is a separate copy of a)

# Importing module with alias
import copy as cp
a = [1, 2, 3]
b = cp.deepcopy(a)
print(a is b)  # Outputs: False (b is a separate copy of a)

# Both create a deep copy of a; differ only in import syntax.

# copy is a module: copy is a built-in Python module that provides functions for copying objects.

# deepcopy is a function: deepcopy is a function within the copy module that creates a deep copy of an object, duplicating all nested objects.


# Importing numpy
import numpy as np
print(np)  # Outputs: <module 'numpy'> (shows module object)

# Listing installed packages (Colab-specific)
!pip list  # Outputs: List of packages (e.g., tensorboard, tensorflow)



# ----------------------------------------------------------------------------------
# 2:57:52 Python Scripts / Files

# Key Points:
# - Python Scripts: Files with `.py` extension containing Python code, executed top-to-bottom.
# - Running Scripts: Use `python filename.py` in a terminal to execute.
# - Importing Scripts: Place reusable code (e.g., classes) in a `.py` file and import it (e.g., `from human import Human`) to use in other scripts.
# - Practical Use: Scripts are ideal for standalone programs or reusable modules. Importing allows modular code organization, avoiding code duplication.
# - Pitfalls: Scripts don’t retain variables after execution. Ensure imported files are in the same directory or specify the path.
# - Example: A `test.py` script validates user input; a `human.py` file contains the `Human` class, imported into `test.py` for reuse.

# Checking files
# ls  # Outputs: test.py, human.py, ...

# Content of test.py (simulated as inline code)

# test.py
u = input("Give us a number please: ")
if u.isnumeric():
    print(f"Thank you for the number {u}")
else:
    print("Hey, why didn't you give us a number??")

# Run test.py
python3 test.py  # Prompts: Give us a number please: e.g., "6" 
# Outputs: Thank you for the number 6

# -----------------------------------------------------------------------------
# Content of human.py (for reference, not executed)
# human.py
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

# -----------------------------------------------------------------------------
# test.py
from human import Human 

print(Human)

# Output:
# Give us a number please: e.g., "6"
# Thank you for the number 6
# <class 'human.Human'>


# ----------------------------------------------------------------------------------
# 3:04:11 Local Python

# Key Points:
# - Local Setup: Install Python from python.org (e.g., version 3.8 for stability, not the latest 3.10). Use a terminal to run scripts (`python filename.py`).
# - File Management: Place `.py` files in a working directory (e.g., `test` folder); use `dir` (Windows) or `ls` (Linux/Mac) to verify files; navigate with `cd`.
# - Editors: Use VS Code, Notepad++, or any text editor to write `.py` files. Ensure correct indentation and file extensions.
# - Practical Use: Local Python enables running scripts without Colab, ideal for production or offline work. Virtual environments (not covered here) manage package dependencies.
# - Pitfalls: Local Python has fewer pre-installed packages than Colab; install needed packages via `pip`. Incorrect file paths or missing Python installation cause errors.
# - Example: Running `test.py` locally mirrors Colab execution, assuming `human.py` is in the same directory.

# Simulating local execution (same as test.py above)
# In terminal:
# 1. Create test folder: mkdir test
# 2. Navigate: cd test
# 3. Create test.py and human.py (as above)
# 4. Run: python test.py
# Input: Give us a number, please: 67
# Outputs: 
# Thank you for the number 67
# <class 'human.Human'>

# Checking local packages
!pip list  
# Outputs: Minimal local list (e.g., pip, setuptools) compared to Colab extensive list

# ----------------------------------------------------------------------------------
# 3:07:38 Conclusion

# Key Points:
# - This tutorial covers Python basics: data types (int, float, str, bool, list, tuple, set, dict), control structures (if, loops), functions, classes, file I/O, error handling, and list comprehensions.
# - Practical Advice: Use Colab for learning due to pre-installed libraries; transition to local Python for standalone scripts or production.
# - Next Steps: Explore virtual environments for package management (see Greg’s recommended video). Practice by experimenting with scripts and modules.
# - Takeaway: Python’s simplicity and powerful features (e.g., list comprehensions, modules) make it ideal for data science, automation, and more.
