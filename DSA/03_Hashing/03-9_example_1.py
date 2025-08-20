# Longest Substring with At Most K Distinct Characters

# Example 1: You are given a string s and an integer k. Find the length of the longest substring that contains at most k distinct characters.

# Example
# Input: s = "eceba" and k = 2, 
# Output: return 3.
# The longest substring with at most 2 distinct characters is "ece".

# ece (positions 0-2): Characters {e, c} → 2 distinct → valid.
# ceb (positions 1-3): Characters {c, e, b} → 3 distinct → invalid.
# eba (positions 2-4): Characters {e, b, a} → 3 distinct → invalid.


from collections import defaultdict

def find_longest_substring(s, k):
    counts = defaultdict(int)
    left = ans = 0
    
    # Sliding window: expand right pointer
    for right in range(len(s)):
        counts[s[right]] += 1
        
        # Shrink window if too many distinct characters
        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1
        
        # Update max substring length
        ans = max(ans, right - left + 1)
    
    return ans

s = "eceba"
print(find_longest_substring(s, 2))  
# Output: 3


# Time: O(n)
# - Right pointer moves across the string once.
# - Left pointer also moves at most n steps in total.
# - Each character is added to and removed from the dictionary at most once.
# - Dictionary operations (add, update, delete) are O(1) on average.
# - Overall: O(n) time.

# Space: O(k)
# - Dictionary 'counts' stores at most k distinct characters at any time.
# - A few variables (left, right, ans) take O(1) space.
# - Overall: O(k) space, which is O(1) if k is considered a small constant.


# Trace Overview
"""
Trace of find_longest_substring("eceba", k=2):
| r | s[r] | counts       | len | Action       | l | ans |
|---|------|--------------|-----|--------------|---|-----|
| 0 | e    | {e:1}        | 1   | None         | 0 | 1   |
| 1 | c    | {e:1,c:1}    | 2   | None         | 0 | 2   |
| 2 | e    | {e:2,c:1}    | 2   | None         | 0 | 3   |
| 3 | b    | {e:2,c:1,b:1}| 3   | Drop e,c     | 2 | 3   |
| 4 | a    | {e:1,b:1,a:1}| 3   | Drop e       | 3 | 3   |
Output: 3 ('ece')
"""

# ––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
from collections import defaultdict  # Initialize defaultdict for character counts

def find_longest_substring(s, k):
    counts = defaultdict(int)  # Track character frequencies in window
    left = ans = 0            # Left bound, max length of substring
    for right in range(len(s)):  # Iterate right pointer over string
        counts[s[right]] += 1  # Increment count of current character
        while len(counts) > k: # Shrink window if distinct characters exceed k
            counts[s[left]] -= 1  # Decrement count of leftmost character
            if counts[s[left]] == 0:  # Remove character if count becomes 0
                del counts[s[left]]
            left += 1          # Move left pointer forward
        ans = max(ans, right - left + 1)  # Update max substring length
    return ans                # Return longest substring length with <= k distinct characters



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Why use defaultdict instead of regular dictionary {}?
    # defaultdict is used instead of a dictionary because it automatically initializes new keys with 0, simplifying code by eliminating the need to check for key existence before incrementing counts. 

# With regular dict
counts = {}
if s[right] not in counts:
    counts[s[right]] = 0
counts[s[right]] += 1  # Extra check needed

# With defaultdict
from collections import defaultdict
counts = defaultdict(int)
counts[s[right]] += 1  # No check needed, cleaner


# ––––––––––––––––––––––––––––––––––––––––––––––––
# Full Breakdown 
# Task: Find the length of the longest substring with at most k distinct characters.
# Example: s = "eceba", k = 2 → Output = 3 (substring "ece" has 2 distinct characters: 'e', 'c')
# Why: Practices sliding window technique with a hash map to track character counts.

from collections import defaultdict

def find_longest_substring(s, k):  # Example: s = "eceba", k = 2

    # 1️⃣ Initialize variables
    # Initialize a defaultdict to track character counts in the window
    # Why? We need to count occurrences of each character and ensure at most k distinct ones
    counts = defaultdict(int)  # counts = {}

    # Initialize left pointer for the sliding window
    # Why? We use left to shrink the window when we exceed k distinct characters
    left = 0  # left = 0

    # Initialize answer to track the longest substring length
    # Why? We need to store the maximum length of valid substrings
    ans = 0  # ans = 0

    # 2️⃣ Iterate with right pointer
    # Loop through the string with right pointer to expand the window
    # Why? We process each character to build windows and track valid substrings
    for right in range(len(s)):  # right goes from 0 to 4 (len(s) = 5)
        # --- Iteration 1: right = 0 ---
        # Increment count of the current character
        # Why? We track how many times each character appears in the window
        counts[s[right]] += 1  # s[0] = 'e', counts = {'e': 1}

        # Shrink window if we have more than k distinct characters
        # Why? We need to maintain at most k distinct characters in the window
        while len(counts) > k:  # len(counts) = 1, k = 2, 1 > 2 is false, skip
            counts[s[left]] -= 1  # skip
            if counts[s[left]] == 0:  # skip
                del counts[s[left]]
            left += 1  # skip
        # Update maximum length of valid substring
        # Why? The current window length may be the longest so far
        ans = max(ans, right - left + 1)  # right = 0, left = 0, ans = max(0, 0 - 0 + 1) = 1
        # After Iteration 1: left = 0, counts = {'e': 1}, ans = 1
        # Current window: "e" (1 distinct character, length 1)

        # --- Iteration 2: right = 1 ---
        if right == 1:
            counts[s[right]] += 1  # s[1] = 'c', counts = {'e': 1, 'c': 1}
            while len(counts) > k:  # len(counts) = 2, k = 2, 2 > 2 is false, skip
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    del counts[s[left]]
                left += 1
            ans = max(ans, right - left + 1)  # right = 1, left = 0, ans = max(1, 1 - 0 + 1) = 2
            # After Iteration 2: left = 0, counts = {'e': 1, 'c': 1}, ans = 2
            # Current window: "ec" (2 distinct characters, length 2)

        # --- Iteration 3: right = 2 ---
        if right == 2:
            counts[s[right]] += 1  # s[2] = 'e', counts = {'e': 2, 'c': 1}
            while len(counts) > k:  # len(counts) = 2, k = 2, 2 > 2 is false, skip
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    del counts[s[left]]
                left += 1
            ans = max(ans, right - left + 1)  # right = 2, left = 0, ans = max(2, 2 - 0 + 1) = 3
            # After Iteration 3: left = 0, counts = {'e': 2, 'c': 1}, ans = 3
            # Current window: "ece" (2 distinct characters, length 3)

        # --- Iteration 4: right = 3 ---
        if right == 3:
            counts[s[right]] += 1  # s[3] = 'b', counts = {'e': 2, 'c': 1, 'b': 1}
            while len(counts) > k:  # len(counts) = 3, k = 2, 3 > 2 is true
                counts[s[left]] -= 1  # s[0] = 'e', counts['e'] = 2 - 1 = 1
                if counts[s[left]] == 0:  # counts['e'] = 1, not 0, skip
                    del counts[s[left]]
                left += 1  # left = 0 + 1 = 1
                # Check again: len(counts) = 3, k = 2, 3 > 2 is true
                counts[s[left]] -= 1  # s[1] = 'c', counts['c'] = 1 - 1 = 0
                if counts[s[left]] == 0:  # counts['c'] = 0, true
                    del counts[s[left]]  # counts = {'e': 1, 'b': 1}
                left += 1  # left = 1 + 1 = 2
                # Check again: len(counts) = 2, k = 2, 2 > 2 is false, exit while
            ans = max(ans, right - left + 1)  # right = 3, left = 2, ans = max(3, 3 - 2 + 1) = 3
            # After Iteration 4: left = 2, counts = {'e': 1, 'b': 1}, ans = 3
            # Current window: "eb" (2 distinct characters, length 2)

        # --- Iteration 5: right = 4 ---
        if right == 4:
            counts[s[right]] += 1  # s[4] = 'a', counts = {'e': 1, 'b': 1, 'a': 1}
            while len(counts) > k:  # len(counts) = 3, k = 2, 3 > 2 is true
                counts[s[left]] -= 1  # s[2] = 'e', counts['e'] = 1 - 1 = 0
                if counts[s[left]] == 0:  # counts['e'] = 0, true
                    del counts[s[left]]  # counts = {'b': 1, 'a': 1}
                left += 1  # left = 2 + 1 = 3
                # Check again: len(counts) = 2, k = 2, 2 > 2 is false, exit while
            ans = max(ans, right - left + 1)  # right = 4, left = 3, ans = max(3, 4 - 3 + 1) = 3
            # After Iteration 5: left = 3, counts = {'b': 1, 'a': 1}, ans = 3
            # Current window: "ba" (2 distinct characters, length 2)

    # 3️⃣ Return the length of the longest valid substring
    # Why? ans contains the length of the longest substring with at most k distinct characters
    return ans  # ans = 3


s = "eceba"
print(find_longest_substring(s, 2))  
# Output: 3





# ––––––––––––––––––––––––––––––––––––––––––––––––
# Playground 

# Basic Usage of defaultdict for DSA
# defaultdict simplifies dictionary operations by providing default values for new keys

# Regular Dictionary vs defaultdict: Counting Characters

# Regular Dictionary (requires manual key check)
d = {}
s = "aabbc"
for c in s:
    if c not in d:  # Must check if key exists
        d[c] = 0
    d[c] += 1
print(d)  
# Output: {'a': 2, 'b': 2, 'c': 1}

# defaultdict (simplifies with auto-default 0)
from collections import defaultdict
dd = defaultdict(int)
for c in s:
    dd[c] += 1  # No key check needed
print(dd)  
# Output: defaultdict(<class 'int'>, {'a': 2, 'b': 2, 'c': 1})



# Use of defaultdict
from collections import defaultdict

# Input list of (key, value) tuples
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

# Create defaultdict to store lists of values for each key
d = defaultdict(list)

# Group values by key, appending each value to key's list
for k, v in s:
    d[k].append(v)

# Sort key-value pairs by key and print as list of tuples
print(sorted(d.items()))
# Output: [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]