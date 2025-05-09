# 2. Range Sum Query  → Reference problem 1. Compute Prefix Sum Array 

# ----------------------------------------------------------------------------------
# *** Reference: 1. Compute Prefix Sum Array ***
"""
Task: Given an array, create a new array of its prefix sums.
Example: [1, 2, 3, 4] → [1, 3, 6, 10]
"""
def prefix_sum(arr):
    if not arr:
        return []
    result = [arr[0]]  
    for i in range(1, len(arr)):
        result.append(result[-1] + arr[i])  
    return result

print(prefix_sum([1, 2, 3, 4]))  # Output: [1, 3, 6, 10]  →  [1, 1+2, 1+2+3, 1+2+3+4]
# ----------------------------------------------------------------------------------

# 2. Range Sum Query 
"""
Task: Find the sum of elements between two indices (inclusive) using prefix sums.
Example 1: [1, 2, 3, 4], indices 1 to 3 → 9 (2 + 3 + 5)
Example 2: [1, 2, 3, 4], indices 0 to 2 → 6 (1 + 2 + 3)
Why: Teaches efficient range sum calculation.
"""
def range_sum(prefix, start, end):

    # 1️⃣ Handle case where range starts at index 0
    if start == 0:
        return prefix[end]  
    
    # 2️⃣ Compute range sum for non-zero start index
    return prefix[end] - prefix[start - 1]  # Difference gives range sum

prefix = prefix_sum([1, 2, 3, 4])
print(range_sum(prefix, 1, 3))  # Output: 9 
print(range_sum(prefix, 0, 2))  # Output: 6 
print(range_sum(prefix, 2, 2))  # Output: 3 


# Simple Breakdown
def range_sum(prefix, start, end):   # Define the function that takes a prefix sum array and two indices
    """
    Computes the sum of elements between start and end indices using prefix sums.
    
    - Uses subtraction of prefix sums for efficiency.
    - Time Complexity: O(1) per query, Space Complexity: O(1).
    - Direct calculation is simple and showcases prefix sum utility.
    """
    if start == 0:      # If starting from the beginning
        return prefix[end]  # Directly return the prefix sum at 'end'
    return prefix[end] - prefix[start - 1]  # Subtract prefix sum before 'start' from prefix sum at 'end'

# Test the function
prefix = prefix_sum([1, 2, 3, 4])
print(range_sum(prefix, 1, 3))  # Output: 9 (2+3+4 = 9)


"""
Explanation for range_sum(prefix, 2, 2): 
The line return prefix[end] - prefix[start - 1] works because it isolates the sum of numbers from index start to end in the original array.
    - prefix[end] is the total of all numbers up to end (e.g., for end = 2, prefix[2] = 1 + 2 + 3 = 6).
    - prefix[start - 1] is the total up to just before start (e.g., start = 2, start - 1 = 1, prefix[1] = 1 + 2 = 3).
    - Subtracting them (6 - 3 = 3) gives only the numbers from start to end (just 3 here).
It is like taking a big pile of coins up to end and removing the coins before start to get what is in between.

*** Pro Tip: Actually use coins to test this problem to visually understand it ***


# ----------------------------------------------------------------------------------
# Key Lesson: Omitting `else` When `if` Returns

# Why: In `range_sum`, `else` is omitted because:
#   - `if start == 0:` returns `prefix[end]` and exits.
#   - Code after `if` only runs if the condition is false, making `else` redundant.

# Example:
#   if start == 0:          # If true, return and exit
#       return prefix[end]
#   return prefix[end] - prefix[start - 1]  # Runs if start != 0

# Takeaway: Skip `else` if `if` returns, as the function exits early.
"""


# ----------------------------------------------------------------------------------
# Solution with output Full Breakdown 

def range_sum(prefix, start, end):  # Example: prefix = [1, 3, 6, 10], start = 1, end = 3

    # 1️⃣ Handle case where range starts at index 0
    # Check if start index is 0
    # Why? If start is 0, the sum is simply the prefix sum at end index
    if start == 0:                  # start = 1, 1 == 0 → False
        return prefix[end]          # Skip (not applicable since start != 0)
    # After check: Proceed to compute range sum since start is not 0

    # 2️⃣ Compute range sum for non-zero start index
    # Calculate the difference between prefix sums
    # Why? The sum from start to end is prefix[end] - prefix[start - 1]
    return prefix[end] - prefix[start - 1]  # prefix[end] = prefix[3] = 10
                                            # prefix[start - 1] = prefix[1 - 1] = prefix[0] = 1
                                            # 10 - 1 = 9
                                            # Return 9 (sum of arr[1:4] = 2 + 3 + 4)
    # After computation: Function returns 9

    # 3️⃣ Return result
    # Why? The returned value is the sum of elements from start to end (inclusive)
    # Final state: Returned 9 (sum of arr[1:4] = 2 + 3 + 4)
    # Conclusion: Successfully computed range sum for indices 1 to 3

# Example setup
prefix = prefix_sum([1, 2, 3, 4])  # prefix = [1, 3, 6, 10]
print(range_sum(prefix, 1, 3))     # Output: 9


"""
"3️⃣ Return result" Simple Explanation:
    - I added "3️⃣ Return result" to match the detailed, structured style we have used for prior example, which summarizes outcomes in numbered sections. 
    
    -Although there's no explicit return result line, this section recaps the function's output (9) and its meaning (sum from indices 1 to 3) for clarity.
"""

# ----------------------------------------------------------------------------------
# Solution with output Full Breakdown 

def range_sum(prefix, start, end):  # Example: prefix = [1, 3, 6, 10], start = 0, end = 2

    # 1️⃣ Handle case where range starts at index 0
    # Check if start index is 0
    # Why? If start is 0, the sum is simply the prefix sum at end index
    if start == 0:                  # start = 0, 0 == 0 → True
        return prefix[end]          # prefix[2] = 6
                                    # Return 6 (sum of arr[0:3] = 1 + 2 + 3)
    # After check: Since start == 0, return prefix[end] immediately
    # Current state: Function returns 6, no further computation needed

    # 2️⃣ Compute range sum for non-zero start index
    # Calculate the difference between prefix sums
    # Why? The sum from start to end is prefix[end] - prefix[start - 1]
    return prefix[end] - prefix[start - 1]  # Skip (not executed due to start == 0)
    # Note: For non-zero start, this computes sum by subtracting the prefix sum
    # up to start - 1 from the prefix sum up to end

    # 3️⃣ Return result
    # Why? The returned value is the sum of elements from start to end (inclusive)
    # Final state: Returned 6 (sum of arr[0:3] = 1 + 2 + 3)
    # Conclusion: Successfully computed range sum for indices 0 to 2

# Example setup
prefix = prefix_sum([1, 2, 3, 4])  # prefix = [1, 3, 6, 10]
print(range_sum(prefix, 0, 2))     # Output: 6




# ----------------------------------------------------------------------------------
# Solution with output 
def range_sum(prefix, start, end):
    if start == 0:  # False (start = 1)
        return prefix[end]  # skip
    return prefix[end] - prefix[start - 1]  # prefix[3] - prefix[1] = 10 - 1 = 9

prefix = prefix_sum([1, 2, 3, 4])  # → [1, 3, 6, 10]
print(range_sum(prefix, 1, 3))  # Output: 9

# ----------------------------------------------------------------------------------
# Solution with output 
def range_sum(prefix, start, end):
    if start == 0:  # False (start = 2)
        return prefix[end]  # skip
    return prefix[end] - prefix[start - 1]  # prefix[3] - prefix[1] = 10 - 3 = 7

prefix = prefix_sum([1, 2, 3, 4])  # → [1, 3, 6]
print(range_sum(prefix, 2, 3))  # Output: 7

# ----------------------------------------------------------------------------------
# Solution with output 
def range_sum(prefix, start, end):  # range_sum([1, 3, 6], 0, 1)
    if start == 0:  # True (start = 0)
        return prefix[end]  # prefix[1] = 3
    return prefix[end] - prefix[start - 1]  # skip

prefix = prefix_sum([1, 2, 3])  # → [1, 3, 6]
print(range_sum(prefix, 0, 1))  # Output: 3  

# ----------------------------------------------------------------------------------
# Solution with output 
def range_sum(prefix, start, end):  # range_sum([1, 3, 6], 1, 2)
    if start == 0:  # False (start = 1)
        return prefix[end]  # skip
    return prefix[end] - prefix[start - 1]  # prefix[2] - prefix[0] = 6 - 1 = 5

prefix = prefix_sum([1, 2, 3])  # → [1, 3, 6]
print(range_sum(prefix, 1, 2))  # Output: 5 

# ----------------------------------------------------------------------------------
# Solution with output 
def range_sum(prefix, start, end):
    if start == 0:  # False (start = 2)
        return prefix[end]  # skip
    return prefix[end] - prefix[start - 1]  # prefix[2] - prefix[1] = 6 - 3 = 3

prefix = prefix_sum([1, 2, 3])  # → [1, 3, 6]
print(range_sum(prefix, 2, 2))  # Output: 3
