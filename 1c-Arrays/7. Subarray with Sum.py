# Subarray Manipulation: Subarray with Sum
"""
Task: Find a contiguous subarray that sums to a given target (non-negative numbers).
    - Input is a non-empty array of integers with a target

Example 1: [1, 2, 3, 7, 5], target=12 → [2, 3, 7] (sums to 12)

Why: Teaches sliding window technique for subarray problems.
"""


def subarray_with_sum(arr, target):
    # 1️⃣ Initialize window sum and start pointer
    current_sum = arr[0]
    start = 0
    
    # 2️⃣ Slide window to find subarray with target sum
    for end in range(1, len(arr)):
        while current_sum > target and start < end:
            current_sum -= arr[start]  # Shrink window from start
            start += 1
        if current_sum == target:
            return arr[start:end]  # Return subarray if sum matches
        current_sum += arr[end]  # Expand window by adding end element
    
    # 3️⃣ Check final window
    if current_sum == target:
        return arr[start:]
    return None

print(subarray_with_sum([1, 2, 3, 7, 5], 12))  # Output: [2, 3, 7]


# Simple Breakdown
"""
Finds a subarray with a given sum using sliding window.
- Adjusts window size dynamically to match the target sum.
- Time Complexity: O(n), Space Complexity: O(1).
- Introduces sliding window in a clear, practical way.
"""