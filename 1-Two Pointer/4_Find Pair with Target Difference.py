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