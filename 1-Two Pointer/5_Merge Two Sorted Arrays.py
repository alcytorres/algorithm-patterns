# 5. Merge Two Sorted Arrays
"""
Task: Merge two sorted arrays into one sorted array.

Example 1: [1, 3], [2, 4, 6] → [1, 2, 3, 4, 6]
Example 2: [1, 3], [2, 4] → [1, 2, 3, 4]

Why: Reinforces pointer use in sorted data, akin to Remove Duplicates From Sorted Array.
"""

def merge_sorted_arrays(arr1, arr2):
    # 1️⃣ Initialize result array and pointers
    result = []        
    i, j = 0, 0     

    # 2️⃣ Merge arrays while both pointers are within bounds     
    while i < len(arr1) and j < len(arr2): 
        if arr1[i] < arr2[j]:  
            result.append(arr1[i]) 
            i += 1        
        else:              
            result.append(arr2[j])  
            j += 1         

    # 3️⃣ Append remaining elements from arr1, if any
    result.extend(arr1[i:])  
    # 4️⃣ Append remaining elements from arr2, if any
    result.extend(arr2[j:])  

    # 5️⃣ Return the merged sorted array
    return result       

print(merge_sorted_arrays([1, 3], [2, 4, 6]))  # Output: [1, 2, 3, 4, 6]
print(merge_sorted_arrays([1, 3], [2, 4]))  # Output: [1, 2, 3, 4]


# Simple Breakdown
def merge_sorted_arrays(arr1, arr2):   # Define the function that takes two arrays 'arr1' and 'arr2' as inputs
    """
    Merges two sorted arrays into one sorted array.
    
    - Uses two pointers to compare and build result iteratively.
    - Time Complexity: O(n + m), Space Complexity: O(n + m) for result.
    - Iterative merging is straightforward and beginner-friendly.
    """

    # 1️⃣ Initialize result array and pointers
    result = []           # Create empty list to store the merged sorted array
    i, j = 0, 0           # Set 'i' as pointer for arr1, 'j' as pointer for arr2, both start at 0
    
    # 2️⃣ Merge arrays while both pointers are within bounds     
    while i < len(arr1) and j < len(arr2):  # Loop while both arrays have elements to compare
        if arr1[i] < arr2[j]:  # Compare elements at pointers: if arr1's is smaller
            result.append(arr1[i])  # Add arr1's element to result
            i += 1          # Move arr1's pointer forward
        else:               # If arr2's element is smaller or equal
            result.append(arr2[j])  # Add arr2's element to result
            j += 1          # Move arr2's pointer forward
    
    # 3️⃣ Append remaining elements from arr1, if any
    result.extend(arr1[i:])  # Add any remaining elements from arr1 (from i to end)
    # 4️⃣ Append remaining elements from arr2, if any
    result.extend(arr2[j:])  # Add any remaining elements from arr2 (from j to end)
    
    # 5️⃣ Return the merged sorted array
    return result         # Return the fully merged and sorted array


# print(merge_sorted_arrays([1, 3], [2, 4]))  # Output: [1, 2, 3, 4]
# print(merge_sorted_arrays([1, 3], [2, 4, 6]))  # Output: [1, 2, 3, 4, 6]

"""
Explanation: Why Only One Array Has Leftovers for the last couple of line?
    - Context: Look at result.extend(arr1[i:]) and result.extend(arr2[j:])
    - The while i < len(arr1) and j < len(arr2) loop stops when one array is used up (i = len(arr1) or j = len(arr2)).
    - After the loop:
        - arr1[i:] is empty if arr1 is done, or has leftovers if not.
        - arr2[j:] is empty if arr2 is done, or has leftovers if not.
    - Never both: The loop runs until at least one array is empty, so only the longer array (if any) has numbers left for result.extend().
"""


# ----------------------------------------------------------------------------------
# Solution with output Full Breakdown 

def merge_sorted_arrays(arr1, arr2):  # Example: arr1 = [1, 3], arr2 = [2, 4, 6]

    # 1️⃣ Initialize result array and pointers
    # Create an empty list to store the merged sorted array
    # Why? We'll build the result by comparing elements from both arrays
    result = []                      # result = []
    
    # Set pointers for arr1 and arr2
    # Why? Pointers i and j track our position in arr1 and arr2, respectively
    i, j = 0, 0                      # i = 0 (points to arr1[0] = 1), j = 0 (points to arr2[0] = 2)
    # After initialization: i tracks arr1, j tracks arr2, result is empty

    # 2️⃣ Merge arrays while both pointers are within bounds
    # Continue while both arrays have elements to compare
    # Why? We compare elements from arr1 and arr2, adding the smaller one to result
    while i < len(arr1) and j < len(arr2):  # len(arr1) = 2, len(arr2) = 3, i = 0, j = 0
                                            # i < 2 and j < 3 → True (loop starts)
        
        # --- Iteration 1: i = 0, j = 0 ---
        # Compare elements at pointers i and j
        # Why? We need to determine which element is smaller to maintain sorted order
        if arr1[i] < arr2[j]:               # arr1[0] = 1, arr2[0] = 2, 1 < 2 → True
            result.append(arr1[i])          # Append arr1[0] = 1 to result
                                            # result = [1]
            i += 1                          # i = 0 + 1 = 1
            # After if: i = 1 (points to arr1[1] = 3), j = 0 (points to arr2[0] = 2)
            # Current result: [1]
        else:                               # Skip (arr1[i] < arr2[j] is True)
            result.append(arr2[j])          # Skip
            j += 1                          # Skip
        # After Iteration 1: i = 1, j = 0, result = [1]
        # Element added: 1 from arr1

        # --- Iteration 2: i = 1, j = 0 ---
        if i < len(arr1) and j < len(arr2):  # i = 1 < 2 and j = 0 < 3 → True
            if arr1[i] < arr2[j]:           # arr1[1] = 3, arr2[0] = 2, 3 < 2 → False
                result.append(arr1[i])       # Skip
                i += 1                       # Skip
            else:                            # Execute else block
                result.append(arr2[j])       # Append arr2[0] = 2 to result
                                             # result = [1, 2]
                j += 1                       # j = 0 + 1 = 1
                # After else: i = 1 (points to arr1[1] = 3), j = 1 (points to arr2[1] = 4)
                # Current result: [1, 2]
        # After Iteration 2: i = 1, j = 1, result = [1, 2]
        # Element added: 2 from arr2

        # --- Iteration 3: i = 1, j = 1 ---
        if i < len(arr1) and j < len(arr2):  # i = 1 < 2 and j = 1 < 3 → True
            if arr1[i] < arr2[j]:           # arr1[1] = 3, arr2[1] = 4, 3 < 4 → True
                result.append(arr1[i])       # Append arr1[1] = 3 to result
                                             # result = [1, 2, 3]
                i += 1                       # i = 1 + 1 = 2
                # After if: i = 2 (beyond arr1[1]), j = 1 (points to arr2[1] = 4)
                # Current result: [1, 2, 3]
            else:                            # Skip (arr1[i] < arr2[j] is True)
                result.append(arr2[j])       # Skip
                j += 1                       # Skip
        # After Iteration 3: i = 2, j = 1, result = [1, 2, 3]
        # Element added: 3 from arr1

        # --- Iteration 4: i = 2, j = 1 ---
        if i < len(arr1) and j < len(arr2):  # i = 2 < 2 and j = 1 < 3 → False (i >= len(arr1))
            pass                             # Loop exits
        # Loop terminates: i = 2 (at end of arr1), j = 1 (points to arr2[1] = 4)

    # 3️⃣ Append remaining elements from arr1, if any
    # Why? If arr1 has unprocessed elements, they are larger and should be appended
    result.extend(arr1[i:])              # arr1[2:] = [] (empty, i is at end)
                                         # result = [1, 2, 3] (no change)
    
    # 4️⃣ Append remaining elements from arr2, if any
    # Why? If arr2 has unprocessed elements, they are larger and should be appended
    result.extend(arr2[j:])              # arr2[1:] = [4, 6]
                                         # result = [1, 2, 3] + [4, 6] = [1, 2, 3, 4, 6]
    
    # 5️⃣ Return the merged sorted array
    # Why? The result contains all elements from arr1 and arr2 in sorted order
    return result                        # Return result = [1, 2, 3, 4, 6]
    # Final state: Merged array [1, 2, 3, 4, 6]
    # Conclusion: Successfully merged arr1 = [1, 3] and arr2 = [2, 4, 6]

print(merge_sorted_arrays([1, 3], [2, 4, 6]))  # Output: [1, 2, 3, 4, 6]



# ----------------------------------------------------------------------------------
# Solution with output 

def merge_sorted_arrays(arr1, arr2):  # Example: arr1 = [1, 3], arr2 = [2, 4]

    # 1️⃣ Initialize result array and pointers
    result = []                      # result = []
    
    # Set pointers for arr1 and arr2
    i, j = 0, 0                      # i = 0 (points to arr1[0] = 1), j = 0 (points to arr2[0] = 2)
    # After initialization: i tracks arr1, j tracks arr2, result is empty

    # 2️⃣ Merge arrays while both pointers are within bounds
    # Continue while both arrays have elements to compare
    while i < len(arr1) and j < len(arr2):  # len(arr1) = 2, len(arr2) = 2, i = 0, j = 0
                                            # i < 2 and j < 2 → True (loop starts)
        
        # --- Iteration 1: i = 0, j = 0 ---
        # Compare elements at pointers i and j
        if arr1[i] < arr2[j]:               # arr1[0] = 1, arr2[0] = 2, 1 < 2 → True
            result.append(arr1[i])          # Append arr1[0] = 1 to result
                                            # result = [1]
            i += 1                          # i = 0 + 1 = 1
            # After if: i = 1 (points to arr1[1] = 3), j = 0 (points to arr2[0] = 2)
            # Current result: [1]
        else:                               # Skip (arr1[i] < arr2[j] is True)
            result.append(arr2[j])          # Skip
            j += 1                          # Skip
        # After Iteration 1: i = 1, j = 0, result = [1]
        # Element added: 1 from arr1

        # --- Iteration 2: i = 1, j = 0 ---
        if i < len(arr1) and j < len(arr2):  # i = 1 < 2 and j = 0 < 2 → True
            if arr1[i] < arr2[j]:           # arr1[1] = 3, arr2[0] = 2, 3 < 2 → False
                result.append(arr1[i])       # Skip
                i += 1                       # Skip
            else:                            # Execute else block
                result.append(arr2[j])       # Append arr2[0] = 2 to result
                                             # result = [1, 2]
                j += 1                       # j = 0 + 1 = 1
                # After else: i = 1 (points to arr1[1] = 3), j = 1 (points to arr2[1] = 4)
                # Current result: [1, 2]
        # After Iteration 2: i = 1, j = 1, result = [1, 2]
        # Element added: 2 from arr2

        # --- Iteration 3: i = 1, j = 1 ---
        if i < len(arr1) and j < len(arr2):  # i = 1 < 2 and j = 1 < 2 → True
            if arr1[i] < arr2[j]:           # arr1[1] = 3, arr2[1] = 4, 3 < 4 → True
                result.append(arr1[i])       # Append arr1[1] = 3 to result
                                             # result = [1, 2, 3]
                i += 1                       # i = 1 + 1 = 2
                # After if: i = 2 (beyond arr1[1]), j = 1 (points to arr2[1] = 4)
                # Current result: [1, 2, 3]
            else:                            # Skip (arr1[i] < arr2[j] is True)
                result.append(arr2[j])       # Skip
                j += 1                       # Skip
        # After Iteration 3: i = 2, j = 1, result = [1, 2, 3]
        # Element added: 3 from arr1

        # --- Iteration 4: i = 2, j = 1 ---
        if i < len(arr1) and j < len(arr2):  # i = 2 < 2 and j = 1 < 2 → False (i >= len(arr1))
            pass                             # Loop exits
        # Loop terminates: i = 2 (at end of arr1), j = 1 (points to arr2[1] = 4)

    # 3️⃣ Append remaining elements from arr1, if any
    result.extend(arr1[i:])              # arr1[2:] = [] (empty, i is at end)
                                         # result = [1, 2, 3] (no change)
    # 4️⃣ Append remaining elements from arr2, if any
    result.extend(arr2[j:])              # arr2[1:] = [4]
                                         # result = [1, 2, 3] + [4] = [1, 2, 3, 4]
    
    # 5️⃣ Return the merged sorted array
    return result                        # Return result = [1, 2, 3, 4]
    # Final state: Merged array [1, 2, 3, 4]

print(merge_sorted_arrays([1, 3], [2, 4]))  # Output: [1, 2, 3, 4]
