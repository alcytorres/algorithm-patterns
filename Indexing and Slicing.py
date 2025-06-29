# Index and Slicing

"""
Here's a clear, simple, and thorough guide to indexing and slicing in Python,
designed to be easy to follow with plenty of examples.

--- What Are Indexing and Slicing in Python? ---
   - Indexing: A way to access a single element in a sequence (like a string, list, or tuple) using its position.
   - Slicing: A way to extract a portion (or "slice") of a sequence by specifying a range of positions.

# Python sequences are ordered, and each element has an index (position) starting from 0 for the first element.
# You can also use negative indices to count from the end, where -1 is the last element.
"""

"""
--- 1. Indexing ---
   - Indexing lets you grab one item from a sequence using square brackets [ ] and the position number.

# Syntax: sequence[index]

# Key Points:
   - Positive indices: Start at 0 (first item).
   - Negative indices: Start at -1 (last item) and go backward.
   - If you try an index outside the sequence’s range, you’ll get an IndexError.
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
--- 2. Slicing ---
   - Slicing lets you extract a range of elements from a sequence.
   - You specify a start, stop, and optionally a step.

# Syntax: sequence[start:stop:step]
   - start: The index where the slice begins (inclusive). Defaults to 0 if omitted.
   - stop: The index where the slice ends (exclusive). Defaults to the end if omitted.
   - step: How many positions to skip between elements. Defaults to 1 if omitted.

# Key Points:
   - The stop index is not included in the result.
   - Omitting start means "from the beginning."
   - Omitting stop means "to the end."
   - Negative indices work here too!
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

# From second-to-last to last
print(text[-2:])   # Output: on

# From start to second-to-last  ??? Exclusive
print(text[:-2])   # Output: Pyth

# From third-to-last to second-to-last
print(text[-3:-1]) # Output: ho

# Using Step
# The step value controls how you move through the sequence.
# - Step 1: Take every element (default).
# - Step 2: Take every second element.
# - Step -1: Reverse the sequence.

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

# From second-to-last to start
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
print(text[10])  # Uncommenting this would raise: IndexError: string index out of range

# - Slicing: Returns an empty sequence if the range is invalid, no error.
print(text[10:15])  # Output: "" (empty string)

# Empty Slices
text = "Python"
print(text[3:3])  # Output: "" (start equals stop)

# Step of Zero
# A step of 0 is invalid:
print(text[::0])  # Uncommenting this would raise: ValueError: slice step cannot be zero

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


# --- Summary Table (as comments) ---
| Operation         | Syntax           | Example ("Python") | Result   |
|-------------------|------------------|--------------------|----------|
| Single item       | [3]              | text[3]            | h        |
| Basic slice       | [1:4]            | text[1:4]          | yth      |
| Omit start        | [:3]             | text[:3]           | Pyt      |
| omit stop         | [2:]             | text[2:]           | thon     |
| With step         | [::2]            | text[::2]          | Pto      |
| Reverse           | [::-1]           | text[::-1]         | nohtyP   |

"""
That’s it! You now have a solid grasp of indexing and slicing in Python.
Practice with different sequences (strings, lists, tuples) to get comfortable."
"""
