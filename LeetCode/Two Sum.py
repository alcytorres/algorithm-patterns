# Two Sum

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

# Why: Practices efficient hash map usage for finding pairs with a specific sum.

https://www.youtube.com/watch?v=KLlXCFG5TnA

https://www.youtube.com/watch?v=7jDS9KQEDbI
"""

# Brute force Solution
def two_sum(nums, target):
    n = len(nums)   
    for i in range(n):
        for j in range(n):
            if i != j:
                curr_sum = nums[i] + nums[j]
                if curr_sum == target:
                    return [i, j]
    
    # Time: O(n^2)
    # Space: O(1)


# Hash Map One-Pass Optimal Solution
def two_sum(nums, target):
    h = {}

    for index, num in enumerate(nums): 
        diff = target - num

        if diff in h:
            return [h[diff], index]
        h[num] = index
    
    # Time: O(n)
    # Space: O(n)

print(two_sum([4, 3, 4, 2], 8))  # Output: [0, 2]
# print(two_sum([3, 2, 2, 3], 6))  # Output: [0, 3]


# Pseudocode
# FUNCTION two_sum(nums, target)
#     // Step 1: Create an empty hash map to store number-to-index pairs
#     INITIALIZE hash_map as empty dictionary

#     // Step 2: Loop through the array with index and number
#     FOR EACH index, number IN ENUMERATE(nums)
#         // Step 3: Calculate the complement needed to reach target
#         SET complement = target - number

#         // Step 4: Check if complement exists in hash map
#         IF complement EXISTS IN hash_map
#             // Found a pair: return indices of complement and current number
#             RETURN [hash_map[complement], index]

#         // Step 5: Store current number and its index in hash map
#         SET hash_map[number] = index


"""
Flow:
    Starts with h = {}.
    Each loop, enumerate(nums) gives (i, num) (e.g., (0, 4), (1, 3), (2, 4)).
    Checks if diff is in h. If yes, returns [h[diff], index]. If no, adds num: i to h.
    At index=2, diff=4 is found in h (from h[4]=0), so returns [0, 2].

Final Output: [0, 2] (indices of nums[0]=4 and nums[2]=4, since 4 + 4 = 8).
"""



# ----------------------------------------------------------------------------------
# Task: Find the indices of two numbers in an array that add up to a target sum.
# Assume exactly one solution exists, and the same element cannot be used twice.
# Example: nums = [4, 3, 4, 2], target = 8 → Output = [0, 2] (nums[0] + nums[2] = 4 + 4 = 8)

def two_sum(nums, target):  # Example: nums = [4, 3, 4, 2], target = 8

    # 1️⃣ Initialize hash map
    # Create a dictionary to store number-to-index mappings
    # Why? We need to quickly check if a number's complement (target - num) exists
    h = {}  # h = {}

    # 2️⃣ Iterate through the array
    # Loop through the array with index and value
    # Why? We need both the number and its index to find the pair and return indices
    for index, num in enumerate(nums):  # index, num take values (0, 4), (1, 3), (2, 4), (3, 2)
        # --- Iteration 1: index = 0, num = 4 ---
        # Calculate the complement needed to reach the target
        # Why? We need to find if target - num exists in the hash map
        diff = target - num  # target = 8, num = 4, diff = 8 - 4 = 4

        # Check if the complement exists in the hash map
        # Why? If found, we have a pair that sums to the target
        if diff in h:  # diff = 4, h = {}, 4 not in h, skip
            return [h[diff], index]  # skip
        # Store the current number and its index
        # Why? We need to track numbers we've seen for future complement checks
        h[num] = index  # h = {4: 0}
        # After Iteration 1: h = {4: 0}

        # --- Iteration 2: index = 1, num = 3 ---
        if index == 1:
            diff = target - num  # target = 8, num = 3, diff = 8 - 3 = 5
            if diff in h:  # diff = 5, h = {4: 0}, 5 not in h, skip
                return [h[diff], index]
            h[num] = index  # h = {4: 0, 3: 1}
            # After Iteration 2: h = {4: 0, 3: 1}

        # --- Iteration 3: index = 2, num = 4 ---
        if index == 2:
            diff = target - num  # target = 8, num = 4, diff = 8 - 4 = 4
            if diff in h:  # diff = 4, h = {4: 0, 3: 1}, 4 in h, true
                return [h[diff], index]  # return [h[4], 2] = [0, 2]
            h[num] = index  # skip (return statement executes)
            # After Iteration 3: return [0, 2]

        # --- Iteration 4: index = 3, num = 2 ---
        # Not reached due to return in Iteration 3


print(two_sum([4, 3, 4, 2], 8))  # Output: [0, 2]



# ----------------------------------------------------------------------------------
# Task: Find the indices of two numbers in an array that add up to a target sum.
# Assume exactly one solution exists, and the same element cannot be used twice.
# Example: arr = [3, 2, 2, 3], target = 6 → Output = [0, 3] (arr[0] + arr[3] = 3 + 3 = 6)



print(two_sum([3, 2, 2, 3], 6))  # Output: [0, 3]