# 3. Longest Substring with At Most K Vowels
"""
Task: Find the length of the longest substring with at most k vowels.
Example: "aeiou", k=2 → "ae"
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


print(longest_substring_with_k_vowels("aeiou", 2))  # Output: 2


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
print(longest_substring_with_k_vowels("aeiou", 2))  # Output: 2


# ----------------------------------------------------------------------------------
# Solution with output for longest_substring_with_k_vowels
def longest_substring_with_k_vowels(s, k):      # s = "aeiou", k = 2
    vowels = set('aeiou')                       # vowels = {'a', 'e', 'i', 'o', 'u'}
    max_length = 0                              # max_length = 0
    vowel_count = 0                             # vowel_count = 0
    left = 0                                    # left = 0
    for right in range(len(s)):                 # range(5) → right = 0, 1, 2, 3, 4
        if s[right] in vowels:                  # right = 0: 'a' in vowels → True
                                                # right = 1: 'e' in vowels → True
                                                # right = 2: 'i' in vowels → True
                                                # right = 3: 'o' in vowels → True
                                                # right = 4: 'u' in vowels → True
            vowel_count += 1                    # right = 0: vowel_count = 1
                                                # right = 1: vowel_count = 2
                                                # right = 2: vowel_count = 3
                                                # right = 3: vowel_count = 2
                                                # right = 4: vowel_count = 3
        while vowel_count > k and left <= right:  # right = 0: 1 > 2 → False
                                                  # right = 1: 2 > 2 → False
                                                  # right = 2: 3 > 2 and 0 ≤ 2 → True
                                                  # right = 3: 2 > 2 → False
                                                  # right = 4: 3 > 2 and 1 ≤ 4 → True
            if s[left] in vowels:                 # right = 2: s[0] = 'a' in vowels → True
                                                  # right = 4: s[1] = 'e' in vowels → True
                vowel_count -= 1                  # right = 2: vowel_count = 2
                                                  # right = 4: vowel_count = 2
            left += 1                             # right = 2: left = 1
                                                  # right = 4: left = 2
        max_length = max(max_length, right - left + 1)  # right = 0: max(0, 0-0+1) = 1
                                                        # right = 1: max(1, 1-0+1) = 2
                                                        # right = 2: max(2, 2-1+1) = 2
                                                        # right = 3: max(2, 3-1+1) = 3
                                                        # right = 4: max(3, 4-2+1) = 3
    return max_length                               # Return 2

print(longest_substring_with_k_vowels("aeiou", 2))  # Output: 2 (e.g., "ae" with 2 vowels)

