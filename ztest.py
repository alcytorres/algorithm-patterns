
A = [1, 2, 3]  # Create list

# Append: O(1) amortized
A.append(5)  # Adds 5 to end -> [1, 2, 3, 5]

# Pop from end: O(1)
A.pop()  # Removes last element -> [1, 2, 3]

# Insert at index: O(n)
A.insert(2, 5)  # Inserts 5 at index 2 -> [1, 2, 5, 3]

# Modify: O(1)
A[0] = 7  # Changes index 0 to 7 -> [7, 2, 5, 3]


# Access: O(1)
value = A[2]  # Gets value at index 2 (5)
print(value)


# if 6 in A:  # Search for 6 (O(n))
#     print("True")  # Not printed (6 not in A)
# if 7 in A:  # Search for 7 (O(n))
#     print("True")  # Output: True

# Search: O(n)
is_present = 6 in A  # Returns False (6 not in A)
print(is_present)
is_present = 7 in A  # Returns True (7 not in A)
print(is_present)

print(len(A))  # Length (O(1)) -> Output: 4


# # Cocise explain the difference 

# # Validating user input with try/except
# try:
#     user_input = input("Enter a number: ")  # Gets user input as string
#     number = int(user_input)  # Tries to convert to integer
#     print(f"Success! Your number is {number}.")  # Outputs integer
# except ValueError:
#     print("Error: Please enter a valid number, not text.")  # Catches non-integer input

# # Validating user input with isnumeric()
# user_input = input("Enter a number: ")  # Gets user input as string
# if user_input.isnumeric():  # Checks if input is numeric digits
#     print(f"Success! Your number is {user_input}.")  # Outputs string
# else:
#     print("Error: Please enter a valid number, not text.")  # Handles non-numeric input


