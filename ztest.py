# # print(type(True))

# # if False:
# #     print(1)
# #     print(3)

# # print(10)


grocery_list = ["apple", "grape", "banana", "orange"]

# for i in range(len(grocery_list)):
#     print(grocery_list[i])

# print(range(5))
# print(range(len(grocery_list)))


# for i, item in enumerate(grocery_list):
    # print(i, item)

# j = len(grocery_list) - 1
# while j >= 0:
#     print(grocery_list[j])
#     j -= 1
# print('end')

z = 42

def our_print(s):
    print(z)
    print(s + " hello")

print(our_print("Hi"))

s = 87

# By default a function returns 'None' which is nothing 

def our_print(s):
    print(z)
    print(s + " hello")
    return None  # Here is what it looks like behind the scenes 

print(our_print("Hi"))


# ----------------------------------------------------------------------------------

#  List:  11:11:20

def append_4_to_list(lst):
    lst.append(4) 

a = [1, 2, 3]

append_4_to_list(a)
print(a)  # [1, 2, 3, 4]

b = a
print(b)  # [1, 2, 3, 4]

a is b  # True
a == [1, 2, 3, 4]  # True
a is [1, 2, 3, 4]  # False 

"""
a is [1, 2, 3, 4] is False because is checks object identity, and [1, 2, 3, 4] creates a new list object distinct from a, even if their contents match.

The is operator checks for object identity (whether two variables refer to the exact same object in memory), not whether two lists have the same contents.
"""


a[0] = 7  
print(a)    # [7, 2, 3, 4]
print(b)    # [7, 2, 3, 4]

b[2] = 12
print(b)    # [7, 2, 12, 4]
print(a)    # [7, 2, 12, 4]


from copy import deepcopy
b = deepcopy(a)

print(a)
print(b)

a[0] = 14
print(a)  # [14, 2, 12, 4]
print(b)  # [7, 2, 12, 4]

# ----------------------------------------------------------------------------------
# Guide: Integer vs. List Immutability in Python

# Integer Behavior (q, w)
# Integers are immutable: assigning a new value creates a new object.
q = 5
w = q
# q and w both reference the integer object 5
print(q)  # 5
print(w)  # 5

q = 7
# q now references a new integer object 7; w still references 5
print(q)  # 7
print(w)  # 5
# Why? Immutability means q = 7 creates a new object, leaving w unchanged.

# List Behavior (for contrast)
# Lists are mutable: changes to the object affect all references.
a = [1, 2, 3]
b = a
a.append(4)
# a and b reference the same list object, so both reflect the change
print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4]
# Mutability allows in-place changes to the shared list object.



# ----------------------------------------------------------------------------------

def add_1(x):
    return x + 1
print(add_1(4))  # 9

def add_1(x):
    x = 8
    return x + 1
print(add_1(4))  # 5 

def add_1(x):
    x = [1, 2]
    return x
print(add_1(4))  # [1, 2] 


# Guide: Function Parameter Assignment and List Immutability

# Define a function that assigns a new list to its parameter
def add_1(x):
    x = [1, 2]  # Assigns a new list object to the local variable x
    return x

# Create a list
a = [1, 2, 3]

# Call the function and print results
print(add_1(a))  # [1, 2]  - Returns the new list created in the function
print(a)         # [1, 2, 3] - Original list a is unchanged

# Explanation:
# - In add_1, 'x' is a local variable that initially refers to the same list as 'a'.
# - 'x = [1, 2]' assigns a new list object to 'x', but does NOT modify the original list 'a'.
# - Lists are mutable, but reassigning the parameter 'x' creates a new object, leaving 'a' unaffected.
# - The function returns the new list [1, 2], while 'a' retains its original value [1, 2, 3].


def add_1(x):
    print(x is a) # True
    x = [1, 2]
    print(x is a) # False
    return x

a = [1, 2, 3]
print(add_1(a))  # [1, 2]
print(a)         # [1, 2, 3]


def add_1(x):
    x.append(4)
    x = [1, 2]
    print(x is a)  # False
    return x

a = [1, 2, 3]
print(add_1(a))  # [1, 2]
print(a)         # [1, 2, 3, 4]


def add_1(x):
    x = [1, 2]
    print(x is a)  # False
    x.append(4)
    return x

a = [1, 2, 3]
print(add_1(a))  # [1, 2, 4]
print(a)         # [1, 2, 3]




# ----------------------------------------------------------------------------------
# 2:07:15 List Slicing --> Use my Guide --> Greg skipped this in video



# ----------------------------------------------------------------------------------

# Guide: List Comprehension with Nested Loops and Condition

l = []
for i in range(5):  # i = 0, 1, 2, 3, 4
    for j in range(3):  # j = 0, 1, 2
        if (i + j) % 2 == 0:  # Append i + j if even
            l.append(i + j)
print(l)  # [0, 2, 2, 2, 4, 4, 4, 6]

# Breakdown:
# - Outer loop: i from 0 to 4 (5 iterations).
# - Inner loop: j from 0 to 2 (3 iterations).
# - Condition: (i + j) % 2 == 0 checks if i + j is even.
# - Appends: 
#   - i=0: j=0 (0), j=2 (2)
#   - i=1: j=1 (2)
#   - i=2: j=0 (2), j=2 (4)
#   - i=3: j=1 (4)
#   - i=4: j=0 (4), j=2 (6)
# - Result: l = [0, 2, 2, 2, 4, 4, 4, 6]

# ----------------------------------------------------------------------------------
# 2:08:58 Dictionaries


# ----------------------------------------------------------------------------------
# 2:17:02 Strings in Detail



# Guide: Mutability of Common Python Data Types

# Mutable (can be changed in place):
# - Lists: [1, 2, 3]
# - Dictionaries: {'key': 'value'}
# - Sets: {1, 2, 3}

# Immutable (can NOT be changed, new object created):
# - Strings: "hello"
# - Integers: 42
# - Floats: 3.14
# - Booleans: True, False
# - Tuples: (1, 2, 3)

# Note: Mutability affects how objects behave when modified or passed to functions.


# ----------------------------------------------------------------------------------
# 2:27:47 Tuples


# ----------------------------------------------------------------------------------
# 2:30:35 Sets


# ----------------------------------------------------------------------------------
# 2:34:33 Errors / Try / Except

# ----------------------------------------------------------------------------------
# 2:38:35 User Input



# ----------------------------------------------------------------------------------
# 2:41:18 List Comprehension




# ----------------------------------------------------------------------------------
# 2:49:13 ASCII / Ord / Chr


# ----------------------------------------------------------------------------------
# 2:53:45 Lambda Function 


# ----------------------------------------------------------------------------------
# 2:53:50 Modules / Pip / Packages


# ----------------------------------------------------------------------------------
# 2:57:52 Python Scripts / Files


# ----------------------------------------------------------------------------------
# 3:04:11 Local Python


# ----------------------------------------------------------------------------------
# 3:07:38 Conclusion


