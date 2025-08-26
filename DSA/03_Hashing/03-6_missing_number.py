# 268. Missing Number

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Solution: https://leetcode.com/problems/missing-number/editorial/

def missingNumber(nums):
    num_set = set(nums)
    n = len(nums) + 1

    for num in range(n):
        if num not in num_set:
            return num

l = [3, 0, 1]
print(missingNumber(l))
# Output: 2


# Time: O(n)
# - Creating the set from nums: O(n).
# - Looping through numbers from 0 to n: O(n) iterations.
# - Set lookups ('number not in num_set') are O(1) on average.
# - Overall: O(n) time.

# Space: O(n)
# - Set 'num_set' stores up to n elements: O(n) space.
# - A few variables (n, number) take O(1) space.
# - Overall: O(n) total space.


# Trace Overview
# num_set = {0, 1, 3}
# n       = 4
# num     = 0  1  2  3



# ––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def missingNumber(nums):
    num_set = set(nums)       # Convert array to set for O(1) lookups
    n = len(nums) + 1         # Range of expected numbers (0 to n)
    
    for num in range(n):   # Iterate over numbers 0 to n
        if num not in num_set:  # If number missing from set
            return num         # Return first missing number
        


# ––––––––––––––––––––––––––––––––––––––––––––––––
# Full Breakdown 
# Task: Find the missing number in an array of n distinct numbers in the range [0, n].
# Example: nums = [3, 0, 1] → Output = 2 (2 is missing from the range [0, 3])
# Why: Practices set-based lookup to efficiently identify a missing number.

def missingNumber(nums):  # Example: nums = [3, 0, 1]

    # 1️⃣ Create a set from the input array
    # Convert nums to a set for O(1) lookup
    # Why? Sets allow fast checking of whether a number exists in the array
    num_set = set(nums)  # num_set = {3, 0, 1}

    # 2️⃣ Determine the expected range
    # Calculate n as the length of nums plus 1
    # Why? The range is [0, n], where n is len(nums), so we need n + 1 numbers
    n = len(nums) + 1  # len(nums) = 3, n = 3 + 1 = 4

    # 3️⃣ Iterate through the expected range
    # Check each number in [0, n) to find the missing one
    # Why? Exactly one number in the range is missing, so we check each possibility
    for num in range(n):  # num goes from 0 to 3
        # --- Iteration 1: num = 0 ---
        # Check if the current number is in the set
        # Why? If a number is not in num_set, it is the missing number
        if num not in num_set:  # num = 0, num_set = {3, 0, 1}, 0 in num_set, skip
            return num  # skip
        # After Iteration 1: continue

        # --- Iteration 2: num = 1 ---
        if num == 1:
            if num not in num_set:  # num = 1, num_set = {3, 0, 1}, 1 in num_set, skip
                return num
            # After Iteration 2: continue

        # --- Iteration 3: num = 2 ---
        if num == 2:
            if num not in num_set:  # num = 2, num_set = {3, 0, 1}, 2 not in num_set, true
                return num  # return 2
            # After Iteration 3: return 2 (loop exits)

        # --- Iteration 4: num = 3 ---
        # Not reached due to return in Iteration 3

    # Note: The loop is guaranteed to return a value since one number is missing


l = [3, 0, 1]
print(missingNumber(l))  # Output: 2


