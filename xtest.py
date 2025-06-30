# Head first Python 

# Lists

# Start by defining a list of names, which you then display on screen using the print() BIF. Then, use the len() BIF to work out how many data items are in the list, before accessing and displaying the value of the second data item:

cast = ["Cleese", 'Palin', 'Jones', "Idle"]
print(cast)  # ['Cleese', 'Palin', 'Jones', 'Idle']
# # It’s OK to invoke a BIF on the results of another BIF.
print(len(cast))  # 4
print(cast[1])  # Palin


# With your list created, you can use list methods to add a single data item to the end of your list (using the append() method), remove data from the end of your list (with the pop() method), and add a collection of data items to the end of your list (thanks to the extend() method):

# Methods are invoked using the common “.” dot notation.
cast.append("Gilliam")
print(cast)  # ['Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam']
cast.pop()  # Removes and returns last element ('Gilliam')
print(cast)  # ['Cleese', 'Palin', 'Jones', 'Idle']
# It’s another list: items separated by commas, surrounded by square brackets.
cast.extend(["Gilliam", "Chapman"])
print(cast)  # ['Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam', 'Chapman']


# Finally, find and remove a specific data item from your list (with the remove() method) and then add a data item before a specific slot location (using the insert() method):

cast.remove("Chapman")
print(cast) # ['Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam']
cast.insert(0, "Chapman")
# After all that, we end up with the cast of Monty Python’s Flying Circus!
print(cast)  # ['Chapman', 'Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam']