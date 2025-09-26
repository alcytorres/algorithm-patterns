# 771. Jewels and Stones

# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Solution: https://leetcode.com/problems/jewels-and-stones/solutions/127766/jewels-and-stones/

# Example 1:
    # Input: jewels = "aA", stones = "aAAbbbb"
    # Output: 3

# Example 2:
    # Input: jewels = "z", stones = "ZZ"
    # Output: 0

# Constraints:
    # 1 <= jewels.length, stones.length <= 50
    # jewels and stones consist of only English letters.
    # All the characters of jewels are unique.

# -----------------------------------------------
# Hash Set one line

def numJewelsInStones(jewels, stones):
    Jset = set(jewels)
    return sum(s in Jset for s in stones)

jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))
# Output 3


"""
Time: O(J + S)
  - Let J = length of jewels, S = length of stones.
  - Step 1: Convert the string jewels into a set → O(J).
      • Each jewel is added once.
  - Step 2: Loop through all stones → O(S).
      • For each stone, check if it exists in the set (O(1) average).
      • Add up how many stones are jewels.
  - Overall: O(J + S).

Space: O(J)
  - The set 'Jset' can store at most J unique jewel characters.
  - Only a few extra variables (loop variable, sum counter) use O(1) space.
  - Overall: O(J).

  
Interview Answer: Worst Case

Time: O(J + S)
  - Build set of jewels, then scan stones.

Space: O(J)
  - Need a set for jewel types.



Overview for Each Iteration
Input: jewels = "aA", stones = "aAAbbbb"

Step 1: Create set of jewels
Jset = {'a', 'A'}

Step 2: Sum stones that are in Jset
s   | s in Jset | Sum
----|-----------|----
a   | True      | 1
A   | True      | 2
A   | True      | 3
b   | False     | 3
b   | False     | 3
b   | False     | 3
b   | False     | 3
Final: 3



Most IMPORTANT thing to Understand:
    • We need to count how many characters in stones also appear in jewels.

    • Jewels are unique and case-sensitive (so "a" ≠ "A").

    • A set of jewels makes it easy to quickly check if each stone is a jewel.

---
Why this code Works:
    • Data structure: set(jewels) stores all jewel types for O(1) membership checks.

    • Technique: For each stone, check if it's in the jewel set; True counts as 1, False as 0.

    • Efficiency: Instead of nested loops O(J×S), we reduce to O(J + S): build set once, scan stones once.

    • Intuition: Like having a “whitelist” of jewel types—you just check each stone against the list.

---
TLDR (one sentence):
    • Make a set of jewels and count how many stones belong to that set.

---
Quick Example Walkthrough:

    jewels = "aA", stones = "aAAbbbb"

    Build set: `{'a', 'A'}`

    Check each stone:
    'a' → in jewels → +1
    'A' → in jewels → +1
    'A' → in jewels → +1
    'b' → not in jewels → +0
    'b' → +0
    'b' → +0
    'b' → +0

    Total = 3

"""


# -----------------------------------------------
# Hash Set rewritten w explicit loop: 

def numJewelsInStones(J, S):
    Jset = set(J)
    count = 0

    for s in S:
        if s in Jset:
            count += 1
    return count


jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))
# Output 3


"""
Time: O(J + S)
  - Let J = length of jewels, S = length of stones.
  - Step 1: Convert the string jewels into a set → O(J).
      • Each jewel is added once.
  - Step 2: Loop through all stones → O(S).
      • For each stone, check if it exists in the set (O(1) average).
      • If it is a jewel, increment the counter.
  - Overall: O(J + S).

Space: O(J)
  - The set 'Jset' can store at most J unique jewel characters.
  - Only a few extra variables (loop variable and 'count') use O(1) space.
  - Overall: O(J).

  
Interview Answer: Worst Case

Time: O(J + S)
  - Build set of jewels, then scan stones.

Space: O(J)
  - Need a set for jewel types.



Overview for Each Iteration
Input: jewels = "aA", stones = "aAAbbbb"

Step 1: Create set of jewels
Jset = {'a', 'A'}

Step 2: Count stones that are in Jset
s   | s in Jset | count
----|-----------|------
a   | True      | 1
A   | True      | 2
A   | True      | 3
b   | False     | 3
b   | False     | 3
b   | False     | 3
b   | False     | 3
Final: 3

"""




# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown

def numJewelsInStones(jewels, stones):
    Jset = set(jewels)        # Convert jewels to set for O(1) lookups
    return sum(s in Jset for s in stones)  # Count stones that are in jewels set



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force 

def numJewelsInStones(J, S):
    return sum(s in J for s in S)


jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))
# Output 3

# Time Complexity: O(J.length∗S.length))
# Space Complexity: O(1) 



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Alternate Solutions

from collections import Counter

def numJewelsInStones(J, S):
    letters = Counter(S)
    curr = 0

    for c in J:
        curr += letters[c]
    return curr


jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))
# Output 3

# Counter({'b': 4, 'A': 2, 'a': 1})
