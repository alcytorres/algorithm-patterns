# longest_unique_substring.py

"""
# Longest Substring with At Most K Distinct Characters
Task: Given a string s and an integer k, find the length of the longest substring that contains at most k distinct characters. If the string is empty or k is 0, return 0.

Example 1: s = "eceba", k = 2 → 3 (substring "ece" has 2 distinct characters: 'e', 'c')

Example 2: s = "aa", k = 1 → 2 (substring "aa" has 1 distinct character: 'a')

Example 3: s = "aabbcc", k = 2 → 4 (substring "aabb" or "bbcc" has 2 distinct characters: 'a', 'b' or 'b', 'c')

    Generic dynamic sliding-window template.
    - arr: list of ints (or chars, as numbers)
    - K: problem parameter (e.g. target sum, max distinct count, etc.)
    Returns:
    - result: depends on problem (max window length, min window length, count, sum, etc.)
"""

# Test cases
print(longest_substring_k_distinct("eceba", 2))    # Output: 3
print(longest_substring_k_distinct("aa", 1))       # Output: 2
print(longest_substring_k_distinct("aabbcc", 2))   # Output: 4



def length_of_longest_substring(s):
  
    # 1️⃣ Initialize pointers & tracking variables
    left = 0
    max_len = 0
    char_count = {}  # freq map: char → how many times it appears in window

    # 2️⃣ Expand window by moving `right`
    for right in range(len(s)):
        current_char = s[right]
        # └── include s[right] in our window
        char_count[current_char] = char_count.get(current_char, 0) + 1

        # 3️⃣ Shrink window while it’s invalid (we have a duplicate)
        while char_count[current_char] > 1:
            # └── remove s[left] before we move left forward
            left_char = s[left]
            char_count[left_char] -= 1
            left += 1

        # 4️⃣ Update result for a max-length problem
        window_len = right - left + 1
        if window_len > max_len:
            max_len = window_len

    # 5️⃣ Return final answer
    return max_len


print(length_of_longest_substring("abcabccc"))  # Output: 3 ("abc")
print(length_of_longest_substring("aa"))        # Output: 1 ("a")
print(length_of_longest_substring("aabbcc"))    # Output: 2 ("ab" or "bc")
print(length_of_longest_substring("eceba"))     # Output: 4 ("ceba")




