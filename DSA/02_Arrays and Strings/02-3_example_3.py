# Merge Two Sorted Arrays into One Sorted Array

# Example 3: Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.

def merge_sorted_arrays(arr1, arr2):
    ans = []            
    i = j = 0              

    # Compare elements while both arrays have elements
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:  
            ans.append(arr1[i])
            i += 1
        else:                   
            ans.append(arr2[j])
            j += 1

    # Add remaining elements from arr1, if any
    while i < len(arr1):
        ans.append(arr1[i])
        i += 1

    # Add remaining elements from arr2, if any
    while j < len(arr2):
        ans.append(arr2[j])
        j += 1

    return ans              

arr1 = [1, 4, 7, 20]
arr2 = [3, 5, 6]
print(merge_sorted_arrays(arr1, arr2))
# Output: [1, 3, 4, 5, 6, 7, 20]


# Time: O(n + m)
# - Compare elements from both arrays once: O(n + m), where n = len(arr1) and m = len(arr2).
# - Remaining elements from each array are appended in O(n) or O(m) total.
# - No nested loops that depend on each other.

# Space: O(n + m)
# - Result array 'ans' stores all elements from both arrays, O(n + m) space.
# - Only a constant number of extra variables (i, j) are used besides the output array.
# - If we exclude the result array, extra working space is O(1).


"""

Overview for Each Iteration
Input: arr1 = [1, 4, 7, 20], arr2 = [3, 5, 6]
Step 1: Merge arrays while both have elements
i  | j | arr1[i] | arr2[j] | arr1[i] <= arr2[j] | Action         | ans
---|---|---------|---------|--------------------|----------------|-----------------
0  | 0 | 1       | 3       | True               | Append 1, i+=1 | [1]
1  | 0 | 4       | 3       | False              | Append 3, j+=1 | [1, 3]
1  | 1 | 4       | 5       | True               | Append 4, i+=1 | [1, 3, 4]
2  | 1 | 7       | 5       | False              | Append 5, j+=1 | [1, 3, 4, 5]
2  | 2 | 7       | 6       | False              | Append 6, j+=1 | [1, 3, 4, 5, 6]

Step 2: Add remaining elements from arr1
i  | arr1[i] | Action         | ans
---|---------|----------------|-------------------
2  | 7       | Append 7, i+=1 | [1, 3, 4, 5, 6, 7]
3  | 20      | Append 20, i+=1| [1, 3, 4, 5, 6, 7, 20]

Step 3: Add remaining elements from arr2
j  | arr2[j] | Action         | ans
---|---------|----------------|-------------------
-  | -       | None (j=3)     | [1, 3, 4, 5, 6, 7, 20]
Final: [1, 3, 4, 5, 6, 7, 20]




Q: Why does j=3 in Step 3?
    • The last action in step 1 is j+=1 -> 2+=1=3


Q: Why use while i < len(arr1) and j < len(arr2) to loop thru the array?
    • Only compare while both arrays have elements (prevents index out of range).
    • Once one array is exhausted, stop comparing and append the rest from the other.
    • This “two-pointer + cleanup” pattern is common in merge sort, merging linked lists, and other two-pointer problems.


Q: while vs if: Merging sorted arrays
    • while: Repeats until condition false, processes all items (e.g., full array merge).
    • if: Checks once, processes one item (e.g., partial merge).
    • Use while for loops over multiple items, if for single checks.

"""


# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def merge_sorted_arrays(arr1, arr2):
    ans = []                 # Result array to store merged elements
    i = j = 0                # Pointer for arr1, and arr2 starts at index 0

    # Compare elements while both arrays have elements
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:  # Add smaller element from arr1
            ans.append(arr1[i])
            i += 1
        else:                   # Add smaller element from arr2
            ans.append(arr2[j])
            j += 1

    # Add remaining elements from arr1, if any
    while i < len(arr1):
        ans.append(arr1[i])
        i += 1

    # Add remaining elements from arr2, if any
    while j < len(arr2):
        ans.append(arr2[j])
        j += 1

    return ans                  # Return merged sorted array



# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Task: Merge two sorted integer arrays into a new sorted array.
# Example: arr1 = [1, 4, 7, 20], arr2 = [3, 5, 6] → Output = [1, 3, 4, 5, 6, 7, 20]
# Why: Practices two-pointer technique to efficiently combine sorted arrays.

def merge_sorted_arrays(arr1, arr2):  # Example: arr1 = [1, 4, 7, 20], arr2 = [3, 5, 6]

    # 1️⃣ Initialize result array and pointers
    # Initialize an empty list to store the merged result
    # Why? We need to build a new sorted array containing all elements
    ans = []  # ans = []

    # Initialize pointer i for arr1
    # Why? Tracks the current element in arr1
    i = 0  # i = 0

    # Initialize pointer j for arr2
    # Why? Tracks the current element in arr2
    j = 0  # j = 0

    # 2️⃣ Compare elements while both arrays have elements
    # Continue while both pointers are within their respective arrays
    # Why? We need to compare elements from both arrays to merge in sorted order
    while i < len(arr1) and j < len(arr2):  # i = 0, len(arr1) = 4, j = 0, len(arr2) = 3
        # --- Iteration 1 ---
        # Compare elements at i and j
        # Why? We append the smaller element to maintain sorted order
        if arr1[i] <= arr2[j]:  # arr1[0] = 1, arr2[0] = 3, 1 <= 3 is true
            ans.append(arr1[i])  # ans = [1]
            i += 1  # i = 0 + 1 = 1
        else:
            ans.append(arr2[j])  # skip
            j += 1  # skip
        # After Iteration 1: i = 1, j = 0, ans = [1]

        # --- Iteration 2 ---
        if i == 1 and j == 0:
            if arr1[i] <= arr2[j]:  # arr1[1] = 4, arr2[0] = 3, 4 <= 3 is false
                ans.append(arr1[i])
                i += 1
            else:
                ans.append(arr2[j])  # ans = [1, 3]
                j += 1  # j = 0 + 1 = 1
            # After Iteration 2: i = 1, j = 1, ans = [1, 3]

        # --- Iteration 3 ---
        if i == 1 and j == 1:
            if arr1[i] <= arr2[j]:  # arr1[1] = 4, arr2[1] = 5, 4 <= 5 is true
                ans.append(arr1[i])  # ans = [1, 3, 4]
                i += 1  # i = 1 + 1 = 2
            else:
                ans.append(arr2[j])
                j += 1
            # After Iteration 3: i = 2, j = 1, ans = [1, 3, 4]

        # --- Iteration 4 ---
        if i == 2 and j == 1:
            if arr1[i] <= arr2[j]:  # arr1[2] = 7, arr2[1] = 5, 7 <= 5 is false
                ans.append(arr1[i])
                i += 1
            else:
                ans.append(arr2[j])  # ans = [1, 3, 4, 5]
                j += 1  # j = 1 + 1 = 2
            # After Iteration 4: i = 2, j = 2, ans = [1, 3, 4, 5]

        # --- Iteration 5 ---
        if i == 2 and j == 2:
            if arr1[i] <= arr2[j]:  # arr1[2] = 7, arr2[2] = 6, 7 <= 6 is false
                ans.append(arr1[i])
                i += 1
            else:
                ans.append(arr2[j])  # ans = [1, 3, 4, 5, 6]
                j += 1  # j = 2 + 1 = 3
            # After Iteration 5: i = 2, j = 3, ans = [1, 3, 4, 5, 6]
            # Loop exits: j = 3, len(arr2) = 3, condition j < len(arr2) is false

    # 3️⃣ Add remaining elements from arr1, if any
    # Append any remaining elements from arr1
    # Why? One array may have elements left after the other is exhausted
    while i < len(arr1):  # i = 2, len(arr1) = 4, true
        ans.append(arr1[i])  # ans = [1, 3, 4, 5, 6, 7]
        i += 1  # i = 2 + 1 = 3
        # Next iteration: ans = [1, 3, 4, 5, 6, 7, 20]
        # i = 4, loop exits
    # After arr1 loop: i = 4, ans = [1, 3, 4, 5, 6, 7, 20]

    # 4️⃣ Add remaining elements from arr2, if any
    # Append any remaining elements from arr2
    # Why? Handle case where arr2 has remaining elements
    while j < len(arr2):  # j = 3, len(arr2) = 3, false, skip
        ans.append(arr2[j])  # skip
        j += 1  # skip
    # After arr2 loop: j = 3, ans = [1, 3, 4, 5, 6, 7, 20]

    # 5️⃣ Return the merged sorted array
    # Why? ans contains all elements from both arrays in sorted order
    return ans  # ans = [1, 3, 4, 5, 6, 7, 20]


arr1 = [1, 4, 7, 20]
arr2 = [3, 5, 6]
print(merge_sorted_arrays([1, 4, 7, 20], [3, 5, 6]))  
# Output: [1, 3, 4, 5, 6, 7, 20]