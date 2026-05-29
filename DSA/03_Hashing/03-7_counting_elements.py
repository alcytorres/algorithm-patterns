# 1426. Counting Elements
"""
Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr. 

If there are duplicates in arr, count them separately.

Example:
    Input: arr = [1, 2, 2, 3]
    Output: 3
    Explanation: 1, 2, and 2 are counted cause 2 and 3 are in arr.

Solution: https://leetcode.com/problems/counting-elements/solutions/567376/counting-elements/
"""

# Optimized Solution: Search with HashSet
def countElements(arr):
    seen = set(arr)
    count = 0
    
    for x in arr:
        if x + 1 in seen:
            count += 1
    return count

arr = [1, 2, 2, 3]
print(countElements(arr))
# Output: 3 → 1, 2, and 2 are counted cause 2 and 3 are in arr.


# ––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown

def countElements(arr):
    seen = set(arr)       # Convert array to set for O(1) lookups
    count = 0             # Initialize counter for elements with x+1

    for x in arr:           # Iterate over each element in array
        if x + 1 in seen:   # Check if x+1 exists in set
            count += 1      # Increment counter if x+1 found
    return count            # Return total count of valid elements


"""
Time: O(N)
  - Let N = length of arr, U = number of unique elements.
  - Step 1: Build set from arr → O(N).
      • Each insertion into the set is O(1) average.
  - Step 2: Loop through arr → O(N).
      • For each x, check if x + 1 is in seen → O(1) average per check.
  - Combined: O(N + N) = O(N).
  - Overall: O(N).

Space: O(U) ≈ O(N)
  - Set 'seen' stores up to U unique values from arr.
  - Only a few extra variables (count, x).
  - Overall: O(U).
  - Worst case: U = N (all unique), so O(N).


Interview Answer: Worst Case

Time: O(N)
  - One pass to build the hash set, one pass to check each number.

Space: O(N)
  - Hash set stores up to N unique values.


---
🧠 First Time? Thoughts → Code

Read the problem (10 sec)
    • Count how many elements x have x + 1 also in arr.

    • Duplicates count separately — that's the key constraint hint.

Start naive (totally fine)
    • Loop each x, check if x + 1 in arr with a list lookup.
    • Say out loud: "For every number, search the array for the next number."
    • Time: O(N²) — N elements × N scan each.


The one insight that unlocks the optimal code
    • We're doing the same question N times: "Is this value in arr?"
    • That's a lookup problem — not a loop problem.
    • Put arr in a set once → every lookup becomes O(1).
    • Still loop arr (not the set) so duplicates get counted.


Why a hash set?
    • We only need yes/no: "does x + 1 exist?"
    • Set gives O(1) membership check; list gives O(N).
    • We don't need order or counts — just presence.


Thought → line of code
    seen = set(arr)
        → "I need fast lookup — load everything into a set first."

    for x in arr:
        → "Loop the original array so duplicates are checked separately."

    if x + 1 in seen:
        → "Is the NEXT number in my catalog? Check the set, not the list."

    count += 1
        → "Found a partner — count this x."


Memory hook (one sentence)
    • Set = catalog of what's in arr; loop arr and count x when x + 1 is in the catalog.


Would you arrive at this cold?
    • Immediately: loop arr, if x + 1 in arr, count++ — that's the logic.
    • After "lookup is slow": swap in a set for the in-check.
    • Bookkeeping: count = 0, return count — you write those on instinct.
    • Real insight: duplicates mean loop arr; speed means check seen not arr.


---
Overview for Each Iteration
    Input: arr = [1, 2, 2, 3]

    Step 1: Create set of unique elements
    seen = {1, 2, 3}

    Step 2: Count elements x where x + 1 is in seen
    x   | x + 1 | x + 1 in seen     | count
    ----|-------|-------------------|------
    1   | 2     | True              | 1
    2   | 3     | True              | 2
    2   | 3     | True              | 3
    3   | 4     | False             | 3

Final: 3



---
Most IMPORTANT thing to Understand:
    • For each element x in arr, ask: "Is x + 1 also in arr?"

    • If yes, count that x. If no, skip it.

    • Duplicates count separately — we loop through arr, not the set.

    • The set (seen) is only for fast lookup. It does NOT control what gets counted.


---
Why this code Works:
    • Hash set role:
        • seen = set(arr) stores every unique value from arr.
        • Lets us check "is x + 1 in arr?" in O(1) instead of scanning the whole list.

    • Loop through arr:
        • For each x, check if x + 1 in seen.
        • If true → x has a partner (x + 1) in arr → count += 1.

    • Efficiency:
        • Set lookup: O(1) per check → N checks = O(N) total.
        • List lookup would be O(N) per check → O(N²) total.

    • Intuition:
        • Think of seen as a catalog of every number in arr.
        • For each number x, you flip to the page for x + 1 — if it's there, count x.


---
TLDR:
    • Build a set of all values, then loop arr and count every x where x + 1 exists in the set.


---
Quick Example Walkthrough:
    arr = [1, 2, 2, 3]

    Step 1: Build set
        seen = {1, 2, 3}

    Step 2: Check each x in arr
        x=1 → is 2 in seen? Yes → count = 1
        x=2 → is 3 in seen? Yes → count = 2
        x=2 → is 3 in seen? Yes → count = 3  (duplicate counted again)
        x=3 → is 4 in seen? No  → count = 3

    Final Answer: 3


---
Full Example Walkthrough:
    arr = [1, 2, 2, 3]

    Starting State:
        seen = {1, 2, 3}
        count = 0

    Loop Iteration 1:
        x = 1
        Check: x + 1 in seen → 2 in {1, 2, 3} → True
        count += 1 → count = 1

    --------------------------------------------------

    Loop Iteration 2:
        x = 2
        Check: x + 1 in seen → 3 in {1, 2, 3} → True
        count += 1 → count = 2

    --------------------------------------------------

    Loop Iteration 3:
        x = 2  (duplicate — checked again because we loop arr)
        Check: x + 1 in seen → 3 in {1, 2, 3} → True
        count += 1 → count = 3

    --------------------------------------------------

    Loop Iteration 4:
        x = 3
        Check: x + 1 in seen → 4 in {1, 2, 3} → False
        count stays 3

    --------------------------------------------------

    Final Check:
        return count → 3
        Meaning: 1, 2, and 2 each have their x + 1 partner in arr.

"""



# ––––––––––––––––––––––––––––––––––––––––––––––––
# Set Lookup vs List Lookup Inside the Loop
# The loop always runs N times. What changes is the cost of each check inside it.

arr = [1, 2, 2, 3]
seen = set(arr)

# Set lookup inside loop - O(N) 
count = 0
for x in arr:
    if x + 1 in seen:   # Time: O(1) per check
        count += 1
# Time: O(N)  |  Space: O(N) for the set

# List lookup inside loop - O(N²)
count = 0
for x in arr:
    if x + 1 in arr:    # Time: O(N) per check
        count += 1
# Time: O(N²)  |  Space: O(1) — no extra structure


"""
Set lookup (x + 1 in seen):
  Time:  O(N)  — N checks × O(1) each
  Space: O(N) — hash set stores up to N elements

List lookup (x + 1 in arr):
  Time:  O(N²) — N checks × O(N) each
  Space: O(1)  — only count and loop variable


---
Trade-off (interview answer):
  • Set = faster time O(N), costs more memory O(N)
  • List = slower time O(N²), uses less memory O(1)
  Choose the set because:
    - We do N lookups (one per element)
    - List: each lookup scans the whole array → N × N = slow
    - Set: each lookup is instant → N total checks = fast
    - Example: N = 1,000 → list ~1,000,000 checks vs set ~1,000
  Use list only when N is tiny and memory is very tight.



---
Q: Why use a set instead of a array for lookups?
    • Set lookups are O(1) on average (hash table).
    • Array lookups are O(n) since they scan sequentially.

    
Q: What is the key idea of the solution?
    • Store all numbers in a hash set.
    • For each number x in arr, check if x+1 exists in the set.
    • Count it if true.

    
Q: Why do duplicates count separately?
    • We iterate through arr directly, so duplicates are checked individually.


"""



# –––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force: Approach: Search with Array

def countElements(arr):
    count = 0
    for x in arr:
        if x + 1 in arr:
            count += 1
    return count

arr = [1, 2, 3]
print(countElements(arr))
# Output: 2

"""
Time: O(N^2)
  - Outer loop iterates over all n elements: 0(N).
  - 'x + 1 in arr' is a list lookup, which takes 0(N) in the worst case.
  - Overall: O(N * N) = O(N^2) time.

Space: O(1)
  - Only a constant number of variables (count, x) are used.
  - No additional data structures.
  - Overall: O(1) space.

🔑 Key Difference: Set vs. List Lookup Complexity
    • Set lookup: O(1) on average — uses a hash table for near-instant access.

    • List lookup: 0(N) — requires scanning elements sequentially until a match is found.




Q: ⚠️ Why This Solution is Inefficient?
    • Each x+1 in arr lookup is O(n) because arr is a list.

    • You do this for every element (n iterations).

    • Total time complexity = O(n²).

    • For small inputs, fine. For large arr (like 10⁵ elements), this will time out on LeetCode.

"""