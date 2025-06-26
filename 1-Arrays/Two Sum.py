# Two Sum

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

# Why: Practices efficient hash map usage for finding pairs with a specific sum.

https://www.youtube.com/watch?v=KLlXCFG5TnA

https://www.youtube.com/watch?v=7jDS9KQEDbI
"""

# Hash Map Solution
def two_sum(nums, target):
   
    prevMap = {}

    for index, num in enumerate(nums): 
        diff = target - num

        if diff in prevMap:
            return [prevMap[diff], index]
        prevMap[num] = index
    
    return 

print(two_sum([4, 3, 4, 2], 8))  # Output: [0, 2]
# print(two_sum([3, 2, 2, 3], 6))  # Output: [0, 3]


# One-Pass Optimal Solution (For Bootcamp)
def two_sum(nums, target):
    h = {}

    for index, num in enumerate(nums):
        diff = target - num

        if diff in h:
            return [index, h[diff]]
        else:
            h[num] = index

# Time Complexity: O(n)
# Space Complexity: O(n)

print(two_sum([4, 3, 4, 2], 8))   # Output: [2, 0]


"""
Flow:
    Starts with h = {}.
    Each loop, enumerate(nums) gives (i, num) (e.g., (0, 4), (1, 3), (2, 4)).
    Checks if diff is in h. If yes, returns [i, h[diff]]. If no, adds num: i to h.
    At i=2, diff=4 is found in h (from h[4]=0), so returns [2, 0].

Final Output: [2, 0] (indices of nums[2]=4 and nums[0]=4, since 4 + 4 = 8).
"""

# ----------------------------------------------------------------------------------
# Task: Find the indices of two numbers in an array that add up to a target sum.
# Assume exactly one solution exists, and the same element cannot be used twice.
# Example: nums = [4, 3, 4, 2], target = 8 → Output = [0, 2] (nums[0] + nums[2] = 4 + 4 = 8)

def two_sum(nums, target):  # Example: nums = [4, 3, 4, 2], target = 8

    # 1️⃣ Initialize hash map
    # Create a dictionary to store number-to-index mappings
    # Why? We need to quickly check if a number's complement (target - num) exists
    prevMap = {}  # prevMap = {}

    # 2️⃣ Iterate through the array
    # Loop through the array with index and value
    # Why? We need both the number and its index to find the pair and return indices
    for i, num in enumerate(nums):  # i, num take values (0, 4), (1, 3), (2, 4), (3, 2)
        # --- Iteration 1: i = 0, num = 4 ---
        # Calculate the complement needed to reach the target
        # Why? We need to find if target - num exists in prevMap
        diff = target - num  # target = 8, num = 4, diff = 8 - 4 = 4

        # Check if the complement exists in the hash map
        # Why? If found, we have a pair that sums to the target
        if diff in prevMap:  # diff = 4, prevMap = {}, 4 not in prevMap, skip
            return [prevMap[diff], i]  # skip
        # Store the current number and its index
        # Why? We need to track numbers we've seen for future complement checks
        prevMap[num] = i  # prevMap = {4: 0}
        # After Iteration 1: prevMap = {4: 0}

        # --- Iteration 2: i = 1, num = 3 ---
        if i == 1:
            diff = target - num  # target = 8, num = 3, diff = 8 - 3 = 5
            if diff in prevMap:  # diff = 5, prevMap = {4: 0}, 5 not in prevMap, skip
                return [prevMap[diff], i]
            prevMap[num] = i  # prevMap = {4: 0, 3: 1}
            # After Iteration 2: prevMap = {4: 0, 3: 1}

        # --- Iteration 3: i = 2, num = 4 ---
        if i == 2:
            diff = target - num  # target = 8, num = 4, diff = 8 - 4 = 4
            if diff in prevMap:  # diff = 4, prevMap = {4: 0, 3: 1}, 4 in prevMap, true
                return [prevMap[diff], i]  # return [prevMap[4], 2] = [0, 2]
            prevMap[num] = i  # skip (return statement executes)
            # After Iteration 3: return [0, 2]

        # --- Iteration 4: i = 3, num = 2 ---
        # Not reached due to return in Iteration 3

    # 3️⃣ Return empty list if no solution is found
    # Why? The problem assumes a solution exists, so this is not reached
    return []  # skip


print(two_sum([4, 3, 4, 2], 8))  # Output: [0, 2]





# ----------------------------------------------------------------------------------
# Task: Find the indices of two numbers in an array that add up to a target sum.
# Assume exactly one solution exists, and the same element cannot be used twice.
# Example: arr = [3, 2, 2, 3], target = 6 → Output = [0, 3] (arr[0] + arr[3] = 3 + 3 = 6)



print(two_sum([3, 2, 2, 3], 6))  # Output: [0, 3]