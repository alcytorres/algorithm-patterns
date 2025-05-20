# 3. Longest Substring with At Most K Vowels
"""
Task: Find the length of the longest continous substring with at most k vowels (a, e, i, o, u).

Find the length of the longest continuous chunk of a string that has no more than k vowels (a, e, i, o, u).

Example 1: "aet"     k=1 → 2 (longest substring with at most 1 vowel is "et").
Example 2: "ae"      k=1 → 1 (longest substring with at most 1 vowel is "a" or "e")
Example 3: "banana"  k=2 → 5 (longest substring with at most 2 vowels is "banan")
Example 4: "xyz"     k=1 → 3 (longest substring with at most 1 vowel is "xyz")
Example 5: "aabbcc"  k=1 → 5 (longest substring with at most 1 vowel is "abbcc")

Why: Introduces dynamic window adjustments.
"""

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


# Solution
def longest_substring_with_k_vowels(s, k):   # Define the function that takes a string 's' and integer 'k'
    """
    Finds the longest substring with at most k vowels.
    
    - Uses a sliding window to track vowel count and adjust window size.
    - Time Complexity: O(n), Space Complexity: O(1).
    - Beginner-friendly with clear window adjustment logic.
    """

    # 1️⃣ Initialize pointers & tracking variables
    vowels = set('aeiou')  # Create a set of vowels for quick checking
    max_length = 0         # Initialize the maximum length of a valid substring
    vowel_count = 0        # Track the number of vowels in the current window
    left = 0               # Set the left pointer of the window to the start

    # 2️⃣ Expand window by moving `right` & process characters
    for right in range(len(s)):  # Loop through the string with the right pointer
        if s[right] in vowels:   # If the current character is a vowel
            vowel_count += 1     # Increase the vowel count

        # 3️⃣ Shrink window if vowel count exceeds k
        while vowel_count > k and left <= right:  # If we have more than k vowels, shrink the window
            if s[left] in vowels:  # If the left character is a vowel
                vowel_count -= 1   # Decrease the vowel count
            left += 1            # Move the left pointer one step right

        # 4️⃣ Update the longest substring length
        max_length = max(max_length, right - left + 1)  # Update max_length with the current window size

    # 5️⃣ Return the longest substring length
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
# Solution with output for longest_substring_with_k_vowels FUll Breakdown

"""
Task: Find the length of the longest continous substring with at most k vowels (a, e, i, o, u).
Example 1: "aet"     k=1 → 2 (longest substring with at most 1 vowel is "et").
"""

def longest_substring_with_k_vowels(s, k):  # Example: s = "aet", k = 1

    # 1️⃣ Initialize pointers & tracking variables
    # Create a set of vowels for quick lookup
    # Why? We need to efficiently check if a character is a vowel
    vowels = set('aeiou')      # vowels = {'a', 'e', 'i', 'o', 'u'}

    # Track the longest substring length with at most k vowels
    # Why? We need to update this as we find longer valid substrings
    max_length = 0             # max_length = 0 (no substring checked yet)

    # Track the number of vowels in the current window
    # Why? We need to ensure the window has at most k vowels
    vowel_count = 0            # vowel_count = 0 (no vowels counted yet)

    # Initialize left pointer for the start of the sliding window
    # Why? We'll move this to shrink the window when we have too many vowels
    left = 0                   # left = 0 (start at beginning)

    # 2️⃣ Expand window by moving `right` & process characters
    # Loop through each character as the right end of our window
    # Why? We check each character to build substrings with at most k vowels
    for right in range(len(s)):  # right goes from 0 to 2 (len("aet") = 3)
        # --- Iteration 0: right = 0, s[0] = 'a' ---
        # Check if the current character is a vowel and increment count if it is
        # Why? We need to track vowels to enforce the k-vowel limit
        if s[right] in vowels:    # s[0] = 'a', 'a' in vowels, true
            vowel_count += 1      # vowel_count = 0 + 1 = 1

        # 3️⃣ Shrink window if vowel count exceeds k
        # While we have too many vowels and the window is valid (left <= right)
        # Why? We need to reduce the vowel count to make the substring valid
        while vowel_count > k and left <= right:  # vowel_count = 1, k = 1, 1 > 1 is false, skip
            # If the leftmost character is a vowel, decrease the count
            # Why? Removing a vowel reduces the vowel count
            if s[left] in vowels:    # skip (condition not met)
                vowel_count -= 1     # skip
            # Move the left pointer forward
            # Why? Shrink the window by excluding the leftmost character
            left += 1                # skip

        # 4️⃣ Update the longest substring length
        # Calculate the current window size
        # Why? This is the length of the current substring with at most k vowels
        max_length = max(max_length, right - left + 1)  # right = 0, left = 0
                                                       # size = (0 - 0) + 1 = 1
                                                       # max_length = max(0, 1) = 1
        # After Iteration 0: vowel_count = 1, left = 0, max_length = 1
        # Current window: "a" (1 vowel, length 1)

        # --- Iteration 1: right = 1, s[1] = 'e' ---
        if right == 1:
            if s[right] in vowels:    # s[1] = 'e', 'e' in vowels, true
                vowel_count += 1      # vowel_count = 1 + 1 = 2

            while vowel_count > k and left <= right:  # vowel_count = 2, k = 1, 2 > 1 is true
                # Check s[left] = s[0] = 'a'
                if s[left] in vowels:    # 'a' in vowels, true
                    vowel_count -= 1     # vowel_count = 2 - 1 = 1
                left += 1                # left = 0 + 1 = 1
                # Check again: vowel_count = 1, k = 1, 1 > 1 is false, exit while

            max_length = max(max_length, right - left + 1)  # right = 1, left = 1
                                                           # size = (1 - 1) + 1 = 1
                                                           # max_length = max(1, 1) = 1
            # After Iteration 1: vowel_count = 1, left = 1, max_length = 1
            # Current window: "e" (1 vowel, length 1)

        # --- Iteration 2: right = 2, s[2] = 't' ---
        if right == 2:
            if s[right] in vowels:    # s[2] = 't', 't' not in vowels, false
                vowel_count += 1      # skip (not a vowel)

            while vowel_count > k and left <= right:  # vowel_count = 1, k = 1, 1 > 1 is false, skip
                if s[left] in vowels:
                    vowel_count -= 1
                left += 1

            max_length = max(max_length, right - left + 1)  # right = 2, left = 1
                                                           # size = (2 - 1) + 1 = 2
                                                           # max_length = max(1, 2) = 2
            # After Iteration 2: vowel_count = 1, left = 1, max_length = 2
            # Current window: "et" (1 vowel, length 2)

    # 5️⃣ Return the longest substring length
    # Why? max_length contains the length of the longest substring with at most k vowels
    return max_length             # max_length = 2


print(longest_substring_with_k_vowels("aet", 1))  # Output: 2
# Longest substring with at most 1 vowel is "et" (length 2)



# ----------------------------------------------------------------------------------
# Solution with output for longest_substring_with_k_vowels

def longest_substring_with_k_vowels(s, k):  # Example: s = "banana", k = 2

    # 1️⃣ Initialize pointers & tracking variables
    # Create a set of vowels for quick lookup
    # Why? We need to efficiently check if a character is a vowel
    vowels = set('aeiou')      # vowels = {'a', 'e', 'i', 'o', 'u'}

    # Track the longest substring length with at most k vowels
    # Why? We need to update this as we find longer valid substrings
    max_length = 0             # max_length = 0 (no substring checked yet)

    # Track the number of vowels in the current window
    # Why? We need to ensure the window has at most k vowels
    vowel_count = 0            # vowel_count = 0 (no vowels counted yet)

    # Initialize left pointer for the start of the sliding window
    # Why? We'll move this to shrink the window when we have too many vowels
    left = 0                   # left = 0 (start at beginning)

    # 2️⃣ Expand window by moving `right` & process characters
    # Loop through each character as the right end of our window
    # Why? We check each character to build substrings with at most k vowels
    for right in range(len(s)):  # right goes from 0 to 5 (len("banana") = 6)
        # --- Iteration 0: right = 0, s[0] = 'b' ---
        # Check if the current character is a vowel and increment count if it is
        # Why? We need to track vowels to enforce the k-vowel limit
        if s[right] in vowels:    # s[0] = 'b', 'b' not in vowels, false
            vowel_count += 1      # skip (not a vowel)

        # 3️⃣ Shrink window if vowel count exceeds k
        # While we have too many vowels and the window is valid (left <= right)
        # Why? We need to reduce the vowel count to make the substring valid
        while vowel_count > k and left <= right:  # vowel_count = 0, k = 2, 0 > 2 is false, skip
            # If the leftmost character is a vowel, decrease the count
            # Why? Removing a vowel reduces the vowel count
            if s[left] in vowels:    # skip (condition not met)
                vowel_count -= 1     # skip
            # Move the left pointer forward
            # Why? Shrink the window by excluding the leftmost character
            left += 1                # skip

        # 4️⃣ Update the longest substring length
        # Calculate the current window size
        # Why? This is the length of the current substring with at most k vowels
        max_length = max(max_length, right - left + 1)  # right = 0, left = 0
                                                       # size = (0 - 0) + 1 = 1
                                                       # max_length = max(0, 1) = 1
        # After Iteration 0: vowel_count = 0, left = 0, max_length = 1
        # Current window: "b" (0 vowels, length 1)

        # --- Iteration 1: right = 1, s[1] = 'a' ---
        if right == 1:
            if s[right] in vowels:    # s[1] = 'a', 'a' in vowels, true
                vowel_count += 1      # vowel_count = 0 + 1 = 1

            while vowel_count > k and left <= right:  # vowel_count = 1, k = 2, 1 > 2 is false, skip
                if s[left] in vowels:
                    vowel_count -= 1
                left += 1

            max_length = max(max_length, right - left + 1)  # right = 1, left = 0
                                                           # size = (1 - 0) + 1 = 2
                                                           # max_length = max(1, 2) = 2
            # After Iteration 1: vowel_count = 1, left = 0, max_length = 2
            # Current window: "ba" (1 vowel, length 2)

        # --- Iteration 2: right = 2, s[2] = 'n' ---
        if right == 2:
            if s[right] in vowels:    # s[2] = 'n', 'n' not in vowels, false
                vowel_count += 1      # skip (not a vowel)

            while vowel_count > k and left <= right:  # vowel_count = 1, k = 2, 1 > 2 is false, skip
                if s[left] in vowels:
                    vowel_count -= 1
                left += 1

            max_length = max(max_length, right - left + 1)  # right = 2, left = 0
                                                           # size = (2 - 0) + 1 = 3
                                                           # max_length = max(2, 3) = 3
            # After Iteration 2: vowel_count = 1, left = 0, max_length = 3
            # Current window: "ban" (1 vowel, length 3)

        # --- Iteration 3: right = 3, s[3] = 'a' ---
        if right == 3:
            if s[right] in vowels:    # s[3] = 'a', 'a' in vowels, true
                vowel_count += 1      # vowel_count = 1 + 1 = 2

            while vowel_count > k and left <= right:  # vowel_count = 2, k = 2, 2 > 2 is false, skip
                if s[left] in vowels:
                    vowel_count -= 1
                left += 1

            max_length = max(max_length, right - left + 1)  # right = 3, left = 0
                                                           # size = (3 - 0) + 1 = 4
                                                           # max_length = max(3, 4) = 4
            # After Iteration 3: vowel_count = 2, left = 0, max_length = 4
            # Current window: "bana" (2 vowels, length 4)

        # --- Iteration 4: right = 4, s[4] = 'n' ---
        if right == 4:
            if s[right] in vowels:    # s[4] = 'n', 'n' not in vowels, false
                vowel_count += 1      # skip (not a vowel)

            while vowel_count > k and left <= right:  # vowel_count = 2, k = 2, 2 > 2 is false, skip
                if s[left] in vowels:
                    vowel_count -= 1
                left += 1

            max_length = max(max_length, right - left + 1)  # right = 4, left = 0
                                                           # size = (4 - 0) + 1 = 5
                                                           # max_length = max(4, 5) = 5
            # After Iteration 4: vowel_count = 2, left = 0, max_length = 5
            # Current window: "banan" (2 vowels, length 5)

        # --- Iteration 5: right = 5, s[5] = 'a' ---
        if right == 5:
            if s[right] in vowels:    # s[5] = 'a', 'a' in vowels, true
                vowel_count += 1      # vowel_count = 2 + 1 = 3

            while vowel_count > k and left <= right:  # vowel_count = 3, k = 2, 3 > 2 is true
                # Check s[left] = s[0] = 'b'
                if s[left] in vowels:    # 'b' not in vowels, false
                    vowel_count -= 1     # skip
                left += 1                # left = 0 + 1 = 1
                # Check again: vowel_count = 3, k = 2, 3 > 2 is true
                # Check s[left] = s[1] = 'a'
                if s[left] in vowels:    # 'a' in vowels, true
                    vowel_count -= 1     # vowel_count = 3 - 1 = 2
                left += 1                # left = 1 + 1 = 2
                # Check again: vowel_count = 2, k = 2, 2 > 2 is false, exit while

            max_length = max(max_length, right - left + 1)  # right = 5, left = 2
                                                           # size = (5 - 2) + 1 = 4
                                                           # max_length = max(5, 4) = 5
            # After Iteration 5: vowel_count = 2, left = 2, max_length = 5
            # Current window: "nana" (2 vowels, length 4)

    # 5️⃣ Return the longest substring length
    # Why? max_length contains the length of the longest substring with at most k vowels
    return max_length             # max_length = 5


print(longest_substring_with_k_vowels("banana", 2))  # Output: 5
# Longest substring with at most 2 vowels is "banan" (length 5)



# ----------------------------------------------------------------------------------
# Solution with output for longest_substring_with_k_vowels Full Breakdown

def longest_substring_with_k_vowels(s, k):  # Example: s = "xyz", k = 1

    # 1️⃣ Initialize pointers & tracking variables
    # Create a set of vowels for quick lookup
    # Why? We need to efficiently check if a character is a vowel
    vowels = set('aeiou')      # vowels = {'a', 'e', 'i', 'o', 'u'}

    # Track the longest substring length with at most k vowels
    # Why? We need to update this as we find longer valid substrings
    max_length = 0             # max_length = 0 (no substring checked yet)

    # Track the number of vowels in the current window
    # Why? We need to ensure the window has at most k vowels
    vowel_count = 0            # vowel_count = 0 (no vowels counted yet)

    # Initialize left pointer for the start of the sliding window
    # Why? We'll move this to shrink the window when we have too many vowels
    left = 0                   # left = 0 (start at beginning)

    # 2️⃣ Expand window by moving `right` & process characters
    # Loop through each character as the right end of our window
    # Why? We check each character to build substrings with at most k vowels
    for right in range(len(s)):  # right goes from 0 to 2 (len("xyz") = 3)
        # --- Iteration 0: right = 0, s[0] = 'x' ---
        # Check if the current character is a vowel and increment count if it is
        # Why? We need to track vowels to enforce the k-vowel limit
        if s[right] in vowels:    # s[0] = 'x', 'x' not in vowels, false
            vowel_count += 1      # skip (not a vowel)

        # 3️⃣ Shrink window if vowel count exceeds k
        # While we have too many vowels and the window is valid (left <= right)
        # Why? We need to reduce the vowel count to make the substring valid
        while vowel_count > k and left <= right:  # vowel_count = 0, k = 1, 0 > 1 is false, skip
            # If the leftmost character is a vowel, decrease the count
            # Why? Removing a vowel reduces the vowel count
            if s[left] in vowels:    # skip (condition not met)
                vowel_count -= 1     # skip
            # Move the left pointer forward
            # Why? Shrink the window by excluding the leftmost character
            left += 1                # skip

        # 4️⃣ Update the longest substring length
        # Calculate the current window size
        # Why? This is the length of the current substring with at most k vowels
        max_length = max(max_length, right - left + 1)  # right = 0, left = 0
                                                       # size = (0 - 0) + 1 = 1
                                                       # max_length = max(0, 1) = 1
        # After Iteration 0: vowel_count = 0, left = 0, max_length = 1
        # Current window: "x" (0 vowels, length 1)

        # --- Iteration 1: right = 1, s[1] = 'y' ---
        if right == 1:
            if s[right] in vowels:    # s[1] = 'y', 'y' not in vowels, false
                vowel_count += 1      # skip (not a vowel)

            while vowel_count > k and left <= right:  # vowel_count = 0, k = 1, 0 > 1 is false, skip
                if s[left] in vowels:
                    vowel_count -= 1
                left += 1

            max_length = max(max_length, right - left + 1)  # right = 1, left = 0
                                                           # size = (1 - 0) + 1 = 2
                                                           # max_length = max(1, 2) = 2
            # After Iteration 1: vowel_count = 0, left = 0, max_length = 2
            # Current window: "xy" (0 vowels, length 2)

        # --- Iteration 2: right = 2, s[2] = 'z' ---
        if right == 2:
            if s[right] in vowels:    # s[2] = 'z', 'z' not in vowels, false
                vowel_count += 1      # skip (not a vowel)

            while vowel_count > k and left <= right:  # vowel_count = 0, k = 1, 0 > 1 is false, skip
                if s[left] in vowels:
                    vowel_count -= 1
                left += 1

            max_length = max(max_length, right - left + 1)  # right = 2, left = 0
                                                           # size = (2 - 0) + 1 = 3
                                                           # max_length = max(2, 3) = 3
            # After Iteration 2: vowel_count = 0, left = 0, max_length = 3
            # Current window: "xyz" (0 vowels, length 3)

    # 5️⃣ Return the longest substring length
    # Why? max_length contains the length of the longest substring with at most k vowels
    return max_length             # max_length = 3


print(longest_substring_with_k_vowels("xyz", 1))  # Output: 3
# Longest substring with at most 1 vowel is "xyz" (length 3)

