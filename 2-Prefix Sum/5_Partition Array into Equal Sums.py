# 5. Partition Array into Equal Sums
"""
Task: Check if an array can be split into two non-empty contiguous parts with equal sums.
Example: [1, 5, 6] → True (1 + 5 = 6)
Why: Reinforces cumulative sum usage.
"""

def can_partition(arr):
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return False  # Odd sum can't be split evenly
    target = total_sum // 2
    prefix_sum = 0
    for num in arr:
        prefix_sum += num
        if prefix_sum == target:
            return True  # Found a split point
    return False

# Test the function
print(can_partition([1, 5, 6]))  # Output: True (1 + 5 = 6)


# Solution
def can_partition(arr):    # Define the function that takes an array 'arr' as input
    """
    Checks if the array can be split into two parts with equal sums.
    
    - Uses prefix sum to find a point where left sum equals remaining sum.
    - Time Complexity: O(n), Space Complexity: O(1).
    - Iterative check is straightforward and beginner-friendly.
    """
    total_sum = sum(arr)     # Calculate the total sum of the array
    if total_sum % 2 != 0:   # If total sum is odd
        return False         # Cannot split into two equal integer sums
    target = total_sum // 2  # Each part should sum to half of total_sum
    prefix_sum = 0      # Initialize prefix sum to zero
    for num in arr:     # Iterate through each element in 'arr'
        prefix_sum += num  # Add the current number to the prefix sum
        if prefix_sum == target:  # If prefix sum equals the target
            return True   # A split point is found
    return False          # No split point found

# Test the function
# print(can_partition([1, 5, 6]))  # Output: True (1 + 5 = 6)


# ----------------------------------------------------------------------------------
# Solution with output

def can_partition(arr):
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return False  
    target = total_sum // 2
    prefix_sum = 0
    for num in arr:
        prefix_sum += num
        if prefix_sum == target:
            return True  
    return False

# Test the function
print(can_partition([1, 5, 6]))  # Output: True (1 + 5 = 6)
