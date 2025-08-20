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

# ––––––––––––––––––––––––––––––––––––––––––––––
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


# ––––––––––––––––––––––––––––––––––––––––––––––
# Iterate over key-value pairs
for key, val in hash_map.items():
    print(f"{key}: {val}") # a: 1, b: 2


# ––––––––––––––––––––––––––––––––––––––––––––––
# Iterate over keys with index
print_map = hash_map
for i, val in enumerate(hash_map):
    print(i, val)
# 0 a
# 1 b


# ––––––––––––––––––––––––––––––––––––––––––––––
# Key Difference: items() vs enumerate() for Dictionaries

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



# ––––––––––––––––––––––––––––––––––––––––––––––
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


# Example: Arrays vs Hash Maps for unknown key ranges
# Array approach (problem: unknown key range)
max_key = 100  # Guess max key size
arr = [0] * max_key  # Risk: too small or wastes space
arr[5] = 10  # Works if key (5) fits
# arr[1000] = 20  # Error if key exceeds max_key

# Hash map approach (simpler, no size worry)
hash_map = {}  # No need to predefine size
hash_map[5] = 10  # Any key works
hash_map[1000] = 20  # No issue with large keys
print(hash_map)  # Output: {5: 10, 1000: 20}


# Must-Know: Master dict/set interfaces. Reduces time complexity in many problems.
# In LeetCode: Use for counting, unique checks, mappings.



# ––––––––––––––––––––––––––––––––––––––––––––––
# === Additional Key Hash Map Concepts ===
# Key-Value Pairs: Store mappings; keys unique, values can duplicate.
# Mutability: Dicts are mutable (can change after creation).
# Immutable Keys: Required for hashing; mutable types (lists, dicts, sets) can't be keys as they change hash.
# Examples: Valid keys: int (42), str ('key'), tuple ((1,2)); Invalid: list [1,2] (use tuple instead).

# === Most Important Dictionary Methods (Ranked for Interviews) ===
# 1. get(key, default=None): Safe access; returns value or default if missing.
# 2. pop(key, default=None): Remove and return value; default if missing.
# 3. popitem(): Remove and return arbitrary pair (LIFO in Python 3.7+).
# 4. clear(): Empty the dict.
# 5. update(other_dict): Merge another dict or pairs.
# 6. setdefault(key, default=None): Get value; insert default if missing.
# 7. copy(): Shallow copy of dict.
# 8. fromkeys(keys, value=None): Create dict from iterable keys.

# === Comparison with Other Data Structures ===
# Lists: Mutable, ordered, index access; use for sequences, not mappings. Can't be keys.
# Tuples: Immutable, ordered; use as dict keys for composite immutable data.
# Sets: Mutable, unordered uniques; like dicts without values. Use for membership tests; elements must be immutable.
# Key Use Cases: Dicts for key-value lookups; sets for uniques; lists/tuples for ordered data (tuples as keys when needed).