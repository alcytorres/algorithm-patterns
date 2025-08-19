# Query Subarray Sums with Limit

# Example 1: Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit, return a boolean array that represents the answer to each query. A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.

# Example:
# nums = [1, 6, 3, 2, 7, 2]
# queries = [[0, 3], [2, 5], [2, 4]]
# limit = 13
# Output: [True, False, True]

def answer_queries(nums, queries, limit):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(prefix[-1] + nums[i])

    ans = []
    for x, y in queries:
        curr = prefix[y] - prefix[x] + nums[x]
        ans.append(curr < limit)

    return ans

nums = [1, 6, 3, 2, 7, 2]  # -> [1, 7, 10, 12, 19, 21]
queries = [[0, 3], [2, 5], [2, 4]]
limit = 13
print(answer_queries(nums, queries, limit))
# Output: [True, False, True] --> Sums: [12, 14, 12], compared to limit 13.
# [0, 3] = 12
# [2, 5] = 14
# [2, 4] = 12


# Time: O(n + q)
# - Build prefix sum array: O(n).
# - Answer each query in O(1) using prefix sums, for q queries: O(q).
# - Overall: O(n + q) time.

# Space: O(n + q)
# - Prefix sum array stores n values: O(n) space.
# - Result array 'ans' stores q values: O(q) space.
# - A few variables (i, x, y, curr) take O(1) space.
# - Overall: O(n + q) total space.
# - If we exclude the output array, extra working space is O(n) due to the prefix sum array.


# ––––––––––––––––––––––––––––––––––––––––––––––
# Basic example to show unpacking x, y in a for loop
nums = [[1, 2], [3, 4], [5, 6]]  # List of pairs
for x, y in nums:                # Unpack each pair into x and y
    print(f"x = {x}, y = {y}")   # Print x and y for each pair

# Output:
# x = 1, y = 2
# x = 3, y = 4
# x = 5, y = 6

# Basic example to show unpacking x in a for loop
nums = [[1, 2], [3, 4], [5, 6]]  # List of pairs
for x in nums:                # Unpack each pair into x
    print(f"x = {x}")   # Print x for each pair

# Output:
# x = [1, 2]
# x = [3, 4]
# x = [5, 6]

# List Comprehension: Return List of Pairs
def fn(nums):
    return [[x, y] for x, y in nums]

nums = [[1, 2], [3, 4], [5, 6]] 
print(fn(nums))  # Output: [[1, 2], [3, 4], [5, 6]]

# Iterative: Build List of Pairs
def fn(nums):
    ans = []                   # Initialize empty list to store pairs
    for x, y in nums:          # Iterate through each pair
        ans.append([x, y])     # Append pair as a list
    return ans                 # Return the list of all pairs

nums = [[1, 2], [3, 4], [5, 6]]
print(fn(nums))  # Output: [[1, 2], [3, 4], [5, 6]]



# ––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
def answer_queries(nums, queries, limit):
    prefix = [nums[0]]       # Initialize prefix with first element
    for i in range(1, len(nums)):  # Iterate from index 1
        prefix.append(prefix[-1] + nums[i])  # Add current element to previous sum
    
    ans = []                 # Store results for each query
    for x, y in queries:     # Iterate over each query [x, y]
        curr = prefix[y] - prefix[x] + nums[x]  # Compute subarray sum from x to y
        ans.append(curr < limit)  # Append True if sum < limit, False otherwise
    
    return ans               # Return array of boolean answers



# ––––––––––––––––––––––––––––––––––––––––––––––
# Task: Given an array nums, queries [[x, y]], and limit, return a boolean array where each element is True if the subarray sum from x to y is < limit, False otherwise.
# Example: nums = [1, 6, 3, 2, 7, 2], queries = [[0, 3], [2, 5], [2, 4]], limit = 13 → Output = [True, False, True]
# Why: Practices prefix sum technique to efficiently compute subarray sums.

def answer_queries(nums, queries, limit):  # Example: nums = [1, 6, 3, 2, 7, 2], queries = [[0, 3], [2, 5], [2, 4]], limit = 13

    # 1️⃣ Build prefix sum array
    # Initialize prefix sum with the first element
    # Why? Prefix sums allow efficient calculation of subarray sums
    prefix = [nums[0]]  # prefix = [1]

    # Compute prefix sums for the rest of the array
    # Why? Each prefix[i] stores the sum of nums[0] to nums[i]
    for i in range(1, len(nums)):  # i goes from 1 to 5
        prefix.append(prefix[-1] + nums[i])  # i = 1: prefix[-1] = 1, nums[1] = 6, prefix = [1, 7]
                                             # i = 2: prefix[-1] = 7, nums[2] = 3, prefix = [1, 7, 10]
                                             # i = 3: prefix[-1] = 10, nums[3] = 2, prefix = [1, 7, 10, 12]
                                             # i = 4: prefix[-1] = 12, nums[4] = 7, prefix = [1, 7, 10, 12, 19]
                                             # i = 5: prefix[-1] = 19, nums[5] = 2, prefix = [1, 7, 10, 12, 19, 21]
    # After loop: prefix = [1, 7, 10, 12, 19, 21]

    # 2️⃣ Process queries
    # Initialize answer list to store results
    # Why? We need to store True/False for each query based on subarray sums
    ans = []  # ans = []

    # Iterate through each query [x, y]
    # Why? We compute the subarray sum for each query and compare with limit
    for x, y in queries:  # queries = [[0, 3], [2, 5], [2, 4]]
        # --- Query 1: x = 0, y = 3 ---
        # Compute subarray sum from index x to y using prefix sums
        # Why? prefix[y] - prefix[x] + nums[x] gives sum of nums[x:y+1]
        curr = prefix[y] - prefix[x] + nums[x]  # x = 0, y = 3
                                                # prefix[3] = 12, prefix[0] = 1, nums[0] = 1
                                                # curr = 12 - 1 + 1 = 12
        # Check if subarray sum is less than limit
        # Why? We need to determine if the query satisfies the condition
        ans.append(curr < limit)  # curr = 12, limit = 13, 12 < 13 is True
                                 # ans = [True]
        # After Query 1: ans = [True]
        # Subarray [0, 3]: [1, 6, 3, 2], sum = 12

        # --- Query 2: x = 2, y = 5 ---
        if x == 2 and y == 5:
            curr = prefix[y] - prefix[x] + nums[x]  # x = 2, y = 5
                                                    # prefix[5] = 21, prefix[2] = 10, nums[2] = 3
                                                    # curr = 21 - 10 + 3 = 14
            ans.append(curr < limit)  # curr = 14, limit = 13, 14 < 13 is False
                                     # ans = [True, False]
            # After Query 2: ans = [True, False]
            # Subarray [2, 5]: [3, 2, 7, 2], sum = 14

        # --- Query 3: x = 2, y = 4 ---
        if x == 2 and y == 4:
            curr = prefix[y] - prefix[x] + nums[x]  # x = 2, y = 4
                                                    # prefix[4] = 19, prefix[2] = 10, nums[2] = 3
                                                    # curr = 19 - 10 + 3 = 12
            ans.append(curr < limit)  # curr = 12, limit = 13, 12 < 13 is True
                                     # ans = [True, False, True]
            # After Query 3: ans = [True, False, True]
            # Subarray [2, 4]: [3, 2, 7], sum = 12

    # 3️⃣ Return the boolean array
    # Why? ans contains True/False for each query based on subarray sums
    return ans  # ans = [True, False, True]


nums = [1, 6, 3, 2, 7, 2]
queries = [[0, 3], [2, 5], [2, 4]]
limit = 13
print(answer_queries(nums, queries, limit))  # Output: [True, False, True]



# ––––––––––––––––––––––––––––––––––––––––––––––
# Prefix Sum Query Cheat Sheet

# Problem Overview
# - Input: Array nums, queries [[x, y]], limit
# - Output: Boolean array, True if subarray sum from x to y < limit, else False
# - Example: nums = [1, 6, 3, 2, 7, 2], queries = [[0, 3], [2, 5], [2, 4]], limit = 13 -> [True, False, True]

# Key Code Logic
# 1. Build Prefix Sum:
#    - Initialize: prefix = [nums[0]]
#    - Loop: for i in range(1, len(nums)): prefix.append(prefix[-1] + nums[i])
# 2. Process Queries:
#    - Loop: for x, y in queries
#    - Calculate sum: curr = prefix[y] - prefix[x] + nums[x]
#    - Append result: ans.append(curr < limit)
#
# Code:
def prefix_sum_queries(nums, queries, limit):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(prefix[-1] + nums[i])
    
    ans = []
    for x, y in queries:
        curr = prefix[y] - prefix[x] + nums[x]
        ans.append(curr < limit)
    return ans

# Challenges & Solutions
# - Challenge: Understanding prefix[y] - prefix[x] + nums[x]:
#   - Why: prefix[y] - prefix[x] gives sum from x+1 to y. Add nums[x] to include index x.
#   - Fix: Recognize prefix[x] is sum up to x, so add nums[x] for full range.
# - Challenge: Unpacking queries in loop (for x, y in queries):
#   - Why: Each query is a pair [x, y], unpacking assigns x as start, y as end.
#   - Fix: Understand x, y represent start/end indices of subarray.
# - Challenge: Calculating correct subarray sum:
#   - Why: Using prefix[y] - prefix[x-1] fails when x=0 (invalid index) and requires extra checks.
#   - Fix: Use prefix[y] - prefix[x] + nums[x] for robust sum from x to y, valid for all x.

# Example Walkthrough
"""
# Query [2, 5]:
#   - nums: [1, 6, 3, 2, 7, 2]
#   - Prefix: [1, 7, 10, 12, 19, 21]
#   - curr = prefix[5] - prefix[2] + nums[2] = 21 - 10 + 3 = 14
#   - 14 < 13 -> False
"""