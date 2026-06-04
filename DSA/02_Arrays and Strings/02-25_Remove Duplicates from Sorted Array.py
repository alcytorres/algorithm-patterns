# 26. Remove Duplicates from Sorted Array

"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.


Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 
Example 1:
    Input: nums = [1,1,2]
    Output: 2, nums = [1,2,_]
    Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:
    1 <= nums.length <= 3 * 104
    -100 <= nums[i] <= 100
    nums is sorted in non-decreasing order.

"""

# Solution: Build a new list, then copy back (conceptual bridge)

def removeDuplicates(nums):
    write = 1  # index 0 is always unique

    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1

    return write


nums = [1, 1, 2]
print(removeDuplicates(nums))
# Output: 2 → One pass keeps each new unique at the front; k=2 so nums[:2] = [1, 2] (tail ignored)

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(nums))
# Output: 5 → Sorted duplicates are adjacent; pack uniques to get nums[:5] = [0, 1, 2, 3, 4]


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown

def removeDuplicates(nums):
    write = 1                         # Next open spot after the first value (index 0 stays)

    for read in range(1, len(nums)):  # Walk from index 1 to the end
        if nums[read] != nums[write - 1]:  # New value — different from last one we kept
            nums[write] = nums[read]  # Copy it into the front we are building
            write += 1                # Move the open spot one step right

    return write                      # How many unique values (k); judge only checks nums[:k]


"""
Time: O(N)
  - Let N = length of nums.
  - One loop: read goes from 1 to N - 1 → at most N - 1 iterations.
  - Each iteration: compare nums[read] to nums[write - 1] → O(1); maybe one copy → O(1).
  - Overall: O(N).


Space: O(1)
  - Only write (and read as the loop index); no extra arrays or hash maps.
  - Work is done in place on nums.
  - Overall: O(1).


Interview Answer: Worst Case

Time: O(N)
  - Single pass with read through the array; each step is constant time.

Space: O(1)
  - Only the write pointer (plus the loop index); no extra structures.


---
Overview for Each Iteration
Input: nums = [1, 1, 2]

Write-pointer scan: keep each new unique value at the front; skip duplicates.

read|nums[read]|!= nums[write-1]?| write (before→after)|Action | nums prefix (valid part)
----|----------|-----------------|---------------------|-------|------------------------
1   | 1        | no (same as 1)  | 1                   | skip  | [1, ...]
2   | 2        | yes             | 1→2                 | copy→1| [1, 2]

Final: return write = 2; valid prefix nums[:2] = [1, 2] (index 2 ignored)


---
Most IMPORTANT thing to Understand:
    • You are not deleting duplicates — you are building the unique answer at the front.

    • Because the array is sorted, duplicates sit next to each other.

    • Index 0 is always kept. `write` starts at 1 — the next open spot for a new unique value.

    • Compare `nums[read]` to `nums[write - 1]` (the last value you kept). If different, it's new — copy it and move `write` forward.

    • When done, return `write` as k. Only `nums[0:k]` matters; the rest can be junk.


---
Why this code Works:
    • Write pointer (in-place compact):
        • `read` scans from index 1 to the end.
        • `write` collects each new unique value at the front of nums.

    • Skip rule:
        • If `nums[read] == nums[write - 1]`, it's a duplicate — skip it.
        • If different, place it at `nums[write]` and increment `write`.

    • Sorted array advantage:
        • Duplicates are always adjacent, so you only need to compare to the last kept value.
        • No hash set needed.

    • Efficiency:
        • One pass → O(N) time.
        • No extra array → O(1) space.
        • Beats building a new list or shifting elements.

    • Intuition:
        • Like stamping a passport: each new country gets one stamp; repeat visits don't get another.


---
TLDR:
    • Scan with `read`; whenever `nums[read]` differs from the last kept value, copy it to `nums[write]` and advance `write`.
    • Return `write` — that is k, and `nums[:k]` holds every unique value in order.


---
Quick Example Walkthrough:
    nums = [1, 1, 2]

    Step 1: Start with write = 1 (index 0 = 1 stays automatically)

    Step 2: Scan with read from 1 to 2
        • read=1, nums[1]=1 → same as nums[0] → skip
        • read=2, nums[2]=2 → new → nums[1]=2, write=2

    Step 3: Return write
        • k = 2, valid prefix = [1, 2]

    Final Answer: 2 (nums[:2] = [1, 2]; tail ignored)

---
Quick Example Walkthrough:
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

    Step 1: Start with write = 1 (index 0 = 0 stays automatically)

    Step 2: Scan with read from 1 to 9
        • read=1, nums[1]=0 → same as nums[0] → skip
        • read=2, nums[2]=1 → new → nums[1]=1, write=2
        • read=3, nums[3]=1 → same as nums[1] → skip
        • read=4, nums[4]=1 → same as nums[1] → skip
        • read=5, nums[5]=2 → new → nums[2]=2, write=3
        • read=6, nums[6]=2 → skip
        • read=7, nums[7]=3 → new → nums[3]=3, write=4
        • read=8, nums[8]=3 → skip
        • read=9, nums[9]=4 → new → nums[4]=4, write=5

    Step 3: Return write
        • k = 5, valid prefix = [0, 1, 2, 3, 4]

    Final Answer: 5 (nums[:5] = [0, 1, 2, 3, 4]; tail ignored)


---
Full Example Walkthrough:
    nums = [1, 1, 2]

    Starting State:
        write = 1
        read = 1 (loop will visit 1, 2)

        nums[0] = 1 is already in place (first unique always stays)
        nums = [1, 1, 2]

    Loop Iteration 1 (read = 1):
        Check:
            nums[read] != nums[write - 1]
            nums[1] != nums[0] → 1 != 1 → FALSE

        Action:
            Skip — duplicate of the last kept value

        Now:
            write = 1
            nums = [1, 1, 2]

    --------------------------------------------------

    Loop Iteration 2 (read = 2):
        Check:
            nums[2] != nums[0] → 2 != 1 → TRUE

        Action:
            nums[write] = nums[read] → nums[1] = 2
            write += 1 → write = 2

        Now:
            nums = [1, 2, 2]

    --------------------------------------------------

    Final Check:
        return write → 2

        This means:
            k = 2 unique elements.
            nums[:2] = [1, 2] is the valid answer.
            nums[2] is a leftover the judge ignores.



---
🧠 First Time? Thoughts → Code

Read the problem (10 sec)
    • Remove duplicates in-place, return k = count of unique values.

    • First k slots must hold the unique values in order; the rest can be junk.

    • **Sorted** is the big hint — duplicates are always next to each other.

Start naive (totally fine)
    • Use a set to track seen values, build a new list of uniques, copy back.

    • Or loop and `.pop()` / shift left whenever you see a duplicate of the previous value.

    • Set approach → O(N) time but O(N) extra space. Shifting → O(N²) worst case.

The one insight that unlocks the optimal code
    • You don't need to delete — pack each new unique value at the front as you scan.

    • Because the array is sorted, you only compare to the **last value you kept**, not every value you've ever seen.

    • `read` scans forward; `write` is the next slot for a new unique.

    • If `nums[read]` matches the last kept value, skip. If different, copy and bump `write`.

Why write/read pointers? (only if needed)
    • One array, one pass — no set, no shifting, no extra memory.

    • Same pattern as Remove Element and Move Zeroes — only the "keep" condition changes.

    • Sorted input is what lets you compare to `nums[write - 1]` instead of using a hash set.

Thought → line of code
    • `write = 1`
        → Index 0 is always the first unique; start placing new ones at slot 1.

    • `for read in range(1, len(nums))`
        → Skip index 0 (already kept); scan the rest with read.

    • `if nums[read] != nums[write - 1]`
        → Compare to last kept value, not `nums[read - 1]` — write may lag behind read after copies.

    • `nums[write] = nums[read]`
        → New unique goes into the growing prefix at the front.

    • `write += 1`
        → Prefix grew; next new unique goes one slot right.

    • `return write`
        → That's k; judge only checks nums[0:k].

Memory hook (one sentence)
    • Scan with read, copy each new unique to the front with write, return write.

Would you arrive at this cold?
    • Immediately: loop, skip duplicates, return a count — maybe with a set.

    • After reading carefully: "sorted" means adjacent duplicates → no set needed.

    • The `write = 1` start (not 0) is easy to miss — first element is free.

    • `nums[write - 1]` instead of `nums[read - 1]` is the subtle part — write tracks what you've kept, read tracks what you're looking at.

"""




# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force — build a unique list, then copy back

def removeDuplicates(nums):
    unique = []

    for num in nums:
        if not unique or num != unique[-1]:
            unique.append(num)

    for i in range(len(unique)):
        nums[i] = unique[i]

    return len(unique)


nums = [1, 1, 2]
print(removeDuplicates(nums))
# Output: 2 → Build a unique list, copy back to nums; O(N) time but O(N) extra space

"""
Time: O(N)
  - Let N = length of nums.

  - Step 1: Loop through nums, append each new unique to `unique` → O(N).
      • Each step: compare to unique[-1] → O(1); maybe one append → O(1).

  - Step 2: Copy unique back into nums → O(N).
      • At most N elements in unique.

  - Combined: O(N + N).
  - Overall: O(N).


Space: O(N)
  - `unique` stores up to N distinct values.
  - Only a loop index i beyond that.
  - Overall: O(N).


Interview Answer: Worst Case

Time: O(N)
  - One pass to build the unique list, one pass to copy back.

Space: O(N)
  - Extra list holds all unique values.


---
Overview for Each Iteration
nums = [1, 1, 2]

    unique starts = []

    read 1 → unique is empty → append 1 → unique = [1]
    read 1 → same as unique[-1] → skip
    read 2 → different from unique[-1] → append 2 → unique = [1, 2]

    copy back:
        nums[0] = 1
        nums[1] = 2

    return len(unique) = 2

Final: 2 (nums[:2] = [1, 2])

"""





# Solution: k as “last unique index” (compact two-pointer variant)

def removeDuplicates(nums):
    k = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[k]:
            k += 1
            nums[k] = nums[i]
    return k + 1


nums = [1, 1, 2]
print(removeDuplicates(nums))
# Output: 2 → Same read/write idea: k = last unique index; return k+1 for count

"""
---
Overview for Each Iteration
Input: nums = [1, 1, 2]

k marks the last index where a unique value lives; index 0 stays automatically.

i | nums[i] | != nums[k]? | k (before→after) | Action  | nums prefix
--|---------|-------------|------------------|---------|------------
1 | 1       | no          | 0                | skip    | [1, ...]
2 | 2       | yes         | 0→1              | copy→1  | [1, 2]

Final: return k + 1 = 2; valid prefix nums[:2] = [1, 2] (index 2 ignored)

"""