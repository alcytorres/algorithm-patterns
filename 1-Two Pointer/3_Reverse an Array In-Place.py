# 3. Reverse an Array In-Place 
"""
Task: Reverse an array using two pointers without extra space.
Example: [1, 2, 3] → [3, 2, 1]

Why: Builds intuition for swapping elements with pointers, relevant to Valid Palindrome. 
"""

def reverse_array(arr):
    # 1️⃣ Initialize pointers for swapping elements
    left, right = 0, len(arr) - 1   

    # 2️⃣ Loop to swap elements from both ends
    while left < right:             
        arr[left], arr[right] = arr[right], arr[left]  
        left += 1                   
        right -= 1    

    # 3️⃣ Return the reversed array              
    return arr                      

print(reverse_array([1, 2, 3]))  # Output: [3, 2, 1]
print(reverse_array([1, 2, 3, 4]))  # Output: [4, 3, 2, 1]
print(reverse_array([10]))  # Output: [10]
print(reverse_array([]))  # Output: []


# Simple Beakdown
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
# Solution with output Full Breakdown 

def reverse_array(arr):              # Example: arr = [1, 2, 3]

    # 1️⃣ Initialize pointers for swapping elements
    # Set left pointer to the start and right pointer to the end of the array
    # Why? We'll swap elements from the outer ends and move inward
    left, right = 0, len(arr) - 1    # len(arr) = 3, so left = 0, right = 3 - 1 = 2
    # After initialization: left points to arr[0] = 1, right points to arr[2] = 3

    # 2️⃣ Loop to swap elements from both ends
    # Continue while left pointer is less than right pointer
    # Why? We swap elements until the pointers meet in the middle
    while left < right:              # left = 0, right = 2, 0 < 2 → True (loop starts)
        
        # --- Iteration 1: left = 0, right = 2 ---
        # Swap the elements at left and right pointers
        # Why? This reverses the positions of elements at the current ends
        arr[left], arr[right] = arr[right], arr[left]  # arr[0] = 1, arr[2] = 3
                                                       # Swap: arr[0] = 3, arr[2] = 1
                                                       # arr = [3, 2, 1]
        
        # Move pointers inward
        # Why? We process the next pair of elements closer to the center
        left += 1                    # left = 0 + 1 = 1
        right -= 1                   # right = 2 - 1 = 1
        # After Iteration 1: left = 1 (points to arr[1] = 2), right = 1 (points to arr[1] = 2)
        # Current array: [3, 2, 1]
        # Elements swapped: arr[0] and arr[2]

        # --- Iteration 2: left = 1, right = 1 ---
        if left < right:             # left = 1, right = 1, 1 < 1 → False (loop ends)
            pass                     # No further iterations (included for completeness)

    # 3️⃣ Return the reversed array
    # Why? The array has been modified in-place, and all necessary swaps are complete
    return arr                       # Return arr = [3, 2, 1]
    # Final state: Array fully reversed, all pairs swapped
    # Conclusion: Array [1, 2, 3] reversed to [3, 2, 1]

print(reverse_array([1, 2, 3]))      # Output: [3, 2, 1]


# ----------------------------------------------------------------------------------
# Solution with output 

def reverse_array(arr):              # Example: arr = [1, 2, 3, 4]

    # 1️⃣ Initialize pointers for swapping elements
    left, right = 0, len(arr) - 1    # len(arr) = 4, so left = 0, right = 4 - 1 = 3
    # After initialization: left points to arr[0] = 1, right points to arr[3] = 4

    # 2️⃣ Loop to swap elements from both ends
    # Continue while left pointer is less than right pointer
    while left < right:              # left = 0, right = 3, 0 < 3 → True (loop starts)
        
        # --- Iteration 1: left = 0, right = 3 ---
        arr[left], arr[right] = arr[right], arr[left]  # arr[0] = 1, arr[3] = 4
                                                       # Swap: arr[0] = 4, arr[3] = 1
                                                       # arr = [4, 2, 3, 1]
        left += 1                    # left = 0 + 1 = 1
        right -= 1                   # right = 3 - 1 = 2
        # After Iteration 1: left = 1 (points to arr[1] = 2), right = 2 (points to arr[2] = 3)
        # Current array: [4, 2, 3, 1]
        # Elements swapped: arr[0] and arr[3]

        # --- Iteration 2: left = 1, right = 2 ---
        if left < right:             # left = 1, right = 2, 1 < 2 → True
            arr[left], arr[right] = arr[right], arr[left]  # arr[1] = 2, arr[2] = 3
                                                           # Swap: arr[1] = 3, arr[2] = 2
                                                           # arr = [4, 3, 2, 1]
            left += 1                # left = 1 + 1 = 2
            right -= 1               # right = 2 - 1 = 1
            # After Iteration 2: left = 2 (points to arr[2] = 2), right = 1 (points to arr[1] = 3)
            # Current array: [4, 3, 2, 1]
            # Elements swapped: arr[1] and arr[2]

        # --- Iteration 3: left = 2, right = 1 ---
        if left < right:             # left = 2, right = 1, 2 < 1 → False (loop ends)
            pass                     # No further iterations (included for completeness)

    # 3️⃣ Return the reversed array
    return arr                       # Return arr = [4, 3, 2, 1]

print(reverse_array([1, 2, 3, 4]))   # Output: [4, 3, 2, 1] (reversed array)
