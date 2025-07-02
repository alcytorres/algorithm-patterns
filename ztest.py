# Getting user input
result = input("hey please give us a number: ")
print(f"the result is {result}.")  # Outputs: the result is 32. (if user enters 32)
print(type(result))  # Outputs: <class 'str'>

# Validating input
print(result.isnumeric())  # Outputs: True (if "32"), False (if "hi")