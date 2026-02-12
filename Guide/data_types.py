# Python Data Types: A Beginner-Friendly Guide



# Additional Concepts and Tips for Beginners
# - **Immutable stuff** (like integers, strings, tuples) can be keys in dictionaries or items in sets.
# - **Mutable stuff** (like lists, sets, dictionaries) can’t be keys or set items—Python won’t let you!
# - Tuples are tricky: They’re immutable, but if they hold a mutable item (like a list), that item can change.
# Example:
t = (1, [2, 3], 4)
t[1].append(5)  # The list inside the tuple changes
print(t)        # (1, [2, 3, 5], 4)
# But you can’t replace the list itself:
# t[1] = [6, 7]  # This would fail

# - Copies vs. References: Mutable types (like lists) share changes if assigned (lst2 = lst1), but immutable types don’t.
#   Use lst2 = lst1.copy() for a separate mutable copy.
# - Memory Trick: Immutable types can reuse memory (e.g., a = 5 and b = 5 point to the same 5), saving space.
# - Functions: Mutable types changed in functions affect the original; immutable types don’t.
# - Speed: Mutable types can be faster for in-place changes, avoiding new copies.
# - Hashing: Only immutable types (like tuples, strings) can be dictionary keys.


