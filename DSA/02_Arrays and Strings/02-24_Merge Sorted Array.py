# 88. Merge Sorted Array
"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:
    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]
    Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
    The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Constraints:
    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -109 <= nums1[i], nums2[j] <= 109
 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?

Solution: https://leetcode.com/problems/merge-sorted-array/description/
"""

# Soltuion: Backward two-pointer merge (fill from the end)
def merge(nums1, m, nums2, n):
    p1 = m - 1          # last real value in nums1
    p2 = n - 1          # last value in nums2
    write = m + n - 1   # last slot in nums1

    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[write] = nums1[p1]
            p1 -= 1
        else:
            nums1[write] = nums2[p2]
            p2 -= 1
        write -= 1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3

nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)
# Output: [1, 2, 2, 3, 5, 6] → Merge from the back: always place the larger of p1/p2 into the empty tail


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
def merge(nums1, m, nums2, n):
    p1 = m - 1          # Start at the last real number in nums1 (skip the empty zeros)
    p2 = n - 1          # Start at the last number in nums2
    write = m + n - 1   # Start writing into the last slot of nums1

    while p2 >= 0:      # Keep going until every nums2 value is placed
        if p1 >= 0 and nums1[p1] > nums2[p2]:  # If nums1's current pick is bigger
            nums1[write] = nums1[p1]            # Put that bigger nums1 value in the back
            p1 -= 1                             # Move nums1 pointer left
        else:
            nums1[write] = nums2[p2]            # Otherwise take nums2's current value
            p2 -= 1                             # Move nums2 pointer left
        write -= 1                              # Move write spot one slot to the left


"""
Time: O(M + N)
  - Let M = number of real elements in nums1, N = length of nums2.
  - Three pointers (p1, p2, write) compare and place one value per loop.
  - Each loop step does constant work: one compare, one write, move a pointer.
  - p2 moves left at most N times (every nums2 value gets placed).
  - p1 moves left at most M times (every nums1 value might get moved once).
  - Combined: at most M + N loop steps → O(M + N).
  - Overall: O(M + N).


Space: O(1)
  - Merge happens in-place inside nums1 (the extra zeros were the buffer).
  - Only a few integer variables: p1, p2, write.
  - No extra arrays or hash maps.
  - Overall: O(1).


Interview Answer: Worst Case

Time: O(M + N)
  - One backward pass: each nums2 element is placed once, and nums1 elements are moved at most once.

Space: O(1)
  - In-place merge using only pointer variables.


---
Most IMPORTANT thing to Understand:

• Both arrays are already sorted — the largest remaining value is always at p1 or p2.

• nums1 has empty room at the end (the zeros). That space is your scratch pad.

• If you merge from the front, you overwrite nums1 values you still need.

• So compare from the BACK and write into the empty tail first.

• Each step: pick the bigger of nums1[p1] and nums2[p2], put it at write, move that pointer left.

• Loop until p2 is done — any leftover nums1 values are already sitting in the right spots.


---
Why this code Works:

• Three pointers:
      • p1 = last real value in nums1 (index m - 1)
      • p2 = last value in nums2 (index n - 1)
      • write = last open slot in nums1 (index m + n - 1)

• At every step:
      • compare nums1[p1] and nums2[p2]
      • place the larger value at nums1[write]
      • move the pointer you took from, then move write left

• If nums1[p1] is bigger → take from nums1.

• Otherwise (nums2 is bigger OR equal, OR p1 ran out) → take from nums2.

• Why while p2 >= 0?
      • Every nums2 value must be copied into nums1.
      • When nums2 is empty, remaining nums1 values are already in order at the front.

• Efficiency:
      • Each value moves at most once.
      • Time: O(M + N).
      • Space: O(1) — no extra array.

• Intuition:
      • Two sorted stacks of cards, face-up, largest on top.
      • Always grab the bigger top card and slide it into the back of nums1.


---
TLDR:
    • Compare the current largest values from both arrays, write the bigger one to the back of nums1, and repeat until nums2 is fully merged.


---
Quick Example Walkthrough:

nums1 = [1, 2, 3, 0, 0, 0], m = 3
nums2 = [2, 5, 6], n = 3

Step 1: Start at the ends
    p1 → 3, p2 → 6, write → last slot

Step 2: Compare and fill from the back
    • 3 vs 6 → write 6 → [1, 2, 3, 0, 0, 6]
    • 3 vs 5 → write 5 → [1, 2, 3, 0, 5, 6]
    • 3 vs 2 → write 3 → [1, 2, 3, 3, 5, 6]
    • 2 vs 2 → write 2 → [1, 2, 2, 3, 5, 6]

Step 3: p2 is done — loop stops. Front values already correct.

Final Answer: [1, 2, 2, 3, 5, 6]


---
Full Example Walkthrough:

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    Starting State:
        p1 = 2          → nums1[2] = 3
        p2 = 2          → nums2[2] = 6
        write = 5       → last slot in nums1

        nums1: [1, 2, 3, 0, 0, 0]

    Loop Iteration 1:
        Compare:
            nums1[p1] > nums2[p2]
            3 > 6 → NO

        Take from nums2:
            nums1[write] = 6
            p2 -= 1  → p2 = 1
            write -= 1  → write = 4

        Current state:
            nums1: [1, 2, 3, 0, 0, 6]
            p1 → 3, p2 → 5, write → index 4

    --------------------------------------------------

    Loop Iteration 2:
        Compare:
            3 > 5 → NO

        Take from nums2:
            nums1[4] = 5
            p2 = 0
            write = 3

        Current state:
            nums1: [1, 2, 3, 0, 5, 6]
            p1 → 3, p2 → 2, write → index 3

    --------------------------------------------------

    Loop Iteration 3:
        Compare:
            3 > 2 → YES

        Take from nums1:
            nums1[3] = 3
            p1 = 1
            write = 2

        Current state:
            nums1: [1, 2, 3, 3, 5, 6]
            p1 → 2, p2 → 2, write → index 2

    --------------------------------------------------

    Loop Iteration 4:
        Compare:
            2 > 2 → NO  (equal counts as take nums2)

        Take from nums2:
            nums1[2] = 2
            p2 = -1
            write = 1

        Current state:
            nums1: [1, 2, 2, 3, 5, 6]
            p1 → 2, p2 → done, write → index 1

    --------------------------------------------------

    Final Check:
        p2 >= 0 → False → loop stops.

        nums1[0] and nums1[1] are already 1 and 2 — no moves needed.

        Final merged array: [1, 2, 2, 3, 5, 6]


---
Overview for Each Iteration
Input: nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3
Step: Compare largest remaining values; write bigger one to back of nums1

# | p1 | p2 | w | cmp (nums1[p1] vs nums2[p2]) | take  | nums1
--|----|----|---|-------------------------------|-------|-------------------
- | 2  | 2  | 5 | -                             | -     | [1, 2, 3, 0, 0, 0]
1 | 2  | 1  | 4 | 3 vs 6 → 6 wins               | nums2 | [1, 2, 3, 0, 0, 6]
2 | 2  | 0  | 3 | 3 vs 5 → 5 wins               | nums2 | [1, 2, 3, 0, 5, 6]
3 | 1  | 0  | 2 | 3 vs 2 → 3 wins               | nums1 | [1, 2, 3, 3, 5, 6]
4 | 1  | -1 | 1 | 2 vs 2 → tie, take nums2      | nums2 | [1, 2, 2, 3, 5, 6]

Final: [1, 2, 2, 3, 5, 6]
"""


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# 🧠 First Time? Thoughts → Code

"""
Read the problem (10 sec)
    • Merge two sorted arrays into one sorted array — but store the answer inside nums1.
    • nums1 is longer with zeros at the end → that extra space is the hint. Don't ignore it.

Start naive (totally fine)
    • "Copy nums2 into nums1, then sort." Or "make a new list, merge from the front like merge sort, copy back."
    • Works. O((m + n) log(m + n)) or O(m + n) with extra space. Say that out loud first if you're stuck.

The one insight that unlocks the optimal code
    • Both arrays are sorted → the largest remaining value is always at the end of nums1 or nums2.
    • Compare those two ends → the bigger one belongs at the back of the final array.
    • nums1's tail is empty (the zeros) → safe to write there without losing data you still need.
    • Repeat until every nums2 value is placed.

Why fill from the back?
    • Merging from the front overwrites nums1 values before you've moved them.
    • The empty slots live at the back → fill largest-first into those slots.
    • When nums2 runs out, leftover nums1 values are already in the right spots.

Thought → line of code
    p1 = m - 1
        → Start at the last real nums1 value, not the placeholder zeros.

    p2 = n - 1
        → Start at the last nums2 value (its "big end").

    write = m + n - 1
        → First open slot is the very back of nums1.

    while p2 >= 0
        → Every nums2 value must land in nums1.
        → When p2 is done, nums1's leftovers are already sorted at the front.

    if p1 >= 0 and nums1[p1] > nums2[p2]
        → Compare the two current largest picks.
        → p1 >= 0 guards when nums1 is exhausted.

    else branch (take nums2)
        → nums2 wins when it's bigger, equal, OR nums1 is empty.

    write -= 1
        → After each placement, next write spot moves one left.

Memory hook (one sentence)
    • Compare the two back-of-the-line values → put the bigger one in the empty tail → slide left.

Would you arrive at this cold?
    • Naive path: yes, immediately (combine + sort, or merge into a helper array).
    • Optimal path: only after you ask "why is nums1 longer with zeros at the end?"
    • p1 = m - 1, while p2 >= 0, and writing from the back are NOT first instincts —
      they come AFTER you decide to use the tail as free space. Then the code is just
      bookkeeping for that decision.
"""



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# More Soluttions

# Combine everything, then sort (the “I’m stuck” approach)
def merge(nums1, m, nums2, n):
    nums1[:m + n] = sorted(nums1[:m] + nums2)


nums1 = [1, 2, 3, 0, 0, 0]
m = 3

nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)
# Output: [1, 2, 2, 3, 5, 6] → Concatenate both parts and sort

"""
Time: O((M + N) log(M + N))
  - Concat nums1[:m] + nums2 → O(M + N).
  - sorted() on M + N elements → O((M + N) log(M + N)).
  - Overall: O((M + N) log(M + N)).

Space: O(M + N)
  - nums1[:m] + nums2 builds a new list of size M + N.
  - Overall: O(M + N).
"""


# Forward merge into a helper array (classic merge-sort step)
def merge(nums1, m, nums2, n):
    merged = []
    i, j = 0, 0

    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    merged.extend(nums1[i:m])
    merged.extend(nums2[j:n])
    nums1[:m + n] = merged


nums1 = [1, 2, 3, 0, 0, 0]
m = 3

nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)
# Output: [1, 2, 2, 3, 5, 6] → Classic forward merge into a helper list, then copy back

"""
Time: O(M + N)
  - Each element from nums1 and nums2 is compared and appended at most once.
  - Copy merged back into nums1 → O(M + N).
  - Overall: O(M + N).

Space: O(M + N)
  - merged list stores all M + N elements.
  - Overall: O(M + N).
"""
