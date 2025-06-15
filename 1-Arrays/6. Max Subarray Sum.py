"""
Subarray Manipulation
Task: Find the maximum sum of a contiguous subarray.

Example 1: [-2, 1, -3, 4, -1, 2, 1, -5, 4] → 6 (from [4, -1, 2, 1])
Example 2: [1] → 1

Why: Introduces Kadane’s algorithm for efficient subarray sum calculation.
"""

def max_subarray_sum(arr):
    # 1️⃣ Handle edge case: empty array
    if not arr:
        return 0
    
    # 2️⃣ Initialize current and global max sums with first element
    max_current = max_global = arr[0]
    
    # 3️⃣ Iterate through array, applying Kadane’s algorithm
    for num in arr[1:]:
        max_current = max(num, max_current + num)  # Choose between starting new or extending
        if max_current > max_global:
            max_global = max_current  # Update global max if current is larger
    
    # 4️⃣ Return the maximum subarray sum
    return max_global

# Test the function
print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6
print(max_subarray_sum([1]))                              # Output: 1

# Simple Breakdown
"""
Finds the maximum sum of a contiguous subarray.
- Uses Kadane’s algorithm to track the maximum sum ending at each position.
- Time Complexity: O(n), Space Complexity: O(1).
- Efficient and fundamental for subarray problems.
"""