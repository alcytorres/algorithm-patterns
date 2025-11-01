# Prefix Sum
"""
Foundational Skills
   - Array manipulation
   - Understanding cumulative sums
   - Basic loop structures
Potential Knowledge Gaps
   - Inefficient computation of running sums (e.g., recalculating sums repeatedly)
   - Difficulty applying prefix sums to subarray problems
"""

# ----------------------------------------------------------------------------------
# 1. Compute Prefix Sum Array
"""
Task: Given an array, create a new array of its prefix sums. Return an empty array if input is empty

Example 1: [1, 2, 3, 4] → [1, 3, 6, 10]
Example 2: [3, 7, 5]    → [3, 10, 15]

Why: Direct practice for Running Sum of 1d Array.
"""

def prefix_sum(arr):
    # 1️⃣ Handle empty array case
    if not arr:
        return []
    
    # 2️⃣ Initialize result with the first element
    result = [arr[0]]  

    # 3️⃣ Compute prefix sums for remaining elements
    for i in range(1, len(arr)):
        result.append(result[-1] + arr[i])  

    # 4️⃣ Return the prefix sum array
    return result

print(prefix_sum([1, 2, 3, 4]))  # Output: [1, 3, 6, 10]  → [1, 1+2, 1+2+3 + 1+2+3+4]
print(prefix_sum([3, 7, 5]))     # Output: [3, 7, 10]  → [3, 3+7, 3+7+5]
print(prefix_sum([]))            # Output: []  


# Simple Breakdown
def prefix_sum(arr):   # Define the function that takes an array 'arr' as input
    """
    Computes the prefix sum array where each element is the sum of all prior elements.
    
    - Builds array iteratively, adding each element to the previous sum.
    - Time Complexity: O(n), Space Complexity: O(n) for the result.
    - Simple iteration is beginner-friendly and efficient.
    """
    if not arr:         # Check if the array is empty: "If arr is not true or If arr is empty."
        return []       # Return an empty array if input is empty
    
    result = [arr[0]]   # Start the result with the first element of 'arr'
    for i in range(1, len(arr)):  # Loop from the second element to the end
        result.append(result[-1] + arr[i])  # Add current element to previous sum

    return result       # Return the prefix sum array


# print(prefix_sum([1, 2, 3, 4]))  # Output: [1, 3, 6, 10]  → [1, 1+2, 1+2+3 + 1+2+3+4]


"""
# Key Lesson: Understanding `if not arr` in Python

# Purpose: `if not arr` checks if `arr` is "falsy" (e.g., empty or equivalent to False).
# How `if not` Works: In Python, `if not` inverts the boolean value of the expression.
#   - If `arr` is "truthy" (e.g., non-empty list), `not arr` is False, so the block is skipped.
#   - If `arr` is "falsy" (e.g., []), `not arr` is True, so the block executes.
# Returns: `[]` for any falsy value, like [], {}, '', set(), 0, 0.0, None, False.
# Syntax: `if not arr:` evaluates `arr` in a boolean context.
# Example: In `prefix_sum`, `if not arr: return []` handles empty input.

# Takeaway: Use `if not arr` for concise, readable checks of empty or falsy values.


# ----------------------------------------------------------------------------------
# Key Lesson: Understanding Boolean Context and `if not` in Python

# Boolean Context: When Python evaluates a value in an `if` statement, it treats it as either True or False.
#   - "Truthy" values (e.g., non-empty list [1, 2]) are treated as True.
#   - "Falsy" values (e.g., empty list [], 0, None) are treated as False.

# How `if not` Works: The `not` keyword flips the boolean value.
#   - If `arr` is truthy (e.g., [1, 2]), `not arr` becomes False, so the `if` block is skipped.
#   - If `arr` is falsy (e.g., []), `not arr` becomes True, so the `if` block runs.

# Example:
#   arr = [1, 2]  # Truthy, so `not arr` is False → skip `if not arr` block.
#   arr = []      # Falsy, so `not arr` is True → enter `if not arr` block.

# Takeaway: Boolean context decides if a value acts as True/False in `if` statements; `not` inverts it.
"""

# ----------------------------------------------------------------------------------
# Solution with output Full Breakdown 

def prefix_sum(arr):              # Example: arr = [1, 2, 3, 4]

    # 1️⃣ Handle empty array case
    # Check if the input array is empty
    # Why? An empty array should return an empty array as per the task
    if not arr:                   # arr = [1, 2, 3, 4], not empty → False
        return []                 # Skip (not applicable for this example)
    # After check: Proceed since arr is non-empty

    # 2️⃣ Initialize result with the first element
    # Create result array starting with the first element of arr
    # Why? The first prefix sum is just arr[0], as there's no prior sum
    result = [arr[0]]             # arr[0] = 1, result = [1]
    # After initialization: result = [1], representing sum of arr[0]

    # 3️⃣ Compute prefix sums for remaining elements
    # Iterate through arr starting from index 1
    # Why? For each index i, we add arr[i] to the previous prefix sum
    for i in range(1, len(arr)):  # len(arr) = 4, range(1, 4) → i = 1, 2, 3
        
        # --- Iteration 1: i = 1 ---
        # Add current element to the last prefix sum
        # Why? Each prefix sum is the sum of all elements up to index i
        result.append(result[-1] + arr[i])  # result[-1] = 1, arr[1] = 2
                                            # 1 + 2 = 3, append 3
                                            # result = [1, 3]
        # After Iteration 1: i = 1, result = [1, 3]
        # Current prefix sum: 1 + 2 = 3 (sum of arr[0:2])

        # --- Iteration 2: i = 2 ---
        if i == 2:                          # Check for clarity
            result.append(result[-1] + arr[i])  # result[-1] = 3, arr[2] = 3
                                                # 3 + 3 = 6, append 6
                                                # result = [1, 3, 6]
        # After Iteration 2: i = 2, result = [1, 3, 6]
        # Current prefix sum: 1 + 2 + 3 = 6 (sum of arr[0:3])

        # --- Iteration 3: i = 3 ---
        if i == 3:                          # Check for clarity
            result.append(result[-1] + arr[i])  # result[-1] = 6, arr[3] = 4
                                                # 6 + 4 = 10, append 10
                                                # result = [1, 3, 6, 10]
        # After Iteration 3: i = 3, result = [1, 3, 6, 10]
        # Current prefix sum: 1 + 2 + 3 + 4 = 10 (sum of arr[0:4])

    # 4️⃣ Return the prefix sum array
    # Why? The result contains all prefix sums for the input array
    return result                       # Return result = [1, 3, 6, 10]
    # Final state: result = [1, 3, 6, 10]
    # Conclusion: Successfully computed prefix sums for arr = [1, 2, 3, 4]

print(prefix_sum([1, 2, 3, 4]))  # Output: [1, 3, 6, 10] → [1, 1+2, 1+2+3, 1+2+3+4]



# ----------------------------------------------------------------------------------
# Solution with output 

def prefix_sum(arr):              # Example: arr = [3, 7, 5]

    # 1️⃣ Handle empty array case
    if not arr:                   # arr = [3, 7, 5], not empty → False
        return []                 # Skip 
    # After check: Proceed since arr is non-empty

    # 2️⃣ Initialize result with the first element
    # Create result array starting with the first element of arr
    result = [arr[0]]             # arr[0] = 3, result = [3]
    # After initialization: result = [3], representing sum of arr[0]

    # 3️⃣ Compute prefix sums for remaining elements
    # Iterate through arr starting from index 1
    for i in range(1, len(arr)):  # len(arr) = 3, range(1, 3) → i = 1, 2
        
        # --- Iteration 1: i = 1 ---
        # Add current element to the last prefix sum
        result.append(result[-1] + arr[i])  # result[-1] = 3, arr[1] = 7
                                            # 3 + 7 = 10, append 10
                                            # result = [3, 10]
        # After Iteration 1: i = 1, result = [3, 10]
        # Current prefix sum: 3 + 7 = 10 (sum of arr[0:2])

        # --- Iteration 2: i = 2 ---
        if i == 2:                          # Check for clarity
            result.append(result[-1] + arr[i])  # result[-1] = 10, arr[2] = 5
                                                # 10 + 5 = 15, append 15
                                                # result = [3, 10, 15]
        # After Iteration 2: i = 2, result = [3, 10, 15]
        # Current prefix sum: 3 + 7 + 5 = 15 (sum of arr[0:3])

    # 4️⃣ Return the prefix sum array
    return result                       # Return result = [3, 10, 15]
    # Final state: result = [3, 10, 15]

print(prefix_sum([3, 7, 5]))  # Output: [3, 10, 15] → [3, 3+7, 3+7+5]
