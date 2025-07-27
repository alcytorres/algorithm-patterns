# Hashing Cheat Sheet (Python Focus)
# Key Points for DSA: Hash Maps (Dicts) and Sets

# === Hashing Basics ===
# Hash Function: Converts any immutable input (key) to an integer index via hashing.
# - Deterministic: Same key always hashes to same value.
# - Used with arrays for O(1) access.
# - Don't need to implement; Python handles it.

# === Hash Maps (Dictionaries in Python) ===
# Unordered key-value pairs. Keys must be immutable (e.g., int, str, tuple).
# Operations: O(1) average case for insert, delete, lookup, update.
# Pros: Fast lookups, no need for fixed size like arrays.
# Cons: More overhead than arrays for small sizes; space waste possible.

# Hash Map = Dictionary: Declaration
hash_map = {}  # Empty dict
hash_map = {'a': 1, 'b': 2}  # Initialized

# Check if key exists
print('a' in hash_map)  # True
print('h' in hash_map)  # False

# Access value
print(hash_map['a'])  # 1 (KeyError if missing)

# Add/Update
hash_map['c'] = 3  # Add if new, update if exists
print(hash_map) # {'a': 1, 'b': 2, 'c': 3}

# Delete
del hash_map['c']  # KeyError if missing
print(hash_map) # {'a': 1, 'b': 2}

# Size 
print(len(hash_map))  # 2 

# Print the Entire Hash Map
print(hash_map) # {'a': 1, 'b': 2}


# Iterate
for key in hash_map:  # Keys
    print(key)  # a b
for val in hash_map.values():  # Values
    print(val)  # 1 2
for key, val in hash_map.items():  # Pairs
    print(key, val)  # a 1 b 2

# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Get keys as list
keys = list(hash_map.keys())
print(keys) # ['a', 'b']

# Get keys: use .keys(). You can iterate over this using a for loop.
keys = hash_map.keys()
for key in keys:
    print(key) # a b

# Get values as list
values = list(hash_map.values()) 
print(values) # [1, 2]

# Get values: use .values(). You can iterate over this using a for loop.
values = hash_map.values()
for val in values:
    print(val) # 1 2


# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Iterate over key-value pairs
for key, val in hash_map.items():
    print(f"{key}: {val}") # a: 1, b: 2


# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Iterate over keys with index
print_map = hash_map
for i, val in enumerate(hash_map):
    print(i, val)
# 0 a
# 1 b



# === Sets in Python ===
# Unordered unique elements. Like dict keys only. O(1) add, remove, check.
# No duplicates; doesn't track frequency.

# Declaration
my_set = set()  # Empty
my_set = {1, 2, 3}  # Initialized

# Add
my_set.add(4)  # Ignores if exists

# Check exists
print(4 in my_set)  # True

# Remove
my_set.remove(4)  # KeyError if missing
# or my_set.discard(4)  # No error if missing

# Size
print(len(my_set))

# Iterate
for elem in my_set:
    print(elem)

# === Arrays as Keys ===
# Convert mutable list to immutable tuple or string.
key = tuple([1, 2, 3])  # For dict/set
hash_map[key] = 'value'
# Or string: "1,2,3" (use delimiter not in elements)

# === Comparison with Arrays (Lists in Python) ===
# Lists: O(1) access by index, but O(n) for search/delete.
# Dicts/Sets: O(1) for search/delete, but keys hashed (slower constant for small n).
# Use dict when mapping keys to values; set for existence; list for order/index.

# Must-Know: Master dict/set interfaces. Reduces time complexity in many problems.
# In LeetCode: Use for counting, unique checks, mappings.



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Key Difference: items() vs enumerate() for Dicts

# items(): Use for dicts to iterate over key-value pairs.
# - Returns both key and value directly.
# - Use when you need to access keys AND values.

hash_map = {'a': 1, 'b': 2}
for key, value in hash_map.items():
    print(key, value)  # Outputs: a 1, b 2

# enumerate(): Use for iterables (e.g., lists, dict keys) to get index and item.
# - Returns index and item, not key-value pairs.
# - Use when you need the position (index) of items.

for index, key in enumerate(hash_map):
    print(index, key)  # Outputs: 0 a, 1 b

# When to use:
# - items(): Need key-value pairs from dict.
# - enumerate(): Need index with items (e.g., dict keys or list elements).



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# === Key Hash Map Concepts ===
# Hash Maps (Dictionaries): Store key-value pairs. Unordered, mutable.
# Keys: Must be immutable (hashable) e.g., int, str, tuple. Can't use lists (mutable).
# Values: Any type, mutable or immutable.
# Use case: Fast O(1) lookups, mappings in LeetCode (e.g., counting frequencies).

# BUILT-IN FUNCTION: 
dict()
# What it does: Creates a dictionary from key-value pairs or iterables.
# DSA use case: Initialize mappings for tracking (e.g., char counts in strings).
# Why it’s useful: Flexible creation; handles dynamic data in algorithms.
# Time/Space: O(n) time/space (n = number of pairs).
# Syntax:
dict()  # Empty dict
dict(key1=value1, key2=value2)  # From kwargs
dict([('a', 1), ('b', 2)])  # From iterable of pairs
# DSA Example 1 (Empty Dict):
d = dict()
d['key'] = 'value'  # {'key': 'value'}
# DSA Example 2 (From List of Pairs):
pairs = [('x', 10), ('y', 20)]
d = dict(pairs)  # {'x': 10, 'y': 20}

# METHOD: 
.items()
# What it does: Returns view of key-value pairs as tuples.
# DSA use case: Iterate over mappings (e.g., sum values, find max).
# Why it’s useful: Access both keys and values efficiently.
# Time/Space: O(n) time to iterate, O(1) space for view.
# Syntax:
d.items()  # Returns dict_items object
# DSA Example 1 (Iteration):
d = {'a': 1, 'b': 2}
for k, v in d.items():
    print(k, v)  # a 1 \n b 2
# DSA Example 2 (List Conversion):
pairs = list(d.items())  # [('a', 1), ('b', 2)]

# METHOD: 
.get()
# What it does: Returns value for key if exists, else default (None if omitted).
# DSA use case: Safe access without KeyError (e.g., default counters).
# Why it’s useful: Avoids errors in lookups; common in frequency maps.
# Time/Space: O(1) time.
# Syntax:
d.get(key, default=None)
# DSA Example 1 (Existing Key):
d = {'a': 1}
print(d.get('a'))  # 1
# DSA Example 2 (Missing Key with Default):
print(d.get('b', 0))  # 0

# METHOD: 
.keys()
# What it does: Returns view of all keys.
# DSA use case: Check or iterate keys (e.g., unique elements).
# Why it’s useful: Focus on keys for existence checks.
# Time/Space: O(n) time to iterate, O(1) space for view.
# Syntax:
d.keys()  # Returns dict_keys object
# DSA Example:
d = {'a': 1, 'b': 2}
for k in d.keys():
    print(k)  # a b

# METHOD: 
.values()
# What it does: Returns view of all values.
# DSA use case: Aggregate values (e.g., sum, max).
# Why it’s useful: Process values without keys.
# Time/Space: O(n) time to iterate, O(1) space for view.
# Syntax:
d.values()  # Returns dict_values object
# DSA Example:
d = {'a': 1, 'b': 2}
print(sum(d.values()))  # 3

# METHOD: 
.pop()
# What it does: Removes key and returns its value; default if missing.
# DSA use case: Remove and use item (e.g., process queue-like).
# Why it’s useful: Combines delete and get.
# Time/Space: O(1) time.
# Syntax:
d.pop(key, default=None)
# DSA Example 1:
d = {'a': 1}
print(d.pop('a'))  # 1, d now {}
# DSA Example 2 (Missing):
print(d.pop('b', 0))  # 0, d unchanged

# METHOD: 
.clear()
# What it does: Removes all items.
# DSA use case: Reset mapping between operations.
# Why it’s useful: Quick empty without new object.
# Time/Space: O(1) time (amortized).
# Syntax:
d.clear()
# DSA Example:
d = {'a': 1}
d.clear()  # d now {}

# === Comparison with Other DS ===
# Lists: Mutable, ordered, index access. O(n) search. Use for sequences.
# Tuples: Immutable, ordered. Hashable as keys. Use for fixed data.
# Sets: Mutable, unordered, unique keys. O(1) existence. Like dict without values.
# Dicts vs Others: Dicts for key-value; sets for uniqueness; lists/tuples for order. Keys immutable in dicts/sets.