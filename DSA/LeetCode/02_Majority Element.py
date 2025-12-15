# 169. Given an array nums of size n, return the majority element.
"""
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
    Input: nums = [3, 2, 3]
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

nums = [3, 2, 3]
print(majorityElement(nums))  # Output: 3


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
"""


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


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Follow-up: Could you solve the problem in linear time and in O(1) space?

# Boyer–Moore Voting Algorithm Solution
def majorityElement(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate

nums = [3, 2, 3]
print(majorityElement(nums))  # Output: 3


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
Input: nums = [3, 2, 3]

i | num | count == 0 | candidate | count before | Action          | count after
--|-----|------------|-----------|--------------|-----------------|------------
0 | 3   | True       | None → 3  | 0            | set candidate=3 | +1 → 1
1 | 2   | False      | 3         | 1            | num ≠ candidate | -1 → 0
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

    nums = [3, 2, 3]

    Start:
        candidate=None, count=0

    1) num=3  
        count==0 → candidate=3  
        count=1

    2) num=2  
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

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown – Boyer–Moore Voting Algorithm 
def majorityElement(nums):
    count = 0          # Voting counter – how many "votes" the current candidate has
    candidate = None   # Current candidate for majority element

    for num in nums:       # One pass through the array
        if count == 0:     # No active candidate (votes dropped to zero)
            candidate = num # Elect the current number as new candidate
        
        # Vote for or against the candidate
        count += 1 if num == candidate else -1  
        # Same → +1 vote
        # Different → -1 vote (cancels one vote for candidate)

    return candidate   # Guaranteed to be the majority element

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Boyer–Moore Voting Algorithm reformatted
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

    return candidate    # Guaranteed to be majority (by problem says it exists)




# ============================================================
# 📘 Tutorial: Passing a Function (without parentheses) to key=
# ============================================================
"""
Big Idea:
    key= expects a FUNCTION, not a result.

    • count.get      → gives max() a TOOL to use later
    • count.get()    → runs the tool right now (wrong here)

Why no parentheses?
    We want max() to CALL the function for us internally
    on each item it checks.

Use cases:
    • Choose longest string
    • Choose dict key with biggest value
"""

# --------------------------
# Basic Example (Strings)
# --------------------------
words = ["hi", "banana", "yo"]

# key=len  → "Use length to decide which is biggest"
longest = max(words, key=len)

print(longest)   # Output: "banana"


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






# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Option 2: Defaultdict Frequency Scan
from collections import defaultdict

def majorityElement(nums):
    counts = defaultdict(int)

    for num in nums:
        counts[num] += 1

    max_count = 0
    majorityNum = None

    for key, value in counts.items():
        if value > max_count:
            majorityNum = key
            max_count = value
    
    return majorityNum

nums = [3, 2, 3]
print(majorityElement(nums))  # Output: 3

# Time:  O(N) 
# Space: O(N)  


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Counter-Based Frequency Solution
from collections import Counter

def majorityElement(nums):
    count = Counter(nums)
    return max(count, key=count.get)

nums = [3, 2, 3]
print(majorityElement(nums))  # Output: 3

# Time:  O(N) 
# Space: O(N)  


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Dictionary Count + Threshold Check"
def majorityElement_Simple(nums):
    # 1. Initialize a dictionary to store element counts
    counts = {}

    # 2. Iterate through the array and count frequencies
    for num in nums:
        # If the number is already a key, increment its count.
        # Otherwise, add it with a starting count of 1.
        counts[num] = counts.get(num, 0) + 1

    # 3. Determine the majority threshold
    n = len(nums)
    majority_threshold = n // 2  # integer division gives floor(n/2)

    # 4. Find the element whose count exceeds the threshold
    for num, count in counts.items():
        if count > majority_threshold:
            return num

nums = [3, 2, 3]
print(majorityElement(nums))  # Output: 3

# Time:  O(N) 
# Space: O(N)  

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Sorting-Based Middle Element Solution
def majorityElement(nums):
    nums.sort()
    return nums[len(nums) // 2]

nums = [3, 2, 3]
print(majorityElement(nums))  # Output: 3

# Time: O(nlgn)
# Space: O(1) or (O(n))



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute Force
def majorityElement(nums):
    majority_count = len(nums) // 2
    
    for num in nums:
        count = sum(1 for elem in nums if elem == num)
        if count > majority_count:
            return num

nums = [3, 2, 3]
print(majorityElement(nums))  # Output: 3



# DICTIONARY METHOD: 
.get()