# Template 1: Two Pointers from Opposite Ends
def two_pointer_opposite(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
    # Process the pair (arr[left], arr[right]).
    # For example, compare sum to target, or check if they match some condition.
    # if <some condition based on arr[left] and arr[right]>:
    # Maybe return True/indices or record the result.
        return (left, right)
    elif <condition to move left pointer>:
        left += 1 # Move left pointer to the right
    else:
        right -= 1 # Move right pointer to the left
    # If we exit the loop, either we found a result or there is no valid pair.
    return None



# Template 2: Two Pointers moving in the Same Direction
def two_pointer_same_direction(arr):
    i = 0
    # j will move from 0 to n-1 (or 1 to n-1 if i starts at 0)
    for j in range(len(arr)):
    # Use j to explore and i to build or compare
    if <some condition involving arr[j] (and maybe arr[i])>:
    # If condition met, update arr[i] or record result
    arr[i] = arr[j] # (for example, keep this element)
    i += 1 # move the slow pointer
    # After loop, first i elements of arr might be the result,
    # or use i as a count of valid elements.
    return i


# ----------------------------------------------------------------------------------
# Finding a Pair with Target Sum

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
# Valid Palindrome Check
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
    if s[left] != s[right]:
        return False
    left += 1
    right -= 1
    
    # 4️⃣ Return True if all characters match
    return True

print(is_palindrome("abba"))



"""
Why if s[left] != s[right]:?

This line checks if characters at left and right pointers differ. If they do, the string isn’t a palindrome, so we return False.

    Why needed: Palindromes require exact matches from both ends. != spots any mismatch to fail fast.

    Why this check: Problem demands exact character comparison (e.g., "abba" needs a == a). != is simplest to detect failure.

    Why not others: Direct inequality check avoids extra logic for mismatches.

The focus on exact matching signals != for quick, clear validation.
"""


# ----------------------------------------------------------------------------------


