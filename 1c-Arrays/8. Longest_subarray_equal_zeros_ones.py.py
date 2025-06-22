# Longest Subarray Equal Zeros Ones
"""
Task: Find the length of the longest subarray with an equal number of 0s and 1s.

Example 1: [0, 1] → 2
Example 2: [0, 1, 0] → 2

Why: Introduces hash map usage with cumulative sums for subarray properties.
"""

def longest_subarray_equal_zeros_ones(arr):
    # 1️⃣ Initialize dictionary with base case: sum 0 at index -1
    count = {0: -1}
    max_length = 0
    current_sum = 0
    
    # 2️⃣ Traverse array, treating 0 as -1 and 1 as +1
    for i, num in enumerate(arr):
        current_sum += 1 if num == 1 else -1  # Increment for 1, decrement for 0
        if current_sum in count:
            max_length = max(max_length, i - count[current_sum])  # Update length
        else:
            count[current_sum] = i  # Record first occurrence of this sum
    
    # 3️⃣ Return the maximum length found
    return max_length

print(longest_subarray_equal_zeros_ones([0, 1]))     # Output: 2
print(longest_subarray_equal_zeros_ones([0, 1, 0]))  # Output: 2


# Simple Breakdown
"""
Finds the longest subarray with equal 0s and 1s.
- Uses a hash map to track cumulative sums, where equal sums indicate balance.
- Time Complexity: O(n), Space Complexity: O(n) for the hash map.
- Combines array traversal with hash map usage effectively.
"""