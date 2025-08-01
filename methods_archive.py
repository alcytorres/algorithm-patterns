# DELETE, DELETE DELETE

# Delete this once you determine there is no more value
# Note I updated to a better version of this guide under methods.py


# STRING METHODS
# LIST METHODS
# DICTIONARY METHODS
# SET METHODS
# BUILT-IN FUNCTIONS
# SPECIAL METHODS



# ----------------------------------------------------------------------------------
# STRING METHOD: 
.upper()
# What it does: Converts all characters in a string to uppercase.
# DSA use case: Normalizes strings for case-insensitive comparisons (e.g., palindrome or anagram problems).
# Why it’s useful: Ensures consistent string format, avoiding case-related errors in string manipulation.
# Time/Space: O(n) time (n = string length), O(n) space for new string.
# Syntax:
string.upper()  # Returns a new string with all uppercase letters
# DSA Example 1 (Case-Insensitive Comparison):
text = "Hello"
print(text.upper())  # Output: "HELLO"
# DSA Example 2 (Palindrome Check Prep):
word = "RaCeCaR"
print(word.upper())  # Output: "RACECAR"


# STRING METHOD: 
.lower()
# What it does: Converts all characters in a string to lowercase.
# DSA use case: Standardizes strings for case-insensitive matching (e.g., string pattern problems).
# Why it’s useful: Simplifies string comparisons by eliminating case differences.
# Time/Space: O(n) time (n = string length), O(n) space for new string.
# Syntax:
string.lower()  # Returns a new string with all lowercase letters
# DSA Example 1 (Case-Insensitive Search):
text = "WORLD"
print(text.lower())  # Output: "world"
# DSA Example 2 (Anagram Prep):
word = "Listen"
print(word.lower())  # Output: "listen"


# STRING METHOD: 
.replace()
# What it does: Replaces all occurrences of a substring with another substring.
# DSA use case: Modifies strings in-place for pattern matching or text processing (e.g., string transformation).
# Why it’s useful: Efficiently updates specific parts of a string without manual parsing.
# Time/Space: O(n) time (n = string length), O(n) space for new string.
# Syntax:
string.replace(old, new)  # Returns a new string with 'old' replaced by 'new'
# DSA Example 1 (Text Transformation):
text = "cat hat"
print(text.replace("hat", "cap"))  # Output: "cat cap"
# DSA Example 2 (Clean String):
text = "a#a#a"
print(text.replace("#", ""))  # Output: "aaa"


# STRING METHOD: 
.isdigit()
# What it does: Checks if all characters in a string are digits.
# DSA use case: Validates numeric strings in parsing problems (e.g., atoi, valid number checks).
# Why it’s useful: Quickly confirms if a string represents a number, avoiding manual checks.
# Time/Space: O(n) time (n = string length), O(1) space.
# Syntax:
string.isdigit()  # Returns True if all characters are digits, else False
# DSA Example 1 (Input Validation):
text = "123"
print(text.isdigit())  # Output: True
# DSA Example 2 (Non-Digit Check):
text = "12a3"
print(text.isdigit())  # Output: False


# STRING METHOD: 
.isnumeric()
# What it does: Checks if all characters in a string are numeric (e.g., digits, Unicode numeric characters).
# DSA use case: Validates numeric strings in parsing problems (e.g., atoi, numeric input checks).
# Why it’s useful: Ensures a string contains only numeric characters, useful for robust input validation.
# Time/Space: O(n) time (n = string length), O(1) space.
# Syntax:
string.isnumeric()  # Returns True if all characters are numeric, else False
# DSA Example 1 (Numeric Validation):
text = "123"
print(text.isnumeric())  # Output: True
# DSA Example 2 (Non-Numeric Check):
text = "12a3"
print(text.isnumeric())  # Output: False


# STRING METHOD: 
.split()
# What it does: Splits a string into a list of substrings based on a delimiter (default is whitespace).
# DSA use case: Parses strings into tokens for array or word-based problems (e.g., word count, reverse words).
# Why it’s useful: Simplifies string processing by converting text into manageable list elements.
# Time/Space: O(n) time (n = string length), O(n) space for the resulting list.
# Syntax:
string.split(separator)  # Returns a list of substrings; 'separator' is optional (defaults to whitespace)
# DSA Example 1 (Word Parsing):
text = "hello world"
print(text.split())  # Output: ['hello', 'world']
# DSA Example 2 (Custom Delimiter):
text = "a,b,c"
print(text.split(','))  # Output: ['a', 'b', 'c']


# STRING METHOD: 
.format()
# What it does: Formats a string by replacing placeholders with specified values.
# DSA use case: Constructs formatted output strings in problems requiring specific string patterns (e.g., custom string construction, debugging).
# Why it’s useful: Simplifies creating readable strings with dynamic values, useful for testing or formatting results.
# Time/Space: O(n) time (n = string length), O(n) space for the resulting string.
# Syntax:
string.format(*args, **kwargs)  # Returns a formatted string; placeholders like {0} or {name}
# DSA Example 1 (Format Result):
template = "Value: {}"
print(template.format(42))  # Output: "Value: 42"
# DSA Example 2 (Multiple Values):
template = "x: {}, y: {}"
print(template.format(1, 2))  # Output: "x: 1, y: 2"


# STRING METHOD: 
.join()
# What it does: Concatenates elements of an iterable (e.g., list of strings) into a single string, using a specified separator.
# DSA use case: Combines list elements into a string for output formatting or string manipulation (e.g., reverse words, string construction).
# Why it’s useful: Efficiently builds strings from lists, avoiding manual concatenation loops.
# Time/Space: O(n) time (n = total length of elements), O(n) space for the resulting string.
# Syntax:
separator.join(iterable)  # Returns a string; 'separator' is the string to join elements with
# DSA Example 1 (List to String):
words = ['hello', 'world']
print(' '.join(words))  # Output: "hello world"
# DSA Example 2 (Custom Separator):
chars = ['a', 'b', 'c']
print(','.join(chars))  # Output: "a,b,c"


join()
# Syntax:
# separator.join(iterable)  # Returns a string; 'separator' is the string to join elements with
words = ["1", "2", "3", "4"]
result = " -> ".join(words)
print(result)



# ----------------------------------------------------------------------------------
# LIST METHODS

# LIST METHOD: 
.append()
# What it does: Adds a single element to the end of a list.
# DSA use case: Builds lists dynamically in array or linked list problems (e.g., collecting results, stack operations).
# Why it’s useful: Simple way to grow a list, especially for iterative solutions.
# Time/Space: O(1) amortized time, O(1) space per element.
# Syntax:
list.append(item)  # Modifies the list in place, adding 'item' at the end
# DSA Example 1 (Building Result):
result = [1, 2]
result.append(3)
print(result)  # Output: [1, 2, 3]
# DSA Example 2 (Stack Push):
stack = []
stack.append(5)
print(stack)  # Output: [5]


# LIST METHOD: 
.extend()
# What it does: Adds all elements from an iterable (e.g., list, tuple) to the end of a list.
# DSA use case: Efficiently combines or appends multiple elements in array problems (e.g., merging arrays, collecting results).
# Why it’s useful: Faster than appending items one-by-one; ideal for merging sorted arrays or extending results in-place.
# Time/Space: O(k) time (k = length of iterable), O(k) space for added elements.
# Syntax:
list.extend(iterable)  # Modifies the list in place, adding all items from 'iterable'
# DSA Example 1 (Merging Arrays):
result = [1, 2]
result.extend([3, 4])
print(result)  # Output: [1, 2, 3, 4]
# DSA Example 2 (Collecting Results):
evens = [2, 4]
evens.extend([6, 8])
print(evens)  # Output: [2, 4, 6, 8]


# LIST METHOD: 
.insert()
# What it does: Inserts an element at a specified index in a list.
# DSA use case: Adds elements at specific positions in array manipulation (e.g., inserting in sorted order).
# Why it’s useful: Precise control over element placement, though slower than append/extend.
# Time/Space: O(n) time (n = list length due to shifting), O(1) space per element.
# Syntax:
list.insert(index, item)  # Modifies the list in place, inserting 'item' at 'index'
# DSA Example 1 (Insert in Sorted List):
numbers = [1, 3]
numbers.insert(1, 2)
print(numbers)  # Output: [1, 2, 3]
# DSA Example 2 (Insert at Start):
list = [2, 3]
list.insert(0, 1)
print(list)  # Output: [1, 2, 3]


# LIST METHOD: 
.remove()
# What it does: Removes the first occurrence of a specified value from a list.
# DSA use case: Deletes specific elements in array problems (e.g., removing duplicates or invalid items).
# Why it’s useful: Simplifies value-based removal without needing index knowledge.
# Time/Space: O(n) time (n = list length for search), O(1) space.
# Syntax:
list.remove(value)  # Modifies the list in place; raises ValueError if value not found
# DSA Example 1 (Remove Duplicate):
numbers = [1, 2, 2]
numbers.remove(2)
print(numbers)  # Output: [1, 2]
# DSA Example 2 (Remove Invalid):
list = [0, 1, 0]
list.remove(0)
print(list)  # Output: [1, 0]


# LIST METHOD: 
.pop()
# What it does: Removes and returns an element at a given index (defaults to last item).
# DSA use case: Implements stacks or removes elements in array problems (e.g., stack pop, queue dequeue).
# Why it’s useful: Combines removal and retrieval, efficient for last element.
# Time/Space: O(1) time for last element, O(n) for others (shifting), O(1) space.
# Syntax:
list.pop(index)  # Returns the removed element; 'index' is optional (defaults to -1)
# DSA Example 1 (Stack Pop):
stack = [1, 2, 3]
last = stack.pop()
print(last, stack)  # Output: 3 [1, 2]
# DSA Example 2 (Remove at Index):
list = [1, 2, 3]
item = list.pop(1)
print(item, list)  # Output: 2 [1, 3]



# ----------------------------------------------------------------------------------
# DICTIONARY METHODS

# DICTIONARY METHOD: 
.keys()
# What it does: Returns a view of all keys in a dictionary.
# DSA use case: Iterates over keys in hash map problems (e.g., frequency counting, grouping).
# Why it’s useful: Provides direct access to dictionary keys for iteration or validation.
# Time/Space: O(1) time for view, O(n) to convert to list (n = keys), O(n) space for list.
# Syntax:
dict.keys()  # Returns a view of the dictionary’s keys
# DSA Example 1 (Key Iteration):
ages = {"Alice": 25, "Bob": 30}
print(list(ages.keys()))  # Output: ["Alice", "Bob"]
# DSA Example 2 (Check Keys):
dict = {"a": 1, "b": 2}
print("a" in dict.keys())  # Output: True


# DICTIONARY METHOD: 
.get()
# What it does: Retrieves the value for a key in a dictionary, returning a default if the key is not found.
# DSA use case: Safely accesses values in hash maps (e.g., frequency counting, avoiding KeyError).
# Why it’s useful: Prevents errors when keys may not exist, common in dynamic problems.
# Time/Space: O(1) average time, O(1) space.
# Syntax:
dict.get(key, default)  # Returns the value for 'key' or 'default' (None if not specified)
# DSA Example 1 (Frequency Count):
counts = {"a": 1}
counts["b"] = counts.get("b", 0) + 1
print(counts)  # Output: {"a": 1, "b": 1}
# DSA Example 2 (Default Value):
ages = {"Alice": 25}
print(ages.get("Bob", 0))  # Output: 0


# DICTIONARY METHOD: 
.items()
# What it does: Returns a view of a dictionary’s key-value pairs as tuples.
# DSA use case: Iterates over both keys and values in hash map problems (e.g., frequency counting, key-value processing).
# Why it’s useful: Simplifies simultaneous access to keys and values, avoiding separate key lookups.
# Time/Space: O(1) time for view, O(n) to convert to list (n = pairs), O(n) space for list.
# Syntax:
dict.items()  # Returns a view of (key, value) tuples
# DSA Example 1 (Key-Value Iteration):
ages = {"Alice": 25, "Bob": 30}
print(list(ages.items()))  # Output: [("Alice", 25), ("Bob", 30)]
# DSA Example 2 (Process Pairs):
counts = {"a": 2, "b": 1}
for k, v in counts.items():
    print(k, v)  # Output: a 2, b 1



# ----------------------------------------------------------------------------------
# SET METHODS

# SET METHOD: 
.add()
# What it does: Adds a single element to a set if it’s not already present.
# DSA use case: Maintains unique elements in problems like deduplication or membership testing.
# Why it’s useful: Efficiently builds sets for unique item tracking, O(1) average time.
# Time/Space: O(1) average time, O(1) space per element.
# Syntax:
set.add(element)  # Modifies the set in place, adding 'element'
# DSA Example 1 (Track Unique):
unique = {1, 2}
unique.add(3)
print(unique)  # Output: {1, 2, 3}
# DSA Example 2 (Avoid Duplicate):
seen = {1}
seen.add(1)  # No effect
print(seen)  # Output: {1}



# ----------------------------------------------------------------------------------
# BUILT-IN FUNCTIONS

# BUILT-IN FUNCTION: 
len()
# What it does: Returns the length (number of items) of an object (list, string, etc.).
# DSA use case: Determines size for loops, bounds checking, or validation (e.g., array, string problems).
# Why it’s useful: Essential for iteration and condition checks in most algorithms.
# Time/Space: O(1) time, O(1) space.
# Syntax:
len(object)  # Returns an integer representing the length
# DSA Example 1 (Array Length):
array = [1, 2, 3]
print(len(array))  # Output: 3
# DSA Example 2 (String Length):
text = "abc"
print(len(text))  # Output: 3


# BUILT-IN FUNCTION: 
str()
# What it does: Converts an object to its string representation.
# DSA use case: Converts numbers or objects to strings for output formatting or string manipulation (e.g., string concatenation, parsing).
# Why it’s useful: Enables string operations on non-string data, common in problems requiring text output or type conversion.
# Time/Space: O(n) time (n = string length or object complexity), O(n) space for the new string.
# Syntax:
str(object)  # Returns the string representation of 'object'
# DSA Example 1 (Number to String):
num = 123
print(str(num) + " is a number")  # Output: "123 is a number"
# DSA Example 2 (List to String):
lst = [1, 2]
print(str(lst))  # Output: "[1, 2]"


# BUILT-IN FUNCTION: 
int()
# What it does: Converts a value (like a string or float) to an integer.
# DSA use case: Parses numeric strings in problems like atoi or mathematical computations.
# Why it’s useful: Enables type conversion for arithmetic operations.
# Time/Space: O(n) time (n = string length for strings), O(1) space.
# Syntax:
int(value)  # Returns an integer; 'value' can be a string, float, etc.
# DSA Example 1 (String to Number):
num = "123"
print(int(num) + 1)  # Output: 124
# DSA Example 2 (Float to Int):
value = 5.7
print(int(value))  # Output: 5


# BUILT-IN FUNCTION: 
float()
# What it does: Converts a value (like a string or integer) to a decimal (floating-point number).
# DSA use case: Handles decimal inputs in numerical problems (e.g., geometric or precision calculations).
# Why it’s useful: Supports floating-point arithmetic when decimals are needed.
# How it works:
    # Takes a string (like "123.45") or an integer (like 5) as input.
    # Returns a float (a number with decimals).
# Time/Space: O(n) time (n = string length for strings), O(1) space.
# Syntax:
float(value)  # Returns a float; 'value' can be a string, integer, etc.

# DSA Example 1 (String to Float):
num = "123.45"
print(float(num) + 0.55)  # Output: 124.0
# DSA Example 2 (Int to Float):
value = 5
print(float(value))  # Output: 5.0


# BUILT-IN FUNCTION: 
input()
# What it does: Reads a line of input from the user as a string.
# DSA use case: Collects test inputs in interactive problems or local testing.
# Why it’s useful: Simplifies user input for debugging or problem setup.
# Time/Space: O(n) time (n = input length), O(n) space for string.
# Syntax:
input(prompt)  # Returns a string; 'prompt' is optional text to display
# DSA Example 1 (Read Number):
# num = input("Enter number: ")
# print(int(num) + 1)  # Output: [user input + 1]
# DSA Example 2 (Read String):
# text = input("Enter text: ")
# print(text.upper())  # Output: [user input in uppercase]


# BUILT-IN FUNCTION: 
list()
# What it does: Creates a list from an iterable or converts an object to a list.
# DSA use case: Converts data structures (e.g., strings, sets) to lists for array manipulation.
# Why it’s useful: Enables list operations on non-list iterables in array problems.
# Time/Space: O(n) time (n = iterable length), O(n) space.
# Syntax:
list(iterable)  # Returns a new list; 'iterable' is optional
# DSA Example 1 (String to List):
text = "abc"
print(list(text))  # Output: ['a', 'b', 'c']
# DSA Example 2 (Set to List):
unique = {1, 2, 3}
print(list(unique))  # Output: [1, 2, 3]


# BUILT-IN FUNCTION: 
tuple()
# What it does: Creates a tuple from an iterable or converts an object to a tuple.
# DSA use case: Creates immutable sequences for data storage (e.g., fixed pairs in hash maps, return multiple values).
# Why it’s useful: Provides immutable collections, safer for keys in dictionaries or constant data.
# Time/Space: O(n) time (n = iterable length), O(n) space.
# Syntax:
tuple(iterable)  # Returns a new tuple; 'iterable' is optional
# DSA Example 1 (List to Tuple):
nums = [1, 2, 3]
print(tuple(nums))  # Output: (1, 2, 3)
# DSA Example 2 (String to Tuple):
text = "abc"
print(tuple(text))  # Output: ('a', 'b', 'c')


# BUILT-IN FUNCTION: 
dict()
# What it does: Creates a dict from pairs or kwargs.
# DSA use case: Map keys to values (e.g., counts, caches).
# Why it’s useful: Fast lookups, flexible keys.
# Time/Space: O(n) time/space (n = items).
# Syntax:
dict(iterable)  # From pairs: dict([('a',1), ('b',2)])
# DSA Example 1 (From List of Pairs):
pairs = [('a',1), ('b',2)]
d = dict(pairs)
print(d)  # {'a':1, 'b':2}
# DSA Example 2 (Empty):
d = dict()
d['key'] = 'val'


# BUILT-IN FUNCTION: 
enumerate()
# What it does: Returns an iterator of tuples containing indices and elements from an iterable.
# DSA use case: Tracks both index and value during iteration (e.g., array traversal, index-based operations).
# Why it’s useful: Simplifies loops needing both element and position, avoiding manual index tracking.
# Time/Space: O(1) time to create iterator, O(1) space per iteration.
# Syntax:
enumerate(iterable, start=0)  # Returns (index, element) tuples; 'start' is optional
# DSA Example 1 (Index Tracking):
nums = ['a', 'b']
for i, val in enumerate(nums):
    print(i, val)  # Output: 0 a, 1 b
# DSA Example 2 (Custom Start):
chars = ['x', 'y']
for i, val in enumerate(chars, start=1):
    print(i, val)  # Output: 1 x, 2 y


# BUILT-IN FUNCTION: 
iter()
# What it does: Creates an iterator from an iterable object (e.g., list, string).
# DSA use case: Enables manual iteration in problems requiring custom traversal (e.g., array or string processing).
# Why it’s useful: Allows fine-grained control over iteration, often paired with next() for step-by-step processing.
# Time/Space: O(1) time to create iterator, O(1) space.
# Syntax:
iter(iterable)  # Returns an iterator for 'iterable'
# DSA Example 1 (List Iterator):
nums = [1, 2, 3]
it = iter(nums)
print(next(it))  # Output: 1
# DSA Example 2 (String Iterator):
text = "abc"
it = iter(text)
print(next(it))  # Output: 'a'

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





# BUILT-IN FUNCTION: 
range()
# What it does: Generates a sequence of numbers from 'start' to 'stop-1', optionally with a 'step'.
# DSA use case: Creates iteration ranges for loops in array or matrix problems.
# Why it’s useful: Efficiently generates sequences without storing large lists.
# Time/Space: O(1) time to create, O(1) space (stores only start/stop/step).
# Syntax:
range(stop)  # From 0 to 'stop-1'
range(start, stop, step)  # From 'start' to 'stop-1' with 'step'
# Example 1
print(range(5))  # Output: range(0, 5)
# Example 2
print(list(range(5))) # Output: [0, 1, 2, 3, 4]

# DSA Example 1 (Loop Range):
print(list(range(3)))  # Output: [0, 1, 2]
# DSA Example 2 (Custom Range):
print(list(range(1, 5, 2)))  # Output: [1, 3]


# BUILT-IN FUNCTION: 
zip()
# What it does: Combines multiple iterables into an iterator of tuples, pairing elements by position.
# DSA use case: Pairs elements from multiple lists in problems like merging or comparing arrays (e.g., two-pointer, matrix operations).
# Why it’s useful: Simplifies simultaneous iteration over multiple sequences, reducing manual index management.
# Time/Space: O(1) time to create iterator, O(1) space per iteration.
# Syntax:
zip(*iterables)  # Returns an iterator of tuples; each tuple contains elements from 'iterables'
# DSA Example 1 (Pair Lists):
nums = [1, 2]
chars = ['a', 'b']
print(list(zip(nums, chars)))  # Output: [(1, 'a'), (2, 'b')]
# DSA Example 2 (Matrix Transpose Prep):
matrix = [[1, 2], [3, 4]]
print(list(zip(*matrix)))  # Output: [(1, 3), (2, 4)]


# BUILT-IN FUNCTION: 
next()
# What it does: Retrieves the next item from an iterator, with an optional default if the iterator is exhausted.
# DSA use case: Accesses elements from iterators in problems involving iteration (e.g., custom traversal, generator processing).
# Why it’s useful: Provides controlled access to iterator elements, useful for single-step iteration or handling finite sequences.
# Time/Space: O(1) time per call, O(1) space.
# Syntax:
next(iterator, default)  # Returns the next item from 'iterator'; returns 'default' if exhausted (optional)
# DSA Example 1 (Iterator Traversal):
iter_nums = iter([1, 2, 3])
print(next(iter_nums))  # Output: 1
# DSA Example 2 (Default Value):
iter_empty = iter([])
print(next(iter_empty, 0))  # Output: 0


# BUILT-IN FUNCTION: 
set()
# What it does: Creates a set from an iterable, storing unique elements.
# DSA use case: Removes duplicates or performs set operations (e.g., intersection, union) in array problems.
# Why it’s useful: Fast deduplication and membership testing, O(1) average time.
# Time/Space: O(n) time (n = iterable length), O(n) space.
# Syntax:
set(iterable)  # Returns a new set; 'iterable' is optional
# DSA Example 1 (Remove Duplicates):
nums = [1, 2, 2]
print(set(nums))  # Output: {1, 2}
# DSA Example 2 (Unique Elements):
chars = ['a', 'a', 'b']
print(set(chars))  # Output: {'a', 'b'}


# BUILT-IN FUNCTION: 
isinstance()
# What it does: Checks if an object is an instance of a specified type or tuple of types.
# DSA use case: Validates object types in problems requiring type-specific logic (e.g., input validation, polymorphic handling).
# Why it’s useful: Provides flexible type checking, ensuring correct data handling in algorithms.
# Time/Space: O(1) time, O(1) space.
# Syntax:
isinstance(object, type)  # Returns True if 'object' is an instance of 'type' or its subclasses
# DSA Example 1 (Type Validation):
value = "123"
print(isinstance(value, str))  # Output: True
# DSA Example 2 (Multiple Types):
num = 42
print(isinstance(num, (int, float)))  # Output: True


# BUILT-IN FUNCTION: 
type()
# What it does: Returns the type of an object (e.g., int, str, list).
# DSA use case: Validates or identifies data types in problems requiring type-specific handling (e.g., input parsing, type checking).
# Why it’s useful: Ensures correct data type before operations, preventing type-related errors in algorithms.
# Time/Space: O(1) time, O(1) space.
# Syntax:
type(object)  # Returns the type of 'object' (e.g., <class 'int'>)
# DSA Example 1 (Type Validation):
value = "123"
print(type(value) == str)  # Output: True
# DSA Example 2 (Type Check):
num = 42
print(type(num) == int)  # Output: True


# BUILT-IN FUNCTION: 
sorted()
# What it does: Returns a new sorted list from the elements of an iterable.
# DSA use case: Sorts arrays or iterables for problems like binary search, two-pointer, or pattern finding.
# Why it’s useful: Creates a sorted copy without modifying the original, ideal when preserving input is needed.
# Time/Space: O(n log n) time (n = iterable length), O(n) space for the new list.
# Syntax:
sorted(iterable, reverse=False)  # Returns a new sorted list; 'reverse=True' for descending
# DSA Example 1 (Sort Array):
nums = [3, 1, 2]
print(sorted(nums))  # Output: [1, 2, 3]
# DSA Example 2 (Sort Descending):
chars = ['b', 'a', 'c']
print(sorted(chars, reverse=True))  # Output: ['c', 'b', 'a']



# ----------------------------------------------------------------------------------
# ADDITIONAL COMMON METHODS/FUNCTIONS FOR LEETCODE
# LIST METHOD: 
.sort()
# What it does: Sorts the elements of a list in ascending order.
# DSA use case: Prepares arrays for binary search or pattern finding (e.g., two-pointer problems).
# Why it’s useful: In-place sorting simplifies many algorithms, avoiding extra space.
# Time/Space: O(n log n) time (n = list length), O(1) space (in-place).
# Syntax:
list.sort()  # Modifies the list in place; optional 'reverse=True' for descending
# DSA Example 1 (Sort for Binary Search):
numbers = [3, 1, 2]
numbers.sort()
print(numbers)  # Output: [1, 2, 3]
# DSA Example 2 (Sort Descending):
list = [3, 1, 2]
list.sort(reverse=True)
print(list)  # Output: [3, 2, 1]


# ----------------------------------------------------------------------------------
# BUILT-IN FUNCTION: 
max()
# What it does: Returns the largest item in an iterable or among arguments.
# DSA use case: Finds maximum values in arrays (e.g., max profit, max subarray).
# Why it’s useful: Quick way to identify the largest element without manual comparison.
# Time/Space: O(n) time (n = iterable length), O(1) space.
# Syntax:
max(iterable)  # Returns the maximum value; can also compare multiple arguments
# DSA Example 1 (Max in Array):
numbers = [1, 5, 3]
print(max(numbers))  # Output: 5
# DSA Example 2 (Max of Values):
print(max(1, 2, 3))  # Output: 3


# BUILT-IN FUNCTION: 
sum()
# What it does: Calculates the sum of all items in an iterable (e.g., list of numbers).
# DSA use case: Computes totals in array problems (e.g., subarray sum, cumulative sums).
# Why it’s useful: Simplifies arithmetic aggregation, avoiding manual loops.
# Time/Space: O(n) time (n = iterable length), O(1) space.
# Syntax:
sum(iterable)  # Returns the sum of all elements in 'iterable'
# DSA Example 1 (Array Sum):
numbers = [1, 2, 3]
print(sum(numbers))  # Output: 6
# DSA Example 2 (Subarray Sum):
subarray = [2, 3]
print(sum(subarray))  # Output: 5



# ----------------------------------------------------------------------------------
# SPECIAL METHODS

__init__()
# What it does: Initializes a new instance of a class with specified attributes.

# __init__(self, ...): Sets up a new object when created. It’s like filling out a form with initial details (e.g., age, name) for the object.


# DSA use case: Sets up objects for data structures (e.g., nodes in trees, linked lists, or custom classes in problems).
# Why it’s useful: Defines initial state of objects, essential for creating structured data in algorithms.
# Time/Space: O(1) time (depends on initialization logic), O(1) space (excluding stored attributes).
# Syntax:
def __init__(self, *args):  # Constructor; 'self' is instance, '*args' for attributes
# DSA Example 1 (Basic Class):
class Human:
    def __init__(self, name):
        self.name = name
h = Human("Alice")
print(h.name)  # Output: "Alice"

# DSA Example 2 (Node for Linked List):
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
node = Node(5)
print(node.value)  # Output: 5


# SPECIAL METHOD: 
__str__(self)
# What it does: Defines the string representation of an object when str() or print() is called.

# __str__(self): Tells Python how to turn the object into a string when printed. It’s like writing a short description of the object.

# The __str__ method is called when the following functions are invoked on the object and return a string:
    # The print() method
    # The str() method


# DSA use case: Provides readable output for custom objects in debugging or result formatting (e.g., custom data structures).
# Why it’s useful: Makes objects human-readable, aiding in testing and understanding complex structures.
# Time/Space: O(n) time (n = string length), O(n) space for the string.
# Syntax:
def __str__(self):  # Returns a string describing the instance

# Example 
num = 123
string_rep = str(num)
print(type(string_rep))  # Output: '123'

# DSA Example 1 (Human Class):
class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def __str__(self):
        return f"{self.name}, {self.age}"
h = Human(23, "John")
print(h)  # Output: "John, 23"

# DSA Example 2 (Node String):
class Node:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"Node({self.value})"
node = Node(5)
print(node)  # Output: "Node(5)"