# Static Arrays, Dynamic Arrays, and Strings
# DSA Course in Python Lecture 2
# Video: https://www.youtube.com/watch?v=TQMvBTKn2p0&list=PLKYEe2WisBTFEr6laH5bR2J19j7sl5O8R&index=3

# Overview
# --------
# This guide covers static arrays, dynamic arrays (lists in Python), and strings, focusing on their structure, operations, and Big O complexities.
# Big O notation measures the worst-case growth rate of an algorithm's time or space usage as input size (n) increases.
# Time Complexity: Number of operations relative to input size.
# Space Complexity: Amount of memory used relative to input size.
# We analyze the worst-case scenario, focusing on the dominant complexity term.

# 1. Static Arrays
# ----------------
# Definition: A contiguous block of memory with a fixed size, storing elements of the same type.
# Static arrays do NOT exist in python 
# Characteristics:
# - Fixed size (e.g., 5 elements).
# - Zero-based indexing: indices from 0 to length-1 (e.g., for size 5, indices are 0 to 4).
# - Mutable: Elements can be changed, but size cannot.
# Example: Array A = [1, 2, 3, 4, 5]

# Key Operations and Big O Complexities
# - Access (A[2]): O(1) - Constant time, direct memory access.
# - Modify (A[4] = 7): O(1) - Constant time, updates value at index.
# - Search (5 in A): O(n) - Linear time, may need to scan entire array.
# - Insert (insert 5 at index 2): O(n) - Requires shifting elements, loses last element due to fixed size.
# - Delete (remove element at index 2): O(n) - Requires shifting to maintain contiguous memory.

# Limitations:
# - Fixed size prevents adding new elements without losing data.
# - Insertion/deletion is inefficient due to shifting.

# Code Example: Static Array Operations (Simulated in Python)
# Python uses dynamic arrays (lists), but we simulate static array behavior
A = [1, 2, 3, 4, 5]  # Fixed-size array simulation

# Access: O(1)
def access_element(arr, index):
    return arr[index]  # Example: A[2] returns 3

# Modify: O(1)
def modify_element(arr, index, value):
    arr[index] = value  # Example: A[4] = 7 changes 5 to 7

# Search: O(n)
def search_element(arr, value):
    return value in arr  # Example: 5 in A returns False (if 5 not present)

# Insert: O(n) - Simulated, loses last element
def insert_element(arr, index, value):
    if index < len(arr):
        arr[index:] = arr[index:-1]  # Shift elements, lose last
        arr[index] = value
    return arr  # Example: Insert 5 at index 2 -> [1, 2, 5, 3, 4]

# Delete: O(n) - Simulated, shifts elements
def delete_element(arr, index):
    arr[index:-1] = arr[index+1:]  # Shift elements left
    arr[-1] = None  # Mark last as empty (simulating fixed size)
    return arr  # Example: Delete at index 2 -> [1, 2, 4, 5, None]

# 2. Dynamic Arrays (Lists in Python)
# ----------------------------------
# Definition: An array that can change size, implemented using static arrays under the hood.
# Characteristics:
# - Flexible size, supports appending and resizing.
# - Python lists are dynamic arrays, not static arrays.
# - Underlying static array doubles in size (e.g., 2, 4, 8, 16) when full to accommodate new elements.
# Example: List A = [1, 2, 3] can grow to [1, 2, 3, 4, 5]

# Key Operations and Big O Complexities
# - Access (A[2]): O(1) - Constant time, direct memory access.
# - Modify (A[0] = 7): O(1) - Constant time, updates value at index.
# - Search (6 in A): O(n) - Linear time, scans array.
# - Append (A.append(5)): O(1)***** amortized - Constant time on average, O(n) when resizing.
# - Pop from end (A.pop()): O(1) - Constant time, deallocates last element.
# - Insert (A.insert(2, 5)): O(n) - Shifts elements to make space.
# - Delete (A.pop(2)): O(n) - Shifts elements to fill gap.
# - Length (len(A)): O(1) - Constant time, stored as a property.

# Implementation Details:
# - When appending, if the underlying static array is full, Python creates a new, larger static array (typically doubling size) and copies all elements (O(n)).
# - Doubling minimizes resizing frequency, making append O(1) amortized (on average).
# - Amortized O(1) means most appends are constant, with occasional O(n) resizes.

# Dynamic Array (List) Operations: 
A = [1, 2, 3]  # Create a list (dynamic array)

# Append: O(1) amortized
A.append(5)  # Adds 5 to end -> [1, 2, 3, 5]

# Pop from end: O(1)
A.pop()  # Removes last element -> [1, 2, 3]

# Insert at index: O(n)
A.insert(2, 5)  # Inserts 5 at index 2 -> [1, 2, 5, 3]

# Modify: O(1)
A[0] = 7  # Changes index 0 to 7 -> [7, 2, 5, 3]

# Access: O(1)
value = A[2]  # Gets value at index 2 (5)

# Search: O(n)
is_present = 7 in A  # Returns True (7 in A)

# Search: O(n)
if 7 in A:  # Search for 7 (O(n))
    print("True")  # Output: True

# Length: O(1)
length = len(A)  # Returns 4

# 3. Strings
# -----------
# Definition: A contiguous block of memory storing characters, immutable in Python.
# Characteristics:
# - Immutable: Cannot be modified; operations create new strings.
# - Zero-based indexing, like arrays.
# Example: S = "abc"

# Key Operations and Big O Complexities
# - Access (S[1]): O(1) - Constant time, direct memory access.
# - Search ("e" in S): O(n) - Linear time, scans string.
# - Append (S + "d"): O(n) - Creates new string with all characters.
# - Length (len(S)): O(1) - Constant time, stored as a property.
# - Modify/Insert/Delete: Not allowed directly due to immutability; requires creating new string (O(n)).

# Notes:
# - In languages like C, strings may be mutable, but in Python, they are immutable.
# - Common operations like appending or inserting involve copying the entire string, hence O(n).

# String Operations:
S = "hello"  # Create a string (Immutable)

# Access: O(1)
char = S[2]  # Gets character at index 2 ("l")

# Append: O(n) - Creates new string
B = S + "z"  # Output: "helloz"

# Search: O(n)
is_present = "e" in S  # Returns True

# Search: O(n)
if "e" in S:  # Search for "e" (O(n))
    print("True")  # Output: True

# Length: O(1)
length = len(S)  # Returns 5

# Attempting to modify (not allowed)
S[1] = "d"  # Raises TypeError: 'str' object does not support item assignment


# 4. Complexity Summary (LeetCode Chart)
# -------------------------------------
# Dynamic Arrays (Python Lists: Mutable):
# - Append: O(1) amortized
# - Pop from end: O(1)
# - Insert (not at end): O(n)
# - Delete (not at end): O(n)
# - Modify: O(1)
# - Access: O(1)
# - Search: O(n)
# - Length: O(1)

# Strings (Immutable in Python):
# - Append: O(n)
# - Pop from end: O(n)
# - Insert: O(n)
# - Delete: O(n)
# - Modify: O(n) (requires new string)
# - Access: O(1)
# - Search: O(n)
# - Length: O(1)

# 6. Practical Insights
# ---------------------
# - Static Arrays: Fast for access/modify (O(1)), but limited by fixed size; used in low-level programming.
# - Dynamic Arrays: Flexible for growing/shrinking data; append is efficient (O(1) amortized), but insertions/deletions in the middle are costly (O(n)).
# - Strings: Immutable in Python, making modifications expensive (O(n)); use for text processing where changes are minimal.
# - Python's len() is O(1) for both lists and strings, unlike naive implementations that might count elements.
# - Choose data structures based on operation frequency (e.g., use lists for frequent appends, strings for static text).

# 7. Conclusion
# -------------
# Static arrays, dynamic arrays, and strings are fundamental data structures with distinct properties and complexities.
# Big O notation helps evaluate their efficiency, guiding algorithm design.
# Use this guide to understand their operations, implement them in Python, and optimize code for performance.

# Key Takeaways:
# - Static arrays have fixed size, making insertions/deletions inefficient (O(n)).
# - Dynamic arrays (lists) are flexible, with efficient appends (O(1) amortized) but costly middle operations (O(n)).
# - Strings are immutable in Python, requiring new strings for modifications (O(n)).
# - Access and length operations are O(1) for all three, making them ideal for lookups.
# - Always consider Big O when choosing data structures for specific tasks.

# End of Guide
# ------------
# Run the code examples in a Python environment (e.g., Colab) to experiment and deepen understanding.
# Colab notebook available in the video description: https://www.youtube.com/watch?v=TQMvBTKn2p0