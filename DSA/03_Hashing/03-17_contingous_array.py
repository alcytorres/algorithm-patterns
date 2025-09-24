# 525. Contiguous Array

# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
 
# Example 1:
    # Input: nums = [0, 1]
    # Output: 2
    # Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

# Example 2:
    # Input: nums = [0, 1, 0]
    # Output: 2
    # Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

# Example 3:
    # Input: nums = 0, 1, 1, 1, 1, 1, 0, 0, 0]
    # Output: 6
    # Explanation: [1, 1, 1, 0, 0, 0] is the longest contiguous subarray with equal number of 0 and 1.

# WARNGING: Do NOT try to do the iterations in you head. View the iterations table

# Solution: https://leetcode.com/problems/contiguous-array/editorial/


from collections import defaultdict

def findMaxLength(nums):
    # Step 1: Initialize variables
    counts = defaultdict(int)
    counts[0] = -1            
    diff = 0                 
    max_length = 0        
    
    # Step 2: Process each number
    for i, num in enumerate(nums):
        if num == 1:
            diff += 1         # Add 1 for a 1
        else:
            diff -= 1         # Subtract 1 for a 0

        if diff in counts:    
            max_length = max(max_length, i - counts[diff])  
        else:
            counts[diff] = i  
    
    return max_length


nums = [0, 1, 1, 1, 1, 0, 0]
print(findMaxLength(nums))
# Output 4

# Key (diff): the current score = (# of 1s so far) - (# of 0s so far)
# Value (index): the earliest position where that score was seen.


"""
Time: O(N)
  - Let N = length of nums.
  - Step 1: Initialize dictionary and variables → O(1).
  - Step 2: Single pass over nums → O(N).
      • Update diff in O(1).
      • Dictionary lookup and update in O(1) average.
  - Overall: O(N).

Space: O(N)
  - Dictionary 'counts' stores first index for each diff value.
  - In worst case, diff takes a new value at each index → O(N).
  - Extra variables (diff, max_length, loop index) are O(1).
  - Overall: O(N).

  
Interview Answer: Worst Case

Time: O(N)
  - Single pass, dictionary lookups are O(1).

Space: O(N)
  - Dictionary may hold up to N different diff values.


Overview for Each Iteration
Input: nums = [0, 1, 1, 1, 1, 0, 0]
Step: Process array to find longest subarray with equal 0s and 1s
i | num | diff | counts[diff] | max_length   | counts
--|-----|------|--------------|--------------|-----------------------------
- | -   | 0    | -1           | 0            | {0:-1}
0 | 0   | -1   | absent       | 0            | {0:-1, -1:0}
1 | 1   | 0    | -1           | 2 (1 - (-1)) | {0:-1, -1:0}
2 | 1   | 1    | absent       | 2            | {0:-1, -1:0, 1:2}
3 | 1   | 2    | absent       | 2            | {0:-1, -1:0, 1:2, 2:3}
4 | 1   | 3    | absent       | 2            | {0:-1, -1:0, 1:2, 2:3, 3:4}
5 | 0   | 2    | 3            | 2            | {0:-1, -1:0, 1:2, 2:3, 3:4}
6 | 0   | 1    | 2            | 4 (6 - 2)    | {0:-1, -1:0, 1:2, 2:3, 3:4}
Final: 4 ([1, 1, 0, 0])



# -------------------------------------------------------
Q: What are the key and value of the hash table?
    • Key (diff): the current score = (# of 1s so far) - (# of 0s so far).
    • Value (index): the earliest position where that score was seen.


Q: How is the hash map in the Contiguous Array problem different from the ones we usually use in LeetCode?

    • A: In most problems, the hash map tracks frequencies (how many times a number or character appears).

    • Here, the hash map tracks first-seen indices for each running balance (diff).

    • 👉 Instead of “how many times something appears,” we store “where we first saw this score,” so we can later measure the length of subarrays with equal 0s and 1s.


# -------------------------------------------------------
Q: WHY the FOR LOOP WORKS 

     • Loop structure:  for i, num in enumerate(nums):
        We need both the element (num) and its position (i), because the index tells us where a score first happened and lets us calculate subarray lengths.

    • Update score  (diff):
        Add +1 for a 1, subtract -1 for a 0.
        → This running score shows how many more 1s than 0s we've seen so far.

    • Check notebook:  if diff in counts:
        If this score was seen before, the subarray between then and now must balance out (same number of 0s and 1s).
        → Length = current index - first index of this score.

    • Update max length: max_length = max(max_length, i - counts[diff]):
        Compare the current balanced subarray length with the best one so far and keep the maximum.

    • Update notebook (counts[diff] = i):
        If this score hasn't been seen yet, record the index where it first appeared.
        → Important: only store the earliest index, since that gives the longest subarray later.

    • Why it finds the answer:
        Same score twice = balance in between. By always comparing with the first time that score appeared, we guarantee we find the longest balanced chunk.


# -------------------------------------------------------
Most IMPORTANT thing to Understand:
    • We want the longest subarray where 0s and 1s are equal.  

    • Replace each 1 with +1 and each 0 with -1.  
      → Now the problem becomes finding the longest subarray where the total sum = 0 (equal 1s and 0s).  

    • diff = running balance (how many more 1s than 0s we've seen so far).  

    • If the same diff value shows up again, everything between those two indices must have balanced out (equal 0s and 1s).  

    
Why this code Works:
    • Hash map (counts): stores the first index where each diff value was seen.  

    • Prefix sum idea: diff acts like a prefix sum of (+1 for 1, -1 for 0).  
      → If diff repeats at index i and j, the subarray between i+1 and j has net zero difference → equal 0s and 1s.  

    • Efficiency: O(n) because we only scan once and use O(1) lookups in the map.Brute force would check every subarray in O(n²).  

    • Intuition: Treat diff like a scoreboard. If you see the same score at two indices, the segment between them sums to 0 → equal 0s and 1s.

    
TLDR:
    • Track the balance of 1s and 0s with diff; if diff repeats, the subarray between those two points is balanced.  

    
Quick Example Walkthrough:
    nums = [0, 1, 1, 1, 1, 0, 0]

    Step 1: Initialize counts = {0:-1} (diff=0 seen before the array starts).  
            This lets us catch subarrays starting at index 0.  

    Step 2: Process each element:

    i=0, num=0 → diff=-1 (first time) → save counts[-1]=0.  
    i=1, num=1 → diff=0 (seen at -1) → subarray length = 1 - (-1) = 2.  
    i=2, num=1 → diff=1 (first time) → save counts[1]=2.  
    i=3, num=1 → diff=2 (first time) → save counts[2]=3.  
    i=4, num=1 → diff=3 (first time) → save counts[3]=4.  
    i=5, num=0 → diff=2 (seen at 3) → subarray length = 5 - 3 = 2.  
    i=6, num=0 → diff=1 (seen at 2) → subarray length = 6 - 2 = 4.  

    Step 3: Maximum length found = 4.  

    Final Answer: 4 → Longest balanced subarray is [1, 1, 0, 0] (indices 3-6).




# -------------------------------------------------------
Q: Why counts[0] = -1?

    What it does: Pretends the score 0 happened at index -1 (before the array starts).

    Why needed: This lets us catch subarrays that start at index 0. When diff returns to 0, we can measure the full length as i - (-1).

    Example:
    For [0, 1]:

    At index 1, diff = 0.
    With counts[0] = -1, length = 1 - (-1) = 2 → correct full subarray [0, 1].

    Why it works: It sets a baseline: we “start” balanced (0 score). So anytime we return to score 0, the subarray from the beginning is counted.

    Without it: Subarrays beginning at index 0 would never be recognized as balanced.


# -------------------------------------------------------
Why “Score is 0 before we start”?
    • Before we look at any numbers, we haven't seen any 1s or 0s, so our score (diff = 1s - 0s) is 0 (no hills or valleys yet).

    • We set counts[0] = -1 to say, “At step -1 (before the list), our score was 0.” This helps us catch subarrays starting from index 0.

    Example: nums = [0, 1] (Output: 2)
    Start: counts = {0: -1}, diff = 0, max_length = 0.

    Step 0 (num = 0):
        diff = 0 - 1 = -1. Not in counts. Add counts[-1] = 0.
        max_length = 0.

    Step 1 (num = 1):
        diff = -1 + 1 = 0. counts[0] = -1 exists!
        Length = 1 - (-1) = 2 (chunk [0, 1] has one 0, one 1).
        max_length = 2.

Why counts[0] = -1 worked: When diff = 0 at step 1, we found a balanced chunk from the start (step -1 to 1), giving length 2.


Analogy
    • Imagine walking along a path.
    • Each 1 = step up (+1).
    • Each 0 = step down (-1).
    • Your running score (diff) = your current height.
    • At the start, you’re at ground level (diff = 0).
    • We record: “Ground level first seen at index -1.”
    • Why -1? So if we return to ground level later (like after [0, 1]), the subarray length is current_index - (-1) → includes the whole chunk starting at index 0.

Why It Works
    • counts[0] = -1 lets us catch balanced subarrays starting from the beginning. 
    • Without it, we'd miss chunks like [0, 1]. Only -1 gives the correct length for these cases!

"""




# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
from collections import defaultdict

def findMaxLength(nums):
    # Step 1: Initialize variables
    counts = defaultdict(int)  # Notebook to store difference and index
    counts[0] = -1            # Start with difference 0 at index -1
    diff = 0                  # Running difference (1s count - 0s count)
    max_length = 0            # Longest subarray length

    # Step 2: Process each number
    for i, num in enumerate(nums):  # Check each number and step
        if num == 1:
            diff += 1         # Add 1 for a 1
        else:
            diff -= 1         # Subtract 1 for a 0

        if diff in counts:    # If we've seen this difference before, Found a balanced chunk!
            max_length = max(max_length, i - counts[diff])  # Update longest length
        else:
            counts[diff] = i  # Store new difference with current index

    return max_length



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force
def findMaxLength_bruteforce(nums):
    n = len(nums)
    ans = 0

    for i in range(n):
        zeros = ones = 0
        for j in range(i, n):
            if nums[j] == 0:
                zeros += 1
            else:
                ones += 1
            if zeros == ones:
                ans = max(ans, j - i + 1)

    return ans

nums = [0, 1, 1, 1, 1, 1, 0, 0, 0]
print(findMaxLength_bruteforce(nums))
# Output: 6


"""
Time: O(n^2)
  - Outer loop picks a start index i: O(n).
  - Inner loop extends subarray to j: O(n).
  - Each step updates counts and compares zeros/ones in O(1).
  - Overall: O(n * n) = O(n^2) time.

Space: O(1)
  - Only a constant number of variables (ans, i, j, zeros, ones) are used.
  - No additional data structures.
  - Overall: O(1) space.


Trace Overview
nums = [0,1,1,1,1,1,0,0,0]
i=0: j=1 → zeros=1, ones=1 → len=2 (ans=2)
i=1: (no equal-length found; more 1s than 0s ahead)
i=2: (no equal-length found)
i=3: j=8 → subarray [1,1,1,0,0,0] → zeros=3, ones=3 → len=6 (ans=6)
i=4: j=7 → [1,1,0,0] → len=4 (ans stays 6)
i=5: j=6 → [1,0] → len=2 (ans stays 6)
i=6..8: only 0s remain → no equal-length updates
Final ans = 6

"""


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Best Solution

from collections import defaultdict

def findMaxLength(nums):
    # Step 1: Initialize variables
    counts = defaultdict(int)
    counts[0] = -1            
    diff = 0                 
    max_length = 0        
    
    # Step 2: Process each number
    for i, num in enumerate(nums):
        if num == 1:
            diff += 1         # Add 1 for a 1
        else:
            diff -= 1         # Subtract 1 for a 0

        if diff in counts:    
            max_length = max(max_length, i - counts[diff])  
        else:
            counts[diff] = i  
    
    return max_length


nums = [0, 1]
print(findMaxLength(nums))
# Output 2

"""
Overview for Each Iteration
Input: nums = [0, 1]
Step: Process array to find longest subarray with equal 0s and 1s
i | num | diff | counts[diff] | max_length   | counts
--|-----|------|--------------|--------------|-------------
- | -   | 0    | -1           | 0            | {0:-1}
0 | 0   | -1   | absent       | 0            | {0:-1, -1:0}
1 | 1   | 0    | -1           | 2 (1 - (-1)) | {0:-1, -1:0}
Final: 2 ([0, 1])


"""


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Best Solution

from collections import defaultdict

def findMaxLength(nums):
    # Step 1: Initialize variables
    counts = defaultdict(int)
    counts[0] = -1            
    diff = 0                 
    max_length = 0        
    
    # Step 2: Process each number
    for i, num in enumerate(nums):
        if num == 1:
            diff += 1         # Add 1 for a 1
        else:
            diff -= 1         # Subtract 1 for a 0

        if diff in counts:    
            max_length = max(max_length, i - counts[diff])  
        else:
            counts[diff] = i  
    
    return max_length


nums = [0, 1, 1, 1, 1, 1, 0, 0, 0]
print(findMaxLength(nums))
# Output: 6

"""
Overview for Each Iteration
Input: nums = [0, 1, 1, 1, 1, 1, 0, 0, 0]
Step: Process array to find longest subarray with equal 0s and 1s
i | num | diff | counts[diff] | max_length   | counts
--|-----|------|--------------|--------------|---------------------------------
- | -   | 0    | -1           | 0            | {0:-1}
0 | 0   | -1   | absent       | 0            | {0:-1, -1:0}
1 | 1   | 0    | -1           | 2 (1 - (-1)) | {0:-1, -1:0}
2 | 1   | 1    | absent       | 2            | {0:-1, -1:0, 1:2}
3 | 1   | 2    | absent       | 2            | {0:-1, -1:0, 1:2, 2:3}
4 | 1   | 3    | absent       | 2            | {0:-1, -1:0, 1:2, 2:3, 3:4}
5 | 1   | 4    | absent       | 2            | {0:-1, -1:0, 1:2, 2:3, 3:4, 4:5}
6 | 0   | 3    | 4            | 2 (6 - 4)    | {0:-1, -1:0, 1:2, 2:3, 3:4, 4:5}
7 | 0   | 2    | 3            | 4 (7 - 3)    | {0:-1, -1:0, 1:2, 2:3, 3:4, 4:5}
8 | 0   | 1    | 2            | 6 (8 - 2)    | {0:-1, -1:0, 1:2, 2:3, 3:4, 4:5}
Final: 6 ([1, 1, 1, 0, 0, 0])


Quick Example Walkthrough:
    nums = [0, 1, 1, 1, 1, 1, 0, 0, 0]  

    Step 1: Initialize counts = {0:-1} (diff=0 seen before the array starts).  
            This lets us catch subarrays starting at index 0.  

    Step 2: Process elements one by one:  

        i=0, num=0 → diff=-1 (first time) → save counts[-1]=0.  
        i=1, num=1 → diff=0 (seen at -1) → subarray length = 1 - (-1) = 2.  
        i=2, num=1 → diff=1 (first time) → save counts[1]=2.  
        i=3, num=1 → diff=2 (first time) → save counts[2]=3.  
        i=4, num=1 → diff=3 (first time) → save counts[3]=4.  
        i=5, num=1 → diff=4 (first time) → save counts[4]=5.  
        i=6, num=0 → diff=3 (seen at 4) → subarray length = 6 - 4 = 2.  
        i=7, num=0 → diff=2 (seen at 3) → subarray length = 7 - 3 = 4.  
        i=8, num=0 → diff=1 (seen at 2) → subarray length = 8 - 2 = 6.  

    Step 3: Maximum length found = 6.  

    Final Answer: 6 → subarray [1, 1, 1, 0, 0, 0].  

"""



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Best Solution

from collections import defaultdict

def findMaxLength(nums):
    # Step 1: Initialize variables
    counts = defaultdict(int)
    counts[0] = -1            
    diff = 0                 
    max_length = 0        
    
    # Step 2: Process each number
    for i, num in enumerate(nums):
        if num == 1:
            diff += 1         # Add 1 for a 1
        else:
            diff -= 1         # Subtract 1 for a 0

        if diff in counts:    
            max_length = max(max_length, i - counts[diff])  
        else:
            counts[diff] = i  
    
    return max_length


nums = [0, 1, 1, 0, 0]
print(findMaxLength(nums))
# Output 4


"""
Full Overview for Each Iteration
Input: nums = [0, 1, 1, 0, 0]
Step: Process array to find longest subarray with equal 0s and 1s
i | num | diff | counts[diff] | max_length   | counts
--|-----|------|--------------|--------------|------------------
- | -   | 0    | -1           | 0            | {0:-1}
0 | 0   | -1   | absent       | 0            | {0:-1, -1:0}
1 | 1   | 0    | -1           | 2 (1 - (-1)) | {0:-1, -1:0}
2 | 1   | 1    | absent       | 2            | {0:-1, -1:0, 1:2}
3 | 0   | 0    | -1           | 2 (3 - (-1)) | {0:-1, -1:0, 1:2}
4 | 0   | -1   | 0            | 4 (4 - 0)    | {0:-1, -1:0, 1:2}
Final: 4 ([1, 1, 0, 0])

"""


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Alternate Solution

def findMaxLength(nums):
    prefix_index = {0: -1}   # prefix sum value -> first index seen
    prefix_sum = 0           # running balance of 1s and 0s (0→-1, 1→+1)
    max_length = 0           # longest subarray length found

    for i, num in enumerate(nums):
        prefix_sum += 1 if num == 1 else -1

        if prefix_sum in prefix_index:
            max_length = max(max_length, i - prefix_index[prefix_sum])
        else:
            prefix_index[prefix_sum] = i

    return max_length

nums = [0, 1, 1, 1, 1, 1, 0, 0, 0]
print(findMaxLength(nums))
# Output: 6



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Playground 

def fn(nums):
    ans = {}
    for i, num in enumerate(nums):
        ans[i] = num
    return ans
    
nums = ['a', 'b', 'c']
print(fn(nums))
# Output: {0: 'a', 1: 'b', 2: 'c'}


nums = ['a', 'b', 'c']
for i, num in enumerate(nums):
    print(i, num)  
# Output:
# 0 a
# 1 b
# 2 c





# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Full Breakdown 

# Task: Find the maximum length of a contiguous subarray with equal numbers of 0s and 1s.
# Example: nums = [0, 1, 1, 1, 1, 1, 0, 0, 0] → Output = 6 (subarray [1, 1, 1, 0, 0, 0])
# Why: Practices prefix sum technique with a hash map to track balance of 0s and 1s.

from collections import defaultdict

def findMaxLength(nums):  # Example: nums = [0, 1, 1, 1, 1, 1, 0, 0, 0]

    # 1️⃣ Initialize variables
    # Initialize a defaultdict to store the first index of each prefix sum difference
    # Why? We track the difference (count of 1s - count of 0s) to find equal counts
    counts = defaultdict(int)  # counts = {}
    counts[0] = -1  # Initialize diff=0 at index -1
    # Why? Allows subarrays starting from index 0 to be considered

    # Initialize difference (count of 1s minus count of 0s)
    # Why? Equal 0s and 1s means diff = 0 for a subarray
    diff = 0  # diff = 0

    # Initialize max_length to track the longest valid subarray
    # Why? We need to store the maximum length of subarrays with equal 0s and 1s
    max_length = 0  # max_length = 0

    # 2️⃣ Process each number
    # Iterate through the array with index and value
    # Why? We need to compute the running difference and check for previous occurrences
    for i, num in enumerate(nums):  # i, num takes values (0, 0), (1, 1), ..., (8, 0)
        # --- Iteration 1: i = 0, num = 0 ---
        # Update diff: add 1 for 1, subtract 1 for 0
        # Why? Treat 1 as +1 and 0 as -1 to balance counts
        if num == 1:
            diff += 1  # skip
        else:
            diff -= 1  # diff = 0 - 1 = -1
        # Check if current diff was seen before
        # Why? If diff was seen at index j, subarray [j+1:i] has equal 0s and 1s
        if diff in counts:  # diff = -1, counts = {0: -1}, -1 not in counts, skip
            max_length = max(max_length, i - counts[diff])  # skip
        else:
            counts[diff] = i  # counts[-1] = 0
        # After Iteration 1: diff = -1, max_length = 0, counts = {0: -1, -1: 0}

        # --- Iteration 2: i = 1, num = 1 ---
        if i == 1 and num == 1:
            if num == 1:
                diff += 1  # diff = -1 + 1 = 0
            else:
                diff -= 1
            if diff in counts:  # diff = 0, counts = {0: -1, -1: 0}, 0 in counts
                max_length = max(max_length, i - counts[diff])  # i = 1, counts[0] = -1
                                                               # max_length = max(0, 1 - (-1)) = 2
            else:
                counts[diff] = i  # skip
            # After Iteration 2: diff = 0, max_length = 2, counts = {0: -1, -1: 0}
            # Found subarray: [0, 1] (1 zero, 1 one, length 2)

        # --- Iteration 3: i = 2, num = 1 ---
        if i == 2 and num == 1:
            if num == 1:
                diff += 1  # diff = 0 + 1 = 1
            else:
                diff -= 1
            if diff in counts:  # diff = 1, counts = {0: -1, -1: 0}, 1 not in counts
                max_length = max(max_length, i - counts[diff])
            else:
                counts[diff] = i  # counts[1] = 2
            # After Iteration 3: diff = 1, max_length = 2, counts = {0: -1, -1: 0, 1: 2}

        # --- Iteration 4: i = 3, num = 1 ---
        if i == 3 and num == 1:
            if num == 1:
                diff += 1  # diff = 1 + 1 = 2
            else:
                diff -= 1
            if diff in counts:  # diff = 2, counts = {0: -1, -1: 0, 1: 2}, 2 not in counts
                max_length = max(max_length, i - counts[diff])
            else:
                counts[diff] = i  # counts[2] = 3
            # After Iteration 4: diff = 2, max_length = 2, counts = {0: -1, -1: 0, 1: 2, 2: 3}

        # --- Iteration 5: i = 4, num = 1 ---
        if i == 4 and num == 1:
            if num == 1:
                diff += 1  # diff = 2 + 1 = 3
            else:
                diff -= 1
            if diff in counts:  # diff = 3, counts = {0: -1, -1: 0, 1: 2, 2: 3}, 3 not in counts
                max_length = max(max_length, i - counts[diff])
            else:
                counts[diff] = i  # counts[3] = 4
            # After Iteration 5: diff = 3, max_length = 2, counts = {0: -1, -1: 0, 1: 2, 2: 3, 3: 4}

        # --- Iteration 6: i = 5, num = 1 ---
        if i == 5 and num == 1:
            if num == 1:
                diff += 1  # diff = 3 + 1 = 4
            else:
                diff -= 1
            if diff in counts:  # diff = 4, counts = {0: -1, -1: 0, 1: 2, 2: 3, 3: 4}, 4 not in counts
                max_length = max(max_length, i - counts[diff])
            else:
                counts[diff] = i  # counts[4] = 5
            # After Iteration 6: diff = 4, max_length = 2, counts = {0: -1, -1: 0, 1: 2, 2: 3, 3: 4, 4: 5}

        # --- Iteration 7: i = 6, num = 0 ---
        if i == 6 and num == 0:
            if num == 1:
                diff += 1
            else:
                diff -= 1  # diff = 4 - 1 = 3
            if diff in counts:  # diff = 3, counts = {0: -1, -1: 0, 1: 2, 2: 3, 3: 4, 4: 5}, 3 in counts
                max_length = max(max_length, i - counts[diff])  # i = 6, counts[3] = 4
                                                               # max_length = max(2, 6 - 4) = 2
            else:
                counts[diff] = i  # skip
            # After Iteration 7: diff = 3, max_length = 2, counts = {0: -1, -1: 0, 1: 2, 2: 3, 3: 4, 4: 5}

        # --- Iteration 8: i = 7, num = 0 ---
        if i == 7 and num == 0:
            if num == 1:
                diff += 1
            else:
                diff -= 1  # diff = 3 - 1 = 2
            if diff in counts:  # diff = 2, counts = {0: -1, -1: 0, 1: 2, 2: 3, 3: 4, 4: 5}, 2 in counts
                max_length = max(max_length, i - counts[diff])  # i = 7, counts[2] = 3
                                                               # max_length = max(2, 7 - 3) = 4
            else:
                counts[diff] = i  # skip
            # After Iteration 8: diff = 2, max_length = 4, counts = {0: -1, -1: 0, 1: 2, 2: 3, 3: 4, 4: 5}
            # Found subarray: [1, 1, 1, 1, 0, 0] (3 zeros, 3 ones, length 6)

        # --- Iteration 9: i = 8, num = 0 ---
        if i == 8 and num == 0:
            if num == 1:
                diff += 1
            else:
                diff -= 1  # diff = 2 - 1 = 1
            if diff in counts:  # diff = 1, counts = {0: -1, -1: 0, 1: 2, 2: 3, 3: 4, 4: 5}, 1 in counts
                max_length = max(max_length, i - counts[diff])  # i = 8, counts[1] = 2
                                                               # max_length = max(4, 8 - 2) = 6
            else:
                counts[diff] = i  # skip
            # After Iteration 9: diff = 1, max_length = 6, counts = {0: -1, -1: 0, 1: 2, 2: 3, 3: 4, 4: 5}
            # Found subarray: [1, 1, 1, 0, 0, 0] (3 zeros, 3 ones, length 6)

    # 3️⃣ Return the maximum length
    # Why? max_length contains the length of the longest subarray with equal 0s and 1s
    return max_length  # max_length = 6


nums = [0, 1, 1, 1, 1, 1, 0, 0, 0]
print(findMaxLength(nums))  
# Output: 6