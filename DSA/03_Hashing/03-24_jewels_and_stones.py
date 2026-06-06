# 771. Jewels and Stones
"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
    Input: jewels = "aA", stones = "aAAbbbb"
    Output: 3

Example 2:
    Input: jewels = "z", stones = "ZZ"
    Output: 0

Constraints:
    1 <= jewels.length, stones.length <= 50
    jewels and stones consist of only English letters.
    All the characters of jewels are unique.


Solution: https://leetcode.com/problems/jewels-and-stones/solutions/127766/jewels-and-stones/
"""

# Optimized Solution: Hash Set
def numJewelsInStones(jewels, stones):
    Jset = set(jewels)
    count = 0

    for s in stones:
        if s in Jset:
            count += 1
    return count


jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))
# Output 3: You have 3 stones (a, A, A) that are also jewels.


# ––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown

def numJewelsInStones(jewels, stones):
    Jset = set(jewels)    # Put all jewel types in a set for fast lookup
    count = 0             # Start counting matching stones at zero

    for s in stones:      # Go through each stone you own
        if s in Jset:     # Is this stone type also a jewel?
            count += 1    # Yes — add one to the count
    return count          # Return how many stones are jewels


"""
Time: O(J + S)
  - Let J = length of jewels, S = length of stones.
  - Step 1: Build set from jewels → O(J).
      • Each jewel is added once → O(1) average per insert.
  - Step 2: Loop through stones → O(S).
      • For each stone, check if s in Jset → O(1) average per check.
  - Combined: O(J + S).
  - Overall: O(J + S).

Space: O(J)
  - Set 'Jset' stores at most J unique jewel characters.
  - Only a few extra variables (count, s).
  - Overall: O(J).


Interview Answer: Worst Case

Time: O(J + S)
  - Build hash set of jewels, then scan every stone once.

Space: O(J)
  - Hash set holds all jewel types.


---
🧠 First Time? Thoughts → Code

Read the problem (10 sec)
    • Count how many of your stones are also jewels.

    • Each char in stones = one stone. Case-sensitive ("a" ≠ "A").

    • Jewels are unique — hint that a set works well.

Start naive (totally fine)
    • For each stone, check if it's anywhere in the jewels string.
    • Say out loud: "Is this stone in my jewel list?"
    • Time: O(J × S) — each stone scans all jewels.


The one insight that unlocks the optimal code
    • Same question asked S times: "Is this character a jewel?"
    • That's a lookup — put jewels in a set once, check in O(1).
    • Loop stones (not jewels) — you're counting what you own.

Why a hash set?
    • "s in jewels" on a string is O(J) per stone.
    • "s in Jset" is O(1) per stone.
    • We only need yes/no — no counts, no order.


Thought → line of code
    Jset = set(jewels)
        → "Load jewel types into a set for instant lookup."

    for s in stones:
        → "Walk my bag of stones one by one."

    if s in Jset:
        → "Is this stone type on the jewel whitelist?"

    count += 1
        → "Yes — count it."


Memory hook (one sentence)
    • Set = jewel whitelist; loop stones and count matches.


Would you arrive at this cold?
    • Immediately: loop stones, if stone is in jewels, count++.
    • After spotting slow lookup: use set(jewels) instead of scanning jewels string.
    • Bookkeeping: count = 0, return count — instinct.
    • Real insight: repeated membership check → hash set.



---
Most IMPORTANT thing to Understand:
    • Count how many stones you own are also jewel types.

    • Each character in stones is one stone — check them one by one.

    • Jewels are case-sensitive ("a" ≠ "A").

    • The set stores jewel types for fast "is this a jewel?" checks.


---
Why this code Works:
    • Hash set role:
        • Jset = set(jewels) holds every jewel type.
        • Turns "is this stone a jewel?" into an O(1) lookup.

    • Loop through stones:
        • For each stone s, check if s in Jset.
        • If yes → count += 1.

    • Efficiency:
        • Without a set: check each stone against every jewel → O(J × S).
        • With a set: build once, check each stone once → O(J + S).

    • Intuition:
        • Jset is a whitelist of jewel types.
        • Walk your bag of stones — count any that are on the list.


---
TLDR:
    • Put jewels in a set, loop stones, and count each one that appears in the set.


---
Quick Example Walkthrough:
    jewels = "aA", stones = "aAAbbbb"

    Step 1: Build set
        Jset = {'a', 'A'}

    Step 2: Check each stone
        'a' → in Jset → count = 1
        'A' → in Jset → count = 2
        'A' → in Jset → count = 3
        'b' → not in Jset → count = 3
        'b', 'b', 'b' → skip

    Final Answer: 3


---
Full Example Walkthrough:
    jewels = "aA", stones = "aAAbbbb"

    Starting State:
        Jset = {'a', 'A'}
        count = 0

    Loop Iteration 1:
        s = 'a'
        Check: 'a' in Jset → True
        count += 1 → count = 1

    --------------------------------------------------

    Loop Iteration 2:
        s = 'A'
        Check: 'A' in Jset → True
        count += 1 → count = 2

    --------------------------------------------------

    Loop Iteration 3:
        s = 'A'
        Check: 'A' in Jset → True
        count += 1 → count = 3

    --------------------------------------------------

    Loop Iteration 4:
        s = 'b'
        Check: 'b' in Jset → False
        count stays 3

    --------------------------------------------------

    Loop Iterations 5–7:
        s = 'b', 'b', 'b' → all False → count stays 3

    --------------------------------------------------

    Final Check:
        return count → 3
        Meaning: 3 of your stones (a, A, A) are jewels.



---
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












# -----------------------------------------------
# Hash Set one line

def numJewelsInStones(jewels, stones):
    Jset = set(jewels)
    return sum(s in Jset for s in stones)

jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))
# Output 3: You have 3 stones (a, A, A) that are also jewels.


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown

def numJewelsInStones(jewels, stones):
    Jset = set(jewels)        # Convert jewels to set for O(1) lookups
    return sum(s in Jset for s in stones)  # Count stones that are in jewels set



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


---
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


---
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
TLDR:
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





# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force 

def numJewelsInStones(J, S):
    return sum(s in J for s in S)


jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))
# Output 3


"""
Time: O(J × S)
    • Let J = length of jewels, S = length of stones.
    • The loop runs S times (once per stone).
    • Each s in J scans the jewels string → O(J) per check.
    • Combined: S checks × O(J) each → O(J × S).

Space: O(1)
    • No extra data structures — just the loop and a running count inside sum.
    • The generator (s in J for s in S) is consumed one item at a time, not stored.
"""



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



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Playground

"""
📘 Tutorial: sum(condition for x in items)

  • You can use sum() with a generator expression to count matches.

  • Each condition produces True (1) or False (0).

  • sum() adds them up → count of items where condition is True.
"""

# Example: condition for x in items:
nums = [1, 2, 3, 4]
evens = sum(x % 2 == 0 for x in nums)
print(evens)   # Output 2 (since 2 and 4 are even)


# Example: condition for x in items:
def fn(nums):
    return sum(num % 2 == 0 for num in nums)

nums = [1, 2, 3, 4]
print(fn(nums))   # Output 2 (since 2 and 4 are even)
