# 2824. Count Pairs Whose Sum is Less than Target 
# Easy
"""
Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.
 

Example 1:
    Input: nums = [-1,1,2,3,1], target = 2
    Output: 3
    Explanation: There are 3 pairs of indices that satisfy the conditions in the statement:
    - (0, 1) since 0 < 1 and nums[0] + nums[1] = 0 < target
    - (0, 2) since 0 < 2 and nums[0] + nums[2] = 1 < target 
    - (0, 4) since 0 < 4 and nums[0] + nums[4] = 0 < target
    Note that (0, 3) is not counted since nums[0] + nums[3] is not strictly less than the target.

Example 2:
    Input: nums = [-6,2,5,-2,-7,-1,3], target = -2
    Output: 10
    Explanation: There are 10 pairs of indices that satisfy the conditions in the statement:
    - (0, 1) since 0 < 1 and nums[0] + nums[1] = -4 < target
    - (0, 3) since 0 < 3 and nums[0] + nums[3] = -8 < target
    - (0, 4) since 0 < 4 and nums[0] + nums[4] = -13 < target
    - (0, 5) since 0 < 5 and nums[0] + nums[5] = -7 < target
    - (0, 6) since 0 < 6 and nums[0] + nums[6] = -3 < target
    - (1, 4) since 1 < 4 and nums[1] + nums[4] = -5 < target
    - (3, 4) since 3 < 4 and nums[3] + nums[4] = -9 < target
    - (3, 5) since 3 < 5 and nums[3] + nums[5] = -3 < target
    - (4, 5) since 4 < 5 and nums[4] + nums[5] = -8 < target
    - (4, 6) since 4 < 6 and nums[4] + nums[6] = -4 < target
 

Constraints:
    1 <= nums.length == n <= 50
    -50 <= nums[i], target <= 50

"""

# Solution: Nested loops 
def countPairs(nums, target):
    count = 0
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):      # j starts after i, so i < j is free
            if nums[i] + nums[j] < target:
                count += 1

    return count


nums = [-1, 1, 2, 3, 1]
target = 2
print(countPairs(nums, target))
# Output: 3

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
def countPairs(nums, target):
    count = 0                      # Tally of pairs that work
    n = len(nums)                  # How many numbers we have

    for i in range(n):             # Pick the first number in the pair
        for j in range(i + 1, n):  # Pick a later number so i < j
            if nums[i] + nums[j] < target:  # Their sum is strictly below target
                count += 1         # Count this pair

    return count                   # Return how many pairs we found


"""
Time: O(N²)
  - Let N = length of nums.
  - Outer loop picks the first index i → runs N times.
  - Inner loop picks a later index j → for each i it checks the remaining numbers after i.
  - Total pair checks: (N-1) + (N-2) + ... + 1 = N(N-1)/2 → O(N²).
  - Each check adds two numbers and compares to target → O(1).
  - Overall: O(N²).

Space: O(1)
  - Only a few variables are used: count, n, i, j.
  - No extra list, dictionary, or copy of nums.
  - Overall: O(1).


Interview Answer: Worst Case

Time: O(N²)
  - Nested loops check every pair of numbers once.

Space: O(1)
  - Only a running count and loop indices are used.
"""


"""
---
Most IMPORTANT thing to Understand:

    • A pair is two different indices (i, j) with i < j.

    • We count a pair only when nums[i] + nums[j] is strictly less than target — equal does not count.

    • The inner loop starts at i + 1, so we never reuse the same index and never count the same pair twice.

    • count is a running tally of how many pairs passed the test.

---
Why this code Works:

    • Nested loops:
        • Outer loop picks the first index i.
        • Inner loop picks every later index j.
        • Together they visit every valid pair exactly once.

    • The check:
        • Add the two numbers.
        • If the sum is below target, add 1 to count.

    • Efficiency:
        • n is at most 50, so checking every pair is fine.
        • Time: O(N²). Space: O(1).

    • Intuition:
        • Like lining people up and pairing each person with everyone standing to their right.
        • Each pair gets one handshake. Count the handshakes whose numbers add up below target.

---
TLDR:

    • This works because it tries every pair with i < j and counts the ones whose sum is strictly less than target.


---
Quick Example Walkthrough:

    nums = [-1, 1, 2, 3, 1], target = 2

    Step 1: Start
        count = 0

    Step 2: Check every pair (i, j) with j after i
        • i=0 (-1): partners 1, 2, 3, 1 → sums 0, 1, 2, 0 → three are < 2 → count = 3
        • i=1 (1):  partners 2, 3, 1 → sums 3, 4, 2 → none
        • i=2 (2):  partners 3, 1 → sums 5, 3 → none
        • i=3 (3):  partner 1 → sum 4 → none

    Final Answer: 3


---
Full Example Walkthrough:

    nums = [-1, 1, 2, 3, 1]
    target = 2

    Starting State:
        count = 0
        n = 5

    --------------------------------------------------

    Outer i = 0 (nums[0] = -1)

        j = 1: -1 + 1 = 0 < 2 → YES → count = 1

        j = 2: -1 + 2 = 1 < 2 → YES → count = 2

        j = 3: -1 + 3 = 2 < 2 → NO (equal is not strictly less)

        j = 4: -1 + 1 = 0 < 2 → YES → count = 3

    --------------------------------------------------

    Outer i = 1 (nums[1] = 1)

        j = 2: 1 + 2 = 3 < 2 → NO

        j = 3: 1 + 3 = 4 < 2 → NO

        j = 4: 1 + 1 = 2 < 2 → NO

        count stays 3

    --------------------------------------------------

    Outer i = 2 (nums[2] = 2)

        j = 3: 2 + 3 = 5 < 2 → NO

        j = 4: 2 + 1 = 3 < 2 → NO

        count stays 3

    --------------------------------------------------

    Outer i = 3 (nums[3] = 3)

        j = 4: 3 + 1 = 4 < 2 → NO

        count stays 3

    --------------------------------------------------

    Outer i = 4:
        No later index j exists, so the inner loop does not run.

    --------------------------------------------------

    Final Check:
        return count
        return 3

        This means:
            Three pairs had a sum strictly less than 2: (0, 1), (0, 2), and (0, 4).


---
Overview for Each Iteration
Input: nums = [-1, 1, 2, 3, 1], target = 2

Check every pair (i, j) with j after i. Count when sum < target.

i | j | sum | Action  | count
--|---|-----|---------|------
- | - | -   | start   | 0
0 | 1 | 0   | count++ | 1
0 | 2 | 1   | count++ | 2
0 | 3 | 2   | skip    | 2
0 | 4 | 0   | count++ | 3
1 | 2 | 3   | skip    | 3
1 | 3 | 4   | skip    | 3
1 | 4 | 2   | skip    | 3
2 | 3 | 5   | skip    | 3
2 | 4 | 3   | skip    | 3
3 | 4 | 4   | skip    | 3

Final: 3


---
🧠 First Time? Thoughts → Code

Read the problem (10 sec)
    • Count how many pairs of indices (i, j) have i < j and nums[i] + nums[j] < target.

    • We need a count, not the pairs themselves.

    • n ≤ 50 — checking every pair is fine. Also: strictly less than, not equal.

Start naive (totally fine)
    • Two loops: pick i, then pick every j after i, add the two numbers, count if below target.

    • O(N²) — and for this problem that is the solution, not a draft you throw away.

The one insight that unlocks this code
    • There is no hidden trick. The problem statement is the algorithm.

    • `j` starting at `i + 1` is how you get `i < j` for free — no extra if, no double-counting.

    • Equal sums do not count. Write `< target`, not `<=`.

Why nested loops? (not a hash map)
    • Hash maps are for "equals target" (Two Sum). Here the question is "less than target," so you still have to check a range of partners.

    • With n ≤ 50, just try every pair.

Thought → line of code
    • `count = 0`
        → Running tally of pairs that pass.

    • `n = len(nums)`
        → Use it twice in the ranges — optional, just cleaner.

    • `for i in range(n)`
        → First index in the pair.

    • `for j in range(i + 1, n)`
        → Second index must be later. This is the line that encodes `i < j`.

    • `if nums[i] + nums[j] < target`
        → The problem's condition, word for word.

    • `count += 1`
        → One more valid pair.

    • `return count`
        → Bookkeeping.

Memory hook (one sentence)
    • For each number, try every number to its right, and count the sums that stay strictly below target.

Would you arrive at this cold?
    • Immediately: nested loops. This is the first thing you'd say out loud.

    • The one easy miss: starting `j` at 0 instead of `i + 1` (double-counts and pairs an index with itself).

    • After doing Two Sum, the trap is reaching for a hash map — skip it; "less than" is not a lookup.

    • `count = 0` / `return count` are bookkeeping; the real line is `for j in range(i + 1, n)`.
"""









# Solution: Sort + two pointers
def countPairs(nums, target):
    nums.sort()
    count = 0
    left, right = 0, len(nums) - 1

    while left < right:
        if nums[left] + nums[right] < target:
            count += right - left   # all of (left, left+1) ... (left, right) work
            left += 1
        else:
            right -= 1

    return count

nums = [-1, 1, 2, 3, 1]
target = 2
print(countPairs(nums, target))
# Output: 3


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
def countPairs(nums, target):
    nums.sort()                    # Line up from small to big
    count = 0                      # Tally of pairs that work
    left, right = 0, len(nums) - 1  # Start at both ends

    while left < right:            # Keep going until they meet
        if nums[left] + nums[right] < target:  # Smallest + largest still below target
            count += right - left  # All in-between also work with left
            left += 1              # Try the next small number
        else:
            right -= 1             # Sum too big — shrink from the right

    return count                   # Return how many pairs we found


"""
Time: O(N log N)
  - Let N = length of nums.
  - nums.sort() lines the array up from small to big → O(N log N).
  - Then two pointers walk from both ends. Each step moves left or right by 1, so at most N - 1 steps → O(N).
  - Combined: O(N log N + N).
  - Overall: O(N log N) — sorting is the slow part.

Space: O(1) extra, O(N) in Python
  - Only a few variables: count, left, right.
  - We sort nums in place — no extra list of our own.
  - Python's list.sort() (Timsort) may use O(N) internal buffers.
  - Algorithmically: O(1) extra space.
  - Worst case in Python: O(N).


Interview Answer: Worst Case

Time: O(N log N)
  - Sorting dominates. The two-pointer scan is only O(N).

Space: O(N)
  - A few pointers plus Python sort's extra buffers.
"""


"""
---
Most IMPORTANT thing to Understand:

    • We only need a COUNT of pairs, not the original indices — so sorting is allowed.

    • After sorting, the most useful pair to test is smallest + largest (left + right).

    • If that sum is still < target, then left + every number between left and right also works — those numbers are all ≤ nums[right].

    • That is why we add a whole batch at once: count += right - left.

    • If the sum is too big, shrink from the right. If it works, we are done with this left, so move left in.

---
Why this code Works:

    • Sorting:
        • Puts numbers in order so "too small" and "too big" have a direction to move.

    • Two pointers:
        • left = current small number.
        • right = current large number.
        • We keep left < right so each pair uses two different spots.

    • If nums[left] + nums[right] < target:
        • Partners of left from index left+1 through right all work.
        • That is (right - left) pairs.
        • Then left += 1 to try the next small number (right can stay — it may still work with the new left).

    • If the sum is ≥ target:
        • This large number is too big even for the current small number.
        • right -= 1.

    • Efficiency:
        • Sort once, then each pointer only moves inward.
        • Time: O(N log N). Space: O(1) extra (O(N) in Python for sort).

    • Intuition:
        • Line people up from shortest to tallest.
        • Pair the shortest with the tallest.
        • If they still fit under the height limit, everyone in between also fits with the shortest — count them all at once.

---
TLDR:

    • Sort, then test smallest + largest. If they still fit, count everyone in between with the small number. If not, drop the large number.


---
Quick Example Walkthrough:

    nums = [-1, 1, 2, 3, 1], target = 2

    Step 1: Sort
        nums = [-1, 1, 1, 2, 3]
        left = 0, right = 4, count = 0

    Step 2: Walk from both ends
        • -1 + 3 = 2  not < 2 → right = 3
        • -1 + 2 = 1  < 2 → add 3 pairs (right - left) → count = 3, left = 1
        •  1 + 2 = 3  not < 2 → right = 2
        •  1 + 1 = 2  not < 2 → right = 1
        • left == right → stop

    Final Answer: 3


---
Full Example Walkthrough:

    nums = [-1, 1, 2, 3, 1]
    target = 2

    After sort:
        nums = [-1, 1, 1, 2, 3]
        indices: 0    1  2  3  4

    Starting State:
        count = 0
        left = 0  → -1
        right = 4 → 3

    --------------------------------------------------

    Loop Iteration 1:
        Compare:
            nums[left] + nums[right] < target
            -1 + 3 = 2 < 2 → NO

        Sum is not strictly less, so shrink from the right:
            right -= 1
            right = 3

        Current state:
            left points at -1
            right points at 2
            count = 0

    --------------------------------------------------

    Loop Iteration 2:
        Compare:
            -1 + 2 = 1 < 2 → YES

        Every number from index 1 through 3 also works with -1:
            (-1, 1), (-1, 1), (-1, 2)
            count += right - left
            count += 3 - 0
            count = 3

        Done with this left, so move it in:
            left += 1
            left = 1

        Current state:
            left points at 1
            right points at 2
            count = 3

    --------------------------------------------------

    Loop Iteration 3:
        Compare:
            1 + 2 = 3 < 2 → NO

        Shrink from the right:
            right -= 1
            right = 2

        Current state:
            left points at 1 (index 1)
            right points at 1 (index 2)
            count = 3

    --------------------------------------------------

    Loop Iteration 4:
        Compare:
            1 + 1 = 2 < 2 → NO

        Shrink from the right:
            right -= 1
            right = 1

        Current state:
            left = 1
            right = 1
            They have met, so the loop stops.

    --------------------------------------------------

    Final Check:
        return count
        return 3

        This means:
            Three pairs had a sum strictly less than 2.
            We counted them in one batch when -1 paired with everything up to 2.


---
Overview for Each Iteration
Input: nums = [-1, 1, 2, 3, 1], target = 2

Phase 1: Sort
nums = [-1, 1, 1, 2, 3]

Phase 2: If sum < target, add (r - l) pairs and move l; else shrink r

l | r | sum | Action   | count
--|---|-----|----------|------
0 | 4 | -   | start    | 0
0 | 4 | 2   | r-=1     | 0
0 | 3 | 1   | +3, l+=1 | 3
1 | 3 | 3   | r-=1     | 3
1 | 2 | 2   | r-=1     | 3

Final: 3


---
🧠 First Time? Thoughts → Code

Read the problem (10 sec)
    • Count pairs with i < j whose sum is strictly less than target.

    • We need a count, not the original indices — that is the green light to sort.

    • n ≤ 50 so nested loops already pass. This version is the upgrade for when n is large.

Start naive (totally fine)
    • Two loops, check every pair, count += 1 when the sum is below target.

    • O(N²). Write that first. Then ask: "can sorted order let me skip work?"

The one insight that unlocks this code
    • After sorting, smallest + largest is the most informative pair.

    • If even that large partner still fits with left, every number in between also fits with left.

    • So you add a whole batch: count += right - left. You do not walk those partners one by one.

    • If the sum is too big, drop the large number (right -= 1). If it fits, you are done with this left (left += 1).

Why two pointers?
    • Sorted order gives the sums a direction: too small → move left in, too big → move right in.

    • Each pointer only moves toward the middle, so after the sort the scan is O(N).

    • A hash map still does not help — "less than target" is a range, not one lookup.

Thought → line of code
    • `nums.sort()`
        → Order the numbers so "too small / too big" tells you which pointer to move.
        → Legal because we only return a count.

    • `left, right = 0, len(nums) - 1`
        → Start at the smallest and the largest.

    • `while left < right`
        → Two different spots. Stop when they meet.

    • `if nums[left] + nums[right] < target`
        → Test the current extremes.

    • `count += right - left`
        → NOT intuitive. This is the whole trick: partners left+1 through right all work, so add them in one shot.

    • `left += 1`
        → Finished with this small number. Try the next one. Keep the same right — it may still work.

    • `else: right -= 1`
        → This large number is too big even for the current small one, so it is too big for everyone left of here too. Drop it.

    • `return count`
        → Bookkeeping.

Memory hook (one sentence)
    • Sort, then if smallest + largest still fits, count everyone in between with the small number; if not, drop the large one.

Would you arrive at this cold?
    • Immediately: nested loops. That is the natural first answer.

    • After "we only need a count, so I can sort": two pointers from both ends is a known pair-sum move.

    • What you would NOT invent on instinct: `count += right - left`. That is the line you study. Without it you still have a correct but slower "move right down until it fits, then count += 1" loop.

    • `nums.sort()` / `left, right = ...` / `while left < right` are setup; the real insight is the batch add, then move left.
"""

