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
    write = 1  # write = 1 (first element at arr[0] is kept)

    # 3️⃣ Loop through array to compare adjacent elements
    for read in range(1, len(arr)):

        # 4️⃣ Check for unique element
        if arr[read] != arr[write - 1]:  
            arr[write] = arr[read]  
            write += 1  

    # 4️⃣ Return the new length
    return write  


sorted_nums = [0,0,1,1,1,2,2,3,3,4]
length = remove_duplicates(sorted_nums)  # length = 5
print(length)  # Output: 5
print(sorted_nums[0:length])  # Output: [0, 1, 2, 3, 4]


# Simple Breakdown
def remove_duplicates(arr):   # Define the function that takes a sorted array 'arr' as input
    """
    Removes duplicates from a sorted array in-place and returns the new length.
    
    - Uses two pointers to track unique elements and overwrite duplicates.
    - Time Complexity: O(n) for one pass, Space Complexity: O(1) for in-place.
    - Simple for beginners, leverages sorted property to compare adjacent elements.
    """

    # 1️⃣ Handle edge cases: empty or single-element arrays
    if len(arr) < 2:         # If array has 0 or 1 element
        return len(arr)      # Return length (no duplicates possible)

    # 2️⃣ Initialize write pointer for unique elements
    write = 1                # Set 'write' to 1 (first element is always unique)

    # 3️⃣ Iterate through array with read pointer
    for read in range(1, len(arr)):  # Loop 'read' from 1 to end of array
      
        # 4️⃣ Check for unique element
        if arr[read] != arr[write - 1]:  # If current element differs from last unique
            arr[write] = arr[read]       # Copy current element to 'write' position
            write += 1                   # Move 'write' to next position

    # 5️⃣ Return count of unique elements
    return write             # Return 'write' (number of unique elements)




"""
Why write and read variables?

I used write and read to clearly describe their roles in the two-pointer technique:

    - read: Iterates through the array, "reading" each element to check for duplicates.

    - write: Tracks the position where the next unique element should be "written" in the array.

    These names reflect their purpose: read scans the input, while write updates the array in-place. 
    
    This convention is common in array modification problems for clarity, similar to how left and right are used in other pointer-based solutions like Reverse Array.


    
Why "arr[write - 1]" here:  if arr[read] != arr[write - 1]:

    The -1 in arr[write - 1] is needed because the write pointer marks the position where the next unique element will be placed, but we compare the CURRENT element (arr[read]) with the LAST unique element already placed, which is at arr[write - 1]. 
    
    This ensures we check if the current element is different from the previous unique one before adding it.



Solution Overview
    Goal: Change [0,0,1,1,1,2,2,3,3,4] to [0,1,2,3,4,...], return 5.
    Method: Use write (next unique spot) and read (scan array) pointers.
    Logic: Copy unique elements to write position, increment write.



Solution Breakdown: Explanation of the Output

    Input: arr = [0,0,1,1,1,2,2,3,3,4]
    
    Output: 5 (returned by the function), and the array is modified in-place to [0,1,2,3,4,...]

    Why: The function removed duplicates from the sorted array in-place, keeping only the first occurrence of each unique element:
        Unique elements: 0, 1, 2, 3, 4
        New length: 5
        Modified array (first 5 elements): [0, 1, 2, 3, 4]

    The two-pointer approach uses:
        A write pointer to track where to place the next unique element.
        A read pointer to scan through the array and find unique elements.

    When a new unique element is found (arr[read] != arr[write-1]), it is placed at arr[write], and write is incremented. This ensures all duplicates are overwritten, and the first write elements of the array contain the unique elements in sorted order.

This approach efficiently handles cases like empty arrays (returns 0), single-element arrays (returns 1), or arrays with all duplicates (e.g., [1,1,1] returns 1). For [0,0,1,1,1,2,2,3,3,4], it correctly transforms the array to [0,1,2,3,4,...] and returns the new length 5, practicing in-place array modification with pointer movement.
    
"""

# ----------------------------------------------------------------------------------
# Solution with Output Full Breakdown

def remove_duplicates(arr):  # Example: arr = [0,0,1,1,1,2,2,3,3,4]

    # 1️⃣ Handle edge cases: empty or single-element arrays
    # If the array has fewer than 2 elements, return its length
    # Why? Empty arrays have length 0, and single-element arrays have no duplicates
    if len(arr) < 2:  # len(arr) = 10, 10 < 2 is false, proceed
        return len(arr)  # skip

    # 2️⃣ Initialize write pointer for unique elements
    # Start write pointer at index 1 to keep the first element (always unique)
    # Why? We use 'write' to track where to place the next unique element
    write = 1  # write = 1 (first element at arr[0] is kept)

    # 3️⃣ Iterate through array with read pointer
    # Iterate from index 1 to the end using a read pointer
    # Why? We compare each element with the last unique element to find new unique values
    for read in range(1, len(arr)):  # read goes from 1 to 9 (len(arr) = 10)
        # --- Iteration 1: read = 1 ---
        # Check if current element is different from the last unique element
        # Why? A different element is unique and should be placed at the write position
        
        # 4️⃣ Check for unique element
        # Check if current element is different from the last unique element
        # Why? A different element is unique and should be placed at the write position
        if arr[read] != arr[write - 1]:  # arr[1] = 0, arr[write-1] = arr[0] = 0
                                         # 0 != 0 is false, skip
            arr[write] = arr[read]  # skip
            write += 1  # skip
        # After Iteration 1: write = 1, arr = [0,0,1,1,1,2,2,3,3,4]

        # --- Iteration 2: read = 2 ---
        if read == 2:
            if arr[read] != arr[write - 1]:  # arr[2] = 1, arr[0] = 0
                                             # 1 != 0 is true
                arr[write] = arr[read]  # arr[1] = 1
                write += 1  # write = 1 + 1 = 2
            # After Iteration 2: write = 2, arr = [0,1,1,1,1,2,2,3,3,4]

        # --- Iteration 3: read = 3 ---
        if read == 3:
            if arr[read] != arr[write - 1]:  # arr[3] = 1, arr[1] = 1
                                             # 1 != 1 is false, skip
                arr[write] = arr[read]
                write += 1
            # After Iteration 3: write = 2, arr = [0,1,1,1,1,2,2,3,3,4]

        # --- Iteration 4: read = 4 ---
        if read == 4:
            if arr[read] != arr[write - 1]:  # arr[4] = 1, arr[1] = 1
                                             # 1 != 1 is false, skip
                arr[write] = arr[read]
                write += 1
            # After Iteration 4: write = 2, arr = [0,1,1,1,1,2,2,3,3,4]

        # --- Iteration 5: read = 5 ---
        if read == 5:
            if arr[read] != arr[write - 1]:  # arr[5] = 2, arr[1] = 1
                                             # 2 != 1 is true
                arr[write] = arr[read]  # arr[2] = 2
                write += 1  # write = 2 + 1 = 3
            # After Iteration 5: write = 3, arr = [0,1,2,1,1,2,2,3,3,4]

        # --- Iteration 6: read = 6 ---
        if read == 6:
            if arr[read] != arr[write - 1]:  # arr[6] = 2, arr[2] = 2
                                             # 2 != 2 is false, skip
                arr[write] = arr[read]
                write += 1
            # After Iteration 6: write = 3, arr = [0,1,2,1,1,2,2,3,3,4]

        # --- Iteration 7: read = 7 ---
        if read == 7:
            if arr[read] != arr[write - 1]:  # arr[7] = 3, arr[2] = 2
                                             # 3 != 2 is true
                arr[write] = arr[read]  # arr[3] = 3
                write += 1  # write = 3 + 1 = 4
            # After Iteration 7: write = 4, arr = [0,1,2,3,1,2,2,3,3,4]

        # --- Iteration 8: read = 8 ---
        if read == 8:
            if arr[read] != arr[write - 1]:  # arr[8] = 3, arr[3] = 3
                                             # 3 != 3 is false, skip
                arr[write] = arr[read]
                write += 1
            # After Iteration 8: write = 4, arr = [0,1,2,3,1,2,2,3,3,4]

        # --- Iteration 9: read = 9 ---
        if read == 9:
            if arr[read] != arr[write - 1]:  # arr[9] = 4, arr[3] = 3
                                             # 4 != 3 is true
                arr[write] = arr[read]  # arr[4] = 4
                write += 1  # write = 4 + 1 = 5
            # After Iteration 9: write = 5, arr = [0,1,2,3,4,2,2,3,3,4]

    # 5️⃣ Return count of unique elements
    # Return the count of unique elements
    # Why? 'write' indicates the length of the array with duplicates removed
    return write  # write = 5


sorted_nums = [0,0,1,1,1,2,2,3,3,4]
length = remove_duplicates(sorted_nums)  # length = 5
print(length)  # Output: 5
print(sorted_nums[0:length])  # Output: [0, 1, 2, 3, 4]



# ----------------------------------------------------------------------------------
# Solution with Output Full Breakdown

"""
Task: Given a sorted array, remove duplicates in-place such that each element appears only once and return the new length.

Example: arr = [0,0,1,2,2,3,4] → [0,1,2,3,4,...], return 5
"""

def remove_duplicates(arr):  # Example: arr = [0,0,1,2,2,3,4]

    # 1️⃣ Handle edge cases: empty or single-element arrays
    # If the array has fewer than 2 elements, return its length
    # Why? Empty arrays have length 0, and single-element arrays have no duplicates
    if len(arr) < 2:  # len(arr) = 7, 7 < 2 is false, proceed
        return len(arr)  # skip

    # 2️⃣ Initialize write pointer for unique elements
    # Start write pointer at index 1 to keep the first element (always unique)
    # Why? We use 'write' to track where to place the next unique element
    write = 1  # write = 1 (first element at arr[0] is kept)

    # 3️⃣ Loop through array to compare adjacent elements
    # Iterate from index 1 to the end using a read pointer
    # Why? We compare each element with the last unique element to find new unique values
    for read in range(1, len(arr)):  # read goes from 1 to 6 (len(arr) = 7)
        # --- Iteration 1: read = 1 ---
        # Check if current element is different from the last unique element
        # Why? A different element is unique and should be placed at the write position
        if arr[read] != arr[write - 1]:  # arr[1] = 0, arr[write-1] = arr[0] = 0
                                         # 0 != 0 is false, skip
            arr[write] = arr[read]  # skip
            write += 1  # skip
        # After Iteration 1: write = 1, arr = [0,0,1,2,2,3,4]

        # --- Iteration 2: read = 2 ---
        if read == 2:
            if arr[read] != arr[write - 1]:  # arr[2] = 1, arr[0] = 0
                                             # 1 != 0 is true
                arr[write] = arr[read]  # arr[1] = 1
                write += 1  # write = 1 + 1 = 2
            # After Iteration 2: write = 2, arr = [0,1,1,2,2,3,4]

        # --- Iteration 3: read = 3 ---
        if read == 3:
            if arr[read] != arr[write - 1]:  # arr[3] = 2, arr[1] = 1
                                             # 2 != 1 is true
                arr[write] = arr[read]  # arr[2] = 2
                write += 1  # write = 2 + 1 = 3
            # After Iteration 3: write = 3, arr = [0,1,2,2,2,3,4]

        # --- Iteration 4: read = 4 ---
        if read == 4:
            if arr[read] != arr[write - 1]:  # arr[4] = 2, arr[2] = 2
                                             # 2 != 2 is false, skip
                arr[write] = arr[read]
                write += 1
            # After Iteration 4: write = 3, arr = [0,1,2,2,2,3,4]

        # --- Iteration 5: read = 5 ---
        if read == 5:
            if arr[read] != arr[write - 1]:  # arr[5] = 3, arr[2] = 2
                                             # 3 != 2 is true
                arr[write] = arr[read]  # arr[3] = 3
                write += 1  # write = 3 + 1 = 4
            # After Iteration 5: write = 4, arr = [0,1,2,3,2,3,4]

        # --- Iteration 6: read = 6 ---
        if read == 6:
            if arr[read] != arr[write - 1]:  # arr[6] = 4, arr[3] = 3
                                             # 4 != 3 is true
                arr[write] = arr[read]  # arr[4] = 4
                write += 1  # write = 4 + 1 = 5
            # After Iteration 6: write = 5, arr = [0,1,2,3,4,3,4]

    # 4️⃣ Return the new length
    # Return the count of unique elements
    # Why? 'write' indicates the length of the array with duplicates removed
    return write  # write = 5


sorted_nums = [0,0,1,2,2,3,4]
length = remove_duplicates(sorted_nums)  # length = 5
print(length)  # Output: 5
print(sorted_nums[0:length])  # Output: [0, 1, 2, 3, 4]
