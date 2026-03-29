# ===============================
# GUIDE: What is key= used for?
# Sorting & Selecting the Smart Way
# key= in max(), min(), Passing Functions
# Perfect for DSA interviews: arrays, strings, frequency problems
# ===============================

"""
What is key= ?

    key= tells Python HOW TO COMPARE the items.
    Instead of comparing items by their face value,
    it calls the function you give it on each item
    and compares THOSE RESULTS instead.

    It changes the RULER, not what gets returned.

    • Without key=  
    →  max([3, 1, 2])  →  compares 3, 1, 2 directly  
    →  returns 3

    • With key=     
    →  max(["hi", "banana"], key=len)  →  compares lengths  
    →  returns "banana"


Important rule:
    key= expects a FUNCTION, not a result.

    • count.get      → gives max() a TOOL to use later  ✅
    • count.get()    → runs the tool right now (wrong)   ❌

TLDR:
    key=   → "Sort or pick based on this function's result"

Why no parentheses?
    We want max() to CALL the function for us internally
    on each item it checks. 
    We hand over the tool — max() decides when to use it.


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


# Sort full names by last name (VERY common)
def get_last_name(name):
    return name.split()[-1]

names = ["John Smith", "Bob Lee", "Amy Adams"]
print(sorted(names, key=get_last_name))
# → ['Amy Adams', 'Bob Lee', 'John Smith']

# Behind the scenes:
#   1. sorted() loops through names
#   2. For each one, it calls get_last_name() to decide how to compare:
#        get_last_name("John Smith") → "Smith"
#        get_last_name("Bob Lee")    → "Lee"
#        get_last_name("Amy Adams")  → "Adams"
#   3. Python internally holds those results: ["Smith", "Lee", "Adams"]
#   4. Sorts by those results: "Adams" < "Lee" < "Smith"
#   5. Returns the original names in that order: ['Amy Adams', 'Bob Lee', 'John Smith']


# Sort full names by last name (Using Lambda)
names = ["Amy Adams", "Bob Lee", "John Smith"]
print(sorted(names, key=lambda n: n.split()[-1]))
# → ['Amy Adams', 'Bob Lee', 'John Smith']



# Sort tuples by second value
def get_second(pair):
    return pair[1]

pairs = [(1, "b"), (3, "c"), (2, "a")]
print(sorted(pairs, key=get_second))
# → [(2, 'a'), (1, 'b'), (3, 'c')]

# Behind the scenes:
#   1. sorted() loops through pairs
#   2. For each one, it calls get_second() to decide how to compare:
#        get_second((1, "b"))  → "b"
#        get_second((3, "c"))  → "c"
#        get_second((2, "a"))  → "a"
#   3. Python internally holds those results: ["b", "c", "a"]
#   4. Sorts by those results: "a" < "b" < "c"
#   5. Returns the original tuples in that order: [(2, 'a'), (1, 'b'), (3, 'c')]



# Sort tuples by second value (Using Lambda)
pairs = [(1, "b"), (3, "c"), (2, "a")]
print(sorted(pairs, key=lambda p: p[1]))
# → [(2, 'a'), (1, 'b'), (3, 'c')]



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
Mental model:
  ✔ max(..., key=fn)     → "Pick the item where fn(item) is biggest"
  ✔ min(..., key=fn)     → "Pick the smallest by fn(item)"
  ✔ sorted(..., key=fn)  → "Order items by fn(item)"
  ✔ reverse=True         → Flip the final order
"""


# ===============================
# Interview Use Cases (90% of problems)
# ===============================
"""
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
