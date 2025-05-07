# 2. Check if Array is Sorted
"""
# Task: Determine if an array is sorted in ascending order. If not return false.
# Example: [1, 2, 3, 4] → True,  [1, 3, 2] → False
# Why: Practices moving pointers to compare adjacent elements.
"""

def is_sorted(arr):
    # 1️⃣ Handle base cases: empty or single-element arrays are always sorted
    if len(arr) < 2:
        return True
    
    # 2️⃣ Initialize pointers for comparing adjacent elements
    i, j = 0, 1

    # 3️⃣ Loop through the array to compare adjacent elements
    while j < len(arr):
        if arr[i] > arr[j]:
            return False
        i += 1
        j += 1

    # 4️⃣ Return result
    return True

print(is_sorted([1, 2, 3, 4]))  # Output: True
print(is_sorted([1, 3, 2]))     # Output: False


# Simple Beakdown
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

def is_sorted(arr):              # Example: arr = [1, 2, 3, 4]
    # 1️⃣ Handle base cases: empty or single-element arrays are always sorted
    if len(arr) < 2:             # len(arr) = 4 < 2 → False
        return True              # Skip
    
    # 2️⃣ Initialize pointers for comparing adjacent elements
    i, j = 0, 1                  # i = 0, j = 1
    # After initialization: i points to arr[0] = 1, j points to arr[1] = 2

    # 3️⃣ Loop through the array to compare adjacent elements
    while j < len(arr):          # len(arr) = 4, j = 1 < 4 → True (loop starts)
        
        # --- Iteration 1: i = 0, j = 1 ---
        # Check if the current element is greater than the next
        if arr[i] > arr[j]:      # arr[0] = 1, arr[1] = 2, 1 > 2 → False
            return False         # Skip (no violation found)
        # Move pointers to the next pair
        i += 1                   # i = 0 + 1 = 1
        j += 1                   # j = 1 + 1 = 2
        # After Iteration 1: i = 1 (points to arr[1] = 2), j = 2 (points to arr[2] = 3)
        # Current pair checked: (1, 2), 1 ≤ 2 (valid)

        # --- Iteration 2: i = 1, j = 2 ---
        if j < len(arr):         # j = 2 < 4 → True
            if arr[i] > arr[j]:  # arr[1] = 2, arr[2] = 3, 2 > 3 → False
                return False     # Skip (no violation found)
            i += 1               # i = 1 + 1 = 2
            j += 1               # j = 2 + 1 = 3
            # After Iteration 2: i = 2 (points to arr[2] = 3), j = 3 (points to arr[3] = 4)
            # Current pair checked: (2, 3), 2 ≤ 3 (valid)

        # --- Iteration 3: i = 2, j = 3 ---
        if j < len(arr):         # j = 3 < 4 → True
            if arr[i] > arr[j]:  # arr[2] = 3, arr[3] = 4, 3 > 4 → False
                return False     # Skip (no violation found)
            i += 1               # i = 2 + 1 = 3
            j += 1               # j = 3 + 1 = 4
            # After Iteration 3: i = 3 (points to arr[3] = 4), j = 4
            # Current pair checked: (3, 4), 3 ≤ 4 (valid)

        # --- Iteration 4: i = 3, j = 4 ---
        if j < len(arr):         # j = 4 < 4 → False (loop ends)
            pass                 # No further iterations (included for completeness)

    # 4️⃣ Return result
    return True              # Return True (array is sorted)

print(is_sorted([1, 2, 3, 4]))  # Output: True (1 ≤ 2, 2 ≤ 3, 3 ≤ 4)


# Solution with output Full Breakdown 
def is_sorted(arr):              # Example: arr = [1, 2, 3, 4]

    # 1️⃣ Handle base cases: empty or single-element arrays are always sorted
    # Check if the array has fewer than 2 elements
    # Why? Arrays with 0 or 1 elements are inherently sorted
    if len(arr) < 2:             # len(arr) = 4 < 2 → False
        return True              # Skip (not applicable for this example)
    
    # 2️⃣ Initialize pointers for comparing adjacent elements
    # Set i to the first index and j to the second index
    # Why? We'll compare arr[i] with arr[j] to check if each pair is in order
    i, j = 0, 1                  # i = 0, j = 1
    # After initialization: i points to arr[0] = 1, j points to arr[1] = 2

    # 3️⃣ Loop through the array to compare adjacent elements
    # Continue while j is within the array bounds
    # Why? We need to check all adjacent pairs until we reach the end
    while j < len(arr):          # len(arr) = 4, j = 1 < 4 → True (loop starts)
        
        # --- Iteration 1: i = 0, j = 1 ---
        # Check if the current element is greater than the next
        # Why? If arr[i] > arr[j], the array is not sorted
        if arr[i] > arr[j]:      # arr[0] = 1, arr[1] = 2, 1 > 2 → False
            return False         # Skip (no violation found)
        
        # Move pointers to the next pair
        # Why? We advance to compare the next adjacent elements
        i += 1                   # i = 0 + 1 = 1
        j += 1                   # j = 1 + 1 = 2
        # After Iteration 1: i = 1 (points to arr[1] = 2), j = 2 (points to arr[2] = 3)
        # Current pair checked: (1, 2), 1 ≤ 2 (valid)

        # --- Iteration 2: i = 1, j = 2 ---
        if j < len(arr):         # j = 2 < 4 → True
            if arr[i] > arr[j]:  # arr[1] = 2, arr[2] = 3, 2 > 3 → False
                return False     # Skip (no violation found)
            i += 1               # i = 1 + 1 = 2
            j += 1               # j = 2 + 1 = 3
            # After Iteration 2: i = 2 (points to arr[2] = 3), j = 3 (points to arr[3] = 4)
            # Current pair checked: (2, 3), 2 ≤ 3 (valid)

        # --- Iteration 3: i = 2, j = 3 ---
        if j < len(arr):         # j = 3 < 4 → True
            if arr[i] > arr[j]:  # arr[2] = 3, arr[3] = 4, 3 > 4 → False
                return False     # Skip (no violation found)
            i += 1               # i = 2 + 1 = 3
            j += 1               # j = 3 + 1 = 4
            # After Iteration 3: i = 3 (points to arr[3] = 4), j = 4
            # Current pair checked: (3, 4), 3 ≤ 4 (valid)

        # --- Iteration 4: i = 3, j = 4 ---
        if j < len(arr):         # j = 4 < 4 → False (loop ends)
            pass                 # No further iterations (included for completeness)

    # 4️⃣ Return result
    # If we exit the loop, all adjacent pairs are in order
    # Why? No violations (arr[i] > arr[j]) were found
    return True              # Return True (array is sorted)
    # Final state: All pairs checked: (1, 2), (2, 3), (3, 4) are valid
    # Conclusion: Array [1, 2, 3, 4] is sorted

print(is_sorted([1, 2, 3, 4]))  # Output: True (1 ≤ 2, 2 ≤ 3, 3 ≤ 4)


# ----------------------------------------------------------------------------------
# Solution with output 

def is_sorted(arr):              # Example: arr = [1, 3, 2]
    # 1️⃣ Handle base cases: empty or single-element arrays are always sorted
    if len(arr) < 2:             # len(arr) = 3 < 2 → False
        return True              # Skip
    
    # 2️⃣ Initialize pointers for comparing adjacent elements
    i, j = 0, 1                  # i = 0, j = 1
    # After initialization: i points to arr[0] = 1, j points to arr[1] = 3

    # 3️⃣ Loop through the array to compare adjacent elements
    while j < len(arr):          # len(arr) = 3, j = 1 < 3 → True (loop starts)
        
        # --- Iteration 1: i = 0, j = 1 ---
        # Check if the current element is greater than the next
        if arr[i] > arr[j]:      # arr[0] = 1, arr[1] = 3, 1 > 3 → False
            return False         # Skip (no violation found)
        # Move pointers to the next pair
        i += 1                   # i = 0 + 1 = 1
        j += 1                   # j = 1 + 1 = 2
        # After Iteration 1: i = 1 (points to arr[1] = 3), j = 2 (points to arr[2] = 2)
        # Current pair checked: (1, 3), 1 ≤ 3 (valid)

        # --- Iteration 2: i = 1, j = 2 ---
        if j < len(arr):         # j = 2 < 3 → True
            if arr[i] > arr[j]:  # arr[1] = 3, arr[2] = 2, 3 > 2 → True
                return False     # Return False (3 > 2 breaks ascending order)
            i += 1               # Skip (function already returned)
            j += 1               # Skip (function already returned)
            # After Iteration 2: Execution stops due to violation
            # Current pair checked: (3, 2), 3 > 2 (invalid)

    # 4️⃣ Return result
    return True              # Skip (function returned False in Iteration 2)

print(is_sorted([1, 3, 2]))     # Output: False (3 > 2 breaks ascending order)



"""
Explanation of what happens when 3 > 2: 
Since 3 > 2 is True, we hit return False.
What happens now? We break out of the loop completely and stop the function. return False sends False back and ends everything—no going back to the top, no more looping, no checking other numbers.
"""
# ----------------------------------------------------------------------------------
