# 125. Valid Palindrome
"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
 
Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.
 
Constraints:
    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.

https://leetcode.com/problems/valid-palindrome/description/
"""

# Simple Palindrome Check (Build String → Two Pointers)
def is_palindrome(s):
    new_string = ""
    
    for c in s:
        if c.isalpha() or c.isdigit():
            new_string += c.lower()  
    
    # Check if the new string reads the same forwards and backwards
    l = 0
    r = len(new_string) - 1
    
    while l < r:
        if new_string[l] != new_string[r]:
            return False
        l += 1
        r -= 1
        
    return True

s = "A man, a plan, a canal: Panama"
print(is_palindrome(s))  # Output: True


# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
def is_palindrome(s):
    # Step 1: Create a new string with only letters and numbers, all lowercase
    new_string = ""    # Empty string to store valid chars
    
    for c in s:        # Go through every character in string
        if c.isalpha() or c.isdigit():  # if it's a letter or number
            new_string += c.lower()     # make it lowercase and add
    

    # Step 2: Check if the new string reads the same forwards and backwards
    left = 0                      # Pointer starting from beginning
    right = len(new_string) - 1   # Pointer starting from end
    
    while left < right:    # Continue until pointers meet
        if new_string[left] != new_string[right]:   # If characters don't match
            return False    # Not a palindrome
        left += 1           # Move left pointer right
        right -= 1          # Move right pointer left
        
    return True     # All pairs matched → it's a palindrome

"""
Time: O(N)
  - Let N = length of the original string s.
  - Step 1: Build a cleaned, lowercase string by scanning s once → O(N).
      • Checking c.isalpha() / isdigit() is O(1).
      • Appending with new_string = new_string + c is technically O(N) each time (strings are immutable),
        but for complexity study we treat this as O(N) total if rewritten with a list.
  - Step 2: Two-pointer palindrome check scans the cleaned string once → O(N).
  - Overall: O(N).

Space: O(N)
  - new_string stores all alphanumeric characters from s → up to N characters.
  - Two pointer variables use O(1).
  - Overall: O(N).

  
Interview Answer: Worst Case

Time: O(N)
  - Clean the string and check with two pointers.

Space: O(N)
  - Need space to store the filtered version of the string.


---
Overview for Each Iteration
Input: s = "A man, a plan, a canal: Panama"

Step 1: Build cleaned string (alphanumeric + lowercase)
c            | isalpha/isnum | c.lower() | new_string
-------------|---------------|-----------|--------------------
A            | Yes           | a         | "a"
(space)      | No            | —         | "a"
m            | Yes           | m         | "am"
a            | Yes           | a         | "ama"
n            | Yes           | n         | "aman"
,            | No            | —         | "aman"
...          | ...           | ...       | → continues
a            | Yes           | a         | "amanaplanacanalpanama"

Final cleaned: "amanaplanacanalpanama

Step 2: Two-pointer validation
left | right | char left | char right | match? | Action
-----|-------|-----------|------------|--------|-----------
0    | 20    | a         | a          | Yes    | left++, right--
1    | 19    | m         | m          | Yes    | left++, right--
2    | 18    | a         | a          | Yes    | left++, right--
...  | ...   | ...       | ...        | Yes    | continue
10   | 10    | n         | n          | —      | left ≥ right → exit

Final: True



---
Most IMPORTANT thing to Understand:
    • A palindrome must read the same forward and backward *after* we remove non-alphanumeric characters.

    • We build a cleaned lowercase string containing only letters and digits.

    • Then we use two pointers (left & right) to compare characters from both ends toward the center.

---
Why this code Works:
    • Data cleaning: Removing punctuation and spaces ensures we compare only meaningful characters.

    • Two-pointer technique: left and right move inward and check mirrored positions.

    • If any mismatch occurs → not a palindrome.  
      If we finish with all matches → it *is* a palindrome.

    • Efficiency: One pass to clean, one pass to compare → O(N) time.

---
TLDR:
    • Clean the string to letters/digits only, then compare characters from both ends inward.

---
Quick Example Walkthrough:

    s = "A man, a plan, a canal: Panama"

    Cleaned string:
        "amanaplanacanalpanama"

    Comparison:
        a == a
        m == m
        a == a
        n == n
        a == a
        p == p
        l == l
        a == a
        n == n
        a == a
        c == c
        ... pointers meet in the middle with all matches

    Final → True


"""










# def is_palindrome(s):
#     # Step 1: Build a clean string with only letters and digits
#     clean = ""
#     for char in s:
#         if char.isalnum():          # keep only letters + numbers
#             clean += char.lower()   # make everything lowercase

#     # Step 2: Use two pointers to check if clean string is a palindrome
#     left = 0
#     right = len(clean) - 1

#     while left < right:
#         if clean[left] != clean[right]:
#             return False   # mismatch → not a palindrome

#         left += 1
#         right -= 1

#     return True  # if we never found a mismatch, it's a palindrome

# s = "A man, a plan, a canal: Panama"
# print(is_palindrome(s))
