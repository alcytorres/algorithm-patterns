"""
Task: Given a string, find the length of the longest substring with at most K distinct characters.
Example 1: s = "eceba", K = 2 → Output = 3 (substring "ece")
Example 2: s = "aa", K = 1 → Output = 2 (substring "aa")
Example 3: s = "aabbcc", K = 2 → Output = 4 (substring "aabb" or "bbcc")
"""

def longest_substring_with_k_distinct(s, K):
    # 1️⃣ Initialize pointers & tracking variables
    left = 0
    max_length = 0
    char_count = {}  # Dictionary to store character frequencies in the window

    # 2️⃣ Expand window by moving `right` & update conditions
    for right in range(len(s)):
        # Add the current character to the window
        char_count[s[right]] = char_count.get(s[right], 0) + 1

        # 3️⃣ Shrink window when we have more than K distinct characters
        while len(char_count) > K:
            # Reduce the count of the character at the left pointer
            char_count[s[left]] -= 1
            # If its count becomes 0, remove it from the dictionary
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1  # Move the left pointer to shrink the window

        # 4️⃣ Update the maximum length with the current window size
        current_length = right - left + 1
        max_length = max(max_length, current_length)

    # 5️⃣ Return the final result
    return max_length


print(longest_substring_with_k_distinct("aabbcc", 2))  # Output: 4

# ----------------------------------------------------------------------------------
# Solution FULL Breakdown

"""
Task: Given a string, find the length of the longest substring with at most K distinct characters.
Example 1: s = "eceba", K = 2 → Output = 3 (substring "ece")
Example 2: s = "aa", K = 1 → Output = 2 (substring "aa")
Example 3: s = "aabbcc", K = 2 → Output = 4 (substring "aabb" or "bbcc")
"""

def longest_substring_with_k_distinct(s, K):    # Example: s = "aabbcc", K = 2
    # For this breakdown, we use s = "aabbcc" and K = 2
    K = 2

    # 1️⃣ Initialize pointers & tracking variables
    # Initialize left pointer for the start of our sliding window
    # Why? We'll move this to shrink the window when we have too many distinct characters
    left = 0                       # left = 0 (start at beginning)

    # Track the longest substring length we've found
    # Why? We need to update this whenever we find a longer valid substring
    max_length = 0                 # max_length = 0 (no substring checked yet)

    # Create a dictionary to store character frequencies in the current window
    # Why? We need to count distinct characters and remove them when their count hits zero
    char_count = {}                # char_count = {} (empty dictionary)

    # 2️⃣ Expand window by moving `right` & update conditions
    # Loop through each character as the right end of our window
    # Why? We check each character to build substrings with at most K distinct characters
    for right in range(len(s)):    # right goes from 0 to 5 for "aabbcc"
        # --- Iteration 0: right = 0, s[0] = 'a' ---
        # Add the current character to the dictionary
        # Why? We’re expanding the window and need to track this character
        char_count[s[right]] = char_count.get(s[right], 0) + 1  # char_count = {'a': 1}

        # Check if we have more than K distinct characters
        # Why? Our condition is that the window must have at most 2 distinct characters
        while len(char_count) > K:  # len(char_count) = 1 <= 2, skip shrinking
            # Decrease the count of the character at the left pointer
            # Why? We're removing this character from the window to reduce distinct characters
            char_count[s[left]] -= 1    # No execution in Iteration 0 (condition not violated)
            # Check if the character's count becomes zero
            # Why? If zero, we remove it from the dictionary to reflect fewer distinct characters
            if char_count[s[left]] == 0:  # No execution in Iteration 0
                # Remove the character from the dictionary
                # Why? It’s no longer in our window, so we update distinct character count
                del char_count[s[left]]   # No execution in Iteration 0
            # Move the left pointer forward
            # Why? Shrink the window by excluding the leftmost character
            left += 1                   # No execution in Iteration 0

        # --- Iteration 1: right = 1, s[1] = 'a' ---
        if right == 1:
            char_count[s[right]] = char_count.get(s[right], 0) + 1  # char_count = {'a': 2}
            while len(char_count) > K:  # len(char_count) = 1 <= 2, skip
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            current_length = right - left + 1  # right = 1, left = 0
                                              # current_length = 1 - 0 + 1 = 2
            max_length = max(max_length, current_length)  # max(1, 2) = 2
                                                         # max_length = 2
            # After Iteration 1: char_count = {'a': 2}, left = 0, max_length = 2
            # Current substring: "aa" (length 2, 1 distinct character)

        # --- Iteration 2: right = 2, s[2] = 'b' ---
        if right == 2:
            char_count[s[right]] = char_count.get(s[right], 0) + 1  # char_count = {'a': 2, 'b': 1}
            while len(char_count) > K:  # len(char_count) = 2 <= 2, skip
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            current_length = right - left + 1  # right = 2, left = 0
                                              # current_length = 2 - 0 + 1 = 3
            max_length = max(max_length, current_length)  # max(2, 3) = 3
                                                         # max_length = 3
            # After Iteration 2: char_count = {'a': 2, 'b': 1}, left = 0, max_length = 3
            # Current substring: "aab" (length 3, 2 distinct characters)

        # --- Iteration 3: right = 3, s[3] = 'b' ---
        if right == 3:
            char_count[s[right]] = char_count.get(s[right], 0) + 1  # char_count = {'a': 2, 'b': 2}
            while len(char_count) > K:  # len(char_count) = 2 <= 2, skip
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            current_length = right - left + 1  # right = 3, left = 0
                                              # current_length = 3 - 0 + 1 = 4
            max_length = max(max_length, current_length)  # max(3, 4) = 4
                                                         # max_length = 4
            # After Iteration 3: char_count = {'a': 2, 'b': 2}, left = 0, max_length = 4
            # Current substring: "aabb" (length 4, 2 distinct characters)

        # --- Iteration 4: right = 4, s[4] = 'c' ---
        if right == 4:
            char_count[s[right]] = char_count.get(s[right], 0) + 1  # char_count = {'a': 2, 'b': 2, 'c': 1}
            while len(char_count) > K:  # len(char_count) = 3 > 2, shrink
                # Decrease count of character at left
                char_count[s[left]] -= 1    # s[0] = 'a', char_count['a'] = 1
                if char_count[s[left]] == 0:  # char_count['a'] = 1, not 0, skip deletion
                    del char_count[s[left]]
                left += 1                   # left = 1
                # Check again: char_count = {'a': 1, 'b': 2, 'c': 1}, len = 3 > 2
                char_count[s[left]] -= 1    # s[1] = 'a', char_count['a'] = 0
                if char_count[s[left]] == 0:  # char_count['a'] = 0, delete it
                    del char_count[s[left]]   # char_count = {'b': 2, 'c': 1}
                left += 1                   # left = 2
                # Now len(char_count) = 2 <= 2, stop shrinking
            current_length = right - left + 1  # right = 4, left = 2
                                              # current_length = 4 - 2 + 1 = 3
            max_length = max(max_length, current_length)  # max(4, 3) = 4
                                                         # max_length = 4
            # After Iteration 4: char_count = {'b': 2, 'c': 1}, left = 2, max_length = 4
            # Current substring: "bbc" (length 3, 2 distinct characters)

        # --- Iteration 5: right = 5, s[5] = 'c' ---
        if right == 5:
            char_count[s[right]] = char_count.get(s[right], 0) + 1  # char_count = {'b': 2, 'c': 2}
            while len(char_count) > K:  # len(char_count) = 2 <= 2, skip
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            current_length = right - left + 1  # right = 5, left = 2
                                              # current_length = 5 - 2 + 1 = 4
            max_length = max(max_length, current_length)  # max(4, 4) = 4
                                                         # max_length = 4
            # After Iteration 5: char_count = {'b': 2, 'c': 2}, left = 2, max_length = 4
            # Current substring: "bbcc" (length 4, 2 distinct characters)

    # 5️⃣ Return final result
    # Return the length of the longest substring found
    return max_length                  # max_length = 4 (from "aabb" or "bbcc")


print(longest_substring_with_k_distinct("aabbcc", 2))  # Output: 4
