# 5. Merge Two Sorted Arrays
"""
Task: Merge two sorted arrays into one sorted array.
Example: [1, 3], [2, 4] → [1, 2, 3, 4]
Why: Reinforces pointer use in sorted data, akin to Remove Duplicates From Sorted Array.
"""

def merge_sorted_arrays(arr1, arr2):
    result = []        
    i, j = 0, 0          
    while i < len(arr1) and j < len(arr2): 
        if arr1[i] < arr2[j]:  
            result.append(arr1[i]) 
            i += 1        
        else:              
            result.append(arr2[j])  
            j += 1         
    result.extend(arr1[i:])  
    result.extend(arr2[j:])  
    return result       

print(merge_sorted_arrays([1, 3], [2, 4]))  # Output: [1, 2, 3, 4]
print(merge_sorted_arrays([1, 3], [2, 4, 6]))  # Output: [1, 2, 3, 4, 6]


# Solution
def merge_sorted_arrays(arr1, arr2):   # Define the function that takes two arrays 'arr1' and 'arr2' as inputs
    """
    Merges two sorted arrays into one sorted array.
    
    - Uses two pointers to compare and build result iteratively.
    - Time Complexity: O(n + m), Space Complexity: O(n + m) for result.
    - Iterative merging is straightforward and beginner-friendly.
    """

    result = []           # Create empty list to store the merged sorted array
    i, j = 0, 0           # Set 'i' as pointer for arr1, 'j' as pointer for arr2, both start at 0
    while i < len(arr1) and j < len(arr2):  # Loop while both arrays have elements to compare
        if arr1[i] < arr2[j]:  # Compare elements at pointers: if arr1's is smaller
            result.append(arr1[i])  # Add arr1's element to result
            i += 1          # Move arr1's pointer forward
        else:               # If arr2's element is smaller or equal
            result.append(arr2[j])  # Add arr2's element to result
            j += 1          # Move arr2's pointer forward
    result.extend(arr1[i:])  # Add any remaining elements from arr1 (from i to end)
    result.extend(arr2[j:])  # Add any remaining elements from arr2 (from j to end)
    return result         # Return the fully merged and sorted array

# Test the function
# print(merge_sorted_arrays([1, 3], [2, 4]))  # Output: [1, 2, 3, 4]
# print(merge_sorted_arrays([1, 3], [2, 4, 6]))  # Output: [1, 2, 3, 4, 6]


# ----------------------------------------------------------------------------------
# Solution with output 

def merge_sorted_arrays(arr1, arr2):
    result = []        
    i, j = 0, 0          
    while i < len(arr1) and j < len(arr2): 
        if arr1[i] < arr2[j]:  
            result.append(arr1[i]) 
            i += 1        
        else:              
            result.append(arr2[j])  
            j += 1         
    result.extend(arr1[i:])  
    result.extend(arr2[j:])  
    return result       

# print(merge_sorted_arrays([1, 3], [2, 4]))  # Output: [1, 2, 3, 4]

# Solution with output 
def merge_sorted_arrays(arr1, arr2):         # arr1 = [1, 3], arr2 = [2, 4]
    result = []                              # result = []
    i, j = 0, 0                              # i = 0, j = 0
    while i < len(arr1) and j < len(arr2):   # i < 2 and j < 2 → True (loop runs)
        if arr1[i] < arr2[j]:                # Iteration 1: arr1[0] < arr2[0] → 1 < 2 → True
            result.append(arr1[i])           # result = [1]
            i += 1                           # i = 1
        else:                                # skip
            result.append(arr2[j])           # skip
            j += 1                           # skip
                    # Iteration 2: i < 2 and j < 2 → True
                    # arr1[1] < arr2[0] → 3 < 2 → False
                    # else: True
                    # result.append(arr2[0]) → result = [1, 2]
                    # j = 1
                    # Iteration 3: i < 2 and j < 2 → True
                    # arr1[1] < arr2[1] → 3 < 4 → True
                    # result.append(arr1[1]) → result = [1, 2, 3]
                    # i = 2
                    # Iteration 4: i < 2 and j < 2 → False (i = 2, loop ends)
    result.extend(arr1[i:])                  # arr1[2:] = [] → result = [1, 2, 3]
    result.extend(arr2[j:])                  # arr2[1:] = [4] → result = [1, 2, 3, 4]
    return result                            # Return [1, 2, 3, 4]

print(merge_sorted_arrays([1, 3], [2, 4]))  # Output: [1, 2, 3, 4] (merged sorted array)

