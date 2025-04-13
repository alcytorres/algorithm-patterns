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
Task: Given an array, create a new array of its prefix sums.
Example: [1, 2, 3] → [1, 3, 6]
Why: Direct practice for Running Sum of 1d Array.
"""

def prefix_sum(arr):
    if not arr:
        return []
    result = [arr[0]]  # First element is the same
    for i in range(1, len(arr)):
        result.append(result[-1] + arr[i])  # Add current element to previous sum
    return result

# Test the function
print(prefix_sum([1, 2, 3]))  # Output: [1, 3, 6]  →  [1, 1+2, 1+2+3]


# Solution
def prefix_sum(arr):   # Define the function that takes an array 'arr' as input
    """
    Computes the prefix sum array where each element is the sum of all prior elements.
    
    - Builds array iteratively, adding each element to the previous sum.
    - Time Complexity: O(n), Space Complexity: O(n) for the result.
    - Simple iteration is beginner-friendly and efficient.
    """
    if not arr:         # Check if the array is empty
        return []       # Return an empty array if input is empty
    result = [arr[0]]   # Start the result with the first element of 'arr'
    for i in range(1, len(arr)):  # Loop from the second element to the end
        result.append(result[-1] + arr[i])  # Add the previous sum to the current element
    return result       # Return the prefix sum array

# Test the function
print(prefix_sum([1, 2, 3]))  # Output: [1, 3, 6]  →  [1, 1+2, 1+2+3]


# ----------------------------------------------------------------------------------
# Solution with output 

def prefix_sum(arr):  
    if not arr:    # false, arr = [1, 2, 3] 
        return []  # skip
    result = [arr[0]]  # result = [1]
    for i in range(1, len(arr)):  # range(1, 3): i = 1 | i = 2 
        result.append(result[-1] + arr[i])  # [1, 3] | [1, 3, 6]  
    return result  # [1, 3, 6] 


print(prefix_sum([1, 2, 3]))  # Output: [1, 3, 6]  →  [1, 1+2, 1+2+3]
