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
    

h = Human(21, "John")
h.older_younger_than(30)  # Outputs: our age is less than their age.
h.older_younger_than(21)  # Outputs: our age is equal to their age.
h.older_younger_than(10)  # Outputs: our age is more than their age.
print(h.age)              # Outputs: 21
print(h.name)             # Outputs: John
print(h)                  # Outputs: A human with name John. Their age is 21.
h.age = 50
print(h)





# num = 123
# string_rep = str(num)
# print(type(string_rep))  # Output: '123'





