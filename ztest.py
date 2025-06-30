

movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

# Output:
# ['The Holy Grail', 1975, 'Terry Jones & Terry Gilliam', 91, ['Graham Chapman', ['Michael Palin',
# 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]]


# Simple loop printing each item as is
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


# Loop with isinstance checking and nested loop
for each_item in movies:
    if isinstance(each_item, list):
        for nest_item in each_item:
            print(nest_item)
    else:
        print(each_item)

# Output
# The Holy Grail
# 1975
# Terry Jones & Terry Gilliam
# 91
# Graham Chapman
# ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']


# Fully nested loop with two levels of isinstance checking
for each_item in movies:
    if isinstance(each_item, list):
        for nest_item in each_item:
            if isinstance(nest_item, list):
                for deepest_item in nest_item:
                    print(deepest_item)
            else:
                print(nest_item)
    else:
        print(each_item)

# Output:
# The Holy Grail
# 1975
# Terry Jones & Terry Gilliam
# 91
# Graham Chapman
# Michael Palin
# John Cleese
# Terry Gilliam
# Eric Idle
# Terry Jones


# How isinstance() works:

# Solution
# names = ['Michael', 'Terry']
# if isinstance(names, list):
#     print(True)
# else: 
#     print(False)

# num_names = len(names)
# if isinstance(num_names, list):
#     print(True)
# else:
#     print(False)

# Alternative Solution 
# names = ['Michael', 'Terry']
# print(isinstance(names, list))  # True
# num_names = len(names)
# print(isinstance(num_names, list))  # False

