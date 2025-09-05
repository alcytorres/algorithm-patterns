# 560. Subarray Sum Equals K

# Example 4: Given an integer array nums and an integer k, find the number of subarrays whose sum is equal to k.

# Example 1:
    # Input: nums = [1, 1, 1], k = 2
    # Output: 2

# Example 2:
    # Input: nums = [1, 2, 3], k = 3
    # Output: 2

# Solution: https://leetcode.com/problems/subarray-sum-equals-k/solutions/127728/subarray-sum-equals-k/


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

# counts = 
# {0:1}
# {0:1,1:1}
# {0:1,1:1,3:1} 
# {0:1,1:1,3:1,4:1}
# {0:1,1:1,3:1,4:1,6:1}
# {0:1,1:1,3:1,4:1,6:1,7:1}

# Overview for Each Iteration
# Input: nums = [1, 2, 1, 2, 1], k = 3
# Step: Process array to find subarrays with sum k
# Idx | num | curr | curr - k | counts[curr - k] | ans | counts
# -   | -   | 0    | -        | -                | 0   | {0:1}
# 0   | 1   | 1    | 1-3=-2   | 0                | 0   | {0:1, 1:1}
# 1   | 2   | 3    | 3-3=0    | 1                | 1   | {0:1, 1:1, 3:1}
# 2   | 1   | 4    | 4-3=1    | 1                | 2   | {0:1, 1:1, 3:1, 4:1}
# 3   | 2   | 6    | 6-3=3    | 1                | 3   | {0:1, 1:1, 3:1, 4:1, 6:1}
# 4   | 1   | 7    | 7-3=4    | 1                | 4   | {0:1, 1:1, 3:1, 4:1, 6:1, 7:1}
# Final: 4 (subarrays [1,2], [2,1], [1,2], [2,1])


# Time: O(n)
# - Loop through nums once: O(n) iterations.
# - Dictionary lookups and updates ('counts[curr - k]', 'counts[curr] += 1') are O(1) on average.
# - No nested loops, so total time is O(n).

# Space: O(n)
# - Dictionary 'counts' can store up to n different prefix sums in the worst case: O(n) space.
# - A few variables (curr, ans, num) take O(1) space.
# - Overall: O(n) total space.



# Note: The code determines only the total number of subarrays with a sum equal to k, confirming their existence through prefix sum matches without specifying which subarrays they are.

# Most IMPORTANT thing to Understand for this solution:
# ans += counts[curr - k] works simply because if curr - k (a previous sum, let’s call it prev) is in counts, then curr - prev = k, meaning the subarray between those points sums to k, and counts[curr - k] counts how many such prev sums exist.




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


# Time: O(n^2)
# - Outer loop runs n times.
# - Inner loop runs up to n times for each outer loop, computing subarray sums.
# - Overall: O(n^2) time.

# Space: O(1)
# - Only a constant number of variables (ans, curr, i, j) are used.
# - No additional data structures.
# - Overall: O(1) space.


# Trace Overview
# i        = 0 -  - -  1 - -  2 - -  3 - -  4 -
# j        = 0 -  1 2  1 - 2 3  2 - 3 4  3 - 4  4 -
# curr     = 0 1  3 4  0 2 3 5  0 1 3 5  0 2 4  0 1
# ans      = 0 0  1 1  1 1 2 2  2 2 3 3  3 3 4  4



# ––––––––––––––––––––––––––––––––––––––––––––––––
# Simple Breakdown 
from collections import defaultdict

def subarraySum(nums, k):
    counts = defaultdict(int)  # Track frequency of prefix sums
    counts[0] = 1             # Initialize for subarrays starting at index 0
    ans = curr = 0            # ans: counts subarrays, curr: running sum

    for num in nums:          # Iterate over each number
        curr += num            # Add current number to running sum
        ans += counts[curr - k]  # Count subarrays where sum = k
        counts[curr] += 1     # Increment frequency of current sum
        
    return ans                # Return total subarrays with sum k



# ––––––––––––––––––––––––––––––––––––––––––––––––
# Super Simple Breakdown of LeetCode 560: Subarray Sum Equals K
# The goal is to count subarrays in nums that sum to k. The code uses a running sum (curr) and a defaultdict (counts) to track prefix sums.

# Why ans += counts[curr - k]?
# * curr is the sum from start to current index.
# * If curr - k is in counts, it means a previous sum exists where curr - prev = k, forming a subarray with sum k.
# * counts[curr - k] tells how many such subarrays end at the current index.

# Walkthrough for nums = [1, 2, 1, 2, 1], k = 3:
# * Start: counts = {0: 1}, ans = 0, curr = 0
# * Iteration 1: num = 1:
#   * curr = 0 + 1 = 1
#   * curr - k = 1 - 3 = -2. counts[-2] = 0 → ans = 0
#   * counts[1] += 1 → counts = {0: 1, 1: 1}
# * Iteration 2: num = 2:
#   * curr = 1 + 2 = 3
#   * curr - k = 3 - 3 = 0. counts[0] = 1 → ans = 0 + 1 = 1 (found [1, 2])
#   * counts[3] += 1 → counts = {0: 1, 1: 1, 3: 1}
# * Iteration 3: num = 1:
#   * curr = 3 + 1 = 4
#   * curr - k = 4 - 3 = 1. counts[1] = 1 → ans = 1 + 1 = 2 (found [2, 1])
#   * counts[4] += 1 → counts = {0: 1, 1: 1, 3: 1, 4: 1}
# * Iteration 4: num = 2:
#   * curr = 4 + 2 = 6
#   * curr - k = 6 - 3 = 3. counts[3] = 1 → ans = 2 + 1 = 3 (found [1, 2])
#   * counts[6] += 1 → counts = {0: 1, 1: 1, 3: 1, 4: 1, 6: 1}
# * Iteration 5: num = 1:
#   * curr = 6 + 1 = 7
#   * curr - k = 7 - 3 = 4. counts[4] = 1 → ans = 3 + 1 = 4 (found [2, 1])
#   * counts[7] += 1 → counts = {0: 1, 1: 1, 3: 1, 4: 1, 6: 1, 7: 1}
# * Return: ans = 4

# Key Takeaway:
# * ans += counts[curr - k] counts subarrays by checking if a previous sum makes the current subarray sum to k = 3.
# * Output: 4 (subarrays [1, 2] at 0-1, [2, 1] at 1-2, [1, 2] at 2-3, [2, 1] at 3-4).


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

nums = [1, 2, 3]
k = 3
print(subarraySum(nums, k))
# Output: 2 (subarrays [1, 2] and [3])

# counts = {0: 1, 1: 1, 3: 1, 6: 1}


# Trace Overview
# Index = -  0  1  2
# num   = -  1  2  3
# curr  = 0  1  3  6
# ans   = 0  0  1  2
# counts = {0:1} {0:1, 1:1} {0:1, 1:1, 3:1} {0:1, 1:1, 3:1, 6:1}



# ––––––––––––––––––––––––––––––––––––––––––––––––
# 560. Subarray Sum Equals K
# Goal: Count subarrays in nums that sum to k using prefix sums and a hash map.


# Why `ans += counts[curr - k]`?
# - curr: sum from start to current index.
# - If curr - k is in counts, a previous sum exists where curr - prev = k.
# - counts[curr - k] gives number of such subarrays.

# Walkthrough for nums = [1, 2, 3], k = 3:
# Start: counts = {0: 1}, ans = 0, curr = 0
# Iteration 1 (num = 1):
#   - curr = 0 + 1 = 1
#   - curr - k = 1 - 3 = -2, counts[-2] = 0 → ans = 0
#   - counts[1] += 1 → counts = {0: 1, 1: 1}
# Iteration 2 (num = 2):
#   - curr = 1 + 2 = 3
#   - curr - k = 3 - 3 = 0, counts[0] = 1 → ans = 0 + 1 = 1 (found [1, 2])
#   - counts[3] += 1 → counts = {0: 1, 1: 1, 3: 1}
# Iteration 3 (num = 3):
#   - curr = 3 + 3 = 6
#   - curr - k = 6 - 3 = 3, counts[3] = 1 → ans = 1 + 1 = 2 (found [3])
#   - counts[6] += 1 → counts = {0: 1, 1: 1, 3: 1, 6: 1}
# Return: ans = 2



# ––––––––––––––––––––––––––––––––––––––––––––––––
# Task: Find the number of subarrays with sum equal to k in an integer array.
# Example: nums = [1, 2, 3], k = 3 → Output = 2 (subarrays: [1, 2], [3])
# Why: Practices prefix sum technique with a hash map to efficiently count subarrays.

from collections import defaultdict

def subarraySum(nums, k):  # Example: nums = [1, 2, 3], k = 3

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
    for num in nums:  # num takes values [1, 2, 3]
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

        # --- Iteration 3: num = 3 ---
        if num == 3:
            curr += num  # curr = 3 + 3 = 6
            ans += counts[curr - k]  # curr - k = 6 - 3 = 3, counts[3] = 1, ans = 1 + 1 = 2
            counts[curr] += 1  # counts[6] = 0 + 1 = 1
            # After Iteration 3: curr = 6, ans = 2, counts = {0: 1, 1: 1, 3: 1, 6: 1}
            # Found subarray: [3] (sum = 3, index 2)

    # 3️⃣ Return the count of valid subarrays
    # Why? ans contains the number of subarrays with sum equal to k
    return ans  # ans = 2


numbers = [1, 2, 3]
k = 3
print(subarraySum(numbers, k))  
# Output: 2 (subarrays [1, 2] and [3])

# counts = {0: 1, 1: 1, 3: 1, 6: 1}




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

# counts = {0: 1, 1: 1, 3: 1, 6: 1, 10: 1, 16: 1}


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

# counts = {0: 1, 1: 1, 3: 1, 6: 1, 16: 1, 12: 1, 18: 1}


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

# counts = {0: 2, 1: 2}


# ––––––––––––––––––––––––––––––––––––––––––––––––
# Lesson: Why do I sometimes see "extra" keys like -1:0 in defaultdict?
    # defaultdict will automatically create a key with value 0 whenever you *access* a missing key using square brackets:
    #   counts[x]   -> if x not present, insert x with value 0
    # That’s why you might see something like {-1: 0} at the end.

# Important:
    # - This does NOT affect your algorithm’s correctness.
    # - It only changes the final dictionary representation.

# How to avoid it:
    # - Use counts.get(x, 0) when you just want to *check* a value.
    #   This will return 0 without inserting a new key.

# Takeaway:
    # Remember that defaultdict[int] auto-inserts keys on access.
    # If you don’t want that, use .get() instead.


# -------------------------------
# General Rule:
# ans += counts[curr - k]
# If counts[curr - k] = m, then there are m valid subarrays ending here.
# Because each earlier prefix sum occurrence = a different valid start.



# ––––––––––––––––––––––––––––––––––––––––––––––––
# Note the image that explains this problem in this section: Count the number of subarrays with an "exact" constraint only applies when the subarray sum matches k.

# If the subarray sum does not match k, no count is incremented, and the logic moves to the next prefix sum check.

# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4512/


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

# counts = {0: 2, 1: 1, 3: 1, 6: 1, 10: 1}


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
# Output: 4 
# (subarrays [3, 4], [7], [7, 2, -3, 1], [1, 4, 2])

# counts =
# {0:1} -> {0:1,3:1} -> {0:1,3:1,7:1} ->
# {0:1,3:1,7:1,14:1} -> {0:1,3:1,7:1,14:1,16:1} ->
# {0:1,3:1,7:1,14:1,16:1,13:1} ->
# {0:1,3:1,7:1,14:1,16:1,13:1,14:2} ->
# {0:1,3:1,7:1,14:1,16:1,13:1,14:2,18:1} ->
# {0:1,3:1,7:1,14:1,16:1,13:1,14:2,18:1,20:1}



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
# Output: 1


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

nums = [1, -1, 1, -1]
k = 0
print(subarraySum(nums, k))
# Output: 4


# The prefix sum is [1, 0, 1, 0]. There are two subarrays ending on the final index - [1, -1] and the entire array. Remember that we initialize counts[0] = 1, so after the second index, we have counts[0] = 2. So when we reach the final index and do ans += counts[curr - k] = ans += counts[0], we are adding both subarrays to our answer. 

# When there are non-positive numbers in the input, the same prefix can occur multiple times, and a hash map is needed to count the frequency.



# ––––––––––––––––––––––––––––––––––––––––––––––––
"""
Q: Why do we set counts[0] = 1 at the start?

counts[0] = 1

Why do we need this?
    • It’s a starting point that says:
      “Before we add any numbers, we already have one way to make a sum of 0.”
    • This makes it possible to count subarrays that start at the very beginning of the array.

---
Example: nums = [1, 2], k = 3
    • Running sum (curr) starts at 0.
    • First number → curr = 1
    • Second number → curr = 3

Now check: curr - k = 3 - 3 = 0
    • If counts[0] wasn’t initialized to 1, the code would miss the subarray [1, 2] because it wouldn’t recognize that the sum from the start equals k.

---
✅ So counts[0] = 1 is like saying:
    • “We’ve seen a zero-sum once already, before starting. That way, if the running total hits k, we know we found a valid subarray starting at index 0.”
    
"""