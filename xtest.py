#  STRING METHODS
# LIST METHODS
# DICTIONARY METHODS
# SET METHODS
# BUILT-IN FUNCTIONS
# SPECIAL METHODS



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


# STRING METHOD: 
.join()
# What it does: Joins iterable elements into string with separator.
# Why use it: Builds strings from lists efficiently.
# How it works: Iterable must contain strings; concatenates with separator.
# When to use: Constructing outputs from token lists.
# Time/Space: O(n) time (n = total length), O(n) space for string.


# STRING METHOD: 
.lower()
# What it does: Converts all characters in a string to lowercase.
# Why use it: Normalizes text for case-insensitive searches.
# How it works: Returns a new string; original unchanged.
# When to use: Standardizing input in string pattern problems.
# Time/Space: O(n) time (n = string length), O(n) space for new string.


# STRING METHOD: 
.upper()
# What it does: Converts all characters in a string to uppercase.
# Why use it: Standardizes text for comparisons or display.
# How it works: Returns a new string; original unchanged.
# When to use: Case-insensitive matching in palindromes or anagrams.
# Time/Space: O(n) time (n = string length), O(n) space for new string.


# STRING METHOD: 
.replace()
# What it does: Replaces occurrences of a substring with another.
# Why use it: Modifies specific parts of strings efficiently.
# How it works: Returns a new string; optional count parameter.
# When to use: Cleaning or transforming strings in text processing.
# Time/Space: O(n) time (n = string length), O(n) space for new string.


# STRING METHOD: 
.isdigit()
# What it does: Checks if all characters are digits.
# Why use it: Validates numeric strings quickly.
# How it works: Returns True/False; checks ASCII digits 0-9.
# When to use: Parsing inputs in numeric validation problems.
# Time/Space: O(n) time (n = string length), O(1) space.


# STRING METHOD: 
.isnumeric()
# What it does: Checks if all characters are numeric.
# Why use it: Validates broader numeric strings including Unicode.
# How it works: Returns True/False; more inclusive than .isdigit().
# When to use: Robust numeric checks in international inputs.
# Time/Space: O(n) time (n = string length), O(1) space.


# STRING METHOD: 
.format()
# What it does: Formats string with placeholders.
# Why use it: Builds dynamic strings easily.
# How it works: Replaces {} with args or named values.
# When to use: Formatting outputs in debugging or results.
# Time/Space: O(n) time (n = string length), O(n) space for string.






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


# LIST METHOD: 
.pop()
# What it does: Removes and returns element at index (default last).
# Why use it: Removes while retrieving value.
# How it works: Shifts if not last; modifies in place.
# When to use: Implementing stacks or queues.
# Time/Space: O(1) for last, O(n) otherwise, O(1) space.


# LIST METHOD: 
.sort()
# What it does: Sorts list in place.
# Why use it: Prepares data efficiently.
# How it works: Modifies original; stable sort.
# When to use: In-place for two-pointer.
# Time/Space: O(n log n) time, O(1) space.



# LIST METHOD: 
.extend()
# What it does: Adds multiple elements from iterable to list end.
# Why use it: Combines lists efficiently.
# How it works: Modifies in place; iterates over iterable.
# When to use: Merging arrays or collecting batches.
# Time/Space: O(k) time (k = iterable length), O(k) space.


# LIST METHOD: 
.remove()
# What it does: Removes first occurrence of value.
# Why use it: Deletes by value, not index.
# How it works: Searches linearly; raises ValueError if not found.
# When to use: Removing duplicates or invalid items.
# Time/Space: O(n) time (search), O(1) space.


# LIST METHOD: 
.insert()
# What it does: Inserts element at specified index.
# Why use it: Adds at specific positions.
# How it works: Shifts elements right; modifies in place.
# When to use: Maintaining sorted order in arrays.
# Time/Space: O(n) time (shifting), O(1) space per call.



# ============================================================
# DICTIONARY METHODS
# ============================================================

# DICTIONARY METHOD: 
.keys()
# What it does: Returns view of dictionary keys.
# Why use it: Accesses keys for iteration.
# How it works: Dynamic view; changes with dict.
# When to use: Looping over keys in hash maps.
# Time/Space: O(1) for view, O(n) for list conversion.


# DICTIONARY METHOD: 
.values()
# What it does: Returns a view of all values in a dictionary.
# Why use it: Accesses values for iteration or aggregation.
# How it works: Dynamic view; updates with dict changes.
# When to use: Summing values or checking ranges in hash maps.
# Time/Space: O(1) time for view, O(n) for list conversion (n = values).


# DICTIONARY METHOD: 
.items()
# What it does: Returns view of key-value pairs as tuples.
# Why use it: Iterates over keys and values together.
# How it works: Dynamic view; changes with dict.
# When to use: Processing pairs in grouping problems.
# Time/Space: O(1) for view, O(n) for list conversion.


# DICTIONARY METHOD: 
.get()
# What it does: Gets value for key, default if missing.
# Why use it: Safe access without KeyError.
# How it works: O(1) lookup; optional default.
# When to use: Frequency counts in hash maps.
# Time/Space: O(1) average time, O(1) space.





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


# SET METHOD: 
.remove()
# What it does: Removes a specific element from the set.
# Why use it: Deletes a known element quickly.
# How it works: O(1) average lookup and removal; raises KeyError if not present.
# When to use: Removing seen elements, invalid items, or deduplication cleanup.
# Time/Space: O(1) average time, O(1) space.


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


# BUILT-IN FUNCTION: 
range()
# What it does: Generates number sequence.
# Why use it: Efficient looping without list.
# How it works: Lazy; stores start/stop/step.
# When to use: Iteration in arrays or matrices.
# Time/Space: O(1) time, O(1) space.


# BUILT-IN FUNCTION: 
print()
# What regenerative: Outputs objects to console with formatting.
# Why use it: Debugs code and displays results.
# How it works: Converts args to strings; customizable sep/end.
# When to use: Testing outputs during DSA problem solving.
# Time/Space: O(n) time (n = output length), O(1) space.


# BUILT-IN FUNCTION: 
sum()
# What it does: Sums iterable items.
# Why use it: Aggregates numbers easily.
# How it works: Adds elements; start optional.
# When to use: Subarray or cumulative sums.
# Time/Space: O(n) time, O(1) space.


# BUILT-IN FUNCTION: 
enumerate()
# What it does: Pairs indices with iterable elements.
# Why use it: Tracks position in loops.
# How it works: Returns iterator of (index, value).
# When to use: Index-based array operations.
# Time/Space: O(1) create, O(1) per iteration.


# BUILT-IN FUNCTION: 
str()
# What it does: Converts object to string representation.
# Why use it: Enables string ops on non-strings.
# How it works: Calls __str__ if defined.
# When to use: Formatting outputs or concatenation.
# Time/Space: O(n) time, O(n) space for string.


# BUILT-IN FUNCTION: 
int()
# What it does: Converts value to integer.
# Why use it: Parses strings for arithmetic.
# How it works: Truncates floats; bases optional.
# When to use: Numeric parsing in inputs.
# Time/Space: O(n) time for strings, O(1) space.


# BUILT-IN FUNCTION: 
float()
# What it does: Converts value to floating-point number.
# Why use it: Handles decimals in calculations.
# How it works: Parses strings or ints to float.
# When to use: Precision in numeric problems.
# Time/Space: O(n) time for strings, O(1) space.


# BUILT-IN FUNCTION: 
list()
# What it does: Creates list from iterable.
# Why use it: Converts to mutable list.
# How it works: Copies elements into new list.
# When to use: Manipulating converted data.
# Time/Space: O(n) time, O(n) space.


# BUILT-IN FUNCTION: 
tuple()
# What it does: Creates tuple from iterable.
# Why use it: Immutable sequences for keys.
# How it works: Copies to immutable tuple.
# When to use: Fixed data in hash maps.
# Time/Space: O(n) time, O(n) space.


# BUILT-IN FUNCTION: 
dict()
# What it does: Creates dict from pairs or kwargs.
# Why use it: Builds hash maps quickly.
# How it works: From iterable of pairs or args.
# When to use: Caching or counting in DSA.
# Time/Space: O(n) time, O(n) space.


# BUILT-IN FUNCTION: 
defaultdict(int)
# What it does: Dictionary with default 0 for missing keys.
# Why use it: Simplifies frequency counting.
# How it works: Returns 0 on missing key access.
# When to use: Counting characters, words, or occurrences.
# Time/Space: O(1) average access, O(n) space for n items.


# BUILT-IN FUNCTION: 
defaultdict(list)
# What it does: Dictionary with default empty list for missing keys.
# Why use it: Groups items without initialization.
# How it works: Returns [] on missing key access.
# When to use: Grouping anagrams, building adjacency lists.
# Time/Space: O(1) average access, O(n) space for n items.


# BUILT-IN FUNCTION: 
Counter()
# What it does: Counts hashable objects and returns a dict-like counter.
# Why use it: Fast frequency counting without manual loops.
# How it works: Subclass of dict; default 0 for missing keys.
# When to use: Anagram checks, top-k elements, mode finding.
# Time/Space: O(n) time (n = elements), O(k) space (k = unique items).


# BUILT-IN FUNCTION: 
iter()
# What it does: Creates iterator from iterable.
# Why use it: Manual control over iteration.
# How it works: Calls __iter__; pairs with next().
# When to use: Custom traversal in processing.
# Time/Space: O(1) time, O(1) space.


# BUILT-IN FUNCTION: 
zip()
# What it does: Pairs elements from iterables.
# Why use it: Simultaneous iteration.
# How it works: Stops at shortest iterable.
# When to use: Merging or comparing arrays.
# Time/Space: O(1) create, O(1) per iteration.


# BUILT-IN FUNCTION: 
next()
# What it does: Gets next from iterator.
# Why use it: Step-by-step iteration control.
# How it works: Calls __next__; default for exhausted.
# When to use: Custom generator processing.
# Time/Space: O(1) per call, O(1) space.


# BUILT-IN FUNCTION: 
set()
# What it does: Creates set from iterable, unique elements.
# Why use it: Fast deduplication and membership.
# How it works: Hashes elements; unordered.
# When to use: Removing duplicates in arrays.
# Time/Space: O(n) time, O(n) space.


# BUILT-IN FUNCTION: 
sorted()
# What it does: Returns sorted list from iterable.
# Why use it: Sorts without modifying original.
# How it works: Stable sort; optional key/reverse.
# When to use: Preparing for binary search.
# Time/Space: O(n log n) time, O(n) space.


# BUILT-IN FUNCTION: 
max()
# What it does: Returns largest item.
# Why use it: Finds max quickly.
# How it works: Iterates once; optional key.
# When to use: Max in arrays or profits.
# Time/Space: O(n) time, O(1) space.


# BUILT-IN FUNCTION: 
input()
# What it does: Reads user input as string.
# Why use it: Gets interactive data.
# How it works: Optional prompt; strips newline.
# When to use: Testing or user-driven algorithms.
# Time/Space: O(n) time, O(n) space for string.


# BUILT-IN FUNCTION: 
isinstance()
# What it does: Checks if object is instance of type.
# Why use it: Flexible type validation.
# How it works: Includes subclasses; tuple for multiple.
# When to use: Input checks in polymorphic code.
# Time/Space: O(1) time, O(1) space.


# BUILT-IN FUNCTION: 
type()
# What it does: Returns object's type.
# Why use it: Identifies data types.
# How it works: Returns class; compares with ==.
# When to use: Debugging or type-specific logic.
# Time/Space: O(1) time, O(1) space.




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


# SPECIAL METHOD:
 __str__()
# What it does: Defines string representation.
# Why use it: Readable print/str of objects.
# How it works: Called by str() or print().
# When to use: Debugging custom structures.
# Time/Space: O(n) time, O(n) space for string.

