# 349. Intersection of Two Arrays
"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Array Intersection - The intersection of two arrays is defined as the set of elements that are present in both arrays.

Example 1:
    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2]

Example 2:
    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [9,4]
    Explanation: [4,9] is also accepted.
 
Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000


Solution: https://leetcode.com/problems/intersection-of-two-arrays/description/

"""


# Hash set + one pass (recommended to invest in)
def intersection(nums1, nums2):
    lookup = set(nums2)   # fast "is x in nums2?"
    seen = set() # values already added to answer
    result = []

    for x in nums1:
        if x in lookup and x not in seen:
            seen.add(x)
            result.append(x)

    return result


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

print(intersection(nums1, nums2))
# Output: [2]


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown

def intersection(nums1, nums2):
    lookup = set(nums2)          # Put every nums2 value in a fast checklist
    seen = set()                 # Numbers we already added to the answer
    result = []                  # Start with an empty intersection list

    for x in nums1:              # Go through each number in nums1
        if x in lookup and x not in seen:  # In both arrays and not added yet
            seen.add(x)          # Remember we used this number
            result.append(x)     # Add it to the answer

    return result                # Return unique values in both arrays


"""
Time: O(N + M)
  - Let N = length of nums1, M = length of nums2.
  - Build lookup = set(nums2) → O(M) to walk nums2 and store unique values.
  
  - Loop through every x in nums1 → O(N).
  - Each loop step: check x in lookup and x not in seen → O(1) average for sets.
  - Maybe add to seen and result → O(1).
  - Combined: O(M + N).
  - Overall: O(N + M).


Space: O(N + M)
  - lookup stores unique values from nums2 → up to M entries.
  - seen stores values already added to the answer → at most N entries.
  - result list holds the same values as seen → at most N entries.
  - A few extra variables (x, loop counter) → O(1).
  - Combined: O(N + M) in the worst case (many unique numbers).


Interview Answer: Worst Case

Time: O(N + M)
  - One pass to build a set from nums2, then one pass through nums1 with O(1) set checks.

Space: O(N + M)
  - Two sets (lookup and seen) plus the result list in the worst case.


---
Most IMPORTANT thing to Understand:
    • Intersection means: only numbers that appear in BOTH nums1 and nums2.

    • Each number in the answer must appear only once (duplicates in the input do not count twice).

    • lookup = a fast checklist of everything in nums2 — so we can ask "is x in nums2?" in O(1).

    • seen = numbers we already put in the answer — so we never add the same value twice.

---
Why this code Works:
    • Hash set role:
        • lookup stores all unique values from nums2.
        • seen tracks values already added to result.

    • One-pass scan:
        • Walk nums1 left to right.
        • If x is in lookup AND x is not in seen → x is in both arrays and not added yet → add it.

    • Efficiency:
        • Building lookup is O(M); scanning nums1 is O(N).
        • Set checks are O(1) average — much faster than nested loops through both arrays.

    • Intuition:
        • Think of lookup as "what nums2 has."
        • Walk nums1 and collect matches once — like checking items off a shared list.

---
TLDR:
    • Put nums2 in a set, scan nums1, and add each value that is in both arrays exactly once.


---
Quick Example Walkthrough:

    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]

    Step 1: Build lookup from nums2
        lookup = {2}

    Step 2: Scan nums1
        • x = 1 → not in lookup → skip
        • x = 2 → in lookup, not in seen → add 2 → result = [2], seen = {2}
        • x = 2 → in lookup, but already in seen → skip
        • x = 1 → not in lookup → skip

    Final Answer: [2]


---
Full Example Walkthrough:
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]

    Starting State:
        lookup = set(nums2) → {2}
        seen = {}
        result = []

    --------------------------------------------------

    Loop Iteration 1:
        x = nums1[0] = 1

        Check:
            1 in lookup? → NO

        Action:
            Skip — 1 is not in nums2

        Current state:
            seen = {}
            result = []

    --------------------------------------------------

    Loop Iteration 2:
        x = nums1[1] = 2

        Check:
            2 in lookup? → YES
            2 not in seen? → YES

        Action:
            seen.add(2)
            result.append(2)

        Current state:
            seen = {2}
            result = [2]

    --------------------------------------------------

    Loop Iteration 3:
        x = nums1[2] = 2

        Check:
            2 in lookup? → YES
            2 not in seen? → NO (already added)

        Action:
            Skip — duplicate in nums1, already in answer

        Current state:
            seen = {2}
            result = [2]

    --------------------------------------------------

    Loop Iteration 4:
        x = nums1[3] = 1

        Check:
            1 in lookup? → NO

        Action:
            Skip

        Current state:
            seen = {2}
            result = [2]

    --------------------------------------------------

    Final Check:
        return result → [2]

        This means:
            2 is the only value that appears in both arrays (counted once).


---
Overview for Each Iteration
Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]

Build lookup from nums2, then scan nums1

i | x | in lookup? | in seen? | Action | result
--|---|------------|----------|--------|--------
- | - | -          | -        | lookup = {2}, seen = {}, result = [] | []
0 | 1 | No         | -        | skip   | []
1 | 2 | Yes        | No       | add 2  | [2]
2 | 2 | Yes        | Yes      | skip   | [2]
3 | 1 | No         | -        | skip   | [2]

Final: [2]


---
🧠 First Time? Thoughts → Code

Read the problem (10 sec)
    • Return values that appear in **both** nums1 and nums2.

    • Each value in the answer counts **once** — duplicates in the input do not count twice.

    • Order does not matter.

Start naive (totally fine)
    • For each `x` in nums1, loop through nums2 — if you find `x` and it's not already in `result`, append it.

    • O(N × M) — fine as a first answer, slow when arrays get big.

The one insight that unlocks the optimal code
    • **Membership** is the hard part: "is `x` in the other array?" — do that in O(1), not by scanning a list every time.

    • Put all of nums2 into a **set** (`lookup`) → instant yes/no checks.

    • Walk nums1 once; when `x` is in `lookup`, it's in both arrays.

    • Use a second set (`seen`) so a duplicate in nums1 (like the second `2`) does not get added twice.

Why a hash set? (only if needed)
    • Two separate arrays — no sorted order to exploit with two pointers (unless you sort first, which is extra work).

    • A set is the standard tool when you need "have I seen this value?" or "does the other list contain this?" fast.

    • `seen` is only there because the problem says **unique** output, not because sets are always required.

Thought → line of code
    • `lookup = set(nums2)`
        → Remember everything nums2 has before the main loop.

    • `seen = set()`
        → Track values already added so duplicates in nums1 do not duplicate the answer.

    • `result = []`
        → Build the intersection list to return.

    • `for x in nums1`
        → Pick one array to scan; nums2 is already "pre-loaded" in `lookup`.

    • `if x in lookup and x not in seen`
        → In both arrays, and first time we're adding this value.

    • `seen.add(x)` + `result.append(x)`
        → Mark as used and save to the answer.

    • `return result`
        → Done — any order is fine.

Memory hook (one sentence)
    • Hash nums2 into a set, walk nums1, add each match once.

Would you arrive at this cold?
    • Immediately: nested loops ("check every pair") — totally natural.

    • After "membership is slow on a list": you'd think to use a set for nums2 — that's the main unlock.

    • `seen` is easy to forget until `[1,2,2,1]` makes you add `2` twice — then dedup clicks.

    • `lookup` = the real insight; `seen` + `result` = bookkeeping for unique output.

"""






# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Single set — same idea as lookup + seen, but one set + remove

def intersection_single_set(nums1, nums2):
    set1 = set(nums1)          # What's in nums1 (fast lookup)
    ans = []

    for i in nums2:            # Walk nums2
        if i in set1:          # In both arrays?
            ans.append(i)      # Add to answer
            set1.remove(i)     # Can't match this value again (handles duplicates)

    return ans

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection_single_set(nums1, nums2))
# Output: [2]

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown

def intersection_single_set(nums1, nums2):
    set1 = set(nums1)        # Unique values from nums1
    ans = []

    for i in nums2:          # Check each nums2 value
        if i in set1:        # Also in nums1?
            ans.append(i)    # Save it once
            set1.remove(i)   # Remove so second 2 in nums2 won't add again

    return ans


"""
Time: O(N + M)
  - N = len(nums1), M = len(nums2).
  - set(nums1) → O(N).
  - Loop nums2 → O(M); each in / remove → O(1) average.
  - Overall: O(N + M).

Space: O(N)
  - set1 holds up to N unique values from nums1.
  - ans holds the intersection (≤ N).
  - Overall: O(N) — one set vs two in lookup + seen.


Interview Answer: Worst Case

Time: O(N + M)
  - Build set from nums1, one pass over nums2.

Space: O(N)
  - One set plus the answer list.


---
How it works (concise)
    • Put nums1 in a set → O(1) "is this in nums1?"
    • Scan nums2; if value is in the set, append and remove from set.
    • remove = same job as seen in the two-set version — each intersection value added once.

    • Same pattern as lookup + seen above; one fewer structure.

---
TLDR
    • Hash nums1, walk nums2, add matches once via remove.


---
Overview (nums1 = [1,2,2,1], nums2 = [2,2])
    set1 starts = {1, 2}

    i=2 → in set1 → ans=[2], set1={1}
    i=2 → not in set1 → skip

    Final: [2]

"""



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Built-in Set Intersection
def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection(nums1, nums2))
# Output: [2]

# Time: O(N + M)
# Space: O(N + M)




# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force — nested loops (scan nums2 for every x in nums1)
def intersection_bruteforce(nums1, nums2):
    result = []

    for x in nums1:
        in_nums2 = False
        for y in nums2:
            if x == y:
                in_nums2 = True
                break

        if in_nums2 and x not in result:
            result.append(x)

    return result


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection_bruteforce(nums1, nums2))
# Output: [2] → For each nums1 value, scan nums2; add once if found in both


"""
Time: O(N * M)
  - Let N = length of nums1, M = length of nums2.

  - Outer loop walks every x in nums1 → O(N).

  - Inner loop scans nums2 to see if x appears → O(M) per x.

  - Check x not in result before append → O(N) per x in worst case (list scan).

  - Combined: O(N * (M + N)).
  - Worst case: O(N * M) when the inner nums2 scan dominates.


Space: O(K)
  - result stores up to K unique intersection values (K ≤ N).
  - Only a few extra variables (x, y, in_nums2).
  - Overall: O(K) ≈ O(N) for the output list.


Interview Answer: Worst Case

Time: O(N * M)
  - For each value in nums1, scan all of nums2 to check membership.

Space: O(N)
  - Result list holds up to N unique values.


---
Overview for Each Iteration
Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]

For each x in nums1, scan nums2; add x once if found

i | x | found in nums2? | in result? | Action | result
--|---|-----------------|------------|--------|--------
0 | 1 | No              | -          | skip   | []
1 | 2 | Yes (y=2)       | No         | add 2  | [2]
2 | 2 | Yes (y=2)       | Yes        | skip     | [2]
3 | 1 | No              | -          | skip   | [2]

Final: [2]

"""









# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# My first attempt (before looking up the solution) — two frequency dicts
# Valid & optimal time — counts are unused here; sets would be enough for 349

from collections import defaultdict

def intersection_first_attempt(nums1, nums2):
    count1 = defaultdict(int)
    for n in nums1:
        count1[n] += 1

    count2 = defaultdict(int)
    for n in nums2:
        count2[n] += 1

    ans = []
    for key in count1:
        if key in count2:
            ans.append(key)

    return ans


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection_first_attempt(nums1, nums2))
# Output: [2]
# count1 = {1: 2, 2: 2}   count2 = {2: 2}   → key 2 in both → [2]


"""
Breakdown (concise)
    • Count how many times each number appears in nums1 and nums2.
    • Loop keys in count1 — if that key also exists in count2, it's in both arrays.
    • Append once per key (dict keys are already unique → no extra seen set).

Time: O(N + M)
  - Count nums1 → O(N), count nums2 → O(M), loop count1 keys → O(U) with U ≤ N.
  - Overall: O(N + M).

Space: O(N + M)
  - Two dicts of unique values + answer list.
  - Overall: O(N + M) worst case.

Interview: Time O(N + M), Space O(N + M) — same class as the set solution; dict counts are overkill for 349 but useful prep for Intersection II (350).

"""
