# 3. Check Subarray with Zero Sum
"""
Task: Determine if an array has a subarray summing to zero. Return false otherwise.

Example 1: [1, 3, -4, 5] → True  (1 + 3 + -4 = 0)       → prefix_sums: [1, 4, 0, 5]
Example 2: [1, 3, 5, -4] → False (no chunk sums to 0)   → prefix_sums: [1, 4, 9, 5]
Example 3: [1, 2, -2]    → True  (2 + -2 = 0)           → prefix_sums: [1, 3, 1]
Example 4: [4, -4, 1]    → True  (4 + -4 = 0)           → prefix_sums: [4, 0, 1]

Why: Introduces prefix sum applications beyond simple running sums.
"""

def has_zero_sum_subarray(arr):

    # 1️⃣ Initialize prefix sum and set for tracking
    prefix_sum = 0
    seen = set()

    # 2️⃣ Iterate through the array to compute prefix sums
    for num in arr:
        prefix_sum += num
        if prefix_sum == 0 or prefix_sum in seen:
            return True
        seen.add(prefix_sum)

    # 3️⃣ Return False if no zero-sum subarray is found
    return False




# print(has_zero_sum_subarray([1, 3, -4, 5,])) # Output: True  (1 + 3 + -4 = 0)

# print(has_zero_sum_subarray([1, 3, 5, -4]))  # Output: False (no chunk sums to 0)
print(has_zero_sum_subarray([1, 2, -2, 3]))  # Output: True (2 + -2 = 0)
# print(has_zero_sum_subarray([1, 2, -1, -1]))  # Output: True (2 + -1 -1 = 0)

# print(has_zero_sum_subarray([3, -3, 1]))  # Output: True (3 + -3 = 0)
# print(has_zero_sum_subarray([1, 2, -4]))  # Output: False (no chunk sums to 0)
# print(has_zero_sum_subarray([1, 2, -3]))  # Output: True (1 + 2 + -3 = 0)
