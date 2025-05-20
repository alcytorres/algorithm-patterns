def longest_substring_with_k_vowels(s, k):

    # 1️⃣ Initialize pointers & tracking variables
    vowels = set('aeiou')
    max_length = 0
    vowel_count = 0
    left = 0

    # 2️⃣ Expand window by moving `right` & process characters
    for right in range(len(s)):
        if s[right] in vowels:
            vowel_count += 1

        # 3️⃣ Shrink window if vowel count exceeds k
        while vowel_count > k and left <= right:
            if s[left] in vowels:
                vowel_count -= 1
            left += 1

        # 4️⃣ Update the longest substring length
        max_length = max(max_length, right - left + 1)

    # 5️⃣ Return the longest substring length
    return max_length


print(longest_substring_with_k_vowels("aet", 1))  # Output: 2
# Longest substring with at most 1 vowel is "et" (length 2).

print(longest_substring_with_k_vowels("ae", 1))  # Output: 1
# Longest substring with at most 1 vowel is "a" or "e" (length 1).

print(longest_substring_with_k_vowels("banana", 2))  # Output: 5
# Longest substring with at most 2 vowels is "banan" (length 5).

print(longest_substring_with_k_vowels("xyz", 1))  # Output: 3
# Longest substring with at most 1 vowel is "xyz" (length 3).

print(longest_substring_with_k_vowels("aabbcc", 1))  # Output: 5
# Longest substring with at most 1 vowel is "abbcc" (length 5).


def longest_substring_with_k_vowels(s, k):

    # 1️⃣ Initialize pointers & tracking variables
    vowels = set('aeiou')
    max_length = 0
    vowel_count = 0
    left = 0

    # 2️⃣ Expand window by moving `right` & process characters
    for right in range(len(s)):
        if s[right] in vowels:
            vowel_count += 1

        # 3️⃣ Shrink window if vowel count exceeds k
        while vowel_count > k and left <= right:
            if s[left] in vowels:
                vowel_count -= 1  # Reduce count when removing a vowel
            left += 1  # Shrink window

        # 4️⃣ Update the longest substring length
        max_length = max(max_length, right - left + 1)

    # 5️⃣ Return the longest substring length
    return max_length


# print(longest_substring_with_k_vowels("aet", 1))  # Output: 2
# # Longest substring with at most 1 vowel is "et" (length 2).

# print(longest_substring_with_k_vowels("ae", 1))  # Output: 1
# # Longest substring with at most 1 vowel is "a" or "e" (length 1).

# print(longest_substring_with_k_vowels("banana", 2))  # Output: 5
# # Longest substring with at most 2 vowels is "banan" (length 5).

# print(longest_substring_with_k_vowels("xyz", 1))  # Output: 3
# # Longest substring with at most 1 vowel is "xyz" (length 3).

# print(longest_substring_with_k_vowels("aabbcc", 1))  # Output: 5
# # Longest substring with at most 1 vowel is "abbcc" (length 5).