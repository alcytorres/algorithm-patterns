# Python Data Types: A Beginner-Friendly Guide

# Welcome to this guide on Python data types! If you're aiming to become a pro at LeetCode data structures
# and algorithm problems, understanding data types is your first step. This guide focuses on mutable and
# immutable types, explains them with simple examples, and connects them to patterns like Two Pointer,
# Prefix Sum, Fixed Sliding Windows, and Dynamic Sliding Window. Let’s dive in!

# What are Data Types?
# In Python, data types are like containers that hold different kinds of values (numbers, text, collections, etc.).
# Each type has rules about what you can do with it. Some can change after creation (mutable), while others cannot (immutable).

# Mutable vs. Immutable: What Do They Mean?
# - Mutable: These are data types you can change after creating them. Think of them like a notebook where you can erase and rewrite.
#   Examples include lists, dictionaries, and sets.
# - Immutable: These are data types you can’t change once created. It’s like writing in permanent marker—any “change” makes a new copy.
#   Examples include integers, strings, and tuples.
# Knowing this difference helps you manage data efficiently in LeetCode problems, especially for optimizing time and space.

# Data Types from Simplest to Most Complex
# Below, we’ll explore each data type with definitions, examples, and how they tie into LeetCode patterns.

# 1. Integers (int)
# - What it is: Whole numbers (no decimals), like 5 or -10.
# - Mutable or Immutable: Immutable (changing it creates a new number).
# - Common Operations: Add (+), subtract (-), multiply (*), divide (/).
# - Example:
a = 5
b = a  # b gets 5
a = 10  # a is now 10, but b stays 5 because integers are immutable
# - LeetCode Connection: Used everywhere—counting steps, array indices, or sums in Prefix Sum problems.

# 2. Floats (float)
# - What it is: Numbers with decimals, like 3.14 or -0.5.
# - Mutable or Immutable: Immutable (modifying makes a new float).
# - Common Operations: Arithmetic (+, -, *, /), comparisons (<, >).
# - Example:
x = 3.14
y = x  # y is 3.14
x = 2.71  # x is now 2.71, y stays 3.14
# - LeetCode Connection: Handy for precise calculations, like averages or ratios in numeric problems.

# 3. Strings (str)
# - What it is: Text or characters, like "hello" or "123".
# - Mutable or Immutable: Immutable (can’t edit the text directly).
# - Common Operations: Join (+), slice ([start:end]), get character ([index]).
# - Example:
s = "hello"
t = s  # t is "hello"
s = s + " world"  # s becomes "hello world", t stays "hello"
# - LeetCode Connection: Key for Two Pointer problems (e.g., reversing strings or finding substrings).

# 4. Tuples (tuple)
# - What it is: A fixed collection of items, like (1, 2, "hi").
# - Mutable or Immutable: Immutable (can’t change items inside).
# - Common Operations: Access items ([index]), unpack (a, b = tuple).
# - Example:
tup = (1, 2, 3)
# tup[0] = 4  # Error! Tuples can’t be changed
a, b, c = tup  # Unpacks to a=1, b=2, c=3
# - LeetCode Connection: Great for grouping data that won’t change, like coordinates or pairs.

# 5. Lists (list)
# - What it is: A changeable collection of items, like [1, 2, 3].
# - Mutable or Immutable: Mutable (you can add, remove, or edit items).
# - Common Operations: Add (.append()), remove (.pop()), slice ([start:end]).
# - Example:
lst = [1, 2, 3]
lst.append(4)  # lst becomes [1, 2, 3, 4]
lst[0] = 0     # lst is now [0, 2, 3, 4]
# - LeetCode Connection: A superstar in Fixed/Dynamic Sliding Window and Prefix Sum—think arrays or subarrays.

# 6. Dictionaries (dict)
# - What it is: Pairs of keys and values, like {"name": "Alice", "age": 25}.
# - Mutable or Immutable: Mutable (add, remove, or change pairs).
# - Common Operations: Add (dict[key] = value), get (dict[key]), delete (del dict[key]).
# - Example:
d = {"a": 1, "b": 2}
d["c"] = 3  # d is now {"a": 1, "b": 2, "c": 3}
del d["a"]  # d is now {"b": 2, "c": 3}
# - LeetCode Connection: Perfect for fast lookups (e.g., counting elements or tracking sums in Prefix Sum).

# 7. Sets (set)
# - What it is: A collection of unique items, like {1, 2, 3}.
# - Mutable or Immutable: Mutable (add or remove items, but items must be immutable).
# - Common Operations: Add (.add()), remove (.remove()), union (|, .union()).
# - Example:
s = {1, 2, 3}
s.add(4)     # s is now {1, 2, 3, 4}
s.remove(2)  # s is now {1, 3, 4}
# - LeetCode Connection: Awesome for checking uniqueness or overlaps in Two Pointer problems.


# Extra Data Types (Good to Know)
# These are less common but useful in specific cases.

# 8. Frozensets (frozenset)
# - What it is: Like sets, but unchangeable, like frozenset([1, 2, 3]).
# - Mutable or Immutable: Immutable.
# - Common Operations: Union (|, .union()), intersection (&, .intersection()).
# - Example:
fs = frozenset([1, 2, 3])
# fs.add(4)  # Error! Frozensets are immutable
# - LeetCode Connection: Rare, but useful as dictionary keys when you need an unchangeable set.

# 9. Bytearrays (bytearray)
# - What it is: A changeable sequence of bytes (raw data), like bytearray(b"hi").
# - Mutable or Immutable: Mutable.
# - Common Operations: Edit bytes ([index] = value), convert to/from strings.
# - Example:
ba = bytearray(b"hello")
ba[0] = 104  # Changes first byte to 'h' (ASCII 104), still b"hello"
# - LeetCode Connection: Rare, but could appear in binary or low-level data problems.

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

# Why This Guide is the Best for Your LeetCode Journey
# This guide is crafted for you—a beginner aiming to master LeetCode patterns like Two Pointer, Prefix Sum,
# Fixed Sliding Windows, and Dynamic Sliding Window. Here’s why it’s perfect:
# - LeetCode-Focused: Highlights data types you’ll use most (lists, strings, dictionaries) and links them to your patterns.
# - Mutability Clarity: Knowing what’s mutable helps you avoid bugs and optimize solutions (e.g., reusing a list in Sliding Windows).
# - Simple Examples: Easy-to-follow examples build your confidence for coding real problems.
# - Beginner-Friendly: No confusing terms—just clear, engaging explanations to get you started fast.
# With this foundation, you’ll pick the right data type for each problem and solve them like a pro!

# Let’s Get Coding!
# Now that you understand Python data types, try them out in small examples. Then, tackle LeetCode problems
# using lists for Sliding Windows, dictionaries for Prefix Sums, or strings for Two Pointer challenges.
# Happy coding, and good luck on your LeetCode adventure!