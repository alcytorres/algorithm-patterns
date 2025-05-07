# 4. Find Pair with Target Difference
"""
Task: Find two numbers in an array whose difference is a given target. The larger number minus the smaller should equal the target. Return None if no pair is found.
Example 1: [1, 4, 3, 7], target = 6 → [1, 7]
Example 2: [1, 3, 8],    target = 2 → [1, 3]
Why: Prepares for Two Sum by practicing pointer movement for a condition.
"""

def find_pair_with_difference(arr, target):
    # 1️⃣ Sort the array
    arr.sort()   

    # 2️⃣ Initialize two pointers                
    left, right = 0, 1   

    # 3️⃣ Loop through the array to find the pair        
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

    # 4️⃣ Return None if no pair is found
    return None       

print(find_pair_with_difference([1, 5, 4, 10], 3))  # Output: [1, 4]
print(find_pair_with_difference([1, 3, 8], 2))  # Output: [1, 3]
print(find_pair_with_difference([8, 1, 3, 5], 3))  # Output: [5, 8]
print(find_pair_with_difference([1, 2, 10], 5))  # Output: None


# Simple Breakdown
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
# print(find_pair_with_difference([1, 5, 4, 10], 3))  # Output: [1, 4]
# print(find_pair_with_difference([1, 3, 8], 2))  # Output: [1, 3]
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
# Solution with output Full Breakdown

def find_pair_with_difference(arr, target):  # Example: arr = [1, 4, 3, 7], target = 6

    # 1️⃣ Sort the array
    # Sort the input array in ascending order
    # Why? Sorting allows us to use two pointers to efficiently find a pair with the target difference
    arr.sort()                              # arr = [1, 4, 3, 7] → arr = [1, 3, 4, 7]
    # After sorting: arr = [1, 3, 4, 7]

    # 2️⃣ Initialize two pointers
    # Set left pointer to the start and right pointer to the next position
    # Why? We'll compare pairs of elements to check their difference
    left, right = 0, 1                      # left = 0 (points to arr[0] = 1), right = 1 (points to arr[1] = 3)
    # After initialization: We'll compute arr[right] - arr[left] to find the target difference

    # 3️⃣ Loop through the array to find the pair
    # Continue while right pointer is within array bounds
    # Why? We need to check all possible pairs until we find the target difference or exhaust options
    while right < len(arr):                 # len(arr) = 4, right = 1 < 4 → True (loop starts)
        
        # --- Iteration 1: left = 0, right = 1 ---
        # Calculate the difference between elements at right and left pointers
        # Why? We need to check if arr[right] - arr[left] equals the target
        diff = arr[right] - arr[left]       # arr[1] = 3, arr[0] = 1, diff = 3 - 1 = 2
        
        # Check if the difference equals the target
        # Why? If diff == target, we've found the desired pair
        if diff == target:                  # diff = 2, target = 6, 2 == 6 → False
            return [arr[left], arr[right]]  # Skip (not applicable)
        
        # If difference is less than target, increase the difference
        # Why? Moving right pointer increases arr[right], potentially increasing the difference
        elif diff < target:                 # diff = 2 < 6 → True
            right += 1                      # right = 1 + 1 = 2
            # After elif: left = 0 (points to arr[0] = 1), right = 2 (points to arr[2] = 4)
            # Current array: [1, 3, 4, 7], pair checked: (1, 3), diff = 2
        
        # If difference is greater than target, decrease the difference
        # Why? Moving left pointer increases arr[left], reducing the difference
        else:                               # Skip (diff = 2 < 6, else not executed)
            left += 1                       # Skip
            # Ensure left and right don't point to the same element
            # Why? We need distinct elements for a valid pair
            if left == right:               # Skip
                right += 1                  # Skip
        # After Iteration 1: left = 0, right = 2
        # Current pair checked: (1, 3), diff = 2 (too small)

        # --- Iteration 2: left = 0, right = 2 ---
        if right < len(arr):                # right = 2 < 4 → True
            diff = arr[right] - arr[left]   # arr[2] = 4, arr[0] = 1, diff = 4 - 1 = 3
            if diff == target:              # diff = 3, target = 6, 3 == 6 → False
                return [arr[left], arr[right]]  # Skip
            elif diff < target:             # diff = 3 < 6 → True
                right += 1                  # right = 2 + 1 = 3
                # After elif: left = 0 (points to arr[0] = 1), right = 3 (points to arr[3] = 7)
                # Current array: [1, 3, 4, 7], pair checked: (1, 4), diff = 3
            else:                           # Skip (diff = 3 < 6)
                left += 1                   # Skip
                if left == right:           # Skip
                    right += 1              # Skip
        # After Iteration 2: left = 0, right = 3
        # Current pair checked: (1, 4), diff = 3 (too small)

        # --- Iteration 3: left = 0, right = 3 ---
        if right < len(arr):                # right = 3 < 4 → True
            diff = arr[right] - arr[left]   # arr[3] = 7, arr[0] = 1, diff = 7 - 1 = 6
            if diff == target:              # diff = 6, target = 6, 6 == 6 → True
                return [arr[left], arr[right]]  # Return [arr[0], arr[3]] = [1, 7]
            elif diff < target:             # Skip (diff == target, elif not executed)
                right += 1                  # Skip
            else:                           # Skip (diff == target, else not executed)
                left += 1                   # Skip
                if left == right:           # Skip
                    right += 1              # Skip
        # After Iteration 3: Function returns [1, 7]
        # Current pair checked: (1, 7), diff = 6 (matches target)
        # Loop terminates early due to return

    # 4️⃣ Return None if no pair is found
    # Why? If we exit the loop without finding a pair, no valid pair exists
    return None                         # Skip (not reached due to early return)
    # Final state: Found pair [1, 7] with difference 7 - 1 = 6
    # Conclusion: Pair [1, 7] satisfies the target difference

print(find_pair_with_difference([1, 4, 3, 7], 6))  # Output: [1, 7]


# ----------------------------------------------------------------------------------
# Solution with output 

def find_pair_with_difference(arr, target):  # Example: arr = [1, 3, 8], target = 2

    # 1️⃣ Sort the array
    arr.sort()                              # arr = [1, 3, 8] → arr = [1, 3, 8] (already sorted)
    # After sorting: arr = [1, 3, 8]

    # 2️⃣ Initialize two pointers
    # Set left pointer to the start and right pointer to the next position
    left, right = 0, 1                      # left = 0 (points to arr[0] = 1), right = 1 (points to arr[1] = 3)
    # After initialization: We'll compute arr[right] - arr[left] to find the target difference

    # 3️⃣ Loop through the array to find the pair
    # Continue while right pointer is within array bounds
    while right < len(arr):                 # len(arr) = 3, right = 1 < 3 → True (loop starts)
        
        # --- Iteration 1: left = 0, right = 1 ---
        # Calculate the difference between elements at right and left pointers
        diff = arr[right] - arr[left]       # arr[1] = 3, arr[0] = 1, diff = 3 - 1 = 2
        
        # Check if the difference equals the target
        if diff == target:                  # diff = 2, target = 2, 2 == 2 → True
            return [arr[left], arr[right]]  # Return [arr[0], arr[1]] = [1, 3]
        
        # If difference is less than target, increase the difference
        elif diff < target:                 # Skip (diff == target, elif not executed)
            right += 1                      # Skip
        
        # If difference is greater than target, decrease the difference
        else:                               # Skip (diff == target, else not executed)
            left += 1                       # Skip
            # Ensure left and right don't point to the same element
            if left == right:               # Skip
                right += 1                  # Skip
        # After Iteration 1: Function returns [1, 3]
        # Current pair checked: (1, 3), diff = 2 (matches target)
        # Loop terminates early due to return

    # 4️⃣ Return None if no pair is found
    return None                         # Skip (not reached due to early return)
    # Conclusion: Pair [1, 3] satisfies the target difference

print(find_pair_with_difference([1, 3, 8], 2))  # Output: [1, 3]
