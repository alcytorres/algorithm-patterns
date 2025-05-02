

"""
Task: Given a string, find the length of the longest substring without any repeating characters.
Example 1: s = "abcabccc" → Output = 3 (substring "abc")
Example 2: s = "aa"       → Output = 1 (substring "a") 
Example 3: s = "aabbcc"   → Output = 2 (substring "ab" or "bc")
Example 4: s = "eceba"    → Output = 4 (substring "ceba") 
"""

def lengthOfLongestSubstring(s):    # Example: s = "abcabccc"
    # Initialize left pointer for the start of our sliding window
    # Why? We'll slide this to shrink the window when we find repeating characters
    left = 0                       # left = 0 (start at beginning)

    # Track the longest substring length we've found
    # Why? We need to compare and update this as we find longer valid substrings
    longest_substring = 0          # longest_substring = 0 (no substring checked yet)

    # Create a set to store characters in the current window
    # Why? Sets allow fast lookup to check for repeating characters
    sett = set()                   # sett = {} (empty set)

    # Get the length of the string
    # Why? We'll use this to loop through each character
    n = len(s)                     # n = 8 (for "abcabccc")

    # Loop through each character as the right end of our window
    # Why? We check each character to build valid substrings
    for right in range(n):         # right goes from 0 to 7
        # --- Iteration 0: right = 0, s[0] = 'a' ---
        # Check if the current character is in the set (indicates a repeat)
        # Why? We need to ensure no repeating characters in our window
        while s[right] in sett:    # s[0] = 'a', sett = {}, 'a' not in sett, skip
            # Remove the leftmost character from the set
            # Why? This shrinks the window to remove the repeating character
            sett.remove(s[left])   # skip (no repeat)
            # Move the left pointer forward
            # Why? Adjust the window start after removing a character
            left += 1              # skip (no repeat)

        # Calculate the size of the current window
        # Why? This is the length of our current substring with no repeats
        current_window_size = (right - left) + 1  # right = 0, left = 0
                                                 # size = (0 - 0) + 1 = 1

        # Update the longest length if the current window is bigger
        # Why? We want the maximum length of any valid substring
        longest_substring = max(longest_substring, current_window_size)  # max(0, 1) = 1
                                                                # longest_substring = 1

        # Add the current character to the set
        # Why? We've processed it, so include it in our window
        sett.add(s[right])         # sett = {'a'}

        # After Iteration 0: sett = {'a'}, left = 0, longest_substring = 1
        # Current substring: "a" (length 1)

        # --- Iteration 1: right = 1, s[1] = 'b' ---
        if right == 1:             # Check for clarity
            while s[right] in sett:  # s[1] = 'b', sett = {'a'}, 'b' not in sett, skip
                sett.remove(s[left])
                left += 1

            current_window_size = (right - left) + 1  # right = 1, left = 0
                                                     # size = (1 - 0) + 1 = 2
            longest_substring = max(longest_substring, current_window_size)  # max(1, 2) = 2
                                                                    # longest_substring = 2
            sett.add(s[right])       # sett = {'a', 'b'}
            # After Iteration 1: sett = {'a', 'b'}, left = 0, longest_substring = 2
            # Current substring: "ab" (length 2)

        # --- Iteration 2: right = 2, s[2] = 'c' ---
        if right == 2:
            while s[right] in sett:  # s[2] = 'c', sett = {'a', 'b'}, 'c' not in sett, skip
                sett.remove(s[left])
                left += 1

            current_window_size = (right - left) + 1  # right = 2, left = 0
                                                     # size = (2 - 0) + 1 = 3
            longest_substring = max(longest_substring, current_window_size)  # max(2, 3) = 3
                                                                    # longest_substring = 3
            sett.add(s[right])       # sett = {'a', 'b', 'c'}
            # After Iteration 2: sett = {'a', 'b', 'c'}, left = 0, longest_substring = 3
            # Current substring: "abc" (length 3)

        # --- Iteration 3: right = 3, s[3] = 'a' ---
        if right == 3:
            while s[right] in sett:  # s[3] = 'a', sett = {'a', 'b', 'c'}, 'a' in sett
                # Remove s[left] = s[0] = 'a'
                sett.remove(s[left])  # sett = {'b', 'c'}
                left += 1             # left = 1
                # Check again: s[3] = 'a', sett = {'b', 'c'}, 'a' not in sett, exit while

            current_window_size = (right - left) + 1  # right = 3, left = 1
                                                     # size = (3 - 1) + 1 = 3
            longest_substring = max(longest_substring, current_window_size)  # max(3, 3) = 3
                                                                    # longest_substring = 3
            sett.add(s[right])       # sett = {'b', 'c', 'a'}
            # After Iteration 3: sett = {'b', 'c', 'a'}, left = 1, longest_substring = 3
            # Current substring: "bca" (length 3)

        # --- Iteration 4: right = 4, s[4] = 'b' ---
        if right == 4:
            while s[right] in sett:  # s[4] = 'b', sett = {'b', 'c', 'a'}, 'b' in sett
                # Remove s[left] = s[1] = 'b'
                sett.remove(s[left])  # sett = {'c', 'a'}
                left += 1             # left = 2
                # Check again: s[4] = 'b', sett = {'c', 'a'}, 'b' not in sett, exit while

            current_window_size = (right - left) + 1  # right = 4, left = 2
                                                     # size = (4 - 2) + 1 = 3
            longest_substring = max(longest_substring, current_window_size)  # max(3, 3) = 3
                                                                    # longest_substring = 3
            sett.add(s[right])       # sett = {'c', 'a', 'b'}
            # After Iteration 4: sett = {'c', 'a', 'b'}, left = 2, longest_substring = 3
            # Current substring: "cab" (length 3)

        # --- Iteration 5: right = 5, s[5] = 'c' ---
        if right == 5:
            while s[right] in sett:  # s[5] = 'c', sett = {'c', 'a', 'b'}, 'c' in sett
                # Remove s[left] = s[2] = 'c'
                sett.remove(s[left])  # sett = {'a', 'b'}
                left += 1             # left = 3
                # Check again: s[5] = 'c', sett = {'a', 'b'}, 'c' not in sett, exit while

            current_window_size = (right - left) + 1  # right = 5, left = 3
                                                     # size = (5 - 3) + 1 = 3
            longest_substring = max(longest_substring, current_window_size)  # max(3, 3) = 3
                                                                    # longest_substring = 3
            sett.add(s[right])       # sett = {'a', 'b', 'c'}
            # After Iteration 5: sett = {'a', 'b', 'c'}, left = 3, longest_substring = 3
            # Current substring: "abc" (length 3)

        # --- Iteration 6: right = 6, s[6] = 'c' ---
        if right == 6:
            while s[right] in sett:  # s[6] = 'c', sett = {'a', 'b', 'c'}, 'c' in sett
                # Remove s[left] = s[3] = 'a'
                sett.remove(s[left])  # sett = {'b', 'c'}
                left += 1             # left = 4
                # Check again: s[6] = 'c', sett = {'b', 'c'}, 'c' in sett
                # Remove s[left] = s[4] = 'b'
                sett.remove(s[left])  # sett = {'c'}
                left += 1             # left = 5
                # Check again: s[6] = 'c', sett = {'c'}, 'c' in sett
                # Remove s[left] = s[5] = 'c'
                sett.remove(s[left])  # sett = {}
                left += 1             # left = 6
                # Check again: s[6] = 'c', sett = {}, 'c' not in sett, exit while

            current_window_size = (right - left) + 1  # right = 6, left = 6
                                                     # size = (6 - 6) + 1 = 1
            longest_substring = max(longest_substring, current_window_size)  # max(3, 1) = 3
                                                                    # longest_substring = 3
            sett.add(s[right])       # sett = {'c'}
            # After Iteration 6: sett = {'c'}, left = 6, longest_substring = 3
            # Current substring: "c" (length 1)

        # --- Iteration 7: right = 7, s[7] = 'c' ---
        if right == 7:
            while s[right] in sett:  # s[7] = 'c', sett = {'c'}, 'c' in sett
                # Remove s[left] = s[6] = 'c'
                sett.remove(s[left])  # sett = {}
                left += 1             # left = 7
                # Check again: s[7] = 'c', sett = {}, 'c' not in sett, exit while

            current_window_size = (right - left) + 1  # right = 7, left = 7
                                                     # size = (7 - 7) + 1 = 1
            longest_substring = max(longest_substring, current_window_size)  # max(3, 1) = 3
                                                                    # longest_substring = 3
            sett.add(s[right])       # sett = {'c'}
            # After Iteration 7: sett = {'c'}, left = 7, longest_substring = 3
            # Current substring: "c" (length 1)

    # Return the length of the longest substring found
    return longest_substring       # longest_substring = 3 (from substring "abc")


print(lengthOfLongestSubstring("abcabccc"))  # Output: 3 (substring "abc" has length 3)
