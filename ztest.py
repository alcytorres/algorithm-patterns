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
    
    result.extend(arr1[i:])
    result.extend(arr2[j:])

    # 5️⃣ Return the merged sorted array   
    return result 


print(merge_sorted_arrays([1, 3], [2, 4, 6]))  # Output: [1, 2, 3, 4, 6]