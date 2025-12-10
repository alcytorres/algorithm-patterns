
# ===============================
# GUIDE: key= Superpower — Sorting & Selecting the Smart Way
# Perfect for DSA interviews: arrays, strings, frequency problems
# ===============================

"""
Rule to remember:
    key=   → "Sort or pick based on this function's result"

BIG IDEA:
    key= lets you tell Python:
        "Don't compare the items directly — compare THIS instead."

You'll use this with:
    • sorted()
    • list.sort()
    • max()
    • min()

This shows up CONSTANTLY in real code + DSA problems.
"""


# ===============================
# 1) key= with max() and min() — Pick Best Item by a Rule
# ===============================

words = ["hi", "banana", "cat"]
print(max(words))              # Alphabet rules → 'hi'
print(max(words, key=len))     # Compare length → 'banana'

nums = [-10, -3, 2]
print(min(nums, key=abs))      # Closest to 0 → -3


# DSA: most frequent number (Majority Element idea)
counts = {3: 4, 5: 2, 7: 1}
print(max(counts, key=counts.get))  # 3 (largest frequency)


# ===============================
# 2) key= with sorted() — Sort by a Rule
# ===============================

words = ["apple", "hi", "banana"]
print(sorted(words, key=len))  # ['hi', 'apple', 'banana']
print(sorted(words, key=len, reverse=True))  # ['banana', 'apple', 'hi']


# Sort tuples by second value
pairs = [(1, "b"), (3, "c"), (2, "a")]
print(sorted(pairs, key=lambda p: p[1]))
# → [(2, 'a'), (1, 'b'), (3, 'c')]


# Sort full names by last name (VERY common)
names = ["Amy Johnson", "Bob Lee", "John Smith"]
print(sorted(names, key=lambda n: n.split()[-1]))
# → ['Amy Johnson', 'Bob Lee', 'John Smith']


# ===============================
# 3) reverse=True → Flip the order (Works with or without key)
# ===============================

nums = [1, 4, 10]

# Normal ascending
print(sorted(nums))  # [1, 4, 10]

# Descending
print(sorted(nums, reverse=True))  # [10, 4, 1]

# Combine with key: longest word first
words = ["a", "bbbb", "ccc"]
print(sorted(words, key=len, reverse=True))  # ['bbbb', 'ccc', 'a']


# ===============================
# 4) Mental model (memorize THIS)
# ===============================

"""
✔ max(..., key=fn)     → "Pick the item where fn(item) is biggest"
✔ min(..., key=fn)     → "Pick the smallest by fn(item)"
✔ sorted(..., key=fn)  → "Order items by fn(item)"
✔ reverse=True         → Just flip the result
"""


# ===============================
# Interview Use Cases (90% of problems)
# ===============================

"""
Mental model:
    • max(..., key=fn)     → “Pick the element whose fn(x) is biggest.”
    • min(..., key=fn)     → “Pick the element whose fn(x) is smallest.”
    • sorted(..., key=fn)  → “Order elements by fn(x).”
    • reverse=True         → “Flip the final order.”

Common interview uses (arrays / strings):
    • Sort strings by length:      sorted(words, key=len)
    • Sort by frequency:           sorted(freq.items(), key=lambda x: x[1])
    • Get most frequent element:   max(freq, key=freq.get)
    • Sort tuples by index:        sorted(pairs, key=lambda x: x[1])
    • Sort names by last name:     sorted(names, key=lambda n: n.split()[-1])

If you master:
    • key=
    • reverse=
    • lambda (one-line functions)

…you'll be in great shape for string/array + sorting/searching questions.

"""
