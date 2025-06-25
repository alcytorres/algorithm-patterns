# Two Sum

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

# Hash Map Solution
def two_sum(arr, target):
   
    prevMap = {}

    for i, n in enumerate(arr):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    
    return 


# Use this as the example
print(two_sum([4, 3, 4, 2], 8)) 

# print(two_sum([3, 2, 2, 3], 6))  # Output: [0, 3]



# Sorting Solution 





# Task: Find the indices of two numbers in an array that add up to a target sum.
# Assume exactly one solution exists, and the same element cannot be used twice.
# Example: arr = [4, 3, 4, 2], target = 8 → Output = [0, 2] (arr[0] + arr[2] = 4 + 4 = 8)
# Why: Practices efficient hash map usage for finding pairs with a specific sum.

def two_sum(arr, target):  # Example: arr = [4, 3, 4, 2], target = 8

    # 1️⃣ Initialize hash map
    # Create a dictionary to store number-to-index mappings
    # Why? We need to quickly check if a number's complement (target - n) exists
    prevMap = {}  # prevMap = {}

    # 2️⃣ Iterate through the array
    # Loop through the array with index and value
    # Why? We need both the number and its index to find the pair and return indices
    for i, n in enumerate(arr):  # i, n take values (0, 4), (1, 3), (2, 4), (3, 2)
        # --- Iteration 1: i = 0, n = 4 ---
        # Calculate the complement needed to reach the target
        # Why? We need to find if target - n exists in prevMap
        diff = target - n  # target = 8, n = 4, diff = 8 - 4 = 4

        # Check if the complement exists in the hash map
        # Why? If found, we have a pair that sums to the target
        if diff in prevMap:  # diff = 4, prevMap = {}, 4 not in prevMap, skip
            return [prevMap[diff], i]  # skip
        # Store the current number and its index
        # Why? We need to track numbers we've seen for future complement checks
        prevMap[n] = i  # prevMap = {4: 0}
        # After Iteration 1: prevMap = {4: 0}

        # --- Iteration 2: i = 1, n = 3 ---
        if i == 1:
            diff = target - n  # target = 8, n = 3, diff = 8 - 3 = 5
            if diff in prevMap:  # diff = 5, prevMap = {4: 0}, 5 not in prevMap, skip
                return [prevMap[diff], i]
            prevMap[n] = i  # prevMap = {4: 0, 3: 1}
            # After Iteration 2: prevMap = {4: 0, 3: 1}

        # --- Iteration 3: i = 2, n = 4 ---
        if i == 2:
            diff = target - n  # target = 8, n = 4, diff = 8 - 4 = 4
            if diff in prevMap:  # diff = 4, prevMap = {4: 0, 3: 1}, 4 in prevMap, true
                return [prevMap[diff], i]  # return [prevMap[4], 2] = [0, 2]
            prevMap[n] = i  # skip (return statement executes)
            # After Iteration 3: return [0, 2]

        # --- Iteration 4: i = 3, n = 2 ---
        # Not reached due to return in Iteration 3

    # 3️⃣ Return empty list if no solution is found
    # Why? The problem assumes a solution exists, so this is not reached
    return []  # skip


print(two_sum([4, 3, 4, 2], 8))  # Output: [0, 2]





# ----------------------------------------------------------------------------------



# Task: Find the indices of two numbers in an array that add up to a target sum.
# Assume exactly one solution exists, and the same element cannot be used twice.
# Example: arr = [3, 2, 2, 3], target = 6 → Output = [0, 3] (arr[0] + arr[3] = 3 + 3 = 6)


def two_sum(arr, target):  # Example: arr = [3, 2, 2, 3], target = 6

    # 1️⃣ Initialize hash map
    # Create a dictionary to store number-to-index mappings
    # Why? We need to quickly check if a number's complement (target - n) exists
    prevMap = {}  # prevMap = {}

    # 2️⃣ Iterate through the array
    # Loop through the array with index and value
    # Why? We need both the number and its index to find the pair and return indices
    for i, n in enumerate(arr):  # i, n take values (0, 3), (1, 2), (2, 2), (3, 3)
        # --- Iteration 1: i = 0, n = 3 ---
        # Calculate the complement needed to reach the target
        # Why? We need to find if target - n exists in prevMap
        diff = target - n  # target = 6, n = 3, diff = 6 - 3 = 3

        # Check if the complement exists in the hash map
        # Why? If found, we have a pair that sums to the target
        if diff in prevMap:  # diff = 3, prevMap = {}, 3 not in prevMap, skip
            return [prevMap[diff], i]  # skip
        # Store the current number and its index
        # Why? We need to track numbers we've seen for future complement checks
        prevMap[n] = i  # prevMap = {3: 0}
        # After Iteration 1: prevMap = {3: 0}

        # --- Iteration 2: i = 1, n = 2 ---
        if i == 1:
            diff = target - n  # target = 6, n = 2, diff = 6 - 2 = 4
            if diff in prevMap:  # diff = 4, prevMap = {3: 0}, 4 not in prevMap, skip
                return [prevMap[diff], i]
            prevMap[n] = i  # prevMap = {3: 0, 2: 1}
            # After Iteration 2: prevMap = {3: 0, 2: 1}

        # --- Iteration 3: i = 2, n = 2 ---
        if i == 2:
            diff = target - n  # target = 6, n = 2, diff = 6 - 2 = 4
            if diff in prevMap:  # diff = 4, prevMap = {3: 0, 2: 1}, 4 not in prevMap, skip
                return [prevMap[diff], i]
            prevMap[n] = i  # prevMap = {3: 0, 2: 2} (update index for 2)
            # After Iteration 3: prevMap = {3: 0, 2: 2}

        # --- Iteration 4: i = 3, n = 3 ---
        if i == 3:
            diff = target - n  # target = 6, n = 3, diff = 6 - 3 = 3
            if diff in prevMap:  # diff = 3, prevMap = {3: 0, 2: 2}, 3 in prevMap, true
                return [prevMap[diff], i]  # return [prevMap[3], 3] = [0, 3]
            prevMap[n] = i  # skip (return statement executes)
            # After Iteration 4: return [0, 3]

    # 3️⃣ Return empty list if no solution is found
    # Why? The problem assumes a solution exists, so this is not reached
    return []  # skip


print(two_sum([3, 2, 2, 3], 6))  # Output: [0, 3]