# Two Pointers
"""
Foundational Skills
   - Array indexing and manipulation
   - Loop control (e.g., for, while)
   - Conditional statements within loops
   - Basic arithmetic operations
Potential Knowledge Gaps
   - Difficulty managing multiple pointers (e.g., moving them independently or in sync)
   - Trouble visualizing pointer movements (e.g., from opposite ends or same direction)
   - Handling edge cases (e.g., empty arrays, single elements)
"""

# ----------------------------------------------------------------------------------
# 1. Sum of First and Last Elements
"""
# Task: Given an array, return the sum of its first and last elements. If the input is not an array return 0.

# Example: [1, 2, 3] → 4 (1 + 3)

# Why: Introduces using two pointers at opposite ends.
"""

def sum_first_last(arr):

    # 1️⃣ Check if the array is empty
    if not arr:
        return 0
    
    # 2️⃣ Get the first and last elements
    first = arr[0]
    last = arr[-1]

    # 3️⃣ Compute and return the sum
    return first + last

print(sum_first_last([1, 2, 3]))  # Output: 4 (1 + 3)

print(sum_first_last([5]))        # Output: 10 (5 + 5)
print(sum_first_last([]))         # Output: 0 (0 + 0)
print(sum_first_last([1, 2]))     # Output: 3 (1 + 2)


# Simple Breakdown
def sum_first_last(arr):   # Define the function that takes an array 'arr' as input
    """
    Returns the sum of the first and last elements of the array.
    
    - Uses two pointers to access the start and end directly.
    - Time Complexity: O(1), Space Complexity: O(1).
    - Simple and beginner-friendly as it introduces pointer concepts without iteration.
    """
    
    # 1️⃣ Check if the array is empty
    if not arr:         # Check if the array is empty (no elements)
        return 0        # Return 0 if empty, since there's nothing to sum
    
    # 2️⃣ Get the first and last elements
    first = arr[0]      # Set 'first' to the first element (index 0, start of array)
    last = arr[-1]      # Set 'last' to the last element (index -1, end of array in Python)
    
    # 3️⃣ Compute and return the sum
    return first + last   # Add the first and last elements and return the result

print(sum_first_last([1, 2, 3]))  # Output: 4 (1 + 3)

"""
Explanation: if not arr:
    - if not arr: asks: "Is the array empty?"  →  Same as if len(arr) == 0
    - If yes (like []), it returns 0 and stops.
    - If no (like [1, 2, 3]), it skips to sum the first and last elements.
    - It is there to avoid errors and handle the empty case safely.
"""

# ----------------------------------------------------------------------------------
# Solution with output 

# Task: Given an array, return the sum of its first and last elements. If the input is empty, return 0.
# Example: arr = [1, 2, 3] → Output = 4 (1 + 3)
# Why: Introduces using two pointers at opposite ends (first and last elements).

def sum_first_last(arr):  # Example: arr = [1, 2, 3]

    # 1️⃣ Check if the array is empty
    # If the array is empty, return 0
    # Why? An empty array has no first or last element, so the sum is defined as 0
    if not arr:           # arr = [1, 2, 3], not empty, so skip
        return 0          # skip

    # 2️⃣ Get the first and last elements
    # Access the first element at index 0
    # Why? We need the first element for the sum
    first = arr[0]        # arr[0] = 1, so first = 1

    # Access the last element at index -1
    # Why? We need the last element for the sum
    last = arr[-1]        # arr[-1] = arr[2] = 3, so last = 3

    # 3️⃣ Compute and return the sum
    # Add the first and last elements
    # Why? The task requires the sum of these two elements
    return first + last   # first = 1, last = 3, so 1 + 3 = 4


print(sum_first_last([1, 2, 3]))  # Output: 4 (1 + 3)

