class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    
    def __str__(self):
        return f"A human with name {self.name}. Their age is {self.age}."

h = Human(23, "John")
print(h)


