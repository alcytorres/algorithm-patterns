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

print(reverse_array([1, 2, 3]))  # Output: [3, 2, 1]


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
# Solution with output 

def reverse_array(arr):                       # arr = [1, 2, 3]
    left, right = 0, len(arr) - 1             # left = 0, right = 3 - 1 = 2
    while left < right:                       # 0 < 2 → True (loop runs)
        arr[left], arr[right] = arr[right], arr[left]  # arr[0], arr[2] = arr[2], arr[0] → arr = [3, 2, 1]
        left += 1                             # left = 1
        right -= 1                            # right = 1
                                              # Iteration 2: left < right → 1 < 1 → False (loop ends)
    return arr                                # Return arr = [3, 2, 1]

print(reverse_array([1, 2, 3]))  # Output: [3, 2, 1] (reversed array)


# ----------------------------------------------------------------------------------
# Solution with output 

def reverse_array(arr):                     # arr = [1, 2, 3, 4]
    left, right = 0, len(arr) - 1           # left = 0, right = 4 - 1 = 3
    while left < right:                     # 0 < 3 → True (loop runs)
        arr[left], arr[right] = arr[right], arr[left]  # arr[0], arr[3] = arr[3], arr[0] → arr = [4, 2, 3, 1]
        left += 1                           # left = 1
        right -= 1                          # right = 2
                                            # Iteration 2: left < right → 1 < 2 → True
                                            # arr[1], arr[2] = arr[2], arr[1] → arr = [4, 3, 2, 1]
                                            # left = 2
                                            # right = 1
                                            # Iteration 3: left < right → 2 < 1 → False (loop ends)
    return arr                              # Return arr = [4, 3, 2, 1]

print(reverse_array([1, 2, 3, 4]))  # Output: [4, 3, 2, 1] (reversed array)

