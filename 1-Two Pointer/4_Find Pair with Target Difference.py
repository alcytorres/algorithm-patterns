# 4. Find Pair with Target Difference
"""
Task: Find two numbers in an array whose difference is a given target. The larger number minus the smaller should equal the target. Return None if no pair is found
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

print(find_pair_with_difference([1, 3, 5, 8], 2))  # Output: [1, 3]
print(find_pair_with_difference([8, 1, 3, 5], 3))  # Output: [5, 8]
print(find_pair_with_difference([1, 2, 10], 5))  # Output: None


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
# print(find_pair_with_difference([1, 2, 10], 5))  # Output: None


"""
Explanation  if left == right: 
                right += 1  
This part of the find_pair_with_difference code prevents the left and right pointers from pointing to the same number after left moves forward.

How to know when to Use if left == right: right += 1
      - Two pointers (left, right) compare/process pairs in a loop.
      - Moving one pointer (left += 1) might make left == right.
      - You need different elements (e.g., for sum, difference).
   - Sign it’s needed: Overlapping pointers give wrong results (e.g., arr[right] - arr[left] = 0).
   - Examples: Pair-finding (difference = target), two-sum, sorted array problems where left catching right breaks logic.
"""
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
# Solution with output 
def find_pair_with_difference(arr, target):         # arr = [1, 3, 5, 8], target = 2
    arr.sort()                                      # arr = [1, 3, 5, 8] (already sorted)
    left, right = 0, 1                              # left = 0, right = 1
    while right < len(arr):                         # right < 4 → True (loop runs)
        diff = arr[right] - arr[left]               # Iteration 1: arr[1] - arr[0] = 3 - 1 = 2
        if diff == target:                          # 2 == 2 → True
            return [arr[left], arr[right]]          # Return [arr[0], arr[1]] = [1, 3]
        elif diff < target:                         # skip
            right += 1                              # skip
        else:                                       # skip
            left += 1                               # skip
            if left == right:                       # skip
                right += 1                          # skip
    return None                                     # Not reached

print(find_pair_with_difference([1, 3, 5, 8], 2))  # Output: [1, 3] (pair with difference 2)


# ----------------------------------------------------------------------------------
# Solution with output 
def find_pair_with_difference(arr, target):         # arr = [8, 1, 3, 5], target = 3
    arr.sort()                                      # arr = [1, 3, 5, 8]
    left, right = 0, 1                              # left = 0, right = 1
    while right < len(arr):                         # right < 4 → True (loop runs)
        diff = arr[right] - arr[left]               # Iteration 1: arr[1] - arr[0] = 3 - 1 = 2
        if diff == target:                          # 2 == 3 → False
            return [arr[left], arr[right]]          # skip
        elif diff < target:                         # 2 < 3 → True
            right += 1                              # right = 2
        else:                                       # skip
            left += 1                               # skip
            if left == right:                       # skip
                right += 1                          # skip
                                    # Iteration 2: right < 4 → True
                                    # diff = arr[2] - arr[0] = 5 - 1 = 4
                                    # 4 == 3 → False
                                    # 4 < 3 → False
                                    # else: True
                                    # left = 1
                                    # left == right → 1 == 2 → False
                                    # Iteration 3: right < 4 → True
                                    # diff = arr[2] - arr[1] = 5 - 3 = 2
                                    # 2 == 3 → False
                                    # 2 < 3 → True
                                    # right = 3
                                    # Iteration 4: right < 4 → True
                                    # diff = arr[3] - arr[1] = 8 - 5 = 3
                                    # 3 == 3 → True
                                    # Return [arr[1], arr[3]] = [5, 8]
    return None                                      # Not reached

print(find_pair_with_difference([8, 1, 3, 5], 3))  # Output: [5, 8] (pair with difference 3)

