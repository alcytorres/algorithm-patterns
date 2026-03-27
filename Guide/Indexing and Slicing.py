# Indexing and Slicing

"""
INDEXING and SLICING in Python GUIDE

--- What Are Indexing and Slicing in Python? ---
   - Indexing: Access a single element in a sequence (string, list, or tuple) by position.

   - Slicing: Extract a portion of a sequence by specifying a range of positions.

Python sequences are ordered, and each element has an index (position) starting from 0.

You can also use negative indices to count from the end, where -1 is the last element.

Note on other types:
   - Dictionaries use d[key] — that's key lookup, NOT positional indexing. No slicing.
   - Sets have NO [ ] access at all — they're unordered and not sequences.
   - Tuples support indexing and slicing exactly like lists (but are immutable).
"""

"""
--- 1. INDEXING ---
   - Indexing lets you grab one item from a sequence using square brackets [ ] and the position number.

Syntax: sequence[index]

Key Points:
   - Positive indices: Start at 0 (first item).
   - Negative indices: Start at -1 (last item) and go backward.
   - If you try an index outside the sequence's range, you'll get an IndexError.
"""

# Examples with a String
text = "Python"

# Positive indexing
print(text[0])  # Output: P (first character)
print(text[2])  # Output: t (third character)
print(text[5])  # Output: n (sixth character)

# Negative indexing
print(text[-1]) # Output: n (last character)
print(text[-2]) # Output: o (second-to-last)
print(text[-6]) # Output: P (first character)

# Examples with a List
numbers = [10, 20, 30, 40, 50]

print(numbers[1])  # Output: 20 (second item)
print(numbers[-1]) # Output: 50 (last item)
print(numbers[-3]) # Output: 30 (third-to-last)


"""
--- 2. SLICING ---
   - Slicing lets you extract a range of elements from a sequence.
   - You specify a start, stop, and optionally a step.

Syntax: sequence[start:stop:step]
   - start: The index where the slice begins (inclusive).
            Defaults to 0 if step is positive, or the last index if step is negative.

   - stop: The index where the slice ends (exclusive — this index is NOT included).
           Defaults to the end if step is positive, or before the first element if step is negative.

   - step: The direction and size of each jump. Defaults to 1 if omitted.
           +1 → move forward one position at a time (default).
           +2 → move forward two positions (every other element).
           -1 → move backward one position at a time (reverses).
           -2 → move backward two positions (reverse, every other element).

           Think of it as: "from the current element, move this many positions
           to pick the next element."

   *** When step is NEGATIVE, the defaults FLIP:
       - start defaults to the LAST element (not 0)
       - stop defaults to BEFORE the first element (so index 0 is still included)
       This is why [::-1] reverses — it starts at the end and walks backward
       through every element until it passes the beginning.

Key Points:
   - The stop index is NEVER included in the result.
   - Omitting start means "from the beginning" (or "from the end" if step < 0).
   - Omitting stop means "to the end" (or "to the beginning" if step < 0).
   - Negative indices work here too (e.g., -1 means the last element).

How to read ANY slice — ask these 3 questions:
   1. WHERE do I start?  (start index, or default based on step sign)
   2. WHERE do I stop?   (stop index, exclusive — never included)
   3. WHICH DIRECTION and how far do I jump?  (step sign = direction, step value = jump size)

Walk-through:  nums =    [1, 2, 3, 4, 5]
               indices:   0  1  2  3  4
               negative: -5 -4 -3 -2 -1

   nums[1:4]     → start=1, stop=4, step=+1 (default)
                    index 1→2, index 2→3, index 3→4. Stop at 4 (not included).
                    Result: [2, 3, 4]

   nums[::2]     → start=0 (default), stop=end (default), step=+2
                    index 0→1, index 2→3, index 4→5. Done.
                    Result: [1, 3, 5]

   nums[::-1]    → step is -1, so defaults FLIP:
                    start=last (index 4), stop=before first
                    index 4→5, index 3→4, index 2→3, index 1→2, index 0→1. Done.
                    Result: [5, 4, 3, 2, 1]

   nums[3:0:-1]  → start=3, stop=0 (exclusive!), step=-1
                    index 3→4, index 2→3, index 1→2. Stop at 0 (not included).
                    Result: [4, 3, 2]
"""

# Basic Slicing Examples
text = "Python"

# Slice from index 0 to 3 (stop is exclusive)
print(text[0:3])  # Output: Pyt

# Slice from index 1 to 4
print(text[1:4])  # Output: yth

# From start to index 2
print(text[:3])   # Output: Pyt

# From index 2 to end
print(text[2:])   # Output: thon

# Using Negative Indices
text = "Python"

# From second-to-last to end
print(text[-2:])   # Output: on

# From start up to (not including) second-to-last
print(text[:-2])   # Output: Pyth

# From third-to-last up to (not including) last
print(text[-3:-1]) # Output: ho


# Using Step
# The step controls direction and jump size.
# - Step  1: move forward, take every element (default).
# - Step  2: move forward, take every 2nd element.
# - Step -1: move backward through every element (reverses).

text = "Python"

# Every second character
print(text[0:6:2])  # Output: Pto
print(text[::2])    # Output: Pto

# Reverse the string
print(text[::-1])   # Output: nohtyP

# Every second character from index 1 to end
print(text[1::2])   # Output: yhn


# List Slicing Examples
numbers = [10, 20, 30, 40, 50, 60]

# Slice from index 1 to 4
print(numbers[1:4])   # Output: [20, 30, 40]

# Every second item
print(numbers[::2])   # Output: [10, 30, 50]

# Reverse the list
print(numbers[::-1])  # Output: [60, 50, 40, 30, 20, 10]

# From index -2 down to (not including) index 0
print(numbers[-2:0:-1])  # Output: [50, 40, 30, 20]


# --- 3. Common Use Cases ---
# Copying a Sequence
# Use [:] to make a shallow copy of a list or string:
numbers = [1, 2, 3]
copy = numbers[:]
print(copy)  # Output: [1, 2, 3]

# Reversing
# Use [::-1] to reverse any sequence:
text = "Hello"
print(text[::-1])  # Output: olleH

# Extracting Specific Parts
sentence = "I love Python programming"
print(sentence[7:13])  # Output: Python

# --- 4. Edge Cases ---
# Out-of-Range Indices
# - Indexing: Raises an IndexError.
text = "Python"
# print(text[10])  # IndexError: string index out of range

# - Slicing: Returns an empty sequence if the range is invalid, no error.
print(text[10:15])  # Output: "" (empty string)

# Empty Slices
text = "Python"
print(text[3:3])  # Output: "" (start equals stop)

# Step of Zero
# A step of 0 is invalid:
# print(text[::0])  # ValueError: slice step cannot be zero

# --- 5. Practice Problems ---
# Try these to test your understanding:
# 1. Given data = "abcdefgh", extract "cde".
# 2. Reverse the list [1, 2, 3, 4, 5].
# 3. From numbers = [0, 10, 20, 30, 40, 50], get [20, 40].
# 4. Extract every third character from "Pythonista".

# Answers
data = "abcdefgh"
print(data[2:5])  # 1. Output: "cde"

print([1, 2, 3, 4, 5][::-1])  # 2. Output: [5, 4, 3, 2, 1]

numbers = [0, 10, 20, 30, 40, 50]
print(numbers[2:5:2])  # 3. Output: [20, 40]

print("Pythonista"[::3])  # 4. Output: "Phia"


# --- Summary Table ---
# | Operation   | Syntax  | Example ("Python") | Result |
# |-------------|---------|--------------------| -------|
# | Single item | [3]     | text[3]            | h      |
# | Basic slice | [1:4]   | text[1:4]          | yth    |
# | Omit start  | [:3]    | text[:3]           | Pyt    |
# | Omit stop   | [2:]    | text[2:]           | thon   |
# | With step   | [::2]   | text[::2]          | Pto    |
# | Reverse     | [::-1]  | text[::-1]         | nohtyP |


"""
Core facts:
   • Stop index is NEVER included
   • Omitting start → from beginning (from end if step < 0)
   • Omitting stop  → to the end (to the beginning if step < 0)

   • Negative indices count from the end (-1 = last item)
   • Step sign controls direction (+ forward, - backward)
   • Step value controls jump size (1=every element, 2=every other, etc.)

How to read ANY slice:
   1. Where do I START?
   2. Where do I STOP? (never included)
   3. Which DIRECTION and how far do I JUMP?

Most common mistakes to avoid:
   • Thinking stop is included
   • Not realizing defaults flip when step is negative
   • Forgetting that slicing creates a new list (not a view)
"""
