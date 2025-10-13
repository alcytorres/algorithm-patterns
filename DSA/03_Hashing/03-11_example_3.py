# 1941. Check if All Characters Have Equal Number of Occurrences

# Example 3: Given a string s, determine if all characters have the same number of occurrences (i.e., the same frequency).

# Example:
    # Input: s = "abacbc"
    # Output: True
    # Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.

# Solution: https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/solutions/


from collections import defaultdict

def areOccurrencesEqual(s):
    counts = defaultdict(int)

    # Count frequency of each character
    for c in s:
        counts[c] += 1
    
    # Grab all the frequencies
    frequencies = counts.values()
    return len(set(frequencies)) == 1

s = "abacbc"
print(areOccurrencesEqual(s))
# Output: True → Each character in "abacbc" appears exactly twice.


"""
Time: O(N)
  - Let N = length of the string s.
  - Step 1: Count occurrences of each character → O(N).
      • Each character is added/updated in the dictionary in O(1) average.
  - Step 2: Get all frequency values → O(U), where U ≤ 26 for lowercase letters.
  - Step 3: Convert frequencies to a set and check its size → O(U).
  - Overall: O(N).

Space: O(U)
  - Dictionary 'counts' stores up to U unique characters (≤ 26).
  - Set of frequencies also stores up to U elements.
  - A few scalar variables (c, loop counter) use O(1).
  - Overall: O(U), worst case O(1) since U ≤ 26.

  
Interview Answer: Worst Case

Time: O(N)
  - Count all characters and verify equal frequencies.

Space: O(1)
  - Constant space since there are at most 26 lowercase letters.


Overview for Each Iteration
Input: s = "abacbc"

Step 1: Count frequency of each character
i  | c   | counts
---|-----|---------------------
-  | -   | {}
0  | a   | {a: 1}
1  | b   | {a: 1, b: 1}
2  | a   | {a: 2, b: 1}
3  | c   | {a: 2, b: 1, c: 1}
4  | b   | {a: 2, b: 2, c: 1}
5  | c   | {a: 2, b: 2, c: 2}

Step 2: Check if all frequencies are equal
frequencies = counts.values() = [2, 2, 2]
set(frequencies) = {2}
len(set(frequencies)) = 1

Final: True



---------------------------------------------------
Q: How does `return len(set(frequency)) == 1` check if all counts are equal?
    • Convert the list of frequencies into a set.

    • A set only keeps unique values.

    • If all frequencies are the same, the set will have exactly 1 element.

    • Therefore, len(set(frequency)) == 1 means all characters occur equally often.

"""


# ––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
from collections import defaultdict

def areOccurrencesEqual(s):
    counts = defaultdict(int)  # Initialize dictionary for character frequencies

    for c in s:               # Iterate over each character in string
        counts[c] += 1        # Increment count for current character

    frequencies = counts.values()  # Get all frequency values
    return len(set(frequencies)) == 1  # Return True if all frequencies are equal


# –––––––––––––––––––––––––––––––––––––––––––––––––––––
# Alternative Solution I came up with 

from collections import defaultdict

def areOccurrencesEqual(s):
    counts = defaultdict(int)

    for c in s:
        counts[c] += 1

    seen = set()
    for value in counts.values():
        seen.add(value)
    
    return len(seen) == 1


s = "abacbc"
print(areOccurrencesEqual(s))
# Output: True

# {'a': 2, 'b': 2, 'c': 2}




# –––––––––––––––––––––––––––––––––––––––––––––––––––––
# My attempt at a solution which is wrong

from collections import defaultdict

def areOccurrencesEqual(s):
    counts = defaultdict(int)
    for right in range(len(s)):
        counts[s[right]] += 1
    
    if counts['c'] == 2:
        return True
    return False


string = "abacbc"
print(areOccurrencesEqual(string))



# –––––––––––––––––––––––––––––––––––––––––––––––––––––
# Alternative Less Efficient Solution I came up with

from collections import defaultdict

def areOccurrencesEqual(s):
    counts = defaultdict(int)

    for c in s:
        counts[c] += 1
    
    set_map = set()
    for val in counts.values():
        set_map.add(val)
    
    if len(set_map) == 1:
        return True
    return False

s = "abacbc"
print(areOccurrencesEqual(s))
# Output: True




# ––––––––––––––––––––––––––––––––––––––––––––––––
# Task: Determine if all characters in a string have the same frequency.
# Example: s = "abacbc" → Output = True (all characters 'a', 'b', 'c' appear twice)
# Why: Practices hash map usage to count character frequencies and set comparison for equality.

from collections import defaultdict

def areOccurrencesEqual(s):  # Example: s = "abacbc"

    # 1️⃣ Count character frequencies
    # Initialize a defaultdict to store character counts
    # Why? We need to track how many times each character appears
    counts = defaultdict(int)  # counts = {}

    # Iterate through the string to count each character
    # Why? We need to build a frequency map for all characters
    for c in s:  # c takes values ['a', 'b', 'a', 'c', 'b', 'c']
        # --- Iteration 1: c = 'a' ---
        counts[c] += 1  # counts['a'] = 0 + 1 = 1
        # After Iteration 1: counts = {'a': 1}

        # --- Iteration 2: c = 'b' ---
        if c == 'b':
            counts[c] += 1  # counts['b'] = 0 + 1 = 1
            # After Iteration 2: counts = {'a': 1, 'b': 1}

        # --- Iteration 3: c = 'a' ---
        if c == 'a' and counts['a'] == 1:
            counts[c] += 1  # counts['a'] = 1 + 1 = 2
            # After Iteration 3: counts = {'a': 2, 'b': 1}

        # --- Iteration 4: c = 'c' ---
        if c == 'c':
            counts[c] += 1  # counts['c'] = 0 + 1 = 1
            # After Iteration 4: counts = {'a': 2, 'b': 1, 'c': 1}

        # --- Iteration 5: c = 'b' ---
        if c == 'b' and counts['b'] == 1:
            counts[c] += 1  # counts['b'] = 1 + 1 = 2
            # After Iteration 5: counts = {'a': 2, 'b': 2, 'c': 1}

        # --- Iteration 6: c = 'c' ---
        if c == 'c' and counts['c'] == 1:
            counts[c] += 1  # counts['c'] = 1 + 1 = 2
            # After Iteration 6: counts = {'a': 2, 'b': 2, 'c': 2}

    # 2️⃣ Check frequency equality
    # Get the set of frequency values
    # Why? We need to check if all characters have the same frequency
    frequencies = counts.values()  # frequencies = [2, 2, 2] (values for 'a', 'b', 'c')

    # Return True if the set has exactly one unique frequency
    # Why? If len(set(frequencies)) == 1, all characters have the same frequency
    return len(set(frequencies)) == 1  # set([2, 2, 2]) = {2}, len({2}) = 1, True


s = "abacbc"
print(areOccurrencesEqual(s))  # Output: True