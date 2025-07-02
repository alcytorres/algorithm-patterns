# Head first Python 

# Chapter 1: Lists

# Start by defining a list of names, which you then display on screen using the print() BIF. Then, use the len() BIF to work out how many data items are in the list, before accessing and displaying the value of the second data item:

cast = ["Cleese", 'Palin', 'Jones', "Idle"]
print(cast)  # ['Cleese', 'Palin', 'Jones', 'Idle']
# # It’s OK to invoke a BIF on the results of another BIF.
print(len(cast))  # 4
print(cast[1])  # Palin


# With your list created, you can use list methods to add a single data item to the end of your list (using the append() method), remove data from the end of your list (with the pop() method), and add a collection of data items to the end of your list (thanks to the extend() method):

# Methods are invoked using the common “.” dot notation.
cast.append("Gilliam")
print(cast)  # ['Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam']
cast.pop()  # Removes and returns last element ('Gilliam')
print(cast)  # ['Cleese', 'Palin', 'Jones', 'Idle']
# It’s another list: items separated by commas, surrounded by square brackets.
cast.extend(["Gilliam", "Chapman"])
print(cast)  # ['Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam', 'Chapman']


# Finally, find and remove a specific data item from your list (with the remove() method) and then add a data item before a specific slot location (using the insert() method):

cast.remove("Chapman")
print(cast) # ['Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam']
cast.insert(0, "Chapman")
# After all that, we end up with the cast of Monty Python’s Flying Circus!
print(cast)  # ['Chapman', 'Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam']



# ---------------------------------------------------------------------------
# Let’s take a bit of time to try to work out which strategy to use when adding data to your list in this case.
# Given the following list-creation code:
movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]

# 1. Work out the Python code required to insert the numeric year data into the preceding list, changing the list so that it ends up looking like this:
["The Holy Grail", 1975, "The Life of Brian", 1979, "The Meaning of Life", 1983]

movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]
movies.insert(1, 1975)
movies.insert(3, 1979)
movies.append(1983)

print(movies)


# 2. Now write the Python code required to re-create the list with the data you need all in one go:

movies = ["The Holy Grail", 1975, "The Life of Brian", 1979, "The Meaning of Life", 1983]

# In this case, which of these two methods do you think is best?
    # Answer: Yes, method 2 seems the better option here…that is, for a small list like this. Also, there’s no tricky counting to do.


# ---------------------------------------------------------------------------
# Loops

nums = [1, 2, 3]     # nums: list name (source list containing integers)
for num in nums:     # num: target identifier (current integer being processed from nums)
                      # nums: iterable list being looped over
    print(num * 2)    # list-processing code (doubles the current target identifier value)
# Output: 2, 4, 6


# Equivalent For and While Loops:
movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]

# For loops work with lists of any size
for movie in movies:
    print(movie) 
# Output: The Holy Grail, The Life of Brian, The Meaning of Life    

# While Loop
count = 0
while count < len(movies):
    print(movies[count]) 
    count += 1
 # Output: The Holy Grail, The Life of Brian, The Meaning of Life    


# ---------------------------------------------------------------------------
# Store lists within lists
movies = [
"The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

print(movies[0])         # The Holy Grail
print(movies[0][1])      # h
print(movies[4])         # ['Graham Chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]
print(movies[4][0])      # Graham Chapman
print(movies[4][1])      # ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']
print(movies[4][1][3])   # Eric Idle
print(movies[5])         # IndexError: list index out of range


# ---------------------------------------------------------------------------
# Creating a list that contains another list
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

print(movies)
# Output:
# ['The Holy Grail', 1975, 'Terry Jones & Terry Gilliam', 91, ['Graham Chapman', ['Michael Palin',
# 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]]

# The list within a list within a list has been created in memory.
# The “for” loop prints each item of the outer loop ONLY.
# The inner list within the inner list is printed “as-is.”

# ---------------------------------------------------------------------------
# How isinstance() works:

# Solution
names = ['Michael', 'Terry']
if isinstance(names, list):
    print(True)  # Ouput: True
else: 
    print(False)

num_names = len(names)
if isinstance(num_names, list):
    print(True)
else:
    print(False)  # Output: False

# Alternative Solution 
names = ['Michael', 'Terry']
print(isinstance(names, list))  # True
num_names = len(names)
print(isinstance(num_names, list))  # False

# Refer to a Python type here. In this case, the type is “list”.


# ---------------------------------------------------------------------------
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

print(movies)
# Output:
# ['The Holy Grail', 1975, 'Terry Jones & Terry Gilliam', 91, ['Graham Chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]]

# Here’s a copy of the current list-processing code. Your task is to rewrite this code using an if statement and the isinstance() BIF to process a list that displays another list.

# Single-Level Loop: Print Each Item Directly
for each_item in movies:
    print(each_item)

# Output:
# The Holy Grail
# 1975
# Terry Jones & Terry Gilliam
# 91
# ['Graham Chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]

# Write your new code here.

# Single-Level Nested Loop with Type Checking: Unpack First-Level Lists
for each_item in movies:
    if isinstance(each_item, list):
        for nest_item in each_item:
            print(nest_item)
    else:
        print(each_item)

# Output
# The Holy Grail
# 1975
# Terry Jones & Terry Gilliam
# 91
# Graham Chapman
# ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']

# This is a little better, but not by much…there’s another nested list here that’s not being processed properly.


# Double-Level Nested Loop with Type Checking: Fully Unpack Nested Lists
for each_item in movies:
    if isinstance(each_item, list):
        for nest_item in each_item:
            if isinstance(nest_item, list):
                for deepest_item in nest_item:
                    print(deepest_item)
            else:
                print(nest_item)
    else:
        print(each_item)

# Output:
# The Holy Grail
# 1975
# Terry Jones & Terry Gilliam
# 91
# Graham Chapman
# Michael Palin
# John Cleese
# Terry Gilliam
# Eric Idle
# Terry Jones

# Note: in this code, each “if” needs an associated “else”.

# The repeated code replaces the “print()” statement and introduces another target identifier called "deepest_item"


# Triple-Level Nested Loop with Type Checking: Fully Unpack Nested Lists
for each_item in movies:
    if isinstance(each_item, list):
        for nest_item in each_item:
            if isinstance(nest_item, list):
                for deeper_item in nest_item:
                    if isinstance(deeper_item, list):
                        for deepest_item in deeper_item:
                            print(deepest_item)
                    else:
                        print(deeper_item)
            else:
                print(nest_item)
    else:
        print(each_item)


# ---------------------------------------------------------------------------
# What does your function need to do?
    # This function needs to take a list and process each item in the list. If it finds a nested list within the first list, the function needs to repeat. It can do this by invoking itself on the nested list. In other words, the function needs to recur—that is, invoke itself from within the funtion code suite.

# Recursive Function 
def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)

movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

print_lol(movies)

# If the item being processed is itself a list, invoke the function.
# If the item being processed ISN’T a list, display the item on screen.

# Recursion to the rescue!
    # The use of a recursive function has allowed you to reduce 14 lines of messy,hard-to-understand, brain-hurting code into a six-line function. Unlike the earlier code that needs to be amended to support additional nested lists(should the movie buff require them), the recursive function does not need to change to process any depth of nested lists properly.

# ----------------------------------------------------------------------------
# Chapter 2: Modules of functions

# Your code from Chapter 1
def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)

# Here is your module code (which is saved in the file nester.py). Compose two comments: the first to describe the module and the second to describe the function.

"""This is the “nester.py" module, and it provides one function called print_lol() which prints lists that may or may not include nested lists"""

def print_lol(the_list):
    """
    This function takes a positional argument called “the_list", which is any Python list (of, possibly, nested lists). Each data item in the provided list is (recursively) printed to the screen on its own line.
    """
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)

# Test the function
test_list = [1, [2, 3], 4]
print_lol(test_list)

movies = [
"The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman",
["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
print_lol(movies)

# ----------------------------------------------------------------------------
# How do I know where the Python modules are on my computer?
    # Run python3 -c "import sys; print(sys.path)" 
    # in your Mac Terminal to see the list of directories where Python looks for modules, including built-in libraries and third-party packages.


# ----------------------------------------------------------------------------
# Write a small program that imports your newly created module, defines a small list called “cast,” and then uses the function provided by your module to display the contents of the list on screen. Use the following list data (all strings): Palin, Cleese, Idle, Jones, Gilliam, and Chapman.

import nester

cast = ["Palin", "Cleese", "Idle", "Jones", "Gilliam", "Chapman"]
print_lol(cast)  # NameError: name 'print_lol' is not defined


import nester

cast = ["Palin", "Cleese", "Idle", "Jones", "Gilliam", "Chapman"]
nester.print_lol(cast)

# Output: 
# Palin
# Cleese
# Idle
# Jones
# Gilliam
# Chapman