# ============================================================
# METHODS and BUILT-IN FUNCTIONS GUIDE
# ============================================================
# STRING METHODS
# LIST METHODS
# DICTIONARY METHODS
# SET METHODS
# BUILT-IN FUNCTIONS
# SPECIAL METHODS


# Goal: Build a frequency-based ordering perfectly — scannable, practical, interview-ready Guide.
  # Your order is now OPTIMAL for:
    # Entry-level roles
    # Non-FAANG companies
    # LeetCode Easy/Medium
    # Fast scanning & muscle memory

# Placement Rule:
  # Rank by LeetCode frequency (Easy/Medium, non-FAANG) → Place in natural problem-solving flow.

# How I decide:
  # How often it appears in real problems
  # When it’s used in the solution (input → process → output)
  # What it pairs with (e.g., .split() → .join(), ord() → chr())
  # Put most-used first — so you scan → find → use in 3 seconds



# ============================================================
# STRING METHODS
# ============================================================

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
s = " a b  c"
print(s.split())  # Output: ['a', 'b', 'c']

# Basic Example 2 (Custom Delimiter):
s = "1,2,3"
print(s.split(','))  # Output: ['1', '2', '3']

# Basic Example 3: Splitting a path (LeetCode-relevant)
path = "/a//b/c/"
print(path.split('/'))
# ['', 'a', '', 'b', 'c', '']  ← empty strings come from extra slashes

# DSA Example (Reverse Words in a String):
s = "sky is blue"
words = s.split()            # → ['sky', 'is', 'blue']
print(" ".join(words[::-1])) # → "blue is sky"


"""
📘 split() Mini Cheat Sheet

split()                → smart whitespace split
   • collapses spaces
   • trims ends
   • no empty strings

split(delimiter)       → literal split
   • every delimiter counts
   • keeps empty strings
   • no trimming/collapsing

Examples:
" a  b ".split()       → ['a','b']
"/a//b/".split('/')    → ['','a','','b','']

---
Character Walkthrough: s = "/a//b/c/" 
  s.split('/') → ['', 'a', '', 'b', 'c', '']

    /  starts a new piece → ''  
    a  added to piece → 'a'
    /  slash ends piece → 'a' saved
    /  slash again → empty piece '' saved
    b  added → 'b'
    /  ends piece → 'b' saved
    c  added → 'c'
    /  ends piece → 'c' saved
    (end) trailing slash → '' saved

    Final: ['', 'a', '', 'b', 'c', '']

"""


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
chars = ["a", "b"]
print(" ".join(words))  # Output: "a b"

# Basic Example 2 (No Separator):
chars = ["a", "b"]
print("".join(chars))  # Output: "ab"

# Basic Example 3 (Comma Separator):
chars = ["a", "b", "c"]
print(",".join(chars))  # Output: "a,b,c"

# Basic Example 4 (Arrow Separator):
nums = ["1", "2", "3", "4"]
print(" -> ".join(words))  # 1 -> 2 -> 3 -> 4

# DSA Example (List to String):
chars = ["a", "b"]
print("".join(words))  # Output: "ab"


# STRING METHOD: 
ord()
# What it does: Returns Unicode code point of a character.
# Why use it: Converts char to int for indexing or math.
# How it works: 'a' → 97, 'A' → 65, '0' → 48.
# When to use: String → array index (e.g., 26-letter problems).
# Time/Space: O(1) time, O(1) space.

# Syntax:
ord(char)  # char must be length 1

# Basic Example 1:
print(ord('a'))  # Output: 97

# Basic Example 2:
print(ord('A'))  # Output: 65

# Basic Example 3:
print(ord('0'))  # Output: 48

# DSA Example (Char to Index):
s = "abc"
index = ord(s[0]) - ord('a')  # 'a' → 0
print(index)  # Output: 0


# STRING METHOD: 
chr()
# What it does: Returns character from Unicode code point.
# Why use it: Converts int to char (reverse of ord()).
# How it works: 97 → 'a', 65 → 'A'.
# When to use: Building strings from indices.
# Time/Space: O(1) time, O(1) space.

# Syntax:
chr(integer)  # integer in valid Unicode range

# Basic Example 1:
print(chr(97))  # Output: a

# Basic Example 2:
print(chr(65))  # Output: A

# Basic Example 3:
print(chr(48))  # Output: 0

# DSA Example (Index to Char):
index = 0
char = chr(index + ord('a'))
print(char)  # Output: a


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




# ============================================================
# LIST METHODS
# ============================================================

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


# LIST METHOD: 
.reverse()
# What it does: Reverses list in place.
# Why use it: Flips order without creating new list.
# How it works: Modifies original; O(n) time.
# When to use: Two-pointer, palindrome, or reverse traversal.
# Time/Space: O(n) time, O(1) space.

# Syntax:
list.reverse()  # Reverses list in place

# Basic Example 1 (Simple List):
lst = [1, 2, 3]
lst.reverse()
print(lst)  # Output: [3, 2, 1]

# Basic Example 2 (Empty List):
lst = []
lst.reverse()
print(lst)  # Output: []

# Basic Example 3 (Single Element):
lst = [1]
lst.reverse()
print(lst)  # Output: [1]

# DSA Example (Two-Pointer Prep):
nums = [1, 2, 3]
nums.reverse()
print(nums)  # Output: [3, 2, 1]


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





# ============================================================
# DICTIONARY METHODS
# ============================================================

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
.values()
# What it does: Returns a view of all values in a dictionary.
# Why use it: Accesses values for iteration or aggregation.
# How it works: Dynamic view; updates with dict changes.
# When to use: Summing values or checking ranges in hash maps.
# Time/Space: O(1) time for view, O(n) for list conversion (n = values).

# Syntax:
dict.values()  # Returns a view of dictionary values

# Basic Example 1 (Get Values):
d = {"a": 1, "b": 2}
print(list(d.values()))  # Output: [1, 2]

# Basic Example 2 (Empty Dict):
d = {}
print(list(d.values()))  # Output: []

# Basic Example 3 (Sum Values):
d = {"a": 1, "b": 3}
print(sum(d.values()))  # Output: 4

# DSA Example (Value Aggregation):
scores = {"Alice": 90, "Bob": 85}
print(sum(scores.values()))  # Output: 175





# ============================================================
# SET METHODS
# ============================================================

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


# SET METHOD: 
.remove()
# What it does: Removes a specific element from the set.
# Why use it: Deletes a known element quickly.
# How it works: O(1) average lookup and removal; raises KeyError if not present.
# When to use: Removing seen elements, invalid items, or deduplication cleanup.
# Time/Space: O(1) average time, O(1) space.

# Syntax:
set.remove(element)  # Removes 'element'; raises KeyError if not found

# Basic Example 1 (Remove Existing):
s = {1, 2, 3}
s.remove(2)
print(s)  # Output: {1, 3}

# Basic Example 2 (No Error on Duplicate):
s = {1, 2}
s.remove(2)
s.remove(2)  # Raises KeyError

# Basic Example 3 (Safe Removal):
s = {1, 2}
if 2 in s:
    s.remove(2)
print(s)  # Output: {1}

# DSA Example (Remove Seen):
seen = {1, 2, 3}
seen.remove(2)
print(seen)  # Output: {1, 3}





# ============================================================
# BUILT-IN FUNCTIONS
# ============================================================

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
print()
# What it does: Outputs objects to console with formatting.
# Why use it: Debugs code and displays results.
# How it works: Converts args to strings; customizable sep/end.
# When to use: Testing outputs during DSA problem solving.
# Time/Space: O(n) time (n = output length), O(1) space.

# Syntax:
print(*objects, sep=' ', end='\n')  # Prints objects; sep/end optional

# Basic Example 1 (Single Value):
print(42)  # Output: 42

# Basic Example 2 (Multiple Values):
print(1, "abc", True)  # Output: 1 abc True

# DSA Example (Debug Array):
nums = [1, 2, 3]
print("nums:", nums)  # Output: nums: [1, 2, 3]


print(*objects, sep=' ', end='\n')
    # sep: separates multiple objects with custom text (default ' ')
    # end: ends output with custom text (default '\n')

# Basic Example 4 (Custom Separator):
print("a", "b", "c", sep="-")  # a-b-c

# Basic Example 5 (Custom Ending – no newline):
print("Hello", end="!")  # Hello!

# Basic Example 6 (Custom join + custom end with newline):
print("a", "b", sep="-", end=".\n")  # a-b.


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


# BUILT-IN FUNCTION: 
reversed()
# What it does: Returns reverse iterator of sequence.
# Why use it: Reverses without modifying original.
# How it works: Returns iterator; use list() to materialize.
# When to use: When you need reversed view but want to keep original.
# Time/Space: O(1) to create, O(n) to consume.

# Syntax:
reversed(sequence)  # Returns reverse iterator

# Basic Example 1 (List to Iterator):
nums = [1, 2, 3]
rev = reversed(nums)
print(list(rev))  # Output: [3, 2, 1]

# Basic Example 2 (String):
text = "abc"
print(list(reversed(text)))  # Output: ['c', 'b', 'a']

# Basic Example 3 (Range):
print(list(reversed(range(3))))  # Output: [2, 1, 0]

# DSA Example (Reverse Without Mutating):
nums = [1, 2, 3]
print(list(reversed(nums)))  # Output: [3, 2, 1]
print(nums)  # Output: [1, 2, 3] ← original unchanged


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
defaultdict(int)
# What it does: Dictionary with default 0 for missing keys.
# Why use it: Simplifies frequency counting.
# How it works: Returns 0 on missing key access.
# When to use: Counting characters, words, or occurrences.
# Time/Space: O(1) average access, O(n) space for n items.

# Syntax:
from collections import defaultdict
defaultdict(int)  # Default value is 0

# Basic Example 1 (Count Chars):
from collections import defaultdict
d = defaultdict(int)
for c in "hello":
    d[c] += 1
print(d)  # Output: defaultdict(<class 'int'>, {'h': 1, 'e': 1, 'l': 2, 'o': 1})

# Basic Example 2 (Safe Increment):
from collections import defaultdict
d = defaultdict(int)
d["x"] += 5
print(d["x"])  # Output: 5

# Basic Example 3 (Empty Access):
from collections import defaultdict
d = defaultdict(int)
print(d["missing"])  # Output: 0

# DSA Example (Frequency Count):
from collections import defaultdict
counts = defaultdict(int)
for c in "aba":
    counts[c] += 1
print(dict(counts))  # Output: {'a': 2, 'b': 1}


# BUILT-IN FUNCTION: 
defaultdict(list)
# What it does: Dictionary with default empty list for missing keys.
# Why use it: Groups items without initialization.
# How it works: Returns [] on missing key access.
# When to use: Grouping anagrams, building adjacency lists.
# Time/Space: O(1) average access, O(n) space for n items.

# Syntax:
from collections import defaultdict
defaultdict(list)  # Default value is []

# Basic Example 1 (Group by Key):
from collections import defaultdict
d = defaultdict(list)
d["fruits"].append("apple")
d["fruits"].append("banana")
print(d)  # Output: defaultdict(<class 'list'>, {'fruits': ['apple', 'banana']})

# Basic Example 2 (Safe Append):
from collections import defaultdict
d = defaultdict(list)
d["a"].append(1)
print(d["a"])  # Output: [1]

# Basic Example 3 (Empty Access):
from collections import defaultdict
d = defaultdict(list)
print(d["missing"])  # Output: []

# DSA Example (Group Anagrams):
from collections import defaultdict
groups = defaultdict(list)
groups["eat"].append("tea")
groups["eat"].append("ate")
print(dict(groups))  # Output: {'eat': ['tea', 'ate']}


# BUILT-IN FUNCTION: 
Counter()
# What it does: Counts hashable objects and returns a dict-like counter.
# Why use it: Fast frequency counting without manual loops.
# How it works: Subclass of dict; default 0 for missing keys.
# When to use: Anagram checks, top-k elements, mode finding.
# Time/Space: O(n) time (n = elements), O(k) space (k = unique items).

# Syntax:
from collections import Counter
Counter(iterable)  # Returns Counter object from iterable

# Basic Example 1 (Count String):
from collections import Counter
c = Counter("hello")
print(c)  # Output: Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})

# Basic Example 2 (Count List):
from collections import Counter
c = Counter([1, 2, 2, 3])
print(c)  # Output: Counter({2: 2, 1: 1, 3: 1})

# Basic Example 3 (Empty):
from collections import Counter
c = Counter()
print(c["x"])  # Output: 0

# DSA Example (Most Common):
from collections import Counter
votes = ['a', 'b', 'a', 'c', 'a']
c = Counter(votes)
print(c.most_common(1))  # Output: [('a', 3)]


# BUILT-IN FUNCTION: 
deque()
# What it does: Double-ended queue with O(1) append/pop from both ends.
# Why use it: Fast stack, queue, or sliding window operations.
# How it works: Linked list of blocks; O(1) left/right access.
# When to use: BFS, sliding window, monotonic queue, LRU cache.
# Time/Space: O(1) per operation, O(n) space.

# Syntax:
from collections import deque
deque(iterable)  # Creates deque from iterable

# Basic Example 1 (From List):
from collections import deque
d = deque([1, 2, 3])
print(d)  # Output: deque([1, 2, 3])

# Basic Example 2 (Empty):
from collections import deque
d = deque()
print(d)  # Output: deque([])

# Basic Example 3 (String):
from collections import deque
d = deque("abc")
print(d)  # Output: deque(['a', 'b', 'c'])

# DSA Example (Sliding Window):
from collections import deque
window = deque()
for i in range(3):
    window.append(i)
print(window)  # Output: deque([0, 1, 2])
window.popleft()  # Remove oldest
print(window)  # Output: deque([1, 2])


# DEQUE METHOD: .
append()
# What it does: Adds element to right end.
# Why use it: O(1) push to end.
# How it works: Appends to right.
# When to use: Stack push, queue enqueue.

# Syntax:
deque.append(item)

# Example:
d = deque()
d.append(1)
d.append(2)
print(d)  # Output: deque([1, 2])


# DEQUE METHOD: 
.appendleft()
# What it does: Adds element to left end.
# Why use it: O(1) push to front.
# How it works: Inserts at start.
# When to use: Monotonic queue, BFS.

# Syntax:
deque.appendleft(item)

# Example:
d = deque([2])
d.appendleft(1)
print(d)  # Output: deque([1, 2])


# DEQUE METHOD: 
.pop()
# What it does: Removes and returns rightmost element.
# Why use it: O(1) pop from end.
# How it works: Removes from right.
# When to use: Stack pop.

# Syntax:
deque.pop()

# Example:
d = deque([1, 2])
print(d.pop())  # Output: 2
print(d)        # Output: deque([1])


# DEQUE METHOD: 
.popleft()
# What it does: Removes and returns leftmost element.
# Why use it: O(1) pop from front.
# How it works: Removes from left.
# When to use: Queue dequeue, sliding window.

# Syntax:
deque.popleft()

# Example:
d = deque([1, 2])
print(d.popleft())  # Output: 1
print(d)            # Output: deque([2])



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







# ============================================================
# SPECIAL METHODS
# ============================================================

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
