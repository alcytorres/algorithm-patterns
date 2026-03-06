# 560. Subarray Sum Equals K
"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
    Input: nums = [1, 2, 3], k = 3
    Output: 2 (subarrays [1, 2] and [3])

Example 2:
    Input: nums = [1, 2, 1, 2, 1], k = 3
    Output: 4 (subarrays [1, 2], [2, 1], [1, 2], [2, 1])

Solution: https://leetcode.com/problems/subarray-sum-equals-k/solutions/127728/subarray-sum-equals-k/
"""

# ––––––––––––––––––––––––––––––––––––––––––––––––
from collections import defaultdict

def subarraySum(nums, k):
    counts = defaultdict(int)
    counts[0] = 1
    # Track running sum and count subarrays
    ans = curr = 0

    # Process array to find subarrays with sum k
    for num in nums:
        curr += num
        ans += counts[curr - k]
        counts[curr] += 1

    return ans

nums = [1, 2, 1, 2, 1]
k = 3
print(subarraySum(nums, k))
# Output: 4 (subarrays [1, 2], [2, 1], [1, 2], [2, 1])

# Count: {0: 1, -2: 0, 1: 1, 3: 1, 4: 1, 6: 1, 7: 1})

# Key: running prefix sum (sum of elements up to current index)
# Value: how many prefixes have had that exact sum so far

# ––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
from collections import defaultdict

def subarraySum(nums, k):
    counts = defaultdict(int) # Track frequency of prefix sums
    counts[0] = 1             # Initialize for subarrays starting at index 0
    ans = curr = 0            # ans: counts subarrays, curr: running sum

    for num in nums:           # Iterate over each number
        curr += num            # Add current number to running sum
        ans += counts[curr - k]  # Count subarrays where sum = k
        counts[curr] += 1      # Increment frequency of current sum
        
    return ans                # Return total subarrays with sum k


"""
Time: O(N)
  - Let N = length of nums.
  - Step 1: Iterate through nums once → O(N).
      • Maintain running prefix sum 'curr' in O(1).
      • For each num, lookup (curr - k) in dictionary → O(1) average.
      • Update dictionary with current prefix sum → O(1).
  - Each element is processed exactly once.
  - Overall: O(N).

Space: O(N)
  - Dictionary 'counts' stores frequency of prefix sums.
  - In the worst case (all prefix sums unique), it holds up to N entries.
  - A few scalar variables (curr, ans, num) use O(1).
  - Overall: O(N).

  
Interview Answer: Worst Case

Time: O(N)
  - Single pass using prefix sums and hashmap lookups.

Space: O(N)
  - Hashmap stores prefix sums up to N entries.

  
Q: What is the key and value of counts?

  • Key: running prefix sum (sum of elements up to current index).

  • Value: how many prefixes have had that exact sum so far.

  • Why counts[0] = 1: seeds the empty prefix (sum 0) so subarrays starting at index 0 are counted.


---
Overview for Each Iteration
Input: nums = [1, 2, 1, 2, 1], k = 3

Step: Process array to find subarrays with sum k
i | num | curr | curr - k | counts[curr - k] | ans | counts
--|-----|------|----------|------------------|-----|------------------------------
- | -   | 0    | -        | -                | 0   | {0:1}
0 | 1   | 1    | 1-3=-2   | 0                | 0   | {0:1, 1:1}
1 | 2   | 3    | 3-3=0    | 1                | 1   | {0:1, 1:1, 3:1}
2 | 1   | 4    | 4-3=1    | 1                | 2   | {0:1, 1:1, 3:1, 4:1}
3 | 2   | 6    | 6-3=3    | 1                | 3   | {0:1, 1:1, 3:1, 4:1, 6:1}
4 | 1   | 7    | 7-3=4    | 1                | 4   | {0:1, 1:1, 3:1, 4:1, 6:1, 7:1}

Final: 4 (subarrays [1, 2], [2, 1], [1, 2], [2, 1])


Subarrays found:
    • i=1: curr=3, curr-k=0, counts[0]=1 -> [1, 2] (sum=3)
    • i=2: curr=4, curr-k=1, counts[1]=1 -> [2, 1] (sum=3)
    • i=3: curr=6, curr-k=3, counts[3]=1 -> [1, 2] (sum=3)
    • i=4: curr=7, curr-k=4, counts[4]=1 -> [2, 1] (sum=3)


---
Most IMPORTANT thing to Understand:
    • curr is the running sum up to the current index.

    • If a previous running sum equals (curr - k), then the numbers after that point up to now sum to k. 

    • counts stores how many times each running sum has appeared.
    
    • counts[0] = 1 handles subarrays that start at index 0.

---
Why this code Works:
    • Hash map (counts): key = running sum value, value = how many times we've seen it so far.

    • Prefix sum idea: a subarray sums to k when curr - prev = k  →  prev = curr - k.

    • counts[curr - k] tells us how many subarrays ending at the current index add up to k, so we add that to ans.

    • counts[curr] += 1 records the current running sum so future elements can check against it.

    • One pass, O(n) time; O(1) average lookups; avoids O(n^2) brute-force checks.

---
TLDR:
    • Track running sums and, at each index, add how many earlier sums equal (curr - k) — that gives the number of subarrays ending here whose sum is exactly k.

---
Quick Example Walkthrough:
    nums = [1, 2, 1, 2, 1], k = 3

    Step 1 (setup): counts = {0:1}, curr = 0, ans = 0

    Step 2 (iterate):
        • +1 → curr=1 → curr-k=-2 → counts[-2]=0 → ans=0 → counts[1]=1

        • +2 → curr=3 → curr-k=0  → counts[0]=1  → ans=1 → counts[3]=1   # subarray [1, 2]

        • +1 → curr=4 → curr-k=1  → counts[1]=1  → ans=2 → counts[4]=1   # subarray [2, 1]

        • +2 → curr=6 → curr-k=3  → counts[3]=1  → ans=3 → counts[6]=1   # subarray [1, 2]

        • +1 → curr=7 → curr-k=4  → counts[4]=1  → ans=4 → counts[7]=1   # subarray [2, 1]

    Final Answer: 4


    


---
How the dictionary works in subarraySum:

  • `curr` is the running prefix sum.
  • We access the map using `curr` and `curr - k` → keys must be prefix sums.
  • We do `count[curr] += 1` → values count how many times each sum appears.

So:
  • Key   = prefix sum so far
  • Value = number of times that sum has occurred

Why it works:
  • If `curr - k` was seen before, the numbers between form a subarray with sum = k.
  • Each occurrence adds one valid subarray.

 
---
Q: Why Does CURR - K work?  ****** VERY IMPORTANT TO UNDESTAND ****** 
----------------------------------------------

Core idea (prefix-sum logic):
  - Let `curr` be the running sum up to the current index.
  - If there exists a previous running sum equal to `curr - k`, then the subarray after that previous point up to now sums to k.

Reason:
    previous_sum = curr - k  ⟺  k = curr - previous_sum 

    The difference between two prefix sums is the sum of the elements between them.


Ultra-simple numeric example:
------------------------------------------------
nums = [2, 1, 3], k = 3

Running sums as we scan (include the initial 0 because of counts[0] = 1):
    prefix_sums = [0,   2,  3,  6]
                   ^    ^   ^   ^
                   |    |   |   |
    Indices:      (-1)  0   1   2   (conceptual -1 before the array starts)

Check differences to find subarrays summing to k:
- At curr = 3 (after seeing [2, 1]):
    curr - k = 3 - 3 = 0
    Have we seen a prefix sum of 0 before? Yes (the seeded one).
    → Subarray (after that 0) is [2, 1], and its sum is 3. ✅

- At curr = 6 (after seeing [2, 1, 3]):
    curr - k = 6 - 3 = 3
    Have we seen a prefix sum of 3 before? Yes (after [2, 1]).
    → Subarray (after that 3) is [3], and its sum is 3. ✅

Mental picture with just numbers:
    prefix_sums: [0, 2, 3, 6]
    differences: (3 - 0) = 3  → subarray [2, 1]
                 (6 - 3) = 3  → subarray [3]

Takeaway:
  • Every time you can find an earlier prefix sum exactly k smaller than the current prefix sum, the chunk between them totals k.


"""
  



"""

------------------------------------------------
Q: Why do we set counts[0] = 1 at the start?

counts[0] = 1

  • We conceptually include a "prefix sum before the array starts" with value 0.

  • This seeds the count so that if `curr == k` at some index i,
  the subarray from 0..i is correctly counted (because curr - k = 0 is “already seen” once).

  In other words, we start with a single occurrence of prefix sum 0 to allow subarrays starting at index 0.

  • Seeding `counts[0] = 1` makes sure subarrays starting at the very beginning are counted.


Why do we need this?
    • It's a starting point that says:
      “Before we add any numbers, we already have one way to make a sum of 0.”
    • This makes it possible to count subarrays that start at the very beginning of the array.

---
Example 1: nums = [1, 2], k = 3
    • Running sum (curr) starts at 0.
    • First number → curr = 1
    • Second number → curr = 3

Now check: curr - k = 3 - 3 = 0
    • If counts[0] wasn't initialized to 1, the code would miss the subarray [1, 2] because it wouldn't recognize that the sum from the start equals k.

---
Example 2: nums = [3, 2, 1], k = 3
    • Running sum (curr) starts at 0.

    Step 1:
        • Add 3 → curr = 3
        • Check curr - k = 3 - 3 = 0
        • counts[0] = 1 → valid subarray [3]

    Step 2:
        • Add 2 → curr = 5
        • Check curr - k = 5 - 3 = 2
        • counts[2] = 0 → no match

    Step 3:
        • Add 1 → curr = 6
        • Check curr - k = 6 - 3 = 3
        • counts[3] = 1 (from Step 1) → valid subarray [2, 1]

    ✅ Total valid subarrays = 2 → [3], [2, 1]

---
✅ So counts[0] = 1 is like saying:
    • “We've seen a zero-sum once already, before starting. That way, if the running total hits k, we know we found a valid subarray starting at index 0.”



------------------------------------------------
Q: Can ans increase by more than 1 in a single iteration?

    • Yes, if multiple previous prefix sums match `curr - k`.
    • At each step we do: ans += counts[curr - k].
    • If counts[curr - k] = m, then there are m valid subarrays ending at this index.
    • This means ans can jump by m at once (e.g., go from 1 → 3).

Example:
    • nums = [1, -1, 1, -1], k = 0
    • Prefix sums: [1, 0, 1, 0]
    • At i=3 (curr = 0), counts[0] = 2
    • ans increases by 2 in this step → total ans goes from 2 → 4

Key insight:
    • With only positive numbers, prefix sums are strictly increasing, so ans increases by at most 1 each step.
    
    • With zeros or negatives, prefix sums can repeat → ans can increase by more than 1 in one iteration.

Key insight:
    • With only positive numbers, prefix sums are strictly increasing, so ans increases by at most 1 each step.

    • With zeros or negatives, prefix sums can repeat → ans can increase by more than 1 in one iteration.

    • When there are non-positive numbers, the same prefix can occur multiple times, so we need a hash map (dictionary) to keep track of frequencies instead of just storing seen values once.

"""



# ––––––––––––––––––––––––––––––––––––––––––––––––
# Best Solution:

from collections import defaultdict

def subarraySum(nums, k):
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0

    # Process array to find subarrays with sum k
    for num in nums:
        curr += num
        ans += counts[curr - k]
        counts[curr] += 1

    # print(counts)
    return ans

nums = [1, 2, 3]
k = 3
print(subarraySum(nums, k))
# Output: 2 (subarrays [1, 2] and [3])
# Counts = {0:1, -2:0, 1:1, 3:1, 6:1}


"""
Overview for Each Iteration with the auto-created keys from defaultdict included:
    • Happens when you *access* a missing key. 
Input: nums = [1, 2, 3], k = 3

Step: Process array to find subarrays with sum k
i | num | curr | curr - k | counts[curr - k] | ans | counts
--|-----|------|----------|------------------|-----|---------------------------
- | -   | 0    | -        | -                | 0   | {0:1}
0 | 1   | 1    | 1-3=-2   | 0                | 0   | {0:1, -2:0, 1:1}
1 | 2   | 3    | 3-3=0    | 1                | 1   | {0:1, -2:0, 1:1, 3:1}
2 | 3   | 6    | 6-3=3    | 1                | 2   | {0:1, -2:0, 1:1, 3:1, 6:1}

Final: 2 (subarrays [1,2], [3])


"""

# ––––––––––––––––––––––––––––––––––––––––––––––––
# Best Solution using .get() to remove auto-created keys:

from collections import defaultdict

def subarraySum(nums, k):
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0

    # Process array to find subarrays with sum k
    for num in nums:
        curr += num
        ans += counts.get(curr - k,0 )
        counts[curr] += 1

    # print(counts)
    return ans

nums = [1, 2, 3]
k = 3
print(subarraySum(nums, k))
# Output: 2 (subarrays [1, 2] and [3])
# Counts = {0:1, 1:1, 3:1, 6:1}


"""
Overview for Each Iteration
Input: nums = [1, 2, 3], k = 3

Step: Process array to find subarrays with sum k
i | num | curr | curr - k | counts[curr - k] | ans | counts
--|-----|------|----------|------------------|-----|----------------------
- | -   | 0    | -        | -                | 0   | {0:1}
0 | 1   | 1    | 1-3=-2   | 0                | 0   | {0:1, 1:1}
1 | 2   | 3    | 3-3=0    | 1                | 1   | {0:1, 1:1, 3:1}
2 | 3   | 6    | 6-3=3    | 1                | 2   | {0:1, 1:1, 3:1, 6:1}

Final: 2 (subarrays [1,2], [3])



---
Q: Why are there "extra" keys (e.g., -2:0) if you print counts w/out using .get()?

Why it happens:
    • defaultdict(int) auto-creates keys with value 0 when you *access* a missing key.
    • Example: counts[curr - k] → if (curr - k) not in counts, it gets inserted as 0.

What you'll see:
    • Tools like Python Tutor may show entries like {-2: 0}.
    • A manual iteration table might skip these since they don't affect the result.

Does it matter?
    • No — these extra 0-entries do NOT affect correctness.
    • They are harmless placeholders.

How to avoid it:
    • Use counts.get(curr - k, 0) when you just want to *check* a value.
    • .get() returns 0 without creating a new key.

Key takeaway:
    • defaultdict[int] = convenient for counting, but remember it auto-inserts on access.
    • Extra keys with value 0 are normal and safe to ignore.


counts from table: =             {0:1, 1:1, 3:1, 6:1}
counts from python visualizer: = {0:1, -2:0, 1:1, 3:1, 6:1})



  



-------------------OLD BREAKDOWN-------------------

Most IMPORTANT thing to Understand:    
    • TLDR: If counts[curr - k] exists → curr - prev = k, so that subarray sums to k. 

    • counts[curr - k] tells how many such subarrays end at the current index.

    
Explanation for Beginners: Why this code works
    • If some earlier running total was exactly (curr - k), then the numbers AFTER that point up to i sum to k.
        • “After that point” is what people mean by “prev_index + 1” — start right after where that earlier total was measured.

    • counts is a hash map where counts[prefix] = how many times we've seen that running total before.

    • Finally, we record today's total for future checks: counts[curr] += 1.


Example (quick sanity check):
    • nums = [1, 2], k = 3
    • prefix totals: 1, 3
    • at curr = 3 ⇒ curr - k = 0 ⇒ counts[0] = 1 ⇒ one subarray [1, 2].

    
Note: The code determines only the total number of subarrays with a sum equal to k, confirming their existence through prefix sum matches without specifying which subarrays they are.

"""


# ––––––––––––––––––––––––––––––––––––––––––––––––
# Note the image that explains this problem in this section: Count the number of subarrays with an "exact" constraint only applies when the subarray sum matches k.

# If the subarray sum does not match k, no count is incremented, and the logic moves to the next prefix sum check.

# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4512/



# ––––––––––––––––––––––––––––––––––––––––––––––––
# Brute Force 

def subarraySum(nums, k):
    ans = 0
    # Check every possible subarray
    for i in range(len(nums)):
        curr = 0
        # Compute sum of subarray from i to j
        for j in range(i, len(nums)):
            curr += nums[j]
            # If sum equals k, increment count
            if curr == k:
                ans += 1
    return ans

nums = [1, 2, 1, 2, 1]
k = 3
print(subarraySum(nums, k)) 
# Output: 4 (subarrays [1, 2], [2, 1], [1, 2], [2, 1])

"""
Time: O(n^2)
  - Outer loop runs n times.
  - Inner loop runs up to n times for each outer loop, computing subarray sums.
  - Overall: O(n^2) time.

Space: O(1)
  - Only a constant number of variables (ans, curr, i, j) are used.
  - No additional data structures.
  - Overall: O(1) space.


Overview for Each Iteration
Input: nums = [1, 2, 1, 2, 1], k = 3

Step: Find subarrays with sum equal to k
i  | j  | curr          | curr == k | ans | Subarray
---|----|---------------|-----------|-----|----------------
0  | 0  | 1             | False     | 0   | [1]
0  | 1  | 3 (1+2)       | True      | 1   | [1, 2]
0  | 2  | 4 (3+1)       | False     | 1   | [1, 2, 1]
0  | 3  | 6 (4+2)       | False     | 1   | [1, 2, 1, 2]
0  | 4  | 7 (6+1)       | False     | 1   | [1, 2, 1, 2, 1]
1  | 1  | 2             | False     | 1   | [2]
1  | 2  | 3 (2+1)       | True      | 2   | [2, 1]
1  | 3  | 5 (3+2)       | False     | 2   | [2, 1, 2]
1  | 4  | 6 (5+1)       | False     | 2   | [2, 1, 2, 1]
2  | 2  | 1             | False     | 2   | [1]
2  | 3  | 3 (1+2)       | True      | 3   | [1, 2]
2  | 4  | 4 (3+1)       | False     | 3   | [1, 2, 1]
3  | 3  | 2             | False     | 3   | [2]
3  | 4  | 3 (2+1)       | True      | 4   | [2, 1]
4  | 4  | 1             | False     | 4   | [1]

Final: 4 ([1, 2], [2, 1], [1, 2], [2, 1])

"""




# Example where we increase by more than 1 in a single iteration
from collections import defaultdict

def subarraySum(nums, k):
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0

    for num in nums:
        curr += num
        ans += counts[curr - k]
        counts[curr] += 1
    return ans

nums = [1, -1, 1, -1]
k = 0
print(subarraySum(nums, k))
# Output: 4 (subarrays [1, -1], [-1, 1], [1, -1], [1, -1, 1, -1])

"""
Overview for Each Iteration
Input: nums = [1, -1, 1, -1], k = 0

Step: Process array to find subarrays with sum k
i | num | curr | curr - k | counts[curr - k] | ans | counts
--|-----|------|----------|------------------|-----|-----------
- | -   | 0    | -        | -                | 0   | {0:1}
0 | 1   | 1    | 1-0=1    | 0                | 0   | {0:1, 1:1}
1 | -1  | 0    | 0-0=0    | 1                | 1   | {0:2, 1:1}
2 | 1   | 1    | 1-0=1    | 1                | 2   | {0:2, 1:2}
3 | -1  | 0    | 0-0=0    | 2                | 4   | {0:3, 1:2}

Final: 4 (subarrays [1,-1], [1,-1,1,-1], [-1,1], [1,-1])

👉 Notice at i=3, counts[0] = 2, so ans jumps from 2 → 4 in a single step

"""

# ––––––––––––––––––––––––––––––––––––––––––––––––
# Best Solution:

from collections import defaultdict

def subarraySum(nums, k):
    counts = defaultdict(int)
    counts[0] = 1
    # Track running sum and count subarrays
    ans = curr = 0

    # Process array to find subarrays with sum k
    for num in nums:
        curr += num
        ans += counts[curr - k]
        counts[curr] += 1

    return ans

nums = [1, -1, 1]
k = 1
print(subarraySum(nums, k))
# Output: 3 (subarrays [1], [1, -1, 1], [1])

"""
Overview for Each Iteration
Input: nums = [1, -1, 1], k = 1

Step: Process array to find subarrays with sum k
i | num | curr | curr - k | counts[curr - k] | ans | counts
--|-----|------|----------|------------------|-----|-----------
- | -   | 0    | -        | -                | 0   | {0:1}
0 | 1   | 1    | 1-1=0    | 1                | 1   | {0:1, 1:1}
1 | -1  | 0    | 0-1=-1   | 0                | 1   | {0:2, 1:1}
2 | 1   | 1    | 1-1=0    | 2                | 3   | {0:2, 1:2}

Final: 3 (subarrays [1], [1, -1, 1], [1])

"""


# ––––––––––––––––––––––––––––––––––––––––––––––––
# Best Solution:

from collections import defaultdict

def subarraySum(nums, k):
    counts = defaultdict(int)
    counts[0] = 1
    # Track running sum and count subarrays
    ans = curr = 0

    # Process array to find subarrays with sum k
    for num in nums:
        curr += num
        ans += counts[curr - k]
        counts[curr] += 1

    return ans

nums = [1, 2, 3, 4, 6]
k = 6
print(subarraySum(nums, k))
# Output: 2 (subarrays [1, 2, 3] and [6])

"""
Overview for Each Iteration
Input: nums = [1, 2, 3, 4, 6], k = 6

Step: Process array to find subarrays with sum k
i | num | curr | curr - k | counts[curr - k] | ans | counts
--|-----|------|----------|------------------|-----|---------------------------------
- | -   | 0    | -        | -                | 0   | {0:1}
0 | 1   | 1    | -5       | 0                | 0   | {0:1, 1:1}
1 | 2   | 3    | -3       | 0                | 0   | {0:1, 1:1, 3:1}
2 | 3   | 6    | 0        | 1                | 1   | {0:1, 1:1, 3:1, 6:1}
3 | 4   | 10   | 4        | 0                | 1   | {0:1, 1:1, 3:1, 6:1, 10:1}
4 | 6   | 16   | 10       | 1                | 2   | {0:1, 1:1, 3:1, 6:1, 10:1, 16:1}

Final: 2 (subarrays [1,2,3] and [6])

"""



# ––––––––––––––––––––––––––––––––––––––––––––––––
# Best Solution:

from collections import defaultdict

def subarraySum(nums, k):
    counts = defaultdict(int)
    counts[0] = 1
    # Track running sum and count subarrays
    ans = curr = 0

    # Process array to find subarrays with sum k
    for num in nums:
        curr += num
        ans += counts[curr - k]
        counts[curr] += 1

    return ans

nums = [1, 2, 3, 10, -4, 6]
k = 6
print(subarraySum(nums, k))
# Output: 3 (subarrays [1, 2, 3], [-10, -4],[6])

"""
Overview for Each Iteration
Input: nums = [1, 2, 3, 10, -4, 6], k = 6

Step: Process array to find subarrays with sum k
i | num | curr | curr - k | counts[curr - k] | ans | counts
--|-----|------|----------|------------------|-----|---------------------------------------
- | -   | 0    | -        | -                | 0   | {0:1}
0 | 1   | 1    | -5       | 0                | 0   | {0:1, 1:1}
1 | 2   | 3    | -3       | 0                | 0   | {0:1, 1:1, 3:1}
2 | 3   | 6    | 0        | 1                | 1   | {0:1, 1:1, 3:1, 6:1}
3 | 10  | 16   | 10       | 0                | 1   | {0:1, 1:1, 3:1, 6:1, 16:1}
4 | -4  | 12   | 6        | 1                | 2   | {0:1, 1:1, 3:1, 6:1, 16:1, 12:1}
5 | 6   | 18   | 12       | 1                | 3   | {0:1, 1:1, 3:1, 6:1, 16:1, 12:1, 18:1}

Final: 3 (subarrays [1,2,3], [10,-4], [-4,6])

"""


# ––––––––––––––––––––––––––––––––––––––––––––––––
# Best Solution:

from collections import defaultdict

def subarraySum(nums, k):
    counts = defaultdict(int)
    counts[0] = 1
    # Track running sum and count subarrays
    ans = curr = 0

    # Process array to find subarrays with sum k
    for num in nums:
        curr += num
        ans += counts[curr - k]
        counts[curr] += 1

    return ans

nums = [0, 1, 2, 3, 4]
k = 5
print(subarraySum(nums, k))
# Output: 1 (subarray [2, 3])

"""
Overview for Each Iteration
Input: nums = [0, 1, 2, 3, 4], k = 5

Step: Process array to find subarrays with sum k
i | num | curr | curr - k | counts[curr - k] | ans | counts
--|-----|------|----------|------------------|-----|----------------------------
- | -   | 0    | -        | -                | 0   | {0:1}
0 | 0   | 0    | -5       | 0                | 0   | {0:2}
1 | 1   | 1    | -4       | 0                | 0   | {0:2, 1:1}
2 | 2   | 3    | -2       | 0                | 0   | {0:2, 1:1, 3:1}
3 | 3   | 6    | 1        | 1                | 1   | {0:2, 1:1, 3:1, 6:1}
4 | 4   | 10   | 5        | 0                | 1   | {0:2, 1:1, 3:1, 6:1, 10:1}

Final: 1 (subarray [2, 3])

"""



# ––––––––––––––––––––––––––––––––––––––––––––––––
# Best Solution:

from collections import defaultdict

def subarraySum(nums, k):
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0

    for num in nums:
        curr += num
        ans += counts[curr - k]
        counts[curr] += 1
    return ans

nums = [3, 4, 7, 2, -3, 1, 4, 2]
print(subarraySum(nums, 7))
# Output: 4 (subarrays [3, 4], [7], [7, 2, -3, 1], [1, 4, 2])

"""
Overview for Each Iteration
Input: nums = [3, 4, 7, 2, -3, 1, 4, 2], k = 7

Step: Process array to find subarrays with sum k
i | num | curr | curr - k | counts[curr - k] | ans | counts
--|-----|------|----------|------------------|-----|-----------------------------------------------
- | -   | 0    | -        | -                | 0   | {0:1}
0 | 3   | 3    | -4       | 0                | 0   | {0:1, 3:1}
1 | 4   | 7    | 0        | 1                | 1   | {0:1, 3:1, 7:1}
2 | 7   | 14   | 7        | 1                | 2   | {0:1, 3:1, 7:1, 14:1}
3 | 2   | 16   | 9        | 0                | 2   | {0:1, 3:1, 7:1, 14:1, 16:1}
4 | -3  | 13   | 6        | 0                | 2   | {0:1, 3:1, 7:1, 14:1, 16:1, 13:1}
5 | 1   | 14   | 7        | 1                | 3   | {0:1, 3:1, 7:1, 14:2, 16:1, 13:1}
6 | 4   | 18   | 11       | 0                | 3   | {0:1, 3:1, 7:1, 14:2, 16:1, 13:1, 18:1}
7 | 2   | 20   | 13       | 1                | 4   | {0:1, 3:1, 7:1, 14:2, 16:1, 13:1, 18:1, 20:1}

Final: 4 (subarrays [3,4], [7], [7,2,-3,1], [1,4,2])

"""



# ––––––––––––––––––––––––––––––––––––––––––––––––
# Best Solution:

from collections import defaultdict

def subarraySum(nums, k):
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0

    for num in nums:
        curr += num
        ans += counts[curr - k]
        counts[curr] += 1
    return ans

nums = [13, 1, 2, 3, 1]
k = 7
print(subarraySum(nums, k))
# Output: 1 (subarray [1, 2, 3, 1])

"""
Overview for Each Iteration
Input: nums = [13, 1, 2, 3, 1], k = 7

Step: Process array to find subarrays with sum k
i | num | curr | curr - k | counts[curr - k] | ans | counts
--|-----|------|----------|------------------|-----|-------------------------------------
- | -   | 0    | -        | -                | 0   | {0:1}
0 | 13  | 13   | 6        | 0                | 0   | {0:1, 13:1}
1 | 1   | 14   | 7        | 0                | 0   | {0:1, 13:1, 14:1}
2 | 2   | 16   | 9        | 0                | 0   | {0:1, 13:1, 14:1, 16:1}
3 | 3   | 19   | 12       | 0                | 0   | {0:1, 13:1, 14:1, 16:1, 19:1}
4 | 1   | 20   | 13       | 1                | 1   | {0:1, 13:1, 14:1, 16:1, 19:1, 20:1}

Final: 1 (subarray [1, 2, 3, 1])

"""




# ––––––––––––––––––––––––––––––––––––––––––––––––
# Task: Find the number of subarrays with sum equal to k in an integer array.
# Example: nums = [1, 2, 1, 2, 1], k = 3 → Output = 4 (subarrays: [1, 2], [2, 1], [1, 2], [2, 1])
# Why: Practices prefix sum technique with a hash map to efficiently count subarrays.

from collections import defaultdict

def subarraySum(nums, k):  # Example: nums = [1, 2, 1, 2, 1], k = 3

    # 1️⃣ Initialize variables
    # Initialize a defaultdict to store prefix sum counts
    # Why? We track the frequency of prefix sums to find subarrays with sum k
    counts = defaultdict(int)  # counts = {}
    counts[0] = 1  # Initialize with 0 sum having 1 occurrence
    # Why? A prefix sum of 0 (empty subarray) allows subarrays starting from index 0

    # Initialize answer to count subarrays with sum k
    # Why? We need to accumulate the number of valid subarrays
    ans = 0  # ans = 0

    # Initialize current prefix sum
    # Why? We track the running sum to compute differences
    curr = 0  # curr = 0

    # 2️⃣ Process array to find subarrays
    # Iterate through each number to compute prefix sums
    # Why? We use prefix sums to find subarrays where sum[i:j] = k
    for num in nums:  # num takes values [1, 2, 1, 2, 1]
        # --- Iteration 1: num = 1 ---
        # Update the current prefix sum
        # Why? We accumulate the sum up to the current index
        curr += num  # curr = 0 + 1 = 1
        # Add the number of subarrays ending at the current index with sum k
        # Why? If curr - k exists in counts, it means there are subarrays summing to k
        ans += counts[curr - k]  # curr - k = 1 - 3 = -2, counts[-2] = 0 (not in counts), ans = 0
        # Increment the count of the current prefix sum
        # Why? We track how many times this prefix sum has occurred
        counts[curr] += 1  # counts[1] = 0 + 1 = 1
        # After Iteration 1: curr = 1, ans = 0, counts = {0: 1, 1: 1}

        # --- Iteration 2: num = 2 ---
        if num == 2:
            curr += num  # curr = 1 + 2 = 3
            ans += counts[curr - k]  # curr - k = 3 - 3 = 0, counts[0] = 1, ans = 0 + 1 = 1
            counts[curr] += 1  # counts[3] = 0 + 1 = 1
            # After Iteration 2: curr = 3, ans = 1, counts = {0: 1, 1: 1, 3: 1}
            # Found subarray: [1, 2] (sum = 3, indices 0 to 1)

        # --- Iteration 3: num = 1 ---
        if num == 1 and curr == 3:
            curr += num  # curr = 3 + 1 = 4
            ans += counts[curr - k]  # curr - k = 4 - 3 = 1, counts[1] = 1, ans = 1 + 1 = 2
            counts[curr] += 1  # counts[4] = 0 + 1 = 1
            # After Iteration 3: curr = 4, ans = 2, counts = {0: 1, 1: 1, 3: 1, 4: 1}
            # Found subarray: [2, 1] (sum = 3, indices 1 to 2)

        # --- Iteration 4: num = 2 ---
        if num == 2 and curr == 4:
            curr += num  # curr = 4 + 2 = 6
            ans += counts[curr - k]  # curr - k = 6 - 3 = 3, counts[3] = 1, ans = 2 + 1 = 3
            counts[curr] += 1  # counts[6] = 0 + 1 = 1
            # After Iteration 4: curr = 6, ans = 3, counts = {0: 1, 1: 1, 3: 1, 4: 1, 6: 1}
            # Found subarray: [1, 2] (sum = 3, indices 2 to 3)

        # --- Iteration 5: num = 1 ---
        if num == 1 and curr == 6:
            curr += num  # curr = 6 + 1 = 7
            ans += counts[curr - k]  # curr - k = 7 - 3 = 4, counts[4] = 1, ans = 3 + 1 = 4
            counts[curr] += 1  # counts[7] = 0 + 1 = 1
            # After Iteration 5: curr = 7, ans = 4, counts = {0: 1, 1: 1, 3: 1, 4: 1, 6: 1, 7: 1}
            # Found subarray: [2, 1] (sum = 3, indices 3 to 4)

    # 3️⃣ Return the count of valid subarrays
    # Why? ans contains the number of subarrays with sum equal to k
    return ans  # ans = 4


numbers = [1, 2, 1, 2, 1]
k = 3
print(subarraySum(numbers, k))  
# Output: 4 (subarrays [1, 2], [2, 1], [1, 2], [2, 1])

# counts = {0:1, 1:1, 3:1, 4:1, 6:1, 7:1}