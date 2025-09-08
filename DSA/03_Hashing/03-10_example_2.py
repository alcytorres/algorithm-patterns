# 2248. Intersection of Multiple Arrays

# Example 2: Given a 2D array nums that contains n arrays of distinct integers, return a sorted array containing all the numbers that appear in all n arrays.

# For example, given nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]], return [3, 4]. 3 and 4 are the only numbers that are in all arrays.

# Example:
    # Input: nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
    # Output: [3, 4]
    # Explanation: The only integers present in each of:
        # nums[0] = [3, 1, 2, 4, 5], 
        # nums[1] = [1, 2, 3, 4], and 
        # nums[2] = [3, 4, 5, 6] 
        # are 3 and 4, so we return [3, 4].

# Solution: https://leetcode.com/problems/intersection-of-multiple-arrays/solutions/


# Import defaultdict for counting element occurrences
from collections import defaultdict

def intersection(nums):
    counts = defaultdict(int)
    
    # Count occurrences of each element in all arrays
    for arr in nums:
        for x in arr:
            counts[x] += 1

    # Get number of arrays
    n = len(nums)
    # Initialize result list for common elements
    ans = []
    
    # Collect elements appearing in all arrays (count equals number of arrays)
    for key in counts:
        if counts[key] == n:
            ans.append(key)
    
    # Return sorted list of common elements
    return sorted(ans)

nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
print(intersection(nums))  
# Output: [3, 4]


# Time: O(n * m)
# - Iterate through each of the m arrays in nums: O(m).
# - Each array may contain up to n elements, so filling the counts dictionary is O(n * m).
# - Final loop over all unique keys (up to n * m elements in worst case) is also O(n * m) in worst case.
# - Sorting the result list takes O(r log r), where r is the number of common elements (r ≤ n).
# - Overall: O(n * m + r log r) time.

# Space: O(n)
# - Dictionary 'counts' stores all unique elements across all arrays: O(n * m) in worst case but typically much less if values overlap.
# - Result list 'ans' stores up to n elements: O(n) space.
# - A few variables (key, arr, x) take O(1) space.
# - Overall: O(n) total space assuming n is the total number of unique values.



# Overview for Each Iteration
# Input: nums = [[3,1,2,4,5], [1,2,3,4], [3,4,5,6]]
# Step 1: Count occurrences of each element across all arrays
# arr_idx | arr         | x | counts
# -       | -           | - | {}
# 0       | [3,1,2,4,5] | 3 | {3: 1}
# 0       | [3,1,2,4,5] | 1 | {3: 1, 1: 1}
# 0       | [3,1,2,4,5] | 2 | {3: 1, 1: 1, 2: 1}
# 0       | [3,1,2,4,5] | 4 | {3: 1, 1: 1, 2: 1, 4: 1}
# 0       | [3,1,2,4,5] | 5 | {3: 1, 1: 1, 2: 1, 4: 1, 5: 1}
# 1       | [1,2,3,4]   | 1 | {3: 1, 1: 2, 2: 1, 4: 1, 5: 1}
# 1       | [1,2,3,4]   | 2 | {3: 1, 1: 2, 2: 2, 4: 1, 5: 1}
# 1       | [1,2,3,4]   | 3 | {3: 2, 1: 2, 2: 2, 4: 1, 5: 1}
# 1       | [1,2,3,4]   | 4 | {3: 2, 1: 2, 2: 2, 4: 2, 5: 1}
# 2       | [3,4,5,6]   | 3 | {3: 3, 1: 2, 2: 2, 4: 2, 5: 1}
# 2       | [3,4,5,6]   | 4 | {3: 3, 1: 2, 2: 2, 4: 3, 5: 1}
# 2       | [3,4,5,6]   | 5 | {3: 3, 1: 2, 2: 2, 4: 3, 5: 2}
# 2       | [3,4,5,6]   | 6 | {3: 3, 1: 2, 2: 2, 4: 3, 5: 2, 6: 1}

# Final counts after processing all arrays: 
# {3:3, 1:2, 2:2, 4:3, 5:2, 6:1}


# Step 2: Collect elements appearing in all arrays (count == n = 3)
# key | counts[key] | counts[key] == n | ans
# 1   | 2           | False            | []
# 2   | 2           | False            | []
# 3   | 3           | True             | [3]
# 4   | 3           | True             | [3, 4]
# 5   | 2           | False            | [3, 4]
# 6   | 1           | False            | [3, 4]
# Final: sorted([3, 4]) = [3, 4]





# ––––––––––––––––––––––––––––––––––––––––––––––––
# Simple Breakdown 
def intersection(nums):
    counts = defaultdict(int)  # Initialize dictionary for element frequencies
    for arr in nums:          # Iterate over each subarray
        for x in arr:         # Iterate over each element in subarray
            counts[x] += 1    # Increment count for current element
    n = len(nums)             # Number of subarrays
    ans = []                  # Initialize result list

    for key in counts:        # Iterate over unique elements
        if counts[key] == n:  # If element appears in all subarrays
            ans.append(key)   # Add element to result

    return sorted(ans)        # Return sorted list of common elements



# ––––––––––––––––––––––––––––––––––––––––––––––––
# Task: Given a 2D array of distinct integers, return a sorted array of numbers that appear in all arrays.
# Example: nums = [[3,1,2,4,5], [1,2,3,4], [3,4,5,6]] → Output = [3, 4] (3 and 4 appear in all arrays)
# Why: Practices hash map usage to count occurrences across multiple arrays.

from collections import defaultdict

def intersection(nums):  # Example: nums = [[3,1,2,4,5], [1,2,3,4], [3,4,5,6]]

    # 1️⃣ Count occurrences of each number
    # Initialize a defaultdict to store number counts across all arrays
    # Why? We need to track how many arrays each number appears in
    counts = defaultdict(int)  # counts = {}

    # Iterate through each array and its elements
    # Why? We count each number's occurrences across all arrays
    for arr in nums:  # arr takes values [[3,1,2,4,5], [1,2,3,4], [3,4,5,6]]
        # --- Iteration 1: arr = [3,1,2,4,5] ---
        for x in arr:  # x takes values [3, 1, 2, 4, 5]
            counts[x] += 1  # counts[3] = 1, counts[1] = 1, counts[2] = 1, counts[4] = 1, counts[5] = 1
        # After Iteration 1: counts = {3: 1, 1: 1, 2: 1, 4: 1, 5: 1}

        # --- Iteration 2: arr = [1,2,3,4] ---
        if arr == [1, 2, 3, 4]:
            for x in arr:  # x takes values [1, 2, 3, 4]
                counts[x] += 1  # counts[1] = 2, counts[2] = 2, counts[3] = 2, counts[4] = 2
            # After Iteration 2: counts = {3: 2, 1: 2, 2: 2, 4: 2, 5: 1}

        # --- Iteration 3: arr = [3,4,5,6] ---
        if arr == [3, 4, 5, 6]:
            for x in arr:  # x takes values [3, 4, 5, 6]
                counts[x] += 1  # counts[3] = 3, counts[4] = 3, counts[5] = 2, counts[6] = 1
            # After Iteration 3: counts = {3: 3, 1: 2, 2: 2, 4: 3, 5: 2, 6: 1}

    # 2️⃣ Identify numbers in all arrays
    # Get the number of arrays
    # Why? We need numbers that appear in all n arrays
    n = len(nums)  # n = 3

    # Initialize result list for numbers appearing in all arrays
    # Why? We collect numbers with count equal to n
    ans = []  # ans = []

    # Check each number in counts
    # Why? Numbers with count == n appear in all arrays
    for key in counts:  # key takes values [3, 1, 2, 4, 5, 6]
        if counts[key] == n:  # n = 3
            # --- Key = 3 ---
            if key == 3 and counts[key] == 3:  # counts[3] = 3, 3 == 3, True
                ans.append(key)  # ans = [3]
            # --- Key = 1 ---
            if key == 1 and counts[key] == 3:  # counts[1] = 2, 2 == 3, False, skip
                ans.append(key)
            # --- Key = 2 ---
            if key == 2 and counts[key] == 3:  # counts[2] = 2, 2 == 3, False, skip
                ans.append(key)
            # --- Key = 4 ---
            if key == 4 and counts[key] == 3:  # counts[4] = 3, 3 == 3, True
                ans.append(key)  # ans = [3, 4]
            # --- Key = 5 ---
            if key == 5 and counts[key] == 3:  # counts[5] = 2, 2 == 3, False, skip
                ans.append(key)
            # --- Key = 6 ---
            if key == 6 and counts[key] == 3:  # counts[6] = 1, 1 == 3, False, skip
                ans.append(key)
    # After loop: ans = [3, 4]

    # 3️⃣ Return sorted result
    # Sort the result list
    # Why? The problem requires the output to be sorted
    return sorted(ans)  # sorted([3, 4]) = [3, 4]


nums = [[3,1,2,4,5], [1,2,3,4], [3,4,5,6]]
print(intersection(nums))  
# Output: [3, 4]