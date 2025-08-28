# 1189. Maximum Number of Balloons

# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

# Example 1:
# Input: text = "nlaebolko"
# Output: 1

# Example 2:
# Input: text = "loonbalxballpoon"
# Output: 2

# Example 3:
# Input: text = "leetcode"
# Output: 0

# Solution: https://leetcode.com/problems/maximum-number-of-balloons/editorial/

from collections import defaultdict

def maxNumberOfBalloons(text):
    # Step 1: Count characters in text
    counts = defaultdict(int)
    for c in text:
        counts[c] += 1
    
    # Step 2: Find how many "balloon"s we can make
    return min(counts['b'], counts['a'], counts['l'] // 2, counts['o'] // 2, counts['n'])


text = "nlaebolko"
print(maxNumberOfBalloons(text))
# Output: 1

# counts = {'n': 1, 'l': 2, 'a': 1, 'e': 1, 'b': 1, 'o': 2, 'k': 1}


# Time: O(n)
# - Loop through text once to count characters: O(n).
# - Compute the minimum over fixed letters 'b', 'a', 'l', 'o', 'n': O(1).
# - Overall: O(n) time.

# Space: O(n)
# - Dictionary 'counts' can store up to n entries in the worst case (all characters unique).
# - A few variables (char, text) take O(1) space.
# - Overall: O(n) total space.
# - Since the alphabet size is bounded (26 lowercase letters), practical space can also be considered O(1).


# Overview for Each Iteration
# Step 1: Count characters in text
# Idx | char | counts
# -   | -    | {}
# 0   | n    | {n:1}
# 1   | l    | {n:1, l:1}
# 2   | a    | {n:1, l:1, a:1}
# 3   | e    | {n:1, l:1, a:1, e:1}
# 4   | b    | {n:1, l:1, a:1, e:1, b:1}
# 5   | o    | {n:1, l:1, a:1, e:1, b:1, o:1}
# 6   | l    | {n:1, l:2, a:1, e:1, b:1, o:1}
# 7   | k    | {n:1, l:2, a:1, e:1, b:1, o:1, k:1}
# 8   | o    | {n:1, l:2, a:1, e:1, b:1, o:2, k:1}

# Step 2: Calculate max "balloon"s
# Char | Count | Required      | Available
# b    | 1     | 1 per balloon | 1
# a    | 1     | 1 per balloon | 1
# l    | 2     | 2 per balloon | 2 // 2 = 1
# o    | 2     | 2 per balloon | 2 // 2 = 1
# n    | 1     | 1 per balloon | 1
# Final: min(1, 1, 1, 1, 1) = 1




# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force
def maxNumberOfBalloons_bruteforce(text):
    # Repeatedly try to "build" the word "balloon" by removing needed letters
    letters = list(text)
    target = "balloon"
    count = 0
    while True:
        for c in target:
            if c in letters:
                letters.remove(c)  # remove one occurrence
            else:
                return count
        count += 1

text = "nlaebolko"
print(maxNumberOfBalloons_bruteforce(text))
# Output: 1


# Time: O(n^2)
# - Each attempt to build "balloon" does ~7 `in` + `remove` operations on a list.
# - `in`/`remove` are O(n) (scan + delete shift), so each balloon costs O(n).
# - You can build at most O(n) balloons → O(n^2) overall.

# Space: O(n)
# - Stores the characters in a list, plus a few scalars.
# - Overall: O(n) space.


# Trace Overview
# text = "nlaebolko"
# letters start: [n, l, a, e, b, o, l, k, o]
# Build #1 needs: b a l l o o n
# - remove b → [n, l, a, e, o, l, k, o]
# - remove a → [n, l, e, o, l, k, o]
# - remove l → [n, e, o, l, k, o]
# - remove l → [n, e, o, k, o]
# - remove o → [n, e, k, o]
# - remove o → [n, e, k]
# - remove n → [e, k]
# count = 1
# Next build: need 'b' but not present → stop → answer = 1





# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Simple Breakdown

from collections import defaultdict

def maxNumberOfBalloons(text):
    counts = defaultdict(int)  # Notebook to count each character's occurrences

    for c in text:            # Go through each character in the string
        counts[c] += 1        # Add 1 to the count of this character

    # Return min count of 'b', 'a', 'l'/2, 'o'/2, 'n' for complete "balloon"s
    return min(counts['b'], counts['a'], counts['l'] // 2, counts['o'] // 2, counts['n']) 



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Full Breakdown

# Task: Find the maximum number of "balloon" instances that can be formed using characters from a string, with each character used at most once.
# Example: text = "nlaebolko" → Output = 1 (can form one "balloon" using available characters)
# Why: Practices hash map usage to count characters and determine the limiting factor for forming "balloon".

from collections import defaultdict

def maxNumberOfBalloons(text):  # Example: text = "nlaebolko"

    # 1️⃣ Count characters in text
    # Initialize a defaultdict to store character counts
    # Why? We need to track how many times each character appears
    counts = defaultdict(int)  # counts = {}

    # Iterate through the string to count each character
    # Why? We need to know the frequency of each character to form "balloon"
    for c in text:  # c takes values ['n', 'l', 'a', 'e', 'b', 'o', 'l', 'k', 'o']
        # --- Iteration 1: c = 'n' ---
        counts[c] += 1  # counts['n'] = 0 + 1 = 1
        # After Iteration 1: counts = {'n': 1}

        # --- Iteration 2: c = 'l' ---
        if c == 'l' and counts['l'] == 0:
            counts[c] += 1  # counts['l'] = 0 + 1 = 1
            # After Iteration 2: counts = {'n': 1, 'l': 1}

        # --- Iteration 3: c = 'a' ---
        if c == 'a':
            counts[c] += 1  # counts['a'] = 0 + 1 = 1
            # After Iteration 3: counts = {'n': 1, 'l': 1, 'a': 1}

        # --- Iteration 4: c = 'e' ---
        if c == 'e':
            counts[c] += 1  # counts['e'] = 0 + 1 = 1
            # After Iteration 4: counts = {'n': 1, 'l': 1, 'a': 1, 'e': 1}

        # --- Iteration 5: c = 'b' ---
        if c == 'b':
            counts[c] += 1  # counts['b'] = 0 + 1 = 1
            # After Iteration 5: counts = {'n': 1, 'l': 1, 'a': 1, 'e': 1, 'b': 1}

        # --- Iteration 6: c = 'o' ---
        if c == 'o' and counts['o'] == 0:
            counts[c] += 1  # counts['o'] = 0 + 1 = 1
            # After Iteration 6: counts = {'n': 1, 'l': 1, 'a': 1, 'e': 1, 'b': 1, 'o': 1}

        # --- Iteration 7: c = 'l' ---
        if c == 'l' and counts['l'] == 1:
            counts[c] += 1  # counts['l'] = 1 + 1 = 2
            # After Iteration 7: counts = {'n': 1, 'l': 2, 'a': 1, 'e': 1, 'b': 1, 'o': 1}

        # --- Iteration 8: c = 'k' ---
        if c == 'k':
            counts[c] += 1  # counts['k'] = 0 + 1 = 1
            # After Iteration 8: counts = {'n': 1, 'l': 2, 'a': 1, 'e': 1, 'b': 1, 'o': 1, 'k': 1}

        # --- Iteration 9: c = 'o' ---
        if c == 'o' and counts['o'] == 1:
            counts[c] += 1  # counts['o'] = 1 + 1 = 2
            # After Iteration 9: counts = {'n': 1, 'l': 2, 'a': 1, 'e': 1, 'b': 1, 'o': 2, 'k': 1}

    # 2️⃣ Find how many "balloon"s we can make
    # Return the minimum of required character counts
    # Why? Each "balloon" needs 1 'b', 1 'a', 2 'l', 2 'o', 1 'n'; the minimum count limits the number of instances
    return min(counts['b'], counts['a'], counts['l'] // 2, counts['o'] // 2, counts['n'])
    # counts['b'] = 1, counts['a'] = 1, counts['l'] // 2 = 2 // 2 = 1, counts['o'] // 2 = 2 // 2 = 1, counts['n'] = 1
    # min(1, 1, 1, 1, 1) = 1


text = "nlaebolko"
print(maxNumberOfBalloons(text))  # Output: 1