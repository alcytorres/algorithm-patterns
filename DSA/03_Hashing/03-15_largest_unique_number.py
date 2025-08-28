# 1133. Largest Unique Number

# Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.

# Exampl 1:
    # Input: nums = [1, 3, 9, 4, 9, 8, 3]
    # Output: 8
    # Explanation: The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it is the answer.

# Example 2:
    # Input: nums = [9, 9 ,8, 8]
    # Output: -1
    # Explanation: There is no number that occurs only once.

# Solution: https://leetcode.com/problems/largest-unique-number/solutions/5833698/largest-unique-number/


from collections import defaultdict

def largestUniqueNumber(nums):
    # Step 1: Count occurrences of each number
    counts = defaultdict(int)
    for num in nums:
        counts[num] += 1
    
    # Step 2: Find the largest number with count 1
    max_unique = -1
    for num in counts:
        if counts[num] == 1 and num > max_unique:
            max_unique = num
    
    return max_unique


nums = [1, 3, 9, 4, 9, 8, 3]
print(largestUniqueNumber(nums))
# Output: 8

# counts = {1:1, 3:2, 9:2, 4:1, 8:1}


# Time: O(n)
# - Loop through nums once to count occurrences: O(n).
# - Loop through dictionary keys to find the largest unique number: O(u), where u = number of unique numbers (≤ n).
# - Overall: O(n) time.

# Space: O(n)
# - Dictionary 'counts' can store up to n elements in the worst case (all numbers unique).
# - A few variables (num, max_unique) take O(1) space.
# - Overall: O(n) total space.


# Overview for Each Iteration
# Step 1: Count occurrences
# Idx | num | counts
# -   | -   | {}
# 0   | 1   | {1:1}
# 1   | 3   | {1:1, 3:1}
# 2   | 9   | {1:1, 3:1, 9:1}
# 3   | 4   | {1:1, 3:1, 9:1, 4:1}
# 4   | 9   | {1:1, 3:1, 9:2, 4:1}
# 5   | 8   | {1:1, 3:1, 9:2, 4:1, 8:1}
# 6   | 3   | {1:1, 3:2, 9:2, 4:1, 8:1}

# Step 2: Find largest unique number
# num | counts[num] | max_unique
# -   | -           | -1
# 1   | 1           | 1 (updated)
# 3   | 2           | 1 (skipped)
# 9   | 2           | 1 (skipped)
# 4   | 1           | 4 (updated)
# 8   | 1           | 8 (updated)
# Final: 8



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force 

def largestUniqueNumber(nums):
    max_unique = -1
    
    # Check each number in the array
    for i in range(len(nums)):
        num = nums[i]
        count = 0
        
        # Count how many times num appears in the array
        for j in range(len(nums)):
            if nums[j] == num:
                count += 1
        
        # If num appears exactly once and is larger than max_unique, update
        if count == 1 and num > max_unique:
            max_unique = num
    
    return max_unique

nums = [1, 3, 9, 4, 9, 8, 3]
print(largestUniqueNumber(nums))  
# Output: 8

# Time: O(n^2)
# - Outer loop iterates over all n elements.
# - Inner loop scans the entire array for each element → O(n).
# - Overall: O(n * n) = O(n^2) time.

# Space: O(1)
# - Only a constant number of variables (max_unique, i, j, num, count) are used.
# - No additional data structures.
# - Overall: O(1) space.

# Overview for Each Iteration
# Step 1: Check each number and count occurrences
# i | num | j | nums[j] | count | max_unique
# - | -   | - | -       | -     | -1
# 0 | 1   | 0 | 1       | 1     | -1
#   |     | 1 | 3       | 1     | -1
#   |     | 2 | 9       | 1     | -1
#   |     | 3 | 4       | 1     | -1
#   |     | 4 | 9       | 1     | -1
#   |     | 5 | 8       | 1     | -1
#   |     | 6 | 3       | 1     | -1
#   |     | End: count=1, num=1 > -1 | 1 (updated)
# 1 | 3   | 0 | 1       | 0     | 1
#   |     | 1 | 3       | 1     | 1
#   |     | 2 | 9       | 1     | 1
#   |     | 3 | 4       | 1     | 1
#   |     | 4 | 9       | 1     | 1
#   |     | 5 | 8       | 1     | 1
#   |     | 6 | 3       | 2     | 1
#   |     | End: count=2, skip | 1
# 2 | 9   | 0 | 1       | 0     | 1
#   |     | 1 | 3       | 0     | 1
#   |     | 2 | 9       | 1     | 1
#   |     | 3 | 4       | 1     | 1
#   |     | 4 | 9       | 2     | 1
#   |     | 5 | 8       | 2     | 1
#   |     | 6 | 3       | 2     | 1
#   |     | End: count=2, skip | 1
# 3 | 4   | 0 | 1       | 0     | 1
#   |     | 1 | 3       | 0     | 1
#   |     | 2 | 9       | 0     | 1
#   |     | 3 | 4       | 1     | 1
#   |     | 4 | 9       | 1     | 1
#   |     | 5 | 8       | 1     | 1
#   |     | 6 | 3       | 1     | 1
#   |     | End: count=1, num=4 > 1 | 4 (updated)
# 4 | 9   | 0 | 1       | 0     | 4
#   |     | 1 | 3       | 0     | 4
#   |     | 2 | 9       | 1     | 4
#   |     | 3 | 4       | 1     | 4
#   |     | 4 | 9       | 2     | 4
#   |     | 5 | 8       | 2     | 4
#   |     | 6 | 3       | 2     | 4
#   |     | End: count=2, skip | 4
# 5 | 8   | 0 | 1       | 0     | 4
#   |     | 1 | 3       | 0     | 4
#   |     | 2 | 9       | 0     | 4
#   |     | 3 | 4       | 0     | 4
#   |     | 4 | 9       | 0     | 4
#   |     | 5 | 8       | 1     | 4
#   |     | 6 | 3       | 1     | 4
#   |     | End: count=1, num=8 > 4 | 8 (updated)
# 6 | 3   | 0 | 1       | 0     | 8
#   |     | 1 | 3       | 1     | 8
#   |     | 2 | 9       | 1     | 8
#   |     | 3 | 4       | 1     | 8
#   |     | 4 | 9       | 1     | 8
#   |     | 5 | 8       | 1     | 8
#   |     | 6 | 3       | 2     | 8
#   |     | End: count=2, skip | 8
# Final: 8


# –––––––––––––––––––––––––––––––––––––––––––––––––
# Simple Breakdown 
from collections import defaultdict

def largestUniqueNumber(nums):
    counts = defaultdict(int)  # Notebook to count how many times each number appears
    for num in nums:          # Go through each number in the list
        counts[num] += 1      # Add 1 to the count of this number in the notebook
    
    max_unique = -1           # Start with -1 (return this if no number appears once)
    for num in counts:        # Check each number in the notebook
        if counts[num] == 1 and num > max_unique:  # If number appears once and is bigger
            max_unique = num  # Update to this bigger number
    
    return max_unique         # Return the biggest number that appears once




# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Task: Find the largest integer that occurs only once in an array; return -1 if none exists.
# Example: nums = [1, 3, 9, 4, 9, 8, 3] → Output = 8 (8 occurs once, largest non-repeated number)
# Why: Practices hash map usage to count occurrences and find the maximum unique number.

from collections import defaultdict

def largestUniqueNumber(nums):  # Example: nums = [1, 3, 9, 4, 9, 8, 3]

    # 1️⃣ Count occurrences of each number
    # Initialize a defaultdict to store number counts
    # Why? We need to track how many times each number appears
    counts = defaultdict(int)  # counts = {}

    # Iterate through the array to count each number
    # Why? We need to build a frequency map for all numbers
    for num in nums:  # num takes values [1, 3, 9, 4, 9, 8, 3]
        # --- Iteration 1: num = 1 ---
        counts[num] += 1  # counts[1] = 0 + 1 = 1
        # After Iteration 1: counts = {1: 1}

        # --- Iteration 2: num = 3 ---
        if num == 3 and counts[3] == 0:
            counts[num] += 1  # counts[3] = 0 + 1 = 1
            # After Iteration 2: counts = {1: 1, 3: 1}

        # --- Iteration 3: num = 9 ---
        if num == 9 and counts[9] == 0:
            counts[num] += 1  # counts[9] = 0 + 1 = 1
            # After Iteration 3: counts = {1: 1, 3: 1, 9: 1}

        # --- Iteration 4: num = 4 ---
        if num == 4:
            counts[num] += 1  # counts[4] = 0 + 1 = 1
            # After Iteration 4: counts = {1: 1, 3: 1, 9: 1, 4: 1}

        # --- Iteration 5: num = 9 ---
        if num == 9 and counts[9] == 1:
            counts[num] += 1  # counts[9] = 1 + 1 = 2
            # After Iteration 5: counts = {1: 1, 3: 1, 9: 2, 4: 1}

        # --- Iteration 6: num = 8 ---
        if num == 8:
            counts[num] += 1  # counts[8] = 0 + 1 = 1
            # After Iteration 6: counts = {1: 1, 3: 1, 9: 2, 4: 1, 8: 1}

        # --- Iteration 7: num = 3 ---
        if num == 3 and counts[3] == 1:
            counts[num] += 1  # counts[3] = 1 + 1 = 2
            # After Iteration 7: counts = {1: 1, 3: 2, 9: 2, 4: 1, 8: 1}

    # 2️⃣ Find the largest number with count 1
    # Initialize max_unique to -1
    # Why? We return -1 if no number occurs exactly once
    max_unique = -1  # max_unique = -1

    # Iterate through the numbers in counts
    # Why? We need to find the largest number with a count of 1
    for num in counts:  # num takes values [1, 3, 9, 4, 8] (order may vary due to defaultdict)
        # --- Key = 1 ---
        if counts[num] == 1 and num > max_unique:  # counts[1] = 1, 1 > -1, True
            max_unique = num  # max_unique = 1
        # After num = 1: max_unique = 1

        # --- Key = 3 ---
        if num == 3:
            if counts[num] == 1 and num > max_unique:  # counts[3] = 2, skip
                max_unique = num
        # After num = 3: max_unique = 1

        # --- Key = 9 ---
        if num == 9:
            if counts[num] == 1 and num > max_unique:  # counts[9] = 2, skip
                max_unique = num
        # After num = 9: max_unique = 1

        # --- Key = 4 ---
        if num == 4:
            if counts[num] == 1 and num > max_unique:  # counts[4] = 1, 4 > 1, True
                max_unique = num  # max_unique = 4
        # After num = 4: max_unique = 4

        # --- Key = 8 ---
        if num == 8:
            if counts[num] == 1 and num > max_unique:  # counts[8] = 1, 8 > 4, True
                max_unique = num  # max_unique = 8
        # After num = 8: max_unique = 8

    # 3️⃣ Return the largest unique number
    # Why? max_unique is the largest number that appears exactly once, or -1 if none exists
    return max_unique  # max_unique = 8


nums = [1, 3, 9, 4, 9, 8, 3]
print(largestUniqueNumber(nums))  
# Output: 8





# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Alternative Solution

from collections import Counter

def largestUniqueNumber(nums):
    # Use Counter to count frequencies of numbers
    frequency_map = Counter(nums)

    # Find the largest number with frequency 1, or -1 if none found
    return max(
        (num for num, freq in frequency_map.items() if freq == 1),
        default=-1,
    )

nums = [3, 9, 4, 9, 8, 3]
print(largestUniqueNumber(nums))
# Output: 8
