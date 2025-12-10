# Lambda Functions in Python - Interview-Ready Guide
# Perfect for entry-level software engineer interviews
# Focus: String/Array manipulation + Sorting/Searching
# Style: Clear, beginner-friendly, practical, job-focused

# ===============================
# What is a Lambda Function?
# ===============================
# A lambda function is a small, anonymous (nameless) function.
# It's defined using the `lambda` keyword and can have any number of arguments, but only ONE expression (no multiple statements).

# Regular function:
def square(x):
    return x * x

# Lambda version (same thing, shorter):
square_lambda = lambda x: x * x

print(square(5))         # Outputs: 25
print(square_lambda(5))  # Outputs: 25

# Why "anonymous"?
# - A normal function is usually named and reused.
# - A lambda is often used once, inline, then forgotten.
#   → Perfect as a "quick helper" passed into other functions.

# Important limitation (one expression rule):
# - Inside a lambda, you CANNOT use:
#   if/else blocks, for/while loops, return, or assignment (=) as separate statements.
# - You can only write a single expression, like: x + 1, x * 2, len(s), s.upper(), etc.


# ===============================
# Lambda Syntax
# ===============================
lambda arguments : expression

# Examples:
lambda x: x + 1           # Takes x, returns x + 1
lambda x, y: x + y        # Takes two args
lambda s: s.upper()       # String manipulation
lambda num: num % 2 == 0  # Returns True if even

# You can assign it to a variable (but usually you don't)
add_one = lambda x: x + 1
print(add_one(10))  # Outputs: 11


# ===============================
# Lambda #1: Sorting Lists (MOST COMMON INTERVIEW USE)
# ===============================
# sorted() and list.sort() accept a `key` parameter.
# The key is a function that produces a value to sort by.
# Lambda is PERFECT here.

# Sort list of strings by length
words = ["apple", "hi", "banana", "cat"]
sorted_by_length = sorted(words, key=lambda word: len(word))
print(sorted_by_length)
# Outputs: ['hi', 'cat', 'apple', 'banana']

# Sort list of tuples by second element
pairs = [(1, "one"), (3, "three"), (2, "two"), (4, "four")]
sorted_by_second = sorted(pairs, key=lambda pair: pair[1])
print(sorted_by_second)
# Outputs: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

# Sort list of names by last name
names = ["John Smith", "Amy Johnson", "Bob Williams", "Eve Brown"]
sorted_by_last_name = sorted(names, key=lambda name: name.split()[-1])
print(sorted_by_last_name)
# Outputs: ['Eve Brown', 'Amy Johnson', 'John Smith', 'Bob Williams']

# Reverse sort (descending) — clearer version using reverse=True
numbers = [5, 8, 1]
sorted_desc = sorted(numbers, reverse=True)
print(sorted_desc)  # Outputs: [8, 5, 1]

# (You *can* also do key=lambda x: -x, but reverse=True is more readable.)


# ===============================
# Lambda #2: map() - Transform Every Item (Array Manipulation)
# ===============================
# map(function, iterable) applies a function to every item.

nums = [1, 2, 3, 4, 5]

# Square every number
squared = list(map(lambda x: x * 2, nums))
print(squared)  # Outputs: [2, 4, 6, 8, 10]

# Or square using **2
squared_pow = list(map(lambda x: x**2, nums))
print(squared_pow)  # Outputs: [1, 4, 9, 16, 25]

# Convert numbers to strings
strings = list(map(lambda x: str(x), nums))
print(strings)  # Outputs: ['1', '2', '3', '4', '5']

# String manipulation: make uppercase
words = ["hello", "world", "python"]
upper = list(map(lambda s: s.upper(), words))
print(upper)  # Outputs: ['HELLO', 'WORLD', 'PYTHON']

# Extract first letter
first_letters = list(map(lambda s: s[0], words))
print(first_letters)  # Outputs: ['h', 'w', 'p']


# ===============================
# Lambda #3: filter() - Keep Only Matching Items
# ===============================
# filter(function, iterable) keeps items where function returns True.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Outputs: [2, 4, 6, 8, 10]

# Keep only numbers > 5
greater_than_5 = list(filter(lambda x: x > 5, nums))
print(greater_than_5)  # Outputs: [6, 7, 8, 9, 10]

# Filter strings longer than 5 characters
words = ["hi", "hello", "python", "a", "world"]
long_words = list(filter(lambda s: len(s) > 5, words))
print(long_words)  # Outputs: ['python', 'world']


# ===============================
# Lambda in Interviews: Real Examples
# ===============================


# Example 1: Sort list of strings by length (descending)
words = ["zzz", "a", "bb", "cccc"]
result = sorted(words, key=lambda s: len(s), reverse=True)
print(result)  # Outputs: ['cccc', 'zzz', 'bb', 'a']

# Example 2: Sort list of lists by sum
lists = [[1, 2], [3], [4, 5, 6], [2, 2]]
result = sorted(lists, key=lambda lst: sum(lst))
print(result)  # Outputs: [[3], [1, 2], [2, 2], [4, 5, 6]]

# Example 3: Find max string by length
words = ["apple", "hi", "banana"]
longest = max(words, key=lambda s: len(s))
print(longest)  # Outputs: banana

# Example 4: Group numbers into even/odd
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
odds = list(filter(lambda x: x % 2 != 0, numbers))
print("Evens:", evens)  # [2, 4]
print("Odds:", odds)    # [1, 3, 5]


# ===============================
# When to Use Lambda (Interview Wisdom)
# ===============================
# Use lambda when:
# - You're using sorted(), map(), filter(), max(), min()
# - The function is short and simple (one quick expression)
# - You don't need to reuse it elsewhere

# DON'T use lambda for complex logic — use a real function.

# Good (interview-friendly)
sorted(names, key=lambda x: x.split()[-1])

# Bad (hard to read)
sorted(data, key=lambda x: x[2][1].lower() if len(x) > 2 else "")

# Better: define a helper function
def get_sort_key(item):
    return item[2][1].lower() if len(item) > 2 else ""


# ===============================
# Summary: Lambda Functions for Job Interviews
# ===============================
# Master these 3 patterns — you'll see them in 90% of lambda questions:

# 1. Sorting with key
sorted(data, key=lambda x: x.something)

# 2. map() for transformation
list(map(lambda x: x.do_something(), items))

# 3. filter() for selection
list(filter(lambda x: condition(x), items))

# Core mental model:
#   • Lambda = tiny, one-line function
#   • Mostly used as a helper for key=, map(), filter(), max(), min()
#   • Keep it simple and readable — or use a normal def instead.

# Practice these and you're ready for any entry-level interview!
