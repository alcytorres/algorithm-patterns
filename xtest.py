
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
# print(h)  # TypeError: can
#  only concatenate str (not "int") to str
# Fix: Convert age to string