# Array Manipulation: Remove Duplicates from sorted Array
"""
Task: Remove duplicates from a sorted array in-place and return the new length.
    - Input is a non-empty array of integers

Example 1: [1, 1, 2] → [1, 2], new length: 2
Example 2: [0, 0, 1, 1, 1, 2, 2] → [0, 1, 2], new length: 3

Why: Teaches in-place manipulation and handling of duplicates in sorted data.
"""

def remove_duplicates(arr):    
    # 1️⃣ Initialize pointer for the position of the next unique element
    unique_pos = 1
    
    # 2️⃣ Traverse array, placing unique elements at unique_pos
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:  # If current element differs from previous
            arr[unique_pos] = arr[i]  # Place it at the next unique position
            unique_pos += 1  # Move the unique position forward
    
    # 3️⃣ Return the length of the array with duplicates removed
    return unique_pos

arr1 = [1, 1, 2]
new_len1 = remove_duplicates(arr1)
print(arr1[:new_len1])  # Output: [1, 2]

arr2 = [0, 0, 1, 1, 1, 2, 2]
new_len2 = remove_duplicates(arr2)
print(arr2[:new_len2])  # Output: [0, 1, 2]


# Simple Breakdown
"""
Removes duplicates from a sorted array in-place.
- Uses a pointer to track where to place the next unique element.
- Time Complexity: O(n), Space Complexity: O(1) as it’s in-place.
- Efficient and intuitive for sorted arrays.
"""