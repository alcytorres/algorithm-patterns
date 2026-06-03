# 27. Remove Element
"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
    
    Return k.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.


Example 1:
    Input: nums = [3,2,2,3], val = 3
    Output: 2, nums = [2,2,_,_]
    Explanation: Your function should return k = 2, with the first two elements of nums being 2.
    It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
    Input: nums = [0,1,2,2,3,0,4,2], val = 2
    Output: 5, nums = [0,1,4,0,3,_,_,_]
    Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
    Note that the five elements can be returned in any order.
    It does not matter what you leave beyond the returned k (hence they are underscores).
    
Constraints:
    0 <= nums.length <= 100
    0 <= nums[i] <= 50
    0 <= val <= 100

Solution: https://leetcode.com/problems/remove-element/description/
"""


def removeElement(nums, val):
    write = 0

    for read in range(len(nums)):
        if nums[read] != val:
            nums[write] = nums[read]
            write += 1

    return write


nums = [3, 2, 2, 3]
val = 3
print(removeElement(nums, val))
# Output: 2  
# nums = [2, 2, _, _]


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown

def removeElement(nums, val):
    write = 0                         # Next open spot at the front for a kept value

    for read in range(len(nums)):     # Walk through every index in the array
        if nums[read] != val:         # This one is not the value we are removing
            nums[write] = nums[read]  # Copy it into the front we are building
            write += 1                # Move the front spot one step right

    return write                  # How many we kept (k); judge only checks nums[:k]


"""
Time: O(N)
  - Let N = length of nums.
  - One loop: read goes from 0 to N - 1 → N iterations.
  - Each iteration: check nums[read] != val → O(1); maybe one copy → O(1).
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
Input: nums = [3, 2, 2, 3], val = 3

Write-pointer scan: keep non-val elements at the front; skip val.

read | nums[read] | != val? | write (before→after) | Action | nums (full)
-----|------------|---------|----------------------|--------|------------------
0    | 3          | no      | 0                    | skip   | [3, 2, 2, 3]
1    | 2          | yes     | 0→1                  | copy→0 | [2, 2, 2, 3]
2    | 2          | yes     | 1→2                  | copy→1 | [2, 2, 2, 3]
3    | 3          | no      | 2                    | skip   | [2, 2, 2, 3]

Final: return write = 2; valid prefix nums[:2] = [2, 2] (indices 2–3 ignored)



---
Most IMPORTANT thing to Understand:
    • You are not shrinking the array — you are building the answer at the front.

    • `write` = next empty slot for a kept value, and also how many you have kept so far.

    • `read` scans the whole array once; if `nums[read] != val`, copy it to `nums[write]` and move `write` forward.

    • When done, return `write` as k. Only `nums[0:k]` matters; the rest can be junk.

---
Why this code Works:
    • Write pointer (in-place filter):
        • `read` looks at every element.
        • `write` collects all values that are not `val` at the front of nums.

    • Skip rule:
        • If `nums[read] == val`, do nothing — that element is dropped.
        • If `nums[read] != val`, place it at `nums[write]` and increment `write`.

    • Efficiency:
        • One pass → O(N) time.
        • No extra array → O(1) space.
        • Beats shifting or `.pop()` which can be O(N²).

    • Intuition:
        • Like packing a suitcase: scan each item, keep what you want at the front, ignore the rest.

---
TLDR:
    • Scan once with `read`; copy every non-val element to `nums[write]` and advance `write`.
    • Return `write` — that is k, and `nums[:k]` is your filtered array.


---
Quick Example Walkthrough:
    nums = [3, 2, 2, 3], val = 3

    Step 1: Start with write = 0

    Step 2: Scan with read
        • read=0, nums[0]=3 → equals val → skip
        • read=1, nums[1]=2 → keep → nums[0]=2, write=1
        • read=2, nums[2]=2 → keep → nums[1]=2, write=2
        • read=3, nums[3]=3 → equals val → skip

    Step 3: Return write
        • k = 2, valid prefix = [2, 2]

    Final Answer: 2 (nums[:2] = [2, 2]; tail ignored)


---
Full Example Walkthrough:
    nums = [3, 2, 2, 3], val = 3

    Starting State:
        write = 0
        read = 0 (loop will visit 0, 1, 2, 3)

        nums = [3, 2, 2, 3]

    Loop Iteration 1 (read = 0):
        Check:
            nums[read] != val
            nums[0] != 3 → 3 != 3 → FALSE

        Action:
            Skip — no copy, write stays 0

        Now:
            write = 0
            nums = [3, 2, 2, 3]

    --------------------------------------------------

    Loop Iteration 2 (read = 1):
        Check:
            nums[1] != 3 → 2 != 3 → TRUE

        Action:
            nums[write] = nums[read] → nums[0] = 2
            write += 1 → write = 1

        Now:
            nums = [2, 2, 2, 3]

    --------------------------------------------------

    Loop Iteration 3 (read = 2):
        Check:
            nums[2] != 3 → 2 != 3 → TRUE

        Action:
            nums[1] = 2
            write += 1 → write = 2

        Now:
            nums = [2, 2, 2, 3]

    --------------------------------------------------

    Loop Iteration 4 (read = 3):
        Check:
            nums[3] != 3 → 3 != 3 → FALSE

        Action:
            Skip — write stays 2

        Now:
            nums = [2, 2, 2, 3]

    --------------------------------------------------

    Final Check:
        return write → 2

        This means:
            k = 2 kept elements.
            nums[:2] = [2, 2] is the valid answer.
            nums[2] and nums[3] are leftovers the judge ignores.



---
🧠 First Time? Thoughts → Code

Read the problem (10 sec)
    • Remove every `val` from `nums` in-place, return how many remain (k).

    • The first k slots must hold the kept values; everything after k can be garbage.

    • "In-place" + "order may change" = don't build a new list; overwrite the front of nums.

Start naive (totally fine)
    • Loop and delete: when you see `val`, remove it (`.pop(i)` or shift left).

    • Or build a new list of non-val items and copy back.

    • Shifting / popping each hit → O(N²) worst case.

The one insight that unlocks the optimal code
    • You don't need to delete — pack the keepers at the front as you scan.

    • `read` looks at each element; `write` is the next slot for something worth keeping.

    • If it's not `val`, copy to `nums[write]` and bump `write`. If it is `val`, skip.

    • `write` at the end is both k and the count of kept elements.

Why write/read pointers? (only if needed)
    • One array, one pass — no shifting, no extra memory.

    • "Read" = inspect; "write" = where the filtered prefix grows.

    • Same pattern as Remove Duplicates, Move Zeroes — worth learning once.

Thought → line of code
    • `write = 0`
        → Start with an empty "kept" prefix at index 0.

    • `for read in range(len(nums))`
        → Must check every element; read is the scanner.

    • `if nums[read] != val`
        → Only keepers enter the prefix; val is ignored.

    • `nums[write] = nums[read]`
        → Copy keeper into the front (safe even when read > write).

    • `write += 1`
        → Prefix grew by one; next keeper goes one slot right.

    • `return write`
        → That's k; judge only sorts/checks nums[0:k].

Memory hook (one sentence)
    • Scan with read, pack non-val into the front with write, return write.

Would you arrive at this cold?
    • Immediately: loop, skip or collect non-val values, return a count.

    • After reading carefully: "in-place" nudges you away from a new list.

    • The `write` pointer name is pattern vocabulary — the real insight is pack-at-front, not delete.

    • `nums[write] = nums[read]` when read > write feels odd until you see you're only copying forward into empty prefix slots.


"""






# Brute force with .pop()

def removeElement(nums: list[int], val: int) -> int:
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)   # remove val; everything after i shifts left
            # don't increment i — the next element is now at i
        else:
            i += 1

    return len(nums)

nums = [3, 2, 2, 3]
val = 3
print(removeElement(nums, val))
# Output: 2 | nums = [2,2,_,_]

# nums = [2, 2]

"""
Time: O(N²)
  - Single pointer i scans the list at most n times → O(N).
  - Each nums.pop(i) when i is not the last index shifts all elements after i → O(N) per pop.
  - Worst case (many vals to remove): n pops × O(N) shift each → O(N²).

Space: O(1)
  - Only index i; modifies nums in place, no extra data structures.
"""




# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Same pattern as Move Zeroes (02-22) — slow/fast = write/read


def removeElement(nums: list[int], val: int) -> int:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1

    return slow


"""
read / write  vs  slow / fast  — same idea, different names

    • fast  = read   → scans the whole array (looks at each element)
    • slow  = write  → next spot to place a "keeper" at the front

    • fast finds what to look at; slow finds where to put what you keep


Same pattern as Move Zeroes (283):
    Move Zeroes                          Remove Element
    ─────────────────                    ─────────────────
    fast scans nums                      fast scans nums
    slow = where next keeper goes        slow = where next keeper goes
    keep if nums[fast] != 0              keep if nums[fast] != val
    nums[slow] = nums[fast]              nums[slow] = nums[fast]
    slow += 1                            slow += 1

    • Move Zeroes: Phase 2 fills the tail with 0s (problem requires full array correct).
    • Remove Element: no Phase 2 — judge only checks nums[:slow]; tail can be junk.

    • Both: one pass, pack keepers at the front, O(N) time, O(1) space.

Memory hook:
    If you know Move Zeroes slow/fast, you already know Remove Element — just swap "!= 0" for "!= val".
"""



