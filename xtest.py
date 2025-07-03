# Checking files (Colab-specific)
# !ls  # Outputs: test.py, human.py, ...

# Content of test.py (simulated as inline code)
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
# Run with: !python test.py (prompts "Give us a number please: ", e.g., "45" outputs "Thank you for the number 45", <class '__main__.Human'>)

# Content of human.py (for reference, not executed)
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

# Running test.py (Colab-specific)
# !python test.py  # Prompts for input, e.g., "45" outputs "Thank you for the number 45", <class '__main__.Human'>