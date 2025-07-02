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