# STRING METHODS
# ----------------------------------------------------------------------------------
# STRING METHOD: 
.upper()
# What it does: Converts all characters in a string to uppercase.
# Why use it: Standardizes text for comparisons or display.
# How it works: Returns a new string; original unchanged.
# When to use: Case-insensitive matching in palindromes or anagrams.
# Time/Space: O(n) time (n = string length), O(n) space for new string.

# Syntax:
string.upper()  # Returns a new string with all uppercase letters

# Basic Example 1 (Simple String):
text = "hello"
print(text.upper())  # Output: "HELLO"

# Basic Example 2 (Mixed Case):
text = "Hello World"
print(text.upper())  # Output: "HELLO WORLD"

# Basic Example 3 (Empty String):
text = ""
print(text.upper())  # Output: ""

# DSA Example (Palindrome Prep):
word = "RaCeCaR"
print(word.upper())  # Output: "RACECAR"


# STRING METHOD: 
.lower()
# What it does: Converts all characters in a string to lowercase.
# Why use it: Normalizes text for case-insensitive searches.
# How it works: Returns a new string; original unchanged.
# When to use: Standardizing input in string pattern problems.
# Time/Space: O(n) time (n = string length), O(n) space for new string.

# Syntax:
string.lower()  # Returns a new string with all lowercase letters

# Basic Example 1 (Simple String):
text = "WORLD"
print(text.lower())  # Output: "world"

# Basic Example 2 (Mixed Case):
text = "Hello World"
print(text.lower())  # Output: "hello world"

# Basic Example 3 (Empty String):
text = ""
print(text.lower())  # Output: ""

# DSA Example (Anagram Prep):
word = "Listen"
print(word.lower())  # Output: "listen"


# STRING METHOD: 
.replace()
# What it does: Replaces occurrences of a substring with another.
# Why use it: Modifies specific parts of strings efficiently.
# How it works: Returns a new string; optional count parameter.
# When to use: Cleaning or transforming strings in text processing.
# Time/Space: O(n) time (n = string length), O(n) space for new string.

# Syntax:
string.replace(old, new)  # Returns new string with 'old' replaced by 'new'

# Basic Example 1 (Simple Replace):
text = "hello world"
print(text.replace("world", "python"))  # Output: "hello python"

# Basic Example 2 (Multiple Occurrences):
text = "cat cat cat"
print(text.replace("cat", "dog"))  # Output: "dog dog dog"

# Basic Example 3 (No Match):
text = "hello"
print(text.replace("world", "python"))  # Output: "hello"

# DSA Example (Clean String):
text = "a#a#a"
print(text.replace("#", ""))  # Output: "aaa"


# STRING METHOD: 
.isdigit()
# What it does: Checks if all characters are digits.
# Why use it: Validates numeric strings quickly.
# How it works: Returns True/False; checks ASCII digits 0-9.
# When to use: Parsing inputs in numeric validation problems.
# Time/Space: O(n) time (n = string length), O(1) space.

# Syntax:
string.isdigit()  # Returns True if all characters are digits, else False

# Basic Example 1 (All Digits):
text = "123"
print(text.isdigit())  # Output: True

# Basic Example 2 (With Letters):
text = "12a3"
print(text.isdigit())  # Output: False

# Basic Example 3 (Empty String):
text = ""
print(text.isdigit())  # Output: False

# DSA Example (Input Validation):
text = "123"
print(text.isdigit())  # Output: True


# STRING METHOD: 
.isnumeric()
# What it does: Checks if all characters are numeric.
# Why use it: Validates broader numeric strings including Unicode.
# How it works: Returns True/False; more inclusive than .isdigit().
# When to use: Robust numeric checks in international inputs.
# Time/Space: O(n) time (n = string length), O(1) space.

# Syntax:
string.isnumeric()  # Returns True if all characters are numeric, else False

# Basic Example 1 (All Digits):
text = "123"
print(text.isnumeric())  # Output: True

# Basic Example 2 (With Letters):
text = "12a3"
print(text.isnumeric())  # Output: False

# Basic Example 3 (Unicode Numeric):
text = "½"
print(text.isnumeric())  # Output: True

# DSA Example (Numeric Validation):
text = "123"
print(text.isnumeric())  # Output: True


# STRING METHOD: 
.split()
# What it does: Splits string into list based on delimiter.
# Why use it: Parses strings into tokens efficiently.
# How it works: Default delimiter is whitespace; optional maxsplit.
# When to use: Tokenizing inputs in word or array problems.
# Time/Space: O(n) time (n = string length), O(n) space for list.

# Syntax:
string.split(separator)  # Returns list; 'separator' optional (defaults to whitespace)

# Basic Example 1 (Default Whitespace):
text = "hello world"
print(text.split())  # Output: ['hello', 'world']

# Basic Example 2 (Custom Delimiter):
text = "a,b,c"
print(text.split(','))  # Output: ['a', 'b', 'c']

# Basic Example 3 (No Delimiter):
text = "abc"
print(text.split())  # Output: ['abc']

# DSA Example (Word Parsing):
text = "hello world"
print(text.split())  # Output: ['hello', 'world']


# STRING METHOD: 
.format()
# What it does: Formats string with placeholders.
# Why use it: Builds dynamic strings easily.
# How it works: Replaces {} with args or named values.
# When to use: Formatting outputs in debugging or results.
# Time/Space: O(n) time (n = string length), O(n) space for string.

# Syntax:
string.format(*args, **kwargs)  # Returns formatted string; placeholders like {}

# Basic Example 1 (Positional):
template = "Value: {}"
print(template.format(42))  # Output: "Value: 42"

# Basic Example 2 (Multiple):
template = "{} + {} = {}"
print(template.format(1, 2, 3))  # Output: "1 + 2 = 3"

# Basic Example 3 (Named):
template = "{name}: {age}"
print(template.format(name="Alice", age=25))  # Output: "Alice: 25"

# DSA Example (Format Result):
template = "Value: {}"
print(template.format(42))  # Output: "Value: 42"


# STRING METHOD: 
.join()
# What it does: Joins iterable elements into string with separator.
# Why use it: Builds strings from lists efficiently.
# How it works: Iterable must contain strings; concatenates with separator.
# When to use: Constructing outputs from token lists.
# Time/Space: O(n) time (n = total length), O(n) space for string.

# Syntax:
separator.join(iterable)  # Returns string from 'iterable' elements

# Basic Example 1 (Space Separator):
words = ["hello", "world"]
print(" ".join(words))  # Output: "hello world"

# Basic Example 2 (Comma Separator):
chars = ["a", "b", "c"]
print(",".join(chars))  # Output: "a,b,c"

# Basic Example 3 (No Separator):
chars = ["a", "b"]
print("".join(chars))  # Output: "ab"

# Basic Example 4 (Arrow Separator):
words = ["1", "2", "3", "4"]
print(" -> ".join(words))

# DSA Example (List to String):
words = ["hello", "world"]
print(" ".join(words))  # Output: "hello world"




# LIST METHODS
# ----------------------------------------------------------------------------------
# LIST METHOD: 
.append()
# What it does: Adds a single element to the end of a list.
# Why use it: Grows lists dynamically.
# How it works: Modifies in place; amortized O(1) time.
# When to use: Collecting results or stack push in loops.
# Time/Space: O(1) amortized time, O(1) space per call.

# Syntax:
list.append(item)  # Adds 'item' to end

# Basic Example 1 (Empty List):
lst = []
lst.append(1)
print(lst)  # Output: [1]

# Basic Example 2 (Add Number):
lst = [1, 2]
lst.append(3)
print(lst)  # Output: [1, 2, 3]

# Basic Example 3 (Add String):
lst = ["a", "b"]
lst.append("c")
print(lst)  # Output: ["a", "b", "c"]

# DSA Example (Build Result in Loop):
result = []
for i in range(3):
    result.append(i)
print(result)  # Output: [0, 1, 2]


# LIST METHOD: 
.extend()
# What it does: Adds multiple elements from iterable to list end.
# Why use it: Combines lists efficiently.
# How it works: Modifies in place; iterates over iterable.
# When to use: Merging arrays or collecting batches.
# Time/Space: O(k) time (k = iterable length), O(k) space.

# Syntax:
list.extend(iterable)  # Adds items from 'iterable'

# Basic Example 1 (Extend List):
lst = [1, 2]
lst.extend([3, 4])
print(lst)  # Output: [1, 2, 3, 4]

# Basic Example 2 (Extend String):
lst = ["a"]
lst.extend("bc")
print(lst)  # Output: ["a", "b", "c"]

# Basic Example 3 (Empty Iterable):
lst = [1]
lst.extend([])
print(lst)  # Output: [1]

# DSA Example (Merging Arrays):
result = [1, 2]
result.extend([3, 4])
print(result)  # Output: [1, 2, 3, 4]


# LIST METHOD: 
.insert()
# What it does: Inserts element at specified index.
# Why use it: Adds at specific positions.
# How it works: Shifts elements right; modifies in place.
# When to use: Maintaining sorted order in arrays.
# Time/Space: O(n) time (shifting), O(1) space per call.

# Syntax:
list.insert(index, item)  # Inserts 'item' at 'index'

# Basic Example 1 (Insert Middle):
lst = [1, 3]
lst.insert(1, 2)
print(lst)  # Output: [1, 2, 3]

# Basic Example 2 (Insert Start):
lst = [2, 3]
lst.insert(0, 1)
print(lst)  # Output: [1, 2, 3]

# Basic Example 3 (Insert End):
lst = [1, 2]
lst.insert(2, 3)
print(lst)  # Output: [1, 2, 3]

# DSA Example (Insert in Sorted List):
numbers = [1, 3]
numbers.insert(1, 2)
print(numbers)  # Output: [1, 2, 3]


# LIST METHOD: 
.remove()
# What it does: Removes first occurrence of value.
# Why use it: Deletes by value, not index.
# How it works: Searches linearly; raises ValueError if not found.
# When to use: Removing duplicates or invalid items.
# Time/Space: O(n) time (search), O(1) space.

# Syntax:
list.remove(value)  # Removes first 'value'

# Basic Example 1 (Remove Value):
lst = [1, 2, 3]
lst.remove(2)
print(lst)  # Output: [1, 3]

# Basic Example 2 (Multiple Occurrences):
lst = [1, 2, 2]
lst.remove(2)
print(lst)  # Output: [1, 2]

# Basic Example 3 (No Value):
# lst = [1, 2]
# lst.remove(3)  # Raises ValueError

# DSA Example (Remove Duplicate):
numbers = [1, 2, 2]
numbers.remove(2)
print(numbers)  # Output: [1, 2]


# LIST METHOD: 
.pop()
# What it does: Removes and returns element at index (default last).
# Why use it: Removes while retrieving value.
# How it works: Shifts if not last; modifies in place.
# When to use: Implementing stacks or queues.
# Time/Space: O(1) for last, O(n) otherwise, O(1) space.

# Syntax:
list.pop(index)  # Removes/returns at 'index' (optional, defaults -1)

# Basic Example 1 (Pop Last):
lst = [1, 2, 3]
item = lst.pop()
print(item, lst)  # Output: 3 [1, 2]

# Basic Example 2 (Pop Index):
lst = [1, 2, 3]
item = lst.pop(1)
print(item, lst)  # Output: 2 [1, 3]

# Basic Example 3 (Empty List):
# lst = []
# lst.pop()  # Raises IndexError

# DSA Example (Stack Pop):
stack = [1, 2, 3]
last = stack.pop()
print(last, stack)  # Output: 3 [1, 2]




# DICTIONARY METHODS
# ----------------------------------------------------------------------------------
# DICTIONARY METHOD: 
.keys()
# What it does: Returns view of dictionary keys.
# Why use it: Accesses keys for iteration.
# How it works: Dynamic view; changes with dict.
# When to use: Looping over keys in hash maps.
# Time/Space: O(1) for view, O(n) for list conversion.

# Syntax:
dict.keys()  # Returns keys view

# Basic Example 1 (Get Keys):
d = {"a": 1, "b": 2}
print(list(d.keys()))  # Output: ["a", "b"]

# Basic Example 2 (Empty Dict):
d = {}
print(list(d.keys()))  # Output: []

# Basic Example 3 (Check Key):
d = {"a": 1}
print("a" in d.keys())  # Output: True

# DSA Example (Key Iteration):
ages = {"Alice": 25, "Bob": 30}
print(list(ages.keys()))  # Output: ["Alice", "Bob"]


# DICTIONARY METHOD: 
.get()
# What it does: Gets value for key, default if missing.
# Why use it: Safe access without KeyError.
# How it works: O(1) lookup; optional default.
# When to use: Frequency counts in hash maps.
# Time/Space: O(1) average time, O(1) space.

# Syntax:
dict.get(key, default)  # Returns value or 'default' (None if omitted)

# Basic Example 1 (Existing Key):
d = {"a": 1}
print(d.get("a"))  # Output: 1

# Basic Example 2 (Missing Key):
d = {"a": 1}
print(d.get("b"))  # Output: None

# Basic Example 3 (With Default):
d = {"a": 1}
print(d.get("b", 0))  # Output: 0

# DSA Example (Frequency Count):
counts = {"a": 1}
counts["b"] = counts.get("b", 0) + 1
print(counts)  # Output: {"a": 1, "b": 1}


# DICTIONARY METHOD: 
.items()
# What it does: Returns view of key-value pairs as tuples.
# Why use it: Iterates over keys and values together.
# How it works: Dynamic view; changes with dict.
# When to use: Processing pairs in grouping problems.
# Time/Space: O(1) for view, O(n) for list conversion.

# Syntax:
dict.items()  # Returns (key, value) tuples view

# Basic Example 1 (Get Items):
d = {"a": 1, "b": 2}
print(list(d.items()))  # Output: [("a", 1), ("b", 2)]

# Basic Example 2 (Empty Dict):
d = {}
print(list(d.items()))  # Output: []

# Basic Example 3 (Loop Pairs):
d = {"a": 1, "b": 2}
for k, v in d.items():
    print(k, v)  # Output: a 1, b 2

# DSA Example (Key-Value Iteration):
ages = {"Alice": 25, "Bob": 30}
print(list(ages.items()))  # Output: [("Alice", 25), ("Bob", 30)]





# SET METHODS
# ----------------------------------------------------------------------------------
# SET METHOD: 
.add()
# What it does: Adds element if not present.
# Why use it: Builds unique collections efficiently.
# How it works: O(1) average; no duplicates.
# When to use: Deduplication or membership tracking.
# Time/Space: O(1) average time, O(1) space per add.

# Syntax:
set.add(element)  # Adds 'element' if unique

# Basic Example 1 (Add New):
s = {1, 2}
s.add(3)
print(s)  # Output: {1, 2, 3}

# Basic Example 2 (Add Duplicate):
s = {1, 2}
s.add(2)
print(s)  # Output: {1, 2}

# Basic Example 3 (Add String):
s = {"a"}
s.add("b")
print(s)  # Output: {"a", "b"}

# DSA Example (Track Unique):
unique = {1, 2}
unique.add(3)
print(unique)  # Output: {1, 2, 3}





# BUILT-IN FUNCTIONS
# ----------------------------------------------------------------------------------
# BUILT-IN FUNCTION: 
len()
# What it does: Returns number of items in object.
# Why use it: Checks size for loops or validations.
# How it works: O(1) for most collections.
# When to use: Bounds in arrays or strings.
# Time/Space: O(1) time, O(1) space.

# Syntax:
len(object)  # Returns integer length

# Basic Example 1 (List Length):
lst = [1, 2, 3]
print(len(lst))  # Output: 3

# Basic Example 2 (String Length):
text = "abc"
print(len(text))  # Output: 3

# Basic Example 3 (Empty):
lst = []
print(len(lst))  # Output: 0

# DSA Example (Array Length):
array = [1, 2, 3]
print(len(array))  # Output: 3


# BUILT-IN FUNCTION: 
str()
# What it does: Converts object to string representation.
# Why use it: Enables string ops on non-strings.
# How it works: Calls __str__ if defined.
# When to use: Formatting outputs or concatenation.
# Time/Space: O(n) time, O(n) space for string.

# Syntax:
str(object)  # Returns string rep

# Basic Example 1 (Number):
num = 123
print(str(num))  # Output: "123"

# Basic Example 2 (List):
lst = [1, 2]
print(str(lst))  # Output: "[1, 2]"

# Basic Example 3 (Bool):
b = True
print(str(b))  # Output: "True"

# DSA Example (Number to String):
num = 123
print(str(num) + " is a number")  # Output: "123 is a number"


# BUILT-IN FUNCTION: 
int()
# What it does: Converts value to integer.
# Why use it: Parses strings for arithmetic.
# How it works: Truncates floats; bases optional.
# When to use: Numeric parsing in inputs.
# Time/Space: O(n) time for strings, O(1) space.

# Syntax:
int(value)  # Converts to int

# Basic Example 1 (String):
s = "123"
print(int(s))  # Output: 123

# Basic Example 2 (Float):
f = 5.7
print(int(f))  # Output: 5

# Basic Example 3 (Binary String):
s = "101"
print(int(s, 2))  # Output: 5

# DSA Example (String to Number):
num = "123"
print(int(num) + 1)  # Output: 124


# BUILT-IN FUNCTION: 
float()
# What it does: Converts value to floating-point number.
# Why use it: Handles decimals in calculations.
# How it works: Parses strings or ints to float.
# When to use: Precision in numeric problems.
# Time/Space: O(n) time for strings, O(1) space.

# Syntax:
float(value)  # Converts to float

# Basic Example 1 (String):
s = "123.45"
print(float(s))  # Output: 123.45

# Basic Example 2 (Int):
i = 5
print(float(i))  # Output: 5.0

# Basic Example 3 (Empty):
# float("")  # Raises ValueError

# DSA Example (String to Float):
num = "123.45"
print(float(num) + 0.55)  # Output: 124.0


# BUILT-IN FUNCTION: 
input()
# What it does: Reads user input as string.
# Why use it: Gets interactive data.
# How it works: Optional prompt; strips newline.
# When to use: Testing or user-driven algorithms.
# Time/Space: O(n) time, O(n) space for string.

# Syntax:
input(prompt)  # Returns string; 'prompt' optional

# Basic Example 1 (No Prompt):
# input()  # Waits for input, returns string

# Basic Example 2 (With Prompt):
# input("Enter: ")  # Displays "Enter: ", returns input

# Basic Example 3 (Process Input):
# num = input("Num: ")
# print(int(num))  # Converts input to int

# DSA Example (Read Number):
# num = input("Enter number: ")
# print(int(num) + 1)  # Output: input + 1


# BUILT-IN FUNCTION: 
list()
# What it does: Creates list from iterable.
# Why use it: Converts to mutable list.
# How it works: Copies elements into new list.
# When to use: Manipulating converted data.
# Time/Space: O(n) time, O(n) space.

# Syntax:
list(iterable)  # New list from 'iterable'

# Basic Example 1 (String):
text = "abc"
print(list(text))  # Output: ["a", "b", "c"]

# Basic Example 2 (Tuple):
t = (1, 2)
print(list(t))  # Output: [1, 2]

# Basic Example 3 (Empty):
print(list())  # Output: []

# DSA Example (String to List):
text = "abc"
print(list(text))  # Output: ["a", "b", "c"]


# BUILT-IN FUNCTION: 
tuple()
# What it does: Creates tuple from iterable.
# Why use it: Immutable sequences for keys.
# How it works: Copies to immutable tuple.
# When to use: Fixed data in hash maps.
# Time/Space: O(n) time, O(n) space.

# Syntax:
tuple(iterable)  # New tuple from 'iterable'

# Basic Example 1 (List):
lst = [1, 2]
print(tuple(lst))  # Output: (1, 2)

# Basic Example 2 (String):
text = "ab"
print(tuple(text))  # Output: ("a", "b")

# Basic Example 3 (Empty):
print(tuple())  # Output: ()

# DSA Example (List to Tuple):
nums = [1, 2, 3]
print(tuple(nums))  # Output: (1, 2, 3)


# BUILT-IN FUNCTION: 
dict()
# What it does: Creates dict from pairs or kwargs.
# Why use it: Builds hash maps quickly.
# How it works: From iterable of pairs or args.
# When to use: Caching or counting in DSA.
# Time/Space: O(n) time, O(n) space.

# Syntax:
dict(iterable)  # From pairs or kwargs

# Basic Example 1 (Pairs List):
pairs = [("a", 1), ("b", 2)]
print(dict(pairs))  # Output: {"a": 1, "b": 2}

# Basic Example 2 (Kwargs):
print(dict(a=1, b=2))  # Output: {"a": 1, "b": 2}

# Basic Example 3 (Empty):
print(dict())  # Output: {}

# DSA Example (From List of Pairs):
pairs = [("a", 1), ("b", 2)]
print(dict(pairs))  # Output: {"a": 1, "b": 2}


# BUILT-IN FUNCTION: 
enumerate()
# What it does: Pairs indices with iterable elements.
# Why use it: Tracks position in loops.
# How it works: Returns iterator of (index, value).
# When to use: Index-based array operations.
# Time/Space: O(1) create, O(1) per iteration.

# Syntax:
enumerate(iterable, start=0)  # (index, value) tuples

# Basic Example 1 (Default Start):
nums = ["a", "b"]
for i, v in enumerate(nums):
    print(i, v)  # Output: 0 a, 1 b

# Basic Example 2 (Custom Start):
nums = ["a", "b"]
for i, v in enumerate(nums, 1):
    print(i, v)  # Output: 1 a, 2 b

# Basic Example 3 (To List):
nums = ["a"]
print(list(enumerate(nums)))  # Output: [(0, "a")]

# DSA Example (Index Tracking):
nums = ["a", "b"]
for i, val in enumerate(nums):
    print(i, val)  # Output: 0 a, 1 b


# BUILT-IN FUNCTION: 
iter()
# What it does: Creates iterator from iterable.
# Why use it: Manual control over iteration.
# How it works: Calls __iter__; pairs with next().
# When to use: Custom traversal in processing.
# Time/Space: O(1) time, O(1) space.

# Syntax:
iter(iterable)  # Returns iterator

# Basic Example 1 (List):
lst = [1, 2]
it = iter(lst)
print(next(it))  # Output: 1

# Basic Example 2 (String):
text = "ab"
it = iter(text)
print(next(it))  # Output: "a"

# Basic Example 3 (Type Check):
lst = [1]
it = iter(lst)
print(type(it))  # Output: <class 'list_iterator'>

# DSA Example (List Iterator):
nums = [1, 2, 3]
it = iter(nums)
print(next(it))  # Output: 1


# Create a list and get its iterator
nums = [1, 2, 3]
iterator = iter(nums)

# Use next() to get items one by one
print(next(iterator))  # Outputs: 1
print(next(iterator))  # Outputs: 2
print(next(iterator))  # Outputs: 3
print(next(iterator))  # Raises StopIteration (no more items)
print(next(iterator, "end"))  # Outputs: end

# Check the iterator type
print(type(iterator))  # Output: <class 'list_iterator'>
# -------------------------------------------------------------------------


# BUILT-IN FUNCTION: 
range()
# What it does: Generates number sequence.
# Why use it: Efficient looping without list.
# How it works: Lazy; stores start/stop/step.
# When to use: Iteration in arrays or matrices.
# Time/Space: O(1) time, O(1) space.

# Syntax:
range(stop)  # From 0 to 'stop-1'
range(start, stop, step)  # From 'start' to 'stop-1' with 'step'

# Basic Example 1 (Default):
print(list(range(3)))  # Output: [0, 1, 2]

# Basic Example 2 (Start/Stop):
print(list(range(1, 4)))  # Output: [1, 2, 3]

# Basic Example 3 (With Step):
print(list(range(0, 6, 2)))  # Output: [0, 2, 4]

# DSA Example (Loop Range):
print(list(range(3)))  # Output: [0, 1, 2]


# BUILT-IN FUNCTION: 
zip()
# What it does: Pairs elements from iterables.
# Why use it: Simultaneous iteration.
# How it works: Stops at shortest iterable.
# When to use: Merging or comparing arrays.
# Time/Space: O(1) create, O(1) per iteration.

# Syntax:
zip(*iterables)  # Iterator of tuples

# Basic Example 1 (Two Lists):
a = [1, 2]
b = ["a", "b"]
print(list(zip(a, b)))  # Output: [(1, "a"), (2, "b")]

# Basic Example 2 (Unequal Length):
a = [1, 2, 3]
b = ["a", "b"]
print(list(zip(a, b)))  # Output: [(1, "a"), (2, "b")]

# Basic Example 3 (Three Iterables):
a = [1]
b = ["a"]
c = [True]
print(list(zip(a, b, c)))  # Output: [(1, "a", True)]

# DSA Example (Pair Lists):
nums = [1, 2]
chars = ["a", "b"]
print(list(zip(nums, chars)))  # Output: [(1, "a"), (2, "b")]


# BUILT-IN FUNCTION: 
next()
# What it does: Gets next from iterator.
# Why use it: Step-by-step iteration control.
# How it works: Calls __next__; default for exhausted.
# When to use: Custom generator processing.
# Time/Space: O(1) per call, O(1) space.

# Syntax:
next(iterator, default)  # Next item or 'default'

# Basic Example 1 (From List Iterator):
it = iter([1, 2])
print(next(it))  # Output: 1

# Basic Example 2 (With Default):
it = iter([])
print(next(it, "end"))  # Output: "end"

# Basic Example 3 (Multiple Calls):
it = iter([1, 2])
print(next(it))  # Output: 1
print(next(it))  # Output: 2

# DSA Example (Iterator Traversal):
iter_nums = iter([1, 2, 3])
print(next(iter_nums))  # Output: 1


# BUILT-IN FUNCTION: 
set()
# What it does: Creates set from iterable, unique elements.
# Why use it: Fast deduplication and membership.
# How it works: Hashes elements; unordered.
# When to use: Removing duplicates in arrays.
# Time/Space: O(n) time, O(n) space.

# Syntax:
set(iterable)  # New set; 'iterable' optional

# Basic Example 1 (From List):
lst = [1, 2, 2]
print(set(lst))  # Output: {1, 2}

# Basic Example 2 (From String):
text = "aab"
print(set(text))  # Output: {"a", "b"}

# Basic Example 3 (Empty):
print(set())  # Output: set()

# DSA Example (Remove Duplicates):
nums = [1, 2, 2]
print(set(nums))  # Output: {1, 2}


# BUILT-IN FUNCTION: 
isinstance()
# What it does: Checks if object is instance of type.
# Why use it: Flexible type validation.
# How it works: Includes subclasses; tuple for multiple.
# When to use: Input checks in polymorphic code.
# Time/Space: O(1) time, O(1) space.

# Syntax:
isinstance(object, type)  # True if instance or subclass

# Basic Example 1 (Single Type):
value = "abc"
print(isinstance(value, str))  # Output: True

# Basic Example 2 (Multiple Types):
num = 42
print(isinstance(num, (int, float)))  # Output: True

# Basic Example 3 (Subclass):
class Child(int): pass
c = Child()
print(isinstance(c, int))  # Output: True

# DSA Example (Type Validation):
value = "123"
print(isinstance(value, str))  # Output: True


# BUILT-IN FUNCTION: 
type()
# What it does: Returns object's type.
# Why use it: Identifies data types.
# How it works: Returns class; compares with ==.
# When to use: Debugging or type-specific logic.
# Time/Space: O(1) time, O(1) space.

# Syntax:
type(object)  # Returns type class

# Basic Example 1 (String):
value = "abc"
print(type(value))  # Output: <class 'str'>

# Basic Example 2 (Compare Type):
num = 42
print(type(num) == int)  # Output: True

# Basic Example 3 (List):
lst = []
print(type(lst))  # Output: <class 'list'>

# DSA Example (Type Validation):
value = "123"
print(type(value) == str)  # Output: True


# BUILT-IN FUNCTION: 
sorted()
# What it does: Returns sorted list from iterable.
# Why use it: Sorts without modifying original.
# How it works: Stable sort; optional key/reverse.
# When to use: Preparing for binary search.
# Time/Space: O(n log n) time, O(n) space.

# Syntax:
sorted(iterable, reverse=False)  # New sorted list

# Basic Example 1 (Ascending):
nums = [3, 1, 2]
print(sorted(nums))  # Output: [1, 2, 3]

# Basic Example 2 (Descending):
nums = [3, 1, 2]
print(sorted(nums, reverse=True))  # Output: [3, 2, 1]

# Basic Example 3 (Strings):
chars = ["b", "a"]
print(sorted(chars))  # Output: ["a", "b"]

# DSA Example (Sort Array):
nums = [3, 1, 2]
print(sorted(nums))  # Output: [1, 2, 3]




# ADDITIONAL COMMON METHODS/FUNCTIONS FOR LEETCODE
# ----------------------------------------------------------------------------------
# LIST METHOD: 
.sort()
# What it does: Sorts list in place.
# Why use it: Prepares data efficiently.
# How it works: Modifies original; stable sort.
# When to use: In-place for two-pointer.
# Time/Space: O(n log n) time, O(1) space.

# Syntax:
list.sort()  # Sorts in place; reverse optional

# Basic Example 1 (Ascending):
nums = [3, 1, 2]
nums.sort()
print(nums)  # Output: [1, 2, 3]

# Basic Example 2 (Descending):
nums = [3, 1, 2]
nums.sort(reverse=True)
print(nums)  # Output: [3, 2, 1]

# Basic Example 3 (Strings):
chars = ["b", "a"]
chars.sort()
print(chars)  # Output: ["a", "b"]

# DSA Example (Sort for Binary Search):
numbers = [3, 1, 2]
numbers.sort()
print(numbers)  # Output: [1, 2, 3]


# BUILT-IN FUNCTION: 
max()
# What it does: Returns largest item.
# Why use it: Finds max quickly.
# How it works: Iterates once; optional key.
# When to use: Max in arrays or profits.
# Time/Space: O(n) time, O(1) space.

# Syntax:
max(iterable)  # Largest in iterable

# Basic Example 1 (List):
nums = [1, 5, 3]
print(max(nums))  # Output: 5

# Basic Example 2 (Arguments):
print(max(1, 2, 3))  # Output: 3

# Basic Example 3 (Strings):
chars = ["a", "c", "b"]
print(max(chars))  # Output: "c"

# DSA Example (Max in Array):
numbers = [1, 5, 3]
print(max(numbers))  # Output: 5


# BUILT-IN FUNCTION: 
sum()
# What it does: Sums iterable items.
# Why use it: Aggregates numbers easily.
# How it works: Adds elements; start optional.
# When to use: Subarray or cumulative sums.
# Time/Space: O(n) time, O(1) space.

# Syntax:
sum(iterable)  # Sum of elements

# Basic Example 1 (List):
nums = [1, 2, 3]
print(sum(nums))  # Output: 6

# Basic Example 2 (With Start):
nums = [1, 2]
print(sum(nums, 10))  # Output: 13

# Basic Example 3 (Empty):
print(sum([]))  # Output: 0

# DSA Example (Array Sum):
numbers = [1, 2, 3]
print(sum(numbers))  # Output: 6





# SPECIAL METHODS
# ----------------------------------------------------------------------------------
# SPECIAL METHOD: 
__init__()
# What it does: Initializes class instance.
# Why use it: Sets initial attributes.
# How it works: Called on object creation.
# When to use: Defining nodes or custom classes.
# Time/Space: O(1) typically, varies.

# Syntax:
def __init__(self, *args):  # Initializes attributes

# Basic Example 1 (Simple Class):
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
p = Point(1, 2)
print(p.x, p.y)  # Output: 1 2

# Basic Example 2 (Default Values):
class Person:
    def __init__(self, name="Unknown"):
        self.name = name
p = Person()
print(p.name)  # Output: "Unknown"

# Basic Example 3 (No Args):
class Empty:
    def __init__(self):
        pass
e = Empty()

# DSA Example (Node for Linked List):
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
node = Node(5)
print(node.value)  # Output: 5


# SPECIAL METHOD:
 __str__()
# What it does: Defines string representation.
# Why use it: Readable print/str of objects.
# How it works: Called by str() or print().
# When to use: Debugging custom structures.
# Time/Space: O(n) time, O(n) space for string.

# Syntax:
def __str__(self):  # Returns string description

# Basic Example 1 (Basic Class):
class Point:
    def __init__(self, x):
        self.x = x
    def __str__(self):
        return f"Point({self.x})"
p = Point(1)
print(p)  # Output: "Point(1)"

# Basic Example 2 (Multiple Attributes):
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} ({self.age})"
p = Person("Alice", 25)
print(p)  # Output: "Alice (25)"

# Basic Example 3 (Default Override):
class Empty:
    def __str__(self):
        return "Empty"
e = Empty()
print(e)  # Output: "Empty"

# DSA Example (Human Class):
class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def __str__(self):
        return f"{self.name}, {self.age}"
h = Human(23, "John")
print(h)  # Output: "John, 23"

















DELETE  DELETE DELETE DELETE
# ––––––––––––––––––––––––––
# STRING METHODS

# STRING METHOD: 
.upper()
# What it does: Converts all characters in a string to uppercase.
# Why use it: Normalizes text for case-insensitive operations.
# How it works: Creates a new string with uppercase letters.
# When to use: In string problems like palindromes or anagrams for consistency.
# Time/Space: O(n) time (n = length), O(n) space.

# Syntax:
string.upper()  # Returns uppercase string

# Basic Example 1 (Simple String):
text = "hello"
print(text.upper())  # Output: "HELLO"

# Basic Example 2 (Mixed Case):
text = "HeLLo"
print(text.upper())  # Output: "HELLO"

# Basic Example 3 (With Numbers):
text = "hello123"
print(text.upper())  # Output: "HELLO123"

# DSA Example (Palindrome Prep):
s = "Racecar"
normalized = s.upper()
print(normalized)  # Output: "RACECAR"

# STRING METHOD: 
.lower()
# What it does: Converts all characters in a string to lowercase.
# Why use it: Standardizes text for comparisons.
# How it works: Creates a new string with lowercase letters.
# When to use: In case-insensitive searches or matching.
# Time/Space: O(n) time (n = length), O(n) space.

# Syntax:
string.lower()  # Returns lowercase string

# Basic Example 1 (Simple String):
text = "WORLD"
print(text.lower())  # Output: "world"

# Basic Example 2 (Mixed Case):
text = "WoRLd"
print(text.lower())  # Output: "world"

# Basic Example 3 (With Numbers):
text = "WORLD123"
print(text.lower())  # Output: "world123"

# DSA Example (Anagram Prep):
s = "Listen"
normalized = s.lower()
print(normalized)  # Output: "listen"

# STRING METHOD: 
.replace()
# What it does: Replaces occurrences of a substring with another.
# Why use it: Modifies strings efficiently.
# How it works: Scans and replaces, returns new string.
# When to use: In text cleaning or transformations.
# Time/Space: O(n) time (n = length), O(n) space.

# Syntax:
string.replace(old, new)  # Replaces 'old' with 'new'

# Basic Example 1 (Simple Replace):
text = "hello"
print(text.replace("h", "j"))  # Output: "jello"

# Basic Example 2 (Multiple):
text = "aaab"
print(text.replace("a", "c"))  # Output: "cccb"

# Basic Example 3 (No Match):
text = "hello"
print(text.replace("x", "y"))  # Output: "hello"

# DSA Example (Clean String):
s = "a#b#c"
cleaned = s.replace("#", "")
print(cleaned)  # Output: "abc"

# STRING METHOD: 
.isdigit()
# What it does: Checks if all characters are digits.
# Why use it: Validates numeric strings quickly.
# How it works: Returns True if digits only, else False.
# When to use: In parsing or input validation.
# Time/Space: O(n) time (n = length), O(1) space.

# Syntax:
string.isdigit()  # Returns bool

# Basic Example 1 (All Digits):
text = "123"
print(text.isdigit())  # Output: True

# Basic Example 2 (With Letter):
text = "12a"
print(text.isdigit())  # Output: False

# Basic Example 3 (Empty String):
text = ""
print(text.isdigit())  # Output: False

# DSA Example (Validate Number):
s = "456"
if s.isdigit():
    num = int(s)
print(num)  # Output: 456

# STRING METHOD: 
.isnumeric()
# What it does: Checks if all characters are numeric.
# Why use it: Validates broader numeric inputs.
# How it works: Returns True for digits/Unicode numerics.
# When to use: In robust numeric parsing.
# Time/Space: O(n) time (n = length), O(1) space.

# Syntax:
string.isnumeric()  # Returns bool

# Basic Example 1 (Digits):
text = "123"
print(text.isnumeric())  # Output: True

# Basic Example 2 (With Letter):
text = "12a"
print(text.isnumeric())  # Output: False

# Basic Example 3 (Unicode Numeric):
text = "½"
print(text.isnumeric())  # Output: True

# DSA Example (Check Input):
s = "789"
if s.isnumeric():
    num = int(s)
print(num)  # Output: 789

# STRING METHOD: 
.split()
# What it does: Splits string into list by delimiter.
# Why use it: Parses strings into tokens.
# How it works: Defaults to whitespace; returns list.
# When to use: In word or data parsing problems.
# Time/Space: O(n) time (n = length), O(n) space.

# Syntax:
string.split(separator)  # 'separator' optional

# Basic Example 1 (Whitespace):
text = "a b c"
print(text.split())  # Output: ['a', 'b', 'c']

# Basic Example 2 (Custom Delim):
text = "a,b,c"
print(text.split(','))  # Output: ['a', 'b', 'c']

# Basic Example 3 (No Delim):
text = "abc"
print(text.split())  # Output: ['abc']

# DSA Example (Word Count):
s = "hello world"
words = s.split()
print(len(words))  # Output: 2

# STRING METHOD: 
.format()
# What it does: Formats string with placeholders.
# Why use it: Builds dynamic strings easily.
# How it works: Replaces {} with args.
# When to use: In output or debugging.
# Time/Space: O(n) time (n = length), O(n) space.

# Syntax:
string.format(*args)  # Placeholders like {}

# Basic Example 1 (Single):
s = "Value: {}"
print(s.format(5))  # Output: "Value: 5"

# Basic Example 2 (Multiple):
s = "{} + {} = {}"
print(s.format(1, 2, 3))  # Output: "1 + 2 = 3"

# Basic Example 3 (Named):
s = "{name}: {age}"
print(s.format(name="Bob", age=30))  # Output: "Bob: 30"

# DSA Example (Format Result):
key, val = 'a', 1
print("{}: {}".format(key, val))  # Output: "a: 1"

# STRING METHOD: 
.join()
# What it does: Joins iterable elements into string.
# Why use it: Builds strings from lists efficiently.
# How it works: Uses separator between elements.
# When to use: In reversing words or output.
# Time/Space: O(n) time (n = total length), O(n) space.

# Syntax:
separator.join(iterable)  # Joins with 'separator'

# Basic Example 1 (Space Join):
lst = ['a', 'b']
print(' '.join(lst))  # Output: "a b"

# Basic Example 2 (Comma Join):
lst = ['1', '2']
print(','.join(lst))  # Output: "1,2"

# Basic Example 3 (Empty Join):
lst = []
print(''.join(lst))  # Output: ""

# DSA Example (Rebuild String):
words = ['hello', 'world']
s = ' '.join(words)
print(s)  # Output: "hello world"





# ----------------------------------------------------------------------------------
# LIST METHODS

# LIST METHOD: 
.append()
# What it does: Adds element to list end.
# Why use it: Grows lists dynamically.
# How it works: Modifies in place; amortized O(1).
# When to use: Collecting results in loops.
# Time/Space: O(1) amortized time, O(1) space.

# Syntax:
list.append(item)  # Adds 'item'

# Basic Example 1 (Empty List):
lst = []
lst.append(1)
print(lst)  # Output: [1]

# Basic Example 2 (Add Number):
lst = [1, 2]
lst.append(3)
print(lst)  # Output: [1, 2, 3]

# Basic Example 3 (Add String):
lst = ['a', 'b']
lst.append('c')
print(lst)  # Output: ['a', 'b', 'c']

# DSA Example (Build in Loop):
result = []
for i in range(3):
    result.append(i)
print(result)  # Output: [0, 1, 2]

# LIST METHOD: 
.extend()
# What it does: Adds iterable elements to list end.
# Why use it: Merges collections efficiently.
# How it works: Iterates and appends; O(k) time.
# When to use: Merging arrays in DSA.
# Time/Space: O(k) time (k = added), O(k) space.

# Syntax:
list.extend(iterable)  # Adds from 'iterable'

# Basic Example 1 (Add List):
lst = [1, 2]
lst.extend([3, 4])
print(lst)  # Output: [1, 2, 3, 4]

# Basic Example 2 (Add String):
lst = ['a']
lst.extend('bc')
print(lst)  # Output: ['a', 'b', 'c']

# Basic Example 3 (Empty Extend):
lst = [1]
lst.extend([])
print(lst)  # Output: [1]

# DSA Example (Merge Arrays):
a = [1, 3]
a.extend([2, 4])
print(sorted(a))  # Output: [1, 2, 3, 4]

# LIST METHOD: 
.insert()
# What it does: Inserts element at index.
# Why use it: Places items at positions.
# How it works: Shifts elements; O(n) time.
# When to use: Maintaining sorted lists.
# Time/Space: O(n) time, O(1) space.

# Syntax:
list.insert(index, item)  # Inserts at 'index'

# Basic Example 1 (At Start):
lst = [2, 3]
lst.insert(0, 1)
print(lst)  # Output: [1, 2, 3]

# Basic Example 2 (In Middle):
lst = [1, 3]
lst.insert(1, 2)
print(lst)  # Output: [1, 2, 3]

# Basic Example 3 (At End):
lst = [1, 2]
lst.insert(2, 3)
print(lst)  # Output: [1, 2, 3]

# DSA Example (Sorted Insert):
lst = [1, 3, 4]
lst.insert(1, 2)
print(lst)  # Output: [1, 2, 3, 4]

# LIST METHOD: 
.remove()
# What it does: Removes first matching value.
# Why use it: Deletes by value.
# How it works: Searches and shifts; O(n) time.
# When to use: Removing duplicates/invalids.
# Time/Space: O(n) time, O(1) space.

# Syntax:
list.remove(value)  # Removes 'value'

# Basic Example 1 (Remove Number):
lst = [1, 2, 1]
lst.remove(1)
print(lst)  # Output: [2, 1]

# Basic Example 2 (Remove String):
lst = ['a', 'b', 'a']
lst.remove('a')
print(lst)  # Output: ['b', 'a']

# Basic Example 3 (No Match Error):
# lst = [1]
# lst.remove(2)  # ValueError

# DSA Example (Remove Duplicate):
dups = [1, 2, 2]
dups.remove(2)
print(dups)  # Output: [1, 2]

# LIST METHOD: 
.pop()
# What it does: Removes and returns item at index (default last).
# Why use it: Retrieves while removing.
# How it works: O(1) for last, O(n) otherwise.
# When to use: In stacks or queues.
# Time/Space: O(1)/O(n) time, O(1) space.

# Syntax:
list.pop(index)  # 'index' optional (-1 default)

# Basic Example 1 (Last Item):
lst = [1, 2, 3]
print(lst.pop())  # Output: 3

# Basic Example 2 (At Index):
lst = [1, 2, 3]
print(lst.pop(1))  # Output: 2

# Basic Example 3 (Empty Error):
# lst = []
# lst.pop()  # IndexError

# DSA Example (Stack Pop):
stack = [1, 2, 3]
popped = stack.pop()
print(popped, stack)  # Output: 3 [1, 2]





# ----------------------------------------------------------------------------------
# DICTIONARY METHODS

# DICTIONARY METHOD: 
.keys()
# What it does: Returns view of keys.
# Why use it: Accesses keys for iteration.
# How it works: Dynamic view; O(1) creation.
# When to use: In frequency or grouping.
# Time/Space: O(1) view, O(n) list.

# Syntax:
dict.keys()  # Returns keys view

# Basic Example 1 (Get Keys):
d = {'a':1, 'b':2}
print(list(d.keys()))  # Output: ['a', 'b']

# Basic Example 2 (Empty Dict):
d = {}
print(list(d.keys()))  # Output: []

# Basic Example 3 (Check Key):
d = {'key': 'val'}
print('key' in d.keys())  # Output: True

# DSA Example (Iterate Keys):
counts = {'a':1, 'b':2}
for k in counts.keys():
    print(k)  # Output: a b

# DICTIONARY METHOD: 
.get()
# What it does: Gets value for key, default if missing.
# Why use it: Safe access without errors.
# How it works: O(1) lookup.
# When to use: In frequency maps.
# Time/Space: O(1) time/space.

# Syntax:
dict.get(key, default)  # 'default' optional

# Basic Example 1 (Existing Key):
d = {'a':1}
print(d.get('a'))  # Output: 1

# Basic Example 2 (Missing Key):
d = {'a':1}
print(d.get('b', 0))  # Output: 0

# Basic Example 3 (No Default):
d = {}
print(d.get('key'))  # Output: None

# DSA Example (Frequency):
counts = {}
counts['a'] = counts.get('a', 0) + 1
print(counts)  # Output: {'a': 1}

# DICTIONARY METHOD: 
.items()
# What it does: Returns view of key-value pairs.
# Why use it: Iterates keys and values together.
# How it works: Dynamic view; O(1) creation.
# When to use: In processing pairs.
# Time/Space: O(1) view, O(n) list.

# Syntax:
dict.items()  # Returns (key, value) view

# Basic Example 1 (Get Items):
d = {'a':1, 'b':2}
print(list(d.items()))  # Output: [('a', 1), ('b', 2)]

# Basic Example 2 (Empty):
d = {}
print(list(d.items()))  # Output: []

# Basic Example 3 (Loop Pairs):
d = {'a':1}
for k, v in d.items():
    print(k, v)  # Output: a 1

# DSA Example (Sum Values):
counts = {'a':1, 'b':2}
total = sum(v for k, v in counts.items())
print(total)  # Output: 3




# ----------------------------------------------------------------------------------
# SET METHODS

# SET METHOD: 
.add()
# What it does: Adds element if not present.
# Why use it: Builds unique collections.
# How it works: O(1) average insert.
# When to use: Deduplication or membership.
# Time/Space: O(1) time/space average.

# Syntax:
set.add(element)  # Adds 'element'

# Basic Example 1 (Add New):
s = {1, 2}
s.add(3)
print(s)  # Output: {1, 2, 3}

# Basic Example 2 (Duplicate):
s = {1}
s.add(1)
print(s)  # Output: {1}

# Basic Example 3 (Add String):
s = {'a'}
s.add('b')
print(s)  # Output: {'a', 'b'}

# DSA Example (Unique Tracking):
seen = set()
seen.add(5)
print(5 in seen)  # Output: True




# ----------------------------------------------------------------------------------
# BUILT-IN FUNCTIONS

# BUILT-IN FUNCTION: 
len()
# What it does: Returns length of object.
# Why use it: Checks size for control.
# How it works: O(1) for most types.
# When to use: Loops, validations.
# Time/Space: O(1) time/space.

# Syntax:
len(object)  # Returns int length

# Basic Example 1 (List):
lst = [1, 2, 3]
print(len(lst))  # Output: 3

# Basic Example 2 (String):
s = "abc"
print(len(s))  # Output: 3

# Basic Example 3 (Dict):
d = {'a':1}
print(len(d))  # Output: 1

# DSA Example (Array Check):
arr = [1, 2]
if len(arr) > 1:
    print("Multi")  # Output: Multi

# BUILT-IN FUNCTION: 
int()
# What it does: Converts to integer.
# Why use it: Parses numbers for math.
# How it works: Handles strings/floats.
# When to use: Input parsing.
# Time/Space: O(n) time, O(1) space.

# Syntax:
int(value)  # Converts 'value'

# Basic Example 1 (String):
s = "123"
print(int(s))  # Output: 123

# Basic Example 2 (Float):
f = 5.9
print(int(f))  # Output: 5

# Basic Example 3 (Base 2):
s = "101"
print(int(s, 2))  # Output: 5

# DSA Example (Atoi Sim):
s = "42"
num = int(s)
print(num + 1)  # Output: 43

# BUILT-IN FUNCTION: 
float()
# What it does: Converts to float.
# Why use it: Handles decimals.
# How it works: Parses strings/ints.
# When to use: Precision calculations.
# Time/Space: O(n) time, O(1) space.

# Syntax:
float(value)  # Converts 'value'

# Basic Example 1 (String):
s = "1.23"
print(float(s))  # Output: 1.23

# Basic Example 2 (Int):
i = 5
print(float(i))  # Output: 5.0

# Basic Example 3 (Scientific):
s = "1e3"
print(float(s))  # Output: 1000.0

# DSA Example (Decimal Add):
s = "3.14"
pi = float(s)
print(pi + 0.01)  # Output: 3.15

# BUILT-IN FUNCTION: 
input()
# What it does: Reads user input as string.
# Why use it: Gets interactive data.
# How it works: Prompts and reads line.
# When to use: Testing or inputs.
# Time/Space: O(n) time, O(n) space.

# Syntax:
input(prompt)  # 'prompt' optional

# Basic Example 1 (No Prompt):
# name = input()
# print(name)  # User input

# Basic Example 2 (With Prompt):
# age = input("Age: ")
# print(age)  # User input

# Basic Example 3 (To Int):
# num = int(input())
# print(num + 1)  # User input +1

# DSA Example (Read List):
# nums = list(map(int, input().split()))
# print(nums)  # e.g., input "1 2" -> [1, 2]

# BUILT-IN FUNCTION: 
list()
# What it does: Creates list from iterable.
# Why use it: Converts to mutable list.
# How it works: Copies elements.
# When to use: String/set to list.
# Time/Space: O(n) time/space.

# Syntax:
list(iterable)  # From 'iterable'

# Basic Example 1 (From String):
s = "abc"
print(list(s))  # Output: ['a', 'b', 'c']

# Basic Example 2 (From Tuple):
t = (1, 2)
print(list(t))  # Output: [1, 2]

# Basic Example 3 (Empty):
print(list())  # Output: []

# DSA Example (Set to List):
unique = {3, 1, 2}
sorted_list = sorted(list(unique))
print(sorted_list)  # Output: [1, 2, 3]

# BUILT-IN FUNCTION: 
tuple()
# What it does: Creates tuple from iterable.
# Why use it: Immutable sequences.
# How it works: Copies to tuple.
# When to use: Dict keys or returns.
# Time/Space: O(n) time/space.

# Syntax:
tuple(iterable)  # From 'iterable'

# Basic Example 1 (From List):
lst = [1, 2]
print(tuple(lst))  # Output: (1, 2)

# Basic Example 2 (From String):
s = "ab"
print(tuple(s))  # Output: ('a', 'b')

# Basic Example 3 (Empty):
print(tuple())  # Output: ()

# DSA Example (Pair for Key):
pair = tuple([1, 2])
d = {pair: 'val'}
print(d)  # Output: {(1, 2): 'val'}

# BUILT-IN FUNCTION: 
dict()
# What it does: Creates dict from pairs/kwargs.
# Why use it: Builds key-value maps.
# How it works: Adds items; O(n) time.
# When to use: Frequency or caching.
# Time/Space: O(n) time/space.

# Syntax:
dict(iterable)  # From pairs or kwargs

# Basic Example 1 (From Pairs):
pairs = [('a',1)]
print(dict(pairs))  # Output: {'a':1}

# Basic Example 2 (Kwargs):
print(dict(a=1, b=2))  # Output: {'a':1, 'b':2}

# Basic Example 3 (Empty):
print(dict())  # Output: {}

# DSA Example (Frequency Map):
chars = 'aab'
counts = dict()
for c in chars:
    counts[c] = counts.get(c, 0) + 1
print(counts)  # Output: {'a':2, 'b':1}

# BUILT-IN FUNCTION: 
enumerate()
# What it does: Pairs index with elements.
# Why use it: Tracks position in loops.
# How it works: Yields (index, value).
# When to use: Array index operations.
# Time/Space: O(1) create, O(1) per.

# Syntax:
enumerate(iterable, start=0)  # 'start' optional

# Basic Example 1 (Default Start):
lst = ['a', 'b']
for i, v in enumerate(lst):
    print(i, v)  # Output: 0 a 1 b

# Basic Example 2 (Custom Start):
lst = ['x', 'y']
for i, v in enumerate(lst, 1):
    print(i, v)  # Output: 1 x 2 y

# Basic Example 3 (List Conversion):
lst = [10, 20]
print(list(enumerate(lst)))  # Output: [(0,10), (1,20)]

# DSA Example (Index Mapping):
arr = [5, 3, 8]
for i, val in enumerate(arr):
    if val > 4:
        print(i)  # Output: 0 2

# BUILT-IN FUNCTION: 
iter()
# What it does: Creates iterator from iterable.
# Why use it: Manual iteration control.
# How it works: Returns iterator object.
# When to use: Custom traversal.
# Time/Space: O(1) time/space.

# Syntax:
iter(iterable)  # Returns iterator

# Basic Example 1 (From List):
lst = [1, 2]
it = iter(lst)
print(next(it))  # Output: 1

# Basic Example 2 (From String):
s = "ab"
it = iter(s)
print(next(it))  # Output: 'a'

# Basic Example 3 (Exhaust):
it = iter([3])
print(next(it))  # Output: 3
# next(it)  # StopIteration

# DSA Example (Manual Loop):
arr = [4, 5]
it = iter(arr)
while True:
    try:
        print(next(it))  # Output: 4 5
    except StopIteration:
        break

# BUILT-IN FUNCTION: 
range()
# What it does: Generates number sequence.
# Why use it: Efficient looping ranges.
# How it works: Lazy; doesn't store list.
# When to use: For loops in arrays.
# Time/Space: O(1) time/space.

# Syntax:
range(stop)  # 0 to stop-1
range(start, stop)  # start to stop-1
range(start, stop, step)  # with step

# Basic Example 1 (Default):
print(list(range(3)))  # Output: [0, 1, 2]

# Basic Example 2 (Start Stop):
print(list(range(1, 4)))  # Output: [1, 2, 3]

# Basic Example 3 (With Step):
print(list(range(0, 6, 2)))  # Output: [0, 2, 4]

# DSA Example (Loop Indices):
for i in range(3):
    print(i)  # Output: 0 1 2

# BUILT-IN FUNCTION: 
zip()
# What it does: Pairs elements from iterables.
# Why use it: Simultaneous iteration.
# How it works: Stops at shortest.
# When to use: Merging lists or matrices.
# Time/Space: O(1) create, O(1) per.

# Syntax:
zip(*iterables)  # Pairs iterables

# Basic Example 1 (Two Lists):
a = [1, 2]
b = ['a', 'b']
print(list(zip(a, b)))  # Output: [(1,'a'), (2,'b')]

# Basic Example 2 (Unequal Length):
a = [1]
b = ['x', 'y']
print(list(zip(a, b)))  # Output: [(1,'x')]

# Basic Example 3 (Three):
print(list(zip([1], [2], [3])))  # Output: [(1,2,3)]

# DSA Example (Transpose):
matrix = [[1,2], [3,4]]
trans = list(zip(*matrix))
print(trans)  # Output: [(1,3), (2,4)]

# BUILT-IN FUNCTION: 
next()
# What it does: Gets next from iterator.
# Why use it: Step-by-step iteration.
# How it works: Advances iterator.
# When to use: Custom loops.
# Time/Space: O(1) time/space.

# Syntax:
next(iterator, default)  # 'default' optional

# Basic Example 1 (Basic):
it = iter([1, 2])
print(next(it))  # Output: 1

# Basic Example 2 (Default):
it = iter([])
print(next(it, 'end'))  # Output: 'end'

# Basic Example 3 (Error on Exhaust):
it = iter([3])
next(it)  # 3
# next(it)  # StopIteration

# DSA Example (Consume Iterator):
it = iter('ab')
print(next(it) + next(it))  # Output: 'ab'

# BUILT-IN FUNCTION: 
set()
# What it does: Creates set from iterable.
# Why use it: Unique elements storage.
# How it works: Removes duplicates.
# When to use: Dedup or membership.
# Time/Space: O(n) time/space.

# Syntax:
set(iterable)  # From 'iterable'

# Basic Example 1 (From List):
lst = [1, 2, 1]
print(set(lst))  # Output: {1, 2}

# Basic Example 2 (From String):
s = "aab"
print(set(s))  # Output: {'a', 'b'}

# Basic Example 3 (Empty):
print(set())  # Output: set()

# DSA Example (Unique Check):
nums = [1, 2, 3]
unique = set(nums)
print(len(unique) == len(nums))  # Output: True

# BUILT-IN FUNCTION: 
isinstance()
# What it does: Checks object type.
# Why use it: Validates types.
# How it works: True if matches or subclass.
# When to use: Input handling.
# Time/Space: O(1) time/space.

# Syntax:
isinstance(object, type)  # Or tuple of types

# Basic Example 1 (Single Type):
num = 5
print(isinstance(num, int))  # Output: True

# Basic Example 2 (Tuple Types):
val = 3.14
print(isinstance(val, (int, float)))  # Output: True

# Basic Example 3 (False Check):
s = "text"
print(isinstance(s, list))  # Output: False

# DSA Example (Validate Input):
data = [1, 2]
if isinstance(data, list):
    print(len(data))  # Output: 2

# BUILT-IN FUNCTION: 
type()
# What it does: Returns object type.
# Why use it: Identifies data types.
# How it works: Returns class.
# When to use: Debugging or checks.
# Time/Space: O(1) time/space.

# Syntax:
type(object)  # Returns type

# Basic Example 1 (Int):
num = 42
print(type(num))  # Output: <class 'int'>

# Basic Example 2 (String):
s = "hi"
print(type(s))  # Output: <class 'str'>

# Basic Example 3 (List):
lst = []
print(type(lst))  # Output: <class 'list'>

# DSA Example (Type Check):
val = "123"
if type(val) == str:
    num = int(val)
print(num)  # Output: 123

# BUILT-IN FUNCTION: 
sorted()
# What it does: Returns sorted list from iterable.
# Why use it: Sorts without modifying original.
# How it works: Stable sort; O(n log n).
# When to use: Prep for binary search.
# Time/Space: O(n log n) time, O(n) space.

# Syntax:
sorted(iterable, reverse=False)  # 'reverse' optional

# Basic Example 1 (Ascending):
lst = [3, 1, 2]
print(sorted(lst))  # Output: [1, 2, 3]

# Basic Example 2 (Descending):
lst = [3, 1, 2]
print(sorted(lst, True))  # Output: [3, 2, 1]

# Basic Example 3 (Strings):
s = "bac"
print(sorted(s))  # Output: ['a', 'b', 'c']

# DSA Example (Sort for Search):
nums = [4, 2, 5]
sorted_nums = sorted(nums)
print(sorted_nums)  # Output: [2, 4, 5]

# ADDITIONAL COMMON METHODS/FUNCTIONS FOR LEETCODE

# LIST METHOD: 
.sort()
# What it does: Sorts list in place.
# Why use it: Modifies original efficiently.
# How it works: Stable; O(n log n).
# When to use: In-place for space saving.
# Time/Space: O(n log n) time, O(1) space.

# Syntax:
list.sort(reverse=False)  # 'reverse' optional

# Basic Example 1 (Ascending):
lst = [3, 1, 2]
lst.sort()
print(lst)  # Output: [1, 2, 3]

# Basic Example 2 (Descending):
lst = [3, 1, 2]
lst.sort(reverse=True)
print(lst)  # Output: [3, 2, 1]

# Basic Example 3 (Strings):
lst = ['b', 'a', 'c']
lst.sort()
print(lst)  # Output: ['a', 'b', 'c']

# DSA Example (Prep Two-Pointer):
nums = [5, 3, 4]
nums.sort()
print(nums)  # Output: [3, 4, 5]

# BUILT-IN FUNCTION: 
max()
# What it does: Returns max in iterable.
# Why use it: Finds largest quickly.
# How it works: Scans elements; O(n).
# When to use: Max profit/subarray.
# Time/Space: O(n) time, O(1) space.

# Syntax:
max(iterable)  # Or max(arg1, arg2, ...)

# Basic Example 1 (List):
lst = [1, 3, 2]
print(max(lst))  # Output: 3

# Basic Example 2 (Args):
print(max(4, 5, 6))  # Output: 6

# Basic Example 3 (Strings):
lst = ['a', 'c', 'b']
print(max(lst))  # Output: 'c'

# DSA Example (Max in Array):
arr = [10, 20, 15]
highest = max(arr)
print(highest)  # Output: 20

# BUILT-IN FUNCTION: 
sum()
# What it does: Sums iterable items.
# Why use it: Computes totals fast.
# How it works: Adds elements; O(n).
# When to use: Subarray or cumulative sums.
# Time/Space: O(n) time, O(1) space.

# Syntax:
sum(iterable)  # Sums numbers

# Basic Example 1 (List):
lst = [1, 2, 3]
print(sum(lst))  # Output: 6

# Basic Example 2 (Tuple):
t = (4, 5)
print(sum(t))  # Output: 9

# Basic Example 3 (Empty):
print(sum([]))  # Output: 0

# DSA Example (Subarray Sum):
sub = [1, 2, 3]
total = sum(sub)
print(total)  # Output: 6










# STRING METHODS

# STRING METHOD: 
.upper()
# What it does: Converts all characters in a string to uppercase.
# Why use it: Normalizes text for case-insensitive ops.
# How it works: Creates new string; no change to original.
# When to use: In palindrome/anagram checks for uniformity.
# Time/Space: O(n) time (n = length), O(n) space.

# Syntax:
string.upper()  # Returns uppercase string

# Basic Example 1 (Basic String):
text = "hi"
print(text.upper())  # Output: "HI"

# Basic Example 2 (Mixed Case):
text = "Hello"
print(text.upper())  # Output: "HELLO"

# Basic Example 3 (Empty String):
text = ""
print(text.upper())  # Output: ""

# DSA Example (Palindrome Prep):
word = "Racecar"
print(word.upper())  # Output: "RACECAR"

# STRING METHOD: 
.lower()
# What it does: Converts all characters in a string to lowercase.
# Why use it: Standardizes text for matching.
# How it works: Creates new string; original unchanged.
# When to use: In searches or anagram validation.
# Time/Space: O(n) time (n = length), O(n) space.

# Syntax:
string.lower()  # Returns lowercase string

# Basic Example 1 (Basic String):
text = "HI"
print(text.lower())  # Output: "hi"

# Basic Example 2 (Mixed Case):
text = "World"
print(text.lower())  # Output: "world"

# Basic Example 3 (Empty String):
text = ""
print(text.lower())  # Output: ""

# DSA Example (Anagram Prep):
word = "Listen"
print(word.lower())  # Output: "listen"

# STRING METHOD: 
.replace()
# What it does: Replaces substring occurrences with another.
# Why use it: Modifies text efficiently.
# How it works: Scans and replaces; returns new string.
# When to use: In string cleaning or transformations.
# Time/Space: O(n) time (n = length), O(n) space.

# Syntax:
string.replace(old, new)  # Replaces 'old' with 'new'

# Basic Example 1 (Simple Replace):
text = "cat"
print(text.replace("c", "b"))  # Output: "bat"

# Basic Example 2 (Multiple):
text = "a a a"
print(text.replace("a", "b"))  # Output: "b b b"

# Basic Example 3 (No Match):
text = "hello"
print(text.replace("x", "y"))  # Output: "hello"

# DSA Example (Clean String):
text = "a#b#c"
print(text.replace("#", ""))  # Output: "abc"

# STRING METHOD: 
.isdigit()
# What it does: Checks if all characters are digits.
# Why use it: Validates numeric strings quickly.
# How it works: Scans characters; returns bool.
# When to use: In input parsing like atoi.
# Time/Space: O(n) time (n = length), O(1) space.

# Syntax:
string.isdigit()  # True if all digits

# Basic Example 1 (Digits Only):
text = "123"
print(text.isdigit())  # Output: True

# Basic Example 2 (With Non-Digit):
text = "12a"
print(text.isdigit())  # Output: False

# Basic Example 3 (Empty String):
text = ""
print(text.isdigit())  # Output: False

# DSA Example (Validate Number):
text = "456"
print(text.isdigit())  # Output: True

# STRING METHOD: 
.isnumeric()
# What it does: Checks if all characters are numeric.
# Why use it: Broader numeric validation than isdigit.
# How it works: Includes Unicode numerics; returns bool.
# When to use: In robust parsing for numbers.
# Time/Space: O(n) time (n = length), O(1) space.

# Syntax:
string.isnumeric()  # True if all numeric

# Basic Example 1 (Digits):
text = "123"
print(text.isnumeric())  # Output: True

# Basic Example 2 (Non-Numeric):
text = "12a"
print(text.isnumeric())  # Output: False

# Basic Example 3 (Unicode Numeric):
text = "½"
print(text.isnumeric())  # Output: True

# DSA Example (Input Check):
text = "789"
print(text.isnumeric())  # Output: True

# STRING METHOD: 
.split()
# What it does: Splits string into list by delimiter.
# Why use it: Parses text into tokens.
# How it works: Defaults to whitespace; returns list.
# When to use: In word counting or tokenization.
# Time/Space: O(n) time (n = length), O(n) space.

# Syntax:
string.split(separator)  # Splits by 'separator' (optional)

# Basic Example 1 (Whitespace):
text = "a b c"
print(text.split())  # Output: ['a', 'b', 'c']

# Basic Example 2 (Custom Delim):
text = "a,b,c"
print(text.split(','))  # Output: ['a', 'b', 'c']

# Basic Example 3 (No Delim):
text = "abc"
print(text.split())  # Output: ['abc']

# DSA Example (Word Parse):
text = "hello world"
print(text.split())  # Output: ['hello', 'world']

# STRING METHOD: 
.format()
# What it does: Formats string with placeholders.
# Why use it: Builds dynamic strings easily.
# How it works: Replaces {} with args; returns string.
# When to use: In output formatting or debugging.
# Time/Space: O(n) time (n = length), O(n) space.

# Syntax:
string.format(*args, **kwargs)  # Formats with args

# Basic Example 1 (Single {}):
s = "{}"
print(s.format(1))  # Output: "1"

# Basic Example 2 (Multiple):
s = "{} {}"
print(s.format(1, 2))  # Output: "1 2"

# Basic Example 3 (Named):
s = "{name}"
print(s.format(name="A"))  # Output: "A"

# DSA Example (Result Format):
template = "Sum: {}"
print(template.format(5))  # Output: "Sum: 5"

# STRING METHOD: 
.join()
# What it does: Joins iterable elements into string.
# Why use it: Builds strings from lists efficiently.
# How it works: Uses separator; returns string.
# When to use: In reversing words or concatenation.
# Time/Space: O(n) time (n = total length), O(n) space.

# Syntax:
separator.join(iterable)  # Joins with 'separator'

# Basic Example 1 (Space Join):
lst = ['a', 'b']
print(' '.join(lst))  # Output: "a b"

# Basic Example 2 (Comma Join):
lst = ['1', '2']
print(','.join(lst))  # Output: "1,2"

# Basic Example 3 (Empty Separator):
lst = ['x', 'y']
print(''.join(lst))  # Output: "xy"

# DSA Example (List to String):
words = ['hello', 'world']
print(' '.join(words))  # Output: "hello world"

# LIST METHODS

# LIST METHOD: 
.append()
# What it does: Adds element to list end.
# Why use it: Grows lists dynamically.
# How it works: Modifies in place; amortized O(1).
# When to use: Collecting results in loops.
# Time/Space: O(1) amortized time, O(1) space.

# Syntax:
list.append(item)  # Adds 'item' to end

# Basic Example 1 (Empty List):
lst = []
lst.append(1)
print(lst)  # Output: [1]

# Basic Example 2 (Add Number):
lst = [1, 2]
lst.append(3)
print(lst)  # Output: [1, 2, 3]

# Basic Example 3 (Add String):
lst = ['a', 'b']
lst.append('c')
print(lst)  # Output: ['a', 'b', 'c']

# DSA Example (Build in Loop):
result = []
for i in range(3):
    result.append(i)
print(result)  # Output: [0, 1, 2]

# LIST METHOD: 
.extend()
# What it does: Adds iterable elements to list end.
# Why use it: Merges multiple items efficiently.
# How it works: Modifies in place; O(k) for k items.
# When to use: Merging arrays or collecting batches.
# Time/Space: O(k) time, O(k) space.

# Syntax:
list.extend(iterable)  # Adds from 'iterable'

# Basic Example 1 (Add List):
lst = [1]
lst.extend([2, 3])
print(lst)  # Output: [1, 2, 3]

# Basic Example 2 (Add Tuple):
lst = [1]
lst.extend((2, 3))
print(lst)  # Output: [1, 2, 3]

# Basic Example 3 (Add String):
lst = ['a']
lst.extend("bc")
print(lst)  # Output: ['a', 'b', 'c']

# DSA Example (Merge Arrays):
result = [1, 2]
result.extend([3, 4])
print(result)  # Output: [1, 2, 3, 4]

# LIST METHOD: 
.insert()
# What it does: Inserts element at index.
# Why use it: Adds at specific position.
# How it works: Shifts elements; modifies in place.
# When to use: Maintaining sorted order.
# Time/Space: O(n) time (shift), O(1) space.

# Syntax:
list.insert(index, item)  # Inserts at 'index'

# Basic Example 1 (Insert Start):
lst = [2, 3]
lst.insert(0, 1)
print(lst)  # Output: [1, 2, 3]

# Basic Example 2 (Insert Middle):
lst = [1, 3]
lst.insert(1, 2)
print(lst)  # Output: [1, 2, 3]

# Basic Example 3 (Insert End):
lst = [1, 2]
lst.insert(2, 3)
print(lst)  # Output: [1, 2, 3]

# DSA Example (Sorted Insert):
numbers = [1, 3]
numbers.insert(1, 2)
print(numbers)  # Output: [1, 2, 3]

# LIST METHOD: 
.remove()
# What it does: Removes first value occurrence.
# Why use it: Deletes by value, not index.
# How it works: Searches and shifts; raises if not found.
# When to use: Removing duplicates/invalids.
# Time/Space: O(n) time (search), O(1) space.

# Syntax:
list.remove(value)  # Removes first 'value'

# Basic Example 1 (Remove Existing):
lst = [1, 2, 1]
lst.remove(1)
print(lst)  # Output: [2, 1]

# Basic Example 2 (Remove String):
lst = ['a', 'b', 'a']
lst.remove('a')
print(lst)  # Output: ['b', 'a']

# Basic Example 3 (No Multiple Remove):
lst = [1, 1]
lst.remove(1)
print(lst)  # Output: [1]

# DSA Example (Remove Duplicate):
numbers = [1, 2, 2]
numbers.remove(2)
print(numbers)  # Output: [1, 2]

# LIST METHOD: 
.pop()
# What it does: Removes/returns element at index (default last).
# Why use it: Retrieves while removing.
# How it works: Modifies in place; O(1) for end.
# When to use: Stack ops or queue dequeue.
# Time/Space: O(1) end/O(n) other, O(1) space.

# Syntax:
list.pop(index)  # Removes at 'index' (optional -1)

# Basic Example 1 (Pop Last):
lst = [1, 2, 3]
print(lst.pop())  # Output: 3, lst: [1, 2]

# Basic Example 2 (Pop Index):
lst = [1, 2, 3]
print(lst.pop(1))  # Output: 2, lst: [1, 3]

# Basic Example 3 (Empty List Error):
# lst = []
# lst.pop()  # IndexError

# DSA Example (Stack Pop):
stack = [1, 2, 3]
last = stack.pop()
print(last)  # Output: 3

# DICTIONARY METHODS

# DICTIONARY METHOD: 
.keys()
# What it does: Returns view of dictionary keys.
# Why use it: Iterates or checks keys.
# How it works: Dynamic view; no copy unless listed.
# When to use: Frequency maps or grouping.
# Time/Space: O(1) view/O(n) list, O(n) space list.

# Syntax:
dict.keys()  # Returns keys view

# Basic Example 1 (Get Keys):
d = {'a':1, 'b':2}
print(list(d.keys()))  # Output: ['a', 'b']

# Basic Example 2 (Check In Keys):
d = {'x':3}
print('x' in d.keys())  # Output: True

# Basic Example 3 (Empty Dict):
d = {}
print(list(d.keys()))  # Output: []

# DSA Example (Key Iteration):
ages = {"Alice":25, "Bob":30}
print(list(ages.keys()))  # Output: ['Alice', 'Bob']

# DICTIONARY METHOD: 
.get()
# What it does: Gets value for key, default if missing.
# Why use it: Safe access without KeyError.
# How it works: O(1) lookup; returns default.
# When to use: Frequency counts or optional keys.
# Time/Space: O(1) time, O(1) space.

# Syntax:
dict.get(key, default)  # Value or 'default'

# Basic Example 1 (Existing Key):
d = {'a':1}
print(d.get('a', 0))  # Output: 1

# Basic Example 2 (Missing Key):
d = {'a':1}
print(d.get('b', 0))  # Output: 0

# Basic Example 3 (No Default):
d = {'a':1}
print(d.get('b'))  # Output: None

# DSA Example (Frequency):
counts = {"a":1}
counts["b"] = counts.get("b", 0) + 1
print(counts)  # Output: {'a':1, 'b':1}

# DICTIONARY METHOD: 
.items()
# What it does: Returns view of key-value pairs as tuples.
# Why use it: Iterates keys and values together.
# How it works: Dynamic view; convertible to list.
# When to use: Processing pairs in maps.
# Time/Space: O(1) view/O(n) list, O(n) space list.

# Syntax:
dict.items()  # Returns pairs view

# Basic Example 1 (Get Items):
d = {'a':1, 'b':2}
print(list(d.items()))  # Output: [('a',1), ('b',2)]

# Basic Example 2 (Loop Pairs):
d = {'x':3, 'y':4}
for k, v in d.items():
    print(k, v)  # Output: x 3, y 4

# Basic Example 3 (Empty Dict):
d = {}
print(list(d.items()))  # Output: []

# DSA Example (Process Pairs):
counts = {"a":2, "b":1}
for k, v in counts.items():
    print(k, v)  # Output: a 2, b 1

# SET METHODS

# SET METHOD: 
.add()
# What it does: Adds element if not present.
# Why use it: Maintains unique items.
# How it works: O(1) average; no duplicates.
# When to use: Deduplication or membership.
# Time/Space: O(1) average time, O(1) space.

# Syntax:
set.add(element)  # Adds 'element'

# Basic Example 1 (Add New):
s = {1, 2}
s.add(3)
print(s)  # Output: {1,2,3}

# Basic Example 2 (Add Existing):
s = {1}
s.add(1)
print(s)  # Output: {1}

# Basic Example 3 (Add String):
s = {'a'}
s.add('b')
print(s)  # Output: {'a','b'}

# DSA Example (Track Unique):
unique = {1, 2}
unique.add(3)
print(unique)  # Output: {1,2,3}

# BUILT-IN FUNCTIONS

# BUILT-IN FUNCTION: 
len()
# What it does: Returns object length.
# Why use it: Checks size for loops/conditions.
# How it works: O(1) for most types.
# When to use: Bounds in arrays/strings.
# Time/Space: O(1) time, O(1) space.

# Syntax:
len(object)  # Returns integer length

# Basic Example 1 (List Length):
lst = [1, 2, 3]
print(len(lst))  # Output: 3

# Basic Example 2 (String Length):
text = "abc"
print(len(text))  # Output: 3

# Basic Example 3 (Empty):
d = {}
print(len(d))  # Output: 0

# DSA Example (Array Check):
array = [1, 2, 3]
print(len(array))  # Output: 3

# BUILT-IN FUNCTION: 
int()
# What it does: Converts to integer.
# Why use it: Parses for math ops.
# How it works: Truncates floats; parses strings.
# When to use: Input conversion like atoi.
# Time/Space: O(n) time (strings), O(1) space.

# Syntax:
int(value)  # Converts 'value' to int

# Basic Example 1 (String):
s = "123"
print(int(s))  # Output: 123

# Basic Example 2 (Float):
f = 5.9
print(int(f))  # Output: 5

# Basic Example 3 (Bool):
b = True
print(int(b))  # Output: 1

# DSA Example (Parse Number):
num = "123"
print(int(num) + 1)  # Output: 124

# BUILT-IN FUNCTION: 
float()
# What it does: Converts to float.
# Why use it: Handles decimals in calcs.
# How it works: Parses strings; adds .0 to ints.
# When to use: Precision in numeric problems.
# Time/Space: O(n) time (strings), O(1) space.

# Syntax:
float(value)  # Converts 'value' to float

# Basic Example 1 (String):
s = "1.23"
print(float(s))  # Output: 1.23

# Basic Example 2 (Int):
i = 5
print(float(i))  # Output: 5.0

# Basic Example 3 (Bool):
b = True
print(float(b))  # Output: 1.0

# DSA Example (Decimal Parse):
num = "123.45"
print(float(num) + 0.55)  # Output: 124.0

# BUILT-IN FUNCTION: 
input()
# What it does: Reads user input as string.
# Why use it: Gets interactive data.
# How it works: Prompts and reads line.
# When to use: Testing or input problems.
# Time/Space: O(n) time (n = length), O(n) space.

# Syntax:
input(prompt)  # Reads with 'prompt' (optional)

# Basic Example 1 (No Prompt):
# input()  # Waits for input

# Basic Example 2 (With Prompt):
# input("Name: ")  # Prompts "Name: "

# Basic Example 3 (Store Input):
# name = input("Hi: ")
# print(name)  # Outputs input

# DSA Example (Read Number):
# num = input("Num: ")
# print(int(num) + 1)  # Adds to input

# BUILT-IN FUNCTION: 
list()
# What it does: Creates list from iterable.
# Why use it: Converts for list ops.
# How it works: Copies elements to new list.
# When to use: Transform strings/sets to arrays.
# Time/Space: O(n) time, O(n) space.

# Syntax:
list(iterable)  # New list from 'iterable'

# Basic Example 1 (From String):
text = "abc"
print(list(text))  # Output: ['a','b','c']

# Basic Example 2 (From Tuple):
t = (1,2)
print(list(t))  # Output: [1,2]

# Basic Example 3 (Empty):
print(list())  # Output: []

# DSA Example (Set to List):
unique = {1,2,3}
print(list(unique))  # Output: [1,2,3]

# BUILT-IN FUNCTION: 
enumerate()
# What it does: Pairs indices with elements.
# Why use it: Tracks position in loops.
# How it works: Returns iterator of (index, value).
# When to use: Array traversal needing indices.
# Time/Space: O(1) create, O(1) per iteration.

# Syntax:
enumerate(iterable, start=0)  # (index, value) tuples

# Basic Example 1 (Default Start):
lst = ['a','b']
for i,v in enumerate(lst):
    print(i,v)  # Output: 0 a, 1 b

# Basic Example 2 (Custom Start):
lst = ['x','y']
for i,v in enumerate(lst, 1):
    print(i,v)  # Output: 1 x, 2 y

# Basic Example 3 (String):
text = "ab"
for i,v in enumerate(text):
    print(i,v)  # Output: 0 a, 1 b

# DSA Example (Index Track):
nums = ['a','b']
for i,val in enumerate(nums):
    print(i,val)  # Output: 0 a, 1 b

# BUILT-IN FUNCTION: 
range()
# What it does: Generates number sequence.
# Why use it: Creates loop ranges efficiently.
# How it works: Lazy; doesn't store list.
# When to use: For loops in arrays/matrices.
# Time/Space: O(1) time, O(1) space.

# Syntax:
range(stop)  # From 0 to 'stop-1'
range(start, stop)  # From 'start' to 'stop-1'
range(start, stop, step)  # With 'step'

# Basic Example 1 (To Stop):
print(list(range(3)))  # Output: [0,1,2]

# Basic Example 2 (Start Stop):
print(list(range(1,4)))  # Output: [1,2,3]

# Basic Example 3 (With Step):
print(list(range(0,6,2)))  # Output: [0,2,4]

# DSA Example (Loop Range):
print(list(range(3)))  # Output: [0,1,2]

# BUILT-IN FUNCTION: 
zip()
# What it does: Pairs elements from iterables.
# Why use it: Simultaneous iteration.
# How it works: Stops at shortest; returns iterator.
# When to use: Merging/comparing arrays.
# Time/Space: O(1) create, O(1) per iteration.

# Syntax:
zip(*iterables)  # Tuple iterator from iterables

# Basic Example 1 (Two Lists):
a = [1,2]
b = ['a','b']
print(list(zip(a,b)))  # Output: [(1,'a'),(2,'b')]

# Basic Example 2 (Three Iterables):
c = [3,4]
print(list(zip(a,b,c)))  # Output: [(1,'a',3),(2,'b',4)]

# Basic Example 3 (Uneven Length):
d = [1,2,3]
e = ['x','y']
print(list(zip(d,e)))  # Output: [(1,'x'),(2,'y')]

# DSA Example (Pair Lists):
nums = [1,2]
chars = ['a','b']
print(list(zip(nums,chars)))  # Output: [(1,'a'),(2,'b')]

# BUILT-IN FUNCTION: 
next()
# What it does: Gets next from iterator.
# Why use it: Step-by-step iteration.
# How it works: Advances iterator; default if end.
# When to use: Custom traversal.
# Time/Space: O(1) time, O(1) space.

# Syntax:
next(iterator, default)  # Next item or 'default'

# Basic Example 1 (From List Iter):
it = iter([1,2])
print(next(it))  # Output: 1

# Basic Example 2 (With Default):
it = iter([])
print(next(it, 0))  # Output: 0

# Basic Example 3 (String Iter):
it = iter("ab")
print(next(it))  # Output: 'a'

# DSA Example (Traversal):
iter_nums = iter([1,2,3])
print(next(iter_nums))  # Output: 1

# BUILT-IN FUNCTION: 
set()
# What it does: Creates set from iterable.
# Why use it: Unique elements, fast membership.
# How it works: Removes duplicates; unordered.
# When to use: Dedup or set ops like union.
# Time/Space: O(n) time, O(n) space.

# Syntax:
set(iterable)  # New set from 'iterable'

# Basic Example 1 (From List):
lst = [1,2,2]
print(set(lst))  # Output: {1,2}

# Basic Example 2 (From String):
text = "aab"
print(set(text))  # Output: {'a','b'}

# Basic Example 3 (Empty):
print(set())  # Output: set()

# DSA Example (Remove Dups):
nums = [1,2,2]
print(set(nums))  # Output: {1,2}

# BUILT-IN FUNCTION: isinstance()
# What it does: Checks object type instance.
# Why use it: Validates types flexibly.
# How it works: True if matches type/subclass.
# When to use: Input validation.
# Time/Space: O(1) time, O(1) space.

# Syntax:
isinstance(object, type)  # True if instance

# Basic Example 1 (Single Type):
v = "abc"
print(isinstance(v, str))  # Output: True

# Basic Example 2 (Tuple Types):
n = 5
print(isinstance(n, (int, float)))  # Output: True

# Basic Example 3 (False Check):
l = [1]
print(isinstance(l, str))  # Output: False

# DSA Example (Type Validation):
value = "123"
print(isinstance(value, str))  # Output: True

# BUILT-IN FUNCTION: 
type()
# What it does: Returns object type.
# Why use it: Identifies data types.
# How it works: Returns class like <class 'int'>.
# When to use: Parsing or type checks.
# Time/Space: O(1) time, O(1) space.

# Syntax:
type(object)  # Returns type class

# Basic Example 1 (String Type):
v = "abc"
print(type(v))  # Output: <class 'str'>

# Basic Example 2 (Int Type):
n = 5
print(type(n))  # Output: <class 'int'>

# Basic Example 3 (List Type):
l = []
print(type(l))  # Output: <class 'list'>

# DSA Example (Validation):
value = "123"
print(type(value) == str)  # Output: True

# BUILT-IN FUNCTION: 
sorted()
# What it does: Returns sorted list from iterable.
# Why use it: Sorts without modifying original.
# How it works: Stable sort; new list.
# When to use: Binary search prep.
# Time/Space: O(n log n) time, O(n) space.

# Syntax:
sorted(iterable, reverse=False)  # New sorted list

# Basic Example 1 (Asc Sort):
lst = [3,1,2]
print(sorted(lst))  # Output: [1,2,3]

# Basic Example 2 (Desc Sort):
lst = [1,3,2]
print(sorted(lst, reverse=True))  # Output: [3,2,1]

# Basic Example 3 (String Sort):
text = "bac"
print(sorted(text))  # Output: ['a','b','c']

# DSA Example (Array Sort):
nums = [3,1,2]
print(sorted(nums))  # Output: [1,2,3]

# ADDITIONAL COMMON METHODS/FUNCTIONS FOR LEETCODE

# LIST METHOD: 
.sort()
# What it does: Sorts list in place.
# Why use it: Prepares for search/patterns.
# How it works: Modifies original; stable.
# When to use: Two-pointer or binary search.
# Time/Space: O(n log n) time, O(1) space.

# Syntax:
list.sort(reverse=False)  # Sorts in place

# Basic Example 1 (Asc Sort):
lst = [3,1,2]
lst.sort()
print(lst)  # Output: [1,2,3]

# Basic Example 2 (Desc Sort):
lst = [1,3,2]
lst.sort(reverse=True)
print(lst)  # Output: [3,2,1]

# Basic Example 3 (Strings):
lst = ['b','a','c']
lst.sort()
print(lst)  # Output: ['a','b','c']

# DSA Example (For Binary):
numbers = [3,1,2]
numbers.sort()
print(numbers)  # Output: [1,2,3]

# BUILT-IN FUNCTION: 
max()
# What it does: Returns largest item.
# Why use it: Finds max without loop.
# How it works: Scans iterable.
# When to use: Max profit/subarray.
# Time/Space: O(n) time, O(1) space.

# Syntax:
max(iterable)  # Largest in 'iterable'

# Basic Example 1 (List Max):
lst = [1,5,3]
print(max(lst))  # Output: 5

# Basic Example 2 (Args Max):
print(max(1,2,3))  # Output: 3

# Basic Example 3 (Strings Max):
lst = ['a','c','b']
print(max(lst))  # Output: 'c'

# DSA Example (Array Max):
numbers = [1,5,3]
print(max(numbers))  # Output: 5

# BUILT-IN FUNCTION: 
sum()
# What it does: Sums iterable items.
# Why use it: Quick totals.
# How it works: Adds numbers; starts at 0.
# When to use: Subarray/cumulative sums.
# Time/Space: O(n) time, O(1) space.

# Syntax:
sum(iterable)  # Sum of elements

# Basic Example 1 (List Sum):
lst = [1,2,3]
print(sum(lst))  # Output: 6

# Basic Example 2 (Tuple Sum):
t = (4,5)
print(sum(t))  # Output: 9

# Basic Example 3 (Empty Sum):
print(sum([]))  # Output: 0

# DSA Example (Array Sum):
numbers = [1,2,3]
print(sum(numbers))  # Output: 6

# BUILT-IN FUNCTION: 
tuple()
# What it does: Creates tuple from iterable.
# Why use it: Immutable sequences.
# How it works: Copies to fixed collection.
# When to use: Dict keys or multiple returns.
# Time/Space: O(n) time, O(n) space.

# Syntax:
tuple(iterable)  # New tuple

# Basic Example 1 (From List):
lst = [1,2]
print(tuple(lst))  # Output: (1,2)

# Basic Example 2 (From String):
text = "ab"
print(tuple(text))  # Output: ('a','b')

# Basic Example 3 (Empty):
print(tuple())  # Output: ()

# DSA Example (List to Tuple):
nums = [1,2,3]
print(tuple(nums))  # Output: (1,2,3)

# BUILT-IN FUNCTION: 
dict()
# What it does: Creates dict from pairs/kwargs.
# Why use it: Builds key-value maps.
# How it works: From iterable or args.
# When to use: Counts or caches.
# Time/Space: O(n) time, O(n) space.

# Syntax:
dict(iterable)  # From pairs

# Basic Example 1 (From Pairs):
pairs = [('a',1),('b',2)]
print(dict(pairs))  # Output: {'a':1,'b':2}

# Basic Example 2 (From Kwargs):
print(dict(x=3,y=4))  # Output: {'x':3,'y':4}

# Basic Example 3 (Empty):
print(dict())  # Output: {}

# DSA Example (From Pairs):
pairs = [('a',1),('b',2)]
print(dict(pairs))  # Output: {'a':1,'b':2}

# BUILT-IN FUNCTION: 
iter()
# What it does: Creates iterator from iterable.
# Why use it: Manual iteration control.
# How it works: Returns iterator object.
# When to use: Custom traversal with next().
# Time/Space: O(1) time, O(1) space.

# Syntax:
iter(iterable)  # Iterator for 'iterable'

# Basic Example 1 (List Iter):
lst = [1,2]
it = iter(lst)
print(next(it))  # Output: 1

# Basic Example 2 (String Iter):
text = "ab"
it = iter(text)
print(next(it))  # Output: 'a'

# Basic Example 3 (Set Iter):
s = {1,2}
it = iter(s)
print(next(it))  # Output: 1 (order varies)

# DSA Example (List Iter):
nums = [1,2,3]
it = iter(nums)
print(next(it))  # Output: 1

















# LIST METHOD: .append()
# What it does: Adds a single element to the end of a list.
# Why use it: Grows lists dynamically, efficient for building results.
# How it works: Modifies list in place; amortized O(1) time.
# When to use: In loops for collecting items (e.g., array building, stack push).
# Time/Space: O(1) amortized time, O(1) space per call.

# Syntax:
list.append(item)  # Adds 'item' to end

# Basic Example 1 (Empty List):
lst = []
lst.append(1)
print(lst)  # Output: [1]

# Basic Example 2 (Add Number):
lst = [1, 2]
lst.append(3)
print(lst)  # Output: [1, 2, 3]

# Basic Example 3 (Add String):
lst = ['a', 'b']
lst.append('c')
print(lst)  # Output: ['a', 'b', 'c']

# DSA Example (Build Result in Loop):
result = []
for i in range(3):
    result.append(i)
print(result)  # Output: [0, 1, 2]


















# fix methods guide
# make it super clear with simple examples


# # DSA Example 1 (Key-Value Iteration):
# ages = {"Alice": 25, "Bob": 30}
# print(list(ages.items()))  # Output: [("Alice", 25), ("Bob", 30)]
















# how to identidy time and space
# how to know if  aquestion is commonly asked






# What is point of this from typing import List


# prefix[j] - prefix[i - 1]
# prefix[j] - prefix[i] + nums[i]


# # Template 1
# def fn(arr):
#     prefix = [arr[0]]
#     for i in range(1, len(arr)):
#         prefix.append(prefix[-1] + arr[i])
    
#     return prefix

# print(fn([1, 6, 3, 2, 7, 2]))


# # Template 2
# def prefix_sum(arr):
#     prefix = [arr[0]]  # Array to store prefix sums, starts with first element
#     curr = arr[0]      # Tracks running sum for building prefix array
    
#     for i in range(1, len(arr)):  # Iterate from index 1
#         # Add current element to running sum
#         curr += arr[i]
#         # Append running sum to prefix array
#         prefix.append(curr)
    
#     return prefix  # Return prefix sum array for subarray sum queries

# print(prefix_sum([1, 6, 3, 2, 7, 2]))
