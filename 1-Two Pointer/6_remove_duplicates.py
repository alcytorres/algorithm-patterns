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
        if arr[read] != arr[write - 1]:  
            arr[write] = arr[read]  
            write += 1  

    # 4️⃣ Return the new length
    return write  


arr1 = [0,0,1,1,1,2,2,3,3,4]
length = remove_duplicates(arr1)  # length = 5
print(length)  # Output: 5
print(arr1[0:length])  # Output: [0, 1, 2, 3, 4]


"""
Why write and read variables?

I used write and read to clearly describe their roles in the two-pointer technique:

    - read: Iterates through the array, "reading" each element to check for duplicates.

    - write: Tracks the position where the next unique element should be "written" in the array.

    These names reflect their purpose: read scans the input, while write updates the array in-place. 
    
    This convention is common in array modification problems for clarity, similar to how left and right are used in other pointer-based solutions like Reverse Array.





    
"""

# ----------------------------------------------------------------------------------
# Solution with output Full Breakdown 


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

    # 3️⃣ Loop through array to compare adjacent elements
    # Iterate from index 1 to the end using a read pointer
    # Why? We compare each element with the last unique element to find new unique values
    for read in range(1, len(arr)):  # read goes from 1 to 9 (len(arr) = 10)
        # --- Iteration 1: read = 1 ---
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

    # 4️⃣ Return the new length
    # Return the count of unique elements
    # Why? 'write' indicates the length of the array with duplicates removed
    return write  # write = 5


arr1 = [0,0,1,1,1,2,2,3,3,4]
length = remove_duplicates(arr1)  # length = 5
print(length)  # Output: 5
print(arr1[0:length])  # Output: [0, 1, 2, 3, 4]



# ----------------------------------------------------------------------------------
# Solution with output Full Breakdown 

