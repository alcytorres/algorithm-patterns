# ----------------------------------------------------------------------------------
# 1. Compute Prefix Sum Array
"""
Task: Given an array, create a new array of its prefix sums. Return an empty array if input is empty
Example: [1, 2, 3] → [1, 3, 6]
Why: Direct practice for Running Sum of 1d Array.
"""

def prefix_sum(arr):
    if not arr:
        return []
    result = [arr[0]]
    for i in range(1, len(arr)):
        result.append(result[-1] + arr[i])
    return result


# print(prefix_sum([1, 2, 3]))     # Output: [1, 3, 6]  → [1, 1+2, 1+2+3]
# print(prefix_sum([1, 2, 3, 4]))  # Output: [1, 3, 6, 10]  → [1, 1+2, 1+2+3 + 1+2+3+4]


# ----------------------------------------------------------------------------------
# 3. Check Subarray with Zero Sum
"""
Task: Determine if an array has a subarray summing to zero. Return false otherwise.
Example: [4, -4, 1] → True
Why: Introduces prefix sum applications beyond simple running sums.
"""

def has_zero_sum_subarray(arr):
    prefix_sum = 0
    seen = set()
    for num in arr:
        prefix_sum += num
        if prefix_sum == 0 or prefix_sum in seen:
            return True
        seen.add(prefix_sum)
    return False


print(has_zero_sum_subarray([4, -4, 1]))  # Output: True (4 + -4 = 0)
print(has_zero_sum_subarray([1, 2, -4]))  # Output: False (no chunk sums to 0)
print(has_zero_sum_subarray([1, 2, -3]))  # Output: True (1 + 2 + -3 = 0)

