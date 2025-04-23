# 3. Longest Substring with At Most K Vowels
"""
Task: Find the length of the longest substring with at most k vowels.

Find the length of the longest continuous chunk of a string that has no more than k vowels (a, e, i, o, u).

Example 1: "ae", k=1 → 1 (longest substring with at most 1 vowel is "a" or "e")
Example 2: "oa", k=1 → 1 (longest substring with at most 1 vowel is "o" or "a").
Example 3: "aet", k=1 → 2 (longest substring with at most 1 vowel is "et").
Why: Introduces dynamic window adjustments.
"""

def longest_substring_with_k_vowels(s, k):
    vowels = set('aeiou')
    max_length = 0
    vowel_count = 0
    left = 0
    for right in range(len(s)):
        if s[right] in vowels:
            vowel_count += 1
        while vowel_count > k and left <= right:
            if s[left] in vowels:
                vowel_count -= 1  # Reduce count when removing a vowel
            left += 1  # Shrink window
        max_length = max(max_length, right - left + 1)
    return max_length


print(longest_substring_with_k_vowels("ae", 1))  # Output: 1


# Solution
def longest_substring_with_k_vowels(s, k):   # Define the function that takes a string 's' and integer 'k'
    """
    Finds the longest substring with at most k vowels.
    
    - Uses a sliding window to track vowel count and adjust window size.
    - Time Complexity: O(n), Space Complexity: O(1).
    - Beginner-friendly with clear window adjustment logic.
    """
    vowels = set('aeiou')  # Create a set of vowels for quick checking
    max_length = 0         # Initialize the maximum length of a valid substring
    vowel_count = 0        # Track the number of vowels in the current window
    left = 0               # Set the left pointer of the window to the start
    for right in range(len(s)):  # Loop through the string with the right pointer
        if s[right] in vowels:   # If the current character is a vowel
            vowel_count += 1     # Increase the vowel count
        while vowel_count > k and left <= right:  # If we have more than k vowels, shrink the window
            if s[left] in vowels:  # If the left character is a vowel
                vowel_count -= 1   # Decrease the vowel count
            left += 1            # Move the left pointer one step right
        max_length = max(max_length, right - left + 1)  # Update max_length with the current window size
    return max_length          # Return the length of the longest valid substring

# Test the function
print(longest_substring_with_k_vowels("ae", 1))  # Output: 1


"""
Concise Walkthrough of Why longest_substring_with_k_vowels Works

The longest_substring_with_k_vowels function finds the longest substring in a string with at most k vowels (a, e, i, o, u). Here’s why it works for "ae", k=1, explained simply:

    1. Track Vowels with a Window: It uses two pointers (left and right) to form a sliding window. vowel_count tracks how many vowels are in the window. For "ae", k=1, it starts with vowel_count = 0.
    2. Expand Window: For each right, it checks if s[right] is a vowel (a, e, i, o, u). If yes, it adds 1 to vowel_count. For s[0] = 'a', vowel_count = 1. For s[1] = 'e', vowel_count = 2.
    3. Shrink if Too Many Vowels: If vowel_count > k, it shrinks the window by moving left forward, subtracting 1 from vowel_count if s[left] is a vowel. For s[1] = 'e', vowel_count = 2 > 1, so it removes s[0] = 'a', making vowel_count = 1.
    4. Update Longest Length: After each step, it calculates the window length (right - left + 1) and keeps the maximum. For "ae", it checks windows like "a" (length 1) and "e" (length 1 after shrinking), so max_length = 1.
    5. Repeat Until End: It processes all characters, ensuring every valid window (with at most k vowels) is checked. For "ae", no window longer than 1 is valid (e.g., "ae" has 2 vowels).

    Why It Works: The sliding window expands to include new characters and shrinks when there are too many vowels, keeping vowel_count <= k. It tracks the longest valid window found. For "ae", k=1, it correctly identifies single-vowel substrings "a" or "e" (length = 1), returning 1.
"""


# ----------------------------------------------------------------------------------
# Solution with output for longest_substring_with_k_vowels

def longest_substring_with_k_vowels(s, k):      # s = "ae", k = 1
    vowels = set('aeiou')                       # vowels = {'a', 'e', 'i', 'o', 'u'} (set of vowels)
    max_length = 0                              # max_length = 0 (start with no length)
    vowel_count = 0                             # vowel_count = 0 (start with no vowels)
    left = 0                                    # left = 0 (left pointer at start)
    for right in range(len(s)):                 # right = 0 to 1 (len = 2)
                                                # Iteration 1: right = 0
        if s[right] in vowels:                  # Is s[0] = 'a' in {'a', 'e', 'i', 'o', 'u'}? Yes
            vowel_count += 1                    # vowel_count = 0 + 1 = 1
        while vowel_count > k and left <= right:  # Is 1 > 1 and 0 <= 0? No
            if s[left] in vowels:               # skip
                vowel_count -= 1                # skip
            left += 1                           # skip
        max_length = max(max_length, right - left + 1)  # max(0, 0 - 0 + 1) = 1, max_length = 1
                                                # Iteration 2: right = 1
        if s[right] in vowels:                  # Is s[1] = 'e' in {'a', 'e', 'i', 'o', 'u'}? Yes
            vowel_count += 1                    # vowel_count = 1 + 1 = 2
        while vowel_count > k and left <= right:  # Is 2 > 1 and 0 <= 1? Yes
            if s[left] in vowels:               # Is s[0] = 'a' in {'a', 'e', 'i', 'o', 'u'}? Yes
                vowel_count -= 1                # vowel_count = 2 - 1 = 1
            left += 1                           # left = 0 + 1 = 1
        while vowel_count > k and left <= right:  # Is 1 > 1 and 1 <= 1? No
            if s[left] in vowels:               # skip
                vowel_count -= 1                # skip
            left += 1                           # skip
        max_length = max(max_length, right - left + 1)  # max(1, 1 - 1 + 1) = 1, max_length = 1
    return max_length                          # Return 1 (longest substring length)

# Test the function
print(longest_substring_with_k_vowels("ae", 1))  # Output: 1


# ----------------------------------------------------------------------------------
# Solution with output for longest_substring_with_k_vowels

def longest_substring_with_k_vowels(s, k):      # s = "oa", k = 1
    vowels = set('aeiou')                       # vowels = {'a', 'e', 'i', 'o', 'u'} (set of vowels)
    max_length = 0                              # max_length = 0 (start with no length)
    vowel_count = 0                             # vowel_count = 0 (start with no vowels)
    left = 0                                    # left = 0 (left pointer at start)
    for right in range(len(s)):                 # right = 0 to 1 (len = 2)
                                                # Iteration 1: right = 0
        if s[right] in vowels:                  # Is s[0] = 'o' in {'a', 'e', 'i', 'o', 'u'}? Yes
            vowel_count += 1                    # vowel_count = 0 + 1 = 1
        while vowel_count > k and left <= right:  # Is 1 > 1 and 0 <= 0? No
            if s[left] in vowels:               # skip
                vowel_count -= 1                # skip
            left += 1                           # skip
        max_length = max(max_length, right - left + 1)  # max(0, 0 - 0 + 1) = 1, max_length = 1
                                                # Iteration 2: right = 1
        if s[right] in vowels:                  # Is s[1] = 'a' in {'a', 'e', 'i', 'o', 'u'}? Yes
            vowel_count += 1                    # vowel_count = 1 + 1 = 2
        while vowel_count > k and left <= right:  # Is 2 > 1 and 0 <= 1? Yes
            if s[left] in vowels:               # Is s[0] = 'o' in {'a', 'e', 'i', 'o', 'u'}? Yes
                vowel_count -= 1                # vowel_count = 2 - 1 = 1
            left += 1                           # left = 0 + 1 = 1
        while vowel_count > k and left <= right:  # Is 1 > 1 and 1 <= 1? No
            if s[left] in vowels:               # skip
                vowel_count -= 1                # skip
            left += 1                           # skip
        max_length = max(max_length, right - left + 1)  # max(1, 1 - 1 + 1) = 1, max_length = 1
    return max_length                          # Return 1 (longest substring length)


print(longest_substring_with_k_vowels("oa", 1))  # Output: 1



# # ----------------------------------------------------------------------------------
# # Solution with output for longest_substring_with_k_vowels

def longest_substring_with_k_vowels(s, k):      # s = "aet", k = 1
    vowels = set('aeiou')                       # vowels = {'a', 'e', 'i', 'o', 'u'} (set of vowels)
    max_length = 0                              # max_length = 0 (start with no length)
    vowel_count = 0                             # vowel_count = 0 (start with no vowels)
    left = 0                                    # left = 0 (left pointer at start)
    for right in range(len(s)):                 # right = 0 to 2 (len = 3)
                                                # Iteration 1: right = 0
        if s[right] in vowels:                  # Is s[0] = 'a' in {'a', 'e', 'i', 'o', 'u'}? Yes
            vowel_count += 1                    # vowel_count = 0 + 1 = 1
        while vowel_count > k and left <= right:  # Is 1 > 1 and 0 <= 0? No
            if s[left] in vowels:               # skip
                vowel_count -= 1                # skip
            left += 1                           # skip
        max_length = max(max_length, right - left + 1)  # max(0, 0 - 0 + 1) = 1, max_length = 1
                                                # Iteration 2: right = 1
        if s[right] in vowels:                  # Is s[1] = 'e' in {'a', 'e', 'i', 'o', 'u'}? Yes
            vowel_count += 1                    # vowel_count = 1 + 1 = 2
        while vowel_count > k and left <= right:  # Is 2 > 1 and 0 <= 1? Yes
            if s[left] in vowels:               # Is s[0] = 'a' in {'a', 'e', 'i', 'o', 'u'}? Yes
                vowel_count -= 1                # vowel_count = 2 - 1 = 1
            left += 1                           # left = 0 + 1 = 1
        while vowel_count > k and left <= right:  # Is 1 > 1 and 1 <= 1? No
            if s[left] in vowels:               # skip
                vowel_count -= 1                # skip
            left += 1                           # skip
        max_length = max(max_length, right - left + 1)  # max(1, 1 - 1 + 1) = 1, max_length = 1
                                                # Iteration 3: right = 2
        if s[right] in vowels:                  # Is s[2] = 't' in {'a', 'e', 'i', 'o', 'u'}? No
            vowel_count += 1                    # skip
        while vowel_count > k and left <= right:  # Is 1 > 1 and 1 <= 2? No
            if s[left] in vowels:               # skip
                vowel_count -= 1                # skip
            left += 1                           # skip
        max_length = max(max_length, right - left + 1)  # max(1, 2 - 1 + 1) = 2, max_length = 2
    return max_length                          # Return 2 (longest substring length)


print(longest_substring_with_k_vowels("aet", 1))  # Output: 2
