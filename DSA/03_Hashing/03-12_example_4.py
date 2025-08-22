# 560. Subarray Sum Equals K

# Example 4: 

# Given an integer array nums and an integer k, find the number of subarrays whose sum is equal to k.

# Example 1:
# Input: nums = [1, 1, 1], k = 2
# Output: 2

# Example 2:
# Input: nums = [1, 2, 3], k = 3
# Output: 2

# Solution: https://leetcode.com/problems/subarray-sum-equals-k/solutions/127728/subarray-sum-equals-k/


# ––––––––––––––––––––––––––––––––––––––––––––––––
# Brute Force 

def subarraySum(nums, k):
    ans = 0
    # Check every possible subarray
    for i in range(len(nums)):
        curr_sum = 0
        # Compute sum of subarray from i to j
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            # If sum equals k, increment count
            if curr_sum == k:
                ans += 1
    return ans

numbers = [1, 2, 3]
print(subarraySum(numbers, 3)) 
# Output: 2 (subarrays [1, 2] and [3])

# counts = {0: 1, 1: 1, 3: 1, 6: 1}

# Time: O(n^2)
# - Outer loop runs n times.
# - Inner loop runs up to n times for each outer loop, computing subarray sums.
# - Overall: O(n^2) time.

# Space: O(1)
# - Only a constant number of variables (ans, curr_sum, i, j) are used.
# - No additional data structures.
# - Overall: O(1) space.


# Trace Overview
# i        = 0 -  - -  1 - -  2 -
# j        = 0 -  1 2  1 - 2  2 -
# curr_sum = 0 1  3 6  0 2 5  0 3
# ans      = 0 0  1 1  1 1 1  1 2


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
print(subarraySum(nums, 3))
# Output: 2 (subarrays [1, 2] and [3])

# counts = {0: 1, 1: 1, 3: 1, 6: 1}

# Time: O(n)
# - Loop through nums once: O(n) iterations.
# - Dictionary lookups and updates ('counts[curr - k]', 'counts[curr] += 1') are O(1) on average.
# - No nested loops, so total time is O(n).

# Space: O(n)
# - Dictionary 'counts' can store up to n different prefix sums in the worst case: O(n) space.
# - A few variables (curr, ans, num) take O(1) space.
# - Overall: O(n) total space.


# Trace Overview
# Index = -  0  1  2
# num   = -  1  2  3
# curr  = 0  1  3  6
# ans   = 0  0  1  2
# counts = {0:1} {0:1, 1:1} {0:1, 1:1, 3:1} {0:1, 1:1, 3:1, 6:1}


# ––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
from collections import defaultdict

def subarraySum(nums, k):
    counts = defaultdict(int)  # Track frequency of prefix sums
    counts[0] = 1             # Initialize for subarrays starting at index 0
    ans = curr = 0            # Initialize result and running sum
    for num in nums:          # Iterate over each number
        curr += num           # Update running sum
        ans += counts[curr - k]  # Add count of prefix sums that form sum k
        counts[curr] += 1     # Increment frequency of current sum
    return ans                # Return total subarrays with sum k



# ––––––––––––––––––––––––––––––––––––––––––––––––
# 560. Subarray Sum Equals K
# Goal: Count subarrays in nums that sum to k using prefix sums and a hash map.

from collections import defaultdict

def subarraySum(nums, k):
    counts = defaultdict(int)  # Tracks frequency of prefix sums
    counts[0] = 1             # Empty subarray sum = 0
    ans = curr = 0            # ans: counts subarrays, curr: running sum
    for num in nums:
        curr += num           # Add current number to running sum
        ans += counts[curr - k]  # Count subarrays where sum = k
        counts[curr] += 1     # Record this sum
    return ans

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

nums = [1, 2, 3]
k = 3
print(subarraySum(nums, k))  
# Output: 2 (subarrays [1, 2] and [3])

# counts = {0: 1, 1: 1, 3: 1, 6: 1}

# Time: O(n) - Single pass through nums, O(1) hash map operations.
# Space: O(n) - counts stores up to n prefix sums.



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
print(subarraySum(numbers, 3))  
# Output: 2 (subarrays [1, 2] and [3])

# counts = {0: 1, 1: 1, 3: 1, 6: 1}



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

numbers = [1, 2, 1, 2, 1]
print(subarraySum(numbers, 3))
# Output: 4


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
print(subarraySum(numbers, 3))  
# Output: 4




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
print(subarraySum(nums, 6))
# Output: 2 (subarrays [1, 2, 3] and [6])

# counts = {0: 1, 1: 1, 3: 1, 6: 1, 10: 1, 16: 1}