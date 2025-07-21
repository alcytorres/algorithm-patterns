# 344. Reverse String

# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
 
# Solution: https://leetcode.com/problems/reverse-string/editorial/

def reverseString(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    
    return s

string = ["h","e","l","l","o"]
print(reverseString(string))  # Output: ["o","l","l","e","h"]

# Time: O(n) - Performs n/2 swaps for an array of length n, with each swap being O(1).
# Space: O(1) - Uses only two integer pointers (left, right), modifying the input array in-place with no additional data structures.


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Shortcut solution

def reverseString(s):
    s.reverse    
    return s

string = ["h","e","l","l","o"]
print(reverseString(string))  # Output: ["o","l","l","e","h"]

# Time: O(n) - Python's list.reverse() method processes n elements, performing n/2 swaps internally, each O(1).
# Space: O(1) - Modifies the input array in-place, using only a constant amount of auxiliary space for internal operations.



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
def reverseString(s):
    left = 0                 # Initialize left pointer at start of list
    right = len(s) - 1       # Initialize right pointer at end of list
    
    while left < right:               # Continue until pointers meet
        s[left], s[right] = s[right], s[left]  # Swap elements at left and right pointers
        left += 1                     # Move left pointer inward
        right -= 1                    # Move right pointer inward
    
    return s                          # Return the reversed list

# Complexity
# Time: O(n) - Performs n/2 swaps to reverse n elements.
# Space: O(1) - Uses two pointers, modifying list in-place.

# Output: ["o","l","l","e","h"] - Returns the list with characters reversed in-place.


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Task: Reverse a string (given as an array of characters) in-place using O(1) extra memory.
# Example: s = ["h", "e", "l", "l", "o"] → Output = ["o", "l", "l", "e", "h"]
# Why: Practices two-pointer technique for in-place array manipulation.

def reverseString(s):  # Example: s = ["h", "e", "l", "l", "o"]

    # 1️⃣ Initialize pointers
    # Start left pointer at the beginning of the array
    # Why? We swap characters from the start toward the middle
    left = 0  # left = 0

    # Start right pointer at the end of the array
    # Why? We swap characters from the end toward the middle
    right = len(s) - 1  # len(s) = 5, right = 5 - 1 = 4

    # 2️⃣ Swap characters while pointers don't meet
    # Continue until left pointer is less than right pointer
    # Why? Once pointers meet or cross, the array is fully reversed
    while left < right:  # left = 0, right = 4, 0 < 4 is true
        # --- Iteration 1 ---
        # Swap characters at left and right pointers
        # Why? To reverse the string, we exchange characters from both ends
        s[left], s[right] = s[right], s[left]  # s[0] = "h", s[4] = "o"
                                               # Swap: s[0] = "o", s[4] = "h"
        # Move pointers inward
        # Why? We process the next pair of characters
        left += 1  # left = 0 + 1 = 1
        right -= 1  # right = 4 - 1 = 3
        # After Iteration 1: left = 1, right = 3, s = ["o", "e", "l", "l", "h"]
        # Current pair: s[1] = "e", s[3] = "l"

        # --- Iteration 2 ---
        if left == 1 and right == 3:
            s[left], s[right] = s[right], s[left]  # s[1] = "e", s[3] = "l"
                                                   # Swap: s[1] = "l", s[3] = "e"
            left += 1  # left = 1 + 1 = 2
            right -= 1  # right = 3 - 1 = 2
            # After Iteration 2: left = 2, right = 2, s = ["o", "l", "l", "e", "h"]
            # Loop exits: left = 2, right = 2, 2 < 2 is false

    # 3️⃣ Return the reversed array
    # Why? The array has been modified in-place to be reversed
    return s  # s = ["o", "l", "l", "e", "h"]


string = ["h", "e", "l", "l", "o"]
print(reverseString(string))  # Output: ["o", "l", "l", "e", "h"]