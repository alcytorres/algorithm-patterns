# 2. Check if Array is Sorted
"""
# Task: Determine if an array is sorted in ascending order.
# Example: [1, 2, 3, 4] → True, [1, 3, 2] → False
# Why: Practices moving pointers to compare adjacent elements.
"""

def is_sorted(arr):
    if len(arr) < 2:
        return True
    i, j = 0, 1
    while j < len(arr):
        if arr[i] > arr[j]:
            return False
        i += 1
        j += 1
    return True

# print(is_sorted([1, 2, 3, 4]))  # Output: True
# print(is_sorted([1, 3, 2]))     # Output: False


# Solution
def is_sorted(arr):   # Define the function that takes an array 'arr' as input
    """
    Determines if the array is sorted in ascending order.
    
    - Uses two pointers to compare adjacent elements iteratively.
    - Time Complexity: O(n), Space Complexity: O(1).
    - Iterative approach chosen for simplicity over recursive alternatives.
    """

    if len(arr) < 2:      # Check if array has 0 or 1 element (nothing to compare)
        return True       # Return True since empty or single-element arrays are sorted
    i, j = 0, 1           # Set 'i' to 0 (current element) and 'j' to 1 (next element)
    while j < len(arr):   # Loop until 'j' reaches the end of the array
        if arr[i] > arr[j]:  # Compare: if current element is greater than next, not sorted
            return False     # Return False since order is broken
        i += 1            # Move 'i' forward to the next element
        j += 1            # Move 'j' forward to the element after that
    return True           # If loop finishes, all elements are in order, so return True

# Test the function
# print(is_sorted([1, 2, 3, 4]))  # Output: True
# print(is_sorted([1, 3, 2]))     # Output: False
