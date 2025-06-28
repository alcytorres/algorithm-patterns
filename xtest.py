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