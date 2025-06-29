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
        return f"a human with name {self._name}."

h = Human(age=4, name="greg")
print(h)  # Outputs: a human with name greg.

# Adding age to __str__ and __repr__
class Human:
    def __init__(self, age, name):
        self._age = age
        self._name = name
    
    def __str__(self):
        return f"a human with name {self._name}. their age is {self._age}."
    
h = Human(age=4, name="greg")
# print(h)  # TypeError: can only concatenate str (not "int") to str
# Fix: Convert age to string
class Human:
    def __init__(self, age, name):
        self._age = age
        self._name = name
    
    def __str__(self):
        return f"a human with name {self._name}. their age is {str(self._age)}."
    
    def __repr__(self):
        return f"a human with name {self._name}. their age is {str(self._age)}."
h = Human(age=4, name="greg")
print(h)  # Outputs: a human with name greg. their age is 4.

# Accessing attributes
print(h._age)  # Outputs: 4
print(h._name)  # Outputs: greg
print(h.__str__())  # Outputs: a human with name greg. their age is 4.

# Adding a method
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
h = Human(age=4, name="greg")
h.older_younger_than(3)  # Outputs: our age is bigger than their age.
h.older_younger_than(4)  # Outputs: our age is equal to their age.
h.older_younger_than(5)  # Outputs: our age is less than their age.