# 7.1 Finding a Pair with Target Sum

"""
Task: Given an array of integers and a target value, find two numbers that add up to the target. Return the pair as a list. If no pair exists return None.

Example: [2, 10, 5, 15], target = 7 → [2, 5] (since 2 + 5 = 7)

Why: Practices two-pointer technique on sorted data, similar to Find Pair with Target Difference and Merge Sorted Arrays.
"""

def find_pair_with_target_sum(arr, target):
    # 1️⃣ Sort the array
    arr.sort()   

    # 2️⃣ Initialize two pointers                
    left, right = 0, len(arr) - 1 

    # 3️⃣ Loop through the array to find the pair        
    while left < right:      
        current_sum = arr[left] + arr[right]
        if current_sum == target:       
            return [arr[left], arr[right]]  
        elif current_sum < target:      
            left += 1           
        else:                   
            right -= 1            

    # 4️⃣ Return None if no pair is found
    return None       

print(find_pair_with_target_sum([1, 5, 4, 10], 15))  # Output: [5, 10]


"""
Why while left < right:?
    
    The while left < right: ensures left and right pointers don’t meet or cross, so we always check pairs of different elements in the sorted array.
"""


# ----------------------------------------------------------------------------------
# 7.2 Valid Palindrome Check
"""
Task: Determine if a given string is a palindrome (reads the same forward and backward). Consider exact characters (no case or space handling for simplicity).

Example: "level" → True, 
Example: "abba" → True, 
Example: "abc" → False

Why: Practices two-pointer technique from both ends, similar to Reverse Array and Find Pair with Target Difference.
"""

def is_palindrome(s):
    # 1️⃣ Handle edge cases: empty or single-character strings are palindromes
    if len(s) < 2:
        return True
    
    # 2️⃣ Initialize pointers for comparing characters from both ends
    left, right = 0, len(s) - 1
    
    # 3️⃣ Loop to compare characters from both ends
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    # 4️⃣ Return True if all characters match
    return True

print(is_palindrome("abba"))  # Output: True



"""
Why if s[left] != s[right]:?

This line checks if characters at left and right pointers differ. If they do, the string isn’t a palindrome, so we return False.

    Why needed: Palindromes require exact matches from both ends. != spots any mismatch to fail fast.

    Why this check: Problem demands exact character comparison (e.g., "abba" needs a == a). != is simplest to detect failure.

    Why not others: Direct inequality check avoids extra logic for mismatches.

The focus on exact matching signals != for quick, clear validation.
"""

# ----------------------------------------------------------------------------------


