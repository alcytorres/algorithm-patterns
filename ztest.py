# 6. Remove Duplicates from Sorted Array – In-Place Array Modification

"""
# Task: Given a sorted array, remove duplicates in-place such that each element appears only once and return the new length.

# Example: arr = [0,0,1,1,1,2,2,3,3,4] → [0,1,2,3,4,...], return 5

# Why: Practices pointer movement to modify arrays in-place, similar to Reverse Array and Merge Sorted Arrays.
"""

def remove_duplicates(arr):  # Example: arr = [0,0,1,1,1,2,2,3,3,4]

    # 1️⃣ Handle edge cases: empty or single-element arrays
    if len(arr) < 2:
        return len(arr)
    
    # 2️⃣ Initialize write pointer for unique elements
    write = 1

    # 3️⃣ Loop through array to compare adjacent elements
    for read in range(1, len(arr)):
        
        # 4️⃣ Check for unique element
        if arr[read] != arr[write -1]:
            arr[write] = arr[read]
            write += 1

    # 4️⃣ Return the new length
    return write


arr1 = [0,0,1,1,1,2,2,3,3,4]
length = remove_duplicates(arr1)  # length = 5
print(length)  # Output: 5
print(arr1[0:length])  # Output: [0, 1, 2, 3, 4]