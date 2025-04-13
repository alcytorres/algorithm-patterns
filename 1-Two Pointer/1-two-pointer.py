# Two Pointers
"""
Foundational Skills
   - Array indexing and manipulation
   - Loop control (e.g., for, while)
   - Conditional statements within loops
   - Basic arithmetic operations
Potential Knowledge Gaps
   - Difficulty managing multiple pointers (e.g., moving them independently or in sync)
   - Trouble visualizing pointer movements (e.g., from opposite ends or same direction)
   - Handling edge cases (e.g., empty arrays, single elements)
"""

# ----------------------------------------------------------------------------------
# 1. Sum of First and Last Elements
"""
# Task: Given an array, return the sum of its first and last elements.
# Example: [1, 2, 3] → 4 (1 + 3)
# Why: Introduces using two pointers at opposite ends.
"""

def sum_first_last(arr):
    if not arr:
        return 0
    first = arr[0]
    last = arr[-1]
    return first + last

# print(sum_first_last([1, 2, 3]))  # Output: 4 (1 + 3)

# Test cases:
# print(sum_first_last([5]))        # Output: 10 (5 + 5)
# print(sum_first_last([]))         # Output: 0 (0 + 0)
# print(sum_first_last([1, 2]))     # Output: 3 (1 + 2)


# Solution
def sum_first_last(arr):   # Define the function that takes an array 'arr' as input
    """
    Returns the sum of the first and last elements of the array.
    
    - Uses two pointers to access the start and end directly.
    - Time Complexity: O(1), Space Complexity: O(1).
    - Simple and beginner-friendly as it introduces pointer concepts without iteration.
    """
    if not arr:         # Check if the array is empty (no elements)
        return 0        # Return 0 if empty, since there's nothing to sum
    first = arr[0]      # Set 'first' to the first element (index 0, start of array)
    last = arr[-1]      # Set 'last' to the last element (index -1, end of array in Python)
    return first + last   # Add the first and last elements and return the result

# Test the function
print(sum_first_last([1, 2, 3]))  # Output: 4 (1 + 3)


# ----------------------------------------------------------------------------------
# 2. Check if Array is Sorted
"""
# Task: Determine if an array is sorted in ascending order.
# Example: [1, 2, 3, 4] → True, [1, 3, 2] → False
# Why: Practices moving pointers to compare adjacent elements.
"""

def is_sorted(arr):
    if len(arr) < 2:
        return True
    i, j = 0, 1
    while j < len(arr):
        if arr[i] > arr[j]:
            return False
        i += 1
        j += 1
    return True

# print(is_sorted([1, 2, 3, 4]))  # Output: True
# print(is_sorted([1, 3, 2]))     # Output: False


# Solution
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
# print(is_sorted([1, 2, 3, 4]))  # Output: True
# print(is_sorted([1, 3, 2]))     # Output: False


# ----------------------------------------------------------------------------------
# 3. Reverse an Array In-Place 
"""
Task: Reverse an array using two pointers without extra space.
Example: [1, 2, 3] → [3, 2, 1]
Why: Builds intuition for swapping elements with pointers, relevant to Valid Palindrome. 
"""

def reverse_array(arr):
    left, right = 0, len(arr) - 1   
    while left < right:             
        arr[left], arr[right] = arr[right], arr[left]  
        left += 1                   
        right -= 1                  
    return arr                      

# print(reverse_array([1, 2, 3]))  # Output: [3, 2, 1]


# Solution
def reverse_array(arr):   # Define the function that takes an array 'arr' as input
    """
    Reverses the array in-place using two pointers.
    
    - Pointers start at both ends and swap elements, moving inward.
    - Time Complexity: O(n/2) = O(n), Space Complexity: O(1).
    - In-place swapping makes this memory-efficient and beginner-friendly.
    """

    left, right = 0, len(arr) - 1   # Set 'left' to start (0) and 'right' to end (last index)
    while left < right:             # Loop until pointers meet in the middle
        arr[left], arr[right] = arr[right], arr[left]  # Swap elements at left and right pointers
        left += 1                   # Move left pointer one step right
        right -= 1                  # Move right pointer one step left
    return arr                      # Return the reversed array

# Test the function
# print(reverse_array([1, 2, 3]))  # Output: [3, 2, 1]


# ----------------------------------------------------------------------------------
# 4. Find Pair with Target Difference
"""
Task: Find two numbers in an array whose difference is a given target. The larger number minus the smaller should equal the target.
Example: [1, 3, 5, 8], target = 2 → [1, 3]
Why: Prepares for Two Sum by practicing pointer movement for a condition.
"""

def find_pair_with_difference(arr, target):
    arr.sort()                   
    left, right = 0, 1           
    while right < len(arr):      
        diff = arr[right] - arr[left]  
        if diff == target:       
            return [arr[left], arr[right]]  
        elif diff < target:      
            right += 1           
        else:                   
            left += 1            
            if left == right:   
                right += 1       
    return None       

# print(find_pair_with_difference([1, 3, 5, 8], 2))  # Output: [1, 3]
# print(find_pair_with_difference([8, 1, 3, 5], 3))  # Output: [5, 8]
# print(find_pair_with_difference([1, 2, 4], 5))  # Output: None
# print(find_pair_with_difference([1, 5, 6], 2))  # Output: None


# Solution
def find_pair_with_difference(arr, target):   # Define the function that takes an array 'arr' and an integer 'target' as inputs
    """
    Finds two numbers in the array whose difference equals the target.
    
    - Sorts array first, then uses two pointers to find the pair.
    - Time Complexity: O(n log n) due to sorting, Space Complexity: O(1).
    - Sorting simplifies the problem for beginners, though a hash table could be O(n).
    """
    arr.sort()                   # Sort array in ascending order to use two pointers effectively
    left, right = 0, 1           # Set 'left' to 0 and 'right' to 1 (start with adjacent elements)
    while right < len(arr):      # Loop until 'right' reaches the end of the array
        diff = arr[right] - arr[left]  # Calculate difference between elements at right and left
        if diff == target:       # Check if the difference matches the target
            return [arr[left], arr[right]]  # Return the pair if target is found
        elif diff < target:      # If difference is too small
            right += 1           # Move 'right' forward to increase the difference
        else:                    # If difference is too large
            left += 1            # Move 'left' forward to decrease the difference
            if left == right:    # If pointers overlap after moving 'left'
                right += 1       # Move 'right' forward to keep them distinct
    return None                  # Return None if no pair is found

# Test the function
# print(find_pair_with_difference([1, 3, 5, 8], 2))  # Output: [1, 3]
# print(find_pair_with_difference([8, 1, 3, 5], 3))  # Output: [5, 8]
# print(find_pair_with_difference([1, 2, 4], 5))  # Output: None
# print(find_pair_with_difference([1, 5, 6], 2))  # Output: None


# ----------------------------------------------------------------------------------
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

# print(merge_sorted_arrays([1, 3], [2, 4]))  # Output: [1, 2, 3, 4]
# print(merge_sorted_arrays([1, 3], [2, 4, 6]))  # Output: [1, 2, 3, 4, 6]


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

