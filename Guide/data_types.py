# Python Data Types - Quick Reference for Interviews & LeetCode

"""
What are Data Types?
    • Data types are like containers that hold different kinds of values (numbers, text, collections, etc.).

    Each type has rules about what you can do with it. Some can change after creation (mutable), while others cannot (immutable).

TL;DR - Mutable vs Immutable

Mutable   → can change after creation (list, dict, set)
            → Ex: a notebook where you can erase and rewrite
            → in-place edits are fast
            → assignment shares the same object → can cause bugs
            → list.append(), dict["key"]=val

Immutable → cannot change (int, float, str, tuple, bool)
            → Ex: writing in permanent marker
            → "change" = create new object
            → safe assignment, memory reuse for small values
            → string += in loop is slow (O(n²))

Why it matters: understanding this prevents bugs and helps you pick the right type for speed and optimize for time and space.
"""

# ======================================================================
# Most Important Types 

# Mutable
list   = [1, 2, 3]         # type: list
dict   = {"a": 1}          # type: dict
set    = {1, 2, 3}         # type: set

# Immutable
int    = 10                # type: int
float  = 3.14              # type: float
str    = "hello"           # type: str
tuple  = (1, 2, 3)         # type: tuple
bool   = True              # type: bool


# Empty defaults
empty_list    = []
empty_string  = ""
empty_dict    = {}
empty_int     = 0
empty_tuple   = ()
empty_set     = set()      # {} is dict!
empty_float   = 0.0
empty_bool    = False
none_value    = None


# ======================================================================
# Data Types from Simplest to Most Complex

# 1. Integers 
# – Whole numbers (no decimals), like 5 or -10
# - Immutable (changing it creates a new number).
# - Common Operations: Add (+), subtract (-), multiply (*), divide (/).
# - Ex:
a = 5
b = a  # b gets 5
a = 10  # a is now 10, but b stays 5 because integers are immutable
# - LeetCode Connection: Used everywhere—counting steps, array indices, or sums in Prefix Sum problems.

# 2. Floats 
# - Numbers with decimals, like 3.14 or -0.5
# - Immutable (modifying makes a new float).
# - Common Operations: Arithmetic (+, -, *, /), comparisons (<, >).
# - Ex:
x = 3.14
y = x  # y is 3.14
x = 2.71  # x is now 2.71, y stays 3.14
# - LeetCode Connection: Handy for precise calculations, like averages or ratios in numeric problems.

# 3. Strings 
# - Text or characters, like "hello" or "123".
# - Immutable (can’t edit the text directly).
# - Common Operations: Join (+), slice ([start:end]), get character ([index]).
# - Ex:
s = "hello"
t = s  # t is "hello"
s = s + " world"  # s becomes "hello world", t stays "hello"
# - LeetCode Connection: Key for Two Pointer problems (e.g., reversing strings or finding substrings).

# 4. Tuples 
# - A fixed collection of items, like (1, 2, "hi")
# - Immutable (can’t change items inside).
# - Common Operations: Access items ([index]), unpack (a, b = tuple).
# - Ex:
tup = (1, 2, 3)
# tup[0] = 4  # Error! Tuples can’t be changed
a, b, c = tup  # Unpacks to a=1, b=2, c=3
# - LeetCode Connection: Great for grouping data that won’t change, like coordinates or pairs.

# 5. Lists 
# - A changeable collection of items, like [1, 2, 3]
# - Mutable (you can add, remove, or edit items).
# - Common Operations: Add (.append()), remove (.pop()), slice ([start:end]).
# - Ex:
lst = [1, 2, 3]
lst.append(4)  # lst becomes [1, 2, 3, 4]
lst[0] = 0     # lst is now [0, 2, 3, 4]
# - LeetCode Connection: A superstar in Fixed/Dynamic Sliding Window and Prefix Sum—think arrays or subarrays.

# 6. Dictionaries 
# - Pairs of keys and values, like {"name": "Alice", "age": 25}
# - Mutable (add, remove, or change pairs).
# - Common Operations: Add (dict[key] = value), get (dict[key]), delete (del dict[key]).
# - Ex:
d = {"a": 1, "b": 2}
d["c"] = 3  # d is now {"a": 1, "b": 2, "c": 3}
del d["a"]  # d is now {"b": 2, "c": 3}
# - LeetCode Connection: Perfect for fast lookups (e.g., counting elements or tracking sums in Prefix Sum).

# 7. Sets 
# - A collection of unique items, like {1, 2, 3}
# - Mutable (add or remove items, but items must be immutable).
# - Common Operations: Add (.add()), remove (.remove()).
# - Ex:
s = {1, 1, 2, 3}
s.add(4)     # s is now {1, 2, 3, 4}
s.remove(2)  # s is now {1, 3, 4}
# - LeetCode Connection: Awesome for checking uniqueness or overlaps in Two Pointer problems.

# 8. Boolean 
# - True or False values, used for logic and conditions.
# - Immutable (you can't change True into False).
# - Common Operations: Logical (and, or, not), comparisons (==, !=, >, <).
# - Ex:
is_valid = True
is_empty = False
result = is_valid and not is_empty   # True
# - LeetCode Connection: Controls flow in every problem (while loops, if conditions, DFS/BFS visited checks).



# ======================================================================
# Must-Know Gotchas: Mutable vs Immutable

# 1. Only immutable types can be dict keys or set elements
#    → Hashable: int, str, tuple, bool, float
#    → Unhashable: list, dict, set → TypeError


# 2. Tuples are immutable but can contain mutable objects
t = (1, [2, 3], 4)
t[1].append(5)      # allowed → (1, [2, 3, 5], 4)
# But you can’t replace the list itself:
t[1] = [6, 7]       # TypeError → This would fail


# 3. Mutable assignment shares the same object (watch out!)
    # - Mutable (list, dict, set): Assignment = same object → changes affect both
lst1 = [1, 2, 3]
lst2 = lst1          # points to SAME list
lst2.append(4)
print(lst1)          # [1, 2, 3, 4]  ← surprise!

# Fix: make real copy
lst3 = lst1.copy()   # or lst1[:]
lst3.append(5)       # lst1 stays unchanged


# 4. Small integers (and some strings) get reused in memory
    # - Immutable (int, str, tuple, etc.): Assignment = safe, no shared changes
x = 5
y = x
y = 10
print(x)             # still 5

# Memory trick (cool optimization)
a = 256
b = 256
print(a is b)        # True → Python reuses the same object (small ints & some strings)


# 5. Functions only mutate mutable arguments (not immutables)
def modify_list(l):
    l.append(99)     # changes the original list!

def modify_int(n):
    n += 1           # creates new int, original unchanged

my_list = [1, 2]
modify_list(my_list)
print(my_list)       # [1, 2, 99]

my_num = 10
modify_int(my_num)
print(my_num)        # 10


# Quick speed note
# Mutable → fast in-place changes
# Immutable → creates new objects → slow in loops (string +=)