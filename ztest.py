

# movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
# ["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

# # print(movies)
# # Output:
# ['The Holy Grail', 1975, 'Terry Jones & Terry Gilliam', 91, ['Graham Chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]]


# # Triple-Level Nested Loop with Type Checking: Fully Unpack Nested Lists
# for each_item in movies:
#     if isinstance(each_item, list):
#         for nest_item in each_item:
#             if isinstance(nest_item, list):
#                 for deeper_item in nest_item:
#                     if isinstance(deeper_item, list):
#                         for deepest_item in deeper_item:
#                             print(deepest_item)
#                     else:
#                         print(deeper_item)
#             else:
#                 print(nest_item)
#     else:
#         print(each_item)

# # Output:


