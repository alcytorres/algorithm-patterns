# 2. Check if Array is Sorted
"""
# Task: Determine if an array is sorted in ascending order. If not return false.
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

print(is_sorted([1, 2, 3, 4]))  # Output: True
print(is_sorted([1, 3, 2]))     # Output: False


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
print(is_sorted([1, 2, 3, 4]))  # Output: True
print(is_sorted([1, 3, 2]))     # Output: False


# ----------------------------------------------------------------------------------
# Solution with output 

def is_sorted(arr):              # arr = [1, 2, 3, 4]
    if len(arr) < 2:             # 4 < 2 → False
        return True              # skip
    i, j = 0, 1                  # i = 0, j = 1
    while j < len(arr):          # j < 4 → True (loop runs)
        if arr[i] > arr[j]:      # Iteration 1: arr[0] > arr[1] → 1 > 2 → False
            return False         # skip
        i += 1                   # i = 1
        j += 1                   # j = 2
                                 # Iteration 2: j < 4 → True
                                 # arr[1] > arr[2] → 2 > 3 → False
                                 # i = 2, j = 3
                                 # Iteration 3: j < 4 → True
                                 # arr[2] > arr[3] → 3 > 4 → False
                                 # i = 3, j = 4
                                 # Iteration 4: j < 4 → False (loop ends)
    return True                  # Return True (all pairs in order)

print(is_sorted([1, 2, 3, 4]))  # Output: True (1≤2, 2≤3, 3≤4)


# ----------------------------------------------------------------------------------
# Solution with output 

def is_sorted(arr):              # arr = [1, 3, 2]
    if len(arr) < 2:             # 3 < 2 → False
        return True              # skip
    i, j = 0, 1                  # i = 0, j = 1
    while j < len(arr):          # j < 3 → True (loop runs)
        if arr[i] > arr[j]:      # Iteration 1: arr[0] > arr[1] → 1 > 3 → False
            return False         # skip
        i += 1                   # i = 1
        j += 1                   # j = 2
                                 # Iteration 2: j < 3 → True
                                 # arr[1] > arr[2] → 3 > 2 → True
                                 # Return False (triggered when 3 > 2)
                                 # Loop stops here → Break out completely
    return True                  # Not reached

print(is_sorted([1, 3, 2]))   # Output: False (3 > 2 breaks ascending order)


"""
Explanation of what happens when 3 > 2: 
Since 3 > 2 is True, we hit return False.
What happens now? We break out of the loop completely and stop the function. return False sends False back and ends everything—no going back to the top, no more looping, no checking other numbers.
"""
# ----------------------------------------------------------------------------------
