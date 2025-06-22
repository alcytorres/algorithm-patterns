"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1: Input: nums = [0,1,0,3,12] --> Output: [1,3,12,0,0]
Example 2: Input: nums = [3,5,0,0,4] --> Output: [3,5,4,0,0]

https://www.youtube.com/watch?v=ls2rIJoj0c4&t=100s
"""



def move_zeros(arr):

    non_zero_pos = 0

    for read in range(len(arr)):
        if arr[read] != 0:
            arr[non_zero_pos], arr[read] = arr[read], arr[non_zero_pos]
            non_zero_pos += 1

    return arr

print(move_zeros([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]

print(move_zeros([3, 5, 0, 0, 4]))  # Output: [3, 5, 4, 0, 0]





# Task: Move all zeros to the end of an integer array in-place while maintaining the relative order of non-zero elements.
# Example: arr = [0, 1, 0, 3, 12] → Output = [1, 3, 12, 0, 0]

def move_zeros(arr):  # Example: arr = [0, 1, 0, 3, 12]

    # 1️⃣ Initialize pointer for non-zero elements
    # non_zero_pos tracks where to place the next non-zero element
    # Why? We need to keep non-zero elements in their relative order at the start of the array
    non_zero_pos = 0  # non_zero_pos = 0

    # 2️⃣ Move non-zero elements to the front
    # Iterate through the array with a read pointer
    # Why? We scan each element to identify non-zeros and move them forward
    for read in range(len(arr)):  # read goes from 0 to 4 (len(arr) = 5)
        # --- Iteration 1: read = 0 ---
        # Check if the current element is non-zero
        # Why? Non-zero elements need to be moved to the non_zero_pos
        if arr[read] != 0:  # arr[0] = 0, 0 != 0 is false, skip
            arr[non_zero_pos], arr[read] = arr[read], arr[non_zero_pos]  # skip
            non_zero_pos += 1  # skip
        # After Iteration 1: non_zero_pos = 0, arr = [0, 1, 0, 3, 12]

        # --- Iteration 2: read = 1 ---
        if read == 1:
            if arr[read] != 0:  # arr[1] = 1, 1 != 0 is true
                # Swap the non-zero element to non_zero_pos
                # Why? This places the non-zero element in the correct position
                arr[non_zero_pos], arr[read] = arr[read], arr[non_zero_pos]  # arr[0] = 0, arr[1] = 1
                                                                     # Swap: arr[0] = 1, arr[1] = 0
                non_zero_pos += 1  # non_zero_pos = 0 + 1 = 1
            # After Iteration 2: non_zero_pos = 1, arr = [1, 0, 0, 3, 12]

        # --- Iteration 3: read = 2 ---
        if read == 2:
            if arr[read] != 0:  # arr[2] = 0, 0 != 0 is false, skip
                arr[non_zero_pos], arr[read] = arr[read], arr[non_zero_pos]
                non_zero_pos += 1
            # After Iteration 3: non_zero_pos = 1, arr = [1, 0, 0, 3, 12]

        # --- Iteration 4: read = 3 ---
        if read == 3:
            if arr[read] != 0:  # arr[3] = 3, 3 != 0 is true
                arr[non_zero_pos], arr[read] = arr[read], arr[non_zero_pos]  # arr[1] = 0, arr[3] = 3
                                                                     # Swap: arr[1] = 3, arr[3] = 0
                non_zero_pos += 1  # non_zero_pos = 1 + 1 = 2
            # After Iteration 4: non_zero_pos = 2, arr = [1, 3, 0, 0, 12]

        # --- Iteration 5: read = 4 ---
        if read == 4:
            if arr[read] != 0:  # arr[4] = 12, 12 != 0 is true
                arr[non_zero_pos], arr[read] = arr[read], arr[non_zero_pos]  # arr[2] = 0, arr[4] = 12
                                                                     # Swap: arr[2] = 12, arr[4] = 0
                non_zero_pos += 1  # non_zero_pos = 2 + 1 = 3
            # After Iteration 5: non_zero_pos = 3, arr = [1, 3, 12, 0, 0]

    # 3️⃣ Return the modified array
    # Why? The array has been modified in-place with all zeros at the end
    return arr  # arr = [1, 3, 12, 0, 0]


print(move_zeros([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]




# ----------------------------------------------------------------------------------

# Task: Move all zeros to the end of an integer array in-place while maintaining the relative order of non-zero elements.
# Example: arr = [3, 5, 0, 0, 4] → Output = [3, 5, 4, 0, 0]

def move_zeros(arr):  # Example: arr = [3, 5, 0, 0, 4]

    # 1️⃣ Initialize pointer for non-zero elements
    # non_zero_pos tracks where to place the next non-zero element
    # Why? We need to keep non-zero elements in their relative order at the start of the array
    non_zero_pos = 0  # non_zero_pos = 0

    # 2️⃣ Move non-zero elements to the front
    # Iterate through the array with a read pointer
    # Why? We scan each element to identify non-zeros and move them forward
    for read in range(len(arr)):  # read goes from 0 to 4 (len(arr) = 5)
        # --- Iteration 1: read = 0 ---
        # Check if the current element is non-zero
        # Why? Non-zero elements need to be moved to the non_zero_pos
        if arr[read] != 0:  # arr[0] = 3, 3 != 0 is true
            # Swap the non-zero element to non_zero_pos
            # Why? This places the non-zero element in the correct position
            arr[non_zero_pos], arr[read] = arr[read], arr[non_zero_pos]  # arr[0] = 3, arr[0] = 3
                                                                         # Swap: arr[0] = 3, arr[0] = 3 (no change)
            non_zero_pos += 1  # non_zero_pos = 0 + 1 = 1
        # After Iteration 1: non_zero_pos = 1, arr = [3, 5, 0, 0, 4]

        # --- Iteration 2: read = 1 ---
        if read == 1:
            if arr[read] != 0:  # arr[1] = 5, 5 != 0 is true
                arr[non_zero_pos], arr[read] = arr[read], arr[non_zero_pos]  # arr[1] = 5, arr[1] = 5
                                                                             # Swap: arr[1] = 5, arr[1] = 5 (no change)
                non_zero_pos += 1  # non_zero_pos = 1 + 1 = 2
            # After Iteration 2: non_zero_pos = 2, arr = [3, 5, 0, 0, 4]

        # --- Iteration 3: read = 2 ---
        if read == 2:
            if arr[read] != 0:  # arr[2] = 0, 0 != 0 is false, skip
                arr[non_zero_pos], arr[read] = arr[read], arr[non_zero_pos]
                non_zero_pos += 1
            # After Iteration 3: non_zero_pos = 2, arr = [3, 5, 0, 0, 4]

        # --- Iteration 4: read = 3 ---
        if read == 3:
            if arr[read] != 0:  # arr[3] = 0, 0 != 0 is false, skip
                arr[non_zero_pos], arr[read] = arr[read], arr[non_zero_pos]
                non_zero_pos += 1
            # After Iteration 4: non_zero_pos = 2, arr = [3, 5, 0, 0, 4]

        # --- Iteration 5: read = 4 ---
        if read == 4:
            if arr[read] != 0:  # arr[4] = 4, 4 != 0 is true
                arr[non_zero_pos], arr[read] = arr[read], arr[non_zero_pos]  # arr[2] = 0, arr[4] = 4
                                                                             # Swap: arr[2] = 4, arr[4] = 0
                non_zero_pos += 1  # non_zero_pos = 2 + 1 = 3
            # After Iteration 5: non_zero_pos = 3, arr = [3, 5, 4, 0, 0]

    # 3️⃣ Return the modified array
    # Why? The array has been modified in-place with all zeros at the end
    return arr  # arr = [3, 5, 4, 0, 0]


print(move_zeros([3, 5, 0, 0, 4]))  # Output: [3, 5, 4, 0, 0]