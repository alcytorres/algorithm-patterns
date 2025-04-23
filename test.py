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