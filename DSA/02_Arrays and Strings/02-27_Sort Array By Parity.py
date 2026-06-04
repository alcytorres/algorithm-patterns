# 905. Sort Array By Parity

"""
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

Example 1:
    Input: nums = [3, 1, 2, 4]
    Output: [2, 4, 3, 1]
    Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Example 2:
    Input: nums = [0]
    Output: [0]
 
Constraints:
    1 <= nums.length <= 5000
    0 <= nums[i] <= 5000

"""

# Solution — One pass: read / write + swap

def sortArrayByParity(nums):
    write = 0
    
    for read in range(len(nums)):
        if nums[read] % 2 == 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1
    
    return nums

nums = [3, 1, 2, 4]
print(sortArrayByParity(nums))
# Output: [2, 4, 3, 1] → One pass swaps each even to the front so all evens come before all odds


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown

def sortArrayByParity(nums):
    write = 0       # Next open spot at the front for an even

    for read in range(len(nums)):   # Walk through every index in the array
        if nums[read] % 2 == 0:     # This number is even
            nums[write], nums[read] = nums[read], nums[write]  # Swap even to front, odd goes to read
            write += 1    # Move the front spot one step right

    return nums          # Evens at start, odds after write


"""
Time: O(N)
  - Let N = length of nums.
  - One loop: read goes from 0 to N - 1 → N iterations.
  - Each iteration: check if even (nums[read] % 2) → O(1); maybe one swap → O(1).
  - Overall: O(N).


Space: O(1)
  - Only write (and read as the loop index); no extra arrays or hash maps.
  - Work is done in place on nums.
  - Overall: O(1).


Interview Answer: Worst Case

Time: O(N)
  - Single pass with read through the whole array; each step is constant time.

Space: O(1)
  - Only the write pointer (plus the loop index); no extra structures.


---
Overview for Each Iteration
Input: nums = [3, 1, 2, 4]

Read/write scan: swap each even to nums[write]; advance write.

i | nums[i] | even? | w (→after) | Action   | nums
--|---------|-------|------------|----------|-------------
0 | 3       | no    | 0          | skip     | [3,1,2,4]
1 | 1       | no    | 0          | skip     | [3,1,2,4]
2 | 2       | yes   | 0→1        | swap↔i   | [2,1,3,4]
3 | 4       | yes   | 1→2        | swap↔i   | [2,4,3,1]

Final: [2, 4, 3, 1] (evens at 0–1, odds at 2–3)



---
Most IMPORTANT thing to Understand:
    • Goal: all evens first, then all odds — every number must still appear exactly once.

    • `write` = next open slot at the front of the "evens zone."

    • `read` scans the whole array once.

    • When `nums[read]` is even, swap it with `nums[write]` and move `write` forward.

    • Swap (not copy) matters: copying an even to the front leaves stale evens and lost odds in the tail.

    • After the loop, indices `0` to `write - 1` are evens; `write` to end are odds.

---
Why this code Works:
    • Read / write pointers:
        • `read` visits every index left to right.
        • `write` tracks where the next even should go.

    • Even rule:
        • If `nums[read] % 2 == 0`, swap `nums[write]` and `nums[read]`.
        • The even lands at the front; whatever was at `write` (usually an odd) moves to `read`.

    • Odd rule:
        • If `nums[read]` is odd, do nothing — it may get swapped later when an even from the right passes through.

    • Efficiency:
        • One pass → O(N) time.
        • In-place swaps → O(1) extra space.
        • Beats building two new lists (extra O(N) memory).

    • Intuition:
        • Like sorting laundry: every time you spot a clean sock (even), toss it into the front pile and kick whatever was there back into the basket.

---
TLDR:
    • Scan once with `read`; when you see an even, swap it to `nums[write]` and advance `write`.
    • Swaps keep every number in the array — evens pack the front, odds naturally end up after `write`.


---
Quick Example Walkthrough:
    nums = [3, 1, 2, 4]

    Step 1: Start with write = 0

    Step 2: Scan with read
        • read=0, nums[0]=3 → odd → skip
        • read=1, nums[1]=1 → odd → skip
        • read=2, nums[2]=2 → even → swap with nums[0] → [2, 1, 3, 4], write=1
        • read=3, nums[3]=4 → even → swap with nums[1] → [2, 4, 3, 1], write=2

    Step 3: Return nums
        • evens at indices 0–1: [2, 4]
        • odds at indices 2–3: [3, 1]

    Final Answer: [2, 4, 3, 1]


---
Full Example Walkthrough:
    nums = [3, 1, 2, 4]

    Starting State:
        write = 0
        read = 0 (loop will visit 0, 1, 2, 3)

        nums = [3, 1, 2, 4]

    Loop Iteration 1 (read = 0):
        Check:
            nums[read] % 2 == 0
            3 % 2 == 0 → FALSE (odd)

        Action:
            Skip — no swap, write stays 0

        Now:
            write = 0
            nums = [3, 1, 2, 4]

    --------------------------------------------------

    Loop Iteration 2 (read = 1):
        Check:
            1 % 2 == 0 → FALSE (odd)

        Action:
            Skip — write stays 0

        Now:
            write = 0
            nums = [3, 1, 2, 4]

    --------------------------------------------------

    Loop Iteration 3 (read = 2):
        Check:
            2 % 2 == 0 → TRUE (even)

        Action:
            Swap nums[write] and nums[read]
            nums[0] ↔ nums[2] → [2, 1, 3, 4]
            write += 1 → write = 1

        Now:
            write = 1
            nums = [2, 1, 3, 4]

        Current state:
            Front even zone: nums[0] = 2
            read was at 2; odd 3 now sits at index 2 (safe until loop ends)

    --------------------------------------------------

    Loop Iteration 4 (read = 3):
        Check:
            4 % 2 == 0 → TRUE (even)

        Action:
            Swap nums[write] and nums[read]
            nums[1] ↔ nums[3] → [2, 4, 3, 1]
            write += 1 → write = 2

        Now:
            write = 2
            nums = [2, 4, 3, 1]

    --------------------------------------------------

    Final Check:
        return nums → [2, 4, 3, 1]

        This means:
            Indices 0–1 are evens: 2, 4
            Indices 2–3 are odds: 3, 1
            Every original value is still in the array exactly once



---
🧠 First Time? Thoughts → Code

Read the problem (10 sec)
    • Put all evens at the start of `nums`, then all odds.

    • Any valid order inside the even block and odd block is fine — you are partitioning, not fully sorting.

    • Return the array — every original number must still be there exactly once (not like Remove Element where the tail can be junk).

Start naive (totally fine)
    • Two buckets: loop `nums`, append evens to one list and odds to another, return `evens + odds`.

    • Or two passes: copy all evens to the front, then copy all odds after them (needs the original values or a snapshot).

    • Both are O(N) time, O(N) extra space — totally acceptable first answer.

The one insight that unlocks the optimal code
    • Same “pack a group at the front” idea as Remove Element / Move Zeroes — but you must keep **all** elements, not just the keepers.

    • `read` scans; `write` = next slot for an even.

    • When you see an even, **swap** it with `nums[write]` (don't only copy) — swap moves the odd out of the way so nothing is lost.

    • Odds you skip now may land at `read` after a swap; evens you haven't visited yet can still get pulled forward.

Why read/write + swap? (only if needed)
    • Copy-only (`nums[write] = nums[read]`) looks like Remove Element but breaks here — tail keeps duplicate evens and missing odds.

    • Swap exchanges even ↔ whatever sits at `write` (usually an odd) in one step, no extra array.

    • One pass, O(1) extra space.

Thought → line of code
    • `write = 0`
        → Empty “evens zone” starts at index 0.

    • `for read in range(len(nums))`
        → Check every element once.

    • `if nums[read] % 2 == 0`
        → Only act on evens; odds wait (may get swapped later).

    • `nums[write], nums[read] = nums[read], nums[write]`
        → Pull even to front; kick the old front value to `read` so it stays in the array.

    • `write += 1`
        → Even zone grew; next even goes one slot right.

    • `return nums`
        → Full array is valid: `nums[0:write]` evens, `nums[write:]` odds.

Memory hook (one sentence)
    • Scan with read; on even, swap to write and advance write — evens front, odds tail, one pass.

Would you arrive at this cold?
    • Immediately: two lists or two-pass copy — easy and correct.

    • In-place: you might try copy-to-front (like Remove Element) and get wrong output `[2,4,2,4]` until you realize the tail must hold odds, not leftovers.

    • Swap is the non-obvious fix — comes from “every element must still exist somewhere in nums.”

    • `read`/`write` names are pattern vocabulary; the real insight is partition with swap, not sort.


"""




# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force — two lists (evens + odds), return combined
# (905 accepts a new array; no copy-back loop needed)

def sortArrayByParity_bruteforce(nums):
    evens = []
    odds = []

    for x in nums:
        if x % 2 == 0:
            evens.append(x)
        else:
            odds.append(x)

    return evens + odds

nums = [3, 1, 2, 4]
print(sortArrayByParity_bruteforce(nums))
# Output: [2, 4, 3, 1] → Split into evens and odds lists, then return evens + odds


"""
Time: O(N)
  - Let N = length of nums.

  - Step 1: Loop through nums, sort each value into evens or odds → O(N).
      • Each step: check x % 2 → O(1); maybe one append → O(1).

  - Step 2: Return evens + odds (new list) → O(N).

  - Combined: O(N + N).
  - Overall: O(N).


Space: O(N)
  - `evens` and `odds` together store all N values.
  - `evens + odds` builds one more list of size N.
  - Overall: O(N).


Interview Answer: Worst Case

Time: O(N)
  - One pass to split, one concat to build the answer.

Space: O(N)
  - Extra lists hold every element.


---
Overview for Each Iteration
nums = [3, 1, 2, 4]

    evens starts = []
    odds starts = []

    read 3 → odd  → odds = [3]
    read 1 → odd  → odds = [3, 1]
    read 2 → even → evens = [2]
    read 4 → even → evens = [2, 4]

    return evens + odds → [2, 4, 3, 1]

Final: [2, 4, 3, 1]

"""
