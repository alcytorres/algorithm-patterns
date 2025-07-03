

# Cocise explain the difference 

# Validating user input with try/except
try:
    user_input = input("Enter a number: ")  # Gets user input as string
    number = int(user_input)  # Tries to convert to integer
    print(f"Success! Your number is {number}.")  # Outputs integer
except ValueError:
    print("Error: Please enter a valid number, not text.")  # Catches non-integer input

# Validating user input with isnumeric()
user_input = input("Enter a number: ")  # Gets user input as string
if user_input.isnumeric():  # Checks if input is numeric digits
    print(f"Success! Your number is {user_input}.")  # Outputs string
else:
    print("Error: Please enter a valid number, not text.")  # Handles non-numeric input