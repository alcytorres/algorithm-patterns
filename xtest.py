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


# Work out the Python code required to insert the numeric year data into the preceding list,
# changing the list so that it ends up looking like this:
["The Holy Grail", 1975, "The Life of Brian", 1979, "The Meaning of Life", 1983]

movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]
movies.insert(1, 1975)
movies.insert(3, 1979)
movies.append(1983)

print(movies)


# Now write the Python code required to re-create the list with the data you need all in one go:

movies = ["The Holy Grail", 1975, "The Life of Brian", 1979, "The Meaning of Life", 1983]

# You were also to write the Python code required to recreate the list with the data you need all in one go: Assign all your data to the “movies” identifier. What was previously there is replaced.


movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]

for movie in movies:
    print(movie)

count = 0
while count < len(movies):
    print(movies[count])
    count += 1


movies = [
"The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
["Graham Chapman",
["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

print(movies[0])         # The Holy Grail
print(movies[0][1])      # h
print(movies[4])         # ['Graham Chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]
print(movies[4][0])      # Graham Chapman
print(movies[4][1])      # ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']
print(movies[4][1][3])   # Eric Idle


    
movies = [
"The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
["Graham Chapman",
["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]


print(movies[0])         # The Holy Grail
print(movies[0][1])      # h
print(movies[4])         # ['Graham Chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]
print(movies[4][0])      # Graham Chapman
print(movies[4][1])      # ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']
print(movies[4][1][3])   # Eric Idle



movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
print(movies)

# Output:
# ['The Holy Grail', 1975, 'Terry Jones & Terry Gilliam', 91, ['Graham Chapman', ['Michael Palin',
# 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]]

# The list within a list within a list has been created in memory.


for each_item in movies:
    print(each_item)

# Output:
# The Holy Grail
# 1975
# Terry Jones & Terry Gilliam
# 91
# ['Graham Chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]

# The “for” loop prints each item of the outer loop ONLY.
# The inner list within the inner list is printed “as-is.”


# How isinstance() works:

# Solution
names = ['Michael', 'Terry']
if isinstance(names, list):
    print(True)
else: 
    print(False)

num_names = len(names)
if isinstance(num_names, list):
    print(True)
else:
    print(False)

# Alternative Solution 
names = ['Michael', 'Terry']
print(isinstance(names, list))  # True
num_names = len(names)
print(isinstance(num_names, list))  # False

# Refer to a Python type here. In this case, the type is “list”.
