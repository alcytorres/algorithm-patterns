# Check if a String is a Palindrome
# Example 1: Given a string s, return true if it is a palindrome, false otherwise.

# Checks if string s is a palindrome by comparing characters from both ends.
def is_palindrome(s):
    left = 0                    
    right = len(s) - 1          

    while left < right:         
        if s[left] != s[right]: 
            return False
        left += 1               
        right -= 1             

    return True                

print(is_palindrome("racecar"))  # Output: True

# Time: O(n) - Checks up to n/2 character pairs in a string of length n, with O(1) comparisons per iteration.
# Space: O(1) - Uses only two integer pointers (left, right), with no additional data structures.



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown

def is_palindrome(s):
    left = 0                    # Start left pointer at index 0
    right = len(s) - 1          # Start right pointer at last index

    while left < right:         # Continue until pointers meet
        if s[left] != s[right]: # If characters don't match, not a palindrome
            return False
        left += 1               # Move left pointer inward
        right -= 1              # Move right pointer inward

    return True                 # String is a palindrome



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Task: Check if a string is a palindrome (reads the same forward and backward).
# Example: s = "racecar" → Output = True (same when reversed)
# Why: Practices two-pointer technique to efficiently compare characters from both ends.

def is_palindrome(s):  # Example: s = "racecar"

    # 1️⃣ Initialize pointers
    # Start left pointer at the beginning of the string
    # Why? We need to compare characters from the start moving inward
    left = 0  # left = 0

    # Start right pointer at the end of the string
    # Why? We compare with characters from the end moving inward
    right = len(s) - 1  # len(s) = 7, right = 7 - 1 = 6

    # 2️⃣ Compare characters while pointers don't meet
    # Continue until left pointer is less than right pointer
    # Why? Once pointers meet or cross, we've checked all necessary pairs
    while left < right:  # left = 0, right = 6, 0 < 6 is true
        # --- Iteration 1 ---
        # Check if characters at left and right pointers differ
        # Why? If they differ, the string is not a palindrome
        if s[left] != s[right]:  # s[0] = 'r', s[6] = 'r', 'r' != 'r' is false
            return False  # skip
        # Move pointers inward
        # Why? We check the next pair of characters
        left += 1  # left = 0 + 1 = 1
        right -= 1  # right = 6 - 1 = 5
        # After Iteration 1: left = 1, right = 5
        # Current pair: s[1] = 'a', s[5] = 'a'

        # --- Iteration 2 ---
        if left == 1 and right == 5:
            if s[left] != s[right]:  # s[1] = 'a', s[5] = 'a', 'a' != 'a' is false
                return False
            left += 1  # left = 1 + 1 = 2
            right -= 1  # right = 5 - 1 = 4
            # After Iteration 2: left = 2, right = 4
            # Current pair: s[2] = 'c', s[4] = 'c'

        # --- Iteration 3 ---
        if left == 2 and right == 4:
            if s[left] != s[right]:  # s[2] = 'c', s[4] = 'c', 'c' != 'c' is false
                return False
            left += 1  # left = 2 + 1 = 3
            right -= 1  # right = 4 - 1 = 3
            # After Iteration 3: left = 3, right = 3
            # Loop exits: left = 3, right = 3, 3 < 3 is false

    # 3️⃣ Return True
    # Why? If we exit the loop, all checked pairs matched, so the string is a palindrome
    return True  # True


print(is_palindrome("racecar"))  # Output: True