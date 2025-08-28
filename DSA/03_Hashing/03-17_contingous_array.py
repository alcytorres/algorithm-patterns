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


nums = [0, 1, 1, 1, 1, 1, 0, 0, 0]
print(findMaxLength(nums))
# Output: 6


# Time: O(n)
# - Loop through nums once: O(n) iterations.
# - Dictionary lookups ('diff in counts') and updates are O(1) on average.
# - Overall: O(n) time.

# Space: O(n)
# - Dictionary 'counts' can store up to n different diff values in the worst case: O(n).
# - A few variables (diff, max_length, i, num) take O(1) space.
# - Overall: O(n) total space.


# Overview for Each Iteration
# Input: nums = [0, 1, 1, 1, 1, 1, 0, 0, 0]
# Step: Process array to find longest subarray with equal 0s and 1s
# Idx | num | diff | counts[diff] | max_length | counts
# -   | -   | 0    | -1           | 0          | {0:-1}
# 0   | 0   | -1   | absent       | 0          | {0:-1, -1:0}
# 1   | 1   | 0    | -1           | 2 (1 - (-1)) | {0:-1, -1:0}
# 2   | 1   | 1    | absent       | 2          | {0:-1, -1:0, 1:2}
# 3   | 1   | 2    | absent       | 2          | {0:-1, -1:0, 1:2, 2:3}
# 4   | 1   | 3    | absent       | 2          | {0:-1, -1:0, 1:2, 2:3, 3:4}
# 5   | 1   | 4    | absent       | 2          | {0:-1, -1:0, 1:2, 2:3, 3:4, 4:5}
# 6   | 0   | 3    | 4            | 2          | {0:-1, -1:0, 1:2, 2:3, 3:4, 4:5}
# 7   | 0   | 2    | 3            | 4 (7 - 3)  | {0:-1, -1:0, 1:2, 2:3, 3:4, 4:5}
# 8   | 0   | 1    | 2            | 6 (8 - 2)  | {0:-1, -1:0, 1:2, 2:3, 3:4, 4:5}
# Final: 6 ([1,1,1,0,0,0])




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


# Time: O(n^2)
# - Outer loop picks a start index i: O(n).
# - Inner loop extends subarray to j: O(n).
# - Each step updates counts and compares zeros/ones in O(1).
# - Overall: O(n * n) = O(n^2) time.

# Space: O(1)
# - Only a constant number of variables (ans, i, j, zeros, ones) are used.
# - No additional data structures.
# - Overall: O(1) space.


# Trace Overview
# nums = [0,1,1,1,1,1,0,0,0]
# i=0: j=1 → zeros=1, ones=1 → len=2 (ans=2)
# i=1: (no equal-length found; more 1s than 0s ahead)
# i=2: (no equal-length found)
# i=3: j=8 → subarray [1,1,1,0,0,0] → zeros=3, ones=3 → len=6 (ans=6)
# i=4: j=7 → [1,1,0,0] → len=4 (ans stays 6)
# i=5: j=6 → [1,0] → len=2 (ans stays 6)
# i=6..8: only 0s remain → no equal-length updates
# Final ans = 6




# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
from collections import defaultdict

def findMaxLength(nums):
    counts = defaultdict(int)  # Notebook to store difference and index
    counts[0] = -1            # Start with difference 0 at index -1
    diff = 0                  # Running difference (1s count - 0s count)
    max_length = 0            # Longest subarray length

    for i, num in enumerate(nums):
        if num == 1:
            diff += 1         # Add 1 for a 1
        else:
            diff -= 1         # Subtract 1 for a 0
        if diff in counts:    # If we've seen this difference before
            max_length = max(max_length, i - counts[diff])  # Update length
        else:
            counts[diff] = i  # Store new difference with current index

    return max_length



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
