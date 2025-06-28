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
