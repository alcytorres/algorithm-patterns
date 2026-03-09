# 169. Given an array nums of size n, return the majority element.
"""
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
    Input: nums = [1, 3, 3]
    Output: 3

Example 2:
    Input: nums = [3, 1, 1, 3, 3, 3]
    Output: 3
 
Constraints:
    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109
    The input is generated such that a majority element will exist in the array.
 
Follow-up: Could you solve the problem in linear time and in O(1) space?

Solution: https://leetcode.com/problems/majority-element/description/
"""

# Optpion 1: Dictionary Frequency + max() Lookup
def majorityElement(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    return max(count, key=count.get)

nums = [1, 3, 3]
print(majorityElement(nums))  # Output: 3

# count = {1: 1, 3: 2}

# When you PASS a dictionary to `for`, `max`, `min`, etc., Python AUTOMATICALLY ITERATES OVER the KEYS.


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def majorityElement(nums):
    count = {}    # Dictionary to store frequency of each number
    
    for num in nums:     # Go through every number in the array
        if num in count:     # If we've seen this number before
            count[num] += 1  # Increment its count
        else:                # If it's the first time seeing it
            count[num] = 1   # Start counting it with 1
    
    return max(count, key=count.get)  # Return the number with highest count


"""
Time: O(N)
  - Let N = length of nums.
  - Single pass to count frequencies → O(N).
      • Each insertion/update in the hash map is O(1) average.
  - Finding the max-frequency key is O(U), where U ≤ N.
  - Overall: O(N).

Space: O(N)
  - Hash map 'count' stores frequency of each unique number.
  - In worst case (all numbers different), stores N keys.
  - Overall: O(N).

  
Interview Answer: Worst Case

Time: O(N)
  - Count each element once, then take the max.

Space: O(N)
  - Hash map stores counts for all unique numbers.


---
Most IMPORTANT thing to Understand:
    • There is one number that appears more than half the time (> n/2).
    • That means it appears more times than all other numbers combined.
    • We count how often each number appears → the one with highest count is the majority.

---
Why this code Works:
    • Dictionary 'count' tracks frequency of each number.
    • One pass through array to build frequencies.
    • max(count, key=count.get) returns the key (number) with highest value (count).
    • Since majority > n/2, no other number can tie or beat its count.

---
TLDR
    We count frequency of every number → return the one with the highest frequency 
    (it must be the majority since it appears > n/2 times).

---
Quick Example Walkthrough
    nums = [1, 3, 3]

    Step 1: Build frequency count
        • See 1 → count = {1: 1}
        • See 3 → count = {1: 1, 3: 1}
        • See 3 → count = {1: 1, 3: 2}

    Step 2: Find number with highest count
        • Keys: 1 and 3
        • count[1] = 1
        • count[3] = 2 ← highest

    Final Answer: 3




---
Q: Why do we set count[num] = 1 instead of 0?

A: Because the else branch runs when we see a number for the first time — and that's already 1 occurrence!

  • Seeing a number for the first time means it appeared once → the count should be 1.

  • Setting it to 0 would mean "I've seen this number zero times," which is wrong.

  • It still gives the correct answer because the relative order stays the same, but the counts themselves are inaccurate.

  • Use 1 to keep the counts truthful.


---
Q: What's the difference between: 
`max(counts.keys(), key=counts.get)` 
and 
`max(counts, key=counts.get)` ?

A: There is NO difference — they do the exact SAME thing.

  • `max(counts.keys(), key=counts.get)` — explicitly says "loop over the keys."

  • `max(counts, key=counts.get)` — loops over the KEYS by DEFAULT.

  • When you PASS a dictionary to `for`, `max`, `min`, etc., Python AUTOMATICALLY ITERATES OVER the KEYS.

  • So `.keys()` is just extra typing for the same result.


"""


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Follow-up: Could you solve the problem in linear time and in O(1) space?

# Boyer–Moore Voting Algorithm Solution
def majorityElement(nums):
    count = 0         
    candidate = None   

    for num in nums:         
        if count == 0:          
            candidate = num     
        
        if candidate == num:    
            count += 1          
        else:                   
            count -= 1          

    return candidate   

nums = [1, 3, 3]
print(majorityElement(nums))  # Output: 3


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown – Boyer–Moore Voting Algorithm 
def majorityElement(nums):
    count = 0          # Tracks "votes" for current candidate
    candidate = None   # Current suspected majority element

    for num in nums:            # One pass through array
        if count == 0:          # No active candidate
            candidate = num     # Pick current number as new candidate
        
        if candidate == num:    # If current number matches candidate
            count += 1          # Give it a vote
        else:                   # Otherwise
            count -= 1          # Cancel out one vote

    return candidate    # Guaranteed to be majority (problem says it exists)


"""
Time: O(N)
  - Let N = length of nums.
  - Single pass through nums.
  - For each element:
      • Compare to candidate → O(1).
      • Update count in O(1).
  - No nested loops or additional passes.
  - Overall: O(N).

Space: O(1)
  - Stores only two scalar variables: count and candidate.
  - No extra arrays, maps, or data structures used.
  - Overall: O(1).

  
Interview Answer: Worst Case

Time: O(N)
  - Boyer-Moore scans the list once.

Space: O(1)
  - Tracks only a running candidate and counter.


---
Overview for Each Iteration
Input: nums = [1, 3, 3]

i | num | count == 0 | candidate | count before | Action          | count after
--|-----|------------|-----------|--------------|-----------------|------------
0 | 1   | True       | None → 1  | 0            | set candidate=1 | +1 → 1
1 | 3   | False      | 1         | 1            | num ≠ candidate | -1 → 0
2 | 3   | True       | 3         | 0            | set candidate=3 | +1 → 1

Final: candidate = 3 → return 3


---
Most IMPORTANT thing to Understand:
    • The majority element appears MORE than n/2 times — it has more “support” than all other numbers combined.

    • Boyer-Moore's key idea: pair up every occurrence of the majority element with a different element — the majority element ALWAYS survives.

    • The algorithm keeps a running "candidate" and a "vote count." If the count ever hits zero, we pick a new candidate.

---
Why this code Works:
    • Data structure: No extra space — just a candidate and a counter.

    • Technique (voting):
        • When num == candidate → +1 vote.
        • When num != candidate → -1 vote cancels it.
        • Majority element can't be fully canceled because it appears more than all others combined.

    • Efficiency:
        • One-pass scan (O(N)).
        • O(1) space.
        • No hashing, no sorting.

    • Intuition:
        • Think of it as a tournament: every time the candidate meets a different number, they knock each other out.  
        • The majority element has too many “copies” to be eliminated.

---
TLDR:
    • This works because the majority element cannot lose all its votes — it survives the canceling process and becomes the final candidate.

---
Quick Example Walkthrough:

    nums = [1, 3, 3]

    Start:
        candidate=None, count=0

    1) num=1  
        count==0 → candidate=1  
        count=1

    2) num=3  
        different → count=0  
        (candidate "loses all votes")

    3) num=3  
        count==0 → candidate=3  
        count=1

    Final candidate = 3  
    This is the majority element.


---
Quick Example Walkthrough:

    nums = [3, 1, 1, 3, 3, 3]

    Start:
        candidate=None, count=0

    1) num=3
        count==0 → candidate=3
        count=1

    2) num=1
        different → count=0
        (candidate loses all votes)

    3) num=1
        count==0 → candidate=1
        count=1

    4) num=3
        different → count=0
        (candidate loses all votes again)

    5) num=3
        count==0 → candidate=3
        count=1

    6) num=3
        same → count=2

    Final candidate = 3  
    This is the majority element.

"""




# ============================================================
# 📘 GUIDE: What is key= used for?
# Sorting & Selecting the Smart Way
# ============================================================
"""
What is key= ?

    key= tells Python HOW TO COMPARE the items.
    Instead of comparing items by their face value,
    it calls the function you give it on each item
    and compares THOSE RESULTS instead.

    It changes the RULER, not what gets returned.

    • Without key=  
    →  max([3, 1, 2])  →  compares 3, 1, 2 directly  
    →  returns 3

    • With key=     
    →  max(["hi", "banana"], key=len)  →  compares lengths  
    →  returns "banana"


Important rule:
    key= expects a FUNCTION, not a result.

    • count.get      → gives max() a TOOL to use later  ✅
    • count.get()    → runs the tool right now (wrong)   ❌

TLDR:
    key=   → "Sort or pick based on this function's result"

Why no parentheses?
    We want max() to CALL the function for us internally
    on each item it checks. 
    We hand over the tool — max() decides when to use it.
"""

# --------------------------
# Basic Example (Strings)
# --------------------------
words = ["hi", "banana", "yo"]

# key=len  → "Use length to decide which is biggest"
longest = max(words, key=len)

print(longest)   # Output: "banana"

# Behind the scenes, max() does this:
#   len("hi")      → 2
#   len("banana")  → 6
#   len("yo")      → 2
#   6 is biggest   → returns "banana"  (the original item, NOT 6)


# ------------------------------------
# Example Inside a Function (LeetCode)
# Pick the key with the highest value
# ------------------------------------
def majorityElement(nums):
    count = {}

    for num in nums:
        count[num] = count.get(num, 0) + 1

    # key=count.get → "Compare keys by their values"
    return max(count, key=count.get)

nums = [1, 3, 3]
print(majorityElement(nums))  # Output: 3

# Behind the scenes:
#   1. After the loop, count = {1: 1, 3: 2}
#   2. max() loops through the keys: 1, 3
#   3. For each one, it calls count.get() to decide how to compare:
#        count.get(1)  → 1
#        count.get(3)  → 2
#   4. Python internally holds those results: [1, 2]
#   5. Picks the biggest: 2
#   6. Returns the original key that produced it: 3



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Solution 2: Sorting-Based Middle Element Solution
def majorityElement(nums):
    nums.sort()
    return nums[len(nums) // 2]

nums = [1, 3, 3]
print(majorityElement(nums))  # Output: 3

"""
Time: O(N log N)
  - Sorting the array dominates the runtime.
  - Accessing the middle element is O(1).
  - Overall: O(N log N).

Space:
  - Algorithmically: O(1) auxiliary space (no extra data structures).
  - In Python: O(N) worst-case due to Timsort's internal buffers.

Interview Answer (Worst Case):
  - Time: O(N log N)
  - Space: O(N) in Python (implementation-dependent)

  
Timsort Internal Buffers (Python)
--------------------------------
  • Python's list.sort() uses Timsort.
  • While it looks in-place, Timsort may allocate
  • temporary internal arrays ("buffers") during sorting.
  • Because of this, sorting can use up to O(N) extra space
  • in the worst case, even though no extra data structures
  • are created by the user.
"""



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Solution 3: Counter-Based Frequency 
from collections import Counter

def majorityElement(nums):
    count = Counter(nums)
    return max(count, key=count.get)

nums = [1, 3, 3]
print(majorityElement(nums))  # Output: 3

# Time:  O(N) 
# Space: O(N)  


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Solution 4: Majority Element Using Hash Map Frequency
from collections import defaultdict

def majorityElement(nums):
    count = defaultdict(int)
    for num in nums:
        count[num] += 1
    
    return max(count, key=count.get)

nums = [1, 3, 3]
print(majorityElement(nums))  # Output: 3

# Time:  O(N) 
# Space: O(N)  




# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute Force
def majorityElement(nums):
    majority_count = len(nums) // 2
    
    for num in nums:
        count = sum(1 for elem in nums if elem == num)
        if count > majority_count:
            return num

nums = [1, 3, 3]
print(majorityElement(nums))  # Output: 3













# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
"""
Goal: Show why the indented version is wrong and the standard Boyer-Moore version is correct.


Example: nums = [1, 3, 3]
Majority element = 2
"""

# Erroneous version
def majorityElement_wrong(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num

            # ← this 4 line block should NOT be indented here
            if candidate == num:  
                count += 1
            else:
                count -= 1

    return candidate


# Correct Boyer-Moore version
def majorityElement_correct(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num

        if candidate == num:
            count += 1
        else:
            count -= 1

    return candidate


nums = [1, 3, 3]

print("Wrong:", majorityElement_wrong(nums))      # 1
print("Correct:", majorityElement_correct(nums))  # 3



"""
Step-by-step walkthrough
nums = [1, 3, 3]


1) ERRONEOUS CODE

Start:
candidate = None, count = 0

num = 1
• count == 0 -> candidate = 1
• inner if runs
• candidate == num -> count = 1
State: candidate = 1, count = 1

num = 3
• count != 0
• outer if does not run
• inner if is nested inside outer if, so it does not run either
State: candidate = 1, count = 1

num = 3
• same thing, nothing runs
State: candidate = 1, count = 1

Return 1  ❌


2) CORRECT CODE

Start:
candidate = None, count = 0

num = 1
• count == 0 -> candidate = 1
• candidate == num -> count = 1
State: candidate = 1, count = 1

num = 3
• count != 0, candidate stays 1
• candidate != num -> count = 0
State: candidate = 1, count = 0

num = 3
• count == 0 -> candidate = 3
• candidate == num -> count = 1
State: candidate = 3, count = 1

Return 3  ✅


Core difference:
- Wrong code: vote update only happens when count == 0
- Correct code: vote update happens every iteration

That is why the wrong code gets stuck on the first element.
"""